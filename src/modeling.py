import time
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SequentialFeatureSelector, SelectKBest, f_classif
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import confusion_matrix, roc_curve, accuracy_score
from datetime import datetime
from google import genai
from config import GEMINI_API_KEY
from audit import generate_variable_audit_table

def calculate_smoothed_weights(y_data, smoothing='log'):
    class_counts = Counter(y_data)
    majority_count = max(class_counts.values())
    
    weights = {}
    for cls, count in class_counts.items():
        ratio = majority_count / count
        if smoothing == 'sqrt':
            weights[cls] = round(float(np.sqrt(ratio)), 2)
        elif smoothing == 'log':
            weights[cls] = round(float(np.log10(ratio) + 1.0), 2)
        else:
            weights[cls] = round(float(ratio), 2)
    return weights

def get_llm_interpretation(coeff_df_string, target_etf, horizon_days, max_retries=3, delay=10):
    if not GEMINI_API_KEY or GEMINI_API_KEY == "DEIN_API_KEY_HIER":
        return "> *Kein API-Key hinterlegt. LLM-Analyse uebersprungen.*"
    
    # Berechne grob die Monate fuer den Prompt (21 Handelstage = 1 Monat)
    horizon_months = max(1, horizon_days // 21)
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # Setze die dynamische Variable in den Prompt ein
    prompt = f"""
    Du bist ein quantitativer Macro-Analyst eines Hedgefonds. Mein Modell zur Vorhersage 
    des Marktzustandes (Up, Down, Flat) fuer den {target_etf} (Horizont: {horizon_months} Monate) hat 
    basierend auf einer Schrittweisen Variablenselektion folgende Praediktoren ausgewaehlt 
    und gewichtet (Kuerzel am Ende zeigen das Momentum-Fenster, z.B. _6M):
    
    {coeff_df_string}
    
    Liefere eine hochgradig elaborierte, aber extrem praezise oekonomische Einschaetzung, 
    warum dieses spezifische Set an Indikatoren aktuell vorlaufend wirkt. 
    
    Regeln fuer die Ausgabe:
    - Absolutes Verbot von Fliesstexten und Geschwafel. 
    - Antworte ausschliesslich in knackigen Spiegelstrichen.
    - Nutze harte, institutionelle Logik (Korrelationen, Zinsstruktur, Sektor-Rotationen).
    
    Strukturiere deine Antwort zwingend in diese drei kurzen Bloecke:
    **1. Makrooekonomisches Setup:** (Warum wurden Zinsen/Waehrungen/Rohstoffe gewaehlt oder ignoriert?)
    **2. Sektor- & Marktdynamik:** (Was verraten die ausgewaehlten Equities/Sektoren ueber den Konjunkturzyklus?)
    **3. Quant-Konklusion:** (Was ist das uebergeordnete Narrativ fuer den {target_etf} in den naechsten {horizon_months} Monaten?)
    """
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text
        except Exception as e:
            error_msg = str(e).upper()
            if any(err in error_msg for err in ["429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE"]):
                if attempt < max_retries - 1:
                    print(f"Google Server-Spike (503/429). Versuch {attempt+1}/{max_retries} fehlgeschlagen. Warte {delay} Sekunden...")
                    time.sleep(delay)
                    continue
            return f"> *Fehler bei der LLM-Abfrage: {e}*"

def apply_ks_logic(preds, probs, classes, cutoff):
    """
    Wendet den optimierten KS-Cutoff rueckwirkend auf historische Vorhersagen an.
    """
    adjusted_preds = preds.copy()
    if -1 not in classes: return adjusted_preds
    down_idx = list(classes).index(-1)
    
    for i in range(len(adjusted_preds)):
        p_down = probs[i, down_idx]
        if p_down >= cutoff:
            adjusted_preds[i] = -1
        elif adjusted_preds[i] == -1 and p_down < cutoff:
            sub_probs = probs[i].copy()
            sub_probs[down_idx] = -1.0 
            adjusted_preds[i] = classes[np.argmax(sub_probs)]
    return adjusted_preds

def perform_feature_selection(X_scaled, y, latest_features_scaled, target_etf, horizon, final_features=12, pre_filter_k=80, timestamp=None):
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: Fuehre Feature Selection durch (Pre-Filter: Top {pre_filter_k} Variablen)...")
    
    # Klassengewichtung auskommentiert
    # custom_weights = calculate_smoothed_weights(y, smoothing='log')
    # print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: Dynamische Algorithmus-Gewichtung (Log-Smoothed): {custom_weights}")
    custom_weights = None
    
    k_actual = min(pre_filter_k, X_scaled.shape[1])
    kbest = SelectKBest(score_func=f_classif, k=k_actual)
    
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: Starting SelectKBest (ANOVA)...")
    kbest.fit(X_scaled, y)
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: SelectKBest complete.")
    
    features_stage_1 = X_scaled.columns[kbest.get_support()]
    rejected_stage_1 = X_scaled.columns[~kbest.get_support()]
    X_stage_1 = X_scaled[features_stage_1]
    
    initial_train_size = 252 * 3 
    if initial_train_size >= len(X_stage_1):
        initial_train_size = len(X_stage_1) // 2
        
    test_size = (len(X_stage_1) - initial_train_size - (5 * horizon)) // 5
    if test_size < 1:
        test_size = 1

    tscv = TimeSeriesSplit(n_splits=5, gap=horizon, max_train_size=None, test_size=test_size)
    
    log_reg_base = LogisticRegression(solver='lbfgs', max_iter=200, class_weight=custom_weights)
    
    sfs = SequentialFeatureSelector(log_reg_base, n_features_to_select=final_features, direction='forward', cv=tscv, n_jobs=-1)
    
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: Starting SequentialFeatureSelector (SFS). Dies kann einige Minuten dauern...")
    sfs.fit(X_stage_1, y)
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: SFS complete.")
    
    selected_features = features_stage_1[sfs.get_support()]
    rejected_stage_2 = features_stage_1[~sfs.get_support()]
    X_optimal = X_scaled[selected_features]
    
    model = LogisticRegression(solver='lbfgs', max_iter=1000, class_weight=custom_weights)
    
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: Fitting final Logistic Regression...")
    model.fit(X_optimal, y)
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: Final fit complete. Starting OOF Evaluation...")

    # 1. Out-of-Fold (OOF) Evaluierung
    oof_preds = np.full(len(y), np.nan)
    oof_probs = np.full((len(y), len(model.classes_)), np.nan)
    
    for train_idx, test_idx in tscv.split(X_optimal):
        X_train, y_train = X_optimal.iloc[train_idx], y.iloc[train_idx]
        X_test = X_optimal.iloc[test_idx]
        
        fold_model = LogisticRegression(solver='lbfgs', max_iter=1000, class_weight=custom_weights)
        fold_model.fit(X_train, y_train)
        
        oof_preds[test_idx] = fold_model.predict(X_test)
        oof_probs[test_idx] = fold_model.predict_proba(X_test)
        
    valid_indices = ~np.isnan(oof_preds)
    y_valid = y.iloc[valid_indices]
    oof_preds_valid = oof_preds[valid_indices]
    oof_probs_valid = oof_probs[valid_indices]
    
    print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: OOF Evaluation complete.")

    # 2. KS-Statistik (Cutoff Optimierung fuer Klasse -1)
    y_down_true = (y_valid == -1).astype(int)
    optimal_down_threshold = 0.33 
    
    if -1 in model.classes_:
        down_idx = list(model.classes_).index(-1)
        y_down_prob = oof_probs_valid[:, down_idx]
        
        fpr, tpr, thresholds = roc_curve(y_down_true, y_down_prob)
        ks_stats = tpr - fpr
        max_ks_idx = np.argmax(ks_stats)
        optimal_down_threshold = thresholds[max_ks_idx]
        print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: KS-Statistik optimiert: Cutoff fuer -1 liegt bei {optimal_down_threshold:.2%}")

    # 3. Synchronisation der Matrizen mit dem KS-Cutoff
    oof_preds_ks = apply_ks_logic(oof_preds_valid, oof_probs_valid, model.classes_, optimal_down_threshold)
    
    train_probs = model.predict_proba(X_optimal)
    train_preds = model.predict(X_optimal)
    train_preds_ks = apply_ks_logic(train_preds, train_probs, model.classes_, optimal_down_threshold)

    # 4. Quality Gate (basierend auf den realen, KS-optimierten Vorhersagen)
    cv_accuracy = accuracy_score(y_valid, oof_preds_ks)
    is_valid_quality = cv_accuracy >= 0.35

    def plot_advanced_cm(y_true, y_pred, classes, title, accuracy):
        cm = confusion_matrix(y_true, y_pred, labels=classes)
        row_sums = cm.sum(axis=1)[:, np.newaxis]
        cm_perc = np.divide(cm.astype('float'), row_sums, out=np.zeros_like(cm, dtype=float), where=row_sums!=0)
        
        labels = [f"{v1}\n({v2:.1%})" for v1, v2 in zip(cm.flatten(), cm_perc.flatten())]
        labels = np.asarray(labels).reshape(cm.shape)
        
        fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
        sns.heatmap(cm, annot=labels, fmt='', cmap='Blues', 
                    xticklabels=classes, yticklabels=classes, ax=ax, cbar=False,
                    annot_kws={"size": 11, "weight": "bold"})
        
        ax.set_ylabel('Tatsaechlicher Markt (True)', fontsize=12, fontweight='bold', labelpad=10)
        ax.set_xlabel('Modell-Prognose (Predicted)', fontsize=12, fontweight='bold', labelpad=10)
        ax.set_title(f"{title}\nAccuracy: {accuracy:.2%}", fontsize=14, fontweight='bold', pad=15)
        
        plt.xticks(fontsize=11)
        plt.yticks(fontsize=11, rotation=0)
        fig.patch.set_alpha(0.0) 
        plt.tight_layout()
        plt.close(fig)
        return fig

    train_accuracy = accuracy_score(y, train_preds_ks)
    fig_cm_train = plot_advanced_cm(y, train_preds_ks, model.classes_, "1. In-Sample (Training)", train_accuracy)
    fig_cm_cv = plot_advanced_cm(y_valid, oof_preds_ks, model.classes_, "2. Out-of-Sample (Cross-Validation)", cv_accuracy)

    # 5. Live Predict Logik
    X_latest_optimal = latest_features_scaled[selected_features]
    probabilities = model.predict_proba(X_latest_optimal)[0]
    
    prob_dict = dict(zip(model.classes_, probabilities))
    prob_down = prob_dict.get(-1, 0)
    
    if prob_down >= optimal_down_threshold:
        prediction = -1
    else:
        prediction = model.predict(X_latest_optimal)[0]
        if prediction == -1 and prob_down < optimal_down_threshold:
            sub_probs = {k: v for k, v in prob_dict.items() if k != -1}
            prediction = max(sub_probs, key=sub_probs.get)

    class_mapping = {-1: "Down", 0: "Flat", 1: "Up"}
    pred_label = class_mapping.get(prediction, "Unknown")
    
    predict_date = latest_features_scaled.index[0]
    predict_date_str = predict_date.strftime('%Y-%m-%d') if isinstance(predict_date, pd.Timestamp) else str(predict_date)
    
    prob_flat = prob_dict.get(0, 0)
    prob_up = prob_dict.get(1, 0)

    print("\n" + "="*35)
    print("=== Aktuelle Modell-Prognose ===")
    print("="*35)
    print(f"Datum: {predict_date_str}")
    print(f"Vorhersage: {pred_label}")
    print(f"Wahrscheinlichkeiten: Down={prob_down:.2%}, Flat={prob_flat:.2%}, Up={prob_up:.2%}\n")

    # WICHTIG: Berechnung der Feature-Gewichte fuer den Export
    importance = np.mean(np.abs(model.coef_), axis=0)
    feature_names = selected_features.tolist()
    feature_weights = {feat: float(weight) for feat, weight in zip(feature_names, importance)}
    
    coeff_df = pd.DataFrame({
        'Praediktor': selected_features,
        'Einfluss (Mean Absolut)': importance
    }).sort_values(by='Einfluss (Mean Absolut)', ascending=False)
    
    if timestamp:
        print(f"    [{datetime.now().strftime('%H:%M:%S')}] MODELING: Hole oekonomische Interpretation vom LLM...")
        llm_analysis = get_llm_interpretation(coeff_df.to_string(index=False), target_etf, horizon)
        
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
            
            f.write("## Ausgewaehlte Praediktoren (SFS)\n\n")
            f.write("| Praediktor | Einfluss (Mean Absolut) |\n")
            f.write("| :--- | :--- |\n")
            for _, row in coeff_df.iterrows():
                f.write(f"| {row['Praediktor']} | {row['Einfluss (Mean Absolut)']:.6f} |\n")
            f.write("\n")
            
            f.write("## Aussortierte Praediktoren\n\n")
            f.write("### 1. In der Endauswahl verworfen (SFS Rejects)\n")
            f.write(f"`{', '.join(rejected_stage_2.tolist())}`\n\n")
            
            f.write("### 2. Im Basisfilter verworfen (ANOVA Rejects)\n")
            f.write(f"<details>\n<summary>Klicken, um alle <b>{len(rejected_stage_1)}</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>\n\n")
            f.write(f"`{', '.join(rejected_stage_1.tolist())}`\n")
            f.write("\n</details>\n\n")
            f.write("---\n\n")
            
            f.write("## KI-Interpretation der Praediktoren (Hedgefonds Analyst)\n\n")
            f.write(llm_analysis + "\n\n")
            
            f.write("## Mathematische Modellparameter\n\n")
            f.write(f"- **Intercepts:** `{model.intercept_.tolist()}`\n\n")
            f.write("- **Koeffizienten-Matrix:**\n")
            f.write("  ```text\n")
            f.write(str(model.coef_))
            f.write("\n  ```\n")
            
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
            print(f"Fehler bei Audit-Generierung: {e}")
            
    return {
        "model": model,
        "X_optimal": X_optimal,
        "prediction": prediction,
        "probabilities": prob_dict,
        "cm_fig_train": fig_cm_train,
        "cm_fig_cv": fig_cm_cv,
        "cv_accuracy": cv_accuracy,
        "is_valid_quality": is_valid_quality,
        "ks_cutoff": optimal_down_threshold,
        "selected_features": feature_names,
        "feature_weights": feature_weights
    }