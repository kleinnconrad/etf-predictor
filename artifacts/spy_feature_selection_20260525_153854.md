# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-25 15:40:08
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
| ratio_credit_spread_21M_ret | 0.194186 |
| ZW=F_63M_ret | 0.181935 |
| ratio_credit_spread_63M_ret | 0.169862 |
| VNQ_126M_ret | 0.148248 |
| ^IRX_21M_ret | 0.128777 |
| LRHUTTTTEZM156S_21M_ret | 0.110017 |
| ^TNX_21M_ret | 0.082427 |
| ^TNX_63M_ret | 0.072912 |
| ratio_risk_on_off_21M_ret | 0.049974 |

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

*   **Zinsstruktur & Finanzkonditionen:**
    *   **T10Y2Y_63M_ret (0.296560):** Höchster Einfluss. Signalisiert langfristige Trendverschiebungen in der Zinsstrukturkurve, einem prägnanten Indikator für Rezessionsrisiken und Wachstumserwartungen über mehrere Zyklen. Der 63M-Momentum-Faktor filtert zyklisches Rauschen und konzentriert sich auf strukturelle makroökonomische Regime.
    *   **ratio_credit_spread_21M_ret (0.194186) & _63M_ret (0.169862):** Reflektieren essenzielle Verschiebungen in der Marktliquidität, dem Unternehmensfinanzierungsumfeld und der systemischen Risikoaversion. Die Kombination verschiedener Momentum-Fenster (21M, 63M) detektiert sowohl zyklische als auch strukturelle Verschlechterungen/Verbesserungen der Kreditmärkte.
    *   **^IRX_21M_ret (0.128777) & ^TNX_21M_ret (0.082427), ^TNX_63M_ret (0.072912):** Betonen die Bedeutung von kurz- (Fed-Politik) und langfristigen (Inflations-/Wachstumserwartungen) Zinsentwicklungen. Die 21M/63M-Momentum-Fenster erfassen nachhaltige Richtungsänderungen der Geldpolitik und Diskontierungssätze.
*   **Globale Konjunktur & Inflation:**
    *   **ZW=F_63M_ret (0.181935):** Langfristige Weizenpreisdynamik als Proxy für globale Lebensmittelinflation, Lieferkettenstress und agrarwirtschaftliche Kapazitätsauslastung. Signifikant für die Cost-Push-Inflation und globale Kaufkraft.
    *   **LRHUTTTTEZM156S_21M_ret (0.110017):** Eurozone-Arbeitslosenquote. Indiziert die Relevanz der globalen Konjunkturstärke, insbesondere in einem Schlüsselwirtschaftsraum, für die SPY-Performance. Signale von globaler Nachfrage und Handel.
*   **Währungen/Sonstiges:** Direkte Währungsindikatoren wurden nicht ausgewählt, was darauf hindeutet, dass deren Informationsgehalt entweder geringer ist oder bereits über Zinsdifferenziale und globale makroökonomische Faktoren im Modell abgebildet wird.

**2. Sektor- & Marktdynamik:**

*   **Technologie & Marktkapitalisierung:**
    *   **AAPL_126M_ret (0.252018):** Zweithöchster Einfluss. Apple als globaler Tech-Megacap-Bellwether reflektiert langfristige Trends in Konsumausgaben, Innovationskraft und technologischem Wandel. Der 126M-Return erfasst die strukturelle Dominanz und das anhaltende Wachstum von Marktführern und ihre Implikationen für die Marktbreite.
*   **Zyklische Sektoren & Rohstoffe:**
    *   **XLE_63M_ret (0.198326):** Energie-Sektor. Verweist auf die Abhängigkeit des Marktes von Rohstoffpreisen, geopolitischen Risiken und dem globalen Konjunkturzyklus. Das 63M-Momentum zeigt strukturelle Energiepreisregime an (Inflation/Deflation, Angebots-/Nachfrageschock).
    *   **VNQ_126M_ret (0.148248):** REITs/Real Estate Sektor. Hochsensibel gegenüber Zinsänderungen, Inflationserwartungen und der Attraktivität von Real Assets. Das 126M-Momentum indiziert strukturelle Verschiebungen in der Allokation von Kapital und der zugrunde liegenden Wirtschaftsaktivität im Immobiliensektor.
*   **Risikobereitschaft:**
    *   **ratio_risk_on_off_21M_ret (0.049974):** Signalisiert die allgemeine Marktstimmung und Risikobereitschaft der Investoren über einen mittleren Horizont, ergänzend zu den primären Kreditspread-Indikatoren.

**3. Quant-Konklusion:**

*   **Makro-finanzielle Überlegenheit:** Das Modell gewichtet makro-finanzielle Faktoren (Zinskurve, Kreditspreads) sowie die langfristige Performance von Marktführern (AAPL) und zyklischen Sektoren (XLE, VNQ) am höchsten.
*   **Strukturelle Trend-Sensitivität:** Die durchweg langen Momentum-Fenster (21M, 63M, 126M) betonen, dass nachhaltige, strukturelle Trends in Zinssätzen, Kreditmärkten und Sektoren die Haupttreiber für den SPY über 6 Monate sind, nicht kurzfristige Schwankungen.
*   **Narrativ für SPY (6 Monate):** Die SPY-Richtung wird maßgeblich durch die **anhaltende Entwicklung der Zinskurve**, die **Gesundheit der Unternehmensbilanzen und Kreditmärkte** sowie die **strukturelle Stärke von Mega-Cap-Tech** und die **zyklische Dynamik von Rohstoff- und Immobilienmärkten** bestimmt. Das Modell projiziert eine Marktreaktion auf längerfristige, systemische Verschiebungen in der globalen Ökonomie und Finanzlandschaft, nicht auf volatile Ad-hoc-Ereignisse.

## Mathematische Modellparameter

- **Intercepts:** `[0.013037721973541624, -1.234302355716542, 1.2212646337430104]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.11868859  0.22237146  0.22184811  0.27290222  0.18007955 -0.12364096
  -0.07935817 -0.42087713 -0.13976905  0.291279    0.03541509  0.06164119]
 [ 0.25933836 -0.14427211  0.07564068 -0.23591435  0.01308565  0.05607061
   0.10936764 -0.02396344 -0.02525676 -0.20753723 -0.25479231  0.01331979]
 [-0.37802695 -0.07809935 -0.29748879 -0.03698787 -0.1931652   0.06757034
  -0.03000947  0.44484057  0.16502581 -0.08374177  0.21937722 -0.07496098]]
  ```
