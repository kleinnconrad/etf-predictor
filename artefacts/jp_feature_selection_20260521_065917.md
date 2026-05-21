# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-21 07:00:15
- **Target ETF:** DBXJ.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-20** prognostiziert das Modell:

> **Klasse:** Down 🔴
>
> **Wahrscheinlichkeiten:** Down: 80.33% | Flat: 4.95% | Up: 14.72%

---

## Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| ZW=F_6M | 0.411227 |
| ^IRX_3M | 0.244753 |
| ^GDAXI_6M | 0.241238 |
| VNQ_6M | 0.207839 |
| NVDA_3M | 0.199812 |
| XLV_6M | 0.110986 |
| SIE.DE_6M | 0.072678 |
| CL=F_3M | 0.055054 |

## Aussortierte Prädiktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* 

`AAPL_1M, AZN.L_1M, BRK-B_1M, BTC-USD_1M, DBXJ.DE_1M, DX-Y.NYB_1M, GC=F_1M, LE=F_1M, LQD_1M, NVDA_1M, SHEL.L_1M, TLT_1M, XLE_1M, XLP_1M, XLU_1M, XLV_1M, ZC=F_1M, ZW=F_1M, ^TNX_1M, 7203.T_3M, 9984.T_3M, AAPL_3M, AZN.L_3M, BAS.DE_3M, BTC-USD_3M, DBXJ.DE_3M, DX-Y.NYB_3M, EEM_3M, GC=F_3M, HG=F_3M, HYG_3M, LE=F_3M, LQD_3M, RIO.L_3M, SHEL.L_3M, TLT_3M, XLE_3M, XLP_3M, XLU_3M, XLV_3M, ZW=F_3M, ^GDAXI_3M, ^TNX_3M, ^VIX_3M, 7203.T_6M, 9984.T_6M, AAPL_6M, AZN.L_6M, BRK-B_6M, BTC-USD_6M, CL=F_6M, DBXJ.DE_6M, DX-Y.NYB_6M, EEM_6M, GC=F_6M, HG=F_6M, HYG_6M, LQD_6M, NVDA_6M, RIO.L_6M, SAP.DE_6M, SHEL.L_6M, TLT_6M, XBI_6M, XLE_6M, XLF_6M, XLK_6M, XLP_6M, XLU_6M, ZC=F_6M, ^IRX_6M, ^TNX_6M`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>43</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>

`7203.T_1M, 8035.T_1M, 9984.T_1M, BAS.DE_1M, CL=F_1M, EEM_1M, HG=F_1M, HYG_1M, JPM_1M, MSFT_1M, RIO.L_1M, SAP.DE_1M, SIE.DE_1M, VNQ_1M, XBI_1M, XLF_1M, XLK_1M, XLY_1M, ^GDAXI_1M, ^IRX_1M, ^N225_1M, ^VIX_1M, 8035.T_3M, BRK-B_3M, JPM_3M, MSFT_3M, SAP.DE_3M, SIE.DE_3M, VNQ_3M, XBI_3M, XLF_3M, XLK_3M, XLY_3M, ZC=F_3M, ^N225_3M, 8035.T_6M, BAS.DE_6M, JPM_6M, LE=F_6M, MSFT_6M, XLY_6M, ^N225_6M, ^VIX_6M`

</details>

---

## KI-Interpretation der Prädiktoren (Hedgefonds Analyst)

**1. Makroökonomisches Setup:**

*   **ZW=F_6M (Wheat Futures Momentum):** Dominanter Prädiktor. Spiegelt globale Lebensmittel-Rohstoffdynamik wider. Für Japan als Nettoimporteur signalisiert starkes Momentum (steigende Preise) entweder globale Inflationsrisiken (Kosten-Push, schwächt Binnenkonsum) oder robuste globale Nachfrage, die Rohstoffpreise treibt und gleichzeitig exportstarke Ökonomien wie Japan stützt. Die hohe Gewichtung deutet auf eine kritische Sensitivität des japanischen Marktes gegenüber diesen primären Inflations- und/oder globalen Nachfragesignalen hin.
*   **^IRX_3M (US 13-Week Treasury Bill Yield Momentum):** Reflektiert die kurzfristigen US-Zinserwartungen und globale Liquiditätsdynamik. Positives Momentum (steigende Zinsen) indiziert eine Straffung der US-Geldpolitik, potenziell Kapitalabflüsse aus Schwellenländern und erhöhte Diskontierungsfaktoren, was sich global negativ auf Risikowerte, inklusive Japan, auswirken kann.
*   **CL=F_3M (Crude Oil Futures Momentum):** Zeigt globale Energiepreisentwicklung. Als Nettoölimporteur ist Japan anfällig für steigende Rohölpreise, die sich in höheren Importkosten, Inflation und Belastung für Konsum und Margen niederschlagen können. Das geringere Gewicht relativ zu Weizen suggeriert, dass spezifische Energiepreis-Schocks sekundär sind oder bereits in breiteren Rohstoff- oder Makro-Indikatoren erfasst werden.
*   **Implikationen:** Das Modell priorisiert spezifische Rohstoff-Inflationssignale (Lebensmittel, Energie) und die Entwicklung der US-Kurzfristzinsen. Dies deutet auf die extreme Empfindlichkeit Japans gegenüber globalen Kostenstrukturen und der globalen Kapitalkostenentwicklung hin. Eine direkte JPY/USD-FX-Komponente fehlt, wird jedoch indirekt über Zinsdifferenziale und globale Risikostimmung beeinflusst.

