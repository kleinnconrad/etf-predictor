# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-21 06:54:36
- **Target ETF:** CSINDU.SW
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-20** prognostiziert das Modell:

> **Klasse:** Up 🟢
>
> **Wahrscheinlichkeiten:** Down: 42.45% | Flat: 5.84% | Up: 51.71%

---

## Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| VNQ_6M | 0.501012 |
| ^GDAXI_6M | 0.311072 |
| ^TNX_3M | 0.171144 |
| JPM_1M | 0.152891 |
| LE=F_1M | 0.135264 |
| VNQ_1M | 0.122872 |
| SIE.DE_6M | 0.045848 |
| ^IRX_1M | 0.040538 |

## Aussortierte Prädiktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* 

`9984.T_1M, AAPL_1M, BRK-B_1M, BTC-USD_1M, CSINDU.SW_1M, DX-Y.NYB_1M, LQD_1M, TLT_1M, XBI_1M, XLE_1M, XLF_1M, XLP_1M, XLU_1M, XLV_1M, XLY_1M, ZC=F_1M, ZW=F_1M, ^TNX_1M, 8035.T_3M, 9984.T_3M, AAPL_3M, AZN.L_3M, BRK-B_3M, BTC-USD_3M, CL=F_3M, CSINDU.SW_3M, DX-Y.NYB_3M, EEM_3M, GC=F_3M, HG=F_3M, HYG_3M, LE=F_3M, LQD_3M, RIO.L_3M, SHEL.L_3M, VNQ_3M, XBI_3M, XLE_3M, XLP_3M, XLU_3M, XLV_3M, XLY_3M, ZC=F_3M, ZW=F_3M, ^IRX_3M, ^VIX_3M, 7203.T_6M, 8035.T_6M, 9984.T_6M, AAPL_6M, AZN.L_6M, BAS.DE_6M, BTC-USD_6M, CL=F_6M, DX-Y.NYB_6M, EEM_6M, HG=F_6M, JPM_6M, NVDA_6M, RIO.L_6M, SHEL.L_6M, TLT_6M, XBI_6M, XLE_6M, XLP_6M, XLU_6M, XLV_6M, XLY_6M, ZW=F_6M, ^IRX_6M, ^N225_6M, ^TNX_6M`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>43</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>

`7203.T_1M, 8035.T_1M, AZN.L_1M, BAS.DE_1M, CL=F_1M, EEM_1M, GC=F_1M, HG=F_1M, HYG_1M, MSFT_1M, NVDA_1M, RIO.L_1M, SAP.DE_1M, SHEL.L_1M, SIE.DE_1M, XLK_1M, ^GDAXI_1M, ^N225_1M, ^VIX_1M, 7203.T_3M, BAS.DE_3M, JPM_3M, MSFT_3M, NVDA_3M, SAP.DE_3M, SIE.DE_3M, TLT_3M, XLF_3M, XLK_3M, ^GDAXI_3M, ^N225_3M, BRK-B_6M, CSINDU.SW_6M, GC=F_6M, HYG_6M, LE=F_6M, LQD_6M, MSFT_6M, SAP.DE_6M, XLF_6M, XLK_6M, ZC=F_6M, ^VIX_6M`

</details>

---

## KI-Interpretation der Prädiktoren (Hedgefonds Analyst)

Hier ist die ökonomische Einschätzung Ihres Modells:

**1. Makroökonomisches Setup:**

