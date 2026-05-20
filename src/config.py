# src/config.py

import os
from datetime import datetime, timedelta

# ==========================================
# 1. DYNAMISCHE ZEITFENSTER
# ==========================================
# END_DATE ist immer der tagesaktuelle Lauf
END_DATE = datetime.today().strftime('%Y-%m-%d')

# START_DATE liegt exakt 10 Jahre zurück, um dem Modell genug 
# Historie für das Training und die 126-Tage-Features zu geben.
START_DATE = (datetime.today() - timedelta(days=365 * 10)).strftime('%Y-%m-%d')

# ==========================================
# 2. VORHERSAGE-ZIEL & ÖKONOMISCHE PARAMETER
# ==========================================
TARGET_ETF = 'SPY'
FORECAST_HORIZON_DAYS = 126    # Prognose für 6 Monate in die Zukunft

ANNUAL_INFLATION_RATE = 0.025  # 2,5 % Basis-Wachstum (Inflation) p.a.
ANNUAL_MARGIN = 0.01           # 1,0 % Toleranz-Korridor (Up/Flat/Down)
TRADING_DAYS_PER_YEAR = 252    

# ==========================================
# 3. INVESTMENT UNIVERSUM (Features)
# ==========================================

# Globale Makro-Indikatoren (Zinsen, Volatilität, Währungen)
MACRO_INDICATORS = [
    '^TNX',    # US 10-Year Treasury Yield (Langfristige Zinsen)
    '^IRX',    # 13-Week Treasury Bill (Kurzfristige Zinsen)
    '^VIX',    # Volatility Index (Angst-Barometer)
    'DX-Y.NYB',# US Dollar Index
]

# Rohstoffe (Inflations- und Konjunktur-Signale)
COMMODITIES = [
    'CL=F',    # Crude Oil (Konjunkturmotor)
    'GC=F',    # Gold (Sicherer Hafen)
    'HG=F',    # Kupfer (Frühindikator für Industrie)
]

# Breite Sektoren & Märkte
SECTORS_AND_INDICES = [
    'XLF',     # US Financials ETF
    'XLK',     # US Technology ETF
    'XLE',     # US Energy ETF
    'XBI',     # Biotech ETF (Zinssensibel)
    'EEM',     # Emerging Markets ETF
    '^GDAXI',  # DAX Index (Deutschland - Exportlastig)
    '^N225',   # Nikkei 225 (Japan)
]

# System-relevante Einzelaktien (Fokussiert)
TICKERS_US = ['AAPL', 'MSFT', 'NVDA', 'BRK-B', 'JPM']
TICKERS_DE = ['SAP.DE', 'SIE.DE', 'BAS.DE']
TICKERS_UK = ['SHEL.L', 'AZN.L', 'RIO.L']
TICKERS_JP = ['7203.T', '9984.T', '8035.T']

def get_all_tickers():
    """Führt das gesamte Universum für die yfinance-Abfrage zusammen."""
    return list(set(
        [TARGET_ETF] + 
        MACRO_INDICATORS + 
        COMMODITIES + 
        SECTORS_AND_INDICES + 
        TICKERS_US + TICKERS_DE + TICKERS_UK + TICKERS_JP
    ))

# ==========================================
# 4. LLM CONFIGURATION
# ==========================================
# Wird sicher als Umgebungsvariable über die GitHub Codespace Secrets geladen
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")