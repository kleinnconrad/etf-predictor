# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-26 05:33:46
- **Target ETF:** IDEV
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2025-11-20** prognostiziert das Modell:

> **Klasse:** Down
>
> **Wahrscheinlichkeiten:** Down: 23.29% | Flat: 1.67% | Up: 75.05%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| ZW=F_126M_ret | 0.374639 |
| ^IRX_63M_ret | 0.256794 |
| AAPL_126M_ret | 0.204925 |
| CL=F_126M_ret | 0.193306 |
| XLP_126M_ret | 0.186944 |
| ECBASSETS_21M_ret | 0.177978 |
| BNDX_21M_ret | 0.136830 |
| CL=F_21M_ret | 0.127625 |
| CPIAUCSL_63M_ret | 0.117738 |
| GC=F_21M_ret | 0.089198 |
| SHEL.L_63M_ret | 0.087494 |
| CL=F_63M_ret | 0.044282 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`9984.T_63M_ret, 9984.T_126M_ret, AAPL_21M_ret, AAPL_63M_ret, AZN.L_63M_ret, AZN.L_126M_ret, BAS.DE_63M_ret, BNDX_63M_ret, BRK-B_126M_ret, BTC-USD_21M_ret, BTC-USD_63M_ret, BWX_21M_ret, BWX_63M_ret, DX-Y.NYB_21M_ret, DX-Y.NYB_63M_ret, DX-Y.NYB_126M_ret, EEM_63M_ret, EEM_126M_ret, GC=F_63M_ret, GC=F_126M_ret, HYG_63M_ret, IGOV_21M_ret, IGOV_63M_ret, JPM_63M_ret, LQD_21M_ret, LQD_63M_ret, MSFT_126M_ret, SHEL.L_126M_ret, SIE.DE_63M_ret, VNQ_63M_ret, VNQ_126M_ret, XBI_63M_ret, XBI_126M_ret, XLE_63M_ret, XLE_126M_ret, XLP_63M_ret, XLU_63M_ret, XLV_63M_ret, XLV_126M_ret, ZW=F_21M_ret, ZW=F_63M_ret, ^GDAXI_63M_ret, ^IRX_21M_ret, ^IRX_126M_ret, ^N225_63M_ret, ^N225_126M_ret, CPIAUCSL_21M_ret, CPIAUCSL_126M_ret, PAYEMS_63M_ret, PAYEMS_126M_ret, UNRATE_63M_ret, UNRATE_126M_ret, CP00MI15EA20M086NEST_63M_ret, CP00MI15EA20M086NEST_126M_ret, LRHUTTTTEZM156S_21M_ret, LRHUTTTTEZM156S_63M_ret, LRHUTTTTEZM156S_126M_ret, ECBASSETS_63M_ret, ECBASSETS_126M_ret, JPNCPIALLMINMEI_21M_ret, JPNCPIALLMINMEI_63M_ret, JPNCPIALLMINMEI_126M_ret, LRHUTTTTJPM156S_126M_ret, LRHUTTTTGBM156S_21M_ret, LRHUTTTTGBM156S_63M_ret, LRHUTTTTGBM156S_126M_ret, ratio_intl_vs_us_bonds_63M_ret, ratio_intl_vs_us_bonds_126M_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>112</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21M_ret, 7203.T_63M_ret, 7203.T_126M_ret, 8035.T_21M_ret, 8035.T_63M_ret, 8035.T_126M_ret, 9984.T_21M_ret, AZN.L_21M_ret, BAS.DE_21M_ret, BAS.DE_126M_ret, BNDX_126M_ret, BRK-B_21M_ret, BRK-B_63M_ret, BTC-USD_126M_ret, BWX_126M_ret, EEM_21M_ret, HG=F_21M_ret, HG=F_63M_ret, HG=F_126M_ret, HYG_21M_ret, HYG_126M_ret, IDEV_21M_ret, IDEV_63M_ret, IDEV_126M_ret, IGOV_126M_ret, JPM_21M_ret, JPM_126M_ret, LE=F_21M_ret, LE=F_63M_ret, LE=F_126M_ret, LQD_126M_ret, MSFT_21M_ret, MSFT_63M_ret, NVDA_21M_ret, NVDA_63M_ret, NVDA_126M_ret, RIO.L_21M_ret, RIO.L_63M_ret, RIO.L_126M_ret, SAP.DE_21M_ret, SAP.DE_63M_ret, SAP.DE_126M_ret, SHEL.L_21M_ret, SIE.DE_21M_ret, SIE.DE_126M_ret, TLT_21M_ret, TLT_63M_ret, TLT_126M_ret, VNQ_21M_ret, XBI_21M_ret, XLE_21M_ret, XLF_21M_ret, XLF_63M_ret, XLF_126M_ret, XLK_21M_ret, XLK_63M_ret, XLK_126M_ret, XLP_21M_ret, XLU_21M_ret, XLU_126M_ret, XLV_21M_ret, XLY_21M_ret, XLY_63M_ret, XLY_126M_ret, ZC=F_21M_ret, ZC=F_63M_ret, ZC=F_126M_ret, ^GDAXI_21M_ret, ^GDAXI_126M_ret, ^N225_21M_ret, ^TNX_21M_ret, ^TNX_63M_ret, ^TNX_126M_ret, ^VIX_21M_ret, ^VIX_63M_ret, ^VIX_126M_ret, PAYEMS_21M_ret, UNRATE_21M_ret, T10Y2Y_21M_ret, T10Y2Y_63M_ret, T10Y2Y_126M_ret, WALCL_21M_ret, WALCL_63M_ret, WALCL_126M_ret, CP00MI15EA20M086NEST_21M_ret, PRINTO01EZQ661S_21M_ret, PRINTO01EZQ661S_63M_ret, PRINTO01EZQ661S_126M_ret, LRHUTTTTJPM156S_21M_ret, LRHUTTTTJPM156S_63M_ret, JPNASSETS_21M_ret, JPNASSETS_63M_ret, JPNASSETS_126M_ret, JPNPROINDMISMEI_21M_ret, JPNPROINDMISMEI_63M_ret, JPNPROINDMISMEI_126M_ret, GBRCPIALLMINMEI_21M_ret, GBRCPIALLMINMEI_63M_ret, GBRCPIALLMINMEI_126M_ret, GBRPROINDMISMEI_21M_ret, GBRPROINDMISMEI_63M_ret, GBRPROINDMISMEI_126M_ret, ratio_copper_gold_21M_ret, ratio_copper_gold_63M_ret, ratio_copper_gold_126M_ret, ratio_credit_spread_21M_ret, ratio_credit_spread_63M_ret, ratio_credit_spread_126M_ret, ratio_consumer_risk_21M_ret, ratio_consumer_risk_63M_ret, ratio_consumer_risk_126M_ret, ratio_intl_vs_us_bonds_21M_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makrooekonomisches Setup:**

*   **Zinsen:**
    *   ^IRX_63M_ret: Langfristiges Momentum kurzer US-Zinsen (13-Wochen T-Bill) indiziert persistente Ausrichtung der US-Geldpolitik und makroökonomische Zyklusphase. Globale Referenz für Diskontierung und Kapitalkosten.
    *   BNDX_21M_ret: Momentum internationaler Anleihen (ex-US) signalisiert globale Zinsdifferenziale, aggregierte Risikobereitschaft und Kapitalflüsse zwischen Währungsräumen.
*   **Währungen:**
    *   ZW=F_126M_ret: Extrem langfristiges Momentum des Schweizer Frankens als führender Safe-Haven-Indikator reflektiert strukturelle, anhaltende globale Risikoaversion und geopolitische Unsicherheit. Höchste prädiktive Kraft.
*   **Rohstoffe:**
    *   CL=F (126M, 63M, 21M): Multiple Momentum-Fenster für Rohöl (WTI) unterstreichen die kritische Rolle als globaler Nachfrageindikator, Inflationstreiber und geopolitischer Risikofaktor. Erfasst verschiedene Zykluslängen.
    *   GC=F_21M_ret: Mittelfristiges Gold-Momentum ergänzt das Safe-Haven-Narrativ, signalisiert Inflationsschutzpräferenzen und/oder sinkende Realzinsen.
*   **Zentralbankpolitik:**
    *   ECBASSETS_21M_ret: Momentum der EZB-Bilanzsumme quantifiziert europäische Liquiditätsbedingungen und geldpolitische Haltung, direkt relevant für die Risikobereitschaft in europäischen IDEV-Märkten.
*   **Inflation:**
    *   CPIAUCSL_63M_ret: Langfristiges Momentum der US-Konsuminflation dient als globaler Anker für Inflationserwartungen und impliziert die zukünftige Reaktionsfunktion der Zentralbanken.

**2. Sektor- & Marktdynamik:**

*   **Sektorrotation:**
    *   XLP_126M_ret: Langfristiges Momentum im defensiven Konsumgütersektor signalisiert Präferenz für stabile Erträge und geringe Beta-Werte, typisch für Spätzyklusphasen oder wirtschaftliche Abschwächung.
    *   SHEL.L_63M_ret: Mittelfristiges Momentum eines globalen Energieriesen indiziert zyklische Stärke oder Schwäche im traditionellen Industriesektor, korreliert stark mit globaler Wirtschaftstätigkeit und Rohölpreisen.
    *   AAPL_126M_ret: Langfristiges Momentum eines globalen Technologieführers repräsentiert die Performance von Wachstumswerten und Konsumdiscretionary. Zeigt die Resilienz oder Schwäche von Tech-Dominanz gegenüber anderen Sektoren.
*   **Korrelationen & Divergenzen:**
    *   Die gleichzeitige Relevanz von defensiven Sektoren (XLP), zyklischen Rohstoffen (CL=F, SHEL.L) und einem selektiven Growth-Titel (AAPL) signalisiert keine homogene Sektor-Rotation, sondern eine fragmentierte Marktbewertung und divergierende Einschätzung des Konjunkturzyklus.
    *   Das Set spiegelt eine komplexe Interaktion zwischen risikobereitem Wachstumskapital und defensiven Allokationen wider, oft charakteristisch für Wendepunkte oder Phasen erhöhter Unsicherheit.

**3. Quant-Konklusion:**

*   **Anhaltende Risikoaversion:** Die Dominanz von ZW=F_126M_ret und die Präsenz von XLP_126M_ret und GC=F_21M_ret deuten auf ein anhaltend vorsichtiges Marktumfeld mit struktureller Neigung zu sicheren Häfen und defensiven Anlagestrategien hin.
*   **Omnipräsenter Inflations-/Zinsdruck:** Mehrere Öl-Momentum-Fenster, CPIAUCSL_63M_ret und ^IRX_63M_ret unterstreichen die anhaltende Relevanz von Inflation und Zentralbankzinsen als primäre Makro-Treiber für die IDEV-Märkte.
*   **Fragmentierter Konjunkturzyklus:** Die gemischte Signatur aus Wachstumstiteln (AAPL) und defensiven Werten (XLP), zusammen mit zyklischen Rohstoffen (CL=F, SHEL.L), deutet auf eine nicht-lineare, wahrscheinlich moderatere Wachstumsphase mit sektoralen Disparitäten hin.
*   **IDEV-Narrativ:** Für die nächsten 6 Monate ist ein IDEV-Umfeld zu erwarten, das von anhaltendem Inflations- und Zinsdruck geprägt ist, kombiniert mit struktureller Unsicherheit. Das Marktklima wird wahrscheinlich volatil bleiben, mit einer Tendenz zur Kapitalallokation in Qualität und Defensivwerte, während selektive Wachstumsstorys und rohstoffgetriebene Sektoren ihre Relevanz behalten. Das übergeordnete Signal ist ein erhöhter Bedarf an Risikomanagement.

## Mathematische Modellparameter

- **Intercepts:** `[0.45140285257298207, -1.3727952061618625, 0.9213923535888853]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.27254453 -0.10218031  0.14034458 -0.00227235 -0.22186584 -0.01730842
  -0.00152477 -0.02587284  0.56195786  0.36925374  0.17660771  0.12201357]
 [-0.30738825  0.20524574  0.05109324  0.06642329  0.28995839 -0.11648899
  -0.12971592  0.28041638 -0.29139905  0.0159378  -0.16041183  0.14495281]
 [ 0.03484372 -0.10306543 -0.19143782 -0.06415094 -0.06809255  0.13379741
   0.1312407  -0.25454354 -0.27055882 -0.38519154 -0.01619589 -0.26696638]]
  ```
