# src/config.py
import os
from datetime import datetime, timedelta

# --- Dynamische Zeitfenster-Berechnung ---
# END_DATE ist dynamisch der heutige Tag
END_DATE = datetime.today().strftime('%Y-%m-%d')

# START_DATE liegt 10 Jahre zurück. 
# Das gibt ausreichend Puffer für die Feature-Verschiebungen (z.B. 126 Tage Rolling Returns)
START_DATE = (datetime.today() - timedelta(days=365 * 10)).strftime('%Y-%m-%d')

TARGET_ETF = 'SPY'
FORECAST_HORIZON_DAYS = 126  

# Ökonomische Parameter (Annualisiert)
ANNUAL_INFLATION_RATE = 0.025  # 2,5 %
ANNUAL_MARGIN = 0.01           # 1 % (+/-) Korridor
TRADING_DAYS_PER_YEAR = 252    

TICKERS_US = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'BRK-B', 'LLY', 'V', 'JPM']
TICKERS_DE = ['SAP.DE', 'SIE.DE', 'ALV.DE', 'DTE.DE', 'AIR.DE', 'VOW3.DE', 'MBG.DE', 'BMW.DE', 'BAS.DE', 'MUV2.DE']
TICKERS_UK = ['SHEL.L', 'AZN.L', 'HSBA.L', 'ULVR.L', 'BP.L', 'GSK.L', 'REL.L', 'DGE.L', 'BATS.L', 'RIO.L']
TICKERS_JP = ['7203.T', '6758.T', '8306.T', '9984.T', '6861.T', '9432.T', '8035.T', '9983.T', '4063.T', '8058.T']

def get_all_tickers():
    return list(set([TARGET_ETF] + TICKERS_US + TICKERS_DE + TICKERS_UK + TICKERS_JP))

# LLM Configuration (Loaded securely from GitHub Codespaces Environment)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")