# PROCESS ARCHITECTURE AND UNIT OPERATION SELECTION
**Document ID:** ENG-REP-15T-003  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** Process Chemical Engineering  

---

## 1. Process Route Evaluation & Comparison

Three distinct process flow architectures were evaluated for the 15 MT/day facility to balance product quality, retained sodium, water consumption, and capital expenditure:

```mermaid
graph TD
    subgraph Route B (Selected Base Case)
        R1[Raw Dal Feed 15 TPD] --> R2[Pre-Cleaning & Destoning SCN-101]
        R2 --> R3[Gravimetric Dosing GF-101]
        R3 --> R4[Batch Soaking TK-101A/B 0.5% NaHCO3]
        R4 --> R5[Vibratory Dewatering VS-101]
        R5 --> R6[Single-Pass Water Mist Rinse 0.15:1 Ratio]
        R6 --> R7[Continuous Fluid-Bed Drying DR-101 60C]
        R7 --> R8[Integral Fluid-Bed Cooling CLR-101 25C]
        R8 --> R9[Optical/Gravity Scalping SCN-102 & MD-101]
        R9 --> R10[14-Head Multihead Packaging PK-101]
    end
    
    subgraph Route C (Emergency Bypass Line)
        R2 -.->|Quality/Treatment Trip| BYPASS[Direct Bypass to Packaging PK-101]
    end
```

### Comparative Route Matrix:

| Evaluation Criteria | Route A: Counter-Current 3-Stage Rinse | Route B: Single-Pass Mist Rinse (Selected Base) | Route C: Bypass Untreated Line |
| :--- | :--- | :--- | :--- |
| **Product Format** | Ordinary intact split dal | Ordinary intact split dal | Ordinary intact split dal (Standard) |
| **Cooking Time Target** | ~3 whistles (~15 min) | ~3 whistles (~15 min) | ~6 whistles (~22 min baseline) |
| **Fresh Water Demand** | $14.5\text{ m}^3\text{/day}$ | $18.8\text{ m}^3\text{/day}$ | $0.0\text{ m}^3\text{/day}$ (Dry process) |
| **Retained Sodium** | $6.4\text{ mg Na/100g dal}$ | $53.9\text{ mg Na/100g dal}$ (FSSAI $<350$) | $3.5\text{ mg Na/100g dal}$ (Natural) |
| **Dryer Thermal Load** | $265.1\text{ kW}$ ($3,695\text{ kg H2O/day}$) | $265.1\text{ kW}$ ($3,695\text{ kg H2O/day}$) | $0.0\text{ kW}$ |
| **System Complexity** | High (3 pumps, 3 tanks, level controls) | **Moderate (Single spray header on screen)** | Minimal |
| **CapEx Estimate** | ₹76.5 Lakhs | **₹68.5 Lakhs** | ₹32.0 Lakhs |
| **OpEx Estimate** | ₹1.41 / kg finished dal | **₹1.34 / kg finished dal** | ₹0.22 / kg finished dal |
| **Hygiene / Biofilm Risk** | Moderate (Recycle liquor build-up) | **Low (Single-pass fresh mist)** | None |

**Selection Decision:** Route B is selected as the industrial design base case. While Route A slightly reduces water demand, Route B achieves full FSSAI sodium compliance ($53.9\text{ mg/100g} \ll 350\text{ mg/100g}$) with significantly lower mechanical complexity, zero microbial recycle contamination risk, and ₹8 Lakhs lower CapEx.

---

## 2. Unit-Operation Decision Register

Every unit operation proposed for the facility was evaluated under a strict evidence-driven decision matrix:

| Unit Operation | Tag | Status | Technical Rationale & Decision Basis |
| :--- | :--- | :--- | :--- |
| **Receiving Hopper & Screener** | `HOP-101`, `SCN-101` | **REQUIRED** | Removes stones, chaff, and tramp metal from imported sea containers. Essential for machine protection and food safety. |
| **Gravimetric Batch Feeder** | `GF-101` | **REQUIRED** | Loss-in-weight twin-screw feeder. Guarantees precise 1:1.5 mass ratio between dal and chemical soak liquor ($\pm 0.5\%$). |
| **Jacketed Dual Soak Vessels** | `TK-101A/B` | **REQUIRED** | Dual alternating tanks allow continuous 16h line operation while maintaining exact 30-minute batch contact time per lot. |
| **Low-Shear Hydrofoil Agitator** | `AG-101A/B` | **REQUIRED** | Hydrofoil impeller ($D=600\text{ mm}$, $N=35\text{ rpm}$, $v_{tip}=1.1\text{ m/s}$). Gently suspends pulses without causing grain splitting. |
| **Vibratory Dewatering Screen** | `VS-101` | **REQUIRED** | 1.0 mm SS316L wedge-wire screen. Rapidly separates soaked grains from free liquor in $<10$ seconds with integrated mist rinse. |
| **Continuous Fluid-Bed Dryer** | `DR-101` | **REQUIRED** | Vibrating fluid-bed with steam heat exchanger. Gently removes $3,695\text{ kg H2O/day}$ at 60°C without case-hardening or starch gelatinization. |
| **Fluid-Bed Product Cooler** | `CLR-101` | **REQUIRED** | Cools dal from 50°C to $<30°C$ using filtered ambient air. Prevents condensation and mould spoilage inside sealed plastic retail pouches. |
| **Gravity-Fall Metal Detector** | `MD-101` | **REQUIRED** | Critical Control Point (CCP-1). High-speed pneumatic reject diverter detects $1.0\text{ mm}$ Fe, $1.2\text{ mm}$ NFe, $1.5\text{ mm}$ SS. |
| **14-Head Multihead Weigher & VFFS**| `PK-101` | **REQUIRED** | Automatic packaging of 1 kg and 2 kg pouches at 30-35 bpm with $\pm 1.5\text{ g}$ accuracy under Legal Metrology standards. |
| **Clean-In-Place Skid** | `CIP-101` | **REQUIRED** | 2-tank automated skid (warm caustic wash + hot water sanitization) for tanks, slurry pumps, and dewatering screens. |
| **Process Effluent Plant** | `ETP-101` | **REQUIRED** | Equalization, acid neutralization (pH 8.8 to 7.0), dual-media filtration, and clarifier to meet SPCB discharge standards. |
| **Ultrasound Contact Skid** | `US-101` | **REJECTED** | Literature (Vásquez 2021) shows ultrasound erodes seed coats. The target lot is already dehulled/split. CapEx ($>₹15\text{ Lakhs}$) is uneconomical. |
| **Flaking / Rolling Mills** | `FLK-101` | **REJECTED** | Literature (Sethi 2014) confirms flaked dal suffers severe cooking-time retrogradation (triples after 10 months) and turns rancid. Disqualified. |
| **Continuous Drag-Chain Contactor**| `CC-101` | **REJECTED** | Continuous drag flight contactors cause severe pulse breakage and attrition ($>6\%$ fines loss) compared to gentle fluid-bed suspension. |
