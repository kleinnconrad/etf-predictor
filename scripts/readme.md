# Scripts Directory Overview

This directory contains utility scripts for data preparation and documentation maintenance.

* `generate_seed.py`: Processes the Xetra T7 instrument data. It extracts exchange-traded funds and commodities traded in euros, formats the mnemonics for API compatibility, and writes a deduplicated seed list to a text file.
* `build_etf_batch.py`: Evaluates the eligibility of the generated seed list. It implements a multithreaded screening process to verify a minimum trading history of 10 years and a minimum daily turnover of one million euros. The validated tickers are exported as a JSON batch file.
* `update_catalog.py`: Maintains the variable documentation. It utilizes an LLM API to cross-reference the codebase with the existing documentation catalog. Missing financial features or engineered ratios are identified and automatically appended to the documentation.
