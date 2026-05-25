# ETF Predictor Pipeline-Report

- **Generiert am:** 2026-05-25 14:55:47
- **Target ETF:** CSINDU.SW
- **Forecast Horizon:** 126 Trading Days

## Aktuelle Marktprognose (Predict)

Basierend auf den Schlusskursen vom **2025-11-14** prognostiziert das Modell:

> **Klasse:** Up
>
> **Wahrscheinlichkeiten:** Down: 19.15% | Flat: 9.12% | Up: 71.74%

---

## Ausgewaehlte Praediktoren (SFS)

| Praediktor | Einfluss (Mean Absolut) |
| :--- | :--- |
| VNQ_126M_ret | 0.400744 |
| UNRATE_63M_ret | 0.352738 |
| BTC-USD_126M_ret | 0.304116 |
| JPNCPIALLMINMEI_63M_ret | 0.287996 |
| PRINTO01EZQ661S_63M_ret | 0.243200 |
| DX-Y.NYB_126M_ret | 0.176852 |
| UNRATE_21M_ret | 0.114305 |
| XLE_126M_ret | 0.113003 |
| ^TNX_21M_ret | 0.104183 |
| CP00MI15EA20M086NEST_21M_ret | 0.075972 |
| CPIAUCSL_21M_ret | 0.029507 |
| CPIAUCSL_63M_ret | 0.016775 |

## Aussortierte Praediktoren

### 1. In der Endauswahl verworfen (SFS Rejects)
`8035.T_126M_ret, 9984.T_63M_ret, 9984.T_126M_ret, AAPL_63M_ret, AAPL_126M_ret, AZN.L_126M_ret, BNDX_21M_ret, BNDX_63M_ret, BRK-B_21M_ret, BRK-B_63M_ret, BTC-USD_63M_ret, BWX_21M_ret, BWX_63M_ret, BWX_126M_ret, CSINDU.SW_21M_ret, DX-Y.NYB_63M_ret, EEM_63M_ret, EEM_126M_ret, HG=F_63M_ret, HG=F_126M_ret, IGOV_21M_ret, IGOV_63M_ret, IGOV_126M_ret, LE=F_21M_ret, LE=F_63M_ret, LQD_63M_ret, RIO.L_126M_ret, TLT_126M_ret, XBI_63M_ret, XBI_126M_ret, XLE_21M_ret, XLE_63M_ret, XLP_21M_ret, XLP_63M_ret, XLP_126M_ret, XLU_21M_ret, XLU_63M_ret, XLU_126M_ret, XLV_21M_ret, XLV_63M_ret, XLV_126M_ret, ZW=F_63M_ret, ZW=F_126M_ret, ^IRX_21M_ret, ^IRX_63M_ret, ^N225_126M_ret, CPIAUCSL_126M_ret, PAYEMS_63M_ret, PAYEMS_126M_ret, UNRATE_126M_ret, T10Y2Y_126M_ret, CP00MI15EA20M086NEST_126M_ret, LRHUTTTTEZM156S_21M_ret, LRHUTTTTEZM156S_63M_ret, LRHUTTTTEZM156S_126M_ret, ECBASSETS_126M_ret, PRINTO01EZQ661S_126M_ret, JPNCPIALLMINMEI_21M_ret, JPNCPIALLMINMEI_126M_ret, LRHUTTTTJPM156S_126M_ret, JPNASSETS_126M_ret, GBRCPIALLMINMEI_126M_ret, LRHUTTTTGBM156S_21M_ret, LRHUTTTTGBM156S_63M_ret, LRHUTTTTGBM156S_126M_ret, ratio_copper_gold_126M_ret, ratio_intl_vs_us_bonds_63M_ret, ratio_intl_vs_us_bonds_126M_ret`

### 2. Im Basisfilter verworfen (ANOVA Rejects)
<details>
<summary>Klicken, um alle <b>112</b> in Stufe 1 aussortierten Variablen anzuzeigen</summary>

