# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-20 13:49:14
- **Target ETF:** SPY
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-19** prognostiziert das Modell:

> **Klasse:** Down 🔴
>
> **Wahrscheinlichkeiten:** Down: 47.41% | Flat: 39.07% | Up: 13.53%

---

## Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| VNQ_6M | 0.546894 |
| ^GDAXI_6M | 0.464495 |
| ZW=F_6M | 0.311735 |
| ^IRX_6M | 0.280370 |
| ^TNX_1M | 0.256970 |
| CL=F_6M | 0.151128 |
| SHEL.L_3M | 0.086063 |
| SAP.DE_3M | 0.067068 |

## Aussortierte Prädiktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* 

`AAPL_1M, BAS.DE_1M, BTC-USD_1M, DX-Y.NYB_1M, EEM_1M, GC=F_1M, HG=F_1M, LE=F_1M, LQD_1M, TLT_1M, XBI_1M, XLE_1M, XLP_1M, XLU_1M, ZC=F_1M, ZW=F_1M, 8035.T_3M, 9984.T_3M, AAPL_3M, AZN.L_3M, BAS.DE_3M, BTC-USD_3M, DX-Y.NYB_3M, EEM_3M, GC=F_3M, HG=F_3M, HYG_3M, JPM_3M, LQD_3M, MSFT_3M, NVDA_3M, RIO.L_3M, SIE.DE_3M, TLT_3M, VNQ_3M, XBI_3M, XLE_3M, XLP_3M, XLU_3M, XLV_3M, ZW=F_3M, ^GDAXI_3M, ^IRX_3M, ^TNX_3M, 8035.T_6M, 9984.T_6M, AAPL_6M, AZN.L_6M, BAS.DE_6M, BTC-USD_6M, DX-Y.NYB_6M, EEM_6M, GC=F_6M, HG=F_6M, HYG_6M, JPM_6M, LE=F_6M, LQD_6M, MSFT_6M, NVDA_6M, RIO.L_6M, SAP.DE_6M, SHEL.L_6M, SIE.DE_6M, XBI_6M, XLE_6M, XLF_6M, XLK_6M, XLP_6M, XLU_6M, XLV_6M, ^N225_6M`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>43</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>

`7203.T_1M, 8035.T_1M, 9984.T_1M, AZN.L_1M, BRK-B_1M, CL=F_1M, HYG_1M, JPM_1M, MSFT_1M, NVDA_1M, RIO.L_1M, SAP.DE_1M, SHEL.L_1M, SIE.DE_1M, SPY_1M, VNQ_1M, XLF_1M, XLK_1M, XLV_1M, XLY_1M, ^GDAXI_1M, ^IRX_1M, ^N225_1M, ^VIX_1M, 7203.T_3M, BRK-B_3M, CL=F_3M, LE=F_3M, SPY_3M, XLF_3M, XLK_3M, XLY_3M, ZC=F_3M, ^N225_3M, ^VIX_3M, 7203.T_6M, BRK-B_6M, SPY_6M, TLT_6M, XLY_6M, ZC=F_6M, ^TNX_6M, ^VIX_6M`

</details>

---

## KI-Interpretation der Prädiktoren (Hedgefonds Analyst)

> *Fehler bei der LLM-Abfrage: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}*

# Umfassendes Variablen-Audit (Feature Encyclopedia)

**Generiert am:** 2026-05-20 13:50:00

> Dieses Dokument protokolliert alle berechneten Momentum-Variablen der Pipeline. Es erklärt transparent, welche Variablen aktiv Vorhersagen treffen, welche aufgrund redundanter Informationen (Multikollinearität) vom Algorithmus ignoriert wurden, und welche Variablen keine statistische Relevanz (ANOVA F-Test) aufwiesen.

