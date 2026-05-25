import os
import sys
from google import genai

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    # File paths (assuming script runs from repo root)
    config_path = 'src/config.py'
    catalog_path = 'docs/var_catalog.md'

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_content = f.read()
        with open(catalog_path, 'r', encoding='utf-8') as f:
            catalog_content = f.read()
    except FileNotFoundError as e:
        print(f"Error reading files: {e}")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are a technical documenter for a quantitative finance pipeline.
    Compare the financial tickers and indicators defined in the lists of this config.py file 
    with the existing markdown table in var_catalog.md.
    
    Identify any variable in config.py that is missing from the markdown table.

    Generate ONLY the missing table rows in this exact markdown format:
    | `ticker_1M_ret`, `ticker_3M_ret`, `ticker_6M_ret` | Full Name | Brief Description | Category (as named in config.py) | Source (Yahoo Finance or FRED) |

    Rules:
    - The code abbreviation must be lowercase and stripped of special characters (e.g., ^TNX becomes tnx, CL=F becomes cl, BRK-B becomes brkb, SAP.DE becomes sap).
    - Do not output table headers. Do not output markdown codeblock backticks (```).
    - If there are no missing variables, output the exact string "NO_MISSING_VARIABLES".

    === config.py ===
    {config_content}

    === var_catalog.md ===
    {catalog_content}
    """

    print("Checking for missing catalog entries...")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        new_rows = response.text.strip()

        if new_rows and "NO_MISSING_VARIABLES" not in new_rows:
            with open(catalog_path, 'a', encoding='utf-8') as f:
                # Ensure we start on a new line
                if not catalog_content.endswith('\n'):
                    f.write('\n')
                f.write(new_rows + '\n')
            print("Successfully appended new variables to var_catalog.md:")
            print(new_rows)
        else:
            print("Catalog is already up to date. No changes made.")

    except Exception as e:
        print(f"Error during LLM generation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()