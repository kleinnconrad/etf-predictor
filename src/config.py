# src/config.py

import os
from datetime import datetime, timedelta

# ==========================================
# 1. DYNAMISCHE ZEITFENSTER
# ==========================================
END_DATE = datetime.today().strftime('%Y-%m-%d')
# 10 Jahre Historie für saubere 126-Tage-Features und genug Trainingsdaten
START_DATE = (datetime.today() - timedelta(days=365 * 10)).strftime('%Y-%m-%d')

# ==========================================
# 2. VORHERSAGE-ZIEL & ÖKONOMISCHE PARAMETER
# ==========================================
TARGET_ETF = 'BBUS'
FORECAST_HORIZON_DAYS = 126    # Prognose für 6 Monate in die Zukunft

ANNUAL_INFLATION_RATE = 0.025  # 2,5 % Basis-Wachstum p.a.
ANNUAL_MARGIN = 0.01           # 1,0 % Toleranz-Korridor (Up/Flat/Down)
TRADING_DAYS_PER_YEAR = 252    

# ==========================================
# 3. DAS 360-GRAD INVESTMENT UNIVERSUM
# ==========================================

# Makro-Basics (Zinsen, Volatilität, Währungen)
MACRO_INDICATORS = [
    '^TNX',    # US 10-Year Treasury Yield
    '^IRX',    # 13-Week Treasury Bill 
    '^VIX',    # Volatility Index 
    'DX-Y.NYB',# US Dollar Index
]

# Industrie- & Edelrohstoffe
COMMODITIES = [
    'CL=F',    # Crude Oil 
    'GC=F',    # Gold 
    'HG=F',    # Copper ("Dr. Copper")
]

# Agrar-Rohstoffe (Inflations-Indikatoren)
AGRI_COMMODITIES = [
    'ZC=F',    # Corn (Mais)
    'ZW=F',    # Wheat (Weizen)
    'LE=F',    # Live Cattle (Lebendrind)
]

# Kreditrisiko & Anleihen (Frühindikatoren für Stress)
CREDIT_RISK = [
    'HYG',     # High Yield Corporate Bonds (Junk Bonds)
    'TLT',     # 20+ Year Treasury Bonds (Sicherer Hafen)
    'LQD',     # Investment Grade Corporate Bonds
]

# Breite Sektoren & Internationale Indizes
SECTORS_AND_INDICES = [
    'XLF',     # Financials
    'XLK',     # Technology
    'XLE',     # Energy
    'XBI',     # Biotech
    'EEM',     # Emerging Markets
    '^GDAXI',  # DAX Index
    '^N225',   # Nikkei 225
]

# Sektor-Rotation (Offensiv vs. Defensiv)
MORE_SECTORS = [
    'XLU',     # Utilities (Defensiv)
    'XLP',     # Consumer Staples (Defensiv)
    'XLY',     # Consumer Discretionary (Offensiv/Zyklisch)
    'XLV',     # Healthcare (Defensiv)
]

# Immobilien (Extrem zinssensibel)
REAL_ESTATE = [
    'VNQ',     # Vanguard Real Estate ETF
]

# Alternative Liquidität
CRYPTO = [
    'BTC-USD', # Bitcoin (Proxy für globale Überschussliquidität)
]

# System-relevante Einzelaktien
TICKERS_US = ['AAPL', 'MSFT', 'NVDA', 'BRK-B', 'JPM']
TICKERS_DE = ['SAP.DE', 'SIE.DE', 'BAS.DE']
TICKERS_UK = ['SHEL.L', 'AZN.L', 'RIO.L']
TICKERS_JP = ['7203.T', '9984.T', '8035.T']

def get_all_tickers():
    """Führt das gesamte Universum für die yfinance-Abfrage zusammen."""
    return list(set(
        [TARGET_ETF] + 
        MACRO_INDICATORS + COMMODITIES + AGRI_COMMODITIES + 
        CREDIT_RISK + SECTORS_AND_INDICES + MORE_SECTORS + 
        REAL_ESTATE + CRYPTO + 
        TICKERS_US + TICKERS_DE + TICKERS_UK + TICKERS_JP
    ))

# ==========================================
# 4. LLM CONFIGURATION
# ==========================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")