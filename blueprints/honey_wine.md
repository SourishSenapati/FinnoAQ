# Honey Wine (Mead) Industrial Production: SOP

## 1. Process Overview and Stoichiometry
Honey wine production relies on the biochemical conversion of fructose and glucose into ethanol and CO2. At an industrial scale (10,000L), precision in "Must" preparation and nutrient management ensures consistent final ABV and flavor stability.

### 1.1 Target Specifications
- **Final ABV:** 12.5% ± 0.5%
- **Initial Gravity (OG):** 1.095 - 1.110
- **Final Gravity (FG):** 0.990 - 1.002
- **Volatile Acidity (VA):** < 0.4 g/L
- **Shelf Life:** 24+ Months (Bottle-stabilized)

## 2. Comprehensive Formulation (Per 10,000L Batch)
| Component | Quantity | Industrial Grade | Purpose |
| :--- | :--- | :--- | :--- |
| **Mustard Honey** | 3,800 kg | SS-Filtration (100 mesh) | Primary Carbon Source |
| **Purified Water** | ~6,500 L | RO / De-chlorinated | Diluent |
| **Yeast (S. cerevisiae)** | 2.5 kg | Lalvin EC-1118 (Active Dry) | Fermentation Agent |
| **YAN Booster** | 4.0 kg | Diammonium Phosphate (DAP) | Nitrogen Source |
| **Complex Nutrients** | 3.5 kg | Fermaid O / Go-Ferm | Micronutrient Support |
| **Tartaric Acid** | As needed | Food Grade | pH Correction |

## 3. Detailed Process Blueprint

### Phase 1: Must Preparation and Homogenization (T-Minus 0-12 hrs)
1. **Sanitization:** All SS316 10kL fermenters must be CIP (Clean-in-Place) cleaned with 2% caustic followed by peracetic acid.
2. **Honey Liquification:** Warm honey to 45°C in a jacketed pre-mix tank. Do not exceed 50°C to preserve enzymatic activity.
3. **Blending:** Mix honey with RO water at a 40:60 ratio. Use a high-capacity paddle agitator (45 RPM) for 60 minutes.
4. **Gravity Adjustment:** Measure Specific Gravity (SG) using a bridge refractometer. Targeted OG: 1.102 @ 20°C.
5. **Initial Acidification:** Measure pH. Add Tartaric acid in 1kg increments till pH reaches 3.4 - 3.6.

### Phase 2: Yeast Rehydration and Inoculation (T-Minus 12-14 hrs)
1. **Go-Ferm Addition:** Suspend Go-Ferm in 50L of 40°C water.
2. **Pitching:** Add EC-1118 yeast to the suspension. Stir gently and allow 20 minutes for rehydration.
3. **Tempering:** Slowly add 10L of must to the yeast slurry to reduce temperature. Pitch into the main tank when within 5°C of tank temp.
4. **Aeration:** Pump-over or sputter-aerate for 30 minutes to ensure 8-10 mg/L dissolved oxygen for the lag phase.

### Phase 3: Fermentation Dynamics (Days 1 - 21)
1. **Temperature Control:** Maintain jacket coolant temp to keep must at 21°C ± 1.0°C.
2. **Staggered Nutrient Addition (SNA):**
   - **T+24 hrs:** Add 1kg DAP + 1kg Fermaid O.
   - **T+48 hrs:** Add 1.5kg DAP.
   - **1/3 Sugar Break:** When SG hits 1.065, add the final 1.5kg DAP.
3. **Degassing:** Daily pump-over for first 7 days to release CO2 and prevent yeast stress.
4. **Monitoring:** Execute 2x daily SG and Temp checks. Plot decay curve vs. CUDA baseline model.

### Phase 4: Stabilization and Racking (Days 22 - 45)
1. **Primary Racking:** Once SG < 1.000 (verified by hydrometer), rack mead to a secondary conical tank.
2. **Cold Crashing:** Drop coolant temperature to 2°C for 5 days. This accelerates yeast flocculation.
3. **Sulfiting:** Add Potassium Metabisulphite (PMS) @ 50ppm (approx 1g per 20L).
4. **Clarification:** Dosing with 2% Bentonite slurry (1kg/10kL) to remove haze.

### Phase 5: Filtration and Bottling (Days 45+)
1. **Coarse Filtration:** Pass through 2.0-micron plate-and-frame filter.
2. **Polishing:** Use 0.45-micron absolute pleated cartridge filter for sterile bottling.
3. **Back-sweetening (Optional):** If semi-sweet is desired, add honey and Potassium Sorbate (200ppm) to prevent bottle bombs.
4. **Atmospheric Control:** Bottle under Nitrogen sparging to minimize oxidation.

