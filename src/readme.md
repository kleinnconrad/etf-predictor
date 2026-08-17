# Source Code

This directory contains the core implementation of the quantitative ETF forecasting pipeline. 

* `app.py`: Defines the Streamlit web application. Facilitates interactive data exploration, backtest evaluation, and visualization of batch predictions.
* `audit.py`: Generates markdown-based audit trails for feature selection and model parameters. Logs selected variables, p-values, and model coefficients for compliance and review.
* `config.py`: Stores static configuration parameters, including API keys, file paths, target instrument lists, and predefined macroeconomic indicator selections.
* `data_pipeline.py`: Executes data ingestion and feature engineering. Fetches financial time series, computes rolling returns, generates interaction ratios, and defines the target classification logic.
* `evaluation.py`: Computes validation metrics for the predictive models. Evaluates out-of-sample accuracy and utilizes Kolmogorov-Smirnov statistics to determine optimal probability thresholds for classification cutoffs.
* `main.py`: Orchestrates the quantitative pipeline. Serves as the entry point for data ingestion, feature selection, model training, evaluation, and report generation.
* `modeling.py`: Implements the machine learning logic. Features class-weight balancing, temporal cross-validation, and a logistic regression classifier with Sequential Feature Selection (SFS). Applies dual-cutoff probability rules for risk-adjusted predictions.

## Runtime View

```mermaid
sequenceDiagram
    participant User as CLI / Web App
    participant Main as main.py (Orchestrator)
    participant Data as data_pipeline.py
    participant Model as modeling.py
    participant Ext as External APIs (YF/FRED)
    participant FS as Local Storage

    User->>Main: Execute pipeline (Batch / Single)
    
    alt is Batch Mode
        Main->>Ext: Master-Fetch Global Yahoo Data
        Ext-->>Main: Returns Price Matrix
        Main->>Ext: Master-Fetch FRED Data
        Ext-->>Main: Returns Macro Series
    end
    
    loop For each target ETF ticker
        Main->>Data: load_and_prepare_data(ticker)
        alt is Single Mode
            Data->>Ext: Fetch Yahoo & FRED (if not pre-fetched)
            Ext-->>Data: Data Series
        end
        Data-->>Main: X_train, y_train, X_live
        
        Main->>Model: perform_feature_selection()
        Model-->>Main: selected_features, predictions, probabilities
        
        alt is Single Mode
            Main->>FS: Export Diagnostic Artifacts (CSV)
        end
    end
    
    alt is Batch Mode
        Main->>FS: Save batch_results.json
    end
    Main-->>User: Pipeline Complete
```