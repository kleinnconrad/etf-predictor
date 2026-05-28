# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-28 14:30:03
- **Target ETF:** DBXJ.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-27** prognostiziert das Modell:

> **Klasse:** Down
>
> **Wahrscheinlichkeiten:** Down: 40.07% | Flat: 21.34% | Up: 38.59%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| LRHUTTTTEZM156S_63D_ret | 0.506845 |
| ZW=F_126D_ret | 0.386595 |
| ratio_credit_spread_21D_ret | 0.344839 |
| RIO.L_63D_ret | 0.296621 |
| PAYEMS_63D_ret | 0.283035 |
| ^TNX_21D_ret | 0.222956 |
| DBXJ.DE_126D_ret | 0.160249 |
| XLU_126D_ret | 0.145300 |
| ECBASSETS_21D_ret | 0.134825 |
| UNRATE_63D_ret | 0.122858 |
| LRHUTTTTJPM156S_21D_ret | 0.109826 |
| LRHUTTTTJPM156S_63D_ret | 0.088945 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`9984.T_63D_ret, 9984.T_126D_ret, AZN.L_126D_ret, BNDX_21D_ret, BNDX_63D_ret, BRK-B_126D_ret, BTC-USD_126D_ret, BWX_21D_ret, BWX_63D_ret, BWX_126D_ret, CL=F_63D_ret, CL=F_126D_ret, DBXJ.DE_63D_ret, DX-Y.NYB_21D_ret, DX-Y.NYB_63D_ret, DX-Y.NYB_126D_ret, EEM_63D_ret, EEM_126D_ret, GC=F_21D_ret, GC=F_63D_ret, GC=F_126D_ret, HG=F_63D_ret, HG=F_126D_ret, IGOV_21D_ret, IGOV_63D_ret, IGOV_126D_ret, LE=F_21D_ret, LE=F_63D_ret, LQD_21D_ret, LQD_63D_ret, LQD_126D_ret, RIO.L_126D_ret, SHEL.L_63D_ret, SHEL.L_126D_ret, TLT_21D_ret, TLT_63D_ret, VNQ_126D_ret, XBI_126D_ret, XLE_63D_ret, XLE_126D_ret, XLV_126D_ret, ZW=F_63D_ret, ^GDAXI_126D_ret, ^IRX_63D_ret, ^IRX_126D_ret, ^TNX_63D_ret, ^TNX_126D_ret, CPIAUCSL_63D_ret, CPIAUCSL_126D_ret, PAYEMS_126D_ret, UNRATE_126D_ret, T10Y2Y_126D_ret, WALCL_126D_ret, CP00MI15EA20M086NEST_126D_ret, LRHUTTTTEZM156S_21D_ret, LRHUTTTTEZM156S_126D_ret, PRINTO01EZQ661S_63D_ret, PRINTO01EZQ661S_126D_ret, JPNCPIALLMINMEI_126D_ret, LRHUTTTTJPM156S_126D_ret, LRHUTTTTGBM156S_63D_ret, LRHUTTTTGBM156S_126D_ret, ratio_copper_gold_126D_ret, ratio_credit_spread_63D_ret, ratio_credit_spread_126D_ret, ratio_tech_dominance_63D_ret, ratio_tech_dominance_126D_ret, ratio_intl_vs_us_bonds_126D_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>115</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21D_ret, 7203.T_63D_ret, 7203.T_126D_ret, 8035.T_21D_ret, 8035.T_63D_ret, 8035.T_126D_ret, 9984.T_21D_ret, AAPL_21D_ret, AAPL_63D_ret, AAPL_126D_ret, AZN.L_21D_ret, AZN.L_63D_ret, BAS.DE_21D_ret, BAS.DE_63D_ret, BAS.DE_126D_ret, BNDX_126D_ret, BRK-B_21D_ret, BRK-B_63D_ret, BTC-USD_21D_ret, BTC-USD_63D_ret, CL=F_21D_ret, DBXJ.DE_21D_ret, EEM_21D_ret, HG=F_21D_ret, HYG_21D_ret, HYG_63D_ret, HYG_126D_ret, JPM_21D_ret, JPM_63D_ret, JPM_126D_ret, LE=F_126D_ret, MSFT_21D_ret, MSFT_63D_ret, MSFT_126D_ret, NVDA_21D_ret, NVDA_63D_ret, NVDA_126D_ret, RIO.L_21D_ret, SAP.DE_21D_ret, SAP.DE_63D_ret, SAP.DE_126D_ret, SHEL.L_21D_ret, SIE.DE_21D_ret, SIE.DE_63D_ret, SIE.DE_126D_ret, SPY_21D_ret, SPY_63D_ret, SPY_126D_ret, TLT_126D_ret, VNQ_21D_ret, VNQ_63D_ret, XBI_21D_ret, XBI_63D_ret, XLE_21D_ret, XLF_21D_ret, XLF_63D_ret, XLF_126D_ret, XLK_21D_ret, XLK_63D_ret, XLK_126D_ret, XLP_21D_ret, XLP_63D_ret, XLP_126D_ret, XLU_21D_ret, XLU_63D_ret, XLV_21D_ret, XLV_63D_ret, ZC=F_21D_ret, ZC=F_63D_ret, ZC=F_126D_ret, ZW=F_21D_ret, ^GDAXI_21D_ret, ^GDAXI_63D_ret, ^IRX_21D_ret, ^N225_21D_ret, ^N225_63D_ret, ^N225_126D_ret, ^VIX_21D_ret, ^VIX_63D_ret, ^VIX_126D_ret, CPIAUCSL_21D_ret, PAYEMS_21D_ret, UNRATE_21D_ret, T10Y2Y_21D_ret, T10Y2Y_63D_ret, WALCL_21D_ret, WALCL_63D_ret, CP00MI15EA20M086NEST_21D_ret, CP00MI15EA20M086NEST_63D_ret, ECBASSETS_63D_ret, ECBASSETS_126D_ret, PRINTO01EZQ661S_21D_ret, JPNCPIALLMINMEI_21D_ret, JPNCPIALLMINMEI_63D_ret, JPNASSETS_21D_ret, JPNASSETS_63D_ret, JPNASSETS_126D_ret, JPNPROINDMISMEI_21D_ret, JPNPROINDMISMEI_63D_ret, JPNPROINDMISMEI_126D_ret, GBRCPIALLMINMEI_21D_ret, GBRCPIALLMINMEI_63D_ret, GBRCPIALLMINMEI_126D_ret, LRHUTTTTGBM156S_21D_ret, GBRPROINDMISMEI_21D_ret, GBRPROINDMISMEI_63D_ret, GBRPROINDMISMEI_126D_ret, ratio_copper_gold_21D_ret, ratio_copper_gold_63D_ret, ratio_risk_on_off_21D_ret, ratio_risk_on_off_63D_ret, ratio_risk_on_off_126D_ret, ratio_tech_dominance_21D_ret, ratio_intl_vs_us_bonds_21D_ret, ratio_intl_vs_us_bonds_63D_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

Hier ist die ökonomische Einschätzung Ihres Indikator-Sets:

**1. Makroökonomisches Setup:**

*   **Globale Liquidität & Zinslandschaft (LRHUTTTTEZM156S, ^TNX, ECBASSETS):** Die hohe Signifikanz von Eurozonen-Anleihe-Futures (Bobl-Proxy), der US-10-Jahresrendite und der EZB-Bilanz suggeriert, dass DBXJ.DE primär auf externe Zins- und Liquiditätszyklen, insbesondere jene der EZB und der Fed, reagiert. Globale Zinsdivergenzen und die Geldpolitik der großen Zentralbanken sind dominante Treiber.
*   **Systemisches Risiko & Kreditkonditionen (ratio_credit_spread):** Der hohe Einfluss von Kreditspread-Veränderungen unterstreicht die Rolle von globaler Risikoaversion und der Verfügbarkeit von Kredit. Eine Verschlechterung der Kreditbedingungen führt zu einer Flucht aus Risikokapital, welche sich direkt auf den japanischen Markt auswirkt.
*   **Globale Wachstums- & Inflationserwartungen (ZW=F, PAYEMS, UNRATE):** Weizen-Futures (ZW=F) als Indikator für globale Rohstoffpreise und Inflation sowie US-Arbeitsmarktdaten (PAYEMS, UNRATE) als Proxy für die US-Konjunktur zeigen, dass DBXJ.DE stark an die globalen Wachstums- und Inflationsdynamiken gekoppelt ist.
*   **Ignorierte Währungen/Nationale Zinsen:** Die geringere Relevanz spezifischer japanischer Anleihe-Futures (LRHUTTTTJPM156S) im Vergleich zu Eurozonen-Anleihen deutet darauf hin, dass die BoJ-Politik und Yen-Bewegungen weniger entscheidend sind als die globalen Zins- und Liquiditätsbedingungen. Dies unterstreicht die externe Abhängigkeit.

**2. Sektor- & Marktdynamik:**

*   **Zyklische Sensitivität (RIO.L):** Die prominente Rolle von Rio Tinto (globaler Bergbau) signalisiert eine starke Korrelation des DBXJ.DE mit der globalen Industrieproduktion und dem Rohstoffzyklus, insbesondere der Nachfrage aus China. Dies positioniert DBXJ.DE als späten Früh- oder Mittelzykliker im globalen Kontext.
*   **Defensive vs. Zyklische Rotation (XLU):** Das Momentum des US-Versorger-Sektors (XLU) indiziert eine Abbildung der globalen Sektor-Rotation. Eine überdurchschnittliche Performance von XLU (defensiv) impliziert eine Risikoaversion und eine Flucht in Sicherheit, was für den zyklischen japanischen Exportmarkt negativ wäre.
*   **Intrinsisches Markt-Momentum (DBXJ.DE_126D_ret):** Die Einbeziehung des eigenen 6-Monats-Momentums des DBXJ.DE bestätigt die Relevanz von Trendfolgestrategien und Marktpersistenz für die kurz- bis mittelfristige Vorhersage.

**3. Quant-Konklusion:**

*   **Japan als globaler Beta-Hebel:** Das Modell identifiziert DBXJ.DE primär als einen hochgradig derivativen Markt, dessen Zustand stark durch die globale Konjunktur, die monetären Bedingungen der grossen Zentralbanken und die globale Risikobereitschaft bestimmt wird.
*   **Priorität externer Impulse:** Die Prognosequalität für DBXJ.DE basiert hauptsächlich auf externen makroökonomischen Signalen, wobei die Eurozone und die USA als führende Indikatoren für globale Liquidität, Zinsen und Wachstumsdynamik agieren.
*   **Sensitivität gegenüber systemischem Stress:** Kreditspreads fungieren als Frühwarnsystem für systemischen Stress, der direkt auf die Performance von DBXJ.DE durch Kapitalflucht aus Risikoanlagen wirkt.
*   **Momentum-Bestätigung:** Die Relevanz des eigenen 6-Monats-Momentums des DBXJ.DE bedeutet, dass bestehende Markttrends wahrscheinlich anhalten, und die externen Makroindikatoren diese Trends entweder bestätigen oder Wendepunkte signalisieren.

## Mathematische Modellparameter

- **Intercepts:** `[-0.14023186283342148, -0.19152367871326165, 0.33175554154669396]`

- **Koeffizienten-Matrix:**
  ```text
[[ 2.14877435e-01 -4.44931101e-01  1.03155267e-01  5.79892675e-01
  -1.80290130e-01 -2.14718378e-01 -3.23796317e-02 -7.60267652e-01
  -7.32003771e-04 -1.15421844e-01  2.04422926e-02  5.17258450e-01]
 [ 2.54960608e-02  2.19981822e-02  1.14794286e-01 -1.97689940e-01
   3.34433761e-01  4.24552365e-01  1.84287379e-01  2.63835473e-01
   2.02236792e-01 -4.93178284e-02 -1.33417540e-01 -2.96315747e-01]
 [-2.40373496e-01  4.22932919e-01 -2.17949553e-01 -3.82202735e-01
  -1.54143631e-01 -2.09833987e-01 -1.51907747e-01  4.96432179e-01
  -2.01504789e-01  1.64739673e-01  1.12975248e-01 -2.20942703e-01]]
  ```
