# scripts/generate_seed.py

import pandas as pd
import os

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Der Pfad zu deiner offiziellen Xetra-Datei
    csv_path = os.path.join(project_root, 'config', 't7-xetr-allTradableInstruments.csv')
    output_path = os.path.join(project_root, 'config', 'all_etfs_seed.txt')

    if not os.path.exists(csv_path):
        print(f"Fehler: Bitte speichere den Xetra-Dump unter:\n{csv_path}")
        return

    print("Lese offizielle Xetra-Instrumente (T7) ein...")
    
    # skiprows=2 ignoriert die ersten beiden Metadaten-Zeilen der Deutschen Börse
    # sep=';' da die Börse Semikolons verwendet
    try:
        df = pd.read_csv(csv_path, sep=';', skiprows=2, low_memory=False)
    except Exception as e:
        print(f"Fehler beim Lesen der CSV: {e}")
        return

    # 1. Nur ETFs und ETCs (Exchange Traded Commodities wie Xetra-Gold) filtern
    if 'Instrument Type' not in df.columns or 'Mnemonic' not in df.columns:
        print("Fehler: Die erwarteten Spalten 'Instrument Type' oder 'Mnemonic' fehlen.")
        return

    etf_df = df[df['Instrument Type'].isin(['ETF', 'ETC'])].copy()
    
    # 2. Währung filtern (Optional, aber empfohlen für den deutschen Privatanleger)
    # Wir behalten nur die Instrumente, die auch in Euro (EUR) notieren
    if 'Currency' in etf_df.columns:
        etf_df = etf_df[etf_df['Currency'] == 'EUR']
    
    # 3. Ticker für Yahoo Finance bauen (.DE für Xetra anhängen)
    # Aus 'SXR8' wird 'SXR8.DE'
    yahoo_tickers = etf_df['Mnemonic'].astype(str).str.strip().str.upper() + ".DE"
    
    # 4. Duplikate entfernen (zur Sicherheit)
    unique_tickers = sorted(list(set(yahoo_tickers.tolist())))

    # In die Textdatei für deine Pipeline schreiben
    with open(output_path, 'w') as f:
        for ticker in unique_tickers:
            f.write(f"{ticker}\n")

    print("\n" + "="*50)
    print(f"Erfolg! {len(unique_tickers)} handelbare Xetra-ETFs/ETCs extrahiert.")
    print(f"Seed-Universum gespeichert unter: {output_path}")
    print("="*50)
    print("Du kannst nun 'python scripts/build_etf_batch.py' ausführen, um die Liste nach Alter/Liquidität zu filtern.")

if __name__ == "__main__":
    main()