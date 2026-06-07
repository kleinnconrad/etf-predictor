# src/evaluation.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LogisticRegression

def evaluate_and_plot(model, X_optimal, y, forecast_horizon):
    print("Evaluating model (Training & Cross-validation)...")
    class_names = ['Down', 'Flat', 'Up']

    # 1. Confusion Matrix: In-Sample (Training)
    y_pred_train = model.predict(X_optimal)
    cm_train = confusion_matrix(y, y_pred_train, labels=[-1, 0, 1])

    # 2. Confusion Matrix: Out-of-Sample (Cross-validation)
    tscv = TimeSeriesSplit(n_splits=5, gap=forecast_horizon)
    y_cv_true, y_cv_pred = [], []

    for train_index, test_index in tscv.split(X_optimal):
        X_tr, X_te = X_optimal.iloc[train_index], X_optimal.iloc[test_index]
        y_tr, y_te = y.iloc[train_index], y.iloc[test_index]
        
        # Check: Are there at least 2 different classes in the training split?
        unique_classes = np.unique(y_tr)
        
        if len(unique_classes) == 1:
            # Fallback: The model only knows one class and predicts it across the board
            fallback_class = unique_classes[0]
            y_cv_pred.extend([fallback_class] * len(X_te))
        else:
            # Normal training if >= 2 classes are present
            log_reg_cv = LogisticRegression(solver='lbfgs', max_iter=1000)
            log_reg_cv.fit(X_tr, y_tr)
            y_cv_pred.extend(log_reg_cv.predict(X_te))
            
        y_cv_true.extend(y_te)

    cm_cv = confusion_matrix(y_cv_true, y_cv_pred, labels=[-1, 0, 1])

    # Text Output
    print("=== Confusion Matrix (In-Sample) ===")
    print(pd.DataFrame(cm_train, index=[f'True {c}' for c in class_names], columns=[f'Pred {c}' for c in class_names]), "\n")
    
    print("=== Confusion Matrix (5-Fold CV Out-of-Sample) ===")
    print(pd.DataFrame(cm_cv, index=[f'True {c}' for c in class_names], columns=[f'Pred {c}' for c in class_names]), "\n")

    # Visual Output (Plots)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.heatmap(cm_train, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names, ax=axes[0])
    axes[0].set_title('Training (In-Sample)')
    axes[0].set_ylabel('Actual Direction')
    
    sns.heatmap(cm_cv, annot=True, fmt='d', cmap='Oranges', xticklabels=class_names, yticklabels=class_names, ax=axes[1])
    axes[1].set_title('Cross-validation (Out-of-Sample)')
    axes[1].set_ylabel('Actual Direction')
    
    plt.tight_layout()
    
    # Dynamic path resolution for GitHub Codespaces
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..'))
    output_dir = os.path.join(project_root, 'output')
    
    os.makedirs(output_dir, exist_ok=True)
    plot_path = os.path.join(output_dir, 'confusion_matrix.png')
    
    plt.savefig(plot_path)
    print(f"Plot saved at {plot_path}")