| Variable | Klarname | Status | p-Wert (ANOVA) | Einfluss (Modell) | Ökonomische Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ZW=F_6M** | Weizen-Futures | 🟢 Aktiv (Gewählt) | 4.77e-72 | 0.3117 | Misst den Preis für Weizen; ein Indikator für Agrarpreise, globale Nahrungsmittelsicherheit und geopolitische Einflüsse auf die Versorgungsketten. |
| **^IRX_6M** | US 13 Week Treasury Bill Yield | 🟢 Aktiv (Gewählt) | 2.68e-40 | 0.2804 | Misst die Rendite kurzfristiger US-Staatsanleihen; ein wichtiger Indikator für die kurzfristige Liquidität und die Erwartungen der Federal Reserve. |
| **^GDAXI_6M** | DAX Performance Index | 🟢 Aktiv (Gewählt) | 6.67e-26 | 0.4645 | Führt die 40 größten und umsatzstärksten deutschen Unternehmen; ein Schlüsselindikator für die Gesundheit der deutschen und europäischen Wirtschaft. |
| **VNQ_6M** | Vanguard Real Estate ETF | 🟢 Aktiv (Gewählt) | 1.18e-21 | 0.5469 | Investiert in US-Immobilien-REITs; ein Stimmungsbarometer für den US-Immobilienmarkt und die Entwicklung der Immobilienpreise und Mieten. |
| **^TNX_1M** | US 10-Year Treasury Yield | 🟢 Aktiv (Gewählt) | 3.66e-13 | 0.2570 | Misst die Rendite 10-jähriger US-Staatsanleihen; ein zentraler Indikator für langfristige Zins- und Inflationserwartungen sowie Kreditkosten. |
| **CL=F_6M** | WTI Rohöl-Futures | 🟢 Aktiv (Gewählt) | 1.73e-07 | 0.1511 | Misst den Preis für Rohöl; ein entscheidender Indikator für globale Wirtschaftswachstumserwartungen, Inflationsdruck und geopolitische Risiken. |
| **SHEL.L_3M** | Shell PLC | 🟢 Aktiv (Gewählt) | 5.78e-06 | 0.0861 | Einer der größten Energiekonzerne weltweit; spiegelt die Entwicklung der globalen Öl- und Gaspreise sowie die Energieversorgung wider. |
| **SAP.DE_3M** | SAP SE | 🟢 Aktiv (Gewählt) | 5.35e-05 | 0.0671 | Europas größter Softwarehersteller; Indikator für die Investitionen von Unternehmen in Geschäftssoftware und die Digitalisierung der europäischen Wirtschaft. |
| **DX-Y.NYB_6M** | US Dollar Index (DXY) | 🟡 Verworfen (Multikollinearität) | 4.47e-57 | - | Misst den Wert des US-Dollars gegenüber einem Korb wichtiger Währungen; beeinflusst globale Handelsströme, Rohstoffpreise und die Geldpolitik der Fed. |
| **DX-Y.NYB_3M** | US Dollar Index (DXY) | 🟡 Verworfen (Multikollinearität) | 9.33e-57 | - | Misst den Wert des US-Dollars gegenüber einem Korb wichtiger Währungen; beeinflusst globale Handelsströme, Rohstoffpreise und die Geldpolitik der Fed. |
| **HG=F_6M** | Kupfer-Futures | 🟡 Verworfen (Multikollinearität) | 8.20e-54 | - | Misst den Preis für Kupfer; wird als 'Dr. Copper' bezeichnet, da er oft als Frühindikator für die globale Industrieproduktion und das Wirtschaftswachstum dient. |
| **EEM_6M** | iShares MSCI Emerging Markets ETF | 🟡 Verworfen (Multikollinearität) | 3.08e-52 | - | Bündelt Aktien aus Schwellenländern; ein Indikator für das Wirtschaftswachstum und die Anlegerstimmung in diesen dynamischen Regionen. |
| **9984.T_6M** | SoftBank Group Corp. | 🟡 Verworfen (Multikollinearität) | 1.50e-40 | - | Japanisches Technologie- und Investment-Konglomerat; Indikator für Risikobereitschaft und Bewertungen im globalen Tech-Start-up-Sektor. |
| **AZN.L_6M** | AstraZeneca PLC | 🟡 Verworfen (Multikollinearität) | 3.44e-39 | - | Führendes Pharma- und Biotechnologieunternehmen; repräsentiert die Stabilität und Innovationskraft des globalen Gesundheitssektors. |
| **XBI_6M** | SPDR S&P Biotech ETF | 🟡 Verworfen (Multikollinearität) | 2.71e-38 | - | Fokussiert auf den Biotechnologiesektor; ein Indikator für Risikobereitschaft und Innovationskraft in der Pharma- und Biotech-Industrie. |
| **BTC-USD_6M** | Bitcoin / US Dollar | 🟡 Verworfen (Multikollinearität) | 8.81e-37 | - | Die größte Kryptowährung; ein Stimmungsbarometer für Risikobereitschaft und ein Frühindikator für die Adaption digitaler Assets. |
| **HG=F_3M** | Kupfer-Futures | 🟡 Verworfen (Multikollinearität) | 6.59e-36 | - | Misst den Preis für Kupfer; wird als 'Dr. Copper' bezeichnet, da er oft als Frühindikator für die globale Industrieproduktion und das Wirtschaftswachstum dient. |
| **^IRX_3M** | US 13 Week Treasury Bill Yield | 🟡 Verworfen (Multikollinearität) | 1.58e-35 | - | Misst die Rendite kurzfristiger US-Staatsanleihen; ein wichtiger Indikator für die kurzfristige Liquidität und die Erwartungen der Federal Reserve. |
| **XLU_6M** | Utilities Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 2.38e-34 | - | Repräsentiert den Versorgersektor des S&P 500; gilt als defensiver Sektor und Indikator für das Anlegerbedürfnis nach Stabilität und Dividenden. |
| **BTC-USD_3M** | Bitcoin / US Dollar | 🟡 Verworfen (Multikollinearität) | 9.60e-34 | - | Die größte Kryptowährung; ein Stimmungsbarometer für Risikobereitschaft und ein Frühindikator für die Adaption digitaler Assets. |
| **BAS.DE_6M** | BASF SE | 🟡 Verworfen (Multikollinearität) | 2.04e-30 | - | Weltgrößter Chemiekonzern; ein wichtiger Frühindikator für die globale Industrieproduktion und Rohstoffnachfrage, insbesondere in Europa. |
| **RIO.L_6M** | Rio Tinto PLC | 🟡 Verworfen (Multikollinearität) | 7.43e-30 | - | Einer der größten Bergbaukonzerne der Welt; ein Barometer für die globale Nachfrage nach Rohstoffen und die Industrieproduktion. |
| **SIE.DE_6M** | Siemens AG | 🟡 Verworfen (Multikollinearität) | 9.46e-29 | - | Globaler Technologiekonzern mit Fokus auf Industrie, Infrastruktur und Mobilität; ein Indikator für die globale Investitionsgüterindustrie und Automatisierungstrends. |
| **ZW=F_3M** | Weizen-Futures | 🟡 Verworfen (Multikollinearität) | 3.64e-25 | - | Misst den Preis für Weizen; ein Indikator für Agrarpreise, globale Nahrungsmittelsicherheit und geopolitische Einflüsse auf die Versorgungsketten. |
| **EEM_3M** | iShares MSCI Emerging Markets ETF | 🟡 Verworfen (Multikollinearität) | 3.80e-25 | - | Bündelt Aktien aus Schwellenländern; ein Indikator für das Wirtschaftswachstum und die Anlegerstimmung in diesen dynamischen Regionen. |
| **DX-Y.NYB_1M** | US Dollar Index (DXY) | 🟡 Verworfen (Multikollinearität) | 2.31e-24 | - | Misst den Wert des US-Dollars gegenüber einem Korb wichtiger Währungen; beeinflusst globale Handelsströme, Rohstoffpreise und die Geldpolitik der Fed. |
| **^N225_6M** | Nikkei 225 Stock Average | 🟡 Verworfen (Multikollinearität) | 2.41e-23 | - | Japans wichtigster Aktienindex; ein Barometer für die Performance des japanischen Aktienmarktes und die globale asiatische Wirtschaftsstimmung. |
| **XLE_6M** | Energy Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 1.86e-22 | - | Repräsentiert den Energiesektor des S&P 500; ein Indikator für die Rentabilität von Öl- und Gasunternehmen und die Energiepreisentwicklung. |
| **XLU_3M** | Utilities Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 4.45e-22 | - | Repräsentiert den Versorgersektor des S&P 500; gilt als defensiver Sektor und Indikator für das Anlegerbedürfnis nach Stabilität und Dividenden. |
| **JPM_6M** | JPMorgan Chase & Co. | 🟡 Verworfen (Multikollinearität) | 1.54e-20 | - | Größte US-Bank; ein führender Indikator für die Gesundheit des Finanzsektors und die allgemeine Wirtschaftslage in den USA. |
| **8035.T_6M** | Tokyo Electron Limited | 🟡 Verworfen (Multikollinearität) | 1.44e-18 | - | Führender Hersteller von Halbleiterproduktionsanlagen; spiegelt die Gesundheit der globalen Tech-Branche und Investitionen in die Digitalisierung wider. |
| **XLE_3M** | Energy Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 1.71e-17 | - | Repräsentiert den Energiesektor des S&P 500; ein Indikator für die Rentabilität von Öl- und Gasunternehmen und die Energiepreisentwicklung. |
| **LQD_3M** | iShares iBoxx $ Investment Grade Corporate Bond ETF | 🟡 Verworfen (Multikollinearität) | 1.55e-16 | - | Investiert in qualitativ hochwertige Unternehmensanleihen; spiegelt die Kreditkosten für große Unternehmen und die Liquidität im Investment-Grade-Segment wider. |
| **SHEL.L_6M** | Shell PLC | 🟡 Verworfen (Multikollinearität) | 1.83e-16 | - | Einer der größten Energiekonzerne weltweit; spiegelt die Entwicklung der globalen Öl- und Gaspreise sowie die Energieversorgung wider. |
| **HYG_6M** | iShares iBoxx $ High Yield Corporate Bond ETF | 🟡 Verworfen (Multikollinearität) | 2.26e-16 | - | Investiert in hochverzinsliche Unternehmensanleihen; ein Barometer für die Risikobereitschaft im Kreditmarkt und die Gesundheit des Unternehmenssektors. |
| **8035.T_3M** | Tokyo Electron Limited | 🟡 Verworfen (Multikollinearität) | 3.51e-16 | - | Führender Hersteller von Halbleiterproduktionsanlagen; spiegelt die Gesundheit der globalen Tech-Branche und Investitionen in die Digitalisierung wider. |
| **LQD_1M** | iShares iBoxx $ Investment Grade Corporate Bond ETF | 🟡 Verworfen (Multikollinearität) | 5.96e-13 | - | Investiert in qualitativ hochwertige Unternehmensanleihen; spiegelt die Kreditkosten für große Unternehmen und die Liquidität im Investment-Grade-Segment wider. |
| **TLT_1M** | iShares 20+ Year Treasury Bond ETF | 🟡 Verworfen (Multikollinearität) | 9.54e-13 | - | Investiert in langfristige US-Staatsanleihen; ein Indikator für langfristige Zinsbewegungen, Inflationserwartungen und Anlegerflucht in Sicherheit. |
| **AAPL_6M** | Apple Inc. | 🟡 Verworfen (Multikollinearität) | 1.10e-12 | - | Weltgrößtes Technologieunternehmen; ein Barometer für den globalen Konsumgüter- und Technologiesektor sowie für die Innovationskraft der US-Wirtschaft. |
| **BTC-USD_1M** | Bitcoin / US Dollar | 🟡 Verworfen (Multikollinearität) | 1.48e-12 | - | Die größte Kryptowährung; ein Stimmungsbarometer für Risikobereitschaft und ein Frühindikator für die Adaption digitaler Assets. |
| **GC=F_3M** | Gold-Futures | 🟡 Verworfen (Multikollinearität) | 3.08e-12 | - | Misst den Preis für Gold; gilt als sicherer Hafen in Krisenzeiten und als Indikator für Inflationserwartungen und die Stärke des US-Dollars. |
| **9984.T_3M** | SoftBank Group Corp. | 🟡 Verworfen (Multikollinearität) | 4.02e-12 | - | Japanisches Technologie- und Investment-Konglomerat; Indikator für Risikobereitschaft und Bewertungen im globalen Tech-Start-up-Sektor. |
| **JPM_3M** | JPMorgan Chase & Co. | 🟡 Verworfen (Multikollinearität) | 1.12e-11 | - | Größte US-Bank; ein führender Indikator für die Gesundheit des Finanzsektors und die allgemeine Wirtschaftslage in den USA. |
| **AAPL_3M** | Apple Inc. | 🟡 Verworfen (Multikollinearität) | 3.29e-11 | - | Weltgrößtes Technologieunternehmen; ein Barometer für den globalen Konsumgüter- und Technologiesektor sowie für die Innovationskraft der US-Wirtschaft. |
| **NVDA_6M** | NVIDIA Corporation | 🟡 Verworfen (Multikollinearität) | 5.58e-11 | - | Führender Hersteller von Grafikprozessoren; ein entscheidender Indikator für die Halbleiterindustrie, KI-Entwicklung und den Gaming-Markt. |
| **LQD_6M** | iShares iBoxx $ Investment Grade Corporate Bond ETF | 🟡 Verworfen (Multikollinearität) | 8.36e-11 | - | Investiert in qualitativ hochwertige Unternehmensanleihen; spiegelt die Kreditkosten für große Unternehmen und die Liquidität im Investment-Grade-Segment wider. |
| **XBI_3M** | SPDR S&P Biotech ETF | 🟡 Verworfen (Multikollinearität) | 1.21e-10 | - | Fokussiert auf den Biotechnologiesektor; ein Indikator für Risikobereitschaft und Innovationskraft in der Pharma- und Biotech-Industrie. |
| **^GDAXI_3M** | DAX Performance Index | 🟡 Verworfen (Multikollinearität) | 1.27e-10 | - | Führt die 40 größten und umsatzstärksten deutschen Unternehmen; ein Schlüsselindikator für die Gesundheit der deutschen und europäischen Wirtschaft. |
| **SAP.DE_6M** | SAP SE | 🟡 Verworfen (Multikollinearität) | 6.08e-10 | - | Europas größter Softwarehersteller; Indikator für die Investitionen von Unternehmen in Geschäftssoftware und die Digitalisierung der europäischen Wirtschaft. |
| **HYG_3M** | iShares iBoxx $ High Yield Corporate Bond ETF | 🟡 Verworfen (Multikollinearität) | 1.23e-09 | - | Investiert in hochverzinsliche Unternehmensanleihen; ein Barometer für die Risikobereitschaft im Kreditmarkt und die Gesundheit des Unternehmenssektors. |
| **ZW=F_1M** | Weizen-Futures | 🟡 Verworfen (Multikollinearität) | 1.44e-09 | - | Misst den Preis für Weizen; ein Indikator für Agrarpreise, globale Nahrungsmittelsicherheit und geopolitische Einflüsse auf die Versorgungsketten. |
| **NVDA_3M** | NVIDIA Corporation | 🟡 Verworfen (Multikollinearität) | 5.52e-09 | - | Führender Hersteller von Grafikprozessoren; ein entscheidender Indikator für die Halbleiterindustrie, KI-Entwicklung und den Gaming-Markt. |
| **BAS.DE_3M** | BASF SE | 🟡 Verworfen (Multikollinearität) | 1.67e-08 | - | Weltgrößter Chemiekonzern; ein wichtiger Frühindikator für die globale Industrieproduktion und Rohstoffnachfrage, insbesondere in Europa. |
| **XLE_1M** | Energy Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 1.97e-08 | - | Repräsentiert den Energiesektor des S&P 500; ein Indikator für die Rentabilität von Öl- und Gasunternehmen und die Energiepreisentwicklung. |
| **XLP_6M** | Consumer Staples Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 3.07e-08 | - | Repräsentiert den Basiskonsumgütersektor des S&P 500; ein Indikator für die Widerstandsfähigkeit der Konsumentenausgaben in wirtschaftlich unsicheren Zeiten. |
| **AZN.L_3M** | AstraZeneca PLC | 🟡 Verworfen (Multikollinearität) | 3.23e-08 | - | Führendes Pharma- und Biotechnologieunternehmen; repräsentiert die Stabilität und Innovationskraft des globalen Gesundheitssektors. |
| **AAPL_1M** | Apple Inc. | 🟡 Verworfen (Multikollinearität) | 3.29e-08 | - | Weltgrößtes Technologieunternehmen; ein Barometer für den globalen Konsumgüter- und Technologiesektor sowie für die Innovationskraft der US-Wirtschaft. |
| **^TNX_3M** | US 10-Year Treasury Yield | 🟡 Verworfen (Multikollinearität) | 1.16e-07 | - | Misst die Rendite 10-jähriger US-Staatsanleihen; ein zentraler Indikator für langfristige Zins- und Inflationserwartungen sowie Kreditkosten. |
| **RIO.L_3M** | Rio Tinto PLC | 🟡 Verworfen (Multikollinearität) | 1.18e-07 | - | Einer der größten Bergbaukonzerne der Welt; ein Barometer für die globale Nachfrage nach Rohstoffen und die Industrieproduktion. |
| **XLU_1M** | Utilities Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 2.69e-07 | - | Repräsentiert den Versorgersektor des S&P 500; gilt als defensiver Sektor und Indikator für das Anlegerbedürfnis nach Stabilität und Dividenden. |
| **XLP_3M** | Consumer Staples Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 2.73e-07 | - | Repräsentiert den Basiskonsumgütersektor des S&P 500; ein Indikator für die Widerstandsfähigkeit der Konsumentenausgaben in wirtschaftlich unsicheren Zeiten. |
| **MSFT_3M** | Microsoft Corporation | 🟡 Verworfen (Multikollinearität) | 4.47e-06 | - | Eines der weltweit größten Technologieunternehmen; ein Schlüsselindikator für den Software- und Cloud-Markt und die digitale Transformation der Wirtschaft. |
| **LE=F_1M** | Live Cattle Futures | 🟡 Verworfen (Multikollinearität) | 6.70e-06 | - | Misst den Preis für Lebendvieh; Indikator für Agrarpreise, Inflationsdruck bei Lebensmitteln und das Angebot in der Fleischindustrie. |
| **XLV_3M** | Health Care Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 1.36e-05 | - | Repräsentiert den Gesundheitssektor des S&P 500; ein Indikator für defensive Stabilität und Innovationskraft in der Medikamenten- und Medizintechnikbranche. |
| **ZC=F_1M** | Mais-Futures | 🟡 Verworfen (Multikollinearität) | 1.81e-05 | - | Misst den Preis für Mais; ein Indikator für Agrarpreise, Inflationsdruck bei Lebensmitteln und globale Ernteerwartungen. |
| **HG=F_1M** | Kupfer-Futures | 🟡 Verworfen (Multikollinearität) | 2.06e-05 | - | Misst den Preis für Kupfer; wird als 'Dr. Copper' bezeichnet, da er oft als Frühindikator für die globale Industrieproduktion und das Wirtschaftswachstum dient. |
| **SIE.DE_3M** | Siemens AG | 🟡 Verworfen (Multikollinearität) | 3.08e-05 | - | Globaler Technologiekonzern mit Fokus auf Industrie, Infrastruktur und Mobilität; ein Indikator für die globale Investitionsgüterindustrie und Automatisierungstrends. |
| **XLK_6M** | Technology Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 4.64e-05 | - | Repräsentiert den Technologiesektor des S&P 500; ein wichtiger Indikator für Innovation, Wachstum und die allgemeine Marktstimmung im Tech-Bereich. |
| **VNQ_3M** | Vanguard Real Estate ETF | 🟡 Verworfen (Multikollinearität) | 5.43e-05 | - | Investiert in US-Immobilien-REITs; ein Stimmungsbarometer für den US-Immobilienmarkt und die Entwicklung der Immobilienpreise und Mieten. |
| **LE=F_6M** | Live Cattle Futures | 🟡 Verworfen (Multikollinearität) | 6.84e-05 | - | Misst den Preis für Lebendvieh; Indikator für Agrarpreise, Inflationsdruck bei Lebensmitteln und das Angebot in der Fleischindustrie. |
| **TLT_3M** | iShares 20+ Year Treasury Bond ETF | 🟡 Verworfen (Multikollinearität) | 6.94e-05 | - | Investiert in langfristige US-Staatsanleihen; ein Indikator für langfristige Zinsbewegungen, Inflationserwartungen und Anlegerflucht in Sicherheit. |
| **XLV_6M** | Health Care Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 7.48e-05 | - | Repräsentiert den Gesundheitssektor des S&P 500; ein Indikator für defensive Stabilität und Innovationskraft in der Medikamenten- und Medizintechnikbranche. |
| **XBI_1M** | SPDR S&P Biotech ETF | 🟡 Verworfen (Multikollinearität) | 1.02e-04 | - | Fokussiert auf den Biotechnologiesektor; ein Indikator für Risikobereitschaft und Innovationskraft in der Pharma- und Biotech-Industrie. |
| **XLF_6M** | Financial Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 1.07e-04 | - | Repräsentiert den Finanzsektor des S&P 500; ein Schlüsselindikator für die Gesundheit des Bankensystems und die Auswirkungen von Zinsänderungen. |
| **EEM_1M** | iShares MSCI Emerging Markets ETF | 🟡 Verworfen (Multikollinearität) | 1.59e-04 | - | Bündelt Aktien aus Schwellenländern; ein Indikator für das Wirtschaftswachstum und die Anlegerstimmung in diesen dynamischen Regionen. |
| **GC=F_6M** | Gold-Futures | 🟡 Verworfen (Multikollinearität) | 2.40e-04 | - | Misst den Preis für Gold; gilt als sicherer Hafen in Krisenzeiten und als Indikator für Inflationserwartungen und die Stärke des US-Dollars. |
| **XLP_1M** | Consumer Staples Select Sector SPDR Fund | 🟡 Verworfen (Multikollinearität) | 3.16e-04 | - | Repräsentiert den Basiskonsumgütersektor des S&P 500; ein Indikator für die Widerstandsfähigkeit der Konsumentenausgaben in wirtschaftlich unsicheren Zeiten. |
| **GC=F_1M** | Gold-Futures | 🟡 Verworfen (Multikollinearität) | 6.49e-04 | - | Misst den Preis für Gold; gilt als sicherer Hafen in Krisenzeiten und als Indikator für Inflationserwartungen und die Stärke des US-Dollars. |
| **MSFT_6M** | Microsoft Corporation | 🟡 Verworfen (Multikollinearität) | 9.27e-04 | - | Eines der weltweit größten Technologieunternehmen; ein Schlüsselindikator für den Software- und Cloud-Markt und die digitale Transformation der Wirtschaft. |
| **BAS.DE_1M** | BASF SE | 🟡 Verworfen (Multikollinearität) | 0.0013 | - | Weltgrößter Chemiekonzern; ein wichtiger Frühindikator für die globale Industrieproduktion und Rohstoffnachfrage, insbesondere in Europa. |
| **^IRX_1M** | US 13 Week Treasury Bill Yield | 🔴 Verworfen (Keine Signifikanz) | 0.0016 | - | Misst die Rendite kurzfristiger US-Staatsanleihen; ein wichtiger Indikator für die kurzfristige Liquidität und die Erwartungen der Federal Reserve. |
| **BRK-B_1M** | Berkshire Hathaway Inc. Class B | 🔴 Verworfen (Keine Signifikanz) | 0.0019 | - | Konglomerat unter Führung von Warren Buffett; ein Indikator für die Bewertung des breiten US-Wirtschaftsmarktes und die Value-Investment-Strategie. |
| **7203.T_6M** | Toyota Motor Corporation | 🔴 Verworfen (Keine Signifikanz) | 0.0025 | - | Einer der größten Automobilhersteller weltweit; dient als wichtiger Indikator für die globale Konjunktur und den Zustand der japanischen Exportwirtschaft. |
| **^VIX_3M** | CBOE Volatility Index (VIX) | 🔴 Verworfen (Keine Signifikanz) | 0.0027 | - | Misst die implizite Volatilität von S&P 500 Optionen; wird als 'Angstbarometer' des Marktes für die erwartete kurzfristige Volatilität genutzt. |
| **XLY_1M** | Consumer Discretionary Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.0039 | - | Repräsentiert den zyklischen Konsumgütersektor des S&P 500; ein entscheidender Indikator für das Vertrauen und die Ausgabenbereitschaft der Verbraucher. |
| **8035.T_1M** | Tokyo Electron Limited | 🔴 Verworfen (Keine Signifikanz) | 0.0040 | - | Führender Hersteller von Halbleiterproduktionsanlagen; spiegelt die Gesundheit der globalen Tech-Branche und Investitionen in die Digitalisierung wider. |
| **SPY_6M** | SPDR S&P 500 ETF Trust | 🔴 Verworfen (Keine Signifikanz) | 0.0047 | - | Bildet den S&P 500 Index ab; das meistgehandelte Produkt für die Performance der 500 größten US-Unternehmen und ein Barometer für den breiten US-Aktienmarkt. |
| **XLK_3M** | Technology Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.0055 | - | Repräsentiert den Technologiesektor des S&P 500; ein wichtiger Indikator für Innovation, Wachstum und die allgemeine Marktstimmung im Tech-Bereich. |
| **XLV_1M** | Health Care Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.0056 | - | Repräsentiert den Gesundheitssektor des S&P 500; ein Indikator für defensive Stabilität und Innovationskraft in der Medikamenten- und Medizintechnikbranche. |
| **^N225_3M** | Nikkei 225 Stock Average | 🔴 Verworfen (Keine Signifikanz) | 0.0056 | - | Japans wichtigster Aktienindex; ein Barometer für die Performance des japanischen Aktienmarktes und die globale asiatische Wirtschaftsstimmung. |
| **SHEL.L_1M** | Shell PLC | 🔴 Verworfen (Keine Signifikanz) | 0.0062 | - | Einer der größten Energiekonzerne weltweit; spiegelt die Entwicklung der globalen Öl- und Gaspreise sowie die Energieversorgung wider. |
| **HYG_1M** | iShares iBoxx $ High Yield Corporate Bond ETF | 🔴 Verworfen (Keine Signifikanz) | 0.0063 | - | Investiert in hochverzinsliche Unternehmensanleihen; ein Barometer für die Risikobereitschaft im Kreditmarkt und die Gesundheit des Unternehmenssektors. |
| **LE=F_3M** | Live Cattle Futures | 🔴 Verworfen (Keine Signifikanz) | 0.0281 | - | Misst den Preis für Lebendvieh; Indikator für Agrarpreise, Inflationsdruck bei Lebensmitteln und das Angebot in der Fleischindustrie. |
| **ZC=F_3M** | Mais-Futures | 🔴 Verworfen (Keine Signifikanz) | 0.0287 | - | Misst den Preis für Mais; ein Indikator für Agrarpreise, Inflationsdruck bei Lebensmitteln und globale Ernteerwartungen. |
| **MSFT_1M** | Microsoft Corporation | 🔴 Verworfen (Keine Signifikanz) | 0.0303 | - | Eines der weltweit größten Technologieunternehmen; ein Schlüsselindikator für den Software- und Cloud-Markt und die digitale Transformation der Wirtschaft. |
| **CL=F_3M** | WTI Rohöl-Futures | 🔴 Verworfen (Keine Signifikanz) | 0.0322 | - | Misst den Preis für Rohöl; ein entscheidender Indikator für globale Wirtschaftswachstumserwartungen, Inflationsdruck und geopolitische Risiken. |
| **^VIX_1M** | CBOE Volatility Index (VIX) | 🔴 Verworfen (Keine Signifikanz) | 0.0466 | - | Misst die implizite Volatilität von S&P 500 Optionen; wird als 'Angstbarometer' des Marktes für die erwartete kurzfristige Volatilität genutzt. |
| **XLF_3M** | Financial Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.0536 | - | Repräsentiert den Finanzsektor des S&P 500; ein Schlüsselindikator für die Gesundheit des Bankensystems und die Auswirkungen von Zinsänderungen. |
| **^GDAXI_1M** | DAX Performance Index | 🔴 Verworfen (Keine Signifikanz) | 0.0747 | - | Führt die 40 größten und umsatzstärksten deutschen Unternehmen; ein Schlüsselindikator für die Gesundheit der deutschen und europäischen Wirtschaft. |
| **9984.T_1M** | SoftBank Group Corp. | 🔴 Verworfen (Keine Signifikanz) | 0.0826 | - | Japanisches Technologie- und Investment-Konglomerat; Indikator für Risikobereitschaft und Bewertungen im globalen Tech-Start-up-Sektor. |
| **NVDA_1M** | NVIDIA Corporation | 🔴 Verworfen (Keine Signifikanz) | 0.1050 | - | Führender Hersteller von Grafikprozessoren; ein entscheidender Indikator für die Halbleiterindustrie, KI-Entwicklung und den Gaming-Markt. |
| **BRK-B_6M** | Berkshire Hathaway Inc. Class B | 🔴 Verworfen (Keine Signifikanz) | 0.1289 | - | Konglomerat unter Führung von Warren Buffett; ein Indikator für die Bewertung des breiten US-Wirtschaftsmarktes und die Value-Investment-Strategie. |
| **TLT_6M** | iShares 20+ Year Treasury Bond ETF | 🔴 Verworfen (Keine Signifikanz) | 0.1370 | - | Investiert in langfristige US-Staatsanleihen; ein Indikator für langfristige Zinsbewegungen, Inflationserwartungen und Anlegerflucht in Sicherheit. |
| **^TNX_6M** | US 10-Year Treasury Yield | 🔴 Verworfen (Keine Signifikanz) | 0.1783 | - | Misst die Rendite 10-jähriger US-Staatsanleihen; ein zentraler Indikator für langfristige Zins- und Inflationserwartungen sowie Kreditkosten. |
| **JPM_1M** | JPMorgan Chase & Co. | 🔴 Verworfen (Keine Signifikanz) | 0.1818 | - | Größte US-Bank; ein führender Indikator für die Gesundheit des Finanzsektors und die allgemeine Wirtschaftslage in den USA. |
| **SPY_1M** | SPDR S&P 500 ETF Trust | 🔴 Verworfen (Keine Signifikanz) | 0.2058 | - | Bildet den S&P 500 Index ab; das meistgehandelte Produkt für die Performance der 500 größten US-Unternehmen und ein Barometer für den breiten US-Aktienmarkt. |
| **SPY_3M** | SPDR S&P 500 ETF Trust | 🔴 Verworfen (Keine Signifikanz) | 0.2119 | - | Bildet den S&P 500 Index ab; das meistgehandelte Produkt für die Performance der 500 größten US-Unternehmen und ein Barometer für den breiten US-Aktienmarkt. |
| **7203.T_3M** | Toyota Motor Corporation | 🔴 Verworfen (Keine Signifikanz) | 0.2168 | - | Einer der größten Automobilhersteller weltweit; dient als wichtiger Indikator für die globale Konjunktur und den Zustand der japanischen Exportwirtschaft. |
| **SAP.DE_1M** | SAP SE | 🔴 Verworfen (Keine Signifikanz) | 0.2289 | - | Europas größter Softwarehersteller; Indikator für die Investitionen von Unternehmen in Geschäftssoftware und die Digitalisierung der europäischen Wirtschaft. |
| **CL=F_1M** | WTI Rohöl-Futures | 🔴 Verworfen (Keine Signifikanz) | 0.2525 | - | Misst den Preis für Rohöl; ein entscheidender Indikator für globale Wirtschaftswachstumserwartungen, Inflationsdruck und geopolitische Risiken. |
| **^VIX_6M** | CBOE Volatility Index (VIX) | 🔴 Verworfen (Keine Signifikanz) | 0.3234 | - | Misst die implizite Volatilität von S&P 500 Optionen; wird als 'Angstbarometer' des Marktes für die erwartete kurzfristige Volatilität genutzt. |
| **7203.T_1M** | Toyota Motor Corporation | 🔴 Verworfen (Keine Signifikanz) | 0.3668 | - | Einer der größten Automobilhersteller weltweit; dient als wichtiger Indikator für die globale Konjunktur und den Zustand der japanischen Exportwirtschaft. |
| **AZN.L_1M** | AstraZeneca PLC | 🔴 Verworfen (Keine Signifikanz) | 0.3854 | - | Führendes Pharma- und Biotechnologieunternehmen; repräsentiert die Stabilität und Innovationskraft des globalen Gesundheitssektors. |
| **BRK-B_3M** | Berkshire Hathaway Inc. Class B | 🔴 Verworfen (Keine Signifikanz) | 0.4377 | - | Konglomerat unter Führung von Warren Buffett; ein Indikator für die Bewertung des breiten US-Wirtschaftsmarktes und die Value-Investment-Strategie. |
| **XLY_6M** | Consumer Discretionary Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.4652 | - | Repräsentiert den zyklischen Konsumgütersektor des S&P 500; ein entscheidender Indikator für das Vertrauen und die Ausgabenbereitschaft der Verbraucher. |
| **ZC=F_6M** | Mais-Futures | 🔴 Verworfen (Keine Signifikanz) | 0.5305 | - | Misst den Preis für Mais; ein Indikator für Agrarpreise, Inflationsdruck bei Lebensmitteln und globale Ernteerwartungen. |
| **XLK_1M** | Technology Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.5531 | - | Repräsentiert den Technologiesektor des S&P 500; ein wichtiger Indikator für Innovation, Wachstum und die allgemeine Marktstimmung im Tech-Bereich. |
| **XLF_1M** | Financial Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.6190 | - | Repräsentiert den Finanzsektor des S&P 500; ein Schlüsselindikator für die Gesundheit des Bankensystems und die Auswirkungen von Zinsänderungen. |
| **RIO.L_1M** | Rio Tinto PLC | 🔴 Verworfen (Keine Signifikanz) | 0.7027 | - | Einer der größten Bergbaukonzerne der Welt; ein Barometer für die globale Nachfrage nach Rohstoffen und die Industrieproduktion. |
| **^N225_1M** | Nikkei 225 Stock Average | 🔴 Verworfen (Keine Signifikanz) | 0.7042 | - | Japans wichtigster Aktienindex; ein Barometer für die Performance des japanischen Aktienmarktes und die globale asiatische Wirtschaftsstimmung. |
| **VNQ_1M** | Vanguard Real Estate ETF | 🔴 Verworfen (Keine Signifikanz) | 0.7061 | - | Investiert in US-Immobilien-REITs; ein Stimmungsbarometer für den US-Immobilienmarkt und die Entwicklung der Immobilienpreise und Mieten. |
| **SIE.DE_1M** | Siemens AG | 🔴 Verworfen (Keine Signifikanz) | 0.7497 | - | Globaler Technologiekonzern mit Fokus auf Industrie, Infrastruktur und Mobilität; ein Indikator für die globale Investitionsgüterindustrie und Automatisierungstrends. |
| **XLY_3M** | Consumer Discretionary Select Sector SPDR Fund | 🔴 Verworfen (Keine Signifikanz) | 0.7838 | - | Repräsentiert den zyklischen Konsumgütersektor des S&P 500; ein entscheidender Indikator für das Vertrauen und die Ausgabenbereitschaft der Verbraucher. |

## Mathematische Modellparameter

- **Intercepts:** `[-0.443980754258516, 0.203050337496946, 0.24093041676157814]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.38545441  0.10060164  0.07113646 -0.22669208  0.82034036  0.46760306
  -0.69674253  0.2116925 ]
 [-0.16233006 -0.09658396 -0.12909444  0.19788537 -0.06686218 -0.11712139
   0.10311529  0.20886208]
 [-0.22312435 -0.00401768  0.05795798  0.02880671 -0.75347819 -0.35048167
   0.59362723 -0.42055458]]
  ```
