# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-21 06:40:33
- **Target ETF:** SPY
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-20** prognostiziert das Modell:

> **Klasse:** Up 🟢
>
> **Wahrscheinlichkeiten:** Down: 8.24% | Flat: 4.79% | Up: 86.96%

---

## Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| BAS.DE_6M | 0.563911 |
| VNQ_6M | 0.469806 |
| BAS.DE_3M | 0.388259 |
| ^IRX_6M | 0.362718 |
| XBI_3M | 0.307989 |
| LE=F_1M | 0.223963 |
| XLU_1M | 0.132425 |
| EEM_1M | 0.099385 |

## Aussortierte Prädiktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* 

`AAPL_1M, BAS.DE_1M, BTC-USD_1M, DX-Y.NYB_1M, GC=F_1M, HG=F_1M, LQD_1M, TLT_1M, XBI_1M, XLE_1M, XLP_1M, ZC=F_1M, ZW=F_1M, ^TNX_1M, 8035.T_3M, 9984.T_3M, AAPL_3M, AZN.L_3M, BTC-USD_3M, DX-Y.NYB_3M, EEM_3M, GC=F_3M, HG=F_3M, HYG_3M, JPM_3M, LQD_3M, MSFT_3M, NVDA_3M, RIO.L_3M, SAP.DE_3M, SHEL.L_3M, SIE.DE_3M, TLT_3M, VNQ_3M, XLE_3M, XLP_3M, XLU_3M, XLV_3M, ZW=F_3M, ^GDAXI_3M, ^IRX_3M, ^TNX_3M, 8035.T_6M, 9984.T_6M, AAPL_6M, AZN.L_6M, BTC-USD_6M, CL=F_6M, DX-Y.NYB_6M, EEM_6M, GC=F_6M, HG=F_6M, HYG_6M, JPM_6M, LE=F_6M, LQD_6M, MSFT_6M, NVDA_6M, RIO.L_6M, SAP.DE_6M, SHEL.L_6M, SIE.DE_6M, XBI_6M, XLE_6M, XLF_6M, XLK_6M, XLP_6M, XLU_6M, XLV_6M, ZW=F_6M, ^GDAXI_6M, ^N225_6M`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>43</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>

`7203.T_1M, 8035.T_1M, 9984.T_1M, AZN.L_1M, BRK-B_1M, CL=F_1M, HYG_1M, JPM_1M, MSFT_1M, NVDA_1M, RIO.L_1M, SAP.DE_1M, SHEL.L_1M, SIE.DE_1M, SPY_1M, VNQ_1M, XLF_1M, XLK_1M, XLV_1M, XLY_1M, ^GDAXI_1M, ^IRX_1M, ^N225_1M, ^VIX_1M, 7203.T_3M, BRK-B_3M, CL=F_3M, LE=F_3M, SPY_3M, XLF_3M, XLK_3M, XLY_3M, ZC=F_3M, ^N225_3M, ^VIX_3M, 7203.T_6M, BRK-B_6M, SPY_6M, TLT_6M, XLY_6M, ZC=F_6M, ^TNX_6M, ^VIX_6M`

</details>

---

## KI-Interpretation der Prädiktoren (Hedgefonds Analyst)

**1. Makroökonomisches Setup:**

*   **Zinsstruktur (Short-Term):** Die hohe Gewichtung von `^IRX_6M` (13-Wochen T-Bill Rendite) signalisiert eine *dominante Abhängigkeit des SPY von kurzfristigen Zins- und Liquiditätserwartungen*. Der 6-Monats-Momentum-Fokus deutet auf die Relevanz persistent geänderter Fed-Politik-Projektionen für die Diskontierung von Cashflows und Kapitalkosten.
*   **Währungen:** Die *Ignoranz expliziter Währungs-Prädiktoren* impliziert, dass deren Einfluss entweder bereits in den globalen Equity- und Rohstoffpreisen diskontiert oder für den 6-Monats-Horizont als sekundär gegenüber Zinserwartungen und sektorspezifischer Dynamik erachtet wird.
*   **Rohstoffe (Spezifisch):** `LE=F_1M` (Live Cattle Futures) deutet auf eine *feingranulare Berücksichtigung von Konsumentenpreisinflation und Agrarlieferketten-Druck*. Das 1-Monats-Momentum signalisiert hier taktische, kurzfristige Verschiebungen in Kostenfaktoren, welche die Konsumkraft und somit die Gesamtwirtschaft beeinflussen können. Die *Abwesenheit breiterer Industrie- oder Energierohstoffe* legt nahe, dass der direkte Einfluss dieser Sektoren als weniger prägnant bewertet wird als die zugrundeliegende industrielle Aktivität selbst (ref. BAS.DE).
*   **Globaler Fokus:** Die signifikante Präsenz von `BAS.DE` (Deutsches Industrie-Schwergewicht) unterstreicht eine *ausgeprägte Sensitivität des SPY gegenüber globalen Industriezyklen und internationalem Handelssentiment*, was auf eine starke Verknüpfung der US-Marktentwicklung mit der globalen Wirtschaftsdynamik hindeutet.

