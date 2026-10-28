# FINNOAQ PRODUCT REQUIREMENTS DOCUMENT (PRD)
## Quick-Cooking Split Toor Dal (*Cajanus cajan*) — Product Specifications & Client Acceptance Boundaries

**Document ID:** HKT-PRD-2026-001  
**Version:** 3.0.0  
**Governing SOW:** Phase 1 Diagnostic Scope (`Phase1_Scope_of_Work_Toor_Dal.docx`)  
**Target Format:** Shelf-Stable Dry Split Toor Dal (*Skinned & Split Cotyledons*)  
**Target Market:** Indian Domestic Consumer & Foodservice Retail (FSSAI Regulated)  
**Status:** PROVISIONAL WORKING ASSUMPTION — REQUIRES FORMAL CLIENT SIGN-OFF  

---

## 1. Product Concept & Foundational Assumptions

### 1.1 Core Working Hypothesis
The intended commercial product is a **shelf-stable, dry split toor dal product** derived from imported Tanzanian grain that:
1. Reaches cooked tenderness comparable to premium Indian benchmark dal in **$\le 3.5$ standard pressure-cooker whistles** (compared to ~6 whistles for untreated Tanzanian dal).
2. Preserves authentic cotyledon integrity, rich yellow appearance, creamy mouthfeel, and nutty roasted aroma without slurring or disintegrating into thin soup.
3. Retains $\ge 95\%$ of essential nutritional density (specifically available lysine and protein solubility).
4. Operates within an added industrial processing OPEX $\le \text{INR } 2.50\text{/kg}$.
5. Strictly complies with FSSAI standards for dry pulses (moisture $\le 14.0\%$, water activity $a_w \le 0.65$).

### 1.2 Out-of-Scope Formats (Excluded)
This engineering programme **does not silently convert** into an instant, pre-cooked, ready-to-eat (RTE), retort-pouched, canned, or extruded snack project. Any transition to pre-gelatinized instant dal or wet retort packaging represents a fundamentally different thermodynamic and capital architecture and requires a separate Scope of Work.

---

## 2. Configurable Product Requirements Matrix

