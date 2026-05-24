### Feature Engineering Architecture

The feature engineering pipeline processes a 10-year historical dataset using a row-by-row sliding window. This continuous timeframe captures multiple macroeconomic regimes and establishes a statistical baseline for feature scaling. The pipeline calculates momentum variables by referencing historical price points relative to the current evaluation day.

For every trading day in the dataset, the algorithm executes a backward-looking function to engineer predictor variables and a forward-looking function to establish the target classification. The backward window calculates 1-month, 3-month, and 6-month percentage returns for all assets in the macro universe. Macroeconomic indicators sourced from FRED are published at lower frequencies (typically monthly) than equity pricing. To reconcile these datasets, the pipeline applies a forward-fill imputation strategy upon merging. Each daily observation for a macroeconomic variable inherits the most recent published value, ensuring the model exclusively consumes "point-in-time" verified data. This logic forces the algorithm to recognize macro regime shifts only as they occur, preventing look-ahead bias and aligning physical economic reality with high-frequency market dynamics. The forward window evaluates the price of the target asset exactly 126 trading days in the future.

<img src="https://github.com/kleinnconrad/etf-predictor/blob/main/docs/sliding_window.png?raw=true" width="50%">

This bidirectional windowing creates two temporal boundaries. The initial 126 days of the dataset lack sufficient historical data to calculate the 6-month momentum features. Rows falling within this initialization phase are discarded. The final 126 days of the dataset lack the future price data required to assign a target class. The absolute latest row in this terminal phase is isolated and passed to the inference engine for live prediction. All other rows lacking a target class are excluded from the training matrix.

Logistic regression requires stationary input variables. Absolute asset prices violate this requirement due to structural market drift. The pipeline drops all absolute prices after computing the percentage returns. The continuous return variables are subsequently transformed into Z-scores. This normalizes volatility differences across the asset classes.

The resulting output is a two-dimensional matrix. The primary key is the valid trading date. The columns consist of a single discrete target variable and 114 continuous, scaled features representing the momentum of 38 assets across three time horizons.

| date | target_class | spy_1M_scaled | spy_3M_scaled | spy_6M_scaled | tnx_1M_scaled | ... up to X114 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2016-11-20 | 1 | 0.85 | 1.12 | 0.45 | -0.30 | ... |
| 2016-11-21 | 1 | 0.91 | 1.15 | 0.48 | -0.25 | ... |
| ... | ... | ... | ... | ... | ... | ... |
| 2020-03-15 | -1 | -3.50 | -4.10 | -2.80 | -5.10 | ... |
| ... | ... | ... | ... | ... | ... | ... |
| 2025-11-23 | 0 | 0.15 | -0.10 | 0.22 | 1.05 | ... |