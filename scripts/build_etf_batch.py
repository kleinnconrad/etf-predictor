# scripts/build_etf_batch.py

import yfinance as yf
import pandas as pd
import json
import os
from datetime import datetime, timedelta

# 1. Das massiv erweiterte Seed-Universum (ca. 350 Ticker)
SEED_UNIVERSE = {
    "US_Broad_Large": [
        "SPY", "QQQ", "DIA", "IWM", "VOO", "VTI", "IVV", "RSP", "SCHX", "VV", 
        "ITOT", "IWB", "IWD", "IWF", "IWY", "IWX", "SPYG", "SPYV", "VUG", "VTV",
        "SCHG", "SCHV", "OEF", "RPG", "RPV", "MGK", "MGV", "MGC", "IUSG", "IUSV"
    ],
    "US_Mid_Small": [
        "MDY", "IJH", "IJR", "SCHA", "SCHB", "VBR", "VBK", "VB", "VO", "VOE", 
        "VOT", "IWN", "IWO", "IWC", "SLY", "SLYG", "SLYV", "MDYG", "MDYV", "XMHQ",
        "RWJ", "XMLV", "XSLV", "FNDX", "FNDA", "FNDB", "PRFZ", "SPSM", "DES", "DON"
    ],
    "Factors_Dividends": [
        "VIG", "VYM", "SDY", "QUAL", "VLUE", "MTUM", "USMV", "SCHD", "DGRO", "DVY", 
        "HDV", "FVD", "NOBL", "SPLV", "SPHD", "RDIV", "PEY", "DTD", "DON", "DES",
        "DHS", "DLN", "DGRW", "FDVV", "VDC", "COWZ", "SYLD", "PKW", "DEF", "QDF"
    ],
    "Sectors_Tech_Comm": [
        "XLK", "XLC", "SMH", "VGT", "VOX", "IYW", "IGV", "SOXX", "FTEC", "IXN", 
        "IGN", "IGM", "QTEC", "SKYY", "CIBR", "HACK", "FDN", "PNQI", "TECL", "SOXL"
    ],
    "Sectors_Health_Bio": [
        "XLV", "VHT", "IBB", "XBI", "IHI", "IYH", "FHLC", "PJP", "IHE", "IXJ", 
        "RXD", "CURE", "SBIO", "BBC", "BBP"
    ],
    "Sectors_Finance_RealEstate": [
        "XLF", "VFH", "KRE", "IYF", "KBE", "IAI", "IAT", "EUFN", "IXG", "FNCL", 
        "VNQ", "SCHH", "IYR", "XLRE", "REET", "RWR", "ICF", "FREL", "USRT", "MORT", 
        "REM", "KBWY", "ROIC", "REZ", "FRI"
    ],
    "Sectors_Energy_Materials": [
        "XLE", "VDE", "XOP", "OIH", "IYE", "FENY", "IXC", "FCG", "NLR", "PXE", 
        "XLB", "VAW", "XME", "IYM", "FMAT", "GDX", "GDXJ", "SIL", "SILJ", "COPX", 
        "REMX", "PICK", "LIT", "URNM", "URA"
    ],
    "Sectors_Industrials_Consumer": [
        "XLI", "VIS", "IYJ", "FIDU", "EXI", "ITA", "JETS", "PPA", "XAR", "XTN", 
        "XLY", "VCR", "IYC", "FDIS", "RXI", "XRT", "PEJ", "PBS", "XLP", "VDC", 
        "IYK", "FSTA", "KXI", "PBJ"
    ],
    "Sectors_Defensive": [
        "XLU", "VPU", "IDU", "FUTY", "JXI"
    ],
    "International_Developed": [
        "EFA", "VEA", "IEFA", "SCHF", "EZU", "VGK", "EWJ", "EWC", "EWU", "EWG", 
        "EWH", "EWA", "EWI", "EWQ", "EWP", "EWL", "EWD", "EWN", "EWS", "EFV", 
        "EFG", "HEDJ", "DXJ", "HEFA", "EUDG", "DOO", "DBEF", "DBJP", "FNDF"
    ],
    "International_Emerging": [
        "EEM", "VWO", "IEMG", "MCHI", "INDA", "EWZ", "EWT", "EWY", "FXI", "KWEB", 
        "ASHR", "EPHE", "EIDO", "THD", "EWM", "EZA", "TUR", "EWW", "ARGT", "ECH", 
        "EPU", "EPU", "ILF", "GMF", "CQQQ", "CHIQ", "EPI", "INDY"
    ],
    "Fixed_Income_US_Treasury": [
        "TLT", "IEF", "SHY", "GOVT", "BIL", "SHV", "VGIT", "VGLT", "VGSH", "SCHO", 
        "SCHR", "SPTL", "TLO", "EDV", "ZROZ", "IEI", "TLH", "PLW"
    ],
    "Fixed_Income_Corp_HighYield": [
        "LQD", "HYG", "VCIT", "VCSH", "JNK", "IGSB", "IGIB", "USIG", "SPSB", "SPIB", 
        "SPLB", "SJNK", "FALN", "ANGL", "HYD", "CWB", "PHB", "HYLB"
    ],
    "Fixed_Income_Broad_Muni": [
        "BND", "AGG", "MBB", "MUB", "BSV", "BIV", "BLV", "SPAB", "SCHZ", "BNDW", 
        "FLOT", "SRLN", "TIP", "VTIP", "STIP", "SCHP", "TFI", "NYF", "CMF", "SUB"
    ],
    "Fixed_Income_International": [
        "BNDX", "VWOB", "IGOV", "BWX", "EMB", "PCY", "EBND", "LEMB"
    ],
    "Commodities_Broad": [
        "GLD", "SLV", "USO", "UNG", "DBA", "PDBC", "GSG", "CPER", "IAU", "PPLT", 
        "PALL", "GLTR", "DBC", "BNO", "CORN", "WEAT", "SOYB", "SGOL", "SIVR", 
        "BAR", "CMDY", "COM", "FTGC", "GCC", "GSP", "DJP", "RJI", "USCI", "JJC"
    ]
}

