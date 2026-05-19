# src/data_pipeline.py

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore', category=pd.errors.PerformanceWarning)

def load_and_prepare_data(target_ticker, all_tickers, start_date, end_date, forecast_horizon, annual_inflation, annual_margin, trading_days):
    print(f"Lade Daten für {len(all_tickers)} Ticker...")
    # show_errors=False entfernt. Um den Output dennoch sauber zu halten, nutzen wir progress=False
    raw_data = yf.download(all_tickers, start=start_date, end=end_date, progress=False)['Adj Close']    
    threshold = len(raw_data) * 0.9
    data = raw_data.dropna(axis=1, thresh=threshold).ffill().dropna()
    
    ret_1m = data.pct_change(21).add_suffix('_1M')
    ret_3m = data.pct_change(63).add_suffix('_3M')
    ret_6m = data.pct_change(126).add_suffix('_6M')
    features = pd.concat([ret_1m, ret_3m, ret_6m], axis=1)
    
    future_return = data[target_ticker].pct_change(forecast_horizon).shift(-forecast_horizon)

    time_fraction = forecast_horizon / trading_days
    
    period_baseline = annual_inflation * time_fraction
    period_margin = annual_margin * time_fraction

    upper_threshold = period_baseline + period_margin
    lower_threshold = period_baseline - period_margin

    print(f"Zeitanteil (Jahre): {time_fraction:.2f}")
    print(f"Klassifizierungs-Baseline für {forecast_horizon} Tage: {period_baseline:.2%}")
    print(f"Dynamischer Korridor: +/- {period_margin:.2%}")
    print(f"Schwellenwerte -> Up: > {upper_threshold:.2%} | Down: < {lower_threshold:.2%}\n")

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
    
    print(f"Daten vorbereitet. Skalierte Feature-Matrix: {X_scaled.shape}\n")
    return X_scaled, y