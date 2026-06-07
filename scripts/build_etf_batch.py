# scripts/build_etf_batch.py

import yfinance as yf
import pandas as pd
import json
import os
import time
from datetime import datetime, timedelta
import sys

# Add the src directory to path so we can import the centralized config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from config import MIN_YEARS_HISTORY

# 1. Calibrated Metrics for Europe
MIN_AVG_DAILY_TURNOVER_EUR = 1000000  # 1 Million Euro daily trading turnover
CHUNK_SIZE = 100
SLEEP_BETWEEN_CHUNKS = 5

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    seed_file_path = os.path.join(project_root, 'config', 'all_etfs_seed.txt')
    
    if not os.path.exists(seed_file_path):
        print(f"Error: Seed file not found at {seed_file_path}")
        return

    with open(seed_file_path, 'r') as f:
        all_tickers = [line.strip() for line in f if line.strip()]
        
    print("\n" + "="*60)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] STARTING CALIBRATED XETRA SCREENING")
    print(f"Conditions: > {MIN_YEARS_HISTORY} years history AND > 1 M € daily turnover")
    print(f"Checking {len(all_tickers)} tickers in chunks of {CHUNK_SIZE} (rate limit protected)...")
    print("="*60 + "\n")
    
    valid_etfs = []
    
    # Calculate the cutoff date (exactly 10 years ago)
    target_start_date = datetime.now() - timedelta(days=365 * MIN_YEARS_HISTORY)
    
    # We fetch from slightly earlier to guarantee we capture the start date 
    # if the ETF was launched exactly 10 years ago.
    fetch_start_date = target_start_date - timedelta(days=15)
    start_date_str = fetch_start_date.strftime('%Y-%m-%d')
    
    # Split the tickers into manageable chunks to avoid API timeouts
    chunks = [all_tickers[i:i + CHUNK_SIZE] for i in range(0, len(all_tickers), CHUNK_SIZE)]
    
    for idx, chunk in enumerate(chunks):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading Chunk {idx + 1}/{len(chunks)} ({len(chunk)} Tickers)...")
        
        try:
            # group_by="ticker" creates a MultiIndex where level 0 is the Ticker and level 1 is OHLCV
            df = yf.download(chunk, start=start_date_str, group_by="ticker", threads=True, progress=False)
            
            # If the chunk only has 1 ticker, yfinance returns a single-index DataFrame
            if len(chunk) == 1:
                ticker = chunk[0]
                if df.empty:
                    print(f"  [REJECTED] {ticker} - No data found")
                else:
                    _process_single_ticker_df(ticker, df, target_start_date, valid_etfs)
                continue
                
            # For multiple tickers, iterate over the downloaded columns
            # Handle cases where some tickers completely failed to download (not in columns)
            downloaded_tickers = set(df.columns.get_level_values(0))
            
            for ticker in chunk:
                if ticker not in downloaded_tickers:
                    print(f"  [REJECTED] {ticker} - No data found / API Timeout")
                    continue
                    
                # Extract the subset for this specific ticker
                ticker_data = df[ticker].dropna(subset=['Close', 'Volume'])
                
                if ticker_data.empty:
                    print(f"  [REJECTED] {ticker} - No usable price data in this period")
                    continue
                    
                _process_single_ticker_df(ticker, ticker_data, target_start_date, valid_etfs)
                
        except Exception as e:
            print(f"Error at Chunk {idx + 1}: {e}")
            
        # Intentional delay to avoid getting IP-banned by Yahoo Finance
        if idx < len(chunks) - 1:
            print(f"  > Pausing for {SLEEP_BETWEEN_CHUNKS} seconds to protect against rate limits...")
            time.sleep(SLEEP_BETWEEN_CHUNKS)

    valid_etfs.sort()

    print("\n" + "="*60)
    print(f"SELECTION COMPLETED!")
    print(f"{len(valid_etfs)} highly liquid, proven ETFs are ready for the model.")
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
        
    print(f"Batch targets saved at: {output_path}")

def _process_single_ticker_df(ticker, ticker_data, target_start_date, valid_etfs):
    """
    Evaluates age and liquidity locally on the downloaded Pandas DataFrame.
    """
    # 1. Check: Age of the ETF
    # The first index in the dataframe must be on or before the target_start_date
    first_date = ticker_data.index[0]
    if first_date.tzinfo is not None:
        first_date = first_date.tz_localize(None)
        
    if first_date > target_start_date:
        # print(f"  [REJECTED] {ticker} - Too young (Start: {first_date.strftime('%Y-%m')})")
        return

    # 2. Check: Real liquidity (Turnover in Euro)
    # Average over the last 60 trading days
    recent_data = ticker_data.tail(60)
    avg_turnover = (recent_data['Volume'] * recent_data['Close']).mean()
    
    if avg_turnover < MIN_AVG_DAILY_TURNOVER_EUR:
        # print(f"  [REJECTED] {ticker} - Too illiquid (Volume: {avg_turnover/1000000:.1f} M €)")
        return

    print(f"  [OK] {ticker} (Target reached!)")
    valid_etfs.append(ticker)

if __name__ == "__main__":
    main()