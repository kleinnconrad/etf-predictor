# ETF Predictor

This repository contains a machine learning pipeline to forecast the medium-term market development of a target ETF (default: SPY). The model classifies the future market state into three discrete classes: **Up**, **Down**, and **Flat**. The statistical foundation is a Multinomial Logistic Regression (One-vs-Rest).

## Table of Contents

- [Model Architecture](#model-architecture)
  - [1. Feature Engineering & Variable Transformation](#1-feature-engineering--variable-transformation)
  - [2. Dynamic Target Classification](#2-dynamic-target-classification)
  - [3. Two-Stage Feature Selection](#3-two-stage-feature-selection)
  - [4. Evaluation (TimeSeries Split)](#4-evaluation-timeseries-split)
  - [5. Combating Base Rate Bias (Logarithmic Class Smoothing)](#5-combating-base-rate-bias-logarithmic-class-smoothing)
- [Risk Management & Model Safeguards](#6-risk-management--model-safeguards)
  - [1. Quality Gate (Out-of-Fold Evaluation)](#61-quality-gate-out-of-fold-evaluation)
  - [2. KS Statistic Cutoff Optimization (Crash Sensor)](#62-ks-statistic-cutoff-optimization-crash-sensor)
- [Automated Economic Interpretation (LLM)](#automated-economic-interpretation-llm)
- [Configuration (`config.py`)](#configuration-configpy)
- [Data Source & Macro Universe](#data-source--macro-universe)
- [Execution (Local & Development)](#execution-local--development)
- [Cloud Deployment (Docker & Railway)](#cloud-deployment-docker--railway)

---

## Model Architecture

The pipeline addresses typical financial time series modeling issues, specifically multicollinearity and high dimensionality, through a multi-stage architecture.

### 1. Feature Engineering & Variable Transformation

The model does not process absolute stock prices. The raw data undergoes a three-stage transformation prior to modeling. First, the pipeline retrieves the adjusted closing prices of all defined tickers up to the current date. Second, absolute prices are converted into rolling percentage returns (`pct_change`) representing short- and medium-term momentum (1 month/21 days, 3 months/63 days, and 6 months/126 days). Third, to prevent scale effects in the logistic regression, rolling returns are transformed into Z-scores using a `StandardScaler` fitted exclusively on historical training data. The final input variables measure the distance of a return from its 10-year mean in standard deviations.

### 2. Dynamic Target Classification

Return classification is based on macroeconomic assumptions scaled to the forecast horizon. The model applies an assumed base inflation rate (e.g., 2.5% p.a.) and a tolerance corridor (e.g., +/- 1.0% p.a.). These annualized values are linearly scaled to the forecast horizon (e.g., 126 trading days). The classification logic dictates that a future return exceeding the upper threshold is classified as `Up` (1). A return below the lower threshold is `Down` (-1). A return within the corridor is classified as `Flat` (0).

### 3. Two-Stage Feature Selection

Predictor selection is performed in two steps to ensure model stability. The filter stage uses a univariate ANOVA F-test (`SelectKBest`) to reduce the feature space to the 80 strongest predictors. This eliminates variables with low significance to limit the computational load. The wrapper stage employs Sequential Feature Selection (`SequentialFeatureSelector`) with 3-fold cross-validation to identify the optimal subset (default: 8 features) from the remaining variables, reducing multicollinearity.

### 4. Evaluation (TimeSeries Split)

Out-of-sample evaluation utilizes a `TimeSeriesSplit`. The `gap` parameter equals the forecast horizon. This prevents data leakage caused by overlapping return windows between training and test data.

### 5. Combating Base Rate Bias (Logarithmic Class Smoothing)

Forecasting broad market indices is complicated by historical upward trends, known as base rate bias. Uncorrected models often favor the `Up` class due to asymmetric class distribution. Linear weight corrections tend to overcompensate, increasing false positive rates. The pipeline calculates dynamic class weights based on logarithmic smoothing. The penalty weight ($W$) per class is calculated as:

$$W_{class} = \log_{10}\left(\frac{N_{majority}}{N_{class}}\right) + 1.0$$

This function dampens statistical outliers in weighting. The majority class receives a base weight of 1.0. Underrepresented classes receive logarithmically scaled, higher penalty weights. This sensitizes the model to minority classes without generating excessive false alarms.

## Risk Management & Model Safeguards

The pipeline integrates two statistical mechanisms to prevent overfitting and improve out-of-sample reliability.

### 1. Quality Gate (Out-of-Fold Evaluation)

Feature selection algorithms risk overfitting in large variable spaces. A model might perfectly fit historical data but fail on unseen data. The model undergoes an Out-of-Fold (OOF) validation before issuing a final forecast. The dataset is chronologically partitioned via a `TimeSeriesSplit`. The prediction accuracy on unseen data blocks is aggregated. The quality gate requires a cross-validated accuracy exceeding 35%. Below this threshold, the model offers no significant advantage over random classification, and the forecast is blocked to prevent statistically insignificant signals.

### 2. KS Statistic Cutoff Optimization (Crash Sensor)

A logistic regression defaults to the class with the highest probability. This static threshold is inadequate for asymmetric risk profiles like market crashes. The pipeline dynamically optimizes the trigger threshold for the `Down` class using the Kolmogorov-Smirnov (KS) statistic. The KS statistic identifies the probability cutoff that maximizes the difference between the True Positive Rate (TPR) and the False Positive Rate (FPR). This data-driven cutoff becomes the new threshold for the `Down` signal. If the current crash probability exceeds this optimized cutoff, the model issues a `Down` warning, regardless of whether another class holds a higher absolute probability.

## Automated Economic Interpretation (LLM)

The pipeline integrates the Google Gemini API to provide an economic rationale for the selected predictors. After identifying the top variables, the resulting coefficient matrix is passed to the LLM. The model interprets economic relationships, such as sector dependencies or inverse correlations, and appends a quantitative analysis to the output report. The API request includes an automatic retry mechanism to handle rate limits (HTTP 429) or server overloads (HTTP 503). The API key is dynamically loaded from the `GEMINI_API_KEY` environment variable.

## Configuration (`config.py`)

Hyperparameters and economic assumptions are managed in `src/config.py`.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `TARGET_ETF` | `str` | Ticker symbol of the target ETF (e.g., `'SPY'`). |
| `FORECAST_HORIZON_DAYS` | `int` | Forecast horizon in trading days (e.g., `126`). Defines the CV gap. |
| `ANNUAL_INFLATION_RATE` | `float` | Assumed annual inflation rate (e.g., `0.025`). |
| `ANNUAL_MARGIN` | `float` | Tolerance corridor around the baseline (e.g., `0.01`). |
| `START_DATE` / `END_DATE` | `str` | Historical training period boundaries. |

## Data Source & Macro Universe

Historical adjusted closing prices are fetched via the Yahoo Finance API (`yfinance`). Training a model on highly correlated equities causes multicollinearity, providing redundant signals and leading to overfitting. The pipeline mitigates this by utilizing a macro-proxy universe. The configuration curates approximately 50 distinct assets representing orthogonal economic factors. These include cost of capital (Treasury Yields, VIX, US Dollar Index), credit risk (High Yield Corporate Bonds, Long-Term Treasuries), inflation indicators (Crude Oil, Copper, Agricultural Commodities), sector rotation (cyclical vs. defensive ETFs), alternative liquidity (Bitcoin), and global systemic equities. The pipeline calculates the 1-month, 3-month, and 6-month momentum for these base assets, yielding a matrix of approximately 150 distinct macroeconomic variables.

## Execution (Local & Development)

The repository is configured for GitHub Codespaces. Dependencies install automatically via the `.devcontainer/devcontainer.json` configuration. The pipeline is executed via the `python src/main.py` command. It generates three artifacts in the `/output` directory: a visual confusion matrix evaluation (`.png`), the cleaned historical dataset (`.csv`), and a statistical documentation report (`.md`) including predictor ranking and the LLM interpretation.

## Cloud Deployment (Docker & Railway)

The model is deployed as a web service using Streamlit, Docker, and Railway.app. The `Dockerfile` handles system dependencies and exposes port 8501. Deployment is automated via GitHub integration on Railway. The `GEMINI_API_KEY` and `PORT` environment variables must be configured securely in the Railway dashboard. The deployed application fetches live data and generates macroeconomic forecasts upon user request.

[etf-predictor-web-service](https://etf-predictor-production.up.railway.app)

[yahoo-finance-etf-overview](https://de.finance.yahoo.com/m%C3%A4rkte/etfs/top-performer/)

Copyright (c) 2026 Conrad Kleinn. Alle Rechte vorbehalten. / All rights reserved.
