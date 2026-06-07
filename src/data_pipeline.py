# src/data_pipeline.py

import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.preprocessing import StandardScaler
from fredapi import Fred
from config import (
    ALL_FRED_INDICATORS,
    ANNUAL_INFLATION_RATE,
    ANNUAL_MARGIN_UP,
    ANNUAL_MARGIN_DOWN,
    TRADING_DAYS_PER_YEAR
)
from datetime import datetime
import time
import os
import socket

# Global security timeout for the API
socket.setdefaulttimeout(15.0)

def fetch_and_lag_fred_data(start_date, end_date, lag_days=30):
    """
    Fetches macroeconomic data natively using the official FRED API 
    and applies a uniform publication lag. Gracefully skips missing series.
    Includes rate-limiting and DateTime index enforcement to prevent shift() errors.
    """
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Initiating FRED API data download for {len(ALL_FRED_INDICATORS)} indicators...", flush=True)
    
    adjusted_start = pd.to_datetime(start_date) - pd.Timedelta(days=60)
    series_list = []
    failed_tickers = []  # List to track failed downloads
    
    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        raise ValueError("CRITICAL ERROR: FRED_API_KEY is not set.")
        
    fred = Fred(api_key=api_key)
    
    for indicator in ALL_FRED_INDICATORS:
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Fetching {indicator} via API...", flush=True)
        try:
            series = fred.get_series(indicator, observation_start=adjusted_start, observation_end=end_date)
            df = pd.DataFrame(series, columns=[indicator])
            df.index.name = 'DATE'
            series_list.append(df[indicator])
            
            # Rate-Limiting Protection (120 req/min limit on FRED)
            time.sleep(0.5) 
            
        except Exception as e:
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE WARNING: Failed to fetch {indicator}. Details: {e}", flush=True)
            failed_tickers.append(indicator)
            time.sleep(1) # Extra cooldown on error
            continue 
            
    # =========================================================================
    # HARD ERROR CHECKING (ANTI DATA-LEAKAGE)
    # =========================================================================
    if failed_tickers:
        # The script MUST crash if FRED data is missing, otherwise the batch run learns 
        # on a smaller/incorrect feature set than your local test!
        raise ValueError(f"CRITICAL: FRED API Timeout for {failed_tickers}. Local and batch features would be asynchronous!")
            
    fred_raw = pd.concat(series_list, axis=1)

    # API Crash Protection: Ensure data is not completely empty
    if fred_raw.empty:
        raise ValueError("FRED API returned a completely empty matrix. Most likely the rate limit was exceeded!")

    # Type Enforcement: Force index to be DateTime to prevent ".shift() Got type Index" errors
    fred_raw.index = pd.to_datetime(fred_raw.index)
    
    # Safe shifting to simulate real-world publication lag
    fred_shifted = fred_raw.shift(freq=pd.Timedelta(days=lag_days))
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: FRED API data download complete.", flush=True)
    return fred_shifted

