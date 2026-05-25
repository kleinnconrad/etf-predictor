# src/data_pipeline.py

import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.preprocessing import StandardScaler
from fredapi import Fred
from config import ALL_FRED_INDICATORS
from datetime import datetime
import os

def fetch_and_lag_fred_data(start_date, end_date, lag_days=30):
    """
    Fetches macroeconomic data natively using the official FRED API 
    and applies a uniform publication lag.
    """
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Initiating FRED API data download for {len(FRED_INDICATORS)} indicators...")
    
    adjusted_start = pd.to_datetime(start_date) - pd.Timedelta(days=60)
    series_list = []
    
    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        raise ValueError("CRITICAL ERROR: FRED_API_KEY is not set.")
        
    fred = Fred(api_key=api_key)
    
    for indicator in ALL_FRED_INDICATORS:
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Fetching {indicator} via API...")
        try:
            series = fred.get_series(indicator, observation_start=adjusted_start, observation_end=end_date)
            df = pd.DataFrame(series, columns=[indicator])
            df.index.name = 'DATE'
            series_list.append(df[indicator])
        except Exception as e:
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE ERROR: Failed to fetch {indicator}. Details: {e}")
            raise 
            
    fred_raw = pd.concat(series_list, axis=1)
    fred_shifted = fred_raw.shift(freq=pd.Timedelta(days=lag_days))
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: FRED API data download complete.")
    return fred_shifted

def load_and_prepare_data(target_ticker, all_tickers, start_date, end_date, forecast_horizon=126, **kwargs):
    """
    Ingests, merges, and engineers features for the trading calendar.
    """
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Initiating Yahoo Finance download...")
    raw_yahoo = yf.download(all_tickers, start=start_date, end=end_date)['Close']
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Yahoo Finance download complete.")
    
    master_calendar = raw_yahoo.dropna(subset=[target_ticker])
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Calling FRED data fetch...")
    fred_shifted = fetch_and_lag_fred_data(start_date, end_date)
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Merging matrices and forward-filling...")
    combined_data = master_calendar.join(fred_shifted, how='left')
    imputed_data = combined_data.ffill().dropna(axis=1, how='all').dropna()
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Calculating rolling momentum (Feature Engineering)...")
    windows = [21, 63, 126]

    # Build all columns at once to avoid DataFrame fragmentation
    col_dict = {}
    for col in imputed_data.columns:
        for w in windows:
            col_dict[f'{col}_{w}M_ret'] = imputed_data[col].pct_change(w)

    features = pd.DataFrame(col_dict, index=imputed_data.index)

    # Clean Inf and NaN values caused by rolling calculations
    features = features.replace([np.inf, -np.inf], np.nan)

    features['future_6M_return'] = (
        imputed_data[target_ticker].shift(-forecast_horizon) 
        / imputed_data[target_ticker] - 1
    )
    
    def categorize_return(ret):
        if pd.isna(ret): return None
        elif ret > 0.0175: return 1
        elif ret < 0.0075: return -1
        else: return 0
            
    features['target_class'] = features['future_6M_return'].apply(categorize_return)

    # Impute NaN in feature columns for ALL rows (training, CV, and live) uniformly.
    # ffill: last known value forward; bfill: fallback for any leading NaNs.
    # Applied before splitting so the scaler sees a consistent distribution.
    feature_cols_for_impute = [c for c in features.columns if c not in ['target_class', 'future_6M_return']]
    features[feature_cols_for_impute] = features[feature_cols_for_impute].ffill().bfill()

    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Splitting live and training rows...")

    # Separate live rows BEFORE any dropna, so they aren't wiped out
    live_predict_row = features[features['target_class'].isna()].copy()

    # Drop rows where target_class is missing (live rows) or any feature is NaN
    training_matrix = features.dropna(subset=['target_class']).copy()
    training_matrix = training_matrix.dropna()

    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Training rows: {len(training_matrix)}, Live rows: {len(live_predict_row)}")

    if live_predict_row.empty:
        raise ValueError(
            "No live prediction rows found. All rows have a known future return, "
            "which means end_date may not be recent enough to produce unlabelled rows."
        )

    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Scaling features...")
    feature_cols = [c for c in training_matrix.columns if c not in ['target_class', 'future_6M_return']]
    
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(training_matrix[feature_cols]), 
        columns=feature_cols, 
        index=training_matrix.index
    )
    y_train = training_matrix['target_class']
    
    X_live_scaled = pd.DataFrame(
        scaler.transform(live_predict_row[feature_cols]), 
        columns=feature_cols, 
        index=live_predict_row.index
    )
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Data preparation complete.")
    return X_train_scaled, y_train, X_live_scaled