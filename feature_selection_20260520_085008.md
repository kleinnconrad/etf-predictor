# Ergebnisse der Variablenselektion & Modellparameter

- **Generiert am:** 2026-05-20 08:50:35
- **Anzahl finaler Features:** 8

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

Die dominante Rolle von europäischen und asiatischen Large-Caps, insbesondere aus dem Vereinigten Königreich und Japan, deutet darauf hin, dass der mittelfristige Marktzustand des SPY maßgeblich von globalen statt rein US-dominierten Wirtschaftstrends beeinflusst wird. Die hohe Relevanz von Rohstoffunternehmen (Rio Tinto) und Energiekonzernen (BP) signalisiert, dass die globale Industrieproduktion, Nachfrage nach Grundmaterialien und Energiepreise – und damit Inflationstendenzen – entscheidende Vorlaufindikatoren für die Weltwirtschaft und folglich den US-Markt sind. Ein starkes Momentum in diesen Bereichen antizipiert typischerweise eine breitere wirtschaftliche Expansion.

Gleichzeitig spiegeln globale Konsumgüter (Unilever) und der Einzelhandel (Fast Retailing) das Vertrauen und die Kaufkraft internationaler Konsumenten wider. Deren Performance dient als Barometer für die globale Konsumausgabenentwicklung, die direkt die Umsatz- und Gewinnprognosen vieler multinationaler Unternehmen im SPY beeinflusst. Die Präsenz von AstraZeneca unterstreicht zudem die Bedeutung des globalen Gesundheitssektors als stabiler, aber innovationsgetriebener Wirtschaftsfaktor.

Die signifikante Einflussnahme von globalen Technologie-Investoren (SoftBank Group) und führenden US-Technologieplattformen (Meta) unterstreicht die Sensibilität des SPY gegenüber der globalen Risikobereitschaft und Kapitalallokation in Wachstumsbereiche. Positive Entwicklungen hier signalisieren Optimismus hinsichtlich zukünftiger Innovation und Profitabilität und fungieren als wichtiger Indikator für das allgemeine Marktvertrauen. Meta's kürzerer Betrachtungszeitraum deutet zudem auf eine unmittelbare Reflexion der Werbeausgaben und Tech-Stimmung hin.

## Modellparameter (Multinomial Logistic Regression)

- **Intercepts (Klassenordnung: Down [-1], Flat [0], Up [1]):**
  `[0.020234443701747238, -1.6735518750817375, 1.6533174313799979]`

- **Koeffizienten-Matrix (Form: Klassen x Features):**
  ```text
[[-0.11774768 -0.29113623  0.15148124 -0.18015667 -0.16062755  0.27276534
   0.17083455 -0.23994689]
 [ 0.09258395  0.12329957  0.04818967  0.27047195 -0.26337449  0.23286674
   0.098455   -0.06459463]
 [ 0.02516373  0.16783666 -0.19967091 -0.09031528  0.42400204 -0.50563209
  -0.26928955  0.30454152]]
  ```