*   **Zinsen als Primärtreiber:** Die Auswahl von ^TNX_3M und ^IRX_1M unterstreicht die Sensitivität des CSINDU.SW gegenüber globalen Zinsänderungserwartungen und Liquiditätsbedingungen. Die *Momentum*-Faktoren signalisieren, dass sich *Veränderungen* in der Zinsstrukturkurve – insbesondere kurzfristige Anpassungen an die Geldpolitik und mittelfristige Erwartungen an Wachstum/Inflation – als führend erweisen.
*   **Fehlende Währungen:** Das explizite Fehlen von Währungspaaren deutet darauf hin, dass Zinsdifferenziale, Rohstofftrends und globale Sektorrotationen die Kapitalflüsse nach Indien über den 6-Monats-Horizont hinreichend erklären, ohne dass direkte FX-Signale eine zusätzliche, *führende* Rolle spielen. Globale Risikoprämien und Asset-Allokationsentscheidungen dominieren Währungstrends.
*   **Commodity-Momentum als Inflationssignal:** LE=F_1M (Live Cattle Futures) fungiert als kurzfristiger Indikator für Rohstoffpreise, möglicherweise als Proxy für globale Konsumgüterinflation oder Angebots-Schocks. Dieses kurzfristige Momentum reflektiert unmittelbare Inflationserwartungen oder Nachfrageverschiebungen, die über Leitzinserwartungen indirekt auf EM-Märkte wirken.

**2. Sektor- & Marktdynamik:**

*   **US Real Estate (VNQ) als Risikobarometer:** Die dominante Rolle von VNQ_6M und VNQ_1M betont die hohe Korrelation des CSINDU.SW mit der globalen Risikobereitschaft und Zins-Sensitivität. Starke US-Immobilienmärkte signalisieren tendenziell ein "Risk-on"-Umfeld mit Kapitalsuche nach Rendite, während eine Schwäche auf steigende Zinsen, Rezessionsängste und breite Risikoaversion hindeutet, was EM-Abflüsse verstärkt.
*   **Globale Konjunktur via DAX & Siemens:** ^GDAXI_6M und SIE.DE_6M (Deutscher Industriewert) spiegeln die Gesundheit der exportorientierten europäischen Wirtschaft und globalen Industrieproduktion wider. Ihre Momentum-Signale indizieren somit die weltweite zyklische Stärke, die für eine offene Volkswirtschaft wie Indien entscheidend ist (Nachfrage nach indischen Exporten, globale Lieferketten).
*   **Finanzsektor als Kreditindikator:** JPM_1M dient als kurzfristiger Barometer für die Gesundheit des US-Finanzsektors und die globale Kreditverfügbarkeit. Ein positives Momentum signalisiert stabile Kreditmärkte und eine verbesserte Profitabilität, was ein förderliches Umfeld für globale Kapitalmärkte und EM-Zuflüsse darstellt.

**3. Quant-Konklusion:**

*   **Global-Macro Dominanz:** Das Modell postuliert eine überwältigende Abhängigkeit des CSINDU.SW von globalen Makro- und Sektortrends, insbesondere aus den USA und Europa, anstatt rein inländischer indischer Faktoren über den 6-Monats-Horizont.
*   **Zins- und Risikoprämien-Fokus:** Das übergeordnete Narrativ ist, dass die indische Marktentwicklung maßgeblich durch die Neukalibrierung globaler Zins- und Inflationserwartungen (getrieben durch US-Zinsen und globale Rohstoffe) und die daraus resultierende Verschiebung der globalen Risikoprämien (reflektiert in US-REITs und DM-Equities) bestimmt wird.
*   **Konjunkturzyklus-Sensitivität:** Die Mischung aus zinssensiblen (VNQ), zyklischen (GDAXI, SIE.DE) und finanzsektorspezifischen (JPM) Indikatoren deutet darauf hin, dass das Modell sowohl die aktuelle Position im globalen Konjunkturzyklus als auch die Dynamik des Übergangs zu neuen Phasen als kritisch für Indien erachtet.

## Mathematische Modellparameter

- **Intercepts:** `[0.12419867384509144, -1.2561701870854087, 1.1319715132403296]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.04896833  0.18662351 -0.16479885  0.06080719  0.208387    0.01531766
   0.48035587 -0.46660855]
 [ 0.22933624  0.01627257  0.18430726 -0.00151834 -0.2567158  -0.06877216
   0.27116247  0.02309483]
 [-0.18036791 -0.20289609 -0.01950841 -0.05928885  0.0483288   0.05345449
  -0.75151834  0.44351372]]
  ```
