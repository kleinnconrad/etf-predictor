# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-28 10:09:00
- **Target ETF:** DBXJ.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-27** prognostiziert das Modell:

> **Klasse:** Down
>
> **Wahrscheinlichkeiten:** Down: 52.75% | Flat: 13.06% | Up: 34.19%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| UNRATE_126D_ret | 1.101996 |
| UNRATE_63D_ret | 0.743217 |
| PAYEMS_63D_ret | 0.650534 |
| ratio_intl_vs_us_bonds_126D_ret | 0.530426 |
| DX-Y.NYB_63D_ret | 0.334787 |
| CL=F_63D_ret | 0.329935 |
| LRHUTTTTGBM156S_21D_ret | 0.176368 |
| ratio_tech_dominance_126D_ret | 0.171969 |
| RIO.L_63D_ret | 0.135357 |
| LRHUTTTTJPM156S_21D_ret | 0.119696 |
| ^IRX_63D_ret | 0.096831 |
| PRINTO01EZQ661S_63D_ret | 0.081015 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`9984.T_63D_ret, 9984.T_126D_ret, AZN.L_126D_ret, BNDX_21D_ret, BNDX_63D_ret, BTC-USD_63D_ret, BTC-USD_126D_ret, BWX_21D_ret, BWX_63D_ret, BWX_126D_ret, CL=F_126D_ret, DBXJ.DE_63D_ret, DBXJ.DE_126D_ret, DX-Y.NYB_21D_ret, DX-Y.NYB_126D_ret, EEM_63D_ret, EEM_126D_ret, GC=F_21D_ret, GC=F_63D_ret, GC=F_126D_ret, HG=F_63D_ret, HG=F_126D_ret, HYG_63D_ret, HYG_126D_ret, IGOV_21D_ret, IGOV_63D_ret, IGOV_126D_ret, LE=F_21D_ret, LE=F_63D_ret, LQD_21D_ret, LQD_63D_ret, LQD_126D_ret, RIO.L_126D_ret, SHEL.L_63D_ret, SHEL.L_126D_ret, TLT_21D_ret, TLT_63D_ret, VNQ_126D_ret, XBI_126D_ret, XLE_21D_ret, XLE_63D_ret, XLE_126D_ret, XLU_126D_ret, ZW=F_63D_ret, ZW=F_126D_ret, ^GDAXI_126D_ret, ^IRX_126D_ret, ^TNX_21D_ret, ^TNX_63D_ret, ^TNX_126D_ret, CPIAUCSL_63D_ret, CPIAUCSL_126D_ret, PAYEMS_126D_ret, T10Y2Y_126D_ret, CP00MI15EA20M086NEST_126D_ret, LRHUTTTTEZM156S_21D_ret, LRHUTTTTEZM156S_63D_ret, LRHUTTTTEZM156S_126D_ret, PRINTO01EZQ661S_126D_ret, JPNCPIALLMINMEI_126D_ret, LRHUTTTTJPM156S_126D_ret, LRHUTTTTGBM156S_63D_ret, LRHUTTTTGBM156S_126D_ret, ratio_credit_spread_21D_ret, ratio_credit_spread_63D_ret, ratio_credit_spread_126D_ret, ratio_risk_on_off_21D_ret, ratio_intl_vs_us_bonds_63D_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>121</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21D_ret, 7203.T_63D_ret, 7203.T_126D_ret, 8035.T_21D_ret, 8035.T_63D_ret, 8035.T_126D_ret, 9984.T_21D_ret, AAPL_21D_ret, AAPL_63D_ret, AAPL_126D_ret, AZN.L_21D_ret, AZN.L_63D_ret, BAS.DE_21D_ret, BAS.DE_63D_ret, BAS.DE_126D_ret, BNDX_126D_ret, BRK-B_21D_ret, BRK-B_63D_ret, BRK-B_126D_ret, BTC-USD_21D_ret, CL=F_21D_ret, DBXJ.DE_21D_ret, EEM_21D_ret, HG=F_21D_ret, HYG_21D_ret, JPM_21D_ret, JPM_63D_ret, JPM_126D_ret, LE=F_126D_ret, MSFT_21D_ret, MSFT_63D_ret, MSFT_126D_ret, NVDA_21D_ret, NVDA_63D_ret, NVDA_126D_ret, RIO.L_21D_ret, SAP.DE_21D_ret, SAP.DE_63D_ret, SAP.DE_126D_ret, SHEL.L_21D_ret, SIE.DE_21D_ret, SIE.DE_63D_ret, SIE.DE_126D_ret, SPY_21D_ret, SPY_63D_ret, SPY_126D_ret, TLT_126D_ret, VNQ_21D_ret, VNQ_63D_ret, XBI_21D_ret, XBI_63D_ret, XLF_21D_ret, XLF_63D_ret, XLF_126D_ret, XLK_21D_ret, XLK_63D_ret, XLK_126D_ret, XLP_21D_ret, XLP_63D_ret, XLP_126D_ret, XLU_21D_ret, XLU_63D_ret, XLV_21D_ret, XLV_63D_ret, XLV_126D_ret, XLY_21D_ret, XLY_63D_ret, XLY_126D_ret, ZC=F_21D_ret, ZC=F_63D_ret, ZC=F_126D_ret, ZW=F_21D_ret, ^GDAXI_21D_ret, ^GDAXI_63D_ret, ^IRX_21D_ret, ^N225_21D_ret, ^N225_63D_ret, ^N225_126D_ret, ^VIX_21D_ret, ^VIX_63D_ret, ^VIX_126D_ret, CPIAUCSL_21D_ret, PAYEMS_21D_ret, UNRATE_21D_ret, T10Y2Y_21D_ret, T10Y2Y_63D_ret, WALCL_21D_ret, WALCL_63D_ret, WALCL_126D_ret, CP00MI15EA20M086NEST_21D_ret, CP00MI15EA20M086NEST_63D_ret, ECBASSETS_21D_ret, ECBASSETS_63D_ret, ECBASSETS_126D_ret, PRINTO01EZQ661S_21D_ret, JPNCPIALLMINMEI_21D_ret, JPNCPIALLMINMEI_63D_ret, LRHUTTTTJPM156S_63D_ret, JPNASSETS_21D_ret, JPNASSETS_63D_ret, JPNASSETS_126D_ret, JPNPROINDMISMEI_21D_ret, JPNPROINDMISMEI_63D_ret, JPNPROINDMISMEI_126D_ret, GBRCPIALLMINMEI_21D_ret, GBRCPIALLMINMEI_63D_ret, GBRCPIALLMINMEI_126D_ret, GBRPROINDMISMEI_21D_ret, GBRPROINDMISMEI_63D_ret, GBRPROINDMISMEI_126D_ret, ratio_copper_gold_21D_ret, ratio_copper_gold_63D_ret, ratio_copper_gold_126D_ret, ratio_consumer_risk_21D_ret, ratio_consumer_risk_63D_ret, ratio_consumer_risk_126D_ret, ratio_risk_on_off_63D_ret, ratio_risk_on_off_126D_ret, ratio_tech_dominance_21D_ret, ratio_tech_dominance_63D_ret, ratio_intl_vs_us_bonds_21D_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makrooekonomisches Setup:**

*   **US-Arbeitsmarkt als Primärindikator:** Die Dominanz von UNRATE und PAYEMS (US-Arbeitsmarktdaten) unterstreicht die fundamentale Abhängigkeit japanischer Exporte und des globalen Wachstums vom Zustand der US-Wirtschaft. Momentum in diesen Indikatoren signalisiert Akzeleration/Dezeleration der globalen Nachfrage.
*   **Globale Kapitalströme & FX-Arbitrage:** Das "ratio_intl_vs_us_bonds" und der DX-Y.NYB-Momentum spiegeln die relative Attraktivität von Nicht-US-Anleihen und die USD-Stärke wider. Positive Dynamik hier indiziert Kapitalrotation aus US-Anleihen, potenziell hin zu risikoreicheren Anlagen in Exportnationen wie Japan, oder eine USD-Schwäche, die japanische Exporte begünstigt.
*   **Rohstoff- & Industriedynamik:** CL=F und RIO.L (Rohöl und Bergbau) signalisieren die Stärke der globalen Industrieproduktion und Rohstoffnachfrage. Steigendes Momentum hier korreliert mit einer globalen Expansion, die für Japans exportorientierte Wirtschaft essentiell ist.
*   **Geringe Zinsrelevanz auf 6M-Sicht:** Die geringe Gewichtung von ^IRX (kurzfristige US-Zinsen) und das Fehlen längerfristiger Zinskurvenindikatoren implizieren, dass direkte Zinsbewegungen für das 6-Monats-Outlook für DBXJ.DE nachrangig gegenüber globaler Realwirtschaft und Kapitalflüssen sind.
*   **Globale Liquidität als Nebenstrom:** PRINTO01EZQ661S (EZB M1 Geldmenge) deutet an, dass globale Liquiditätsbedingungen eine Rolle spielen, jedoch mit geringer Prädiktionskraft im Vergleich zu harten Konjunkturdaten.

**2. Sektor- & Marktdynamik:**

*   **Zyklische Dominanz:** Die Konzentration auf Arbeitsmarktdaten (USA, UK, JP) und Rohstoffe weist auf eine hohe Sensitivität gegenüber dem globalen Konjunkturzyklus hin. Japanische Unternehmen sind stark in exportorientierten und kapitalintensiven Sektoren (Automobil, Maschinenbau, Elektronik) positioniert, die von robustem globalem Wachstum profitieren.
*   **Technologie als Wachstumsbarometer:** "ratio_tech_dominance" als Indikator spiegelt die allgemeine Risikobereitschaft und das Wachstumsumfeld wider. Eine zunehmende Tech-Dominanz deutet auf ein "Risk-On"-Umfeld hin, das auch japanischen Technologie- und Automatisierungsunternehmen zugutekommt.
*   **Interkonnektivität von Arbeitsmärkten:** Die sehr kurzen Momentum-Fenster (21D) für UK- und Japan-Arbeitslosigkeit deuten auf eine hohe Relevanz von Echtzeit-Arbeitsmarktstimmungen hin, die als Frühindikatoren für Konsum und Investitionen in wichtigen Handelspartnerländern Japans dienen.

**3. Quant-Konklusion:**

*   **Globales Wachstum als primäres Narrativ:** Das Modell prognostiziert den Marktzustand von DBXJ.DE primär über die Stärke und das Momentum der globalen Wirtschaftsexpansion, angeführt durch den US-Arbeitsmarkt und die industrielle Nachfrage.
*   **Kapitalrotation & USD-Hedge:** DBXJ.DE wird als potenzieller Profiteur von Kapitalströmen außerhalb der USA und/oder einer relativen Schwäche des US-Dollars positioniert.
*   **Zyklische Aufwärtsbewegung erwartet:** Ein positives Signal für DBXJ.DE impliziert ein synchrones globales Wachstumsumfeld, das durch starke Beschäftigung, erhöhte Rohstoffnachfrage und günstige Wechselkursentwicklungen für exportierende Volkswirtschaften gekennzeichnet ist.

## Mathematische Modellparameter

- **Intercepts:** `[-0.351360476682447, -0.5099318353543173, 0.861292312036777]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.40891869  0.45769074 -0.09199882  0.08236881 -0.9100471  -0.7928248
  -1.65299462  0.00209831 -0.08411527  0.13032032 -0.02881794 -0.79563932]
 [ 0.0859834   0.0444891  -0.1110373   0.06287806 -0.06575458 -0.32200089
   0.67426636  0.11942418 -0.09542873  0.13423135 -0.22913544  0.33663343]
 [-0.4949021  -0.50217984  0.20303611 -0.14524688  0.97580168  1.1148257
   0.97872826 -0.12152249  0.179544   -0.26455167  0.25795338  0.45900589]]
  ```
