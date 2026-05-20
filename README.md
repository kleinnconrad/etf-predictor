# ETF Predictor

This repository contains a machine learning pipeline to predict the medium-term market development of a target ETF (default: SPY). 

The model classifies the future market state into three discrete classes: Up, Down, and Flat. The statistical pipeline is based on Multinomial Logistic Regression (One-vs-Rest).

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
- **Classification Logic:** - Future return > upper threshold: `Up` (1)
  - Future return < lower threshold: `Down` (-1)
  - Future return within corridor: `Flat` (0)

### 3. Two-Stage Feature Selection
To maintain model stability, feature selection is performed in two steps:
- **Stage 1 (Filter):** A univariate ANOVA F-test (`SelectKBest`) reduces the feature space to the top 40 predictors, decreasing computational load.
- **Stage 2 (Wrapper):** Sequential Feature Selection (`SequentialFeatureSelector`) with 3-fold cross-validation identifies the optimal subset (default: 8 features) for the logistic regression model.

### 4. Evaluation (TimeSeries Split)
Out-of-sample evaluation is performed using a `TimeSeriesSplit`. The `gap` parameter is set exactly to the forecast horizon to prevent data leakage from overlapping return windows.

---

## Automated Economic Interpretation (LLM)

The pipeline integrates the Google Gemini API to provide a fundamental economic rationale for the statistically selected predictors. 

Once the Sequential Feature Selector identifies the top variables, the resulting coefficient matrix is sent to the LLM. The model interprets the economic relationships (e.g., sector dependencies, inverse correlations) and appends a concise, quantitative analysis directly to the output report. 

- **Robustness:** The API request is wrapped in an automatic retry mechanism to gracefully handle rate limits (Code 429) during repeated test runs.
- **Security:** The API key is not hardcoded but dynamically loaded from the `GEMINI_API_KEY` environment variable via GitHub Secrets.

---

## Configuration (config.py)

Hyperparameters and economic assumptions are managed in `src/config.py`.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `TARGET_ETF` | `str` | Ticker symbol of the target ETF (e.g., `'SPY'`). |
| `FORECAST_HORIZON_DAYS` | `int` | Forecast horizon in trading days (e.g., `126`). Defines the CV gap. |
| `ANNUAL_INFLATION_RATE` | `float` | Assumed annual inflation rate (e.g., `0.025`). |
| `ANNUAL_MARGIN` | `float` | Tolerance corridor around the baseline (e.g., `0.01`). |
| `START_DATE` / `END_DATE` | `str` | Historical training period boundaries. |

---

## Data Source & Investment Universe

Historical price data (Adjusted Close) is fetched via the Yahoo Finance API (`yfinance`). 

To ensure a robust and globally diversified feature space, the base universe (`config.py`) is structured across orthogonal macro asset classes rather than just highly correlated single stocks:
- **Macro Indicators:** Treasury Yields (10Y, 13W), VIX (Volatility), US Dollar Index.
- **Commodities:** Crude Oil, Gold, Copper ("Dr. Copper" as a leading economic indicator).
- **Broad Sectors & Indices:** US Financials, Tech, Energy, Biotech, Emerging Markets, DAX, Nikkei.
- **Systemic Single Stocks:** Select heavyweight drivers across the US, EU, UK, and Japan.

**Resulting Feature Space:**
While the base universe consists of approximately 35 raw tickers, the pipeline's feature engineering expands this into a high-dimensional dataset. By calculating the 1-month, 3-month, and 6-month momentum for every single asset, the model generates and trains on **over 100 distinct macroeconomic variables**. This allows the algorithm to detect complex cross-asset relationships (e.g., falling copper momentum combined with a rising Dollar) before predicting the target ETF.

Tickers missing more than 10% of the requested historical data (e.g., due to recent IPOs) are automatically dropped during preprocessing.

---

## Execution (GitHub Codespaces)

The repository is configured for GitHub Codespaces.

1. Open the repository in a GitHub Codespace.
2. Dependencies are automatically installed via `.devcontainer/devcontainer.json`.
3. Execute the pipeline via the integrated terminal:

```bash
python src/main.py
```

## Artifacts generated in the /output directory:

1. confusion_matrix.png: Visual evaluation (In-Sample vs. Out-of-Sample).
2. yahoo_data_YYYYMMDD_HHMMSS.csv: The cleaned historical dataset used for the run.
3. feature_selection_YYYYMMDD_HHMMSS.md: The complete statistical documentation, including the predictor ranking, model intercepts, and the LLM-generated economic interpretation.