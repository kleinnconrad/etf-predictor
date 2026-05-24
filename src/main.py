# src/main.py

from datetime import datetime
from config import (
    TARGET_ETF, START_DATE, END_DATE, FORECAST_HORIZON_DAYS, 
    ANNUAL_INFLATION_RATE, ANNUAL_MARGIN, TRADING_DAYS_PER_YEAR, 
    get_all_tickers
)
from data_pipeline import load_and_prepare_data
from modeling import perform_feature_selection

def main():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] PIPELINE START")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] INITIALIZING: Fetching ticker universe...")
    all_tickers = get_all_tickers()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 1. Daten laden und vorbereiten
    print(f"[{datetime.now().strftime('%H:%M:%S')}] CALLING: load_and_prepare_data")
    X_scaled, y, latest_features_scaled = load_and_prepare_data(
        target_ticker=TARGET_ETF, 
        all_tickers=all_tickers, 
        start_date=START_DATE, 
        end_date=END_DATE, 
        forecast_horizon=FORECAST_HORIZON_DAYS,
        annual_inflation=ANNUAL_INFLATION_RATE,
        annual_margin=ANNUAL_MARGIN,
        trading_days=TRADING_DAYS_PER_YEAR,
        timestamp=timestamp
    )
    print(f"[{datetime.now().strftime('%H:%M:%S')}] RETURNED: load_and_prepare_data. Matrix shape: X={X_scaled.shape}, y={y.shape}")
    
    # 2. Modell trainieren & KS-Statistik optimieren
    # Wir fangen das gesamte Dictionary ab!
    print(f"[{datetime.now().strftime('%H:%M:%S')}] CALLING: perform_feature_selection")
    results_dict = perform_feature_selection(
        X_scaled=X_scaled, 
        y=y, 
        latest_features_scaled=latest_features_scaled,
        target_etf=TARGET_ETF,
        horizon=FORECAST_HORIZON_DAYS,
        final_features=8, 
        timestamp=timestamp
    )
    print(f"[{datetime.now().strftime('%H:%M:%S')}] RETURNED: perform_feature_selection")
    
    # 3. Lokale Konsolen-Ausgabe der neuen Metriken
    print("\n" + "="*40)
    print("=== Pipeline erfolgreich beendet ===")
    print("="*40)
    print(f"OOF Cross-Validation Accuracy: {results_dict['cv_accuracy']:.2%}")
    print(f"Quality Gate bestanden:        {results_dict['is_valid_quality']}")
    print(f"Optimierter KS-Cutoff (-1):    {results_dict['ks_cutoff']:.2%}")
    
    if not results_dict['is_valid_quality']:
        print("\nWARNUNG: Quality Gate nicht bestanden! Prognose ist statistisch nicht signifikant.")

if __name__ == "__main__":
    main()