## 4. Machinery & CAPEX Requirements
- **Fermenters:** Jacketed SS316L Conical Tanks (15kL Capacity).
- **Cooling:** Glycol Chiller Plant (25kW Thermal capacity).
- **Pump:** Sanitary Centrifugal Pump (Food Grade).
- **Control:** PLC-based Temperature and SG monitoring system.

## 5. Potential Failure Modes and Mitigations (FMEA)
| Failure Mode | Root Cause | Mitigation |
| :--- | :--- | :--- |
| **Stuck Fermentation** | Low YAN / Temperature Shock | Re-pitch with uvaferm 43 or add 50ppm Nitrogen. |
| **Oxidation (Cardboard taste)** | High O2 exposure post-Ferment | CO2 headspace blanketing mandatory. |
| **Volatile Acidity (Vinegar)** | Acetobacter contamination | Maintain SO2 levels and hermetic seals. |

## 6. Regulatory Compliance & Licensing (West Bengal & India)

### 6.1 Central Level (India)
- **FSSAI License:** Central License mandatory for 10kL+ batches or turnover > ₹20 Cr. 
- **AGMARK:** Compulsory for Mead/Honey products to certify purity.
- **GST Registration:** Mandatory (HSN 2206 for Mead/Wine).
- **APEDA:** Mandatory for export of honey/wine products from India.

### 6.2 State Level (West Bengal)
- **WB Excise License:** L-1/L-2 license for Mead (Alcoholic) production and bottling.
- **WB Fire & Emergency Services:** Fire safety NOC for storage tanks.
- **WB Pollution Control Board (WBPCB):** "Orange" Category Consent to Operate (CTO) for fermentation units.
- **Trade License:** From local Municipality/Panchayat (Kolkata/Howrah etc).
- **SWAS (Single Window Agency System):** Recommended for West Bengal food processing units.

### 6.3 Exemptions & Thresholds
- **FSSAI:** Registration (instead of License) if turnover < ₹12 Lakhs.
- **Excise Duty:** Exempt for personal consumption units ( < 50L/year) in certain districts.
- **Pollution NOC:** Exempt for micro-cottage units in approved rural clusters.

## 7. Utility & Sustainability (Resource Optimization)

- **Power Load:** 15kW Peak (Mostly chiller & pump load). Use high-efficiency VFD motors.
- **Cooling:** Shared Glycol Chiller for multiple fermentation lines.
- **Waste Management:** Spent yeast (lees) as high-protein livestock feed additive.
- **Energy:** Heat recovery from chiller exhaust for pre-heating raw honey.

## 8. Financial & Tax Efficiency (West Bengal Specs)

- **WB Incentive:** WB Industrial Promotion Assistance (IPA) - 10-25% subsidy on fixed capital.
- **Tax Efficiency:** Use HSN 2206 (GST 18%) for Mead. Leverage MSME "ZED" Certification for lower interest rates.
- **Procurement:** Source through Farmer Producer Organizations (FPOs) in Sundarbans/Nadia to avail West Bengal "Agri-Market" tax exemptions.
- **Break-Even (Est):** 14-18 months at 60% production capacity.

## 9. Production Readiness & QC Checklist (Batch Start)

- **Pre-Flight Check:** Verify Glycol temperature is at 4°C. Ensure all SS-valves are in 'Closed' position. CIP (Clean in Place) verification complete (No caustic residue).
- **MBR Entry:** Log Batch ID (WINE-001); Lot ID for Honey; Initial Temperature & SG.
- **In-Process QC:** Portable Refractometer (Check SG every 12h); Hydrometer (Verify terminal gravity).
- **Safety Protocol:** Chemical-resistant aprons & Face shields for acid handling (pH correction). 
- **Kill Switch:** If temperature exceeds 32°C, activate auxiliary cooling loop immediately.

## 10. Maintenance & Disaster Recovery (West Bengal Specs)

- **Traceability:** Each batch linked to CUDA-simulated kinetics via QR code on label.
- **Monsoon Recovery:** Double-palletizing of raw honey barrels to prevent ground moisture seepage. Active dehumidification to keep cellar RH < 65%.
- **Maintenance:** Bi-weekly seal/gasket inspection (Food Grade H1 Grease).

---
*FinnoAQ Industrial Blueprint - Engineering Specification V3.0*
*Master Production Record Ready - Go-Live Version*
