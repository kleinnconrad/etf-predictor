# src/modeling.py

import time
import pandas as pd
import numpy as np
import os
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SequentialFeatureSelector, SelectKBest, f_classif
from sklearn.model_selection import TimeSeriesSplit
from google import genai
from config import GEMINI_API_KEY
from audit import generate_variable_audit_table

def calculate_smoothed_weights(y_data, smoothing='log'):
    """
    Algorithmically estimates custom class weights to combat base rate bias 
    without causing algorithmic paranoia.
    """
    class_counts = Counter(y_data)
    majority_count = max(class_counts.values())
    
    weights = {}
    for cls, count in class_counts.items():
        ratio = majority_count / count
        
        if smoothing == 'sqrt':
            weights[cls] = round(float(np.sqrt(ratio)), 2)
        elif smoothing == 'log':
            weights[cls] = round(float(np.log10(ratio) + 1.0), 2)
        else: # 'strict'
            weights[cls] = round(float(ratio), 2)
            
    return weights

def get_llm_interpretation(coeff_df_string, target_etf, max_retries=3, delay=10):
    if not GEMINI_API_KEY or GEMINI_API_KEY == "DEIN_API_KEY_HIER":
        return "> *Kein API-Key hinterlegt. LLM-Analyse übersprungen.*"
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = f"""
    Du bist ein quantitativer Macro-Analyst eines Hedgefonds. Mein Modell zur Vorhersage 
    des Marktzustandes (Up, Down, Flat) für den {target_etf} (Horizont: 6 Monate) hat 
    basierend auf einer Schrittweisen Variablenselektion folgende Prädiktoren ausgewählt 
    und gewichtet (Kürzel am Ende zeigen das Momentum-Fenster, z.B. _6M):
    
    {coeff_df_string}
    
    Liefere eine hochgradig elaborierte, aber extrem präzise ökonomische Einschätzung, 
    warum dieses spezifische Set an Indikatoren aktuell vorlaufend wirkt. 
    
    Regeln für die Ausgabe:
    - Absolutes Verbot von Fließtexten und Geschwafel. 
    - Antworte ausschließlich in knackigen Spiegelstrichen.
    - Nutze harte, institutionelle Logik (Korrelationen, Zinsstruktur, Sektor-Rotationen).
    
    Strukturiere deine Antwort zwingend in diese drei kurzen Blöcke:
    **1. Makroökonomisches Setup:** (Warum wurden Zinsen/Währungen/Rohstoffe gewählt oder ignoriert?)
    **2. Sektor- & Marktdynamik:** (Was verraten die ausgewählten Equities/Sektoren über den Konjunkturzyklus?)
    **3. Quant-Konklusion:** (Was ist das übergeordnete Narrativ für den {target_etf} in den nächsten 6 Monaten?)
    """
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text
        except Exception as e:
            # Wir machen die Fehlermeldung sicherheitshalber groß (UPPERCASE), um Treffer zu garantieren
            error_msg = str(e).upper()
            
            # --- DER FIX: Die Logik fängt jetzt auch die 503 UNAVAILABLE Spikes ab ---
            if any(err in error_msg for err in ["429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE"]):
                if attempt < max_retries - 1:
                    print(f"Google Server-Spike (503/429). Versuch {attempt+1}/{max_retries} fehlgeschlagen. Warte {delay} Sekunden...")
                    time.sleep(delay)
                    continue
            return f"> *Fehler bei der LLM-Abfrage: {e}*"

