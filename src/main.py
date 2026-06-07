# src/main.py

import os
import json
import math
import argparse
import random
import time
from datetime import datetime
import pandas as pd
import yfinance as yf

from config import (
    TARGET_ETF, 
    ALL_TICKERS, 
    START_DATE, 
    END_DATE, 
    FORECAST_HORIZON_DAYS,
    ANNUAL_INFLATION_RATE,
    ANNUAL_MARGIN_UP,
    ANNUAL_MARGIN_DOWN
)
from data_pipeline import load_and_prepare_data, fetch_and_lag_fred_data
from modeling import perform_feature_selection

# Suppress warnings for clean logs
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', category=RuntimeWarning)
try:
    from sklearn.exceptions import UndefinedMetricWarning
    warnings.filterwarnings('ignore', category=UndefinedMetricWarning)
except ImportError:
    pass

def run_pipeline_for_ticker(ticker, is_batch=False, timestamp=None, pre_fetched_yahoo=None, pre_fetched_fred=None):
    """Executes the prediction pipeline for a single ticker."""
    print(f"\n" + "-"*40, flush=True)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] SUB-PROCESS: Calculating model for {ticker}", flush=True)
    print(f"Model uses static universe: {len(ALL_TICKERS)} tickers.", flush=True)
    print("-"*40, flush=True)
    
    ticker_universe = sorted(list(set(ALL_TICKERS + [ticker])))
    
    try:
        # IMPORTANT: In batch mode we prevent data leakage and incomplete feature matrices!
        if pre_fetched_yahoo is not None:
            # 1. Check if the target ETF exists
            if ticker not in pre_fetched_yahoo.columns:
                raise ValueError(f"Target ETF {ticker} is missing in Yahoo Download (Delisted/Error).")
            
            # 2. Hard check if Yahoo Finance swallowed macro data!
            missing_macro = [t for t in ALL_TICKERS if t not in pre_fetched_yahoo.columns]
            if missing_macro:
                raise ValueError(f"CRITICAL: Yahoo Bulk-Download swallowed {len(missing_macro)} macro tickers (e.g. {missing_macro[0]}). Model matrix would be corrupt!")
            
            # Slicing: Only macro universe + this ONE target ETF
            available_tickers = [t for t in ticker_universe if t in pre_fetched_yahoo.columns]
            sliced_yahoo = pre_fetched_yahoo[available_tickers].copy()
        else:
            sliced_yahoo = None

        # Prepare data
        X_train_scaled, y_train, X_live_scaled = load_and_prepare_data(
            target_ticker=ticker,
            all_tickers=ticker_universe,
            start_date=START_DATE,
            end_date=END_DATE,
            forecast_horizon=FORECAST_HORIZON_DAYS,
            pre_fetched_yahoo=sliced_yahoo,
            pre_fetched_fred=pre_fetched_fred
        )
        
        # In batch mode we suppress the timestamp to avoid generating hundreds of markdown reports
        report_timestamp = None if is_batch else timestamp
        
        results = perform_feature_selection(
            X_scaled=X_train_scaled,
            y=y_train,
            latest_features_scaled=X_live_scaled,
            target_etf=ticker,
            horizon=FORECAST_HORIZON_DAYS,
            timestamp=report_timestamp
        )
        
        class_mapping = {-1: "Down", 0: "Flat", 1: "Up"}
        response = {
            "ticker": ticker,
            "status": "Success",
            "prediction_class": int(results["prediction"]),
            "prediction_label": class_mapping.get(results["prediction"], "Unknown"),
            "prob_down": float(results["probabilities"].get(-1, 0.0)),
            "prob_flat": float(results["probabilities"].get(0, 0.0)),
            "prob_up": float(results["probabilities"].get(1, 0.0)),
            "cv_accuracy": float(results["cv_accuracy"]),
            "quality_gate_passed": bool(results["is_valid_quality"]),
            "ks_cutoff": float(results["ks_cutoff"]),
            
            # Transparent output of the model drivers for the batch JSON
            "selected_features": results.get("selected_features", []),
            "feature_weights": results.get("feature_weights", {})
        }
        
        # For Streamlit and single executions we return the complete model & graphics
        # For Streamlit and single executions we return the complete model & graphics
        if not is_batch:
            response["raw_results"] = results
            
            # =========================================================================
            # ARTIFACT EXPORT FOR ERROR ANALYSIS & PLAUSIBILITY (Single mode only)
            # =========================================================================
            try:
                project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                artifacts_dir = os.path.join(project_root, 'artifacts')
                os.makedirs(artifacts_dir, exist_ok=True)
                
                safe_ts = timestamp if timestamp else datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # 1. Training Matrix (Full feature space before selection + target vector)
                # On this basis, the algorithm performs the initial variable selection.
                df_train = X_train_scaled.copy()
                df_train['TARGET_CLASS'] = y_train
                df_train.to_csv(os.path.join(artifacts_dir, f"{ticker}_1_train_full_{safe_ts}.csv"))
                
                # 2. CV Matrix (Only the final selected features + target vector)
                # This matrix uses TimeSeriesSplit cross-validation and final model fitting.
                df_cv = results["X_optimal"].copy()
                df_cv['TARGET_CLASS'] = y_train
                df_cv.to_csv(os.path.join(artifacts_dir, f"{ticker}_2_cv_optimal_{safe_ts}.csv"))
                
                # 3. Predict Matrix (The isolated live data point for the current prediction)
                # Reduced to exactly the features that the finished model expects.
                selected_features = results["selected_features"]
                df_predict = X_live_scaled[selected_features].copy()
                df_predict.to_csv(os.path.join(artifacts_dir, f"{ticker}_3_predict_live_{safe_ts}.csv"))
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] ARTIFACTS: 3 diagnostic matrices exported to /artifacts.", flush=True)
            except Exception as e:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] ERROR during artifact export: {e}", flush=True)
            # =========================================================================

        return response
        
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ERROR for Ticker {ticker}: {e}", flush=True)
        return {"ticker": ticker, "status": "Failed", "error": str(e)}