`7203.T_21M_ret, 7203.T_63M_ret, 7203.T_126M_ret, 8035.T_21M_ret, 8035.T_63M_ret, 9984.T_21M_ret, AAPL_21M_ret, AZN.L_21M_ret, AZN.L_63M_ret, BAS.DE_21M_ret, BAS.DE_63M_ret, BAS.DE_126M_ret, BNDX_126M_ret, BRK-B_126M_ret, BTC-USD_21M_ret, CL=F_21M_ret, CL=F_63M_ret, CL=F_126M_ret, CSINDU.SW_63M_ret, CSINDU.SW_126M_ret, DX-Y.NYB_21M_ret, EEM_21M_ret, GC=F_21M_ret, GC=F_63M_ret, GC=F_126M_ret, HG=F_21M_ret, HYG_21M_ret, HYG_63M_ret, HYG_126M_ret, JPM_21M_ret, JPM_63M_ret, JPM_126M_ret, LE=F_126M_ret, LQD_21M_ret, LQD_126M_ret, MSFT_21M_ret, MSFT_63M_ret, MSFT_126M_ret, NVDA_21M_ret, NVDA_63M_ret, NVDA_126M_ret, RIO.L_21M_ret, RIO.L_63M_ret, SAP.DE_21M_ret, SAP.DE_63M_ret, SAP.DE_126M_ret, SHEL.L_21M_ret, SHEL.L_63M_ret, SHEL.L_126M_ret, SIE.DE_21M_ret, SIE.DE_63M_ret, SIE.DE_126M_ret, TLT_21M_ret, TLT_63M_ret, VNQ_21M_ret, VNQ_63M_ret, XBI_21M_ret, XLF_21M_ret, XLF_63M_ret, XLF_126M_ret, XLK_21M_ret, XLK_63M_ret, XLK_126M_ret, XLY_21M_ret, XLY_63M_ret, XLY_126M_ret, ZC=F_21M_ret, ZC=F_63M_ret, ZC=F_126M_ret, ZW=F_21M_ret, ^GDAXI_21M_ret, ^GDAXI_63M_ret, ^GDAXI_126M_ret, ^IRX_126M_ret, ^N225_21M_ret, ^N225_63M_ret, ^TNX_63M_ret, ^TNX_126M_ret, ^VIX_21M_ret, ^VIX_63M_ret, ^VIX_126M_ret, PAYEMS_21M_ret, T10Y2Y_21M_ret, T10Y2Y_63M_ret, WALCL_21M_ret, WALCL_63M_ret, WALCL_126M_ret, CP00MI15EA20M086NEST_63M_ret, ECBASSETS_21M_ret, ECBASSETS_63M_ret, PRINTO01EZQ661S_21M_ret, LRHUTTTTJPM156S_21M_ret, LRHUTTTTJPM156S_63M_ret, JPNASSETS_21M_ret, JPNASSETS_63M_ret, JPNPROINDMISMEI_21M_ret, JPNPROINDMISMEI_63M_ret, JPNPROINDMISMEI_126M_ret, GBRCPIALLMINMEI_21M_ret, GBRCPIALLMINMEI_63M_ret, GBRPROINDMISMEI_21M_ret, GBRPROINDMISMEI_63M_ret, GBRPROINDMISMEI_126M_ret, ratio_copper_gold_21M_ret, ratio_copper_gold_63M_ret, ratio_credit_spread_21M_ret, ratio_credit_spread_63M_ret, ratio_credit_spread_126M_ret, ratio_consumer_risk_21M_ret, ratio_consumer_risk_63M_ret, ratio_consumer_risk_126M_ret, ratio_intl_vs_us_bonds_21M_ret`

</details>

---

## KI-Interpretation der Praediktoren (Hedgefonds Analyst)

**1. Makrooekonomisches Setup:**

*   **Zinsstruktur & Monetärpolitik:**
    *   **^TNX_21M_ret (US 10-Jahresrendite, kurzfristiges Momentum):** Misst kurzfristige Zinsänderungserwartungen in den USA, die globale Finanzierungskosten und Diskontierungsfaktoren beeinflussen. Relevant für Bewertung von Real Assets und Anleihe- vs. Aktienattraktivität.
    *   **PRINTO01EZQ661S_63M_ret (Eurozonen-M3, mittelfristiges Momentum):** Indikator für das Liquiditätsangebot im Euroraum. Beeinflusst Kreditwachstum, Inflation und Kapitalflüsse, essentiell für eine exportorientierte Wirtschaft wie die Schweiz.
    *   **VNQ_126M_ret (US Real Estate, langfristiges Momentum):** Reflektiert die langfristige Attraktivität und Bewertung von Sachwerten. Zeigt an, ob Kapital in Real Assets fließt, was in Niedrigzins- oder Inflationsphasen relevant ist.
*   **Inflation & Wachstum:**
    *   **CPIAUCSL_21M_ret & _63M_ret (US CPI, kurz- & mittelfristig):** Direkte Messgröße der US-Inflation. Dient als Hauptindikator für Fed-Politik, Kaufkraft und Margendruck globaler Unternehmen.
    *   **JPNCPIALLMINMEI_63M_ret (Japan CPI, mittelfristig):** Signalisiert potentielle globale Re-Inflation, da Japans Ausbruch aus der Deflation weitreichende Implikationen für globale Anleiherenditen und Wechselkurse hat.
    *   **UNRATE_63M_ret & _21M_ret (US Arbeitslosenquote) & CP00MI15EA20M086NEST_21M_ret (EZ Arbeitslosenquote):** Arbeitsmarktdynamiken in den USA und der Eurozone auf verschiedenen Zeithorizonten. Frühindikatoren für Konsum, Lohnwachstum und Kapazitätsauslastung, die den globalen Wirtschaftszyklus maßgeblich prägen.
