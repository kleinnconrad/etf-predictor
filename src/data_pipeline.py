# src/data_pipeline.py

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import warnings

warnings.filterwarnings('ignore', category=pd.errors.PerformanceWarning)

def load_and_prepare_data(target_ticker, all_tickers, start_date, end_date, forecast_horizon, annual_inflation, annual_margin, trading_days, timestamp):
    print(f"Lade Daten für {len(all_tickers)} Ticker...")
    
    raw_data = yf.download(all_tickers, start=start_date, end=end_date, progress=False, auto_adjust=True)['Close']
    
    # 1. Master-Kalender erzwingen: Alle Wochenenden/Feiertage löschen, an denen der SPY nicht gehandelt wurde
    raw_data = raw_data.dropna(subset=[target_ticker])
    
    # 2. Erst jetzt den 90%-Filter auf alle anderen Variablen anwenden
    threshold = len(raw_data) * 0.9
    data = raw_data.dropna(axis=1, thresh=threshold).ffill().dropna()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..'))
    output_dir = os.path.join(project_root, 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    csv_path = os.path.join(output_dir, f"yahoo_data_{timestamp}.csv")
    data.to_csv(csv_path)
    print(f"Verwendete Yahoo-Daten gespeichert unter: {csv_path}")
    
    ret_1m = data.pct_change(21).add_suffix('_1M')
    ret_3m = data.pct_change(63).add_suffix('_3M')
    ret_6m = data.pct_change(126).add_suffix('_6M')
    features = pd.concat([ret_1m, ret_3m, ret_6m], axis=1)
    
    # NEU: Wir sichern den allerletzten Tag für den Predict (noch ohne dropna)
    latest_features_raw = features.iloc[-1:]
    
    future_return = data[target_ticker].pct_change(forecast_horizon).shift(-forecast_horizon)
    time_fraction = forecast_horizon / trading_days
    period_baseline = annual_inflation * time_fraction
    period_margin = annual_margin * time_fraction
    upper_threshold = period_baseline + period_margin
    lower_threshold = period_baseline - period_margin

    def categorize_return(ret):
        if pd.isna(ret): return np.nan
        if ret > upper_threshold: return 1       
        elif ret < lower_threshold: return -1    
        else: return 0                           

    target = future_return.apply(categorize_return)
    
    df = features.join(target.rename('Target')).dropna()
    X = df.drop(columns=['Target'])
    y = df['Target']

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns, index=X.index)
    
    # NEU: Wir skalieren den heutigen Datenpunkt mit dem Trainings-Scaler
    latest_features_scaled = pd.DataFrame(scaler.transform(latest_features_raw), columns=X.columns, index=latest_features_raw.index)
    
    print(f"Daten vorbereitet. Skalierte Feature-Matrix: {X_scaled.shape}")
    print(f"Aktuellster Datenpunkt für Prognose isoliert: {latest_features_scaled.index[0].strftime('%Y-%m-%d')}\n")
    
    return X_scaled, y, latest_features_scaled