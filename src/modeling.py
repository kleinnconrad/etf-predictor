# src/modeling.py

import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SequentialFeatureSelector, SelectKBest, f_classif

def perform_feature_selection(X_scaled, y, final_features=8, timestamp=None):
    print("Führe Feature Selection durch...")
    
    kbest = SelectKBest(score_func=f_classif, k=40)
    kbest.fit(X_scaled, y)
    features_stage_1 = X_scaled.columns[kbest.get_support()]
    X_stage_1 = X_scaled[features_stage_1]
    
    log_reg_base = LogisticRegression(solver='lbfgs', max_iter=1000)
    sfs = SequentialFeatureSelector(log_reg_base, n_features_to_select=final_features, direction='forward', cv=3, n_jobs=-1)
    sfs.fit(X_stage_1, y)
    
    selected_features = features_stage_1[sfs.get_support()]
    
    X_optimal = X_scaled[selected_features]
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_optimal, y)

    print("=== Ergebnis der Schrittweisen Variablenselektion (SFS) ===")
    importance = np.mean(np.abs(model.coef_), axis=0)
    
    coeff_df = pd.DataFrame({
        'Prädiktor': selected_features,
        'Einfluss (Mean Absolut)': importance
    }).sort_values(by='Einfluss (Mean Absolut)', ascending=False)
    print(coeff_df.to_string(index=False), "\n")
    
    # Markdown Export der Ergebnisse und Parameter
    if timestamp:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '..'))
        output_dir = os.path.join(project_root, 'output')
        os.makedirs(output_dir, exist_ok=True)
        
        md_path = os.path.join(output_dir, f"feature_selection_{timestamp}.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write("# Ergebnisse der Variablenselektion & Modellparameter\n\n")
            f.write(f"- **Generiert am:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"- **Anzahl finaler Features:** {final_features}\n\n")
            
            f.write("## Ausgewählte Prädiktoren (SFS)\n\n")
            f.write("| Prädiktor | Einfluss (Mean Absolut) |\n")
            f.write("| :--- | :--- |\n")
            for _, row in coeff_df.iterrows():
                f.write(f"| {row['Prädiktor']} | {row['Einfluss (Mean Absolut)']:.6f} |\n")
            
            f.write("\n## Modellparameter (Multinomial Logistic Regression)\n\n")
            f.write(f"- **Intercepts (Klassenordnung: Down [-1], Flat [0], Up [1]):**\n  `{model.intercept_.tolist()}`\n\n")
            f.write("- **Koeffizienten-Matrix (Form: Klassen x Features):**\n")
            f.write("  ```text\n")
            f.write(str(model.coef_))
            f.write("\n  ```\n")
            
        print(f"Ergebnisse und Modellparameter gespeichert unter: {md_path}")
        
    return model, X_optimal