**2. Sektor- & Marktdynamik:**

*   **^GDAXI_6M (DAX Momentum):** Starker Prädiktor. Repräsentiert die globale Risikobereitschaft und die Wirtschaftsdynamik in Industrienationen, insbesondere Europa. Ein positives Momentum signalisiert robuste Exportaussichten und Vertrauen in zyklische Märkte, was Japan als exportorientierter Nation zugutekommt.
*   **NVDA_3M (NVIDIA Momentum):** Schlüsselindikator für globale Technologie- und Halbleiterzyklen sowie Wachstumserwartungen. Positives Momentum deutet auf starke Investitionen in Tech-Infrastruktur und KI hin, was die Nachfrage nach japanischen High-Tech-Produkten und Komponenten antreibt und globale Wachstumsmärkte stärkt.
*   **SIE.DE_6M (Siemens Momentum):** Indikator für globale Industrieproduktion und Investitionsgüternachfrage. Das Momentum signalisiert die Gesundheit des globalen Investitionszyklus und der Kapitalgüterindustrie, was für Japans starkes Industrieproduktions- und Exportprofil direkt relevant ist.
*   **VNQ_6M (US Real Estate ETF Momentum):** Reflektiert die Sensitivität des US-Immobilienmarktes gegenüber Zinsen und Wirtschaftswachstum. Positives Momentum könnte auf stabilere US-Zinsen (Langfristbereich), Inflationserwartungen oder eine robuste US-Wirtschaft hindeuten, deren Stabilität global positiv wahrgenommen wird.
*   **XLV_6M (US Healthcare ETF Momentum):** Sektorindikator, der sowohl defensive Qualitäten als auch Innovationszyklen im US-Gesundheitswesen abbildet. Sein moderater Einfluss kann eine Suche nach stabileren Wachstumspfaden oder bestimmte Innovationszyklen im Markt signalisieren, die breitere Zuflüsse beeinflussen.
*   **Implikationen:** Die Auswahl zyklischer, global ausgerichteter Sektoren (DAX, NVIDIA, Siemens) unterstreicht die starke Korrelation des DBXJ.DE mit dem globalen Konjunkturzyklus, insbesondere im Technologie- und Industriebereich. US-spezifische Sektordynamiken (VNQ, XLV) zeigen die Spillover-Effekte der weltweit größten Volkswirtschaft auf die globale Anlegerstimmung und Kapitalströme.

**3. Quant-Konklusion:**

*   **Globalzyklische Sensitivität:** Die aggregierte Prädiktoren-Struktur offenbart eine hohe Abhängigkeit des DBXJ.DE von der globalen Konjunktur, getrieben durch industrielle Aktivität, Technologieinvestitionen und die allgemeine Risikobereitschaft in entwickelten Märkten.
*   **Rohstoff-Inflations-Hebel:** Die herausragende Rolle von Weizen-Futures hebt die kritische, möglicherweise doppeldeutige, Wirkung globaler Lebensmittelpreise auf Japan hervor – entweder als Indikator für robuste globale Nachfrage oder als Belastung durch importierte Inflation. Dies ist ein prägnanter Schock- und/oder Wachstumsindikator für eine ressourcenarme Nation.
*   **US-Geldpolitik als Katalysator:** Die kurzfristige US-Zinsdynamik (^IRX) agiert als unmittelbarer Indikator für globale Liquiditätsbedingungen und Kapitalströme, der über Zinsdifferenziale und den "Risk-On/Risk-Off"-Modus schnell auf japanische Aktien durchschlägt.
*   **Übergeordnetes Narrativ:** Das Modell prognostiziert den Marktzustand des DBXJ.DE für die nächsten 6 Monate primär auf Basis der Interaktion zwischen **robuster globaler Wirtschaftsdynamik (Industrie & Tech), der Steuerung spezifischer Rohstoff-Inflationsrisiken und der Entwicklung der US-Geldpolitik**. Ein positiver Ausblick für DBXJ.DE erfordert eine Fortsetzung des globalen Konjunkturaufschwungs bei gleichzeitig beherrschbaren Inflationsdruck und einer nicht-restriktiven US-Geldpolitik.

## Mathematische Modellparameter

- **Intercepts:** `[0.26068989949199023, -0.9490037653001488, 0.6883138658081496]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.02152633  0.29971809  0.17769273 -0.0489209   0.3117586  -0.16647913
   0.61684099 -0.24774283]
 [ 0.08258147 -0.2470013   0.18943619  0.10901697 -0.0362288   0.13076972
  -0.23460846 -0.11411435]
 [-0.06105514 -0.05271679 -0.36712892 -0.06009606 -0.2755298   0.03570941
  -0.38223253  0.36185719]]
  ```
