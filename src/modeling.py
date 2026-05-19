# src/modeling.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SequentialFeatureSelector, SelectKBest, f_classif

def perform_feature_selection(X_scaled, y, final_features=8):
    print("Führe Feature Selection durch...")
    
    kbest = SelectKBest(score_func=f_classif, k=40)
    kbest.fit(X_scaled, y)
    features_stage_1 = X_scaled.columns[kbest.get_support()]
    X_stage_1 = X_scaled[features_stage_1]
    
    # Multinomiale Logistische Regression (One-vs-Rest)
    log_reg_base = LogisticRegression(solver='lbfgs', max_iter=1000)
    sfs = SequentialFeatureSelector(log_reg_base, n_features_to_select=final_features, direction='forward', cv=3, n_jobs=-1)
    sfs.fit(X_stage_1, y)
    
    selected_features = features_stage_1[sfs.get_support()]
    
    X_optimal = X_scaled[selected_features]
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_optimal, y)

    print("=== Ergebnis der Schrittweisen Variablenselektion (SFS) ===")
    # Berechnung des durchschnittlichen absoluten Einflusses der Features über die 3 Klassen
    importance = np.mean(np.abs(model.coef_), axis=0)
    
    coeff_df = pd.DataFrame({
        'Prädiktor': selected_features,
        'Einfluss (Mean Absolut)': importance
    }).sort_values(by='Einfluss (Mean Absolut)', ascending=False)
    print(coeff_df.to_string(index=False), "\n")
    
    return model, X_optimal