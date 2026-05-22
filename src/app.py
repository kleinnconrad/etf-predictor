# src/app.py
import streamlit as st
import pandas as pd
import os
from data_pipeline import load_and_prepare_data
from modeling import perform_feature_selection
from config import FORECAST_HORIZON_DAYS

st.set_page_config(page_title="ETF Quant Predictor", layout="wide")

st.title("ETF Engine")
st.sidebar.header("Konfiguration")

target_ticker = st.sidebar.text_input("Ziel-ETF Ticker", value="SPY")
run_button = st.sidebar.button("Analyse starten")

if run_button:
    with st.status("Pipeline läuft...", expanded=True) as status:
        st.write("Lade globale Makro-Daten...")
        # Nutze deine bestehende Pipeline
        X, y, latest = load_and_prepare_data(target_ticker, FORECAST_HORIZON_DAYS)
        
        st.write("Trainiere Modell & Selektiere Features...")
        timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
        model, X_opt = perform_feature_selection(X, y, latest, target_ticker, FORECAST_HORIZON_DAYS, timestamp=timestamp)
        
        status.update(label="Analyse abgeschlossen!", state="complete")

    # Anzeige der Ergebnisse
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Aktuelle Prognose")
        # Hier die Wahrscheinlichkeiten aus dem Modell anzeigen
        st.metric("Haupt-Prognose", "UP" if model.predict(latest[X_opt.columns])[0] == 1 else "DOWN/FLAT")
        
    with col2:
        st.subheader("Trefferquote (Matrix)")
        # Lade die generierte Confusion Matrix
        st.image("output/confusion_matrix.png")

    st.subheader("KI-Interpretation (Hedgefonds-Bericht)")
    with open(f"output/feature_selection_{timestamp}.md", "r") as f:
        st.markdown(f.read())