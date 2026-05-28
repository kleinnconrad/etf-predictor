# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-28 13:32:11
- **Target ETF:** DBXJ.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-27** prognostiziert das Modell:

> **Klasse:** Down
>
> **Wahrscheinlichkeiten:** Down: 34.75% | Flat: 17.50% | Up: 47.76%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| DX-Y.NYB_126D_ret | 0.624937 |
| JPNCPIALLMINMEI_126D_ret | 0.496564 |
| VNQ_126D_ret | 0.484449 |
| ZW=F_126D_ret | 0.480351 |
| ratio_credit_spread_21D_ret | 0.343594 |
| ^TNX_21D_ret | 0.246268 |
| ^IRX_63D_ret | 0.238022 |
| CL=F_126D_ret | 0.205088 |
| LRHUTTTTGBM156S_21D_ret | 0.177956 |
| BTC-USD_126D_ret | 0.173894 |
| LRHUTTTTJPM156S_21D_ret | 0.125630 |
| LE=F_21D_ret | 0.095902 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`9984.T_126D_ret, AZN.L_126D_ret, BNDX_21D_ret, BNDX_63D_ret, BRK-B_126D_ret, BTC-USD_21D_ret, BTC-USD_63D_ret, BWX_21D_ret, BWX_63D_ret, BWX_126D_ret, CL=F_63D_ret, DBXJ.DE_63D_ret, DX-Y.NYB_21D_ret, DX-Y.NYB_63D_ret, EEM_63D_ret, EEM_126D_ret, GC=F_21D_ret, GC=F_63D_ret, GC=F_126D_ret, HG=F_63D_ret, HG=F_126D_ret, HYG_63D_ret, IGOV_21D_ret, IGOV_63D_ret, IGOV_126D_ret, LE=F_63D_ret, LQD_21D_ret, LQD_63D_ret, LQD_126D_ret, RIO.L_63D_ret, RIO.L_126D_ret, SHEL.L_63D_ret, SHEL.L_126D_ret, TLT_21D_ret, TLT_63D_ret, XBI_126D_ret, XLE_63D_ret, XLE_126D_ret, XLU_126D_ret, ZW=F_63D_ret, ^GDAXI_126D_ret, ^IRX_126D_ret, ^TNX_63D_ret, ^TNX_126D_ret, CPIAUCSL_63D_ret, CPIAUCSL_126D_ret, PAYEMS_63D_ret, PAYEMS_126D_ret, UNRATE_63D_ret, UNRATE_126D_ret, T10Y2Y_126D_ret, WALCL_126D_ret, CP00MI15EA20M086NEST_126D_ret, LRHUTTTTEZM156S_21D_ret, LRHUTTTTEZM156S_63D_ret, LRHUTTTTEZM156S_126D_ret, PRINTO01EZQ661S_63D_ret, PRINTO01EZQ661S_126D_ret, LRHUTTTTJPM156S_63D_ret, LRHUTTTTJPM156S_126D_ret, LRHUTTTTGBM156S_63D_ret, LRHUTTTTGBM156S_126D_ret, ratio_copper_gold_126D_ret, ratio_credit_spread_63D_ret, ratio_risk_on_off_21D_ret, ratio_tech_dominance_126D_ret, ratio_intl_vs_us_bonds_63D_ret, ratio_intl_vs_us_bonds_126D_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>121</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21D_ret, 7203.T_63D_ret, 7203.T_126D_ret, 8035.T_21D_ret, 8035.T_63D_ret, 8035.T_126D_ret, 9984.T_21D_ret, 9984.T_63D_ret, AAPL_21D_ret, AAPL_63D_ret, AAPL_126D_ret, AZN.L_21D_ret, AZN.L_63D_ret, BAS.DE_21D_ret, BAS.DE_63D_ret, BAS.DE_126D_ret, BNDX_126D_ret, BRK-B_21D_ret, BRK-B_63D_ret, CL=F_21D_ret, DBXJ.DE_21D_ret, DBXJ.DE_126D_ret, EEM_21D_ret, HG=F_21D_ret, HYG_21D_ret, HYG_126D_ret, JPM_21D_ret, JPM_63D_ret, JPM_126D_ret, LE=F_126D_ret, MSFT_21D_ret, MSFT_63D_ret, MSFT_126D_ret, NVDA_21D_ret, NVDA_63D_ret, NVDA_126D_ret, RIO.L_21D_ret, SAP.DE_21D_ret, SAP.DE_63D_ret, SAP.DE_126D_ret, SHEL.L_21D_ret, SIE.DE_21D_ret, SIE.DE_63D_ret, SIE.DE_126D_ret, SPY_21D_ret, SPY_63D_ret, SPY_126D_ret, TLT_126D_ret, VNQ_21D_ret, VNQ_63D_ret, XBI_21D_ret, XBI_63D_ret, XLE_21D_ret, XLF_21D_ret, XLF_63D_ret, XLF_126D_ret, XLK_21D_ret, XLK_63D_ret, XLK_126D_ret, XLP_21D_ret, XLP_63D_ret, XLP_126D_ret, XLU_21D_ret, XLU_63D_ret, XLV_21D_ret, XLV_63D_ret, XLV_126D_ret, XLY_21D_ret, XLY_63D_ret, XLY_126D_ret, ZC=F_21D_ret, ZC=F_63D_ret, ZC=F_126D_ret, ZW=F_21D_ret, ^GDAXI_21D_ret, ^GDAXI_63D_ret, ^IRX_21D_ret, ^N225_21D_ret, ^N225_63D_ret, ^N225_126D_ret, ^VIX_21D_ret, ^VIX_63D_ret, ^VIX_126D_ret, CPIAUCSL_21D_ret, PAYEMS_21D_ret, UNRATE_21D_ret, T10Y2Y_21D_ret, T10Y2Y_63D_ret, WALCL_21D_ret, WALCL_63D_ret, CP00MI15EA20M086NEST_21D_ret, CP00MI15EA20M086NEST_63D_ret, ECBASSETS_21D_ret, ECBASSETS_63D_ret, ECBASSETS_126D_ret, PRINTO01EZQ661S_21D_ret, JPNCPIALLMINMEI_21D_ret, JPNCPIALLMINMEI_63D_ret, JPNASSETS_21D_ret, JPNASSETS_63D_ret, JPNASSETS_126D_ret, JPNPROINDMISMEI_21D_ret, JPNPROINDMISMEI_63D_ret, JPNPROINDMISMEI_126D_ret, GBRCPIALLMINMEI_21D_ret, GBRCPIALLMINMEI_63D_ret, GBRCPIALLMINMEI_126D_ret, GBRPROINDMISMEI_21D_ret, GBRPROINDMISMEI_63D_ret, GBRPROINDMISMEI_126D_ret, ratio_copper_gold_21D_ret, ratio_copper_gold_63D_ret, ratio_credit_spread_126D_ret, ratio_consumer_risk_21D_ret, ratio_consumer_risk_63D_ret, ratio_consumer_risk_126D_ret, ratio_risk_on_off_63D_ret, ratio_risk_on_off_126D_ret, ratio_tech_dominance_21D_ret, ratio_tech_dominance_63D_ret, ratio_intl_vs_us_bonds_21D_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

> *Fehler bei der LLM-Abfrage: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}*

## Mathematische Modellparameter

- **Intercepts:** `[-0.3388874215212274, -0.10127065212437675, 0.44015807364560194]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.03081473 -0.15894561  0.93740532  0.1329958   0.66315977  0.72052579
   0.13975907 -0.02035953  0.54833162 -0.13925823  0.05664369  0.51539026]
 [ 0.23002659 -0.14868686 -0.01491549  0.01085774  0.06351408 -0.08439629
   0.21727456  0.3694025   0.19651403 -0.04918712  0.21029105 -0.24456896]
 [-0.26084132  0.30763247 -0.92248984 -0.14385355 -0.72667385 -0.6361295
  -0.35703363 -0.34904297 -0.74484565  0.18844535 -0.26693474 -0.2708213 ]]
  ```
