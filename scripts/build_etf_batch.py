# scripts/build_etf_batch.py

import yfinance as yf
import pandas as pd
import json
import os
from datetime import datetime, timedelta

# 1. Das Seed-Universum (LLM generiert)
SEED_UNIVERSE = {
    "US_Broad": ["SPY", "QQQ", "DIA", "IWM", "VOO", "VTI"],
    "Sectors": ["XLF", "XLK", "XLE", "XLV", "XLY", "XLP", "XLU", "XLI", "XLB", "XRE", "XLC", "SMH", "XBI", "KRE"],
    "International": ["EFA", "EEM", "VGK", "EZU", "EWJ", "MCHI", "INDA", "EWZ", "EWT", "EWY"],
    "Fixed_Income": ["TLT", "IEF", "SHY", "LQD", "HYG", "BND", "AGG", "MBB", "MUB", "EMB"],
    "Commodities": ["GLD", "SLV", "USO", "UNG", "DBA", "PDBC", "GSG", "CPER"],
    "Factors_Dividends": ["VIG", "VYM", "SDY", "QUAL", "VLUE", "MTUM", "USMV", "RSP"],
    "Real_Estate": ["VNQ", "SCHH", "IYR", "XLRE"]
}

# 2. Filter
MIN_YEARS_HISTORY = 10
MIN_AVG_DAILY_VOLUME = 1000000
TARGET_BATCH_SIZE = 50

def check_etf_eligibility(ticker):
    """Prüft, ob der ETF alt genug und liquide genug für die Pipeline ist."""
    print(f"Prüfe {ticker}...")
    try:
        etf = yf.Ticker(ticker)
        hist = etf.history(period="max")
        
        if hist.empty:
            return False, "Keine Datenbank-Einträge."

        # 1. Check: Alter des ETFs
        first_date = hist.index[0].tz_localize(None)
        cutoff_date = datetime.now() - timedelta(days=365 * MIN_YEARS_HISTORY)
        
        if first_date > cutoff_date:
            return False, f"Zu jung (Start: {first_date.strftime('%Y-%m-%d')})"

        # 2. Check: Liquidität (Durchschnittliches Volumen der letzten 60 Tage)
        recent_volume = hist['Volume'].tail(60).mean()
        if recent_volume < MIN_AVG_DAILY_VOLUME:
            return False, f"Zu illiquide (Volumen: {recent_volume:,.0f})"

        return True, "Bestanden"
        
    except Exception as e:
        return False, f"API Fehler: {str(e)}"

def main():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starte ETF Selektion...")
    
    valid_etfs = []
    
    # Iteriere gleichmäßig durch alle Kategorien, um Diversifikation zu erzwingen
    for category, tickers in SEED_UNIVERSE.items():
        category_count = 0
        for ticker in tickers:
            # Stoppe, wenn wir insgesamt 50 ETFs haben
            if len(valid_etfs) >= TARGET_BATCH_SIZE:
                break
                
            is_valid, reason = check_etf_eligibility(ticker)
            
            if is_valid:
                valid_etfs.append(ticker)
                category_count += 1
                print(f"  -> [OK] {ticker} hinzugefügt (Kategorie: {category})")
            else:
                print(f"  -> [REJECTED] {ticker}: {reason}")
                
    print("\n" + "="*40)
    print(f"Selektion abgeschlossen. {len(valid_etfs)} ETFs validiert.")
    
    # 3. Speichern des Batch
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'batch_targets.json')
    
    with open(output_path, 'w') as f:
        json.dump({
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_count": len(valid_etfs),
            "tickers": valid_etfs
        }, f, indent=4)
        
    print(f"Liste gespeichert unter: {output_path}")

if __name__ == "__main__":
    main()