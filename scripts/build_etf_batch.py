# scripts/build_etf_batch.py

import yfinance as yf
import pandas as pd
import json
import os
import time
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

# 1. Kalibrierte Metriken für Europa
MIN_YEARS_HISTORY = 10  # 10 Jahre
MIN_AVG_DAILY_TURNOVER_EUR = 1000000  # 1 Million Euro täglicher Handelsumsatz

def check_etf_eligibility(ticker):
    """Prüft, ob der ETF alt genug und liquide genug (in EUR Umsatz) ist."""
    # Wir geben yfinance bis zu 3 Versuche (falls die API kurzzeitig blockt)
    for attempt in range(3):
        try:
            etf = yf.Ticker(ticker)
            hist = etf.history(period="max")
            
            if hist.empty:
                time.sleep(1) # Kurz warten vor dem nächsten Versuch
                continue

            # 1. Check: Alter des ETFs
            first_date = hist.index[0].tz_localize(None)
            cutoff_date = datetime.now() - timedelta(days=365 * MIN_YEARS_HISTORY)
            
            if first_date > cutoff_date:
                return ticker, False, f"Zu jung (Start: {first_date.strftime('%Y-%m')})"

            # 2. Check: Echte Liquidität (Umsatz in Euro, nicht nur Stückzahl)
            recent_data = hist.tail(60)
            # Umsatz = Gehandelte Stücke * Schlusskurs
            avg_turnover = (recent_data['Volume'] * recent_data['Close']).mean()
            
            if avg_turnover < MIN_AVG_DAILY_TURNOVER_EUR:
                return ticker, False, f"Zu illiquide (Umsatz: {avg_turnover/1000000:.1f} Mio. €)"

            return ticker, True, "Bestanden"
            
        except Exception as e:
            time.sleep(1)
            continue
            
    return ticker, False, "API Timeout oder kein Handel auf Xetra"

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    seed_file_path = os.path.join(project_root, 'config', 'all_etfs_seed.txt')
    
    if not os.path.exists(seed_file_path):
        print(f"Fehler: Seed-Datei nicht gefunden unter {seed_file_path}")
        return

    with open(seed_file_path, 'r') as f:
        all_tickers = [line.strip() for line in f if line.strip()]
        
    print("\n" + "="*60)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] STARTE KALIBRIERTES XETRA-SCREENING")
    print(f"Bedingungen: > {MIN_YEARS_HISTORY} Jahre Historie UND > 1 Mio. € Tagesumsatz")
    print(f"Prüfe {len(all_tickers)} Ticker (Rate-Limited, max 10 Threads)...")
    print("="*60 + "\n")
    
    valid_etfs = []
    
    # Auf 10 Threads gedrosselt, um Yahoo Finance nicht zu verärgern
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_etf_eligibility, ticker): ticker for ticker in all_tickers}
        
        for idx, future in enumerate(as_completed(futures), 1):
            ticker, is_valid, reason = future.result()
            
            if is_valid:
                valid_etfs.append(ticker)
                print(f"[{idx:04d}/{len(all_tickers)}] [OK] {ticker} (Target erreicht!)")
            else:
                print(f"[{idx:04d}/{len(all_tickers)}] [REJECTED] {ticker} - {reason}")

    valid_etfs.sort()

    print("\n" + "="*60)
    print(f"SELEKTION ABGESCHLOSSEN!")
    print(f"{len(valid_etfs)} hochliquide, bewährte ETFs stehen für das Modell bereit.")
    print("="*60)
    
    output_dir = os.path.join(project_root, 'config')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'batch_targets.json')
    
    with open(output_path, 'w') as f:
        json.dump({
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_count": len(valid_etfs),
            "tickers": valid_etfs
        }, f, indent=4)
        
    print(f"Batch-Ziele gespeichert unter: {output_path}")

if __name__ == "__main__":
    main()