| Requirement | Purpose & Definition | Measurement Method | Unit | Acceptance Threshold | Criticality | Verification Stage | Responsible Reviewer | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Cooking Performance** | Primary consumer metric; whistles and time to reach cooked core tenderness | Standard 5L pressure cooker test (1:4 dal-to-water ratio) + Mattson cooker | Whistles / Minutes | **$\le 3.5$ Whistles** (or $\le 18.0\text{ min}$) | CRITICAL | Stage 06 / Gate G5 | Food Processing Specialist | `TBD_CLIENT_APPROVAL` |
| **Cooked Texture** | Tenderness, firmness, and mouthfeel of cooked grains | Texture Profile Analysis (TA.XT Plus, 50% compression, 75mm plate) | Newtons (N) | **$20.0 - 24.0\text{ N}$** (Indian benchmark parity) | CRITICAL | Stage 06 / Gate G5 | Food Rheologist | `TBD_CLIENT_APPROVAL` |
| **Hard-Core Percentage** | Proportion of grains with ungelatinized, hard, or gritty cores after cooking | Tactile glass-plate squash test (100 grains, ISO 5670 adapted) | Percentage (%) | **$0.0\%$** (Zero hard cores permissible) | HIGH | Stage 06 / Gate G5 | Sensory Analyst | `TBD_CLIENT_APPROVAL` |
| **Raw-Material Tolerance** | Robust performance across varied crop years, moisture levels, and import lots | Multi-lot testing across $\ge 3$ independent commercial Tanzanian import lots | Ratio / Delta | Cooking time delta across lots $\le \pm 10\%$ | HIGH | Stage 06 / Gate G5 | Agronomic Lead | `TBD_CLIENT_APPROVAL` |
| **Nutritional Quality** | Preservation of essential amino acids and digestible protein content | Available lysine via FDNB method (AOAC 975.44); crude protein (Kjeldahl) | % retention / % dry basis | Available Lysine $\ge 90.0\%$ retention; Protein $\ge 21.0\%$ | MEDIUM | Stage 08 / Gate G7 | Nutritional Chemist | `TBD_CLIENT_APPROVAL` |
| **Sensory Quality** | Color, aroma, absence of beany off-notes, broth viscosity | 9-Point Hedonic Sensory Panel + Foodoscope GC-MS aroma profiling | Hedonic Score (1–9) | **$\ge 7.8 / 9.0$** (Indian Desi Dal parity; BOSI $\ge 0.70$) | HIGH | Stage 06 / Gate G5 | Sensory Panel Head | `TBD_CLIENT_APPROVAL` |
| **Shelf Stability** | Storage longevity under ambient tropical storage without re-hardening (HTC) | Accelerated storage testing (40°C, 75% RH for 6 months, IS 4333) | Months | **$\ge 12\text{ Months}$** without cooking time drift $> 10\%$ | HIGH | Stage 09 / Gate G8 | Packaging Engineer | `TBD_CLIENT_APPROVAL` |
| **Processability** | Grain flowability, resistance to splitting during conditioning and packaging | Angle of repose; friability index; shatter resistance (drum test) | Fines (%) / Degrees (°) | Fines generated during packing $\le 0.5\%$; Angle $\le 32^\circ$ | MEDIUM | Stage 07 / Gate G6 | Process Engineer | `TBD_CLIENT_APPROVAL` |
| **Milling Yield** | Finished saleable quick-cooking dal output per unit raw split input | Mass balance scale measurement across continuous conditioning line | Percentage (%) | **$\ge 98.0\%$** net finished yield | HIGH | Stage 07 / Gate G6 | Milling Operations Lead | `TBD_CLIENT_APPROVAL` |
| **Resource Consumption** | Specific thermal energy, electrical load, and process water addition | Utility power meters; steam flow meters; water mass meters | MJ/kg & kWh/Tonne | Thermal $\le 0.50\text{ MJ/kg}$; Electrical $\le 12\text{ kWh/T}$ | MEDIUM | Stage 07 / Gate G6 | Energy Auditor | `TBD_CLIENT_APPROVAL` |
| **Unit Economics** | Direct incremental operating expenditure to treat raw imported dal | Techno-economic cost model incorporating energy, water, labor, Capex amort. | INR / kg | **$\le \text{INR } 2.50\text{ / kg}$** (Target: $\le \text{INR } 1.00\text{/kg}$) | CRITICAL | Stage 10 / Gate G8 | Financial Strategist | `TBD_CLIENT_APPROVAL` |
| **Food Safety** | Microbiological and chemical safety; absence of mycotoxins and pathogens | ISO/FSSAI accredited lab assays (Aflatoxin HPLC, plate counts) | cfu/g & ppb | Total plate count $< 10^4\text{ cfu/g}$; Aflatoxin B1 $< 10\text{ ppb}$ | CRITICAL | Stage 09 / Gate G8 | Food Safety Officer | `TBD_CLIENT_APPROVAL` |
| **Regulatory Compliance**| Compliance with FSSAI regulations for dry pulses and packaging | FSSAI Food Safety and Standards (Food Products Standards) Reg. 2011 | Categorical | 100% compliant with pulse standards; permitted additives only | CRITICAL | Stage 09 / Gate G8 | Regulatory Counsel | `TBD_CLIENT_APPROVAL` |

---

## 3. Client Sign-Off & Specification Freezing

* **Client Commercial Sponsor:** FinnoaQ Management  
* **Technical Lead Reviewer:** FinnoaQ Autonomous R&D Team  
* **Approval Date:** `PENDING_CLIENT_FORMAL_GATE_REVIEW`  
* **Formal Decision Boundary:** All numerical thresholds marked `TBD_CLIENT_APPROVAL` will remain provisional design targets until FinnoaQ formally signs Gate G0/G1 authorization.
