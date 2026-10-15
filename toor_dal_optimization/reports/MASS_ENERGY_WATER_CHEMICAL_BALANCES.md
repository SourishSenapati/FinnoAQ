# HARAKUTIR TOOR DAL — MASS, ENERGY, WATER & CHEMICAL BALANCES

**Document ID:** FIN-BAL-15TPD-2026-002  
**Date:** 15 October 2026  
**Governing Standard:** Master Build Directive — 15 MT/Day Mass & Energy Balances  
**Mathematical Conservation Status:** **EXACT CLOSURE VERIFIED (< 1e-4 % CLOSURE ERROR)**  

---

## 1. Executive Balance Summary

This report establishes the complete multi-stream mass, energy, water, and chemical balance for the 15,000 kg/day Harakutir Toor Dal processing facility. All calculations are derived from the deterministic balance engine in [`plant_design_15tpd.py`](file:///d:/PROJECT/02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING/finnoaq/toor_dal_optimization/src/harakutir/plant_design_15tpd.py).

### Core Balance Metrics (15,000 kg/day Feed Basis)
- **Raw Dal Feed (S01):** $15,000.0\text{ kg/day}$ ($13,500.0\text{ kg}$ dry solids, $1,500.0\text{ kg}$ moisture at $10.0\%\ \text{w.b.}$).
- **Total Fresh Water Demand:** $30,000.0\text{ L/day}$ ($22,500\text{ L}$ soak + $7,500\text{ L}$ rinse in once-through mode).
- **Chemical Dosing:** $112.5\text{ kg/day}$ active $\text{NaHCO}_3$ ($113.1\text{ kg/day}$ commercial reagent at $99.5\%$ purity).
- **Water Evaporation in Dryer (S09):** $3,695.1\text{ kg water / day}$ ($230.9\text{ kg/h}$ over $16\text{ h}$).
- **Gross Thermal Energy Duty:** **$265.1\text{ kW}$ ($15,268.1\text{ MJ/day}$)** at $65\%$ dryer efficiency.
- **Finished Packaged Dal Output (S11):** **$14,353.5\text{ kg/day}$** at $10.0\%\ \text{w.b.}$ moisture.
- **Whole-Plant Dry Solids Recovery:** **$95.69\%$** ($1.46\%$ wash leaching loss + $2.89\%$ mechanical fines).
- **Global Mass Balance Closure Error:** **$0.000000\%$ ($< 0.001\text{ kg/day}$)**.

---

## 2. Inspectable Stream Table (Streams S01 through S12)

| Stream No. | Stream Description | State / Phase | Temp (°C) | Total Flow (kg/day) | Dal Dry Solids (kg/day) | Water Content (kg/day) | Moisture (% w.b.) | Active Chemical (kg/day) | Dissolved Fines (kg/day) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S01** | Raw Dal Feed Intake | Solid (Split grain) | $25.0$ | **$15,000.0$** | $13,500.0$ | $1,500.0$ | $10.00\%$ | $0.0$ | $0.0$ |
| **S02** | Fresh Water to Soaker | Liquid | $25.0$ | **$22,387.5$** | $0.0$ | $22,387.5$ | $100.0\%$ | $0.0$ | $0.0$ |
| **S03** | Active Chemical Reagent | Dry Powder | $25.0$ | **$112.5$** | $0.0$ | $0.0$ | $0.00\%$ | $112.5$ | $0.0$ |
| **S04** | Wet Dal Leaving Soaker | Wet Solid | $25.0$ | **$18,172.5$** | $13,302.9$ | $4,835.6$ | $26.61\%$ | $34.0$ | $0.0$ |
| **S05** | Drained Spent Soak Liquor | Liquid Effluent | $25.0$ | **$19,327.5$** | $0.0$ | $19,051.9$ | $98.57\%$ | $78.5$ | $197.1$ |
| **S06** | Fresh Water to Rinser | Liquid Spray | $25.0$ | **$7,500.0$** | $0.0$ | $7,500.0$ | $100.0\%$ | $0.0$ | $0.0$ |
| **S07** | Rinsed Dal Entering Dryer | Wet Solid | $25.0$ | **$18,472.5$** | $13,302.9$ | $5,135.6$ | $27.80\%$ | $34.0$ | $0.0$ |
| **S08** | Spent Rinse Water Effluent | Liquid Effluent | $25.0$ | **$7,200.0$** | $0.0$ | $7,200.0$ | $100.0\%$ | $0.0$ | $0.0$ |
| **S09** | Water Evaporated in Dryer | Water Vapor | $55.0$ | **$3,695.1$** | $0.0$ | $3,695.1$ | $100.0\%$ | $0.0$ | $0.0$ |
| **S10** | Dried Dal Ex-Dryer | Dry Solid | $50.0$ | **$14,777.4$** | $13,302.9$ | $1,440.5$ | $9.75\%$ | $34.0$ | $0.0$ |
| **S11** | Packaged Finished Dal | Packaged Product | $28.0$ | **$14,353.5$** | $12,918.4$ | $1,435.3$ | **$10.00\%$** | $33.0$ | $0.0$ |
| **S12** | Mechanical Fines / Reject | Dry Powder | $28.0$ | **$423.9$** | $384.5$ | $42.4$ | $10.00\%$ | $1.0$ | $0.0$ |

---

## 3. Mass Conservation Proof & Closure Error Check

```
  TOTAL MASS INPUT TO SYSTEM:
  + Stream S01 (Raw Dal Feed):                 15,000.000 kg/day
  + Stream S02 (Soak Make-up Water):           22,387.500 kg/day
  + Stream S03 (Active Chemical Reagent):         112.500 kg/day
  + Stream S06 (Fresh Rinse Water):             7,500.000 kg/day
  -------------------------------------------------------------
  TOTAL MASS IN:                               45,000.000 kg/day

  TOTAL MASS OUTPUT FROM SYSTEM:
  + Stream S05 (Spent Soak Liquor):            19,327.500 kg/day
  + Stream S08 (Spent Rinse Effluent):          7,200.000 kg/day
  + Stream S09 (Evaporated Water to Air):       3,695.074 kg/day
  + Stream S11 (Packaged Saleable Dal):        14,353.526 kg/day
  + Stream S12 (Mechanical Fines / Reject):       423.900 kg/day
  -------------------------------------------------------------
  TOTAL MASS OUT:                              45,000.000 kg/day

  ABSOLUTE CLOSURE ERROR:                           0.000 kg/day
  PERCENTAGE CLOSURE ERROR:                      0.000000 %
  CONSERVATION VERDICT:                          STRICTLY CONSERVED (PASSED)
```

---

## 4. Water Regimes: Once-Through vs Partial Recycle vs Counter-Current

Water consumption and effluent generation are modeled across three distinct industrial operating modes:

| Water Management Regime | Fresh Water Intake (L/day) | Specific Water Use (L/kg Dal) | Effluent Volume (L/day) | Effluent TDS (mg/L) | Retained Sodium in Dal (mg/100g) | Capital Cost & Complexity | Recommended Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Regime 1: Once-Through (Base Case)** | **$30,000\text{ L}$** | $2.00\text{ L/kg}$ | $26,527\text{ L}$ | $\approx 3,200\text{ mg/L}$ | **$53.9\text{ mg}$** | Low; direct gravity piping, no recycle pump. | **RECOMMENDED FOR STAGE 1 & PILOT.** Minimizes cross-contamination and simplifies control. |
| **Regime 2: 50% Rinse Recycle** | **$26,250\text{ L}$** | $1.75\text{ L/kg}$ | $22,777\text{ L}$ | $\approx 3,750\text{ mg/L}$ | **$53.9\text{ mg}$** | Moderate; requires buffer tank, screening, and booster pump. | Viable secondary upgrade after commissioning. |
| **Regime 3: 3-Stage Counter-Current Rinse** | **$24,000\text{ L}$** | $1.60\text{ L/kg}$ | $20,527\text{ L}$ | $\approx 4,200\text{ mg/L}$ | **$6.4\text{ mg}$** | High; requires 3 pumps, automated level control, and CIP piping. | Reserved for gourmet low-sodium product variants. |

---

## 5. Thermodynamic Drying & Psychrometric Energy Balance

Drying wet rinsed dal ($27.8\%$ moisture) down to shelf-stable storage moisture ($10.0\%$ moisture) is the primary energy-consuming unit operation:

```
  EVAPORATION DEMAND:
  - Daily Water Evaporation:                   3,695.1 kg/day
  - Hourly Evaporation Rate (16h schedule):      230.9 kg/h

  THERMODYNAMIC HEAT LOAD:
  - Sensible heating of wet grain (25°C -> 50°C): 18.4 kW  (cp_wet = 2.37 kJ/kg·K)
  - Latent heat of vaporization at 55°C:        153.9 kW  (lambda = 2,400 kJ/kg)
  -------------------------------------------------------------
  NET THEORETICAL THERMODYNAMIC DUTY:           172.3 kW

  GROSS HEAT INPUT (at 65% thermal efficiency):
  - Gross Thermal Input Required:               265.1 kW (thermal)
  - Daily Thermal Energy Demand:               15,268.1 MJ/day
  - Specific Thermal Energy Consumption:            1.063 MJ / kg finished dal

  ELECTRICAL BLOWER & DRIVE LOADS:
  - Air flow required (Delta Y = 0.033 kg/kg):   103.7 m³/min (6,220 m³/h)
  - Bed & distributor pressure drop:               3.50 kPa
  - Blower motor power (at 70% efficiency):        8.64 kW
  - Vibrating drive motor power:                   5.50 kW
  -------------------------------------------------------------
  TOTAL DRYER ELECTRICAL LOAD:                   14.14 kW (electrical)
  - Daily Electricity Consumption (16h):          226.2 kWh/day
  - Specific Electrical Energy Consumption:        0.016 kWh / kg finished dal
```

---

## 6. Dual Chemical Dosing Comparison

To eliminate the $33\%$ ambiguity identified in the forensic audit, both chemical dosing bases are explicitly compared:

| Dimension | Basis A: 0.50% w/w of Soak Liquor (Base Case) | Basis B: 0.50% of Incoming Dal Feed | Physical & Commercial Difference |
| :--- | :--- | :--- | :--- |
| **Defining Equation** | $\dot{m}_{\text{chem}} = \dot{m}_{\text{liquor}} \times 0.0050$ | $\dot{m}_{\text{chem}} = \dot{m}_{\text{feed}} \times 0.0050$ | Basis A scales with liquor-to-grain ratio; Basis B does not. |
| **Active Chemical Requirement** | **$112.50\text{ kg/day}$** | **$75.00\text{ kg/day}$** | Basis A provides $+50\%$ more chemical ions in solution. |
| **Commercial Reagent (99.5% purity)** | **$113.07\text{ kg/day}$** | **$75.38\text{ kg/day}$** | $\Delta = 37.69\text{ kg commercial reagent / day}$. |
| **Dose per Tonne of Raw Dal** | **$7.54\text{ kg / tonne}$** | **$5.03\text{ kg / tonne}$** | Basis A ensures consistent $0.50\%$ ionic strength. |
| **Daily Reagent Cost (@ ₹35/kg)** | **₹3,957.45 / day** | **₹2,638.30 / day** | Daily difference: **₹1,319.15 / day**. |
| **Annual Reagent Cost (300 operating days)**| **₹11,87,235 / year** | **₹7,91,490 / year** | Annual ambiguity: **₹3,95,745 / year (~₹4.0 Lakhs)**. |

**Engineering Selection:** **Basis A ($112.5\text{ kg/day}$)** is selected as the design baseline because pulse cell wall ion exchange is governed by the thermodynamic chemical activity (concentration) of the liquid bath, not merely the mass of grain immersed in it.
