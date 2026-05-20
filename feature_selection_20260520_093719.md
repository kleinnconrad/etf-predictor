# 📈 ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-20 09:37:51
- **Target ETF:** SPY
- **Forecast Horizon:** 126 Trading Days

## 🚀 Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2026-05-19** prognostiziert das Modell:

> **Klasse:** Up 🟢
>
> **Wahrscheinlichkeiten:** Down: 16.81% | Flat: 1.94% | Up: 81.25%

---

## Ausgewählte Prädiktoren (SFS)

| Prädiktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| AZN.L_6M | 0.337088 |
| 9984.T_6M | 0.282668 |
| RIO.L_6M | 0.203028 |
| ULVR.L_3M | 0.194091 |
| 9983.T_6M | 0.180315 |
| BP.L_6M | 0.179526 |
| 9432.T_6M | 0.133114 |
| META_1M | 0.078498 |

## 🤖 KI-Interpretation der Prädiktoren

Als quantitativer Finanzanalyst lässt sich die führende Rolle dieser Prädiktoren für den SPY durch ihre globale Diversifizierung, sektorale Sensitivität und ihren Status als Frühindikatoren für makroökonomische Trends und Kapitalflüsse erklären. Die Mehrheit der hier aufgeführten Unternehmen sind global agierende Großkonzerne aus Europa und Japan, die verschiedene Schlüsselsektoren abbilden. Ihre weitreichenden Lieferketten und Absatzmärkte machen sie zu Seismographen für weltwirtschaftliche Verschiebungen, die sich oft zuerst in internationalen Märkten manifestieren, bevor sie sich auf den stärker US-zentrierten SPY auswirken. Veränderungen in deren Geschäftsmodellen, Erwartungen und Aktienkursen signalisieren daher frühzeitig globale Nachfrage-, Angebots- und Stimmungsänderungen.

Insbesondere spiegeln diese Unternehmen kritische Aspekte der Weltwirtschaft wider. Prädiktoren wie RIO.L (Rohstoffe), BP.L (Energie) sind hochzyklisch und reagieren sensitiv auf globale Industrieproduktion und Rohstoffpreise – Indikatoren für zukünftige Inflation und Wirtschaftswachstum. ULVR.L und 9983.T (Konsumgüter) erfassen die Entwicklung der globalen Konsumausgaben und des Konsumentenvertrauens, während 9984.T (Technologie/Investitionen) und META (digitale Werbung) die globale Risikobereitschaft und Investitionsfreudigkeit widerspiegeln. AZN.L (Pharma) und 9432.T (Telekommunikation) hingegen sind oft defensiver und können Veränderungen in der Allokation von Kapital in sicherere Häfen oder längerfristige Infrastrukturtrends anzeigen. Die unterschiedlichen Lookback-Perioden (1M bis 6M) deuten zudem auf eine Mischung aus kurzfristiger Stimmungsanalyse (META) und längerfristigen strukturellen Trends hin.

Zusammenfassend signalisiert die Performance dieser Unternehmen eine Kombination aus realwirtschaftlicher Aktivität, Sektorstärken und globalen Kapitalflüssen. Wenn diese globalen Schwergewichte Anzeichen von Stärke oder Schwäche zeigen – sei es durch steigende Rohstoffnachfrage, veränderte Konsumtrends, sich wandelnde technologische Investitionen oder Verschiebungen in der globalen Risikobereitschaft – dient dies als „Canary in the Coal Mine“ für die allgemeine Marktstimmung und die Wirtschaftszyklen, die letztlich auch den SPY beeinflussen werden. Ihre kollektive Bewegung bietet somit einen wertvollen Einblick in die Entwicklung des globalen Investitionsklimas und der Fundamentaldaten, bevor diese sich umfassend in den US-Märkten widerspiegeln.

## Mathematische Modellparameter

- **Intercepts:** `[0.020234479097947435, -1.67355191291142, 1.6533174338134764]`

- **Koeffizienten-Matrix:**
  ```text
[[-0.11774762 -0.29113595  0.15148104 -0.18015671 -0.16062764  0.27276538
   0.17083476 -0.23994693]
 [ 0.09258381  0.12329955  0.04819011  0.27047208 -0.26337462  0.23286671
   0.09845457 -0.06459446]
 [ 0.02516382  0.1678364  -0.19967114 -0.09031538  0.42400226 -0.50563209
  -0.26928932  0.30454139]]
  ```
