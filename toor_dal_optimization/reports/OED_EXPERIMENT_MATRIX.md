# FINNOAQ BAYESIAN OPTIMAL EXPERIMENTAL DESIGN (OED) MATRIX
## Sequential DoE Protocol, Hypothesis Discrimination (H1–H5) & Sample Allocation

**Document ID:** HKT-OED-2026-008  
**Version:** 3.0.0  
**Implementation:** `src/finnoaq/oed.py`  
**Commercial Ceiling:** ₹2,00,000 + GST (Estimated Execution Cost: **₹70,000.00**)  
**Sample Allocation:** 14.5 kg Tanzanian Dal (from 25 kg lot) + 6.0 kg Indian Benchmark  

---

## 1. Experimental Objective & Hypotheses Under Discrimination

The experimental plan is designed to maximize expected mutual information gain between physical laboratory assays and 5 competing diagnostic hypotheses:
* **$H_1$ (Hydration Diffusion Barrier):** Slower cooking is driven by reduced cotyledon water permeability ($D_{\text{eff}} < 2.5 \times 10^{-11}\text{ m}^2/\text{s}$).
* **$H_2$ (Middle Lamella Insoluble Pectate Gels):** Slower cooking is caused by calcium/magnesium cross-linking of de-esterified pectins.
* **$H_3$ (Starch Gelatinization Thermal Shift):** High DSC gelatinization enthalpy ($\Delta H > 15\text{ J/g}$) or elevated peak temperature ($T_{\text{peak}} > 80^\circ\text{C}$).
* **$H_4$ (Cotyledon Morphological Density & Cell Wall Thickness):** Structural barriers prevent hot water penetration.
* **$H_5$ (Agronomic Storage-Induced HTC Defect):** Extended high-temp/high-humidity maritime transport induced phytase activation.

---

## 2. Sequential 14-Run Optimal Experimental Design Matrix

| Run # | Experimental Block | Sample Type | Treatment / Conditioning Setting | Primary Assay & Endpoint | Sample Qty (g) | Replicates | Target Hypothesis | Estimated Cost (INR) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **R-01** | Baseline Controls | Indian Benchmark | None (Raw Baseline) | 5L Pressure Cooker (Whistle count) + Texture Firmness | 500 g | 3 | Baseline Benchmark | ₹3,000 |
| **R-02** | Baseline Controls | Tanzanian Dal | None (Raw Baseline) | 5L Pressure Cooker (Whistle count) + Texture Firmness | 500 g | 3 | Problem Statement | ₹3,000 |
| **R-03** | Diagnostic Kinetics| Indian Benchmark | Soaking in DI Water (25°C, 0–480 min) | Peleg Hydration Curve ($k_1, k_2, D_{\text{eff}}$) | 1,000 g | 3 | $H_1$ Discrimination | ₹5,000 |
| **R-04** | Diagnostic Kinetics| Tanzanian Dal | Soaking in DI Water (25°C, 0–480 min) | Peleg Hydration Curve ($k_1, k_2, D_{\text{eff}}$) | 1,000 g | 3 | $H_1$ Discrimination | ₹5,000 |
| **R-05** | Cell Wall / Pectin | Tanzanian Dal | CDTA / Na2CO3 Pectin Extraction | Soluble vs Insoluble Pectin Fractionation (FTIR DE%) | 250 g | 2 | $H_2$ Discrimination | ₹8,000 |
| **R-06** | Minerals & Phytate | Tanzanian vs Indian | Total Digestion (ICP-OES + Wade Reagent) | Ca, Mg, Phytate molar cross-linking ratio | 250 g | 2 | $H_2 / H_5$ Discrimination| ₹8,000 |
| **R-07** | Thermal Transitions| Tanzanian vs Indian | DSC Micro-calorimetry (30°C–110°C) | Gelatinization $T_{\text{onset}}, T_{\text{peak}}, \Delta H$ | 100 g | 2 | $H_3$ Discrimination | ₹6,000 |
| **R-08** | Treatment Trial 1 | Tanzanian Dal | Ambient Pre-Hydration (25°C, 90 min) + Dry | Pressure Cooker Whistles + Texture Analysis | 1,000 g | 3 | Candidate F2 Validation | ₹4,500 |
| **R-09** | Treatment Trial 2 | Tanzanian Dal | Warm Pre-Hydration (45°C, 45 min) + Dry | Pressure Cooker Whistles + Texture Analysis | 1,000 g | 3 | Candidate F2 Validation | ₹4,500 |
| **R-10** | Treatment Trial 3 | Tanzanian Dal | NaHCO3 0.5% Chelation (40°C, 30 min) + Dry| Pressure Cooker Whistles + Texture Analysis | 1,000 g | 3 | Candidate F3 Validation | ₹5,500 |
| **R-11** | Treatment Trial 4 | Tanzanian Dal | Catalytic IR HTST (150°C, 60 s) + Dry | Pressure Cooker Whistles + Texture Analysis | 1,500 g | 3 | Candidate F4 Validation | ₹7,500 |
| **R-12** | Treatment Trial 5 | Tanzanian Dal | Catalytic IR HTST (185°C, 45 s) + Dry | Pressure Cooker Whistles + Texture Analysis | 1,500 g | 3 | Candidate F4 Validation | ₹7,500 |
| **R-13** | Sensory & Culinary | Leading Prototype | Sambar Broth Matrix (pH 4.1, Tamarind) | Whistles + Hard-Core Squash Test | 500 g | 3 | Culinary Validation | ₹3,500 |
| **R-14** | Independent Re-test| Fresh Tanzanian Lot | Leading Candidate Setting (IR 185°C) | Independent Confirmation on Fresh Material | 1,000 g | 3 | Stage Gate Confirmation | ₹4,000 |

---

## 3. Budget Summary & Sample Inventory Reconciliation

* **Total Estimated Physical Laboratory Cost:** **INR 70,000.00**  
* **SOW Commercial Ceiling:** **INR 2,00,000.00**  
* **Budget Safety Margin:** **₹1,30,000.00 remaining** (plenty of reserve for re-tests or expanded replicates).  
* **Tanzanian Material Allocated:** $10,600\text{ g}$ ($10.6\text{ kg}$) of available $25.0\text{ kg}$ sample lot.  
* **Indian Benchmark Material Allocated:** $2,250\text{ g}$ ($2.25\text{ kg}$) of available $10.0\text{ kg}$ sample lot.
