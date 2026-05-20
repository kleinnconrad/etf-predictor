# 📈 ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-20 12:17:18
- **Target ETF:** SPY
- **Forecast Horizon:** 126 Trading Days

## 🚀 Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-19** prognostiziert das Modell:

> **Klasse:** Up 🟢
>
> **Wahrscheinlichkeiten:** Down: 31.53% | Flat: 5.13% | Up: 63.34%

---

## 🎯 Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| 9984.T_6M | 0.473802 |
| AAPL_3M | 0.336194 |
| SAP.DE_3M | 0.233382 |
| SHEL.L_6M | 0.229335 |
| AAPL_1M | 0.122061 |
| GC=F_6M | 0.074420 |
| XBI_6M | 0.072574 |
| AZN.L_3M | 0.071036 |

## 🗑️ Aussortierte Prädiktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
> *Diese Variablen hatten anfängliche Relevanz, boten dem Modell in Kombination mit den Top-Prädiktoren aber keinen ausreichenden Informationszugewinn mehr (Multikollinearität).* 

`8035.T_1M, 9984.T_1M, BAS.DE_1M, BRK-B_1M, CL=F_1M, DX-Y.NYB_1M, EEM_1M, GC=F_1M, HG=F_1M, JPM_1M, NVDA_1M, RIO.L_1M, SAP.DE_1M, SHEL.L_1M, SPY_1M, XBI_1M, XLE_1M, ^GDAXI_1M, ^IRX_1M, ^N225_1M, ^TNX_1M, ^VIX_1M, 7203.T_3M, 8035.T_3M, 9984.T_3M, BAS.DE_3M, BRK-B_3M, CL=F_3M, DX-Y.NYB_3M, EEM_3M, GC=F_3M, HG=F_3M, JPM_3M, MSFT_3M, NVDA_3M, RIO.L_3M, SHEL.L_3M, SIE.DE_3M, SPY_3M, XBI_3M, XLE_3M, XLF_3M, XLK_3M, ^GDAXI_3M, ^IRX_3M, ^N225_3M, ^TNX_3M, ^VIX_3M, 7203.T_6M, 8035.T_6M, AAPL_6M, AZN.L_6M, BAS.DE_6M, BRK-B_6M, CL=F_6M, DX-Y.NYB_6M, EEM_6M, HG=F_6M, JPM_6M, MSFT_6M, NVDA_6M, RIO.L_6M, SAP.DE_6M, SIE.DE_6M, SPY_6M, XLE_6M, XLF_6M, XLK_6M, ^GDAXI_6M, ^IRX_6M, ^N225_6M, ^TNX_6M`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>7</b> in Stufe 1 aussortierten Variablen anzuzeigen (Geringste Signifikanz)</summary>

`7203.T_1M, AZN.L_1M, MSFT_1M, SIE.DE_1M, XLF_1M, XLK_1M, ^VIX_6M`

</details>

---

## 🤖 KI-Interpretation der Prädiktoren (Hedgefonds Analyst)

**1. Makroökonomisches Setup:**

*   **Zins- & Währungsindikatoren:** Explizite Zins- oder Währungspaare wurden *nicht* direkt selektiert. Dies deutet darauf hin, dass die Modellarchitektur die impliziten Auswirkungen von Geldpolitik und relativer Währungsstärke primär über die Discountfaktoren und Cashflow-Bewertungen der selektierten Aktien (insbesondere Wachstums- und Technologieaktien) erfasst, anstatt direkte Zins-Spreads oder FX-Volatilität als führend zu identifizieren.
*   **Rohstoffe:** Die Selektion von `SHEL.L_6M` unterstreicht die anhaltende Relevanz von Energierohstoffpreisen als Indikator für globale Industrienachfrage und Inflationstrends. `GC=F_6M` als Gold-Future-Momentum signalisiert persistente Risikowahrnehmungen, Inflationserwartungen oder eine Flucht in Sicherheit in einem mittel- bis langfristigen Horizont. Die gemeinsame Präsenz signalisiert eine Notwendigkeit zur Korrelation von Rohstoffpreisdynamik und Breitenmarkt-Risikoperzeption.

