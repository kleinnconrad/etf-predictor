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
    and applies a uniform publication lag. Gracefully skips missing series.
    """
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Initiating FRED API data download for {len(ALL_FRED_INDICATORS)} indicators...")
    
    adjusted_start = pd.to_datetime(start_date) - pd.Timedelta(days=60)
    series_list = []
    failed_tickers = []  # List to track failed downloads
    
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
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE WARNING: Failed to fetch {indicator}. Skipping. Details: {e}")
            failed_tickers.append(indicator)
            continue 
            
    # Print summary of failures if any occurred
    if failed_tickers:
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE SUMMARY: {len(failed_tickers)} FRED indicators failed and were skipped:")
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] DROPPED TICKERS: {', '.join(failed_tickers)}")
            
    fred_raw = pd.concat(series_list, axis=1)
    fred_shifted = fred_raw.shift(freq=pd.Timedelta(days=lag_days))
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: FRED API data download complete.")
    return fred_shifted

def load_and_prepare_data(target_ticker, all_tickers, start_date, end_date, forecast_horizon=126, pre_fetched_yahoo=None, pre_fetched_fred=None, **kwargs):
    """
    Ingests, merges, and engineers features for the trading calendar.
    Nutzt vorab geladene DataFrames im Batch-Modus, um Mehrfach-Downloads zu verhindern.
    """
    
    # 1. Yahoo Finance Ingestion (Lokal oder via Netzwerk)
    if pre_fetched_yahoo is not None:
        raw_yahoo = pre_fetched_yahoo.copy()
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Using pre-fetched Yahoo Finance data.")
    else:
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Initiating Yahoo Finance download...")
        raw_yahoo = yf.download(all_tickers, start=start_date, end=end_date)['Close']
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Yahoo Finance download complete.")
    
    master_calendar = raw_yahoo.dropna(subset=[target_ticker])
    
    # 2. FRED Ingestion (Lokal oder via Netzwerk)
    if pre_fetched_fred is not None:
        fred_shifted = pre_fetched_fred.copy()
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Using pre-fetched FRED data.")
    else:
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Calling FRED data fetch...")
        fred_shifted = fetch_and_lag_fred_data(start_date, end_date)
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Merging matrices and forward-filling...")
    combined_data = master_calendar.join(fred_shifted, how='left')
    imputed_data = combined_data.ffill().dropna(axis=1, how='all').dropna()
    
    # -------------------------------------------------------------------------
    # DETERMINISTIC INTERACTION EFFECTS (ECONOMIC RATIOS)
    # -------------------------------------------------------------------------
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Engineering economic interaction ratios...")
    
    # Safely calculate ratios only if both tickers exist in the downloaded data
    def safe_ratio(num, den, col_name):
        if num in imputed_data.columns and den in imputed_data.columns:
            imputed_data[col_name] = imputed_data[num] / imputed_data[den]

    safe_ratio('HG=F', 'GC=F', 'ratio_copper_gold')
    safe_ratio('HYG', 'LQD', 'ratio_credit_spread')
    safe_ratio('XLY', 'XLP', 'ratio_consumer_risk')
    safe_ratio('SPY', 'TLT', 'ratio_risk_on_off')
    safe_ratio('XLK', 'SPY', 'ratio_tech_dominance')
    safe_ratio('IGOV', 'TLT', 'ratio_intl_vs_us_bonds')
    # -------------------------------------------------------------------------
    
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

    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Splitting live and training rows...")

    # Separate live rows BEFORE any dropna, so they aren't wiped out
    live_predict_row = features[features['target_class'].isna()].copy()
    
    # NEU: Isoliere ausschließlich den absolut aktuellsten Handelstag (Heute)
    live_predict_row = live_predict_row.iloc[[-1]]

    # Drop rows where target_class is missing (live rows) or any feature is NaN
    # This correctly removes the 126-day warmup period without leaking future data.
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
    
    # =========================================================================
    # DETERMINISTIC WINSORIZATION (CLIPPING OUTLIERS)
    # =========================================================================
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Clipping outliers at 1st and 99th percentiles...")
    
    # 1. Berechne die harten Limits NUR auf Basis der Trainingsdaten
    lower_bounds = training_matrix[feature_cols].quantile(0.01)
    upper_bounds = training_matrix[feature_cols].quantile(0.99)
    
    # 2. Kappe alle extremen Ausreißer auf diese Limits im Trainingsset
    training_matrix[feature_cols] = training_matrix[feature_cols].clip(lower=lower_bounds, upper=upper_bounds, axis=1)
    
    # 3. Wende exakt dieselben Limits auf den Live-Datenpunkt an
    live_predict_row[feature_cols] = live_predict_row[feature_cols].clip(lower=lower_bounds, upper=upper_bounds, axis=1)
    # =========================================================================

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