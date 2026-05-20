# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-20 12:17:18
- **Target ETF:** SPY
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-19** prognostiziert das Modell:

> **Klasse:** Up 🟢
>
> **Wahrscheinlichkeiten:** Down: 31.53% | Flat: 5.13% | Up: 63.34%

---

## Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| 9984.T_6M | 0.473802 |
| AAPL_3M | 0.336194 |
| SAP.DE_3M | 0.233382 |
| SHEL.L_6M | 0.229335 |
| AAPL_1M | 0.122061 |
| GC=F_6M | 0.074420 |
| XBI_6M | 0.072574 |
| AZN.L_3M | 0.071036 |

## Aussortierte Prädiktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* 

`8035.T_1M, 9984.T_1M, BAS.DE_1M, BRK-B_1M, CL=F_1M, DX-Y.NYB_1M, EEM_1M, GC=F_1M, HG=F_1M, JPM_1M, NVDA_1M, RIO.L_1M, SAP.DE_1M, SHEL.L_1M, SPY_1M, XBI_1M, XLE_1M, ^GDAXI_1M, ^IRX_1M, ^N225_1M, ^TNX_1M, ^VIX_1M, 7203.T_3M, 8035.T_3M, 9984.T_3M, BAS.DE_3M, BRK-B_3M, CL=F_3M, DX-Y.NYB_3M, EEM_3M, GC=F_3M, HG=F_3M, JPM_3M, MSFT_3M, NVDA_3M, RIO.L_3M, SHEL.L_3M, SIE.DE_3M, SPY_3M, XBI_3M, XLE_3M, XLF_3M, XLK_3M, ^GDAXI_3M, ^IRX_3M, ^N225_3M, ^TNX_3M, ^VIX_3M, 7203.T_6M, 8035.T_6M, AAPL_6M, AZN.L_6M, BAS.DE_6M, BRK-B_6M, CL=F_6M, DX-Y.NYB_6M, EEM_6M, HG=F_6M, JPM_6M, MSFT_6M, NVDA_6M, RIO.L_6M, SAP.DE_6M, SIE.DE_6M, SPY_6M, XLE_6M, XLF_6M, XLK_6M, ^GDAXI_6M, ^IRX_6M, ^N225_6M, ^TNX_6M`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>7</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>

`7203.T_1M, AZN.L_1M, MSFT_1M, SIE.DE_1M, XLF_1M, XLK_1M, ^VIX_6M`

</details>

---

## KI-Interpretation der Prädiktoren (Hedgefonds Analyst)

**1. Makroökonomisches Setup:**

*   **Zins- & Währungsindikatoren:** Explizite Zins- oder Währungspaare wurden *nicht* direkt selektiert. Dies deutet darauf hin, dass die Modellarchitektur die impliziten Auswirkungen von Geldpolitik und relativer Währungsstärke primär über die Discountfaktoren und Cashflow-Bewertungen der selektierten Aktien (insbesondere Wachstums- und Technologieaktien) erfasst, anstatt direkte Zins-Spreads oder FX-Volatilität als führend zu identifizieren.
*   **Rohstoffe:** Die Selektion von `SHEL.L_6M` unterstreicht die anhaltende Relevanz von Energierohstoffpreisen als Indikator für globale Industrienachfrage und Inflationstrends. `GC=F_6M` als Gold-Future-Momentum signalisiert persistente Risikowahrnehmungen, Inflationserwartungen oder eine Flucht in Sicherheit in einem mittel- bis langfristigen Horizont. Die gemeinsame Präsenz signalisiert eine Notwendigkeit zur Korrelation von Rohstoffpreisdynamik und Breitenmarkt-Risikoperzeption.

**2. Sektor- & Marktdynamik:**

