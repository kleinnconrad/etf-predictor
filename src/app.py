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
    ANNUAL_MARGIN_UP, 
    ANNUAL_MARGIN_DOWN,
    TRADING_DAYS_PER_YEAR,
    TARGET_ETF,
    get_all_tickers
)

st.set_page_config(page_title="Quant Engine", layout="wide")

@st.cache_data(ttl=43200, show_spinner=False)
def get_data(target_ticker, download_list, _timestamp):
    return load_and_prepare_data(
        target_ticker=target_ticker,
        all_tickers=download_list,
        start_date=START_DATE,
        end_date=END_DATE,
        forecast_horizon=FORECAST_HORIZON_DAYS,
        annual_inflation=ANNUAL_INFLATION_RATE,
        annual_margin_up=ANNUAL_MARGIN_UP,
        annual_margin_down=ANNUAL_MARGIN_DOWN,
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
    st.title("Steuerung")
    target_ticker = st.text_input("Ziel-ETF Ticker", value=TARGET_ETF).upper()
    st.divider()
    
    st.caption("Modell-Parameter")
    st.write(f"**Prognose-Horizont:** {FORECAST_HORIZON_DAYS} Tage")
    st.write(f"**Basis-Inflation:** {ANNUAL_INFLATION_RATE*100}%")
    st.write(f"**Up-Marge:** +{ANNUAL_MARGIN_UP*100}%")
    st.write(f"**Down-Marge:** -{ANNUAL_MARGIN_DOWN*100}%")
    
    st.divider()
    run_button = st.button("Analyse starten", use_container_width=True)

st.markdown('<p class="hero-header">ETF Prediction Engine</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Multinomial logistic regression</p>', unsafe_allow_html=True)

if run_button:
    timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
    
    with st.status("Initialisiere Modell...", expanded=True) as status:
        import time 
        
        st.write("Lade Daten...")
        download_list = get_all_tickers()
        if target_ticker not in download_list:
            download_list.append(target_ticker)
            
        X, y, latest = get_data(target_ticker, tuple(download_list), timestamp)
        time.sleep(0.5) 
        
        st.write("Fuehre ANOVA-Filter aus...")
        time.sleep(0.5)
        
        st.write("Starte Sequential Feature Selection...")
        results_dict = train_quant_model(X, y, latest, target_ticker, timestamp)
        
        st.write("KS-Cutoff und generiere Audit-Reports...")
        time.sleep(0.5)
        
        st.session_state.results = results_dict
        st.session_state.results["timestamp"] = timestamp
        st.session_state.analysis_done = True
        
        status.update(label="Analyse erfolgreich abgeschlossen.", state="complete")

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
    
    if not res["is_valid_quality"]:
        st.error(f"Quality Gate nicht bestanden. Die Cross-Validation Accuracy ({res['cv_accuracy']:.2%}) ist zu niedrig.")
        st.warning("Das Modell liefert auf dem aktuellen Daten-Subset keine Edge, die statistisch signifikant ueber reinem Raten liegt.")
    
    else:
        tab1, tab2, tab3, tab4 = st.tabs(["Uebersicht", "LLM Analyse", "Modell-Diagnostik", "Variablen-Audit"])
        
        with tab1:
            st.subheader("Aktuelle Modell-Prognose")
            
            if res["prediction"] == 1:
                st.success("Haupt-Signal: UP (Bullenmarkt erwartet)")
            elif res["prediction"] == -1:
                st.error("Haupt-Signal: DOWN (Baerenmarkt / Crash-Gefahr)")
            else:
                st.warning("Haupt-Signal: FLAT (Seitwaertsmarkt / Inflation schlaegt Rendite)")
                
            st.caption(f"Sensitivitaet fuer Down-Signal datengetrieben optimiert (KS-Cutoff: {res['ks_cutoff']:.2%})")
            
            st.markdown("### Wahrscheinlichkeitsverteilung")
            probs = res["probabilities"]
            p_down = probs.get(-1, 0)
            p_flat = probs.get(0, 0)
            p_up = probs.get(1, 0)
            
            col_d, col_f, col_u = st.columns(3)
            col_d.metric("Down (Crash)", f"{p_down:.1%}")
            col_f.metric("Flat (Seitwaerts)", f"{p_flat:.1%}")
            col_u.metric("Up (Bullenmarkt)", f"{p_up:.1%}")
            
            st.divider()
            st.markdown("**Die staerksten Makro-Treiber aktuell:**")
            st.dataframe(res['X_optimal'].columns.tolist(), hide_index=True, use_container_width=True)

        with tab2:
            st.subheader("Google Gemini interpretation")
            md_path = f"output/feature_selection_{res['timestamp']}.md"
            if os.path.exists(md_path):
                with open(md_path, "r", encoding="utf-8") as f:
                    st.markdown(f.read())
            else:
                st.info("Bericht wird im Hintergrund generiert oder ist nicht verfuegbar.")

        with tab3:
            st.subheader("Modell-Diagnostik")
            st.markdown("""
            Ein robustes Quant-Modell darf historische Daten nicht nur auswendig lernen (Overfitting). 
            Die wahre Qualitaet zeigt sich in der **Out-of-Sample** Matrix rechts.
            """)
            
            col1, col2 = st.columns(2)
            with col1:
                if "cm_fig_train" in res:
                    st.pyplot(res["cm_fig_train"], use_container_width=True)
            with col2:
                if "cm_fig_cv" in res:
                    st.pyplot(res["cm_fig_cv"], use_container_width=True)

        with tab4:
            st.subheader("Variablen-Audit")
            st.markdown("Dokumentation der statistischen Signifikanz aller potenziellen Praediktoren.")
            
            audit_path = f"output/variable_audit_{res['timestamp']}.md"
            if os.path.exists(audit_path):
                with open(audit_path, "r", encoding="utf-8") as f:
                    st.markdown(f.read())
            else:
                st.info("Das Variablen-Audit wurde fuer diesen Lauf nicht gefunden. Stelle sicher, dass `generate_variable_audit_table` erfolgreich durchlaeuft.")
                
