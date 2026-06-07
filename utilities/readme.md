# ETF Return Calculator (Germany)

## Table of Contents
- [Features](#features)
- [How to Use](#how-to-use)

## Features

* **True Compound Interest:** Calculates long-term growth by accurately compounding the annual returns over the holding period.
* **Invisible TER Effect:** Automatically deducts the Total Expense Ratio (TER) from the gross return and visualizes the absolute euro amount lost to fund management fees.
* **Realistic Broker Fees:** Incorporates standard transaction costs for buying and selling (1% of the order volume, capped at a maximum of 200 € per trade).
* **German Taxation Logic:** Automatically calculates the *Abgeltungssteuer* (capital gains tax) and *Solidaritätszuschlag* (solidarity surcharge) totaling 26.375%. It correctly applies the 30% *Teilfreistellung* (partial tax exemption) legally granted for equity ETFs.

## How to Use

1. Ensure you have Python installed on your system.
2. Save the script as `etf_calculator.py`.
3. Run the script via your terminal:

```bash
python etf_calculator.py
