# src/config.py

TARGET_ETF = 'SPY'
START_DATE = "2016-01-01"
END_DATE = "2024-01-01"
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