# ETF Predictor

This repository contains a machine learning pipeline to predict the medium-term market development of a target ETF (default: SPY).

The model classifies the future market state into three discrete classes: **Up**, **Down**, and **Flat**. The statistical pipeline is based on Multinomial Logistic Regression (One-vs-Rest).

## Table of Contents

- [Model Architecture](#model-architecture)
  - [1. Feature Engineering & Variable Transformation](#1-feature-engineering--variable-transformation)
  - [2. Dynamic Target Classification](#2-dynamic-target-classification)
  - [3. Two-Stage Feature Selection](#3-two-stage-feature-selection)
  - [4. Evaluation (TimeSeries Split)](#4-evaluation-timeseries-split)
  - [5. Combating Base Rate Bias (Logarithmic Class Smoothing)](#5-combating-base-rate-bias-logarithmic-class-smoothing)
- [Automated Economic Interpretation (LLM)](#automated-economic-interpretation-llm)
- [Configuration (`config.py`)](#configuration-configpy)
- [Data Source & 360° Macro Universe](#data-source--360-macro-universe)
  - [The "Macro-Proxy" Approach (Combating Multicollinearity)](#the-macro-proxy-approach-combating-multicollinearity)
- [Execution (Local & Development)](#execution-local--development)
- [Cloud Deployment (Docker & Railway)](#cloud-deployment-docker--railway)
  - [1. Containerization (Dockerfile)](#1-containerization-dockerfile)
  - [2. CI/CD Deployment on Railway.app](#2-cicd-deployment-on-railwayapp)

---

## Model Architecture

The pipeline addresses common issues in financial time series modeling, such as multicollinearity and high dimensionality, using a multi-stage architecture.

### 1. Feature Engineering & Variable Transformation

The model does not process absolute stock prices. Instead, the raw data undergoes a strict three-stage transformation pipeline before being fed into the algorithm:

- **Stage 1 (Raw Data):** The pipeline fetches adjusted closing prices for all specified tickers up to the current date.
- **Stage 2 (Momentum Returns):** Absolute prices are converted into rolling percentage returns (`pct_change`) representing short- and medium-term momentum (1 month/21 days, 3 months/63 days, and 6 months/126 days).
- **Stage 3 (Standardization):** Multinomial Logistic Regression requires normalized scales to prevent magnitude bias. A `StandardScaler` (fitted solely on the historical training data) transforms the rolling returns into Z-scores. The final input variables represent the distance of a specific return from its 10-year historical mean, measured in standard deviations.

### 2. Dynamic Target Classification

The model classifies returns based on macroeconomic assumptions scaled to the specific forecast horizon.

- **Baseline:** An assumed annual inflation rate (e.g., 2.5%).
- **Margin:** A tolerance corridor (e.g., +/- 1.0% p.a.) around the baseline.
- **Scaling:** Annualized values are linearly scaled to the forecast horizon (e.g., 126 days).
- **Classification Logic:**
  - Future return > upper threshold → `Up` (1)
  - Future return < lower threshold → `Down` (-1)
  - Future return within corridor → `Flat` (0)

### 3. Two-Stage Feature Selection

To maintain model stability, feature selection is performed in two steps:

- **Stage 1 (Filter):** A univariate ANOVA F-test (`SelectKBest`) reduces the feature space to the top 80 predictors. This dynamic pre-filter rapidly eliminates the ~20–30 weakest variables (pure noise), keeping the computational load for the wrapper stage manageable.
- **Stage 2 (Wrapper):** Sequential Feature Selection (`SequentialFeatureSelector`) with 3-fold cross-validation identifies the optimal subset (default: 8 features) from the remaining 80 variables to combat multicollinearity.

### 4. Evaluation (TimeSeries Split)

Out-of-sample evaluation is performed using a `TimeSeriesSplit`. The `gap` parameter is set exactly to the forecast horizon to prevent data leakage from overlapping return windows.

### 5. Combating Base Rate Bias (Logarithmic Class Smoothing)

A significant challenge when predicting broad market indices like the S&P 500 is the inherent historical upward bias. Because the market rises much more often than it falls, the training dataset becomes highly imbalanced. If left unadjusted, a standard Logistic Regression will default to the historically "safe" bet (predicting `Up`), leading to dangerous insensitivity towards market crashes (`Down`) or sideways markets (`Flat`).

While simple inverse-frequency balancing (like scikit-learn's default `class_weight='balanced'`) solves this, it operates on a strict linear scale. This often overcompensates — if a crash is 10× rarer than a bull market, the algorithm penalizes itself 10× harder for missing it, resulting in a paranoid model that issues constant false crash alarms.

To solve this, the pipeline calculates **Dynamic Custom Weights using Logarithmic Smoothing**.

**Mathematical Implementation:**

The pipeline dynamically evaluates the dataset distribution before training and applies a logarithmic function to calculate the penalty weight ($W$) for each class:

$$W_{class} = \log_{10}\left(\frac{N_{majority}}{N_{class}}\right) + 1.0$$

> **The Effect:** This formula maintains a logical hierarchy of risk while dampening extreme statistical outliers. The majority class (e.g., `Up`) receives a baseline weight of 1.0. Rarer classes (like `Down` and `Flat`) receive mathematically scaled higher penalties (e.g., 1.5 to 2.5).
>
> By utilizing logarithmic smoothing instead of strict linear ratios, the model is forced to actively hunt for macroeconomic warning signals and respect the danger of a market downturn — all without succumbing to algorithmic paranoia.

---

## Automated Economic Interpretation (LLM)

The pipeline integrates the Google Gemini API to provide a fundamental economic rationale for the statistically selected predictors.

Once the Sequential Feature Selector identifies the top variables, the resulting coefficient matrix is sent to the LLM. The model interprets the economic relationships (e.g., sector dependencies, inverse correlations) and appends a concise, quantitative analysis directly to the output report.

- **Robustness:** The API request is wrapped in an automatic retry mechanism to gracefully handle rate limits (HTTP 429) during repeated test runs.
- **Security:** The API key is not hardcoded but dynamically loaded from the `GEMINI_API_KEY` environment variable via GitHub Secrets.

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

## Data Source & 360° Macro Universe

Historical price data (Adjusted Close) is fetched via the Yahoo Finance API (`yfinance`).

### The "Macro-Proxy" Approach (Combating Multicollinearity)

A naive machine learning model trained on 100 random US equities will suffer heavily from **multicollinearity**. Since equities within the same market are highly correlated, the model receives redundant signals (e.g., if the SPY crashes, 95% of its constituents crash simultaneously). This illusion of data density leads to overfitting and poor out-of-sample forecasting.

To solve this, the pipeline utilizes a **360-degree macro-proxy universe**. Instead of tracking highly correlated single stocks, `config.py` curates ~50 distinct assets representing fundamentally orthogonal economic forces:

- **Cost of Capital & Fear:** Treasury Yields (`^TNX`, `^IRX`), the VIX (`^VIX`), and the US Dollar Index (`DX-Y.NYB`).
- **Credit Risk & Systemic Stress:** High Yield Junk Bonds (`HYG`) measure corporate default risks, while long-term Treasuries (`TLT`) act as a proxy for institutional flight-to-safety.
- **Inflation & Industrial Demand:** Crude Oil, "Dr. Copper" (`HG=F`), and Agricultural Commodities (Corn, Wheat) provide leading signals for supply-side inflation.
- **Institutional Sector Rotation:** The model tracks capital flows between cyclical (`XLY` Consumer Discretionary, `XLK` Tech) and defensive (`XLU` Utilities, `XLP` Staples) sectors to detect broad market shifts before they reflect in the main indices.
- **Alternative Liquidity:** Bitcoin (`BTC-USD`) is included as a modern proxy for global excess liquidity and risk-on sentiment.
- **Global Systemic Equities:** A highly restricted, focused selection of heavyweight market drivers across the US, EU, UK, and Japan.

**Resulting Feature Space:**

The pipeline calculates the 1-month, 3-month, and 6-month momentum for each of these ~50 base assets, generating a matrix of **~150 distinct macroeconomic variables**. Because the base assets are carefully selected to be fundamentally orthogonal, the SFS can construct highly robust, non-correlated predictor sets (e.g., combining falling copper momentum with rising junk bond yields and a strong dollar) to forecast the target ETF.

---

## Execution (Local & Development)

The repository is configured for GitHub Codespaces.

1. Open the repository in a GitHub Codespace.
2. Dependencies are automatically installed via `.devcontainer/devcontainer.json`.
3. Run the pipeline via the integrated terminal:

```bash
python src/main.py
```

**Generated Artifacts (`/output` directory):**

| File | Description |
| :--- | :--- |
| `confusion_matrix.png` | Visual evaluation (In-Sample vs. Out-of-Sample). |
| `yahoo_data_YYYYMMDD_HHMMSS.csv` | The cleaned historical dataset used for the run. |
| `feature_selection_YYYYMMDD_HHMMSS.md` | Full statistical documentation including predictor ranking, model intercepts, and LLM-generated economic interpretation. |

---

## Cloud Deployment (Docker & Railway)

The model is provisioned as a webservice using Streamlit, containerized with Docker, and deployed on **Railway.app**.

### 1. Containerization (Dockerfile)

The application is packaged into a portable Docker image. The `Dockerfile` handles the installation of system dependencies and exposes the default Streamlit port:

```dockerfile
# /Dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential curl && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. CI/CD Deployment on Railway.app

The deployment process is fully automated via GitHub integration.

1. **Project Creation:** In the Railway dashboard, click **New Project** and select **Deploy from GitHub repo** to connect this repository.
2. **Runtime Configuration:** Railway will automatically detect the `Dockerfile` at the root of the repository, build the image, and handle the containerization.
3. **Environment Variables & Secrets:** The Gemini API key must never be hardcoded or pushed to the repository. Configure the required variables securely via Railway's **Variables** tab:
   - `GEMINI_API_KEY` → `<YOUR_ACTUAL_API_KEY>`
   - `PORT` → `8501` (Explicitly directs Railway's internal router to the exposed Streamlit port.)

Once deployed, Railway generates a permanent, TLS-encrypted URL (e.g., `https://etf-predictor-production.up.railway.app`). The app runs reliably, fetching fresh Yahoo Finance data and dynamically generating macro-forecasts and LLM reports upon user request.

[etf-predictor-web-service](https://etf-predictor-production.up.railway.app)