def load_and_prepare_data(target_ticker, all_tickers, start_date, end_date, forecast_horizon=126, pre_fetched_yahoo=None, pre_fetched_fred=None, **kwargs):
    """
    Ingests, merges, and engineers features for the trading calendar.
    Uses pre-fetched DataFrames in batch mode to prevent multiple downloads.
    """
    
    # 1. Yahoo Finance Ingestion (Local or via Network)
    if pre_fetched_yahoo is not None:
        raw_yahoo = pre_fetched_yahoo.copy()
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Using pre-fetched Yahoo Finance data.", flush=True)
    else:
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Initiating Yahoo Finance download...", flush=True)
        raw_yahoo = yf.download(all_tickers, start=start_date, end=end_date)['Close']
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Yahoo Finance download complete.", flush=True)
    
    master_calendar = raw_yahoo.dropna(subset=[target_ticker])
    
    # 2. FRED Ingestion (Local or via Network)
    if pre_fetched_fred is not None:
        fred_shifted = pre_fetched_fred.copy()
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Using pre-fetched FRED data.", flush=True)
    else:
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Calling FRED data fetch...", flush=True)
        fred_shifted = fetch_and_lag_fred_data(start_date, end_date)
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Merging matrices and forward-filling...", flush=True)
    combined_data = master_calendar.join(fred_shifted, how='left')
    
    # Uses the new Pandas syntax to avoid FutureWarning
    imputed_data = combined_data.ffill().infer_objects(copy=False).dropna(axis=1, how='all').dropna()
    
    # -------------------------------------------------------------------------
    # DETERMINISTIC INTERACTION EFFECTS (ECONOMIC RATIOS)
    # -------------------------------------------------------------------------
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Engineering economic interaction ratios...", flush=True)
    
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
    # ADVANCED QUANTITATIVE FEATURE ENGINEERING
    # -------------------------------------------------------------------------
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Engineering advanced quantitative features...", flush=True)
    
    # Lookback windows (1 month, 1 quarter, half year, 1 full year)
    windows = [21, 63, 126, 252] 

    # Identify metrics (rates, spreads, quotas, sentiment) where pct_change() MUST NOT be applied
    RATE_KEYWORDS = ['TNX', 'IRX', 'VIX', 'UNRATE', 'T10Y2Y', 'EPU', 'ratio_', 'HUTTTT', 'NFCI', 'BAML', 'UMCSENT']
    
    # Macroeconomic indicators for calculating "acceleration" (2nd derivative)
    MACRO_KEYWORDS = ['CPIAUCSL', 'M2SL', 'PAYEMS', 'UNRATE', 'ASSETS', 'PROIND', 'PERMIT']

    col_dict = {}
    
    for col in imputed_data.columns:
        # Check: Is the column a rate/spread or a regular price/index?
        is_rate_or_spread = any(kw in col for kw in RATE_KEYWORDS)
        
        # --- 0. PRESERVE STATIONARY LEVELS ---
        # Spreads, ratios, and VIX are already stationary. 
        # The model MUST see the absolute level (e.g., VIX at 35 or yield curve < 0).
        if is_rate_or_spread:
            col_dict[f'{col}_Level'] = imputed_data[col]

        # --- 1. MULTI-TIMEFRAME MOMENTUM ---
        for w in windows:
            if is_rate_or_spread:
                # Absolute change in points (e.g., yields rose by +0.5)
                col_dict[f'{col}_{w}D_diff'] = imputed_data[col].diff(w)
            else:
                # Percentage change for prices (e.g., SPY rose by +10%)
                col_dict[f'{col}_{w}D_ret'] = imputed_data[col].pct_change(w)
                
        # --- 2. DISTANCE TO TREND (MEAN REVERSION / 200-DAY SMA) ---
        # Measures overextensions. If an index is 20% above its trend, it often signals danger.
        sma_200 = imputed_data[col].rolling(window=200).mean()
        if is_rate_or_spread:
            col_dict[f'{col}_Dist_SMA200'] = imputed_data[col] - sma_200
        else:
            col_dict[f'{col}_Dist_SMA200'] = (imputed_data[col] / sma_200) - 1.0
            
        # --- 3. MACRO ACCELERATION (2ND DERIVATIVE) ---
        # Is the 1-year macro trend accelerating compared to 3 months ago?
        if any(kw in col for kw in MACRO_KEYWORDS):
            if is_rate_or_spread:
                current_1Y_change = imputed_data[col].diff(252)
                past_1Y_change = imputed_data[col].shift(63).diff(252)
            else:
                current_1Y_change = imputed_data[col].pct_change(252)
                past_1Y_change = imputed_data[col].shift(63).pct_change(252)
            
            col_dict[f'{col}_YoY_Accel_3M'] = current_1Y_change - past_1Y_change

        # --- 4. ROLLING Z-SCORES (REGIME NORMALIZATION) ---
        # Is the current volatility (VIX) or uncertainty normal for the current market environment?
        if 'VIX' in col or 'credit_spread' in col or 'EPU' in col:
            # 2-year window for the rolling baseline
            roll_mean = imputed_data[col].rolling(window=504).mean()
            # Add epsilon (1e-8) to avoid division by zero during temporarily flat spreads
            roll_std = imputed_data[col].rolling(window=504).std() + 1e-8
            col_dict[f'{col}_Roll_ZScore_2Y'] = (imputed_data[col] - roll_mean) / roll_std

    # Assemble the feature matrix
    features = pd.DataFrame(col_dict, index=imputed_data.index)

    # Clean Inf and NaN values caused by mathematical rolling operations
    features = features.replace([np.inf, -np.inf], np.nan)

    # -------------------------------------------------------------------------
    # TARGET VARIABLE CALCULATION
    # -------------------------------------------------------------------------
    # Calculate future return using the original imputed prices to preserve accuracy
    features['future_return'] = (
        imputed_data[target_ticker].shift(-forecast_horizon) 
        / imputed_data[target_ticker] - 1
    )
    
    # --- DYNAMIC THRESHOLD CALCULATION ---
    # Scales the annual rates to the forecast horizon
    time_scaling = forecast_horizon / TRADING_DAYS_PER_YEAR
    
    threshold_up = (ANNUAL_INFLATION_RATE + ANNUAL_MARGIN_UP) * time_scaling
    threshold_down = (ANNUAL_INFLATION_RATE - ANNUAL_MARGIN_DOWN) * time_scaling

    def categorize_return(ret):
        if pd.isna(ret): return None
        elif ret > threshold_up: return 1
        elif ret < threshold_down: return -1
        else: return 0
            
    features['target_class'] = features['future_return'].apply(categorize_return)

    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Splitting live and training rows...", flush=True)

    # Separate live rows BEFORE any dropna, so they aren't wiped out
    live_predict_row = features[features['target_class'].isna()].copy()
    
    # Isolate exclusively the absolutely most recent trading day (Today)
    live_predict_row = live_predict_row.iloc[[-1]]

    # Drop rows where target_class is missing (live rows) or any feature is NaN
    # This correctly removes the extended warmup period required by the 504-day rolling windows
    # without leaking future data.
    training_matrix = features.dropna(subset=['target_class']).copy()
    training_matrix = training_matrix.dropna()

    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Training rows: {len(training_matrix)}, Live rows: {len(live_predict_row)}", flush=True)

    if live_predict_row.empty:
        raise ValueError(
            "No live prediction rows found. All rows have a known future return, "
            "which means end_date may not be recent enough to produce unlabelled rows."
        )

    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Scaling features...", flush=True)
    feature_cols = [c for c in training_matrix.columns if c not in ['target_class', 'future_return']]
    
    # =========================================================================
    # DETERMINISTIC WINSORIZATION (CLIPPING OUTLIERS)
    # =========================================================================
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Clipping outliers at 1st and 99th percentiles...", flush=True)
    
    # 1. Calculate the hard limits ONLY based on the training data
    lower_bounds = training_matrix[feature_cols].quantile(0.01)
    upper_bounds = training_matrix[feature_cols].quantile(0.99)
    
    # 2. Cap all extreme outliers to these limits in the training set
    training_matrix[feature_cols] = training_matrix[feature_cols].clip(lower=lower_bounds, upper=upper_bounds, axis=1)
    
    # 3. Apply exactly the same limits to the live data point
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
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] PIPELINE: Data preparation complete.", flush=True)
    return X_train_scaled, y_train, X_live_scaled