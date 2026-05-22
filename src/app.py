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

st.set_page_config(page_title="Quant Engine", page_icon="📈", layout="wide")

# --- BULLETPROOF CACHING (Überlebt Verbindungsabbrüche!) ---
@st.cache_data(ttl=43200, show_spinner=False)
def get_data(target_ticker, download_list, _timestamp):
    return load_and_prepare_data(
        target_ticker=target_ticker,
        all_tickers=download_list,
        start_date=START_DATE,
        end_date=END_DATE,
        forecast_horizon=FORECAST_HORIZON_DAYS,
        annual_inflation=ANNUAL_INFLATION_RATE,
        annual_margin=ANNUAL_MARGIN,
        trading_days=TRADING_DAYS_PER_YEAR,
        timestamp=_timestamp
    )

@st.cache_resource(show_spinner=False)
def train_quant_model(X, y, latest, target_ticker, _timestamp):
    return perform_feature_selection(
        X_scaled=X, 
        y=y, 
        latest_features_scaled=latest, 
        target_etf=target_ticker, 
        horizon=FORECAST_HORIZON_DAYS, 
        timestamp=_timestamp
    )
# -----------------------------------------------------------

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

st.markdown("""
    <style>
    .block-container { padding-top: 2rem; }
    .hero-header { font-size: 3rem; font-weight: 800; margin-bottom: 0; padding-bottom: 0; color: #E8E8E8;}
    .hero-sub { font-size: 1.2rem; color: #888; margin-top: 0; padding-top: 0.5rem; margin-bottom: 2rem;}
    div.stButton > button:first-child {
        background-color: #2e66ff;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        height: 3rem;
    }
    div.stButton > button:first-child:hover { background-color: #1a4bd1; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/combo-chart.png", width=60)
    st.title("Steuerung")
    target_ticker = st.text_input("Ziel-ETF Ticker", value=TARGET_ETF).upper()
    st.divider()
    run_button = st.button("Analyse starten", use_container_width=True)

st.markdown('<p class="hero-header">Quant-on-Demand Engine</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Institutionelle Makro-Analyse & ML-Prognose</p>', unsafe_allow_html=True)

# Wenn der Button gedrückt wird:
if run_button:
    timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
    
    with st.status("Quant-Pipeline läuft...", expanded=True) as status:
        st.write("📡 Lade globale Makro-Daten...")
        
        download_list = get_all_tickers()
        if target_ticker not in download_list:
            download_list.append(target_ticker)
            
        # HIER NUTZEN WIR JETZT DEN CACHE!
        X, y, latest = get_data(target_ticker, tuple(download_list), timestamp)
        
        st.write("Trainiere Modell (Multi-Core)...")
        model, X_opt = train_quant_model(X, y, latest, target_ticker, timestamp)
        
        st.session_state.results = {
            "model": model,
            "X_opt": X_opt,
            "latest": latest,
            "timestamp": timestamp,
            "prediction": model.predict(latest[X_opt.columns])[0]
        }
        st.session_state.analysis_done = True
        status.update(label="Analyse erfolgreich abgeschlossen!", state="complete")


# --- UI RENDERING ---
if not st.session_state.analysis_done:
    st.subheader(f"Aktueller Kursverlauf: {target_ticker}")
    try:
        ticker_data = yf.download(target_ticker, period="2y", interval="1d", progress=False)
        if not ticker_data.empty:
            st.line_chart(ticker_data['Close'])
    except Exception:
        pass
else:
    res = st.session_state.results
    tab1, tab2, tab3 = st.tabs(["Dashboard", "KI-Interpretation", "Modell-Diagnostik"])
    
    with tab1:
        st.subheader("Aktuelle Modell-Prognose")
        if res["prediction"] == 1:
            st.success("🟢 Haupt-Signal: UP (Bullenmarkt erwartet)")
        elif res["prediction"] == -1:
            st.error("🔴 Haupt-Signal: DOWN (Bärenmarkt / Crash-Gefahr)")
        else:
            st.warning("🟡 Haupt-Signal: FLAT (Seitwärtsmarkt / Inflation schlägt Rendite)")
            
        st.divider()
        st.markdown(f"**Die {len(res['X_opt'].columns)} stärksten Makro-Treiber aktuell:**")
        st.dataframe(res['X_opt'].columns.tolist(), hide_index=True, use_container_width=True)

    with tab2:
        st.subheader("Hedgefonds-Bericht")
        md_path = f"output/feature_selection_{res['timestamp']}.md"
        if os.path.exists(md_path):
            with open(md_path, "r", encoding="utf-8") as f:
                st.markdown(f.read())
        else:
            st.info("Bericht wird generiert oder noch nicht vorhanden.")

    with tab3:
        st.subheader("Out-of-Sample Trefferquote")
        image_path = "output/confusion_matrix.png"
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.info("Keine Confusion Matrix gefunden.")