def execute_batch_processing(runner_id, total_runners):
    """Downloads raw data for the assigned slice and processes the ETFs in a memory-efficient way."""
    
    # === ANTI API-BAN JITTER ===
    sleep_time = random.uniform(1.0, 180.0)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Runner {runner_id}/{total_runners} waiting {sleep_time:.1f} seconds (Anti-429 Jitter)...", flush=True)
    time.sleep(sleep_time)
    # =========================================

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    batch_config_path = os.path.join(project_root, 'config', 'batch_targets.json')
    
    if not os.path.exists(batch_config_path):
        raise FileNotFoundError(f"Batch configuration missing. Please run scripts/build_etf_batch.py first.")
        
    with open(batch_config_path, 'r') as f:
        batch_config = json.load(f)
        
    all_tickers = batch_config.get("tickers", [])
    
    # --- SLICING LOGIC FOR DISTRIBUTED COMPUTE ---
    chunk_size = math.ceil(len(all_tickers) / total_runners)
    start_idx = (runner_id - 1) * chunk_size
    end_idx = start_idx + chunk_size
    my_tickers = all_tickers[start_idx:end_idx]
    
    print(f"\n" + "="*60, flush=True)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] BATCH GLOBAL INITIALIZATION", flush=True)
    print(f"RUNNER ID: {runner_id}/{total_runners}", flush=True)
    print(f"Processing block from index {start_idx} to {end_idx-1} ({len(my_tickers)} ETFs)", flush=True)
    print("="*60, flush=True)
    
    if not my_tickers:
        print("No ETFs left for this runner. Terminating process.", flush=True)
        return

    # Merging the global macro universe ONLY with the ETFs of this specific runner
    global_ticker_universe = list(set(ALL_TICKERS + my_tickers))
    
    # The only two network requests of the entire batch run for this runner
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] MASTER-FETCH: Loading prices from Yahoo Finance ({len(global_ticker_universe)} tickers)...", flush=True)
    global_raw_yahoo = yf.download(global_ticker_universe, start=START_DATE, end=END_DATE)['Close']
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] MASTER-FETCH: Loading macroeconomic series from FRED...", flush=True)
    global_raw_fred = fetch_and_lag_fred_data(START_DATE, END_DATE)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Master download complete. Switching to local computation mode...", flush=True)
    
    batch_results = {
        "execution_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_processed": len(my_tickers),
        "baseline_parameters": {
            "annual_inflation_rate": ANNUAL_INFLATION_RATE,
            "annual_margin_up": ANNUAL_MARGIN_UP,
            "annual_margin_down": ANNUAL_MARGIN_DOWN,
            "forecast_horizon_days": FORECAST_HORIZON_DAYS
        },
        "results": []
    }
    
    # Loop now operates purely locally in memory
    for idx, ticker in enumerate(my_tickers, 1):
        print(f"\nProgress Runner {runner_id}: {idx}/{len(my_tickers)}", flush=True)
        res = run_pipeline_for_ticker(
            ticker=ticker, 
            is_batch=True, 
            pre_fetched_yahoo=global_raw_yahoo, 
            pre_fetched_fred=global_raw_fred
        )
        batch_results["results"].append(res)
        
    # Persist JSON results specifically for this runner
    output_dir = os.path.join(project_root, 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f'batch_results_runner_{runner_id}.json')
    
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(batch_results, f, indent=4)
        
    print(f"\n" + "="*60, flush=True)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] BATCH COMPLETE (Runner {runner_id}).", flush=True)
    print(f"Results successfully saved at: {output_file_path}", flush=True)
    print("="*60, flush=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETF Predictor Pipeline Orchestrator")
    parser.add_argument("--batch", action="store_true", help="Executes the pipeline in batch mode")
    parser.add_argument("--ticker", type=str, help="Single run for a specific ticker")
    parser.add_argument("--runner-id", type=int, default=1, help="The ID of the current runner (1-based)")
    parser.add_argument("--total-runners", type=int, default=1, help="The total number of deployed runners")
    
    args = parser.parse_args()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if args.batch:
        execute_batch_processing(args.runner_id, args.total_runners)
    else:
        chosen_ticker = args.ticker if args.ticker else TARGET_ETF
        run_pipeline_for_ticker(chosen_ticker, is_batch=False, timestamp=timestamp)