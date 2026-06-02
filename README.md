# ETF Predictor

This repository contains a machine learning pipeline to forecast the medium-term market development of a target ETF. The model classifies the future market state into three discrete classes: **Up**, **Down**, and **Flat**. The statistical foundation is a Multinomial Logistic Regression (Softmax).

**ETF Batch Analysis Dashboard:** [![ETF Quant Engine](https://img.shields.io/badge/Launch-Interactive_Dashboard-2ea44f?style=for-the-badge&logo=html5)](https://kleinnconrad.github.io/etf-predictor/)

**ETF Single Mode Webservice:** [![ETF Quant Engine](https://img.shields.io/badge/Launch-Interactive_Dashboard-2ea44f?style=for-the-badge&logo=html5)](https://etf-predictor-production.up.railway.app)

## Motivation for ETF forecasting

I specifically chose to forecast macro ETFs rather than individual equities, futures, or crypto assets for the following reasons:

* **Superior Signal-to-Noise Ratio:** Individual stocks are highly vulnerable to idiosyncratic risks (earnings misses, management scandals, lawsuits) which are statistically unpredictable for retail investors. ETFs represent a broad cross-section of assets, naturally smoothing out these singular shocks. What remains is systemic market movement, which can be far more reliably modeled using macroeconomic indicators.
* **Classification over Exact Pricing:** Predicting exact future asset prices (regression) is notoriously prone to overfitting and noise. This pipeline embraces the reality of available retail data by focusing purely on market regime classification (**Up, Down, Flat**). This creates a fundamentally more robust and honest prediction model.
* **A Different Playing Field:** While the open-source and retail algo-trading space is heavily saturated with volatile day-trading bots for crypto and single stocks, systematic macroeconomic ETF rotation remains an underserved niche. This project aims to provide a stable, long-term analytical tool rather than a high-frequency trading gamble.

## Table of Contents

- [Model Architecture](#model-architecture)
  - [1. Feature Engineering, Interaction Effects & Variable Transformation](#1-feature-engineering-interaction-effects--variable-transformation)
  - [2. Dynamic Target Classification](#2-dynamic-target-classification)
  - [3. Two-Stage Feature Selection](#3-two-stage-feature-selection)
  - [4. Evaluation (TimeSeries Split)](#4-evaluation-timeseries-split)
  - [5. Combating Base Rate Bias (Logarithmic Class Smoothing)](#5-combating-base-rate-bias-logarithmic-class-smoothing)
- [Risk Management & Model Safeguards](#risk-management--model-safeguards)
  - [1. Quality Gate (Out-of-Fold Evaluation)](#1-quality-gate-out-of-fold-evaluation)
  - [2. KS Statistic Cutoff Optimization (Crash Sensor)](#2-ks-statistic-cutoff-optimization-crash-sensor)
  - [3. Dual Cut Off Logic](#3-dual-cut-off-logic)
- [Automated Economic Interpretation (LLM)](#automated-economic-interpretation-llm)
- [Configuration (`config.py`)](#configuration-configpy)
- [Data Source & Macro Universe](#data-source--macro-universe)
- [Target ETF List](#target-etf-list)
- [Automated Batch Processing](#automated-batch-processing)
- [Execution (Local & Development)](#execution-local--development)
- [Cloud Deployment (Docker & Railway)](#cloud-deployment-docker--railway)

---

## Model Architecture

The pipeline addresses typical financial time series modeling issues, specifically multicollinearity and high dimensionality, through a multi-stage architecture.

### 1. Feature Engineering, Interaction Effects & Variable Transformation

The model does not process absolute stock prices. The raw data undergoes a multi-stage transformation prior to modeling:

* **Raw Data Ingestion:** The pipeline retrieves the adjusted closing prices and macroeconomic indicators up to the current date.
* **Deterministic Interaction Effects:** Instead of relying on brute-force polynomial features that introduce noise, the pipeline engineers specific economic ratios (e.g., Copper/Gold for growth vs. inflation, HYG/LQD for credit stress, SPY/TLT for risk appetite). This translates absolute prices into transparent, systemic market spreads.
* **Rolling Momentum:** Absolute prices and ratios are converted into rolling percentage returns (`pct_change`) representing short- and medium-term momentum (1 month/21 days, 3 months/63 days, and 6 months/126 days). This ensures mathematical stationarity.
* **Outlier Treatment (Winsorization):** Financial markets exhibit "fat tails." To prevent extreme market anomalies from causing "feature squashing" during normalization, variables are clipped at the 1st and 99th percentiles. Crucially, these thresholds are derived *exclusively* from the training set to prevent lookahead bias, and then applied identically to the live prediction row.
* **Z-Score Normalization:** To prevent scale effects in the logistic regression, the clipped rolling returns are transformed into Z-scores using a `StandardScaler`. The final input variables measure the distance of a return from its 10-year mean in standard deviations.

### 2. Dynamic Target Classification

Return classification is based on macroeconomic assumptions scaled to the forecast horizon:

* **Economic Baseline:** The model applies an assumed base inflation rate (e.g., 2.5% p.a.) and a tolerance corridor of (e.g. -0.1% for down and +7.5% for up and flat else).
* **Scaling:** These annualized values are linearly scaled to the forecast horizon (e.g., 126 trading days). 
* **Logic:** A future return exceeding the upper threshold is classified as `Up` (1). A return below the lower threshold is `Down` (-1). A return within the corridor is classified as `Flat` (0).

### 3. Two-Stage Feature Selection

Predictor selection is performed in two steps to ensure model stability:

* **Filter Stage:** Uses a univariate ANOVA F-test (`SelectKBest`) to reduce the feature space to the 80 strongest predictors. This eliminates variables with low significance to limit the computational load. 
* **Wrapper Stage:** Employs Sequential Feature Selection (`SequentialFeatureSelector`) with 5-fold cross-validation to identify the optimal subset (default: 12 features) from the remaining variables, systematically stripping out multicollinearity.

### 4. Evaluation (TimeSeries Split)

* Out-of-sample evaluation utilizes a `TimeSeriesSplit`. 
* The `gap` parameter equals the forecast horizon. This strictly prevents data leakage caused by overlapping return windows between historical training batches and test data.

### 5. Combating Base Rate Bias (Logarithmic Class Smoothing)

Forecasting broad market indices is complicated by historical upward trends, known as base rate bias. Uncorrected models often favor the `Up` class due to asymmetric class distribution. Linear weight corrections tend to overcompensate, increasing false positive rates. 

The pipeline calculates dynamic class weights based on logarithmic smoothing. The penalty weight ($W$) per class is calculated as:

$$W_{class} = \log_{10}\left(\frac{N_{majority}}{N_{class}}\right) + 1.0$$

* The majority class receives a base weight of 1.0. 
* Underrepresented classes receive logarithmically scaled, higher penalty weights. 
* This sensitizes the model to minority classes without generating excessive false alarms.

The calculated weights will be applied in the loss function:

$$Loss_{weighted} = - W_{y_{true}} \cdot \log(P(y_{true} \mid X))$$

---

## Risk Management & Model Safeguards

The pipeline integrates two statistical mechanisms to prevent overfitting and improve out-of-sample reliability.

### 1. Quality Gate (Out-of-Fold Evaluation)

Feature selection algorithms risk overfitting in large variable spaces. A model might perfectly fit historical data but fail on unseen data. 
* The model undergoes an Out-of-Fold (OOF) validation before issuing a final forecast. 
* The dataset is chronologically partitioned via a `TimeSeriesSplit`. The prediction accuracy on unseen data blocks is aggregated. 
* The quality gate requires a cross-validated accuracy exceeding a baseline threshold. Below this threshold, the forecast and artifact generation are blocked to prevent statistically insignificant signals from reaching production.

To rigorously prevent data leakage, the pipeline utilizes a `TimeSeriesSplit` with a dynamic **Purging Gap** (Embargo Zone). 

Because the forecast horizon predicts future market states (e.g., 126 trading days ahead), the target labels of the latest training rows intrinsically overlap with the features of the subsequent validation rows. To prevent the model from artificially "peeking" into the future during cross-validation, a strict embargo zone—exactly the size of the forecast horizon—is mathematically deleted between the training block and the validation block during every single fold.

The following graphic illustrates how the dataset (e.g., ~1,000 trading days) is chronologically partitioned across 5 folds. The validation set continuously rolls forward, while the embargo zone ensures absolute separation.

```text
Legend: 
[█] Training Data   [▒] Purging Gap (Embargo)   [▓] Validation Data   [·] Unused Future

Fold 1: ████▒▒▒▒▒▒▓▓▓▓▓▓▓▓································
Fold 2: ████████████▒▒▒▒▒▒▓▓▓▓▓▓▓▓························
Fold 3: ████████████████████▒▒▒▒▒▒▓▓▓▓▓▓▓▓················
Fold 4: ████████████████████████████▒▒▒▒▒▒▓▓▓▓▓▓▓▓········
Fold 5: ████████████████████████████████████▒▒▒▒▒▒▓▓▓▓▓▓▓▓
```

#### Exact Index Partitioning (Example: 1,000 Days, 126-Day Gap)

| Fold | Training Indices | Purging Gap (Deleted) | Validation Indices |
| :--- | :--- | :--- | :--- |
| **Fold 1** | `0 - 40` | `40 - 166` | `166 - 332` |
| **Fold 2** | `0 - 206` | `206 - 332` | `332 - 498` |
| **Fold 3** | `0 - 372` | `372 - 498` | `498 - 664` |
| **Fold 4** | `0 - 538` | `538 - 664` | `664 - 830` |
| **Fold 5** | `0 - 704` | `704 - 830` | `830 - 996` |

> **Note on Exported Matrices:** When exporting the matrices for debugging purposes, you will notice that both the training and the cross-validation matrix end on the exact same date (the end of the available history). This is mathematically correct: As seen in `Fold 5`, the final validation split evaluates the very last available historical sequence. Therefore, the full dataset must be present in memory to allow the sliding window to seamlessly reach the present day to conclude the out-of-sample testing.

### 2. KS Statistic Cutoff Optimization (Crash Sensor)

A logistic regression defaults to the class with the highest probability. This static threshold is inadequate for asymmetric risk profiles like market crashes. 
* The pipeline dynamically optimizes the trigger threshold for the `Down` class using the Kolmogorov-Smirnov (KS) statistic. 
* The KS statistic identifies the probability cutoff that maximizes the difference between the True Positive Rate (TPR) and the False Positive Rate (FPR). 
* **If the current crash probability exceeds this optimized cutoff, the model issues a `Down` warning, regardless of whether another class holds a higher absolute probability.**

### 3. Dual Cut off Logic

To address the inherent asymmetry in financial machine learning and properly classify periods of market indecision ("Flat" markets), the pipeline utilizes a Dual Cutoff approach during the final prediction phase.

**Down-Marge (derived from KS)**
* **What it does:** Acts as an emergency brake. If the predicted probability for a market downturn (`prob_down`) exceeds this threshold, the model forcefully outputs a `-1` (Down) signal, regardless of the other probabilities.
* **Where it is set:** This threshold is **dynamic**. It is calculated datadriven during each run in `src/modeling.py` using the Kolmogorov-Smirnov (KS) statistic on the Out-of-Fold (OOF) cross-validation data. It optimizes the threshold to best separate historical market crashes from false alarms.

**Up-Marge (user constant)**
* **What it does:** Prevents the model from over-predicting bull markets. Due to the smoothing of class weights, the model inherently favors extreme predictions over neutral ones. The Up-Marge demands a high level of conviction (e.g., >65% probability) before the model is allowed to output a `1` (Up) signal. If neither the Down-Marge nor the Up-Marge is breached, the model defaults to `0` (Flat).
* **Where it is set:** This parameter is set in the `modeling.py`. Look for `up_cutoff_value`.

---
**START:** The machine learning model provides probabilities for the three classes (-1, 0, 1).
---

### Step 1: Check Downside Risk (Decision Node 1)
**Is `prob_down` >= `optimal_down_threshold` (KS cutoff)?**

* **YES:** -> **[ SIGNAL: DOWN (-1) ]** *(The process ends here. The risk is too high.)*

* **NO:** *(The downside risk is low. Proceed to Step 2.)*

---

### Step 2: Check Upside Potential (Decision Node 2)
**Is `prob_up` >= `up_cutoff_value=0.65`?**

* **YES:** -> **[ SIGNAL: UP (1) ]** *(The process ends here. High conviction for a rally.)*

* **NO:** *(No extreme signal detected.)*
  -> **[ SIGNAL: FLAT (0) ]** *(The market is trending sideways or the signals are unclear.)*

---
**Priority Rule:** The down cutoff is *always* checked first.

## Automated Economic Interpretation (LLM)

The pipeline integrates the Google Gemini API to provide an economic rationale for the selected predictors. 
* After identifying the top variables, the resulting coefficient matrix is passed to the LLM. 
* The model interprets economic relationships, such as sector dependencies or inverse correlations, and appends a quantitative analysis to the output report. 
* The API request includes an automatic retry mechanism to handle rate limits (HTTP 429) or server overloads (HTTP 503). 
* The API key is dynamically loaded from the `GEMINI_API_KEY` environment variable.

---

## Configuration (`config.py`)

Hyperparameters and economic assumptions are managed in `src/config.py`.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `TARGET_ETF` | `str` | Ticker symbol of the target ETF (e.g., `'SPY'`). |
| `FORECAST_HORIZON_DAYS` | `int` | Forecast horizon in trading days (e.g., `126`). Defines the CV gap. |
| `ANNUAL_INFLATION_RATE` | `float` | Assumed annual inflation rate (e.g., `0.025`). |
| `ANNUAL_MARGIN` | `float` | Tolerance corridor around the baseline (e.g., `0.01`). |
| `START_DATE` / `END_DATE` | `str` | Historical training period boundaries. |

---

## Data Source & Macro Universe

Training a model on highly correlated equities causes multicollinearity, providing redundant signals and leading to overfitting. The pipeline mitigates this by utilizing a macro-proxy universe. The configuration curates approximately 50 distinct assets and economic indicators representing orthogonal economic factors:

* **Cost of Capital:** Treasury Yields, VIX, US Dollar Index.
* **Credit Risk:** High Yield Corporate Bonds, Long-Term Treasuries, Sovereign Yield ETFs.
* **Market Inflation Indicators:** Crude Oil, Copper, Agricultural Commodities.
* **Sector Rotation:** Cyclical vs. defensive ETFs.
* **Alternative Liquidity:** Bitcoin.
* **Systemic Equities:** Global leading corporations across US, EU, UK, and JP markets.
* **Hard Macroeconomics (FRED):** Realized inflation (CPI), employment metrics (Nonfarm Payrolls, Unemployment Rate), systemic liquidity (Central Bank Assets), and leading recessionary indicators (10Y-2Y Treasury Spread) across major industrial nations.

To prevent lookahead bias, **FRED economic data** is structurally shifted forward by a 30-day publication lag before merging with the daily trading calendar. The pipeline calculates the 1-month, 3-month, and 6-month momentum for these combined base assets and economic indicators, yielding a final training matrix of approximately 150 distinct macroeconomic variables.

---

## Target ETF List

**1. The Foundation: Xetra T7 Dump**
The process begins with the official "T7 All Tradable Instruments" CSV export from the Frankfurt Stock Exchange (Xetra). This provides a complete, unadulterated snapshot of the European market.

**2. Seed Extraction (`scripts/generate_seed.py`)**
This script parses the raw T7 dump, isolating only ETFs and ETCs actively traded in Euro (EUR). It automatically maps the official exchange mnemonics (e.g., `SXR8`) to their corresponding Yahoo Finance tickers by appending the Xetra suffix (e.g., `SXR8.DE`). The output is a comprehensive master list of approximately 3,000 European tickers (`config/all_etfs_seed.txt`).

**3. Institutional Filtering (`scripts/build_etf_batch.py`)**
To separate high-quality assets from illiquid or newly launched funds, this script deploys a rate-limited, multithreaded engine to evaluate all ~3,000 tickers via the Yahoo Finance API against strict institutional criteria:
* **Minimum History (10 Years):** Ensures the model has sufficient data points (~1,250 trading days) to identify statistically significant patterns, while specifically capturing the current macroeconomic regime (interest rates, inflation).
* **High Liquidity (> €1M Daily Turnover):** Evaluates the *actual traded volume in Euro* (Volume × Close Price), strictly filtering out illiquid assets to guarantee real-world tradeability without severe spread slippage.

The surviving universe (typically 200–400 premium UCITS ETFs) is finally compiled into `config/batch_targets.json`. This file serves as the definitive, dynamic target list for the automated GitHub Actions ML pipeline.

---

## Automated Batch Processing

The pipeline supports an automated batch execution mode for processing large universes of ETFs sequentially.

* **Intelligent Target Selection:** The script `scripts/build_etf_batch.py` curates the target universe. It filters a pre-defined multi-asset seed list based on strict institutional criteria: minimum historical age (10 years) to ensure full Z-score scaling validity, and a minimum average daily volume (ADV) threshold to guarantee liquidity and prevent pricing gaps.
* **Orchestration (`src/main.py --batch`):** The orchestrator manages the execution loop for the 200 validated targets. 
* **Resource Efficiency:** To prevent API rate-limiting and maximize execution speed, the orchestrator performs a single, global pre-fetch of all required Yahoo Finance pricing data and FRED macroeconomic indicators before initiating the local, memory-bound computation loop.
* **Cloud Infrastructure (GitHub Actions):** The repository includes a serverless CI/CD workflow (`.github/workflows/manual_batch.yml`) for remote execution. The workload is horizontally distributed across **3 parallel runners** to reduce wall-clock execution time. To maintain strict control over API rate limits and compute budgets, this workflow is triggered manually. Upon completion, a final merge job aggregates the distributed results and commits them directly back to the repository.
* **Data Persistence:** The batch runner aggregates the core metrics (prediction class, probabilities, KS-cutoff, and Out-of-Fold accuracy) for all processed targets and persists them as a structured array in the `artifacts/latest_batch_results.json` file. This file is overwritten upon each execution, providing a clean, point-in-time interface for downstream algorithmic rebalancing or database ingestion.

## Execution (Local & Development)

The repository is configured for GitHub Codespaces. 
* Dependencies install automatically via the `.devcontainer/devcontainer.json` configuration. 
* The pipeline is executed via the `python src/main.py` command. 
* It generates artifacts in the `/output` directory: a visual confusion matrix evaluation (`.png`), the cleaned historical dataset (`.csv`), and a statistical documentation report (`.md`) including predictor ranking and the LLM interpretation.

---

## Cloud Deployment (Docker & Railway)

The model is deployed as a web service using Streamlit, Docker, and Railway.app. 
* The `Dockerfile` handles system dependencies and exposes port 8501. 
* Deployment is automated via GitHub integration on Railway. 
* The `GEMINI_API_KEY` and `PORT` environment variables must be configured securely in the Railway dashboard. 
* The deployed application fetches live data and generates macroeconomic forecasts upon user request.

[yahoo-finance-etf-overview](https://de.finance.yahoo.com/m%C3%A4rkte/etfs/top-performer/)

[FRED-API](https://fred.stlouisfed.org/docs/api/fred/)

Copyright (c) 2026 Conrad Kleinn. Alle Rechte vorbehalten. / All rights reserved.