**2. Sektor- & Marktdynamik:**

*   **Zyklische Frühindikatoren (Industrie):** `BAS.DE_6M` und `BAS.DE_3M` als Top-Prädiktoren heben die *hohe Korrelation des SPY mit globaler Industrieproduktion und zyklischer Nachfrage* hervor. Ein anhaltendes Momentum in diesem Sektor ist entscheidend für die Bewertung der globalen Wachstumsaussichten und deren Spillover-Effekte auf den SPY.
*   **Zinssensitivität & Stabilität (Real Estate):** `VNQ_6M` (US REITs) unterstreicht die *Anfälligkeit des Gesamtmarktes für Zinsänderungen, Inflationserwartungen und die Stabilität des Immobilienmarktes*. Ein positives Momentum in REITs kann auf eine solide Wirtschaft oder eine Flucht in Sachwerte/Dividenden hindeuten, während negatives Momentum auf steigende Zinsen oder konjunkturelle Eintrübung verweist.
*   **Risikobereitschaft & Innovation (Biotech):** `XBI_3M` (Biotech) reflektiert die *Abhängigkeit von der Markt-Risikobereitschaft und der Finanzierung von Wachstumssektoren*. Biotech fungiert als Hochbeta-Sektor und Frühindikator für die Spekulationsfreude und das Vertrauen in langfristiges Wachstum, mit dem 3-Monats-Momentum als Indikator für kurzfristige Stimmungswechsel.
*   **Defensive Positionierung (Versorger):** Die Einbeziehung von `XLU_1M` (Versorger) mit kürzerem Momentum weist auf *taktische Shifts in defensive Sektoren* hin. Dies deutet auf eine Berücksichtigung von Phasen erhöhter Unsicherheit oder der Suche nach stabilen Cashflows, was eine potenzielle Rotation aus risikoreicheren Anlagen signalisiert.
*   **Globales Risiko & EM-Flows:** `EEM_1M` (Emerging Markets) signalisiert die Relevanz des *globalen Risikoklimas und der internationalen Kapitalflüsse*. EM-Aktien gelten als Barometer für globales Wachstum und Risikobereitschaft; ihr 1-Monats-Momentum kann kurzfristige globale Liquiditätsverschiebungen oder Änderungen der Risikopräferenzen anzeigen, die indirekt den SPY beeinflussen.

**3. Quant-Konklusion:**

*   **Übergeordnetes Narrativ:** Die Modellstruktur legt nahe, dass die SPY-Performance über 6 Monate maßgeblich durch eine *Verbindung aus globalen Industriezyklen, US-Zinserwartungen und einem dynamischen Zusammenspiel von Risikoappetit und Defensiv-Positionierung* bestimmt wird.
*   **Aktuelle Implikation:** Die hohe Gewichtung zyklischer (BAS.DE) und zinssensitiver (VNQ) Indikatoren auf längerer Sicht, kombiniert mit agileren Risikosignalen (XBI, XLU, EEM) auf kürzerer Sicht, deutet darauf hin, dass der Markt *eine kritische Phase der Konjunkturentwicklung durchläuft*. Die Stärke oder Schwäche dieser Leitsignale wird den Trend des SPY maßgeblich definieren.
*   **SPY Ausblick:** Ein *sustained positives Momentum in globaler Industrie (`BAS.DE`) und stabilen Real Estate-Sektoren (`VNQ`), gestützt durch moderate Zinsentwicklungen (`^IRX`) und anhaltende Risikobereitschaft (`XBI`)*, indiziert eine Tendenz zum "Up"-Marktzustand. Eine Erosion dieser Fundamente, einhergehend mit einer Zunahme defensiver Allokationen (`XLU`), würde hingegen auf "Down" oder "Flat" für den SPY hindeuten. Das Modell ist somit extrem sensitiv für die *zyklische Positionierung im aktuellen makroökonomischen Regime*.

## Mathematische Modellparameter

- **Intercepts:** `[-0.027213548306592363, -1.3026589635471826, 1.329872511853787]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.14907706  0.33594404  0.19863794  0.58238882 -0.35777906 -0.84586723
   0.64170065  0.25247596]
 [ 0.09727303 -0.27820133 -0.18682375 -0.4802834   0.46198354  0.2884597
   0.06300806  0.29160174]
 [ 0.05180404 -0.05774271 -0.01181419 -0.10210542 -0.10420448  0.55740753
  -0.70470871 -0.5440777 ]]
  ```
