# src/config.py

import os
from datetime import datetime, timedelta

# ==========================================
# 1. DYNAMISCHE ZEITFENSTER
# ==========================================
END_DATE = datetime.today().strftime('%Y-%m-%d')
# 10 Jahre Historie für saubere 126-Tage-Features und genug Trainingsdaten
START_DATE = (datetime.today() - timedelta(days=365 * 10.5)).strftime('%Y-%m-%d')

# ==========================================
# 2. VORHERSAGE-ZIEL & ÖKONOMISCHE PARAMETER
# ==========================================
TARGET_ETF = 'DBXJ.DE'
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

# Federal Reserve Data (US)
FRED_INDICATORS = [
    'CPIAUCSL',  # US CPI (Inflation)
    'PAYEMS',    # US Nonfarm Payrolls
    'UNRATE',    # US Unemployment
    'T10Y2Y',    # US 10Y-2Y Yield Spread
    'WALCL'      # US Fed Total Assets
]

# FRED: Eurozone & Germany Macro
FRED_INDICATORS_EU = [
    'CP00MI15EA20M086NEST', # Euro Area CPI (Inflation)
    'LRHUTTTTEZM156S',   # Euro Area Unemployment Rate
    'ECBASSETS',         # ECB Total Assets (Systemic Liquidity)
    'PRINTO01EZQ661S'    # Euro Area Industrial Production
]

# FRED: Japan Macro
FRED_INDICATORS_JP = [
    'JPNCPIALLMINMEI',   # Japan CPI
    'LRHUTTTTJPM156S',   # Japan Unemployment Rate
    'JPNASSETS',         # Bank of Japan Total Assets
    'JPNPROINDMISMEI'    # Japan Industrial Production
]

# FRED: UK Macro
FRED_INDICATORS_UK = [
    'GBRCPIALLMINMEI',   # UK CPI
    'LRHUTTTTGBM156S',   # UK Unemployment Rate
    'GBRPROINDMISMEI'    # UK Industrial Production
]

# Yahoo Finance: International Sovereign Bond Yields (ETF Proxies)
SOVEREIGN_YIELDS = [
    'IGOV',  # iShares International Treasury Bond ETF (Heavy exposure to Eurozone/Japan)
    'BWX',   # SPDR Bloomberg International Treasury Bond ETF (Broad non-US sovereign debt)
    'BNDX'   # Vanguard Total International Bond ETF (Hedged non-US bonds)
]

# Combine all FRED indicators for the pipeline
ALL_FRED_INDICATORS = FRED_INDICATORS + FRED_INDICATORS_EU + FRED_INDICATORS_JP + FRED_INDICATORS_UK

# ==========================================
# MASTER TICKER LIST (BATCH & SINGLE RUN)
# ==========================================
# 'SPY' ist fest integriert, um Data-Drops bei der Berechnung 
# von systemischen Interaktions-Ratios (z.B. SPY/TLT) zu verhindern.
ALL_TICKERS = list(set(
    ['SPY'] + 
    MACRO_INDICATORS + COMMODITIES + AGRI_COMMODITIES + 
    CREDIT_RISK + SECTORS_AND_INDICES + MORE_SECTORS + 
    REAL_ESTATE + CRYPTO + 
    TICKERS_US + TICKERS_DE + TICKERS_UK + TICKERS_JP +
    SOVEREIGN_YIELDS
))

def get_all_tickers():
    """Abwärtskompatibilitäts-Funktion für ältere Pipeline-Skripte."""
    return ALL_TICKERS

# ==========================================
# 4. LLM CONFIGURATION
# ==========================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")