*   **Dominanz der globalen Tech-Riesen (9984.T, AAPL, SAP.DE):** Die hohe Gewichtung von SoftBank (Tech-Venture Capital/Asien), Apple (Konsumtechnologie/Global) und SAP (Enterprise Software/Europa) signalisiert eine entscheidende Abhängigkeit des SPY-Ausblicks von globaler Technologie-Adoption, Unternehmensinvestitionen in Digitalisierung und Konsumlaune. Dies deutet auf eine späte zyklische Wachstumsphase oder einen Technologieführungsmarkt hin, in dem Innovation und Digitalisierung die Treiber sind.
*   **Zyklische vs. Defensive Balance:** Die Präsenz von `SHEL.L_6M` (Energie/Rohstoffzyklus) neben `XBI_6M` (hochbeta Biopharma, risikobereites Wachstum) sowie `AZN.L_3M` (defensive Pharma) und `GC=F_6M` (Safe Haven) indiziert ein Marktregime, das sowohl Wachstumschancen (Tech, Biotech) als auch fundamentale Risikofaktoren (Inflation, Geopolitik, defensiver Sektor) über verschiedene Zeithorizonte aktiv monitort. Die Sektor-Rotation ist fragmentiert, zeigt aber eine Tendenz zur Wachstumsorientierung, die durch fundamentale Sensitivitäten unterlegt ist.
*   **Geografische Diversifizierung:** Die breite geografische Streuung (Japan, USA, Deutschland, UK) der führenden Equity-Indikatoren bestätigt eine tiefe globale Marktintegration, bei der regionale Entwicklungen und Sektor-Performance außerhalb der USA signifikant auf den US-Breitenmarkt wirken.

**3. Quant-Konklusion:**

*   **SPY-Ausblick (6M):** Der SPY-Ausblick wird primär durch die *Momentum-Performance globaler Technologieführer* (SoftBank, Apple, SAP) bestimmt, was auf eine Fortsetzung des strukturellen Wachstums und eine hohe Risikobereitschaft im Tech-Sektor hindeutet.
*   **Subtile Risikosteuerung:** Eine sekundäre, aber substanzielle Rolle spielen Rohstoffpreise (SHEL) für Inflationserwartungen und Safe-Haven-Assets (GC=F) sowie defensive Sektoren (AZN.L) für die Risikobereitschaft. Dies impliziert, dass das positive Tech-Narrativ durch persistente makroökonomische Unsicherheiten (Inflation, Zinsen, Geopolitik) moderiert wird, die ein potenzielles Downside-Risiko darstellen.
*   **Marktcharakterisierung:** Der Markt ist in den nächsten 6 Monaten durch eine Kombination aus *Tech-led Growth Optimism* und einer *diskreten, aber konstanten Vigilanz gegenüber makroökonomischen "Tail-Risiken"* gekennzeichnet, welche über Rohstoffmärkte und traditionelle Safe-Haven-Assets signalisiert werden.

# Variablen-Audit

> Dieses Dokument protokolliert alle berechneten Momentum-Variablen der Pipeline. Es erklärt transparent, welche Variablen aktiv Vorhersagen treffen, welche aufgrund redundanter Informationen (Multikollinearität) vom Algorithmus ignoriert wurden, und welche Variablen keine statistische Relevanz (ANOVA F-Test) aufwiesen.