**2. Sektor- & Marktdynamik:**

*   **Dominanz der globalen Tech-Riesen (9984.T, AAPL, SAP.DE):** Die hohe Gewichtung von SoftBank (Tech-Venture Capital/Asien), Apple (Konsumtechnologie/Global) und SAP (Enterprise Software/Europa) signalisiert eine entscheidende Abhängigkeit des SPY-Ausblicks von globaler Technologie-Adoption, Unternehmensinvestitionen in Digitalisierung und Konsumlaune. Dies deutet auf eine späte zyklische Wachstumsphase oder einen Technologieführungsmarkt hin, in dem Innovation und Digitalisierung die Treiber sind.
*   **Zyklische vs. Defensive Balance:** Die Präsenz von `SHEL.L_6M` (Energie/Rohstoffzyklus) neben `XBI_6M` (hochbeta Biopharma, risikobereites Wachstum) sowie `AZN.L_3M` (defensive Pharma) und `GC=F_6M` (Safe Haven) indiziert ein Marktregime, das sowohl Wachstumschancen (Tech, Biotech) als auch fundamentale Risikofaktoren (Inflation, Geopolitik, defensiver Sektor) über verschiedene Zeithorizonte aktiv monitort. Die Sektor-Rotation ist fragmentiert, zeigt aber eine Tendenz zur Wachstumsorientierung, die durch fundamentale Sensitivitäten unterlegt ist.
*   **Geografische Diversifizierung:** Die breite geografische Streuung (Japan, USA, Deutschland, UK) der führenden Equity-Indikatoren bestätigt eine tiefe globale Marktintegration, bei der regionale Entwicklungen und Sektor-Performance außerhalb der USA signifikant auf den US-Breitenmarkt wirken.

**3. Quant-Konklusion:**

*   **SPY-Ausblick (6M):** Der SPY-Ausblick wird primär durch die *Momentum-Performance globaler Technologieführer* (SoftBank, Apple, SAP) bestimmt, was auf eine Fortsetzung des strukturellen Wachstums und eine hohe Risikobereitschaft im Tech-Sektor hindeutet.
*   **Subtile Risikosteuerung:** Eine sekundäre, aber substanzielle Rolle spielen Rohstoffpreise (SHEL) für Inflationserwartungen und Safe-Haven-Assets (GC=F) sowie defensive Sektoren (AZN.L) für die Risikobereitschaft. Dies impliziert, dass das positive Tech-Narrativ durch persistente makroökonomische Unsicherheiten (Inflation, Zinsen, Geopolitik) moderiert wird, die ein potenzielles Downside-Risiko darstellen.
*   **Marktcharakterisierung:** Der Markt ist in den nächsten 6 Monaten durch eine Kombination aus *Tech-led Growth Optimism* und einer *diskreten, aber konstanten Vigilanz gegenüber makroökonomischen "Tail-Risiken"* gekennzeichnet, welche über Rohstoffmärkte und traditionelle Safe-Haven-Assets signalisiert werden.

## Mathematische Modellparameter

- **Intercepts:** `[-0.08668891609152833, -1.5708409703966066, 1.6575298864881338]`

- **Koeffizienten-Matrix:**
  ```text
[[ 0.16190333  0.47287942  0.08380908 -0.19488734 -0.63759673 -0.04406737
   0.29264159 -0.09244559]
 [ 0.02118795  0.03141228  0.02274425 -0.15518541 -0.07310679 -0.06756288
   0.05136124 -0.01641559]
 [-0.18309129 -0.5042917  -0.10655333  0.35007275  0.71070353  0.11163025
  -0.34400283  0.10886118]]
  ```
