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

from config import TARGET_ETF, ALL_TICKERS, START_DATE, END_DATE, FORECAST_HORIZON_DAYS
from data_pipeline import load_and_prepare_data, fetch_and_lag_fred_data
from modeling import perform_feature_selection

def run_pipeline_for_ticker(ticker, is_batch=False, timestamp=None, pre_fetched_yahoo=None, pre_fetched_fred=None):
    """Führt die Vorhersage-Pipeline für einen einzelnen Ticker aus."""
    print(f"\n" + "-"*40)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] SUB-PROCESS: Berechne Modell für {ticker}")
    print("-"*40)
    
    ticker_universe = list(set(ALL_TICKERS + [ticker]))
    
    try:
        # WICHTIG: Im Batch-Modus verhindern wir Data-Leakage! 
        # Das Modell darf die anderen Ziel-ETFs nicht als Features sehen.
        if pre_fetched_yahoo is not None:
            if ticker not in pre_fetched_yahoo.columns:
                raise ValueError(f"Target ETF {ticker} konnte von Yahoo Finance nicht heruntergeladen werden (Delisted/Fehler).")
            
            # Slicing: Nur Makro-Universum + dieser EINE Ziel-ETF
            available_tickers = [t for t in ticker_universe if t in pre_fetched_yahoo.columns]
            sliced_yahoo = pre_fetched_yahoo[available_tickers].copy()
        else:
            sliced_yahoo = None

        # Daten vorbereiten
        X_train_scaled, y_train, X_live_scaled = load_and_prepare_data(
            target_ticker=ticker,
            all_tickers=ticker_universe,
            start_date=START_DATE,
            end_date=END_DATE,
            forecast_horizon=FORECAST_HORIZON_DAYS,
            pre_fetched_yahoo=sliced_yahoo,
            pre_fetched_fred=pre_fetched_fred
        )
        
        # Im Batch-Modus unterdrücken wir den Timestamp, um keine hunderten Markdown-Reports zu generieren
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
            "ks_cutoff": float(results["ks_cutoff"])
        }
        
        # Für Streamlit und Einzel-Ausführungen geben wir das komplette Modell & Grafiken zurück
        if not is_batch:
            response["raw_results"] = results
            
        return response
        
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ERROR bei Ticker {ticker}: {e}")
        return {"ticker": ticker, "status": "Failed", "error": str(e)}

def execute_batch_processing(runner_id, total_runners):
    """Downloadet Rohdaten für den zugeteilten Slice und verarbeitet die ETFs speicherschonend."""
    
    # === ANTI API-BAN JITTER FÜR 20 RUNNER ===
    # Wir verteilen die 20 Server jetzt über 3 Minuten (180s), um FRED und Yahoo zu schonen
    sleep_time = random.uniform(1.0, 180.0)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Runner {runner_id}/{total_runners} wartet {sleep_time:.1f} Sekunden (Anti-429 Jitter)...")
    time.sleep(sleep_time)
    # =========================================

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    batch_config_path = os.path.join(project_root, 'config', 'batch_targets.json')
    
    if not os.path.exists(batch_config_path):
        raise FileNotFoundError(f"Batch-Konfiguration fehlt. Bitte vorher scripts/build_etf_batch.py ausführen.")
        
    with open(batch_config_path, 'r') as f:
        batch_config = json.load(f)
        
    all_tickers = batch_config.get("tickers", [])
    
    # --- SLICING LOGIK FÜR DISTRIBUTED COMPUTE ---
    chunk_size = math.ceil(len(all_tickers) / total_runners)
    start_idx = (runner_id - 1) * chunk_size
    end_idx = start_idx + chunk_size
    my_tickers = all_tickers[start_idx:end_idx]
    
    print(f"\n" + "="*60)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] BATCH GLOBAL INITIALIZATION")
    print(f"RUNNER ID: {runner_id}/{total_runners}")
    print(f"Verarbeite Block von Index {start_idx} bis {end_idx-1} ({len(my_tickers)} ETFs)")
    print("="*60)
    
    if not my_tickers:
        print("Keine ETFs für diesen Runner übrig. Beende Prozess.")
        return

    # Zusammenführen des globalen Macro-Universums NUR mit den ETFs dieses spezifischen Runners
    global_ticker_universe = list(set(ALL_TICKERS + my_tickers))
    
    # Die zwei einzigen Netzwerk-Anfragen des gesamten Batch-Laufs für diesen Runner
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] MASTER-FETCH: Lade Kurse von Yahoo Finance ({len(global_ticker_universe)} Ticker)...")
    global_raw_yahoo = yf.download(global_ticker_universe, start=START_DATE, end=END_DATE)['Close']
    
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] MASTER-FETCH: Lade makroökonomische Reihen von FRED...")
    global_raw_fred = fetch_and_lag_fred_data(START_DATE, END_DATE)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Master-Download abgeschlossen. Wechsel in lokalen Berechnungsmodus...")
    
    batch_results = {
        "execution_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_processed": len(my_tickers),
        "results": []
    }
    
    # Schleife operiert nun rein lokal im Arbeitsspeicher
    for idx, ticker in enumerate(my_tickers, 1):
        print(f"\nFortschritt Runner {runner_id}: {idx}/{len(my_tickers)}")
        res = run_pipeline_for_ticker(
            ticker=ticker, 
            is_batch=True, 
            pre_fetched_yahoo=global_raw_yahoo, 
            pre_fetched_fred=global_raw_fred
        )
        batch_results["results"].append(res)
        
    # JSON-Ergebnisse spezifisch für diesen Runner persistieren
    output_dir = os.path.join(project_root, 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f'batch_results_runner_{runner_id}.json')
    
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(batch_results, f, indent=4)
        
    print(f"\n" + "="*60)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] BATCH COMPLETE (Runner {runner_id}).")
    print(f"Ergebnisse erfolgreich gespeichert unter: {output_file_path}")
    print("="*60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETF Predictor Pipeline Orchestrator")
    parser.add_argument("--batch", action="store_true", help="Führt die Pipeline im Batch-Modus aus")
    parser.add_argument("--ticker", type=str, help="Single-Run für einen spezifischen Ticker")
    parser.add_argument("--runner-id", type=int, default=1, help="Die ID des aktuellen Runners (1-basiert)")
    parser.add_argument("--total-runners", type=int, default=1, help="Die Gesamtzahl der eingesetzten Runner")
    
    args = parser.parse_args()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if args.batch:
        execute_batch_processing(args.runner_id, args.total_runners)
    else:
        chosen_ticker = args.ticker if args.ticker else TARGET_ETF
        run_pipeline_for_ticker(chosen_ticker, is_batch=False, timestamp=timestamp)