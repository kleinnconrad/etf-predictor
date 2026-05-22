# src/app.py
import streamlit as st
import pandas as pd
import os

from data_pipeline import load_and_prepare_data
from modeling import perform_feature_selection
from config import (
    START_DATE, 
    END_DATE, 
    FORECAST_HORIZON_DAYS, 
    ANNUAL_INFLATION, 
    ANNUAL_MARGIN, 
    TRADING_DAYS_PER_YEAR
)

st.set_page_config(page_title="ETF Quant Predictor", layout="wide")

st.title("📈 ETF Quant-on-Demand Engine")
st.sidebar.header("Konfiguration")

target_ticker = st.sidebar.text_input("Ziel-ETF Ticker", value="SPY")
run_button = st.sidebar.button("Analyse starten")

if run_button:
    # Timestamp generieren, bevor die Pipeline startet
    timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
    
    with st.status("Pipeline läuft...", expanded=True) as status:
        st.write("📡 Lade globale Makro-Daten...")
        
        # FIX: Alle benötigten Parameter aus der config.py übergeben
        X, y, latest = load_and_prepare_data(
            target_ticker=target_ticker,
            start_date=START_DATE,
            end_date=END_DATE,
            forecast_horizon=FORECAST_HORIZON_DAYS,
            annual_inflation=ANNUAL_INFLATION,
            annual_margin=ANNUAL_MARGIN,
            trading_days=TRADING_DAYS_PER_YEAR,
            timestamp=timestamp
        )
        
        st.write("🧠 Trainiere Modell & Selektiere Features...")
        model, X_opt = perform_feature_selection(
            X_scaled=X, 
            y=y, 
            latest_features_scaled=latest, 
            target_etf=target_ticker, 
            horizon=FORECAST_HORIZON_DAYS, 
            timestamp=timestamp
        )
        
        status.update(label="Analyse abgeschlossen!", state="complete")

    # Anzeige der Ergebnisse
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Aktuelle Prognose")
        # Hier lesen wir das Prediction-Label direkt aus dem Modell
        prediction = model.predict(latest[X_opt.columns])[0]
        class_mapping = {-1: "Down 🔴", 0: "Flat 🟡", 1: "Up 🟢"}
        st.metric("Haupt-Prognose", class_mapping.get(prediction, "Unknown"))
        
    with col2:
        st.subheader("Trefferquote (Matrix)")
        # Überprüfen, ob das Bild generiert wurde, bevor wir es laden
        image_path = "output/confusion_matrix.png"
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.info("Keine Confusion Matrix gefunden.")

    st.subheader("KI-Interpretation (Hedgefonds-Bericht)")
    md_path = f"output/feature_selection_{timestamp}.md"
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            st.markdown(f.read())
    else:
        st.info("Bericht wird generiert...")