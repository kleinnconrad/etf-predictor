# src/audit.py

import os
import json
import time
import pandas as pd
import numpy as np
from google import genai
from config import GEMINI_API_KEY

def fetch_ticker_metadata(base_tickers, max_retries=3, delay=60):
    """
    Nutzt die Gemini API, um Klarnamen und ökonomische Beschreibungen 
    für eine Liste von Basis-Tickern als JSON zu generieren.
    """
    if not GEMINI_API_KEY or GEMINI_API_KEY == "DEIN_API_KEY_HIER":
        print("Kein API-Key für das Audit-Skript gefunden.")
        return {}

    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # Die Liste als String für den Prompt formatieren
    tickers_str = ", ".join(base_tickers)
    
    prompt = f"""
    Du bist ein Finanzdaten-Analyst. Ich gebe dir eine Liste von Börsentickern. 
    Liefere mir für jeden Ticker exakt ein JSON-Objekt zurück.
    
    Ticker-Liste: [{tickers_str}]
    
    Regeln für das JSON:
    Der Key muss der exakte Ticker sein. 
    Der Value ist ein Objekt mit 'name' (Klarname des Assets/Indikators) und 'desc' (1 prägnanter Satz, was es ökonomisch im Kontext einer Marktprognose misst).
    
    Beispielstruktur:
    {{
        "^TNX": {{"name": "US 10-Year Treasury Yield", "desc": "Misst die Rendite 10-jähriger US-Staatsanleihen; ein zentraler Indikator für langfristige Zins- und Inflationserwartungen."}},
        "AAPL": {{"name": "Apple Inc.", "desc": "Größtes Technologieunternehmen der Welt; repräsentiert die Stärke des breiten US-Konsum- und Techsektors."}}
    }}
    
    WICHTIG: Antworte AUSSCHLIESSLICH mit dem reinen JSON-Code. Keine Markdown-Blöcke (wie ```json), keine Einleitungen, kein Fließtext.
    """
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            
            # Bereinigung des Outputs (falls die KI doch Markdown-Ticks mitsendet)
            raw_text = response.text.strip()
            if raw_text.startswith("```json"):
                raw_text = raw_text[7:]
            if raw_text.startswith("```"):
                raw_text = raw_text[3:]
            if raw_text.endswith("```"):
                raw_text = raw_text[:-3]
                
            metadata = json.loads(raw_text.strip())
            return metadata
            
        except json.JSONDecodeError as e:
            print(f"JSON Parsing Fehler beim Audit (Versuch {attempt+1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
                continue
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                if attempt < max_retries - 1:
                    print(f"API Rate Limit beim Audit. Warte {delay}s...")
                    time.sleep(delay)
                    continue
            print(f"API Fehler beim Audit: {e}")
            return {}
            
    return {}

def generate_variable_audit_table(X_columns, p_values, selected_features, rejected_stage_2, model_coefs, timestamp):
    """
    Kompiliert alle statistischen Metriken und LLM-Beschreibungen zu einer Markdown-Tabelle.
    """
    print("Starte tiefgreifendes Variablen-Audit (LLM-Abfrage läuft)...")
    
    # 1. Datenstruktur aufbauen
    audit_data = []
    
    # Mean Absolute der Koeffizienten für die finalen Features (Einfluss)
    importance = np.mean(np.abs(model_coefs), axis=0)
    coef_dict = dict(zip(selected_features, importance))
    
    for i, col in enumerate(X_columns):
        # Basis-Ticker extrahieren (z.B. aus 'AAPL_6M' wird 'AAPL')
        base_ticker = col.rsplit('_', 1)[0]
        p_val = p_values[i]
        
        # Status und Einfluss zuweisen
        if col in selected_features:
            status = "🟢 Aktiv (Gewählt)"
            einfluss = f"{coef_dict[col]:.4f}"
        elif col in rejected_stage_2:
            status = "🟡 Verworfen (Multikollinearität)"
            einfluss = "-"
        else:
            status = "🔴 Verworfen (Keine Signifikanz)"
            einfluss = "-"
            
        audit_data.append({
            "Variable": col,
            "Base_Ticker": base_ticker,
            "Status": status,
            "p_Wert": p_val,
            "Einfluss": einfluss
        })
        
    df_audit = pd.DataFrame(audit_data)
    
    # 2. Metadaten über Gemini API abrufen (Nur einzigartige Ticker anfragen)
    unique_tickers = df_audit['Base_Ticker'].unique().tolist()
    metadata = fetch_ticker_metadata(unique_tickers)
    
    # 3. LLM-Daten mit der Statistik matchen
    df_audit['Klarname'] = df_audit['Base_Ticker'].apply(lambda x: metadata.get(x, {}).get('name', 'Unbekannt'))
    df_audit['Beschreibung'] = df_audit['Base_Ticker'].apply(lambda x: metadata.get(x, {}).get('desc', 'Keine Beschreibung verfügbar.'))
    
    # 4. Tabelle sortieren (Aktive Features zuerst, dann nach p-Wert)
    # Eigene Sortierlogik über eine Hilfsspalte
    status_order = {"🟢 Aktiv (Gewählt)": 0, "🟡 Verworfen (Multikollinearität)": 1, "🔴 Verworfen (Keine Signifikanz)": 2}
    df_audit['Sort'] = df_audit['Status'].map(status_order)
    df_audit = df_audit.sort_values(by=['Sort', 'p_Wert']).drop(columns=['Sort', 'Base_Ticker'])
    
    # p-Werte schön formatieren (Wissenschaftliche Notation für sehr kleine Zahlen)
    df_audit['p_Wert'] = df_audit['p_Wert'].apply(lambda x: f"{x:.2e}" if x < 0.001 else f"{x:.4f}")
    
    # 5. Markdown-Tabelle exportieren
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..'))
    output_dir = os.path.join(project_root, 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    md_path = os.path.join(output_dir, f"variable_audit_{timestamp}.md")
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Variablen-Audit (Feature Encyclopedia)\n\n")
        f.write(f"**Generiert am:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("> Dieses Dokument protokolliert alle Variablen der Pipeline. Es erklärt transparent, "
                "welche Variablen aktiv Vorhersagen treffen, welche aufgrund redundanter Informationen (Multikollinearität) "
                "vom Algorithmus ignoriert wurden, und welche Variablen keine statistische Relevanz (ANOVA F-Test) aufwiesen.\n\n")
        
        f.write("| Variable | Klarname | Status | p-Wert (ANOVA) | Einfluss (Modell) | Ökonomische Beschreibung |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
        
        for _, row in df_audit.iterrows():
            f.write(f"| **{row['Variable']}** | {row['Klarname']} | {row['Status']} | {row['p_Wert']} | {row['Einfluss']} | {row['Beschreibung']} |\n")
            
    print(f"Variablen-Audit erfolgreich gespeichert unter: {md_path}")