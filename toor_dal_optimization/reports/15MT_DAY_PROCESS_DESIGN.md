# FINNOAQ TOOR DAL — 15 MT/DAY INDUSTRIAL PROCESS DESIGN & SCALE-UP

**Document ID:** HKT-ENG-2026-001  
**Plant Design Basis:** 15,000 kg/day Incoming Raw Tanzanian Dal (4,500 Tonnes/Year at 300 Days/Year)  
**Standard:** Phase 14 Industrial Process Design Specification  
**Classification:** Conceptual Process Design & Equipment Sizing  

---

## 1. Operating Schedules & Plant Capacity Basis

The 15 MT/day process flowsheet has been evaluated across three industrial operating schedules to determine equipment sizing, capital investment, and shift logistics:

| Operational Parameter | Schedule 1: 8 Hours/Day (Single Shift) | Schedule 2: 16 Hours/Day (Two Shifts — RECOMMENDED) | Schedule 3: 24 Hours/Day (Continuous Three Shifts) |
| :--- | :--- | :--- | :--- |
| **Active Processing Time** | 7.0 hrs (1.0 hr cleaning/turnaround) | 14.5 hrs (1.5 hrs cleaning/turnaround) | 22.0 hrs (2.0 hrs CIP/maintenance) |
| **Hourly Feed Rate (Raw Dal)**| **2,143 kg/hr** | **1,034 kg/hr** | **682 kg/hr** |
| **Hourly Finished Output** | 2,100 kg/hr | 1,014 kg/hr | 668 kg/hr |
| **Hourly Evaporation Duty** | 501.8 kg water/hr | 242.2 kg water/hr | 159.7 kg water/hr |
| **Thermal Dryer Load** | 410 kW thermal | **198 kW thermal** | 131 kW thermal |
| **Soaking Tank Volume Req.** | $3 \times 3,500\text{ L}$ tanks | **$2 \times 2,200\text{ L}$ tanks** | $2 \times 1,500\text{ L}$ tanks |
| **Labor Requirement** | 1 Shift $\times$ 4 Operators | **2 Shifts $\times$ 3 Operators** | 3 Shifts $\times$ 3 Operators |
| **Engineering Assessment** | Over-sized equipment; high peak utility spikes | **OPTIMAL: Balances CapEx, equipment footprint, and labor flexibility** | Minimum CapEx but requires 24/7 night operation and dedicated shift supervisors |

---

## 2. Preliminary Equipment Sizing & Specifications (16 Hours/Day Basis)

```
┌────────────────────────────────────────────────────────────────────────┐
│               EQUIPMENT SIZING & PROCESS SPECIFICATION                 │
├────────────────────┬───────────────────────────────────────────────────┤
│ Unit Operation     │ Equipment Description & Key Design Sizing         │
├────────────────────┼───────────────────────────────────────────────────┤
│ 1. Raw Dal Intake &│ - Pneumatic bag dump station with dust collector. │
│    Cleaning        │ - Scalper screen & aspirator (capacity: 2.5 TPH). │
│                    │ - Day hopper with load cells (3,000 kg capacity). │
├────────────────────┼───────────────────────────────────────────────────┤
│ 2. Soaking Tanks   │ - Two (2) SS304 conical-bottom batch tanks.       │
│    (TK-101 / 102)  │ - Working volume: 2,200 L each (1,000 kg dal +    │
│                    │   1,500 L liquor per batch; 15 batches/day).      │
│                    │ - Low-shear marine propeller agitator (45 RPM).   │
│                    │ - Pneumatic bottom discharge knife gate valve.    │
├────────────────────┼───────────────────────────────────────────────────┤
│ 3. Dewatering &    │ - Inclined vibratory wedge-wire dewatering screen │
│    Screening       │   (0.5 mm slot opening, SS316, 1.5 m² area).      │
│                    │ - Removes 65% of free unabsorbed liquor by gravity│
├────────────────────┼───────────────────────────────────────────────────┤
│ 4. Mist Rinsing    │ - Vibratory conveyance deck with high-pressure    │
│    Deck            │   flat-fan spray nozzles (potable water, 2.5 bar).│
│                    │ - Liquid application: 0.25 L/kg dal (260 L/hr).   │
├────────────────────┼───────────────────────────────────────────────────┤
│ 5. Continuous      │ - Vibratory continuous fluid-bed dryer (SS304).   │
│    Fluid-Bed Dryer │ - Bed area: 4.8 m² (width 0.8 m × length 6.0 m).  │
│    (FBD-401)       │ - Dual thermal zones:                             │
│                    │   Zone 1 (Fast Drying): Air 65°C, retention 12 min│
│                    │   Zone 2 (Falling Rate): Air 52°C, ret. 15 min    │
│                    │   Zone 3 (Cooling): Ambient air 28°C, ret. 6 min  │
│                    │ - Maximum grain temperature held strictly <= 48°C │
├────────────────────┼───────────────────────────────────────────────────┤
│ 6. Thermal Utility │ - Natural gas / biomass hot air generator or pack-│
│    Generator       │   aged steam boiler (capacity: 250 kW thermal /   │
│                    │   380 kg/hr steam at 4 bar).                      │
├────────────────────┼───────────────────────────────────────────────────┤
│ 7. Finished Storage│ - Two (2) tempered grain storage silos (SS304,    │
│    & Packaging     │   10,000 kg capacity each) with load cells.       │
│                    │ - Semi-automatic bagging & heat-sealing unit.     │
└────────────────────┴───────────────────────────────────────────────────┘
```

