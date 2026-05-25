# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-25 12:15:08
- **Target ETF:** SPY
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2025-11-20** prognostiziert das Modell:

> **Klasse:** Up
>
> **Wahrscheinlichkeiten:** Down: 34.65% | Flat: 8.09% | Up: 57.26%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| T10Y2Y_63M_ret | 0.296560 |
| AAPL_126M_ret | 0.252018 |
| XLE_63M_ret | 0.198326 |
| ratio_credit_spread_21M_ret | 0.194185 |
| ZW=F_63M_ret | 0.181935 |
| ratio_credit_spread_63M_ret | 0.169863 |
| VNQ_126M_ret | 0.148247 |
| ^IRX_21M_ret | 0.128777 |
| LRHUTTTTEZM156S_21M_ret | 0.110017 |
| ^TNX_21M_ret | 0.082427 |
| ^TNX_63M_ret | 0.072913 |
| ratio_risk_on_off_21M_ret | 0.049975 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`8035.T_63M_ret, 8035.T_126M_ret, 9984.T_63M_ret, 9984.T_126M_ret, AAPL_63M_ret, AZN.L_126M_ret, BAS.DE_126M_ret, BNDX_21M_ret, BNDX_63M_ret, BNDX_126M_ret, BTC-USD_21M_ret, BTC-USD_63M_ret, BTC-USD_126M_ret, BWX_21M_ret, BWX_63M_ret, BWX_126M_ret, CL=F_126M_ret, DX-Y.NYB_21M_ret, DX-Y.NYB_63M_ret, DX-Y.NYB_126M_ret, EEM_63M_ret, EEM_126M_ret, GC=F_63M_ret, HG=F_63M_ret, HG=F_126M_ret, HYG_63M_ret, HYG_126M_ret, IGOV_21M_ret, IGOV_63M_ret, IGOV_126M_ret, JPM_126M_ret, LQD_21M_ret, LQD_63M_ret, LQD_126M_ret, RIO.L_126M_ret, SHEL.L_126M_ret, SIE.DE_126M_ret, TLT_21M_ret, XBI_63M_ret, XBI_126M_ret, XLE_126M_ret, XLU_63M_ret, XLU_126M_ret, ZW=F_126M_ret, ^GDAXI_126M_ret, ^IRX_63M_ret, ^IRX_126M_ret, ^N225_126M_ret, CPIAUCSL_21M_ret, CPIAUCSL_63M_ret, CPIAUCSL_126M_ret, PAYEMS_126M_ret, UNRATE_126M_ret, T10Y2Y_126M_ret, CP00MI15EA20M086NEST_21M_ret, CP00MI15EA20M086NEST_63M_ret, CP00MI15EA20M086NEST_126M_ret, LRHUTTTTEZM156S_63M_ret, LRHUTTTTEZM156S_126M_ret, LRHUTTTTJPM156S_126M_ret, GBRCPIALLMINMEI_63M_ret, GBRCPIALLMINMEI_126M_ret, LRHUTTTTGBM156S_63M_ret, LRHUTTTTGBM156S_126M_ret, ratio_copper_gold_63M_ret, ratio_copper_gold_126M_ret, ratio_intl_vs_us_bonds_63M_ret, ratio_intl_vs_us_bonds_126M_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>118</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21M_ret, 7203.T_63M_ret, 7203.T_126M_ret, 8035.T_21M_ret, 9984.T_21M_ret, AAPL_21M_ret, AZN.L_21M_ret, AZN.L_63M_ret, BAS.DE_21M_ret, BAS.DE_63M_ret, BRK-B_21M_ret, BRK-B_63M_ret, BRK-B_126M_ret, CL=F_21M_ret, CL=F_63M_ret, EEM_21M_ret, GC=F_21M_ret, GC=F_126M_ret, HG=F_21M_ret, HYG_21M_ret, JPM_21M_ret, JPM_63M_ret, LE=F_21M_ret, LE=F_63M_ret, LE=F_126M_ret, MSFT_21M_ret, MSFT_63M_ret, MSFT_126M_ret, NVDA_21M_ret, NVDA_63M_ret, NVDA_126M_ret, RIO.L_21M_ret, RIO.L_63M_ret, SAP.DE_21M_ret, SAP.DE_63M_ret, SAP.DE_126M_ret, SHEL.L_21M_ret, SHEL.L_63M_ret, SIE.DE_21M_ret, SIE.DE_63M_ret, SPY_21M_ret, SPY_63M_ret, SPY_126M_ret, TLT_63M_ret, TLT_126M_ret, VNQ_21M_ret, VNQ_63M_ret, XBI_21M_ret, XLE_21M_ret, XLF_21M_ret, XLF_63M_ret, XLF_126M_ret, XLK_21M_ret, XLK_63M_ret, XLK_126M_ret, XLP_21M_ret, XLP_63M_ret, XLP_126M_ret, XLU_21M_ret, XLV_21M_ret, XLV_63M_ret, XLV_126M_ret, XLY_21M_ret, XLY_63M_ret, XLY_126M_ret, ZC=F_21M_ret, ZC=F_63M_ret, ZC=F_126M_ret, ZW=F_21M_ret, ^GDAXI_21M_ret, ^GDAXI_63M_ret, ^N225_21M_ret, ^N225_63M_ret, ^TNX_126M_ret, ^VIX_21M_ret, ^VIX_63M_ret, ^VIX_126M_ret, PAYEMS_21M_ret, PAYEMS_63M_ret, UNRATE_21M_ret, UNRATE_63M_ret, T10Y2Y_21M_ret, WALCL_21M_ret, WALCL_63M_ret, WALCL_126M_ret, ECBASSETS_21M_ret, ECBASSETS_63M_ret, ECBASSETS_126M_ret, PRINTO01EZQ661S_21M_ret, PRINTO01EZQ661S_63M_ret, PRINTO01EZQ661S_126M_ret, JPNCPIALLMINMEI_21M_ret, JPNCPIALLMINMEI_63M_ret, JPNCPIALLMINMEI_126M_ret, LRHUTTTTJPM156S_21M_ret, LRHUTTTTJPM156S_63M_ret, JPNASSETS_21M_ret, JPNASSETS_63M_ret, JPNASSETS_126M_ret, JPNPROINDMISMEI_21M_ret, JPNPROINDMISMEI_63M_ret, JPNPROINDMISMEI_126M_ret, GBRCPIALLMINMEI_21M_ret, LRHUTTTTGBM156S_21M_ret, GBRPROINDMISMEI_21M_ret, GBRPROINDMISMEI_63M_ret, GBRPROINDMISMEI_126M_ret, ratio_copper_gold_21M_ret, ratio_credit_spread_126M_ret, ratio_consumer_risk_21M_ret, ratio_consumer_risk_63M_ret, ratio_consumer_risk_126M_ret, ratio_risk_on_off_63M_ret, ratio_risk_on_off_126M_ret, ratio_tech_dominance_21M_ret, ratio_tech_dominance_63M_ret, ratio_tech_dominance_126M_ret, ratio_intl_vs_us_bonds_21M_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makrooekonomisches Setup:**

*   **Zinskurven-Dominanz:** `T10Y2Y_63M_ret` (10Y-2Y Spread) als Top-Prädiktor unterstreicht die fundamentale Rolle der Zinskurvensteilheit als Frühindikator für Rezessionsrisiken und Wachstumsdynamik. Das 5-Jahres-Momentum deutet auf die Relevanz persistenter Trends in den makroökonomischen Erwartungen hin.
*   **Geldpolitik & Zinsniveau:** `^IRX_21M_ret` (3M T-Bill) und `^TNX_21M_ret`/`_63M_ret` (10Y T-Note) bilden das absolute Zinsniveau und kurzfristige geldpolitische Erwartungen ab. Deren Momentum zeigt die Richtung der Finanzierungskonditionen und der Marktliquidität.
*   **Kreditmarkt als Risikometer:** `ratio_credit_spread_21M_ret` und `_63M_ret` signalisieren die Marktliquidität und Risikobereitschaft der Anleger. Sich ausweitende Spreads deuten auf eine Verschlechterung der Kreditbedingungen und erhöhte Rezessionswahrscheinlichkeit hin; sich verengende Spreads auf eine Verbesserung.
*   **Inflationserwartungen:** `ZW=F_63M_ret` (Weizen-Futures) dient als Proxy für globale Agrar-Rohstoffpreise und damit für Inflationsdruck, insbesondere im Kontext von Lebensmittelpreisen und Lieferketten. Das 5-Jahres-Momentum erfasst strukturelle Inflationstrends.
*   **Risikobereitschaft & Sentiment:** `ratio_risk_on_off_21M_ret` misst die Allokationspräferenz zwischen risikoreichen und sicheren Anlagen und quantifiziert somit das übergeordnete Marktsentiment und die Risikobereitschaft.
*   **Makro-Momentum (generisch):** `LRHUTTTTEZM156S_21M_ret` (angenommener makroökonomischer Indikator) mit 1.75-Jahres-Momentum reflektiert die Stärke oder Schwäche zugrunde liegender Wirtschaftsdaten (z.B. Arbeitsmarkt, Konsum) und deren Einfluss auf die breitere Wirtschaft.
*   **Währungs-Neutralität:** Das Fehlen expliziter Währungsindikatoren deutet darauf hin, dass deren Einfluss auf den SPY entweder durch Zinsdifferenziale und Rohstoffpreise implizit erfasst wird oder für den 6-Monats-Horizont keine signifikante eigenständige Prognosekraft besitzt.

**2. Sektor- & Marktdynamik:**

*   **Säkulares Technologie-Wachstum:** `AAPL_126M_ret` (10.5 Jahre Momentum) weist auf die entscheidende Rolle von Mega-Cap-Tech-Momentum als Indikator für globales Wachstum, Konsumentenstärke und die Dominanz von Innovationsführern im Markt hin. Ein positiver Trend hier ist oft korreliert mit Risiko-On-Phasen.
*   **Zyklische Energie als Frühindikator:** `XLE_63M_ret` (5 Jahre Momentum) spiegelt die Stärke des Energie-Sektors wider, der hochzyklisch ist und stark mit Rohstoffpreisen sowie der globalen Industrietätigkeit korreliert. Ein Aufwärtstrend in XLE signalisiert oft eine Expansion.
*   **Real Estate & Zins-Sensitivität:** `VNQ_126M_ret` (10.5 Jahre Momentum) erfasst langfristige Trends im Immobilienmarkt, der empfindlich auf Zinsänderungen, Konjunkturzyklen und Demografie reagiert. Ein robustes VNQ-Momentum kann auf stabile Wachstums- und Inflationserwartungen hindeuten.
*   **Implizite Sektorrotation:** Die Kombination aus säkularer Tech-Stärke, zyklischer Energie und zins-sensitivem Real Estate ermöglicht die Detektion von Sektorrotationen, die charakteristisch für verschiedene Phasen des Konjunkturzyklus und der Risikobereitschaft sind.

**3. Quant-Konklusion:**

*   **Primäre Steuerungsfaktoren:** Der SPY wird primär durch das **makroökonomische Umfeld** getrieben, welches durch die **Zinskurvendynamik** (insbesondere der langfristige Trend der 10Y-2Y-Steilheit) und die **Liquidität/Risikobereitschaft am Kreditmarkt** (Credit Spreads) quantifiziert wird.
*   **Sektorielle Bestätigung:** Das extrem lange Momentum in **Mega-Cap-Tech (AAPL)**, **zyklischer Energie (XLE)** und **Real Estate (VNQ)** fungiert als sekundärer, aber hochgewichteter Bestätigungsindikator für die durch die makroökonomischen Variablen implizierten Wachstums- und Inflationserwartungen.
*   **Synthetisches Narrativ:** Ein bullisches Signal für den SPY über 6 Monate ist zu erwarten bei einer **steiler werdenden Zinskurve** (positiver 5-Jahres-Trend), **sich verengenden Kreditspreads** (positive 1.75/5-Jahres-Trends), unterstützt durch **anhaltendes positives Momentum in Tech, Energie und Real Estate** und einer **zunehmenden Risikobereitschaft** im breiteren Markt. Umgekehrt signalisieren entgegengesetzte Trends ein bearishes Outlook.

## Mathematische Modellparameter

- **Intercepts:** `[0.013037685016784492, -1.2343021945650094, 1.2212645095482313]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.11868892  0.22237087  0.22184851  0.27290245  0.1800793  -0.12363985
  -0.07936019 -0.42087727 -0.1397693   0.29127734  0.03541702  0.06164144]
 [ 0.25933781 -0.14427146  0.07563978 -0.23591433  0.01308591  0.0560679
   0.10936981 -0.02396306 -0.02525644 -0.20753426 -0.25479397  0.01332034]
 [-0.37802673 -0.07809941 -0.29748829 -0.03698812 -0.19316521  0.06757195
  -0.03000962  0.44484033  0.16502575 -0.08374308  0.21937694 -0.07496178]]
  ```
