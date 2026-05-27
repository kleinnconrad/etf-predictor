# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-25 14:52:23
- **Target ETF:** EL4A.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2025-11-18** prognostiziert das Modell:

> **Klasse:** Up
>
> **Wahrscheinlichkeiten:** Down: 13.29% | Flat: 5.83% | Up: 80.89%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| LRHUTTTTEZM156S_126M_ret | 0.737753 |
| MSFT_63M_ret | 0.312637 |
| MSFT_21M_ret | 0.191020 |
| BRK-B_126M_ret | 0.171207 |
| BNDX_21M_ret | 0.170505 |
| AZN.L_126M_ret | 0.147761 |
| LRHUTTTTEZM156S_63M_ret | 0.147075 |
| LRHUTTTTEZM156S_21M_ret | 0.117198 |
| BNDX_63M_ret | 0.109937 |
| ECBASSETS_21M_ret | 0.096668 |
| AZN.L_21M_ret | 0.089750 |
| 9984.T_63M_ret | 0.081009 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`7203.T_63M_ret, 7203.T_126M_ret, 8035.T_126M_ret, 9984.T_126M_ret, AAPL_21M_ret, AAPL_63M_ret, AAPL_126M_ret, AZN.L_63M_ret, BWX_21M_ret, BWX_63M_ret, CL=F_21M_ret, CL=F_63M_ret, CL=F_126M_ret, DX-Y.NYB_21M_ret, DX-Y.NYB_63M_ret, EEM_63M_ret, GC=F_63M_ret, HG=F_63M_ret, HG=F_126M_ret, HYG_63M_ret, IGOV_21M_ret, IGOV_63M_ret, LQD_21M_ret, LQD_63M_ret, MSFT_126M_ret, NVDA_21M_ret, SAP.DE_63M_ret, SAP.DE_126M_ret, SHEL.L_21M_ret, SHEL.L_63M_ret, SHEL.L_126M_ret, SIE.DE_126M_ret, VNQ_126M_ret, XBI_63M_ret, XBI_126M_ret, XLE_63M_ret, XLE_126M_ret, XLK_21M_ret, XLV_21M_ret, XLV_63M_ret, XLV_126M_ret, ZW=F_21M_ret, ZW=F_63M_ret, ZW=F_126M_ret, ^IRX_21M_ret, ^IRX_63M_ret, ^IRX_126M_ret, ^TNX_21M_ret, CPIAUCSL_21M_ret, CPIAUCSL_63M_ret, CPIAUCSL_126M_ret, PAYEMS_21M_ret, PAYEMS_63M_ret, PAYEMS_126M_ret, UNRATE_21M_ret, UNRATE_63M_ret, UNRATE_126M_ret, PRINTO01EZQ661S_63M_ret, PRINTO01EZQ661S_126M_ret, JPNCPIALLMINMEI_21M_ret, JPNCPIALLMINMEI_63M_ret, JPNCPIALLMINMEI_126M_ret, LRHUTTTTJPM156S_126M_ret, LRHUTTTTGBM156S_21M_ret, LRHUTTTTGBM156S_63M_ret, LRHUTTTTGBM156S_126M_ret, ratio_intl_vs_us_bonds_63M_ret, ratio_intl_vs_us_bonds_126M_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>112</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21M_ret, 8035.T_21M_ret, 8035.T_63M_ret, 9984.T_21M_ret, BAS.DE_21M_ret, BAS.DE_63M_ret, BAS.DE_126M_ret, BNDX_126M_ret, BRK-B_21M_ret, BRK-B_63M_ret, BTC-USD_21M_ret, BTC-USD_63M_ret, BTC-USD_126M_ret, BWX_126M_ret, DX-Y.NYB_126M_ret, EEM_21M_ret, EEM_126M_ret, EL4A.DE_21M_ret, EL4A.DE_63M_ret, EL4A.DE_126M_ret, GC=F_21M_ret, GC=F_126M_ret, HG=F_21M_ret, HYG_21M_ret, HYG_126M_ret, IGOV_126M_ret, JPM_21M_ret, JPM_63M_ret, JPM_126M_ret, LE=F_21M_ret, LE=F_63M_ret, LE=F_126M_ret, LQD_126M_ret, NVDA_63M_ret, NVDA_126M_ret, RIO.L_21M_ret, RIO.L_63M_ret, RIO.L_126M_ret, SAP.DE_21M_ret, SIE.DE_21M_ret, SIE.DE_63M_ret, TLT_21M_ret, TLT_63M_ret, TLT_126M_ret, VNQ_21M_ret, VNQ_63M_ret, XBI_21M_ret, XLE_21M_ret, XLF_21M_ret, XLF_63M_ret, XLF_126M_ret, XLK_63M_ret, XLK_126M_ret, XLP_21M_ret, XLP_63M_ret, XLP_126M_ret, XLU_21M_ret, XLU_63M_ret, XLU_126M_ret, XLY_21M_ret, XLY_63M_ret, XLY_126M_ret, ZC=F_21M_ret, ZC=F_63M_ret, ZC=F_126M_ret, ^GDAXI_21M_ret, ^GDAXI_63M_ret, ^GDAXI_126M_ret, ^N225_21M_ret, ^N225_63M_ret, ^N225_126M_ret, ^TNX_63M_ret, ^TNX_126M_ret, ^VIX_21M_ret, ^VIX_63M_ret, ^VIX_126M_ret, T10Y2Y_21M_ret, T10Y2Y_63M_ret, T10Y2Y_126M_ret, WALCL_21M_ret, WALCL_63M_ret, WALCL_126M_ret, CP00MI15EA20M086NEST_21M_ret, CP00MI15EA20M086NEST_63M_ret, CP00MI15EA20M086NEST_126M_ret, ECBASSETS_63M_ret, ECBASSETS_126M_ret, PRINTO01EZQ661S_21M_ret, LRHUTTTTJPM156S_21M_ret, LRHUTTTTJPM156S_63M_ret, JPNASSETS_21M_ret, JPNASSETS_63M_ret, JPNASSETS_126M_ret, JPNPROINDMISMEI_21M_ret, JPNPROINDMISMEI_63M_ret, JPNPROINDMISMEI_126M_ret, GBRCPIALLMINMEI_21M_ret, GBRCPIALLMINMEI_63M_ret, GBRCPIALLMINMEI_126M_ret, GBRPROINDMISMEI_21M_ret, GBRPROINDMISMEI_63M_ret, GBRPROINDMISMEI_126M_ret, ratio_copper_gold_21M_ret, ratio_copper_gold_63M_ret, ratio_copper_gold_126M_ret, ratio_credit_spread_21M_ret, ratio_credit_spread_63M_ret, ratio_credit_spread_126M_ret, ratio_consumer_risk_21M_ret, ratio_consumer_risk_63M_ret, ratio_consumer_risk_126M_ret, ratio_intl_vs_us_bonds_21M_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makroökonomisches Setup:**
*   **EZB-Liquiditätsdominanz:** Die hochgewichtete Präsenz von EZB-Liquiditätsmetriken (LRHUTTTTEZM156S – MRO Allotments; ECBASSETS – Bilanzsumme) über multiple Zeithorizonte (21M-126M) indiziert, dass die primäre treibende Kraft für EL4A.DE die **persistente Bereitstellung und Inanspruchnahme von Zentralbankliquidität** im Euroraum ist. Positives Momentum hier deutet auf ein anhaltend akkommodierendes Umfeld oder strukturell hohen Liquiditätsbedarf hin.
*   **Globale Zins- und Kapitalflussdynamik:** Das Momentum in globalen Ex-US-Anleihen (BNDX) signalisiert die Relevanz **internationaler Zinsdifferenziale und globaler Kapitalflüsse** als sekundären, aber signifikanten Faktor. Es deutet auf eine Abstimmung der globalen Anleihemärkte oder eine Verlagerung der Risikopräferenz hin.
*   **Ignoranz von Rohstoffen/Währungen:** Die explizite Nicht-Selektion direkter Rohstoff- oder Währungsindikatoren impliziert, dass deren Einfluss für EL4A.DE auf 6-Monats-Sicht als nachrangig bewertet wird oder bereits in den vorselektierten Finanzmarktmetriken internalisiert ist.

**2. Sektor- & Marktdynamik:**
*   **Tech-Wachstum als Führungsindikator:** Starkes Momentum globaler Technologie-Blue-Chips (MSFT_63M_ret, MSFT_21M_ret) indiziert anhaltende **Risikobereitschaft und Präferenz für den Wachstumssektor**, welche als Treiber für breitere Equity-Märkte wirken.
*   **Diversifiziertes Value-Vertrauen:** Die Aufnahme von Berkshire Hathaway (BRK-B_126M_ret) mit langjährigem Momentum reflektiert **langfristiges Vertrauen in fundamentale, breit aufgestellte Value-Sektoren** und die Stabilität der Gesamtwirtschaft.
*   **Resiliente Sektoren mit Wachstumspotenzial:** Momentum in AstraZeneca (AZN.L_126M_ret, AZN.L_21M_ret) verweist auf die fortgesetzte Attraktivität von **defensiven Sektoren mit säkularen Wachstumstreibern** (z.B. Healthcare), welche auch in risikofreudigeren Phasen beibehalten wird.
*   **Risikofreudigkeit im High-Beta-Tech:** SoftBank (9984.T_63M_ret) als Indikator für globale Venture Capital und hochbewertete Tech-Investitionen unterstreicht eine **robuste globale Risikobereitschaft und Liquidität**, die spekulative Assets und damit indirekt auch breitere Equity-Märkte stützt.

**3. Quant-Konklusion:**
*   **EZB-Liquidität als Katalysator:** Das übergeordnete Narrativ für EL4A.DE über die nächsten 6 Monate ist ein **durch anhaltende EZB-Liquiditätszufuhr getragenes Marktumfeld**.
*   **Risikobereitschaft & Wachstumsorientierung:** Die starke Korrelation mit globalen Wachstums- und Tech-Sektoren (MSFT, SoftBank) sowie die Absicherung durch Value (BRK-B) und defensive (AZN.L) Sektoren signalisiert eine **breit abgestützte Risikobereitschaft mit Fokus auf Wachstumsbereiche**.
*   **Tendenziell positives Umfeld:** Die spezifische Indikatorenkombination impliziert eine **tendenzielle Aufwärtsbewegung für deutsche Mid-Caps**, gestützt durch günstige Liquiditätsbedingungen und eine Präferenz für globale Risiko-Assets.

## Mathematische Modellparameter

- **Intercepts:** `[0.09254333397643807, -1.0742638223620105, 0.9817204883855846]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.09305664  0.025217    0.21627554 -0.19607809 -0.09422215  0.01929859
   0.03478042  0.46895611  0.12137737 -0.03474862 -1.10662913  0.01385056]
 [ 0.12151353  0.10940769  0.0053667  -0.05968008 -0.0706827   0.23751253
   0.25175009 -0.08139958 -0.17579643  0.22061272  0.22971194  0.13115088]
 [-0.02845689 -0.13462469 -0.22164224  0.25575817  0.16490485 -0.25681112
  -0.28653051 -0.38755653  0.05441906 -0.1858641   0.87691719 -0.14500145]]
  ```