| Variable | Klarname | Status | p-Wert (ANOVA) | Einfluss (Modell) | Ökonomische Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **9984.T_6M** | SoftBank Group Corp. | 🟢 Aktiv (Gewählt) | 3.25e-36 | 0.4738 | Japanischer Investmentkonzern mit Beteiligungen an Technologie- und Telekommunikationsunternehmen weltweit; spiegelt Risikobereitschaft und Bewertungen im Tech-Investment-Sektor wider. |
| **XBI_6M** | SPDR S&P Biotech ETF | 🟢 Aktiv (Gewählt) | 4.17e-31 | 0.0726 | Börsengehandelter Fonds, der kleine bis mittelgroße US-Biotech-Unternehmen abbildet; Indikator für Innovationen und Risikobereitschaft im Biotechnologiesektor. |
| **SHEL.L_6M** | Shell PLC | 🟢 Aktiv (Gewählt) | 1.30e-16 | 0.2293 | Einer der größten Energiekonzerne der Welt; spiegelt die Entwicklungen auf dem Öl- und Gasmarkt sowie die globale Energienachfrage wider. |
| **AAPL_3M** | Apple Inc. | 🟢 Aktiv (Gewählt) | 9.64e-14 | 0.3362 | Größtes Technologieunternehmen der Welt; repräsentiert die Stärke des breiten US-Konsum- und Techsektors. |
| **AAPL_1M** | Apple Inc. | 🟢 Aktiv (Gewählt) | 4.23e-09 | 0.1221 | Größtes Technologieunternehmen der Welt; repräsentiert die Stärke des breiten US-Konsum- und Techsektors. |
| **AZN.L_3M** | AstraZeneca PLC | 🟢 Aktiv (Gewählt) | 1.13e-07 | 0.0710 | Globales Pharma- und Biotechnologieunternehmen; Indikator für die Dynamik im Gesundheitssektor und die europäische Wirtschaft. |
| **GC=F_6M** | Gold Futures | 🟢 Aktiv (Gewählt) | 1.04e-05 | 0.0744 | Misst den Goldpreis; oft als sicherer Hafen in Zeiten wirtschaftlicher Unsicherheit und als Inflationsschutz betrachtet. |
| **SAP.DE_3M** | SAP SE | 🟢 Aktiv (Gewählt) | 5.94e-05 | 0.2334 | Größter europäischer Softwarehersteller; Indikator für Investitionen in Unternehmenssoftware und die digitale Transformation europäischer Unternehmen. |
| **DX-Y.NYB_6M** | US Dollar Index (DXY) | 🟡 Verworfen (Multikollinearität) | 2.13e-64 | - | Misst den Wert des US-Dollars gegenüber einem Korb wichtiger Währungen; beeinflusst internationale Handelsströme, Rohstoffpreise und Kapitalflüsse. |
| **DX-Y.NYB_3M** | US Dollar Index (DXY) | 🟡 Verworfen (Multikollinearität) | 1.61e-62 | - | Misst den Wert des US-Dollars gegenüber einem Korb wichtiger Währungen; beeinflusst internationale Handelsströme, Rohstoffpreise und Kapitalflüsse. |
| **HG=F_6M** | Kupfer Futures | 🟡 Verworfen (Multikollinearität) | 9.52e-60 | - | Misst den Kupferpreis; gilt als 'Dr. Copper', ein wichtiger Frühindikator für die globale Industriekonjunktur und Bauwirtschaft. |
| **EEM_6M** | iShares MSCI Emerging Markets ETF | 🟡 Verworfen (Multikollinearität) | 5.14e-49 | - | Börsengehandelter Fonds, der die Performance von Aktien aus Schwellenländern abbildet; Indikator für das globale Wachstumspotenzial außerhalb entwickelter Märkte. |
| **^IRX_6M** | US 13-Wochen Treasury Bill Rendite | 🟡 Verworfen (Multikollinearität) | 4.85e-48 | - | Misst die Rendite kurzfristiger US-Staatsanleihen; ein wichtiger Indikator für die aktuelle Geldpolitik und Liquidität im Finanzsystem. |
| **HG=F_3M** | Kupfer Futures | 🟡 Verworfen (Multikollinearität) | 6.91e-48 | - | Misst den Kupferpreis; gilt als 'Dr. Copper', ein wichtiger Frühindikator für die globale Industriekonjunktur und Bauwirtschaft. |
| **AZN.L_6M** | AstraZeneca PLC | 🟡 Verworfen (Multikollinearität) | 2.51e-45 | - | Globales Pharma- und Biotechnologieunternehmen; Indikator für die Dynamik im Gesundheitssektor und die europäische Wirtschaft. |
| **BAS.DE_6M** | BASF SE | 🟡 Verworfen (Multikollinearität) | 9.52e-30 | - | Weltgrößter Chemiekonzern; ein Frühindikator für die globale Industriekonjunktur und Rohstoffpreisentwicklung. |
| **^IRX_3M** | US 13-Wochen Treasury Bill Rendite | 🟡 Verworfen (Multikollinearität) | 3.49e-29 | - | Misst die Rendite kurzfristiger US-Staatsanleihen; ein wichtiger Indikator für die aktuelle Geldpolitik und Liquidität im Finanzsystem. |
| **SIE.DE_6M** | Siemens AG | 🟡 Verworfen (Multikollinearität) | 6.58e-28 | - | Globaler Technologiekonzern mit Fokus auf Industrie, Infrastruktur und Mobilität; ein Frühindikator für die deutsche und europäische Industrieproduktion. |
| **RIO.L_6M** | Rio Tinto PLC | 🟡 Verworfen (Multikollinearität) | 1.00e-27 | - | Einer der weltgrößten Bergbaukonzerne; spiegelt die Nachfrage nach Basismetallen und Eisenerz sowie die globale Industriekonjunktur wider. |
| **EEM_3M** | iShares MSCI Emerging Markets ETF | 🟡 Verworfen (Multikollinearität) | 1.58e-25 | - | Börsengehandelter Fonds, der die Performance von Aktien aus Schwellenländern abbildet; Indikator für das globale Wachstumspotenzial außerhalb entwickelter Märkte. |
| **DX-Y.NYB_1M** | US Dollar Index (DXY) | 🟡 Verworfen (Multikollinearität) | 3.41e-25 | - | Misst den Wert des US-Dollars gegenüber einem Korb wichtiger Währungen; beeinflusst internationale Handelsströme, Rohstoffpreise und Kapitalflüsse. |
| **^GDAXI_6M** | DAX Performance Index | 🟡 Verworfen (Multikollinearität) | 4.80e-25 | - | Leitindex für den deutschen Aktienmarkt; repräsentiert die Wertentwicklung der 40 größten und liquidesten Unternehmen in Deutschland. |
| **XLE_6M** | Energy Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 9.16e-23 | - | Börsengehandelter Fonds, der die größten US-Energieunternehmen abbildet; dient als Barometer für den US-Energiesektor und die Entwicklung von Öl- und Gaspreisen. |
| **JPM_6M** | JPMorgan Chase & Co. | 🟡 Verworfen (Multikollinearität) | 1.24e-21 | - | Eine der größten US-Banken; dient als Barometer für die Gesundheit des Finanzsektors und die US-Wirtschaft. |
| **8035.T_6M** | Tokyo Electron Ltd. | 🟡 Verworfen (Multikollinearität) | 1.97e-20 | - | Führender Hersteller von Halbleiterfertigungsanlagen; wichtiger Indikator für Investitionszyklen in der globalen Technologiebranche. |
| **8035.T_3M** | Tokyo Electron Ltd. | 🟡 Verworfen (Multikollinearität) | 3.27e-18 | - | Führender Hersteller von Halbleiterfertigungsanlagen; wichtiger Indikator für Investitionszyklen in der globalen Technologiebranche. |
| **AAPL_6M** | Apple Inc. | 🟡 Verworfen (Multikollinearität) | 3.32e-18 | - | Größtes Technologieunternehmen der Welt; repräsentiert die Stärke des breiten US-Konsum- und Techsektors. |
| **^N225_6M** | Nikkei 225 Stock Average | 🟡 Verworfen (Multikollinearität) | 4.46e-17 | - | Leitindex für den japanischen Aktienmarkt; spiegelt die Wertentwicklung der 225 größten Unternehmen in Japan wider. |
| **XLE_3M** | Energy Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 8.33e-17 | - | Börsengehandelter Fonds, der die größten US-Energieunternehmen abbildet; dient als Barometer für den US-Energiesektor und die Entwicklung von Öl- und Gaspreisen. |
| **GC=F_3M** | Gold Futures | 🟡 Verworfen (Multikollinearität) | 4.20e-15 | - | Misst den Goldpreis; oft als sicherer Hafen in Zeiten wirtschaftlicher Unsicherheit und als Inflationsschutz betrachtet. |
| **NVDA_6M** | NVIDIA Corp. | 🟡 Verworfen (Multikollinearität) | 1.63e-13 | - | Führender Hersteller von Grafikprozessoren; Schlüsselindikator für Innovationen in den Bereichen KI, Gaming und High-Performance-Computing. |
| **JPM_3M** | JPMorgan Chase & Co. | 🟡 Verworfen (Multikollinearität) | 1.16e-11 | - | Eine der größten US-Banken; dient als Barometer für die Gesundheit des Finanzsektors und die US-Wirtschaft. |
| **^GDAXI_3M** | DAX Performance Index | 🟡 Verworfen (Multikollinearität) | 1.78e-11 | - | Leitindex für den deutschen Aktienmarkt; repräsentiert die Wertentwicklung der 40 größten und liquidesten Unternehmen in Deutschland. |
| **BAS.DE_3M** | BASF SE | 🟡 Verworfen (Multikollinearität) | 8.71e-11 | - | Weltgrößter Chemiekonzern; ein Frühindikator für die globale Industriekonjunktur und Rohstoffpreisentwicklung. |
| **^TNX_1M** | US 10-Year Treasury Yield | 🟡 Verworfen (Multikollinearität) | 1.02e-10 | - | Misst die Rendite 10-jähriger US-Staatsanleihen; ein zentraler Indikator für langfristige Zins- und Inflationserwartungen. |
| **NVDA_3M** | NVIDIA Corp. | 🟡 Verworfen (Multikollinearität) | 1.04e-10 | - | Führender Hersteller von Grafikprozessoren; Schlüsselindikator für Innovationen in den Bereichen KI, Gaming und High-Performance-Computing. |
| **SAP.DE_6M** | SAP SE | 🟡 Verworfen (Multikollinearität) | 1.51e-10 | - | Größter europäischer Softwarehersteller; Indikator für Investitionen in Unternehmenssoftware und die digitale Transformation europäischer Unternehmen. |
| **HG=F_1M** | Kupfer Futures | 🟡 Verworfen (Multikollinearität) | 2.43e-10 | - | Misst den Kupferpreis; gilt als 'Dr. Copper', ein wichtiger Frühindikator für die globale Industriekonjunktur und Bauwirtschaft. |
| **9984.T_3M** | SoftBank Group Corp. | 🟡 Verworfen (Multikollinearität) | 4.62e-10 | - | Japanischer Investmentkonzern mit Beteiligungen an Technologie- und Telekommunikationsunternehmen weltweit; spiegelt Risikobereitschaft und Bewertungen im Tech-Investment-Sektor wider. |
| **RIO.L_3M** | Rio Tinto PLC | 🟡 Verworfen (Multikollinearität) | 5.05e-09 | - | Einer der weltgrößten Bergbaukonzerne; spiegelt die Nachfrage nach Basismetallen und Eisenerz sowie die globale Industriekonjunktur wider. |
| **CL=F_6M** | Rohöl WTI Futures | 🟡 Verworfen (Multikollinearität) | 2.32e-07 | - | Misst den Preis für Rohöl der Sorte West Texas Intermediate; ein Schlüsselindikator für Inflation, Transportkosten und globale Wirtschaftstätigkeit. |
| **^TNX_3M** | US 10-Year Treasury Yield | 🟡 Verworfen (Multikollinearität) | 3.29e-07 | - | Misst die Rendite 10-jähriger US-Staatsanleihen; ein zentraler Indikator für langfristige Zins- und Inflationserwartungen. |
| **XBI_3M** | SPDR S&P Biotech ETF | 🟡 Verworfen (Multikollinearität) | 9.06e-07 | - | Börsengehandelter Fonds, der kleine bis mittelgroße US-Biotech-Unternehmen abbildet; Indikator für Innovationen und Risikobereitschaft im Biotechnologiesektor. |
| **XLE_1M** | Energy Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 2.00e-06 | - | Börsengehandelter Fonds, der die größten US-Energieunternehmen abbildet; dient als Barometer für den US-Energiesektor und die Entwicklung von Öl- und Gaspreisen. |
| **BRK-B_3M** | Berkshire Hathaway Inc. Class B | 🟡 Verworfen (Multikollinearität) | 2.46e-06 | - | Konglomerat unter der Führung von Warren Buffett; Indikator für Value-Investing und die Performance diversifizierter US-Wirtschaftssektoren. |
| **SIE.DE_3M** | Siemens AG | 🟡 Verworfen (Multikollinearität) | 1.87e-05 | - | Globaler Technologiekonzern mit Fokus auf Industrie, Infrastruktur und Mobilität; ein Frühindikator für die deutsche und europäische Industrieproduktion. |
| **BAS.DE_1M** | BASF SE | 🟡 Verworfen (Multikollinearität) | 1.88e-05 | - | Weltgrößter Chemiekonzern; ein Frühindikator für die globale Industriekonjunktur und Rohstoffpreisentwicklung. |
| **SHEL.L_3M** | Shell PLC | 🟡 Verworfen (Multikollinearität) | 2.32e-05 | - | Einer der größten Energiekonzerne der Welt; spiegelt die Entwicklungen auf dem Öl- und Gasmarkt sowie die globale Energienachfrage wider. |
| **XLK_6M** | Technology Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 3.67e-05 | - | Börsengehandelter Fonds, der die größten US-Technologieunternehmen abbildet; dient als Barometer für den US-Technologiesektor. |
| **GC=F_1M** | Gold Futures | 🟡 Verworfen (Multikollinearität) | 4.50e-05 | - | Misst den Goldpreis; oft als sicherer Hafen in Zeiten wirtschaftlicher Unsicherheit und als Inflationsschutz betrachtet. |
| **XLF_6M** | Financial Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 4.83e-05 | - | Börsengehandelter Fonds, der die größten US-Finanzunternehmen abbildet; Indikator für die Gesundheit des US-Banken- und Finanzsektors. |
| **EEM_1M** | iShares MSCI Emerging Markets ETF | 🟡 Verworfen (Multikollinearität) | 8.40e-05 | - | Börsengehandelter Fonds, der die Performance von Aktien aus Schwellenländern abbildet; Indikator für das globale Wachstumspotenzial außerhalb entwickelter Märkte. |
| **XBI_1M** | SPDR S&P Biotech ETF | 🟡 Verworfen (Multikollinearität) | 1.36e-04 | - | Börsengehandelter Fonds, der kleine bis mittelgroße US-Biotech-Unternehmen abbildet; Indikator für Innovationen und Risikobereitschaft im Biotechnologiesektor. |
| **MSFT_6M** | Microsoft Corp. | 🟡 Verworfen (Multikollinearität) | 4.22e-04 | - | Führendes Software- und Cloud-Computing-Unternehmen; repräsentiert die Stärke des Technologie- und Unternehmenssoftware-Sektors. |
| **^VIX_3M** | CBOE Volatility Index (VIX) | 🟡 Verworfen (Multikollinearität) | 9.82e-04 | - | Misst die erwartete kurzfristige Volatilität des S&P 500 Index; oft als 'Angstbarometer' des Marktes bezeichnet. |
| **MSFT_3M** | Microsoft Corp. | 🟡 Verworfen (Multikollinearität) | 0.0015 | - | Führendes Software- und Cloud-Computing-Unternehmen; repräsentiert die Stärke des Technologie- und Unternehmenssoftware-Sektors. |
| **SPY_6M** | SPDR S&P 500 ETF Trust | 🟡 Verworfen (Multikollinearität) | 0.0027 | - | Börsengehandelter Fonds, der die Wertentwicklung des S&P 500 Index abbildet; der meistbeachtete Indikator für die Performance des breiten US-Aktienmarktes. |
| **BRK-B_1M** | Berkshire Hathaway Inc. Class B | 🟡 Verworfen (Multikollinearität) | 0.0038 | - | Konglomerat unter der Führung von Warren Buffett; Indikator für Value-Investing und die Performance diversifizierter US-Wirtschaftssektoren. |
| **^IRX_1M** | US 13-Wochen Treasury Bill Rendite | 🟡 Verworfen (Multikollinearität) | 0.0045 | - | Misst die Rendite kurzfristiger US-Staatsanleihen; ein wichtiger Indikator für die aktuelle Geldpolitik und Liquidität im Finanzsystem. |
| **XLF_3M** | Financial Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 0.0066 | - | Börsengehandelter Fonds, der die größten US-Finanzunternehmen abbildet; Indikator für die Gesundheit des US-Banken- und Finanzsektors. |
| **7203.T_6M** | Toyota Motor Corporation | 🟡 Verworfen (Multikollinearität) | 0.0070 | - | Größter Automobilhersteller der Welt; repräsentiert die Gesundheit des globalen Automobilsektors und der japanischen Exportwirtschaft. |
| **JPM_1M** | JPMorgan Chase & Co. | 🟡 Verworfen (Multikollinearität) | 0.0214 | - | Eine der größten US-Banken; dient als Barometer für die Gesundheit des Finanzsektors und die US-Wirtschaft. |
| **NVDA_1M** | NVIDIA Corp. | 🟡 Verworfen (Multikollinearität) | 0.0239 | - | Führender Hersteller von Grafikprozessoren; Schlüsselindikator für Innovationen in den Bereichen KI, Gaming und High-Performance-Computing. |
| **^GDAXI_1M** | DAX Performance Index | 🟡 Verworfen (Multikollinearität) | 0.0256 | - | Leitindex für den deutschen Aktienmarkt; repräsentiert die Wertentwicklung der 40 größten und liquidesten Unternehmen in Deutschland. |
| **XLK_3M** | Technology Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 0.0299 | - | Börsengehandelter Fonds, der die größten US-Technologieunternehmen abbildet; dient als Barometer für den US-Technologiesektor. |
| **BRK-B_6M** | Berkshire Hathaway Inc. Class B | 🟡 Verworfen (Multikollinearität) | 0.0397 | - | Konglomerat unter der Führung von Warren Buffett; Indikator für Value-Investing und die Performance diversifizierter US-Wirtschaftssektoren. |
| **^TNX_6M** | US 10-Year Treasury Yield | 🟡 Verworfen (Multikollinearität) | 0.0554 | - | Misst die Rendite 10-jähriger US-Staatsanleihen; ein zentraler Indikator für langfristige Zins- und Inflationserwartungen. |
| **SHEL.L_1M** | Shell PLC | 🟡 Verworfen (Multikollinearität) | 0.0591 | - | Einer der größten Energiekonzerne der Welt; spiegelt die Entwicklungen auf dem Öl- und Gasmarkt sowie die globale Energienachfrage wider. |
| **CL=F_3M** | Rohöl WTI Futures | 🟡 Verworfen (Multikollinearität) | 0.0612 | - | Misst den Preis für Rohöl der Sorte West Texas Intermediate; ein Schlüsselindikator für Inflation, Transportkosten und globale Wirtschaftstätigkeit. |
| **SPY_3M** | SPDR S&P 500 ETF Trust | 🟡 Verworfen (Multikollinearität) | 0.0662 | - | Börsengehandelter Fonds, der die Wertentwicklung des S&P 500 Index abbildet; der meistbeachtete Indikator für die Performance des breiten US-Aktienmarktes. |
| **8035.T_1M** | Tokyo Electron Ltd. | 🟡 Verworfen (Multikollinearität) | 0.0714 | - | Führender Hersteller von Halbleiterfertigungsanlagen; wichtiger Indikator für Investitionszyklen in der globalen Technologiebranche. |
| **^VIX_1M** | CBOE Volatility Index (VIX) | 🟡 Verworfen (Multikollinearität) | 0.1147 | - | Misst die erwartete kurzfristige Volatilität des S&P 500 Index; oft als 'Angstbarometer' des Marktes bezeichnet. |
| **^N225_3M** | Nikkei 225 Stock Average | 🟡 Verworfen (Multikollinearität) | 0.1153 | - | Leitindex für den japanischen Aktienmarkt; spiegelt die Wertentwicklung der 225 größten Unternehmen in Japan wider. |
| **SAP.DE_1M** | SAP SE | 🟡 Verworfen (Multikollinearität) | 0.1169 | - | Größter europäischer Softwarehersteller; Indikator für Investitionen in Unternehmenssoftware und die digitale Transformation europäischer Unternehmen. |
| **SPY_1M** | SPDR S&P 500 ETF Trust | 🟡 Verworfen (Multikollinearität) | 0.2286 | - | Börsengehandelter Fonds, der die Wertentwicklung des S&P 500 Index abbildet; der meistbeachtete Indikator für die Performance des breiten US-Aktienmarktes. |
| **RIO.L_1M** | Rio Tinto PLC | 🟡 Verworfen (Multikollinearität) | 0.2717 | - | Einer der weltgrößten Bergbaukonzerne; spiegelt die Nachfrage nach Basismetallen und Eisenerz sowie die globale Industriekonjunktur wider. |
| **9984.T_1M** | SoftBank Group Corp. | 🟡 Verworfen (Multikollinearität) | 0.3080 | - | Japanischer Investmentkonzern mit Beteiligungen an Technologie- und Telekommunikationsunternehmen weltweit; spiegelt Risikobereitschaft und Bewertungen im Tech-Investment-Sektor wider. |
| **7203.T_3M** | Toyota Motor Corporation | 🟡 Verworfen (Multikollinearität) | 0.3442 | - | Größter Automobilhersteller der Welt; repräsentiert die Gesundheit des globalen Automobilsektors und der japanischen Exportwirtschaft. |
| **^N225_1M** | Nikkei 225 Stock Average | 🟡 Verworfen (Multikollinearität) | 0.3524 | - | Leitindex für den japanischen Aktienmarkt; spiegelt die Wertentwicklung der 225 größten Unternehmen in Japan wider. |
| **CL=F_1M** | Rohöl WTI Futures | 🟡 Verworfen (Multikollinearität) | 0.4551 | - | Misst den Preis für Rohöl der Sorte West Texas Intermediate; ein Schlüsselindikator für Inflation, Transportkosten und globale Wirtschaftstätigkeit. |
| **XLK_1M** | Technology Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.4552 | - | Börsengehandelter Fonds, der die größten US-Technologieunternehmen abbildet; dient als Barometer für den US-Technologiesektor. |
| **AZN.L_1M** | AstraZeneca PLC | 🔴 Verworfen (Keine Signifikanz) | 0.4568 | - | Globales Pharma- und Biotechnologieunternehmen; Indikator für die Dynamik im Gesundheitssektor und die europäische Wirtschaft. |
| **7203.T_1M** | Toyota Motor Corporation | 🔴 Verworfen (Keine Signifikanz) | 0.6134 | - | Größter Automobilhersteller der Welt; repräsentiert die Gesundheit des globalen Automobilsektors und der japanischen Exportwirtschaft. |
| **^VIX_6M** | CBOE Volatility Index (VIX) | 🔴 Verworfen (Keine Signifikanz) | 0.6223 | - | Misst die erwartete kurzfristige Volatilität des S&P 500 Index; oft als 'Angstbarometer' des Marktes bezeichnet. |
| **XLF_1M** | Financial Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.7607 | - | Börsengehandelter Fonds, der die größten US-Finanzunternehmen abbildet; Indikator für die Gesundheit des US-Banken- und Finanzsektors. |
| **MSFT_1M** | Microsoft Corp. | 🔴 Verworfen (Keine Signifikanz) | 0.7995 | - | Führendes Software- und Cloud-Computing-Unternehmen; repräsentiert die Stärke des Technologie- und Unternehmenssoftware-Sektors. |
| **SIE.DE_1M** | Siemens AG | 🔴 Verworfen (Keine Signifikanz) | 0.8435 | - | Globaler Technologiekonzern mit Fokus auf Industrie, Infrastruktur und Mobilität; ein Frühindikator für die deutsche und europäische Industrieproduktion. |

## Mathematische Modellparameter

- **Intercepts:** `[-0.08668891609152833, -1.5708409703966066, 1.6575298864881338]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.16190333  0.47287942  0.08380908 -0.19488734 -0.63759673 -0.04406737
   0.29264159 -0.09244559]
 [ 0.02118795  0.03141228  0.02274425 -0.15518541 -0.07310679 -0.06756288
   0.05136124 -0.01641559]
 [-0.18309129 -0.5042917  -0.10655333  0.35007275  0.71070353  0.11163025
  -0.34400283  0.10886118]]
  ```
