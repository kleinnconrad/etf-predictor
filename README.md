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
- **Stage 1 (Filter):** A univariate ANOVA F-test (`SelectKBest`) reduces the feature space to the top 80 predictors. This dynamic pre-filter rapidly eliminates the ~20-30 weakest variables (pure noise), keeping the computational load for the wrapper stage manageable.
- **Stage 2 (Wrapper):** Sequential Feature Selection (`SequentialFeatureSelector`) with 3-fold cross-validation identifies the optimal subset (default: 8 features) from the remaining 80 variables to combat multicollinearity.

### 4. Evaluation (TimeSeries Split)
Out-of-sample evaluation is performed using a `TimeSeriesSplit`. The `gap` parameter is set exactly to the forecast horizon to prevent data leakage from overlapping return windows.

### 5. Combating Base Rate Bias (Algorithmic Class Balancing)
A significant challenge when predicting broad market indices like the S&P 500 is the inherent historical upward bias (the market rises more often than it falls). Consequently, the training dataset becomes highly imbalanced, heavily skewing towards the `Up` class.

If left unadjusted, a standard Logistic Regression using an argmax cut-off will become artificially overconfident. The algorithm learns that predicting `Up` yields the highest statistical probability of success, leading to a dangerous insensitivity towards predicting market crashes (`Down`) or sideways markets (`Flat`).

To counteract this, the pipeline enforces **Algorithmic Risk Sensitivity** by passing the `class_weight='balanced'` parameter to the Logistic Regression estimator during both the Sequential Feature Selection and the final model training. 

**Mathematical Effect:**
Instead of treating all errors equally, the algorithm dynamically adjusts the penalty weights inversely proportional to class frequencies in the input data. The model penalizes itself significantly harder for missing a rare event (e.g., a `Down` market) than for missing a common event. This forces the model to actively hunt for macroeconomic warning signals and ensures it retains the confidence to predict market downturns, rather than defaulting to the historically "safe" bull market bet.
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

## Data Source & 360° Macro Universe

Historical price data (Adjusted Close) is fetched via the Yahoo Finance API (`yfinance`). 

### The "Macro-Proxy" Approach (Combating Multicollinearity)
A naive machine learning model trained on 100 random US equities will suffer heavily from **multicollinearity**. Since equities within the same market are highly correlated, the model receives redundant signals (e.g., if the SPY crashes, 95% of its constituents crash simultaneously). This illusion of data density leads to overfitting and poor out-of-sample forecasting.

To solve this, the pipeline utilizes a **360-degree macro-proxy universe**. Instead of tracking highly correlated single stocks, the `config.py` curates ~50 distinct assets representing completely orthogonal economic forces. This ensures the Sequential Feature Selector (SFS) has access to independent, non-overlapping predictors:

- **Cost of Capital & Fear:** Treasury Yields (`^TNX`, `^IRX`), the VIX (`^VIX`), and the US Dollar Index (`DX-Y.NYB`).
- **Credit Risk & Systemic Stress:** High Yield Junk Bonds (`HYG`) measure corporate default risks, while long-term Treasuries (`TLT`) act as a proxy for institutional flight-to-safety.
- **Inflation & Industrial Demand:** Crude Oil, "Dr. Copper" (`HG=F`), and Agricultural Commodities (Corn, Wheat) provide leading signals for supply-side inflation.
- **Institutional Sector Rotation:** The model tracks capital flows between cyclical (`XLY` Consumer Discretionary, `XLK` Tech) and defensive (`XLU` Utilities, `XLP` Staples) sectors to detect broad market shifts before they reflect in the main indices.
- **Alternative Liquidity:** Bitcoin (`BTC-USD`) is included as a modern proxy for global excess liquidity and risk-on sentiment.
- **Global Systemic Equities:** A highly restricted, focused selection of heavyweight market drivers across the US, EU, UK, and Japan.

**Resulting Feature Space:**
The pipeline calculates the 1-month, 3-month, and 6-month momentum for each of these ~50 base assets. This generates a matrix of **~150 distinct macroeconomic variables**. Because the base assets are carefully selected to be fundamentally orthogonal, the algorithmic wrapper (SFS) can construct highly robust, non-correlated predictor sets (e.g., combining falling copper momentum with rising junk bond yields and a strong dollar) to forecast the target ETF.

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