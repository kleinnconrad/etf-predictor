# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-21 07:04:26
- **Target ETF:** EL4A.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-20** prognostiziert das Modell:

> **Klasse:** Down 🔴
>
> **Wahrscheinlichkeiten:** Down: 55.71% | Flat: 9.61% | Up: 34.67%

---

## Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| ZW=F_6M | 0.236071 |
| XLV_6M | 0.149951 |
| XLF_3M | 0.125190 |
| ^TNX_1M | 0.123362 |
| XLV_1M | 0.118430 |
| XLE_1M | 0.106837 |
| CL=F_1M | 0.101380 |
| BAS.DE_3M | 0.064024 |

## Aussortierte Prädiktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* 

`7203.T_1M, 8035.T_1M, 9984.T_1M, AAPL_1M, AZN.L_1M, DX-Y.NYB_1M, GC=F_1M, HG=F_1M, LQD_1M, MSFT_1M, NVDA_1M, SHEL.L_1M, TLT_1M, XLK_1M, ZW=F_1M, ^IRX_1M, ^N225_1M, 7203.T_3M, 9984.T_3M, AAPL_3M, AZN.L_3M, BRK-B_3M, BTC-USD_3M, CL=F_3M, DX-Y.NYB_3M, EEM_3M, EL4A.DE_3M, GC=F_3M, HG=F_3M, HYG_3M, JPM_3M, LQD_3M, MSFT_3M, RIO.L_3M, SAP.DE_3M, SHEL.L_3M, SIE.DE_3M, XBI_3M, XLE_3M, XLK_3M, XLU_3M, XLV_3M, ZW=F_3M, ^GDAXI_3M, ^IRX_3M, 7203.T_6M, 8035.T_6M, 9984.T_6M, AAPL_6M, AZN.L_6M, BAS.DE_6M, BRK-B_6M, CL=F_6M, EEM_6M, EL4A.DE_6M, HG=F_6M, HYG_6M, LE=F_6M, MSFT_6M, RIO.L_6M, SAP.DE_6M, SHEL.L_6M, SIE.DE_6M, TLT_6M, VNQ_6M, XBI_6M, XLE_6M, XLK_6M, ZC=F_6M, ^GDAXI_6M, ^IRX_6M, ^VIX_6M`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>43</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>

`BAS.DE_1M, BRK-B_1M, BTC-USD_1M, EEM_1M, EL4A.DE_1M, HYG_1M, JPM_1M, LE=F_1M, RIO.L_1M, SAP.DE_1M, SIE.DE_1M, VNQ_1M, XBI_1M, XLF_1M, XLP_1M, XLU_1M, XLY_1M, ZC=F_1M, ^GDAXI_1M, ^VIX_1M, 8035.T_3M, LE=F_3M, NVDA_3M, TLT_3M, VNQ_3M, XLP_3M, XLY_3M, ZC=F_3M, ^N225_3M, ^TNX_3M, ^VIX_3M, BTC-USD_6M, DX-Y.NYB_6M, GC=F_6M, JPM_6M, LQD_6M, NVDA_6M, XLF_6M, XLP_6M, XLU_6M, XLY_6M, ^N225_6M, ^TNX_6M`

</details>

---

## KI-Interpretation der Prädiktoren (Hedgefonds Analyst)

**1. Makroökonomisches Setup:**

*   **Zinsstrukturkurven-Dominanz:** Die hohe Gewichtung von ZW=F_6M (kurzfristige Zinsfutures, z.B. 2-jährige T-Notes) und ^TNX_1M (10-jährige T-Note-Rendite) signalisiert eine primäre Steuerung des Marktzustands durch die Form und Dynamik der US-Zinsstrukturkurve, die Erwartungen an die Geldpolitik und die langfristigen Wachstums-/Inflationsaussichten.
*   **Rohstoffpreis-Inflationsdruck:** CL=F_1M (Rohöl-Futures) verankert das Modell in der kurzfristigen globalen Rohstoffpreisinflation und deren direkten Auswirkungen auf Unternehmensmargen, Konsumkraft und das Risiko von Zinskontraktion.
*   **Währungs-Neutralität:** Das Fehlen direkter Währungsindikatoren deutet darauf hin, dass deren Einfluss als nicht vorlaufend oder bereits in Zinsdifferenzialen und Rohstoffpreisen des Modells enthalten eingestuft wird.

**2. Sektor- & Marktdynamik:**

*   **Defensive Kernpositionierung:** Die hohe Gewichtung von XLV_6M und XLV_1M (US Health Care Sektor-ETF) indiziert eine anhaltende präventive Neigung zu defensiven Sektoren, was auf ein spätes Konjunkturzyklus-Stadium oder erhöhte Risikoaversion im Markt hinweist.
*   **Zyklische Wachstumsimpulse:** XLF_3M (US Financials Sektor-ETF) reagiert sensitiv auf Wachstumserwartungen und die Zinskurvensteilheit; XLE_1M (US Energy Sektor-ETF) spiegelt globale Nachfrage und Rohstoffpreisdynamik wider. BAS.DE_3M (BASF) dient als Proxy für die europäische/globale Industrieproduktion und Chemiezyklik.
*   **Rotationsdynamik:** Die Kombination aus langfristiger defensiver Stärke (XLV_6M) und kurzfristiger zyklischer Reaktivität (XLF_3M, XLE_1M, BAS.DE_3M) deutet auf eine Marktphase hin, in der Sektorrotationen und deren Momentum-Signale essenziell für die Vorhersage von Marktregime-Wechseln sind.

**3. Quant-Konklusion:**

*   **Policy-Driven Regime:** Das dominante Narrativ für EL4A.DE (über die nächsten 6 Monate) ist eine extreme Sensitivität gegenüber den globalen Zinspolitik-Erwartungen und der daraus resultierenden Diskontierungsraten für zukünftige Cashflows von Unternehmen.
*   **Growth vs. Risk-Off Trade-Off:** Das Modell reflektiert die kontinuierliche Neubewertung globaler Wachstumsaussichten und potenzieller Inflations-/Rezessionsrisiken, die sich in der relativen Performance zyklischer gegenüber defensiver Sektoren widerspiegelt.
*   **Yield Curve als führender Indikator:** Die Zinsstrukturkurve, durch ihre kurz- und langfristigen Momentum-Komponenten, agiert als primärer Indikator für das übergeordnete Marktregime, während sektorale Umschichtungen die Nuancen der aktuellen Konjunkturphase offenbaren und kritische Wendepunkte signalisieren.

## Mathematische Modellparameter

- **Intercepts:** `[0.35612315528180877, -1.198737235312443, 0.8426140800306287]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.00673286  0.10407317  0.06004372  0.18504364 -0.0631738  -0.18778493
   0.20984513  0.28151259]
 [ 0.14533776 -0.160255    0.11760132 -0.16152161  0.09603674  0.03647335
  -0.22492709  0.07259319]
 [-0.15207062  0.05618182 -0.17764504 -0.02352204 -0.03286294  0.15131158
   0.01508196 -0.35410578]]
  ```
