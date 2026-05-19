# ETF Predictor

This repository contains a machine learning pipeline to predict the medium-term market development of a target ETF (default: SPY). 

The model classifies the future market state into three discrete classes: Up, Down, and Flat. The statistical pipeline is based on Multinomial Logistic Regression (One-vs-Rest).

---

## Model Architecture

The pipeline addresses common issues in financial time series modeling, such as multicollinearity and high dimensionality, using a multi-stage architecture.

### 1. Feature Engineering
Short- and medium-term momentum factors are used as predictors. Rolling returns for 1 month (21 days), 3 months (63 days), and 6 months (126 days) are calculated for each ticker in the specified universe.

### 2. Dynamic Target Classification
The model classifies returns based on macroeconomic assumptions scaled to the specific forecast horizon.
- **Baseline:** An assumed annual inflation rate (e.g., 2.5%).
- **Margin:** A tolerance corridor (e.g., +/- 1.0% p.a.) around the baseline.
- **Scaling:** Annualized values are linearly scaled to the forecast horizon (e.g., 126 days).
- **Classification Logic:** 
  - Future return > upper threshold: `Up` (1)
  - Future return < lower threshold: `Down` (-1)
  - Future return within corridor: `Flat` (0)

### 3. Two-Stage Feature Selection
To maintain model stability, feature selection is performed in two steps:
- **Stage 1 (Filter):** A univariate ANOVA F-test (`SelectKBest`) reduces the feature space to the top 40 predictors, decreasing computational load.
- **Stage 2 (Wrapper):** Sequential Feature Selection (`SequentialFeatureSelector`) with 3-fold cross-validation identifies the optimal subset (default: 8 features) for the logistic regression model.

### 4. Evaluation (TimeSeries Split)
Out-of-sample evaluation is performed using a `TimeSeriesSplit`. The `gap` parameter is set exactly to the forecast horizon to prevent data leakage from overlapping return windows.

---

## Configuration (config.py)

Hyperparameters and economic assumptions are managed in `src/config.py`.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `TARGET_ETF` | `str` | Ticker symbol of the target ETF (e.g., `'ETFL01.DE'`). |
| `FORECAST_HORIZON_DAYS` | `int` | Forecast horizon in trading days (e.g., `126`). Defines the CV gap. |
| `ANNUAL_INFLATION_RATE` | `float` | Assumed annual inflation rate (e.g., `0.025`). |
| `ANNUAL_MARGIN` | `float` | Tolerance corridor around the baseline (e.g., `0.01`). |
| `START_DATE` / `END_DATE` | `str` | Historical training period boundaries. |

---

## Data Source & Investment Universe

Historical price data (Adjusted Close) is fetched via the Yahoo Finance API (`yfinance`). 

The base universe includes major global market drivers and can be modified in `config.py`.
- **USA:** AAPL, MSFT, GOOGL, AMZN, NVDA, META, BRK-B, LLY, V, JPM
- **Germany:** SAP, SIE, ALV, DTE, AIR, VOW3, MBG, BMW, BAS, MUV2
- **UK & Japan:** Selected heavyweights (e.g., SHEL, AZN, Toyota, Sony)

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