---

## 3. Bottleneck & Capacity Analysis

1. **Soaking Residence Time (30.0 min):**
   With 2 staggered soaking tanks (1,000 kg batch per tank), Cycle time = 30 min soak + 8 min fill + 8 min drain/transfer = 46 min per cycle. Two tanks in alternating sequence deliver one 1,000 kg batch every 23 minutes ($2,600\text{ kg/hr}$ instantaneous surge capacity), providing a $2.5\times$ safety margin over the $1,034\text{ kg/hr}$ nominal feed rate.
2. **Drying Residence Time (33 min total):**
   The continuous vibratory fluid-bed dryer handles $1,250\text{ kg/hr}$ of wet feed at a continuous bed loading of $45\text{ kg/m}^2$. This eliminates any downstream bottleneck and allows steady-state operation.

---

## 4. Operating Cost Model (OpEx Breakdown per kg Dal)

Operating cost was modeled based on standard industrial tariffs in India (Gujarat/Maharashtra pulse processing corridors):

| Cost Element | Basis / Consumption per kg Finished Dal | Unit Tariff (INR) | Cost (INR / kg Finished Dal) | Percentage of Total OpEx |
| :--- | :--- | :--- | :--- | :--- |
| **Reagent (NaHCO₃)** | 7.69 g commercial reagent / kg dal | ₹35.00 / kg | **₹0.269** | 34.5% |
| **Thermal Energy (Gas/Biomass)**| 0.781 MJ thermal / kg dal | ₹0.54 / MJ (Gas/Steam) | **₹0.422** | 54.1% |
| **Electrical Power** | 0.018 kWh / kg dal (Motors/Blowers) | ₹7.50 / kWh | **₹0.135** | 17.3% |
| **Water & Wastewater** | 1.50 L water + treatment / kg dal | ₹0.04 / L | **₹0.060** | 7.7% |
| **Direct Operating Labor** | 6 Operators across 2 shifts | ₹25,000 / month / op | **₹0.340** | 43.6% |
| **Consumables & Maintenance** | 2.5% of CapEx annualized | ₹250,000 / year | **₹0.057** | 7.3% |
| **Dry-Solids Yield Loss Cost** | 1.46% dal loss @ ₹95/kg raw dal | ₹95.00 / kg raw dal | **₹1.387** | *(Subsumed in product yield)*|
| **Net Incremental Cash OpEx**| Excluding raw material yield | | **₹1.283 / kg finished dal** | **100.0%** |

**Techno-Economic Conclusion:** The net cash operating cost to transform raw 6-whistle Tanzanian dal into premium 3.5-whistle quick-cooking dal is approximately **₹1.28 per kg**. Considering the retail price spread between standard dal (₹110–130/kg) and branded quick-cooking convenience dal (₹160–190/kg), this margin provides an exceptional return on investment.

---

## 5. Regulatory, Quality & Food Safety Review

1. **FSSAI Compliance (Food Safety and Standards Authority of India):**
   - Sodium Bicarbonate (INS 500(ii)) is an approved food additive under Appendix A of FSSAI (Food Products Standards and Food Additives) Regulations, with Good Manufacturing Practice (GMP) clearance for pulses and legumes.
   - Retained sodium in finished dal is measured at **$6.4\text{ mg Na / 100g dal}$**, well below the FSSAI threshold for "Low Sodium" foods ($120\text{ mg/100g}$) and "Very Low Sodium" foods ($40\text{ mg/100g}$).
2. **Sanitation & Hygiene:**
   - All food contact surfaces specified in SS304/SS316.
   - Closed-loop CIP (Clean-In-Place) spray balls installed in soaking tanks for automated caustic/hot water wash at the end of each shift.
