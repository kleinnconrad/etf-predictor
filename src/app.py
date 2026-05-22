# src/app.py
import streamlit as st
import pandas as pd
import os
import yfinance as yf

from data_pipeline import load_and_prepare_data
from modeling import perform_feature_selection
from config import (
    START_DATE, 
    END_DATE, 
    FORECAST_HORIZON_DAYS, 
    ANNUAL_INFLATION_RATE, 
    ANNUAL_MARGIN, 
    TRADING_DAYS_PER_YEAR,
    TARGET_ETF,
    get_all_tickers
)

# 1. Seiten-Setup (muss immer ganz oben stehen)
st.set_page_config(page_title="Quant Engine", page_icon="📈", layout="wide")

# 2. Custom CSS für ein professionelleres Design
st.markdown("""
    <style>
    /* Haupt-Hintergrund etwas abdunkeln (optional) */
    .block-container { padding-top: 2rem; }
    
    /* Große, moderne Überschriften */
    .hero-header { font-size: 3rem; font-weight: 800; margin-bottom: 0; padding-bottom: 0; color: #E8E8E8;}
    .hero-sub { font-size: 1.2rem; color: #888; margin-top: 0; padding-top: 0.5rem; margin-bottom: 2rem;}
    
    /* Start-Button pimpen */
    div.stButton > button:first-child {
        background-color: #2e66ff;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        height: 3rem;
    }
    div.stButton > button:first-child:hover {
        background-color: #1a4bd1;
        border: 1px solid white;
    }
    
    /* Info-Boxen stylen */
    .metric-box {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2e66ff;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar (Steuerung & Info)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/combo-chart.png", width=60)
    st.title("Steuerung")
    target_ticker = st.text_input("Ziel-ETF Ticker", value=TARGET_ETF).upper()
    
    st.divider()
    
    st.caption("Modell-Parameter (aus config.py)")
    st.write(f"**Prognose-Horizont:** {FORECAST_HORIZON_DAYS} Tage")
    st.write(f"**Basis-Inflation:** {ANNUAL_INFLATION_RATE*100}%")
    st.write(f"**Toleranz-Marge:** ±{ANNUAL_MARGIN*100}%")
    
    st.divider()
    run_button = st.button("Analyse starten", use_container_width=True)

# 4. Main Area (Hero Section)
st.markdown('<p class="hero-header">Quant-on-Demand Engine</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Institutionelle Makro-Analyse & ML-Prognose</p>', unsafe_allow_html=True)

# 5. Was passiert, bevor der Button gedrückt wird (Vorschau-Chart)
if not run_button:
    st.subheader(f"Aktueller Kursverlauf: {target_ticker}")
    try:
        # Lädt schnell die letzten 2 Jahre für ein hübsches Start-Bild
        ticker_data = yf.download(target_ticker, period="2y", interval="1d", progress=False)
        if not ticker_data.empty:
            st.line_chart(ticker_data['Close'])
        else:
            st.info("Warte auf Eingabe...")
    except Exception:
        st.info("Klicke auf 'Analyse starten', um die Prognose zu berechnen.")

# 6. Die Haupt-Pipeline
if run_button:
    timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
    
    with st.status("Quant-Pipeline läuft...", expanded=True) as status:
        st.write("Lade globale Makro-Daten (150+ Ticker)...")
        
        download_list = get_all_tickers()
        if target_ticker not in download_list:
            download_list.append(target_ticker)
            
        X, y, latest = load_and_prepare_data(
            target_ticker=target_ticker,
            all_tickers=download_list,
            start_date=START_DATE,
            end_date=END_DATE,
            forecast_horizon=FORECAST_HORIZON_DAYS,
            annual_inflation=ANNUAL_INFLATION_RATE,
            annual_margin=ANNUAL_MARGIN,
            trading_days=TRADING_DAYS_PER_YEAR,
            timestamp=timestamp
        )
        
        st.write("Trainiere Multinomial-Modell & extrahiere Features...")
        model, X_opt = perform_feature_selection(
            X_scaled=X, 
            y=y, 
            latest_features_scaled=latest, 
            target_etf=target_ticker, 
            horizon=FORECAST_HORIZON_DAYS, 
            timestamp=timestamp
        )
        
        status.update(label="Analyse erfolgreich abgeschlossen!", state="complete")

    # 7. Ergebnisse in TABS präsentieren
    tab1, tab2, tab3 = st.tabs(["🎯 Dashboard", "🤖 KI-Interpretation", "🔬 Modell-Diagnostik"])
    
    with tab1:
        st.subheader("Aktuelle Modell-Prognose")
        prediction = model.predict(latest[X_opt.columns])[0]
        
        # Visuelle Hervorhebung je nach Vorhersage
        if prediction == 1:
            st.success("🟢 Haupt-Signal: UP (Bullenmarkt erwartet)")
        elif prediction == -1:
            st.error("🔴 Haupt-Signal: DOWN (Bärenmarkt / Crash-Gefahr)")
        else:
            st.warning("🟡 Haupt-Signal: FLAT (Seitwärtsmarkt / Inflation schlägt Rendite)")
            
        st.divider()
        st.markdown(f"**Die {len(X_opt.columns)} stärksten Makro-Treiber aktuell:**")
        st.dataframe(X_opt.columns.tolist(), hide_index=True, use_container_width=True)

    with tab2:
        st.subheader("Hedgefonds-Bericht")
        md_path = f"output/feature_selection_{timestamp}.md"
        if os.path.exists(md_path):
            with open(md_path, "r", encoding="utf-8") as f:
                st.markdown(f.read())
        else:
            st.info("Bericht wird generiert...")

    with tab3:
        st.subheader("Out-of-Sample Trefferquote")
        image_path = "output/confusion_matrix.png"
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.info("Keine Confusion Matrix gefunden.")