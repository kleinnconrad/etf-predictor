# scripts/update_catalog.py

import os
import sys
from google import genai

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    # File paths
    config_path = 'src/config.py'
    pipeline_path = 'src/data_pipeline.py'
    catalog_path = 'docs/var_catalog.md'

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_content = f.read()
        with open(pipeline_path, 'r', encoding='utf-8') as f:
            pipeline_content = f.read()
        with open(catalog_path, 'r', encoding='utf-8') as f:
            catalog_content = f.read()
    except FileNotFoundError as e:
        print(f"Error reading files: {e}")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are a technical documenter for a quantitative finance pipeline.
    You need to compare the variables defined in the codebase with the existing markdown table in var_catalog.md.
    
    Identify any variable that is missing from the markdown table. Look in two places:
    1. Financial tickers and indicators in the lists of config.py.
    2. Engineered interaction ratios in data_pipeline.py (look for the string names passed to the `safe_ratio` function, e.g., 'ratio_copper_gold').

    Generate ONLY the missing table rows in this exact markdown format:
    | `ticker_1M_ret`, `ticker_3M_ret`, `ticker_6M_ret` | Full Name | Brief Description | Category | Source |

    Rules:
    - For config.py tickers: The code abbreviation must be lowercase and stripped of special characters (e.g., ^TNX becomes tnx, CL=F becomes cl).
    - For data_pipeline.py ratios: Use the exact string name from the safe_ratio call (e.g., ratio_copper_gold) and append _1M_ret, _3M_ret, _6M_ret.
    - Category for engineered ratios should be "ENGINEERED INTERACTIONS". Source should be "Pipeline Transformation".
    - Do not output table headers. Do not output markdown codeblock backticks (```).
    - If there are no missing variables, output the exact string "NO_MISSING_VARIABLES".

    === config.py ===
    {config_content}
    
    === data_pipeline.py ===
    {pipeline_content}

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