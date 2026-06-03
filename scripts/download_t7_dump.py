# scripts/download_t7_dump.py

import os
import requests
from bs4 import BeautifulSoup
import sys

def main():
    url = "https://www.xetra.com/xetra-en/instruments/all-tradable-instruments"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"Fetching Xetra instruments portal: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"Error accessing Xetra portal: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")
    
    csv_url = None
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'allTradableInstruments.csv' in href:
            csv_url = href
            break
            
    if not csv_url:
        print("Error: Could not locate the dynamic CSV download link on the page.")
        print("The page structure might have changed or requires JavaScript rendering.")
        sys.exit(1)

    if not csv_url.startswith('http'):
        csv_url = "https://www.xetra.com" + csv_url
        
    print(f"Extracted dynamic download URL: {csv_url}")
    print("Initiating download...")
    
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
