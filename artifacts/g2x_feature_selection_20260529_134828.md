# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-29 13:49:53
- **Target ETF:** G2X.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-28** prognostiziert das Modell:

> **Klasse:** Up
>
> **Wahrscheinlichkeiten:** Down: 7.73% | Flat: 16.26% | Up: 76.01%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| JPNASSETS_63D_ret | 0.534142 |
| BNDX_126D_ret | 0.516609 |
| XLK_126D_ret | 0.391183 |
| DX-Y.NYB_63D_ret | 0.339001 |
| GC=F_21D_ret | 0.260597 |
| ^IRX_63D_ret | 0.240865 |
| ^IRX_21D_ret | 0.147572 |
| JPNASSETS_126D_ret | 0.135860 |
| ECBASSETS_21D_ret | 0.082292 |
| WALCL_63D_ret | 0.052850 |
| ZW=F_63D_ret | 0.044515 |
| AAPL_63D_ret | 0.020737 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`7203.T_63D_ret, 8035.T_63D_ret, 8035.T_126D_ret, AAPL_126D_ret, BAS.DE_63D_ret, BAS.DE_126D_ret, BNDX_21D_ret, BNDX_63D_ret, BRK-B_63D_ret, BRK-B_126D_ret, BTC-USD_63D_ret, BTC-USD_126D_ret, CL=F_21D_ret, CL=F_63D_ret, CL=F_126D_ret, DX-Y.NYB_126D_ret, EEM_63D_ret, EEM_126D_ret, GC=F_63D_ret, HG=F_63D_ret, HG=F_126D_ret, LQD_21D_ret, LQD_63D_ret, LQD_126D_ret, MSFT_126D_ret, NVDA_63D_ret, NVDA_126D_ret, RIO.L_63D_ret, RIO.L_126D_ret, SAP.DE_126D_ret, SHEL.L_126D_ret, TLT_21D_ret, TLT_63D_ret, XLE_63D_ret, XLE_126D_ret, XLU_126D_ret, XLV_126D_ret, ZC=F_63D_ret, ZC=F_126D_ret, ZW=F_126D_ret, ^IRX_126D_ret, ^TNX_21D_ret, ^TNX_63D_ret, ^TNX_126D_ret, ^VIX_63D_ret, CPIAUCSL_63D_ret, PAYEMS_21D_ret, WALCL_21D_ret, WALCL_126D_ret, CP00MI15EA20M086NEST_63D_ret, ECBASSETS_63D_ret, ECBASSETS_126D_ret, PRINTO01EZQ661S_63D_ret, PRINTO01EZQ661S_126D_ret, JPNASSETS_21D_ret, GBRCPIALLMINMEI_63D_ret, ratio_copper_gold_21D_ret, ratio_copper_gold_63D_ret, ratio_copper_gold_126D_ret, ratio_credit_spread_21D_ret, ratio_credit_spread_63D_ret, ratio_credit_spread_126D_ret, ratio_risk_on_off_63D_ret, ratio_risk_on_off_126D_ret, ratio_tech_dominance_126D_ret, ratio_intl_vs_us_bonds_21D_ret, ratio_intl_vs_us_bonds_63D_ret, ratio_intl_vs_us_bonds_126D_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>121</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21D_ret, 7203.T_126D_ret, 8035.T_21D_ret, 9984.T_21D_ret, 9984.T_63D_ret, 9984.T_126D_ret, AAPL_21D_ret, AZN.L_21D_ret, AZN.L_63D_ret, AZN.L_126D_ret, BAS.DE_21D_ret, BRK-B_21D_ret, BTC-USD_21D_ret, BWX_21D_ret, BWX_63D_ret, BWX_126D_ret, DX-Y.NYB_21D_ret, EEM_21D_ret, G2X.DE_21D_ret, G2X.DE_63D_ret, G2X.DE_126D_ret, GC=F_126D_ret, HG=F_21D_ret, HYG_21D_ret, HYG_63D_ret, HYG_126D_ret, IGOV_21D_ret, IGOV_63D_ret, IGOV_126D_ret, JPM_21D_ret, JPM_63D_ret, JPM_126D_ret, LE=F_21D_ret, LE=F_63D_ret, LE=F_126D_ret, MSFT_21D_ret, MSFT_63D_ret, NVDA_21D_ret, RIO.L_21D_ret, SAP.DE_21D_ret, SAP.DE_63D_ret, SHEL.L_21D_ret, SHEL.L_63D_ret, SIE.DE_21D_ret, SIE.DE_63D_ret, SIE.DE_126D_ret, SPY_21D_ret, SPY_63D_ret, SPY_126D_ret, TLT_126D_ret, VNQ_21D_ret, VNQ_63D_ret, VNQ_126D_ret, XBI_21D_ret, XBI_63D_ret, XBI_126D_ret, XLE_21D_ret, XLF_21D_ret, XLF_63D_ret, XLF_126D_ret, XLK_21D_ret, XLK_63D_ret, XLP_21D_ret, XLP_63D_ret, XLP_126D_ret, XLU_21D_ret, XLU_63D_ret, XLV_21D_ret, XLV_63D_ret, XLY_21D_ret, XLY_63D_ret, XLY_126D_ret, ZC=F_21D_ret, ZW=F_21D_ret, ^GDAXI_21D_ret, ^GDAXI_63D_ret, ^GDAXI_126D_ret, ^N225_21D_ret, ^N225_63D_ret, ^N225_126D_ret, ^VIX_21D_ret, ^VIX_126D_ret, CPIAUCSL_21D_ret, CPIAUCSL_126D_ret, PAYEMS_63D_ret, PAYEMS_126D_ret, UNRATE_21D_ret, UNRATE_63D_ret, UNRATE_126D_ret, T10Y2Y_21D_ret, T10Y2Y_63D_ret, T10Y2Y_126D_ret, CP00MI15EA20M086NEST_21D_ret, CP00MI15EA20M086NEST_126D_ret, LRHUTTTTEZM156S_21D_ret, LRHUTTTTEZM156S_63D_ret, LRHUTTTTEZM156S_126D_ret, PRINTO01EZQ661S_21D_ret, JPNCPIALLMINMEI_21D_ret, JPNCPIALLMINMEI_63D_ret, JPNCPIALLMINMEI_126D_ret, LRHUTTTTJPM156S_21D_ret, LRHUTTTTJPM156S_63D_ret, LRHUTTTTJPM156S_126D_ret, JPNPROINDMISMEI_21D_ret, JPNPROINDMISMEI_63D_ret, JPNPROINDMISMEI_126D_ret, GBRCPIALLMINMEI_21D_ret, GBRCPIALLMINMEI_126D_ret, LRHUTTTTGBM156S_21D_ret, LRHUTTTTGBM156S_63D_ret, LRHUTTTTGBM156S_126D_ret, GBRPROINDMISMEI_21D_ret, GBRPROINDMISMEI_63D_ret, GBRPROINDMISMEI_126D_ret, ratio_consumer_risk_21D_ret, ratio_consumer_risk_63D_ret, ratio_consumer_risk_126D_ret, ratio_risk_on_off_21D_ret, ratio_tech_dominance_21D_ret, ratio_tech_dominance_63D_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makrooekonomisches Setup:**

*   **Zinsen:**
    *   **^IRX_63D_ret / ^IRX_21D_ret (US-Kurzfristzinsen):** Hohe Relevanz der US-T-Bill-Renditen signalisiert die Dominanz der Fed-Politik und globaler Geldmarkterwartungen für die G2X.DE-Bewertung und internationale Kapitalflüsse.
    *   **BNDX_126D_ret (Globale Anleihen):** Starke Gewichtung globaler Aggregate-Bonds zeigt, dass das makroökonomische Sentiment hinsichtlich Inflation und Wachstum über die globalen festverzinslichen Märkte kritisch für die G2X.DE-Performance ist.
*   **Währungen:**
    *   **DX-Y.NYB_63D_ret (US-Dollar Index):** Die Bedeutung des DXY betont die Sensitivität der G2X.DE gegenüber globalem Risikoappetit und dem relativen Attraktivitätsverhältnis zwischen US- und Eurozone-Anlagen.
*   **Rohstoffe:**
    *   **GC=F_21D_ret (Gold):** Kurzfristiges Gold-Momentum signalisiert herrschende Inflationserwartungen und globale Risikoaversion, welche Realzinsen und die Gesamtmarktstimmung beeinflussen.
    *   **ZW=F_63D_ret (Weizen):** Geringer Einfluss des Weizen-Futures deutet auf eine nachrangige Sensitivität gegenüber spezifischen Rohstoff-Schocks oder indirekten Inflationstrends hin.
*   **Zentralbank-Liquidität:**
    *   **JPNASSETS_63D_ret / JPNASSETS_126D_ret (Japanische Assets):** Die dominante Rolle japanischer Assets unterstreicht die globale Liquiditätsperspektive, möglicherweise durch Carry-Trade-Dynamiken oder die BoJ-Politik, die globale Risikoanlagen beeinflusst.
    *   **ECBASSETS_21D_ret / WALCL_63D_ret (EZB/Fed Bilanz):** Die geringere, aber vorhandene Bedeutung der Zentralbank-Bilanzsummen zeigt die anhaltende Relevanz der direkten Liquiditätsschöpfung, jedoch mit geringerer kurzfristiger Prädiktionskraft als die daraus resultierenden Marktsignale (Zinsen/Anleihen).

**2. Sektor- & Marktdynamik:**

*   **Technologie-Führung:**
    *   **XLK_126D_ret (US-Tech Sektor):** Die hohe Gewichtung des US-Technologie-Sektors deutet darauf hin, dass die G2X.DE stark von der globalen Wachstumsdynamik und dem Risikoappetit gegenüber innovativen, wachstumsstarken Branchen profitiert.
    *   **AAPL_63D_ret (Apple):** Obwohl gering gewichtet, verstärkt Apple die Verbindung zur zyklischen Konsumgüterbranche und zum allgemeinen Sentiment für "Big Tech", was die G2X.DE als wachstumsorientiert positioniert.
*   **Globale Risikoexposition:**
    *   **JPNASSETS_63D_ret / JPNASSETS_126D_ret:** Die Vormachtstellung japanischer Assets als Prädiktor signalisiert eine starke Abhängigkeit der G2X.DE von globaler Risikobereitschaft und Kapitalallokation in Schwellen- und entwickelte Märkte, oft als Frühindikator für globale Liquiditätszyklen.
    *   **BNDX_126D_ret:** Globale Anleihemärkte fungieren als Barometer für "Flight-to-Safety" vs. "Risk-On"-Rotationen, was direkt die Kapitalflüsse in und aus europäischen Mid-Caps beeinflusst.

**3. Quant-Konklusion:**

*   **Dominantes Narrativ:** Die G2X.DE-Performance wird maßgeblich von der globalen Liquiditätsdynamik und dem Risikoappetit bestimmt, die sich primär über die Performance japanischer Assets, globale Anleihemärkte und den US-Technologiesektor manifestieren.
*   **Korrelationen:** Eine starke positive Korrelation mit globalen Wachstums- und Risikoanlagen (Tech, Japan) sowie eine hohe Sensitivität gegenüber globalen kurzfristigen Zinsbewegungen und der US-Dollar-Stärke sind entscheidend.
*   **Zinsstruktur:** Die signifikante Rolle der US-Kurzfristzinsen (^IRX) unterstreicht, dass die Erwartungen an die Geldpolitik der Fed einen kritischen Einfluss auf die zukünftige Diskontierung von Cashflows und somit auf die G2X.DE-Bewertung haben.
*   **Sektor-Rotationen:** Das Modell impliziert, dass die G2X.DE von einer anhaltenden Präferenz für wachstumsstarke Sektoren (Tech-Leadership) profitiert, was auf einen "Risk-On"-Modus im globalen Markt schließen lässt.
*   **Gesamtaussage:** Für die nächsten 6 Monate wird die G2X.DE voraussichtlich positiv auf ein Umfeld anhaltender globaler Liquidität, moderater Risikobereitschaft und einer fortgesetzten Outperformance des Technologie-Sektors reagieren, mit der US-Geldpolitik als primärem Lenkungsfaktor.

## Mathematische Modellparameter

- **Intercepts:** `[0.34700155487573353, -0.8050619624777541, 0.45806040760204136]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.02927001 -0.48604028 -0.30358274  0.15906047  0.25966178  0.02682373
   0.21609697  0.29105126 -0.0522493   0.12343751  0.58285093  0.2037903 ]
 [-0.00183611 -0.28887266 -0.20491909 -0.39089489  0.32711325 -0.06677313
   0.00526028  0.07024636  0.0792748  -0.01756797  0.2183624  -0.05381555]
 [ 0.03110612  0.77491295  0.50850182  0.23183442 -0.58677503  0.03994939
  -0.22135725 -0.36129762 -0.0270255  -0.10586954 -0.80121333 -0.14997475]]
  ```
