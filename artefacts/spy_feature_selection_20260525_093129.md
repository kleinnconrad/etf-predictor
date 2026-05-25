# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-25 09:32:26
- **Target ETF:** SPY
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2025-11-20** prognostiziert das Modell:

> **Klasse:** Up
>
> **Wahrscheinlichkeiten:** Down: 16.53% | Flat: 8.03% | Up: 75.45%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| BAS.DE_126M_ret | 0.538583 |
| VNQ_126M_ret | 0.392067 |
| XLE_63M_ret | 0.382753 |
| CPIAUCSL_63M_ret | 0.276083 |
| JPM_126M_ret | 0.225550 |
| JPNCPIALLMINMEI_21M_ret | 0.223753 |
| XLU_126M_ret | 0.218166 |
| ^IRX_126M_ret | 0.098488 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`8035.T_63M_ret, 8035.T_126M_ret, 9984.T_63M_ret, 9984.T_126M_ret, AAPL_63M_ret, AAPL_126M_ret, AZN.L_126M_ret, BNDX_21M_ret, BNDX_63M_ret, BNDX_126M_ret, BTC-USD_21M_ret, BTC-USD_63M_ret, BTC-USD_126M_ret, BWX_21M_ret, BWX_63M_ret, BWX_126M_ret, DX-Y.NYB_21M_ret, DX-Y.NYB_63M_ret, DX-Y.NYB_126M_ret, EEM_63M_ret, EEM_126M_ret, GC=F_63M_ret, HG=F_63M_ret, HG=F_126M_ret, HYG_63M_ret, HYG_126M_ret, IGOV_21M_ret, IGOV_63M_ret, IGOV_126M_ret, JPM_63M_ret, LE=F_126M_ret, LQD_21M_ret, LQD_63M_ret, LQD_126M_ret, NVDA_63M_ret, RIO.L_126M_ret, SAP.DE_126M_ret, SHEL.L_126M_ret, SIE.DE_126M_ret, TLT_21M_ret, XBI_63M_ret, XBI_126M_ret, XLE_126M_ret, XLU_63M_ret, ZW=F_21M_ret, ZW=F_63M_ret, ZW=F_126M_ret, ^GDAXI_63M_ret, ^GDAXI_126M_ret, ^IRX_63M_ret, ^N225_126M_ret, ^TNX_21M_ret, CPIAUCSL_21M_ret, CPIAUCSL_126M_ret, PAYEMS_126M_ret, UNRATE_126M_ret, CP00MI15EA20M086NEST_21M_ret, CP00MI15EA20M086NEST_63M_ret, CP00MI15EA20M086NEST_126M_ret, LRHUTTTTEZM156S_21M_ret, LRHUTTTTEZM156S_63M_ret, LRHUTTTTEZM156S_126M_ret, ECBASSETS_63M_ret, ECBASSETS_126M_ret, JPNCPIALLMINMEI_126M_ret, LRHUTTTTJPM156S_126M_ret, JPNASSETS_126M_ret, GBRCPIALLMINMEI_21M_ret, GBRCPIALLMINMEI_63M_ret, GBRCPIALLMINMEI_126M_ret, LRHUTTTTGBM156S_63M_ret, LRHUTTTTGBM156S_126M_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>100</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21M_ret, 7203.T_63M_ret, 7203.T_126M_ret, 8035.T_21M_ret, 9984.T_21M_ret, AAPL_21M_ret, AZN.L_21M_ret, AZN.L_63M_ret, BAS.DE_21M_ret, BAS.DE_63M_ret, BRK-B_21M_ret, BRK-B_63M_ret, BRK-B_126M_ret, CL=F_21M_ret, CL=F_63M_ret, CL=F_126M_ret, EEM_21M_ret, GC=F_21M_ret, GC=F_126M_ret, HG=F_21M_ret, HYG_21M_ret, JPM_21M_ret, LE=F_21M_ret, LE=F_63M_ret, MSFT_21M_ret, MSFT_63M_ret, MSFT_126M_ret, NVDA_21M_ret, NVDA_126M_ret, RIO.L_21M_ret, RIO.L_63M_ret, SAP.DE_21M_ret, SAP.DE_63M_ret, SHEL.L_21M_ret, SHEL.L_63M_ret, SIE.DE_21M_ret, SIE.DE_63M_ret, SPY_21M_ret, SPY_63M_ret, SPY_126M_ret, TLT_63M_ret, TLT_126M_ret, VNQ_21M_ret, VNQ_63M_ret, XBI_21M_ret, XLE_21M_ret, XLF_21M_ret, XLF_63M_ret, XLF_126M_ret, XLK_21M_ret, XLK_63M_ret, XLK_126M_ret, XLP_21M_ret, XLP_63M_ret, XLP_126M_ret, XLU_21M_ret, XLV_21M_ret, XLV_63M_ret, XLV_126M_ret, XLY_21M_ret, XLY_63M_ret, XLY_126M_ret, ZC=F_21M_ret, ZC=F_63M_ret, ZC=F_126M_ret, ^GDAXI_21M_ret, ^IRX_21M_ret, ^N225_21M_ret, ^N225_63M_ret, ^TNX_63M_ret, ^TNX_126M_ret, ^VIX_21M_ret, ^VIX_63M_ret, ^VIX_126M_ret, PAYEMS_21M_ret, PAYEMS_63M_ret, UNRATE_21M_ret, UNRATE_63M_ret, T10Y2Y_21M_ret, T10Y2Y_63M_ret, T10Y2Y_126M_ret, WALCL_21M_ret, WALCL_63M_ret, WALCL_126M_ret, ECBASSETS_21M_ret, PRINTO01EZQ661S_21M_ret, PRINTO01EZQ661S_63M_ret, PRINTO01EZQ661S_126M_ret, JPNCPIALLMINMEI_63M_ret, LRHUTTTTJPM156S_21M_ret, LRHUTTTTJPM156S_63M_ret, JPNASSETS_21M_ret, JPNASSETS_63M_ret, JPNPROINDMISMEI_21M_ret, JPNPROINDMISMEI_63M_ret, JPNPROINDMISMEI_126M_ret, LRHUTTTTGBM156S_21M_ret, GBRPROINDMISMEI_21M_ret, GBRPROINDMISMEI_63M_ret, GBRPROINDMISMEI_126M_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makrooekonomisches Setup:**

*   **Zinsstruktur & Monetäre Politik:**
    *   `^IRX_126M_ret`: Langfristiges Momentum der kurzfristigen Zinsen signalisiert persistente Shifts in der Zentralbankpolitik und den Liquiditätsbedingungen, die direkten Einfluss auf Diskontierungssätze und Kreditkosten haben. Fokus auf kurzfristige Raten deutet auf die Relevanz der geldpolitischen Hebel an der kurzen Seite der Kurve hin.
    *   Das Fehlen direkter Langfristzins-Indikatoren legt nahe, dass die Reaktion der kurzfristigen Zinsen auf makroökonomische Faktoren wichtiger ist als die absolute Steigung der Zinskurve selbst.
*   **Inflation & Deflation:**
    *   `CPIAUCSL_63M_ret` (US CPI) und `JPNCPIALLMINMEI_21M_ret` (Japan Core CPI): Die Kombination betont die duale Relevanz von US-Kerninflationstrends über mittlere Frist und die agilere globale (insbesondere asiatische) Inflationsdynamik. Dies unterstreicht die Sensibilität gegenüber sowohl persistentem Preisdruck als auch möglichen externen Dis-/Reflationsimpulsen.
*   **Rohstoffe & Globale Nachfrage:**
    *   Keine direkten Rohstoffpreisindikatoren, aber `XLE_63M_ret` (Energie Sektor) und `BAS.DE_126M_ret` (BASF, Chemie/Industrie) dienen als hochkorrelierte Proxies für globale Rohstoffpreise, Energiekosten und industrielle Aktivität. Dies erfasst indirekt auch Wechselkurs- und Handelsflüsseffekte.

**2. Sektor- & Marktdynamik:**

*   **Zyklische Sensitivität:**
    *   `BAS.DE_126M_ret` (Globale Chemie/Industrie) und `XLE_63M_ret` (Energie): Hohe Gewichte indizieren, dass die globale Industrieproduktion, Energiepreise und die damit verbundene globale Konjunktur der primäre Treiber sind. Langfristige Momentum-Signale bei BASF reflektieren strukturelle Verschiebungen im globalen Produktionszyklus.
*   **Finanzielle Stabilität & Wachstum:**
    *   `JPM_126M_ret` (Finanzsektor) und `VNQ_126M_ret` (Immobilien-ETF): Diese Sektoren sind hochgradig zins- und kreditzyklussensitiv. Ihr langfristiges Momentum signalisiert die zugrundeliegende Gesundheit des Finanzsystems, die Kreditvergabe und die Kapitalflüsse in Real Assets – entscheidend für die Bewertung zukünftigen Wachstums.
*   **Defensive Positionierung:**
    *   `XLU_126M_ret` (Versorger-ETF): Als typisch defensiver Sektor mit Anleihenproxy-Charakteristik zeigt dessen langfristiges Momentum die nachhaltige Nachfrage nach stabilen Erträgen ("Search for Yield") oder eine Risikoaversion im Markt, stark beeinflusst von langfristigen Kapitalkosten.
*   **Konjunkturzyklus-Phase:**
    *   Die gewichtete Mischung aus hochzyklischen (BAS.DE, XLE, JPM) und defensiven/zinskritischen (VNQ, XLU) Sektoren deutet darauf hin, dass das Modell nicht nur eine klare "Risk-On/Off"-Dichotomie abbildet, sondern vielmehr die Übergänge und spezifischen Phasen des Konjunkturzyklus, in denen diese Interdependenzen die Marktentwicklung bestimmen.

**3. Quant-Konklusion:**

*   **Übergreifendes Narrativ:** Die 6-Monats-Prognose für den SPY wird primär durch die Interaktion zwischen der globalen industriellen Aktivität, der Persistenz der Inflation (US & global) und der Resilienz des Finanzsystems sowie der Real Asset-Märkte, die alle durch das langfristige Zinsumfeld beeinflusst werden, bestimmt.
*   **SPY-Treiber:** Das Marktverhalten des SPY hängt entscheidend davon ab, ob die globale Industriekonjunktur (BAS.DE, XLE) nachhaltig ist, ohne dabei einen übermäßigen und anhaltenden Inflationsdruck (CPIs) zu erzeugen. Gleichzeitig ist die Reaktion des Finanzsektors (JPM) und der zinsnahen Sektoren (VNQ, XLU) auf das vorherrschende Zinsumfeld (`^IRX`) von zentraler Bedeutung.
*   **Fokus der Vorhersage:** Das Modell legt nahe, dass langfristige, fundamentale Verschiebungen in der globalen Industrieproduktion, der Kapitalkostenstruktur und den Inflationserwartungen aktuell die dominantesten Kräfte für die breite Marktrichtung darstellen.

## Mathematische Modellparameter

- **Intercepts:** `[-0.1901016810217164, -1.1434904923813307, 1.3335921734030538]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.66025341 -0.19598424  0.58810019  0.57412932  0.14134134 -0.06955292
   0.34950297  0.33562962]
 [-0.1476206   0.33832519 -0.23339135 -0.16978238  0.18590692  0.14773149
   0.0646217  -0.12582563]
 [ 0.80787402 -0.14234095 -0.35470884 -0.40434694 -0.32724826 -0.07817857
  -0.41412468 -0.20980399]]
  ```
