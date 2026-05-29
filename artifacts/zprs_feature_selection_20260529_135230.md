# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-29 13:54:08
- **Target ETF:** ZPRS.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-28** prognostiziert das Modell:

> **Klasse:** Up
>
> **Wahrscheinlichkeiten:** Down: 3.34% | Flat: 25.93% | Up: 70.72%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| UNRATE_63D_ret | 0.946788 |
| ratio_intl_vs_us_bonds_126D_ret | 0.545421 |
| SAP.DE_63D_ret | 0.483626 |
| ^IRX_126D_ret | 0.435413 |
| 8035.T_126D_ret | 0.389330 |
| ^IRX_63D_ret | 0.387009 |
| GBRPROINDMISMEI_126D_ret | 0.251571 |
| HYG_126D_ret | 0.142301 |
| PRINTO01EZQ661S_63D_ret | 0.112353 |
| EEM_21D_ret | 0.103500 |
| ratio_intl_vs_us_bonds_63D_ret | 0.034564 |
| ^IRX_21D_ret | 0.028653 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`7203.T_126D_ret, 8035.T_63D_ret, 9984.T_63D_ret, 9984.T_126D_ret, AAPL_63D_ret, AZN.L_126D_ret, BAS.DE_126D_ret, BNDX_63D_ret, BNDX_126D_ret, BTC-USD_63D_ret, BTC-USD_126D_ret, BWX_21D_ret, BWX_63D_ret, BWX_126D_ret, DX-Y.NYB_21D_ret, DX-Y.NYB_63D_ret, DX-Y.NYB_126D_ret, EEM_63D_ret, EEM_126D_ret, GC=F_21D_ret, GC=F_63D_ret, GC=F_126D_ret, HG=F_63D_ret, HG=F_126D_ret, IGOV_21D_ret, IGOV_63D_ret, IGOV_126D_ret, LQD_63D_ret, LQD_126D_ret, MSFT_126D_ret, RIO.L_63D_ret, RIO.L_126D_ret, SAP.DE_21D_ret, SHEL.L_126D_ret, SPY_126D_ret, TLT_21D_ret, XBI_126D_ret, XLE_126D_ret, XLK_126D_ret, XLY_126D_ret, ZW=F_126D_ret, ^N225_126D_ret, ^VIX_63D_ret, CPIAUCSL_63D_ret, CPIAUCSL_126D_ret, PAYEMS_63D_ret, PAYEMS_126D_ret, UNRATE_126D_ret, T10Y2Y_126D_ret, WALCL_126D_ret, CP00MI15EA20M086NEST_126D_ret, LRHUTTTTEZM156S_63D_ret, LRHUTTTTEZM156S_126D_ret, ECBASSETS_63D_ret, ECBASSETS_126D_ret, PRINTO01EZQ661S_126D_ret, LRHUTTTTJPM156S_126D_ret, JPNASSETS_63D_ret, JPNASSETS_126D_ret, GBRCPIALLMINMEI_21D_ret, GBRCPIALLMINMEI_63D_ret, GBRCPIALLMINMEI_126D_ret, LRHUTTTTGBM156S_63D_ret, LRHUTTTTGBM156S_126D_ret, ratio_copper_gold_126D_ret, ratio_credit_spread_21D_ret, ratio_consumer_risk_126D_ret, ratio_tech_dominance_126D_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>121</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21D_ret, 7203.T_63D_ret, 8035.T_21D_ret, 9984.T_21D_ret, AAPL_21D_ret, AAPL_126D_ret, AZN.L_21D_ret, AZN.L_63D_ret, BAS.DE_21D_ret, BAS.DE_63D_ret, BNDX_21D_ret, BRK-B_21D_ret, BRK-B_63D_ret, BRK-B_126D_ret, BTC-USD_21D_ret, CL=F_21D_ret, CL=F_63D_ret, CL=F_126D_ret, HG=F_21D_ret, HYG_21D_ret, HYG_63D_ret, JPM_21D_ret, JPM_63D_ret, JPM_126D_ret, LE=F_21D_ret, LE=F_63D_ret, LE=F_126D_ret, LQD_21D_ret, MSFT_21D_ret, MSFT_63D_ret, NVDA_21D_ret, NVDA_63D_ret, NVDA_126D_ret, RIO.L_21D_ret, SAP.DE_126D_ret, SHEL.L_21D_ret, SHEL.L_63D_ret, SIE.DE_21D_ret, SIE.DE_63D_ret, SIE.DE_126D_ret, SPY_21D_ret, SPY_63D_ret, TLT_63D_ret, TLT_126D_ret, VNQ_21D_ret, VNQ_63D_ret, VNQ_126D_ret, XBI_21D_ret, XBI_63D_ret, XLE_21D_ret, XLE_63D_ret, XLF_21D_ret, XLF_63D_ret, XLF_126D_ret, XLK_21D_ret, XLK_63D_ret, XLP_21D_ret, XLP_63D_ret, XLP_126D_ret, XLU_21D_ret, XLU_63D_ret, XLU_126D_ret, XLV_21D_ret, XLV_63D_ret, XLV_126D_ret, XLY_21D_ret, XLY_63D_ret, ZC=F_21D_ret, ZC=F_63D_ret, ZC=F_126D_ret, ZPRS.DE_21D_ret, ZPRS.DE_63D_ret, ZPRS.DE_126D_ret, ZW=F_21D_ret, ZW=F_63D_ret, ^GDAXI_21D_ret, ^GDAXI_63D_ret, ^GDAXI_126D_ret, ^N225_21D_ret, ^N225_63D_ret, ^TNX_21D_ret, ^TNX_63D_ret, ^TNX_126D_ret, ^VIX_21D_ret, ^VIX_126D_ret, CPIAUCSL_21D_ret, PAYEMS_21D_ret, UNRATE_21D_ret, T10Y2Y_21D_ret, T10Y2Y_63D_ret, WALCL_21D_ret, WALCL_63D_ret, CP00MI15EA20M086NEST_21D_ret, CP00MI15EA20M086NEST_63D_ret, LRHUTTTTEZM156S_21D_ret, ECBASSETS_21D_ret, PRINTO01EZQ661S_21D_ret, JPNCPIALLMINMEI_21D_ret, JPNCPIALLMINMEI_63D_ret, JPNCPIALLMINMEI_126D_ret, LRHUTTTTJPM156S_21D_ret, LRHUTTTTJPM156S_63D_ret, JPNASSETS_21D_ret, JPNPROINDMISMEI_21D_ret, JPNPROINDMISMEI_63D_ret, JPNPROINDMISMEI_126D_ret, LRHUTTTTGBM156S_21D_ret, GBRPROINDMISMEI_21D_ret, GBRPROINDMISMEI_63D_ret, ratio_copper_gold_21D_ret, ratio_copper_gold_63D_ret, ratio_credit_spread_63D_ret, ratio_credit_spread_126D_ret, ratio_consumer_risk_21D_ret, ratio_consumer_risk_63D_ret, ratio_risk_on_off_21D_ret, ratio_risk_on_off_63D_ret, ratio_risk_on_off_126D_ret, ratio_tech_dominance_21D_ret, ratio_tech_dominance_63D_ret, ratio_intl_vs_us_bonds_21D_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

Als Quantitativer Macro-Analyst präsentiere ich die hochgradig elaborierte Analyse Ihres Modells für ZPRS.DE:

---

**1. Makrooekonomisches Setup:**

*   **Dominanz der US-Geldpolitik und Konjunktur:** Die signifikante Gewichtung von UNRATE_63D_ret (US-Arbeitslosigkeit) und den verschiedenen ^IRX-Momentum-Variablen (US-Kurzfristzinsen) etabliert die globale Vorreiterrolle der US-Makroökonomie. Steigende US-Arbeitslosigkeit oder steigende US-Kurzfristzinsen werden als klare Signale für eine globale Wachstumsverlangsamung oder straffere Finanzierungsbedingungen interpretiert, welche die Diskontierungssätze und die Kapitalflüsse für Immobilienanlagen direkt beeinflussen.
*   **Globale Liquidität und Risikobereitschaft als Preisgeber:** HYG_126D_ret (US High Yield Corporate Bonds) und EEM_21D_ret (Emerging Markets Equities) quantifizieren die globale Risikobereitschaft und die Verfügbarkeit von Liquidität. Ein positives Momentum signalisiert "Risk-On"-Sentiment, niedrigere Risikoaufschläge und verstärkte Investitionsbereitschaft, die sich vorteilhaft auf asset-sensitiven Immobilienmärkte auswirken.
*   **Indikation von Kapitalflussverschiebungen:** Das ratio_intl_vs_us_bonds_126D_ret zeigt die Sensitivität gegenüber globalen Kapitalströmen. Eine Outperformance internationaler Bonds gegenüber US-Bonds signalisiert entweder eine relative Stärke oder Attraktivität internationaler Märkte, eine USD-Schwäche oder eine Umschichtung von Kapital aus den USA, was zu verstärkten Investitionen in nicht-US-Assets wie deutsche Immobilien führen kann.
*   **Fokus auf Finanzierungsbedingungen, nicht Rohstoffe/Direkte Währungen:** Die explizite Nicht-Auswahl von direkten Rohstoffpreisindikatoren oder Währungspaaren deutet darauf hin, dass für den deutschen Wohnimmobilienmarkt im 6-Monats-Horizont die globalen Finanzierungsbedingungen, Zinskurvendynamiken und die realwirtschaftliche Entwicklung (Einkommen, Beschäftigung) als primäre Treiber wichtiger sind als direkte Inputkosten (Rohstoffe) oder isolierte Währungseffekte.

---

**2. Sektor- & Marktdynamik:**

*   **Deutsche & Eurozonen-Wirtschaft als Basis:** SAP.DE_63D_ret dient als Proxy für die Verfassung des deutschen und europäischen Unternehmenssektors, insbesondere im Tech-Segment, das eng mit Innovation, Wachstum und der Schaffung hochqualifizierter Arbeitsplätze verbunden ist. PRINTO01EZQ661S_63D_ret (Eurozonen-Industrieproduktion) liefert ein direktes Signal zur aktuellen wirtschaftlichen Aktivität im Heimatmarkt der EZB, welche die Beschäftigungs- und Einkommensaussichten der Haushalte direkt beeinflusst.
*   **Abhängigkeit von Globalen Industrie- und Tech-Zyklen:** 8035.T_126D_ret (Japanischer Halbleiterzulieferer Tokyo Electron) und GBRPROINDMISMEI_126D_ret (UK Industrieproduktion) indizieren die globale Industrieproduktion und den globalen Tech-Investitionszyklus. Ein positives Momentum hier reflektiert eine robuste globale Konjunktur, die über verbesserte Exportaussichten und Unternehmensgewinne indirekt auch die deutsche Binnenwirtschaft und somit den Immobilienmarkt stützt.
*   **Breite Makro-Kopplung statt Sektor-Spezifika:** Die Auswahl globaler und breit aufgestellter Indikatoren (Industrieproduktion, Tech-Blue-Chips) gegenüber spezifischen Immobilien-, Bau- oder Bankensektorindikatoren legt nahe, dass der ZPRS.DE als integraler Bestandteil der Gesamtökonomie gesehen wird und dessen Performance nicht primär durch isolierte sektorspezifische Faktoren, sondern durch übergreifende makroökonomische und finanzmarktbezogene Dynamiken bestimmt wird.

---

**3. Quant-Konklusion:**

*   **Übergreifendes Narrativ: Prozyklische Kopplung an Globale Finanzbedingungen & Reales Wachstum:** Der ZPRS.DE ist ein hochgradig prozyklisches Asset, dessen Performance in den nächsten 6 Monaten maßgeblich von der Entwicklung der globalen Finanzierungsbedingungen (insbesondere US-Zinskurve, Kreditspreads) und der Stärke des realen Wirtschaftswachstums, sowohl global (US-Arbeitsmarkt, globaler Tech/Industrie-Zyklus) als auch in der Eurozone, abhängt.
*   **Zinsstruktur als Leitsignal:** Eine steilere US-Zinskurve (impliziert durch steigende kurzfristige Renditen bei gleichzeitig eventuell fallenden längerfristigen Renditen, oder allgemein steigenden Renditen als Zeichen einer Normalisierung oder Straffung) oder steigende Kreditspreads wären negativ für den ZPRS.DE, während eine lockere Geldpolitik oder sinkende Zinsen positiv wirken.
*   **Marktzustands-Implikation:** Ein "Up"-Marktzustand für ZPRS.DE wird durch ein Umfeld gestützt, in dem die US-Arbeitslosigkeit stabil bleibt oder sinkt, die US-Kurzfristzinsen ein Wachstum unterstützendes Niveau aufweisen (oder fallen), die globale Risikobereitschaft hoch ist und die industrielle Aktivität in Europa und global expandiert. Ein "Down"-Marktzustand ist die Kehrseite dieser Metriken, während ein "Flat"-Zustand durch gemischte oder sich ausgleichende Signale dieser Indikatoren charakterisiert wäre.

## Mathematische Modellparameter

- **Intercepts:** `[-0.17363566780562445, -0.18977274465140764, 0.3634084124570416]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.58399573  0.06923776 -0.15648892  0.5604304  -0.04297907  0.52699896
   0.25596411 -1.42018165 -0.16852883  0.37735655  0.05184551 -0.81813145]
 [ 0.37243765  0.08601172 -0.05696194  0.1650087   0.0152454   0.05351394
   0.39715517  0.14772617  0.11833417 -0.36465828 -0.02164931  0.33444479]
 [ 0.21155808 -0.15524948  0.21345086 -0.7254391   0.02773367 -0.58051291
  -0.65311927  1.27245548  0.05019467 -0.01269826 -0.0301962   0.48368666]]
  ```
