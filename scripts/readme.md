# Scripts

This directory contains auxiliary modules for data preparation and documentation lifecycle management.

* `build_etf_batch.py`: Filters the ETF seed list based on historical data depth and trading liquidity. Validates instruments requiring a minimum 10-year trading history and 1 million EUR average daily turnover. Exports the validated list as a JSON batch configuration.
* `download_t7_dump.py`: Retrieves the Xetra T7 all tradable instruments dump from the official exchange portal via a direct static URL download.
* `generate_seed.py`: Parses raw Xetra T7 instrument data to extract tradeable EUR-denominated ETFs and ETCs. Formats mnemonics for external API compatibility and outputs a deduplicated text seed list.
* `update_catalog.py`: Automates variable documentation synchronisation. Uses an LLM API to cross-reference macroeconomic indicators and engineered interaction ratios defined in the source code against the markdown catalog, appending missing entries.
