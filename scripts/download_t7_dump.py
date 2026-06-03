# scripts/download_t7_dump.py

import os
import requests
import sys

def main():
    # Direct link to the Xetra T7 allTradableInstruments.csv dump
    csv_url = "https://www.cashmarket.deutsche-boerse.com/resource/blob/1528/6249e15bf93885fd91bd411663a0ff82/data/t7-xetr-allTradableInstruments.csv"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"Initiating direct download from: {csv_url}")
    
    try:
        csv_response = requests.get(csv_url, headers=headers, timeout=30)
        csv_response.raise_for_status()
    except Exception as e:
        print(f"Error downloading the CSV file: {e}")
        sys.exit(1)
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, 'config')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 't7-xetr-allTradableInstruments.csv')
    
    with open(output_path, 'wb') as f:
        f.write(csv_response.content)
        
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Success! Downloaded {file_size_mb:.2f} MB to {output_path}")

if __name__ == "__main__":
    main()
