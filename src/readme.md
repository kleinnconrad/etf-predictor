# Source Code Overview

This directory contains the logic for the ETF Quant Engine pipeline. The components handle configuration, data ingestion, predictive modeling, and batch execution.

* `config.py`: Defines configuration parameters including target ETF selections, macroeconomic thresholds, and file paths.
* `data_pipeline.py`: Manages data ingestion and preprocessing. It retrieves market data and macroeconomic indicators, calculates rolling features, and adjusts target class thresholds.
* `modeling.py`: Contains the machine learning architecture. It implements class weighting and a Logistic Regression model utilizing Sequential Feature Selection.
* `evaluation.py`: Computes performance metrics such as cross-validation accuracy and Kolmogorov-Smirnov statistics to assess model validity and quality gate compliance.
* `audit.py`: Handles execution logging and state tracking to record pipeline runs, anomalies, and processing metadata.
* `app.py`: Implements the Streamlit application for data exploration and visualization of batch prediction results.
* `main.py`: Integrates the modules to execute an iteration of the quantitative pipeline.