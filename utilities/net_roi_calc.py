def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 1000 or 5.5).")

def calculate_broker_fee(volume):
    """
    Calculates the fee: 1% of the order volume, capped at a maximum of 200 €.
    """
    fee = volume * 0.01 
    return min(fee, 200.0)

def main():
    print("--- ETF Return Calculator (Germany) ---\n")
    
    # Inputs
    investment_amount = get_float_input("Investment amount in Euro: ")
    expected_gross_return_pa = get_float_input("Expected gross return (% p.a.): ")
    etf_ter_pa = get_float_input("ETF fees (TER in % p.a.): ")
    holding_period_years = get_float_input("Holding period (in years): ")
    
    # 1. Buy costs
    buy_fee = calculate_broker_fee(investment_amount)
    actual_investment = investment_amount
    total_investment_cost = investment_amount + buy_fee
    
    # 2. Value development (Gross after TER)
    # The TER reduces the annual gross return
    effective_return_pa = (expected_gross_return_pa - etf_ter_pa) / 100.0
    etf_end_value = actual_investment * ((1 + effective_return_pa) ** holding_period_years)
    
    # 3. Sell costs
    sell_fee = calculate_broker_fee(etf_end_value)
    
    # 4. Tax calculation
    # Profit before taxes (after deducting buy and sell costs, as recognized by the tax office)
    pure_capital_gain = etf_end_value - actual_investment
    pre_tax_profit = pure_capital_gain - buy_fee - sell_fee
    
    # Tax calculation only applies to positive profits
    taxes = 0.0
    if pre_tax_profit > 0:
        # 30% partial tax exemption (Teilfreistellung) for equity ETFs
        taxable_profit = pre_tax_profit * 0.7 
        # 25% capital gains tax (Abgeltungssteuer) + 5.5% solidarity surcharge = 26.375%
        tax_rate = 0.26375 
        taxes = taxable_profit * tax_rate
        
    # 5. Net payout
    net_payout = etf_end_value - sell_fee - taxes
    net_profit_euro = net_payout - total_investment_cost
    
    # 6. Return in percent
    gross_profit_euro = etf_end_value - investment_amount
    
    # Annualized net return (CAGR)
    if total_investment_cost > 0:
        net_return_pa_percent = ((net_payout / total_investment_cost) ** (1 / holding_period_years) - 1) * 100
    else:
        net_return_pa_percent = 0.0

    # 7. Output of results
    print("\n--- Evaluation ---")
    print(f"End value of the ETF (before sale): {etf_end_value:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Gross profit (Euro):                {gross_profit_euro:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    
    print("\n--- Costs & Taxes ---")
    print(f"Buy fee (Broker):                   {buy_fee:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Sell fee (Broker):                  {sell_fee:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Capital gains tax (incl. Soli):     {taxes:,.2f} € (considering 30% tax exemption)".replace(',', 'X').replace('.', ',').replace('X', '.'))
    total_costs = buy_fee + sell_fee + taxes
    print(f"Total deductions:                   {total_costs:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    
    print("\n--- Net Result ---")
    print(f"Net payout to bank account:         {net_payout:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Net profit (Euro):                  {net_profit_euro:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Net return (% p.a.):                {net_return_pa_percent:.2f} %")

if __name__ == "__main__":
    main()
    