*   **Währung & Rohstoffe:**
    *   **DX-Y.NYB_126M_ret (US Dollar Index, langfristiges Momentum):** US-Dollar-Stärke als Indikator für globale Risikobereitschaft, Safe-Haven-Status und relative Wirtschaftsstärke der USA. Beeinflusst die Wettbewerbsfähigkeit Schweizer Exporteure.
    *   **XLE_126M_ret (US Energie-Sektor, langfristiges Momentum):** Korreliert mit globaler Industrieproduktion, Rohstoffpreisen (insbesondere Öl und Gas) und inflationsgetriebenem Wachstum. Zeigt die Bewertung der Realwirtschaft.

**2. Sektor- & Marktdynamik:**

*   **Langzyklische Kapitalallokation:**
    *   **VNQ_126M_ret (US Real Estate):** Starkes langfristiges Momentum in Immobilien REITs deutet auf strukturelle Nachfrage nach Sachwerten, Absicherung gegen Inflation oder eine anhaltende Anziehungskraft von Income-Assets im Niedrigzinsumfeld hin.
    *   **XLE_126M_ret (US Energie-Sektor):** Langfristige Outperformance des Energiesektors signalisiert einen potentiellen Rohstoff-Superzyklus oder eine Phase robuster globaler Industriekonjunktur mit steigender Energienachfrage.
*   **Arbeitsmarkt als Zyklusanzeiger:**
    *   **UNRATE (US) & CP00MI15EA20M086NEST (EZ):** Die Momentum-Indikatoren der Arbeitslosenquoten über verschiedene Zeitfenster (kurz- bis mittelfristig) dienen als präzise Indikatoren für die aktuelle Phase des Wirtschaftszyklus (Expansion, Rezession, Erholung) in den größten westlichen Volkswirtschaften.
*   **Risikobereitschaft & Liquiditätsindikator:**
    *   **BTC-USD_126M_ret (Bitcoin, langfristiges Momentum):** Das signifikante langfristige Momentum von Bitcoin dient als proxy für globale Liquiditätsbedingungen und das spekulative Risikoverhalten der Anleger. Eine starke Performance korreliert oft mit einer erhöhten Risikobereitschaft in traditionellen Märkten.

**3. Quant-Konklusion:**

*   **Holistisches Makro-Sentiment:** Die Prognose des CSINDU.SW ist eine hochkomplexe Funktion aus globalen Zins-, Inflations- und Liquiditätstrends, gemessen über Schlüsselindikatoren aus den USA, der Eurozone und Japan.
*   **Zyklische Positionierung entscheidend:** Die dominierende Rolle von zyklischen Sektoren (Real Estate, Energie) und der Dynamik der Arbeitsmärkte impliziert, dass die Modellprognose stark von der aktuellen und erwarteten Position im globalen Wirtschaftszyklus, insbesondere der Interaktion von Inflation und Realwachstum, getrieben wird.
*   **Liquidität & Risikobereitschaft:** Langfristige Trends in Bitcoin und dem US-Dollar unterstreichen die Bedeutung von globaler Liquidität und dem spekulativen Appetit der Anleger. Dies ist für den CSINDU.SW als offene Volkswirtschaft und globaler Finanzplatz ein entscheidender Treiber der Marktstimmung in den nächsten 6 Monaten.

## Mathematische Modellparameter

- **Intercepts:** `[-0.04429058577636871, -1.100145168606088, 1.1444357543824373]`

- **Koeffizienten-Matrix:**
  ```text
[[-2.19935739e-01  2.65277512e-01  4.00332854e-01 -1.69504437e-01
   1.56274686e-01 -3.39509432e-02  2.51623405e-02 -1.32838606e-01
  -5.29106784e-01  8.02950668e-02  3.64800289e-01  4.31993653e-01]
 [-2.36238834e-01 -5.81433494e-04  2.00783234e-01  1.21122476e-01
  -1.53939111e-01 -1.03088770e-02 -1.06413613e-02 -3.86190755e-02
   1.47566893e-01 -1.13958350e-01 -1.30933210e-02 -2.18705297e-01]
 [ 4.56174573e-01 -2.64696079e-01 -6.01116088e-01  4.83819615e-02
  -2.33557528e-03  4.42598201e-02 -1.45209792e-02  1.71457682e-01
   3.81539891e-01  3.36632837e-02 -3.51706968e-01 -2.13288355e-01]]
  ```
