def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben (z.B. 1000 oder 5.5).")

def calculate_sparkasse_fee(volume):
    """
    Berechnet die Gebühr: 1 % vom Kurswert, gedeckelt auf maximal 200 €.
    """
    fee = volume * 0.01 
    return min(fee, 200.0)

def main():
    print("--- ETF Rendite-Rechner (Deutschland) ---\n")
    
    # Eingaben
    anlagebetrag = get_float_input("Anlagebetrag in Euro: ")
    rendite_pa_prozent = get_float_input("Erwartete Bruttorendite (% p.a.): ")
    ter_pa_prozent = get_float_input("ETF Gebühren (TER in % p.a.): ")
    haltedauer_jahre = get_float_input("Haltedauer (in Jahren): ")
    
    # 1. Kaufkosten
    kauf_gebuehr = calculate_sparkasse_fee(anlagebetrag)
    tatsaechliches_investment = anlagebetrag
    gesamtaufwand = anlagebetrag + kauf_gebuehr
    
    # 2. Wertentwicklung (Brutto nach TER)
    # Die TER reduziert die jährliche Bruttorendite
    effektive_rendite_pa = (rendite_pa_prozent - ter_pa_prozent) / 100.0
    endwert_etf = tatsaechliches_investment * ((1 + effektive_rendite_pa) ** haltedauer_jahre)
    
    # 3. Verkaufskosten
    verkauf_gebuehr = calculate_sparkasse_fee(endwert_etf)
    
    # 4. Steuerberechnung
    # Gewinn vor Steuern (nach Abzug der Kauf- und Verkaufskosten, wie vom Finanzamt anerkannt)
    reiner_kursgewinn = endwert_etf - tatsaechliches_investment
    gewinn_vor_steuern = reiner_kursgewinn - kauf_gebuehr - verkauf_gebuehr
    
    # Steuerberechnung greift nur bei positivem Gewinn
    steuern = 0.0
    if gewinn_vor_steuern > 0:
        # 30% Teilfreistellung für Aktien-ETFs
        steuerpflichtiger_gewinn = gewinn_vor_steuern * 0.7 
        # 25% Abgeltungssteuer + 5,5% Soli = 26,375%
        steuersatz = 0.26375 
        steuern = steuerpflichtiger_gewinn * steuersatz
        
    # 5. Netto-Auszahlung
    netto_auszahlung = endwert_etf - verkauf_gebuehr - steuern
    netto_gewinn_euro = netto_auszahlung - gesamtaufwand
    
    # 6. Rendite in Prozent
    brutto_gewinn_euro = endwert_etf - anlagebetrag
    
    # Annualisierte Nettorendite (CAGR)
    if gesamtaufwand > 0:
        netto_rendite_pa_prozent = ((netto_auszahlung / gesamtaufwand) ** (1 / haltedauer_jahre) - 1) * 100
    else:
        netto_rendite_pa_prozent = 0.0

    # 7. Ausgabe der Ergebnisse
    print("\n--- Auswertung ---")
    print(f"Endwert des ETF (vor Verkauf):   {endwert_etf:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Bruttogewinn (Euro):             {brutto_gewinn_euro:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    
    print("\n--- Kosten & Steuern ---")
    print(f"Kaufgebühr (Sparkasse):          {kauf_gebuehr:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Verkaufsgebühr (Sparkasse):      {verkauf_gebuehr:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Abgeltungssteuer inkl. Soli:     {steuern:,.2f} € (unter Berücksichtigung von 30% Teilfreistellung)".replace(',', 'X').replace('.', ',').replace('X', '.'))
    total_kosten = kauf_gebuehr + verkauf_gebuehr + steuern
    print(f"Gesamte Abzüge:                  {total_kosten:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    
    print("\n--- Netto Ergebnis ---")
    print(f"Netto-Auszahlung aufs Konto:     {netto_auszahlung:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Nettogewinn (Euro):              {netto_gewinn_euro:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Nettorendite (% p.a.):           {netto_rendite_pa_prozent:.2f} %")

if __name__ == "__main__":
    main()
  
