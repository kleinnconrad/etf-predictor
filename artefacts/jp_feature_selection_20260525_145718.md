# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-25 14:58:41
- **Target ETF:** DBXJ.DE
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2025-11-17** prognostiziert das Modell:

> **Klasse:** Up
>
> **Wahrscheinlichkeiten:** Down: 0.01% | Flat: 1.21% | Up: 98.78%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| UNRATE_126M_ret | 1.314602 |
| 9984.T_126M_ret | 0.953317 |
| PAYEMS_126M_ret | 0.778128 |
| DX-Y.NYB_63M_ret | 0.534824 |
| XLV_126M_ret | 0.384055 |
| 9984.T_63M_ret | 0.303325 |
| CL=F_126M_ret | 0.262397 |
| LRHUTTTTEZM156S_63M_ret | 0.254367 |
| DBXJ.DE_63M_ret | 0.244790 |
| XLE_126M_ret | 0.191927 |
| ^IRX_21M_ret | 0.109462 |
| ZW=F_63M_ret | 0.075946 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`AAPL_126M_ret, AZN.L_126M_ret, BNDX_21M_ret, BNDX_63M_ret, BTC-USD_21M_ret, BTC-USD_63M_ret, BTC-USD_126M_ret, BWX_21M_ret, BWX_63M_ret, BWX_126M_ret, CL=F_63M_ret, DX-Y.NYB_21M_ret, DX-Y.NYB_126M_ret, EEM_63M_ret, EEM_126M_ret, GC=F_21M_ret, GC=F_63M_ret, GC=F_126M_ret, HG=F_63M_ret, HG=F_126M_ret, HYG_63M_ret, HYG_126M_ret, IGOV_21M_ret, IGOV_63M_ret, IGOV_126M_ret, LQD_21M_ret, LQD_63M_ret, LQD_126M_ret, RIO.L_63M_ret, RIO.L_126M_ret, SHEL.L_63M_ret, SHEL.L_126M_ret, SIE.DE_126M_ret, TLT_21M_ret, TLT_63M_ret, VNQ_126M_ret, XBI_126M_ret, XLE_21M_ret, XLE_63M_ret, XLU_126M_ret, ZW=F_126M_ret, ^GDAXI_126M_ret, ^IRX_63M_ret, ^IRX_126M_ret, ^TNX_21M_ret, ^TNX_63M_ret, ^TNX_126M_ret, CPIAUCSL_63M_ret, CPIAUCSL_126M_ret, PAYEMS_63M_ret, UNRATE_21M_ret, UNRATE_63M_ret, T10Y2Y_126M_ret, CP00MI15EA20M086NEST_126M_ret, LRHUTTTTEZM156S_21M_ret, LRHUTTTTEZM156S_126M_ret, PRINTO01EZQ661S_63M_ret, PRINTO01EZQ661S_126M_ret, JPNCPIALLMINMEI_63M_ret, JPNCPIALLMINMEI_126M_ret, LRHUTTTTJPM156S_126M_ret, LRHUTTTTGBM156S_21M_ret, LRHUTTTTGBM156S_63M_ret, LRHUTTTTGBM156S_126M_ret, ratio_credit_spread_21M_ret, ratio_credit_spread_63M_ret, ratio_intl_vs_us_bonds_63M_ret, ratio_intl_vs_us_bonds_126M_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>112</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21M_ret, 7203.T_63M_ret, 7203.T_126M_ret, 8035.T_21M_ret, 8035.T_63M_ret, 8035.T_126M_ret, 9984.T_21M_ret, AAPL_21M_ret, AAPL_63M_ret, AZN.L_21M_ret, AZN.L_63M_ret, BAS.DE_21M_ret, BAS.DE_63M_ret, BAS.DE_126M_ret, BNDX_126M_ret, BRK-B_21M_ret, BRK-B_63M_ret, BRK-B_126M_ret, CL=F_21M_ret, DBXJ.DE_21M_ret, DBXJ.DE_126M_ret, EEM_21M_ret, HG=F_21M_ret, HYG_21M_ret, JPM_21M_ret, JPM_63M_ret, JPM_126M_ret, LE=F_21M_ret, LE=F_63M_ret, LE=F_126M_ret, MSFT_21M_ret, MSFT_63M_ret, MSFT_126M_ret, NVDA_21M_ret, NVDA_63M_ret, NVDA_126M_ret, RIO.L_21M_ret, SAP.DE_21M_ret, SAP.DE_63M_ret, SAP.DE_126M_ret, SHEL.L_21M_ret, SIE.DE_21M_ret, SIE.DE_63M_ret, TLT_126M_ret, VNQ_21M_ret, VNQ_63M_ret, XBI_21M_ret, XBI_63M_ret, XLF_21M_ret, XLF_63M_ret, XLF_126M_ret, XLK_21M_ret, XLK_63M_ret, XLK_126M_ret, XLP_21M_ret, XLP_63M_ret, XLP_126M_ret, XLU_21M_ret, XLU_63M_ret, XLV_21M_ret, XLV_63M_ret, XLY_21M_ret, XLY_63M_ret, XLY_126M_ret, ZC=F_21M_ret, ZC=F_63M_ret, ZC=F_126M_ret, ZW=F_21M_ret, ^GDAXI_21M_ret, ^GDAXI_63M_ret, ^N225_21M_ret, ^N225_63M_ret, ^N225_126M_ret, ^VIX_21M_ret, ^VIX_63M_ret, ^VIX_126M_ret, CPIAUCSL_21M_ret, PAYEMS_21M_ret, T10Y2Y_21M_ret, T10Y2Y_63M_ret, WALCL_21M_ret, WALCL_63M_ret, WALCL_126M_ret, CP00MI15EA20M086NEST_21M_ret, CP00MI15EA20M086NEST_63M_ret, ECBASSETS_21M_ret, ECBASSETS_63M_ret, ECBASSETS_126M_ret, PRINTO01EZQ661S_21M_ret, JPNCPIALLMINMEI_21M_ret, LRHUTTTTJPM156S_21M_ret, LRHUTTTTJPM156S_63M_ret, JPNASSETS_21M_ret, JPNASSETS_63M_ret, JPNASSETS_126M_ret, JPNPROINDMISMEI_21M_ret, JPNPROINDMISMEI_63M_ret, JPNPROINDMISMEI_126M_ret, GBRCPIALLMINMEI_21M_ret, GBRCPIALLMINMEI_63M_ret, GBRCPIALLMINMEI_126M_ret, GBRPROINDMISMEI_21M_ret, GBRPROINDMISMEI_63M_ret, GBRPROINDMISMEI_126M_ret, ratio_copper_gold_21M_ret, ratio_copper_gold_63M_ret, ratio_copper_gold_126M_ret, ratio_credit_spread_126M_ret, ratio_consumer_risk_21M_ret, ratio_consumer_risk_63M_ret, ratio_consumer_risk_126M_ret, ratio_intl_vs_us_bonds_21M_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makrooekonomisches Setup:**

*   **US-Arbeitsmarkt als Primärtreiber:** Dominanz von UNRATE\_126M\_ret und PAYEMS\_126M\_ret zeigt extreme Sensitivität japanischer Aktien (DBXJ.DE) gegenüber der **langfristigen Wachstumsdynamik und strukturellen Gesundheit des US-Arbeitsmarktes**. Robuste US-Beschäftigungssituation korreliert positiv mit globaler Nachfrage und Exporten.
*   **USD-Stärke & Wechselkursdynamik:** DX-Y.NYB\_63M\_ret unterstreicht die Relevanz einer **mittelfristig starken US-Dollar-Position**. Ein tendenziell starker USD (impliziert schwächeren JPY) verbessert die Wettbewerbsfähigkeit japanischer Exportunternehmen und stützt deren Gewinnmargen.
*   **Globale Inflations- & Rohstoffzyklen:** CL=F\_126M\_ret (Öl) und XLE\_126M\_ret (US-Energie-Sektor) signalisieren die Bedeutung **langfristiger Rohstoffpreistrends und der Energie-Sektor-Performance**. Diese reflektieren globale Nachfrage, Inflationserwartungen und geopolitische Risiken, welche Japans Handelsbilanz und Industriekosten beeinflussen. ZW=F\_63M\_ret (Weizen) ergänzt dies als breiteres Signal für globale Nahrungsmittelinflation oder Lieferketten-Störungen.
*   **US-Geldpolitik & Zinsausblick:** ^IRX\_21M\_ret (kurzfristige US-Staatsanleiherenditen) indiziert, dass die **kurz- bis mittelfristigen Impulse der US-Geldpolitik** und damit die Kosten des globalen Kapitals ein wesentlicher Prädiktor sind. Steigende Renditen signalisieren tendenziell eine Straffung und können die Risikoappetit beeinflussen.
*   **Europäische Konjunktur:** LRHUTTTTEZM156S\_63M\_ret (Eurozone Arbeitslosigkeit) verdeutlicht die **Interkonnektivität der globalen Wirtschaftszentren**. Eine Verbesserung der europäischen Arbeitsmärkte deutet auf eine stärkere Nachfrage aus der Eurozone hin, die Japans Exportwirtschaft indirekt unterstützt.
*   **Ignorierte Faktoren:** Das Fehlen direkter japanischer Zinsindikatoren oder der US-Zinsstrukturkurve suggeriert, dass die Modell-Signale sich stärker auf die **Fundamentaldaten der Realwirtschaft (insbesondere USA)** und **relative Währungsstärke** konzentrieren als auf die Feintuning von Zinsdifferenzialen oder Inversionen für diesen spezifischen Horizont.

**2. Sektor- & Marktdynamik:**

*   **Global Tech & Risikobereitschaft:** 9984.T\_126M\_ret und 9984.T\_63M\_ret (SoftBank Group) sind hochgewichtet. Dies verweist auf die signifikante Korrelation zwischen der **lang- und mittelfristigen Performance globaler Technologie- und Risikokapitalmärkte** (repräsentiert durch SoftBank) und der Entwicklung des breiten japanischen Aktienmarktes. Es signalisiert, dass DBXJ.DE stark vom globalen Innovationszyklus und der Investitionsbereitschaft in zukunftsgerichtete Sektoren profitiert.
*   **Defensiv- & Zykliker-Mix:** XLV\_126M\_ret (US-Gesundheitssektor) und XLE\_126M\_ret (US-Energiesektor) im Modell zeigen eine simultane Sensibilität gegenüber **langfristigen defensiven Anlagemustern** (Gesundheit, als Stabilitätsanker oder Innovationsfokus) sowie **zyklischen Wachstumserwartungen und Inflationssignalen** (Energie). Dies deutet auf eine Auswertung von Sektor-Rotationen über lange Zeiträume hin, die auf das globale Konjunkturklima für Japan schliessen lassen.
*   **Momentum-Persistenz:** DBXJ.DE\_63M\_ret, das eigene Momentum des ETFs, ist ein direkter **Trendfolge-Indikator**. Es bestätigt, dass etablierte mittelfristige Trends im japanischen Aktienmarkt eine hohe Prädiktionskraft für die zukünftige Performance besitzen.

**3. Quant-Konklusion:**

*   **Primäres Narrativ:** DBXJ.DE ist eine **leverageierte Wette auf die anhaltende strukturelle Stärke und das Wachstum der US-Wirtschaft**, insbesondere im Hinblick auf den Arbeitsmarkt und die relative Stärke des US-Dollars.
*   **Sekundäre Treiber:** Die Entwicklung von DBXJ.DE wird massgeblich durch die **globale Risikobereitschaft und Kapitalflüsse in Technologie- und Wachstumsunternehmen** (SoftBank) beeinflusst, was Japans Integration in globale Innovationsökosysteme unterstreicht.
*   **Makro- & Marktintegration:** Das Modell verbindet **langfristige makroökonomische Trends** (US-Arbeitsmarkt, Rohstoffe, Währungen) mit **mittelfristigen Sektor- und Markt-Momentum-Signalen**, um ein robustes Vorhersagemodell für japanische Aktien zu erstellen.
*   **Risikofaktoren:** Eine Abkühlung des US-Arbeitsmarktes, eine signifikante Schwächung des USD oder eine sustained globale Risikovermeidung, insbesondere im Tech-Sektor, würden als **signifikante Abwärtsrisiken** für DBXJ.DE in den nächsten 6 Monaten wirken.

## Mathematische Modellparameter

- **Intercepts:** `[-0.35256796604177476, -0.7093534487455492, 1.0619214147872937]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.45498808 -1.42997538 -0.2552093   0.30724736  0.69300225  0.1726094
   0.52307911  0.11391885  0.05840184 -1.16719168 -1.97190332 -0.3815499 ]
 [-0.07143587  0.23745313  0.39359517  0.05993759  0.10923442 -0.2878907
   0.05300397 -0.10486253 -0.16419273  0.98663537  0.94516586  0.19563924]
 [-0.38355221  1.19252226 -0.13838587 -0.36718495 -0.80223667  0.1152813
  -0.57608308 -0.00905632  0.10579089  0.18055631  1.02673746  0.18591067]]
  ```