def perform_feature_selection(X_scaled, y, latest_features_scaled, target_etf, horizon, final_features=8, pre_filter_k=80, timestamp=None):
    print(f"Führe Feature Selection durch (Pre-Filter: Top {pre_filter_k} Variablen)...")
    
    # --- DYNAMIC BALANCING (Logarithmic Smoothing) ---
    custom_weights = calculate_smoothed_weights(y, smoothing='log')
    print(f"Dynamische Algorithmus-Gewichtung (Log-Smoothed): {custom_weights}")
    
    # Stufe 1: Univariater Filter
    k_actual = min(pre_filter_k, X_scaled.shape[1])
    kbest = SelectKBest(score_func=f_classif, k=k_actual)
    kbest.fit(X_scaled, y)
    
    features_stage_1 = X_scaled.columns[kbest.get_support()]
    rejected_stage_1 = X_scaled.columns[~kbest.get_support()]
    X_stage_1 = X_scaled[features_stage_1]
    
    # --- Robuster TimeSeriesSplit ---
    initial_train_size = 252 * 3 
    
    if initial_train_size >= len(X_stage_1):
        initial_train_size = len(X_stage_1) // 2
        
    test_size = (len(X_stage_1) - initial_train_size - (5 * horizon)) // 5
    if test_size < 1:
        test_size = 1

    tscv = TimeSeriesSplit(
        n_splits=5, 
        gap=horizon,
        max_train_size=None,
        test_size=test_size
    )
    
    # Stufe 2: Wrapper Methode mit dynamischen Custom Weights
    log_reg_base = LogisticRegression(solver='lbfgs', max_iter=1000, class_weight=custom_weights)
    sfs = SequentialFeatureSelector(
        log_reg_base, 
        n_features_to_select=final_features, 
        direction='forward', 
        cv=tscv, 
        n_jobs=-1
    )
    sfs.fit(X_stage_1, y)
    
    selected_features = features_stage_1[sfs.get_support()]
    rejected_stage_2 = features_stage_1[~sfs.get_support()]
    X_optimal = X_scaled[selected_features]
    
    # Finales Modell trainieren (ebenfalls mit dynamischen Weights)
    model = LogisticRegression(solver='lbfgs', max_iter=1000, class_weight=custom_weights)
    model.fit(X_optimal, y)

    # --- PREDICT LOGIK (Für den aktuellen Tag) ---
    X_latest_optimal = latest_features_scaled[selected_features]
    prediction = model.predict(X_latest_optimal)[0]
    probabilities = model.predict_proba(X_latest_optimal)[0]
    
    prob_dict = dict(zip(model.classes_, probabilities))
    prob_down = prob_dict.get(-1, 0)
    prob_flat = prob_dict.get(0, 0)
    prob_up = prob_dict.get(1, 0)
    
    class_mapping = {-1: "Down 🔴", 0: "Flat 🟡", 1: "Up 🟢"}
    pred_label = class_mapping.get(prediction, "Unknown")
    
    predict_date = latest_features_scaled.index[0]
    if isinstance(predict_date, pd.Timestamp):
        predict_date_str = predict_date.strftime('%Y-%m-%d')
    else:
        predict_date_str = str(predict_date)
    
    print("\n" + "="*35)
    print("=== Aktuelle Modell-Prognose ===")
    print("="*35)
    print(f"Datum: {predict_date_str}")
    print(f"Vorhersage: {pred_label}")
    print(f"Wahrscheinlichkeiten: Down={prob_down:.2%}, Flat={prob_flat:.2%}, Up={prob_up:.2%}\n")

    # Wichtigkeit der Variablen berechnen
    importance = np.mean(np.abs(model.coef_), axis=0)
    coeff_df = pd.DataFrame({
        'Prädiktor': selected_features,
        'Einfluss (Mean Absolut)': importance
    }).sort_values(by='Einfluss (Mean Absolut)', ascending=False)
    
    table_string = coeff_df.to_string(index=False)
    
    # Artefakte und LLM-Report generieren
    if timestamp:
        print("Hole ökonomische Interpretation vom LLM...")
        llm_analysis = get_llm_interpretation(table_string, target_etf)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '..'))
        output_dir = os.path.join(project_root, 'output')
        os.makedirs(output_dir, exist_ok=True)
        
        md_path = os.path.join(output_dir, f"feature_selection_{timestamp}.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write("# ETF Predictor Pipeline-Report\n\n")
            f.write(f"- **Generiert am:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"- **Target ETF:** {target_etf}\n")
            f.write(f"- **Forecast Horizon:** {horizon} Trading Days\n\n")
            
            f.write("## Aktuelle Marktprognose (Predict)\n\n")
            f.write(f"Basierend auf den Schlusskursen vom **{predict_date_str}** prognostiziert das Modell:\n\n")
            f.write(f"> **Klasse:** {pred_label}\n>\n")
            f.write(f"> **Wahrscheinlichkeiten:** Down: {prob_down:.2%} | Flat: {prob_flat:.2%} | Up: {prob_up:.2%}\n\n")
            f.write("---\n\n")
            
            f.write("## Ausgewählte Prädiktoren (SFS)\n\n")
            f.write("| Prädiktor | Einfluss (Mean Absolut) |\n")
            f.write("| :--- | :--- |\n")
            for _, row in coeff_df.iterrows():
                f.write(f"| {row['Prädiktor']} | {row['Einfluss (Mean Absolut)']:.6f} |\n")
            f.write("\n")
            
            f.write("## Aussortierte Prädiktoren\n\n")
            f.write("### 1. In der Endauswahl verworfen (SFS Rejects)\n")
            f.write("> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* \n\n")
            f.write(f"`{', '.join(rejected_stage_2.tolist())}`\n\n")
            
            f.write("### 2. Im Basisfilter verworfen (ANOVA Rejects)\n")
            f.write(f"<details>\n<summary>Klicken, um alle <b>{len(rejected_stage_1)}</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>\n\n")
            f.write(f"`{', '.join(rejected_stage_1.tolist())}`\n")
            f.write("\n</details>\n\n")
            f.write("---\n\n")
            
            f.write("## KI-Interpretation der Prädiktoren (Hedgefonds Analyst)\n\n")
            f.write(llm_analysis + "\n\n")
            
            f.write("## Mathematische Modellparameter\n\n")
            f.write(f"- **Intercepts:** `{model.intercept_.tolist()}`\n\n")
            f.write("- **Koeffizienten-Matrix:**\n")
            f.write("  ```text\n")
            f.write(str(model.coef_))
            f.write("\n  ```\n")
            
        print(f"Ergebnisse gespeichert unter: {md_path}")
        
        # === TRIGGER FÜR DAS VARIABLEN-AUDIT ===
        try:
            generate_variable_audit_table(
                X_columns=X_scaled.columns, 
                p_values=kbest.pvalues_, 
                selected_features=selected_features, 
                rejected_stage_2=rejected_stage_2, 
                model_coefs=model.coef_,
                timestamp=timestamp
            )
        except Exception as e:
            print(f"Fehler bei der Generierung des Variablen-Audits: {e}")
        # =======================================
        
    return model, X_optimal
    
