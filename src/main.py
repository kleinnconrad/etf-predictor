# src/main.py

from datetime import datetime
from config import (
    TARGET_ETF, START_DATE, END_DATE, FORECAST_HORIZON_DAYS, 
    ANNUAL_INFLATION_RATE, ANNUAL_MARGIN, TRADING_DAYS_PER_YEAR, 
    get_all_tickers
)
from data_pipeline import load_and_prepare_data
from modeling import perform_feature_selection
from evaluation import evaluate_and_plot

def main():
    all_tickers = get_all_tickers()
    
    # Zentraler Zeitstempel für konsistente Dateinamen über alle Exporte hinweg
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    X_scaled, y = load_and_prepare_data(
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
    
    model, X_optimal = perform_feature_selection(
        X_scaled=X_scaled, 
        y=y, 
        final_features=8, 
        timestamp=timestamp
    )
    
    evaluate_and_plot(model, X_optimal, y, FORECAST_HORIZON_DAYS)

if __name__ == "__main__":
    main()