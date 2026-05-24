import pandas as pd
import yfinance as yf
from sklearn.preprocessing import StandardScaler
from config import FRED_INDICATORS

def fetch_and_lag_fred_data(start_date, end_date, lag_days=30):
    """
    Fetches macroeconomic data natively from FRED CSV endpoints 
    and applies a uniform publication lag.
    """
    adjusted_start = pd.to_datetime(start_date) - pd.Timedelta(days=60)
    series_list = []
    
    # Spoof a standard web browser to bypass FRED's anti-bot 403 Forbidden blocks
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    for indicator in FRED_INDICATORS:
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={indicator}"
        
        # Pass the headers via storage_options
        df = pd.read_csv(
            url, 
            index_col='DATE', 
            parse_dates=True, 
            na_values='.',
            storage_options=headers
        )
        
        df = df.loc[adjusted_start:end_date]
        series_list.append(df[indicator])
        
    fred_raw = pd.concat(series_list, axis=1)
    fred_shifted = fred_raw.shift(freq=pd.Timedelta(days=lag_days))
    
    return fred_shifted

def load_and_prepare_data(target_ticker, all_tickers, start_date, end_date, forecast_horizon=126, **kwargs):
    """
    Ingests, merges, and engineers features for the trading calendar.
    """
    # 1. Ingest Daily Equity Data
    raw_yahoo = yf.download(all_tickers, start=start_date, end=end_date)['Close']
    master_calendar = raw_yahoo.dropna(subset=[target_ticker])
    
    # 2. Ingest and Shift Monthly Macro Data
    fred_shifted = fetch_and_lag_fred_data(start_date, end_date)
    
    # 3. Merge and Impute
    combined_data = master_calendar.join(fred_shifted, how='left')
    imputed_data = combined_data.ffill().dropna(axis=1, how='all').dropna()
    
    # 4. Feature Engineering (Momentum)
    windows = [21, 63, 126]
    features = pd.DataFrame(index=imputed_data.index)
    
    for col in imputed_data.columns:
        for w in windows:
            features[f'{col}_{w}M_ret'] = imputed_data[col].pct_change(w)
            
    # 5. Target Engineering
    features['future_6M_return'] = imputed_data[target_ticker].shift(-forecast_horizon) / imputed_data[target_ticker] - 1
    
    def categorize_return(ret):
        if pd.isna(ret):
            return None
        elif ret > 0.0175:
            return 1
        elif ret < 0.0075:
            return -1
        else:
            return 0
            
    features['target_class'] = features['future_6M_return'].apply(categorize_return)
    
    # 6. Matrix Separation
    features = features.dropna(subset=[f'{target_ticker}_126M_ret'])
    
    live_predict_row = features[features['target_class'].isna()].copy()
    training_matrix = features.dropna(subset=['target_class']).copy()
    
    # 7. Z-Score Scaling
    feature_cols = [c for c in training_matrix.columns if c not in ['target_class', 'future_6M_return']]
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(training_matrix[feature_cols])
    y_train = training_matrix['target_class']
    
    X_live_scaled = scaler.transform(live_predict_row[feature_cols])
    
    return X_train_scaled, y_train, X_live_scaled