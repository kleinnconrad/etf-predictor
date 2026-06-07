# scripts/generate_seed.py

import pandas as pd
import os

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # The path to your official Xetra file
    csv_path = os.path.join(project_root, 'config', 't7-xetr-allTradableInstruments.csv')
    output_path = os.path.join(project_root, 'config', 'all_etfs_seed.txt')

    if not os.path.exists(csv_path):
        print(f"Error: Please save the Xetra-Dump at:\n{csv_path}")
        return

    print("Reading official Xetra instruments (T7)...")
    
    # skiprows=2 ignores the first two metadata rows of the Deutsche Börse
    # sep=';' because the exchange uses semicolons
    try:
        df = pd.read_csv(csv_path, sep=';', skiprows=2, low_memory=False)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # 1. Filter only ETFs and ETCs (Exchange Traded Commodities like Xetra-Gold)
    if 'Instrument Type' not in df.columns or 'Mnemonic' not in df.columns:
        print("Error: The expected columns 'Instrument Type' or 'Mnemonic' are missing.")
        return

    etf_df = df[df['Instrument Type'].isin(['ETF', 'ETC'])].copy()
    
    # 2. Filter currency
    # We only keep instruments traded in Euro (EUR)
    if 'Currency' in etf_df.columns:
        etf_df = etf_df[etf_df['Currency'] == 'EUR']
    
    # 3. Build tickers for Yahoo Finance (append .DE for Xetra)
    # 'SXR8' becomes 'SXR8.DE'
    yahoo_tickers = etf_df['Mnemonic'].astype(str).str.strip().str.upper() + ".DE"
    
    # 4. Remove duplicates (for safety)
    unique_tickers = sorted(list(set(yahoo_tickers.tolist())))

    # Write to the text file for your pipeline
    with open(output_path, 'w') as f:
        for ticker in unique_tickers:
            f.write(f"{ticker}\n")

    print("\n" + "="*50)
    print(f"Successfully saved {len(unique_tickers)} EUR ETFs to {output_path}.")
    print(f"Seed universe saved at: {output_path}")
    print("="*50)
    print("You can now run 'python scripts/build_etf_batch.py' to filter the list by age/liquidity.")

if __name__ == "__main__":
    main()