# 2. Filter-Metriken
MIN_YEARS_HISTORY = 10
MIN_AVG_DAILY_VOLUME = 1000000
TARGET_BATCH_SIZE = 200  # Angehoben auf 200

def check_etf_eligibility(ticker):
    """Prüft, ob der ETF alt genug und liquide genug für die Pipeline ist."""
    try:
        etf = yf.Ticker(ticker)
        hist = etf.history(period="max")
        
        if hist.empty:
            return False, "Keine Datenbank-Einträge."

        # 1. Check: Alter des ETFs
        first_date = hist.index[0].tz_localize(None)
        cutoff_date = datetime.now() - timedelta(days=365 * MIN_YEARS_HISTORY)
        
        if first_date > cutoff_date:
            return False, f"Zu jung (Start: {first_date.strftime('%Y-%m-%d')})"

        # 2. Check: Liquidität (Durchschnittliches Volumen der letzten 60 Tage)
        recent_volume = hist['Volume'].tail(60).mean()
        if recent_volume < MIN_AVG_DAILY_VOLUME:
            return False, f"Zu illiquide (Volumen: {recent_volume:,.0f})"

        return True, "Bestanden"
        
    except Exception as e:
        return False, f"API Fehler: {str(e)}"

def main():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starte dynamische Selektion von {TARGET_BATCH_SIZE} ETFs...")
    
    valid_etfs = []
    category_queues = {cat: list(tickers) for cat, tickers in SEED_UNIVERSE.items()}
    
    # Round-Robin Logik, um eine extrem ausgeglichene Diversifikation zu garantieren
    while len(valid_etfs) < TARGET_BATCH_SIZE:
        added_in_round = False
        
        for category, queue in category_queues.items():
            if len(valid_etfs) >= TARGET_BATCH_SIZE:
                break
                
            if queue:
                ticker = queue.pop(0)  # Nimm den ersten ETF aus der Kategorie
                print(f"Prüfe {ticker} ({category})...", end=" ")
                is_valid, reason = check_etf_eligibility(ticker)
                
                if is_valid:
                    valid_etfs.append(ticker)
                    added_in_round = True
                    print(f"[OK] - Status: {len(valid_etfs)}/{TARGET_BATCH_SIZE}")
                else:
                    print(f"[REJECTED] - {reason}")
                    
        # Abbruchbedingung, falls alle Listen leer sind, aber das Ziel nicht erreicht wurde
        if not added_in_round and all(len(q) == 0 for q in category_queues.values()):
            print("\nWARNUNG: Seed-Universum ausgeschöpft, bevor das Target erreicht wurde.")
            break
                
    print("\n" + "="*40)
    print(f"Selektion abgeschlossen. {len(valid_etfs)} ETFs validiert.")
    
    # 3. Speichern der Batch-Liste
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'batch_targets.json')
    
    with open(output_path, 'w') as f:
        json.dump({
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_count": len(valid_etfs),
            "tickers": valid_etfs
        }, f, indent=4)
        
    print(f"Batch-Ziele gespeichert unter: {output_path}")

if __name__ == "__main__":
    main()