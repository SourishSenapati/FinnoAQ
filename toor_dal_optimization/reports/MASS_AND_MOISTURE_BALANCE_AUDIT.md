# Mass & Moisture Balance Audit & Reconciliation Report

**Project Reference:** FNQ-PR-2026-001 | Phase 1 Diagnostic R&D Study  
**Lead Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Document Ref:** FNQ-REP-BAL-001  
**Date:** 20 October 2026  
**Governing Standard:** Section 4 (Criticism B) — First-Principles Mass Balance Reconciliation  

---

## 1. Executive Summary & Audit Mandate

This report provides an independent, first-principles mathematical recalculation and audit of all stream mass, moisture, and energy balances for the conceptual 15,000 kg/day Toor Dal processing facility. 

The audit explicitly resolves the discrepancy between the two competing dryer evaporation figures reported in earlier drafts (**3,678 kg/day vs. 3,878 kg/day**) and traces the **199.7 kg/day water delta** to inconsistent pre-dryer moisture assumptions. Both scenarios are modeled side by side with unrounded decimal precision ($0.000000\%$ closure error) to ensure that preliminary equipment sizing remains transparent and auditable.

---

## 2. Capacity Basis & Upstream Stream Balances

A capacity statement of `15,000 kg/day` must be defined with exact stream boundaries. In this facility concept, the capacity basis is **incoming as-received raw split dal at 10.5% wet-basis moisture**:

```text
========================================================================================================
STREAM 01: INCOMING RAW GRAIN BASIS
========================================================================================================
Parameter                           Symbol          Equation / Derivation                   Value
--------------------------------------------------------------------------------------------------------
Total Raw Feed Mass                 M_feed          Design capacity basis                   15,000.000 kg/day
Incoming Moisture (Wet Basis)       X_wb,in         Typical commercial import certificate   10.5000% w/w
Incoming Moisture (Dry Basis)       X_db,in         X_wb / (1 - X_wb) = 0.105 / 0.895       11.7318% d.b.
Incoming Dry Solids Mass            M_ds,in         M_feed * (1 - X_wb,in) = 15000 * 0.895  13,425.000 kg/day
Incoming Intrinsic Water Mass       M_w,in          M_feed * X_wb,in = 15000 * 0.105         1,575.000 kg/day
========================================================================================================
```

### 2.1 Dry Solids Loss Audit (184 kg/day vs. 196 kg/day)
Earlier documents contained two competing solids loss assumptions during soaking, washing, and mechanical dewatering:
1. **Reported Constant Loss of 184.000 kg/day:**
   - Absolute dry solids loss: $L_{\text{ds}} = 184.000\text{ kg/day}$.
   - Fractional dry solids loss: $184.000 / 13,425.000 = 1.370577\%$ (approx. $1.3706\%$).
   - Net dry solids reaching dryer: $13,425.000 - 184.000 = \mathbf{13{,}241.000\text{ kg/day}}$.
2. **Alternate Percentage Loss of 1.46% (from literature wash benchmarks):**
   - Implied solids loss: $13,425.000 \times 0.014600 = 196.005\text{ kg/day}$.
   - Net dry solids remaining: $13,425.000 - 196.005 = 13,228.995\text{ kg/day}$.
   - Arithmetic delta: $196.005 - 184.000 = 12.005\text{ kg/day}$.
3. **Reconciliation Verdict:** The documented figure of **13,241.000 kg/day dry solids** is adopted as the reference baseline across all subsequent unit operations.

---

## 3. Final Dried Product Mass Balance

Commercial pigeon pea product is dried to **10.0% wet-basis moisture** ($X_{\text{wb,prod}} = 0.1000$) to guarantee microbiological stability and prevent mold proliferation in ambient storage (FSSAI statutory ceiling is $14.0\%$):

```text
========================================================================================================
STREAM 06: FINAL DRIED PRODUCT SPECIFICATION
========================================================================================================
Parameter                           Symbol          Equation / Derivation                   Value
--------------------------------------------------------------------------------------------------------
Target Finished Moisture (WB)       X_wb,prod       Target commercial moisture              10.0000% w/w
Target Finished Moisture (DB)       X_db,prod       X_wb / (1 - X_wb) = 0.100 / 0.900       11.1111% d.b.
Finished Product Dry Solids         M_ds,prod       Conserved solids (M_ds,net)             13,241.000 kg/day
Total Finished Product Mass         M_prod          M_ds,prod / (1 - X_wb,prod)             14,712.222 kg/day
Finished Product Water Content      M_w,prod        M_prod * X_wb,prod                      1,471.222 kg/day
Daily Packaging Output (1 kg bags)  N_packs         14,712.222 / 1.000                      14,712 units/day
========================================================================================================
```

---

## 4. Reconciled Pre-Dryer & Evaporation Scenarios (Finding B)

Because the physical drainage and surface liquid film retention of the soaked target Tanzanian dal have not yet been measured in a laboratory dewatering screen, two competing pre-dryer scenarios exist in the project records:

### 4.1 Side-by-Side Mathematical Comparison

| Stream Parameter | Parameter Description | Scenario B1 (True 28.0% WB) | Scenario B2 (Reported 18,590 kg) | Arithmetic Difference ($\Delta$) | Impact on Design |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **$M_{\text{dryer,in}}$** | Pre-Dryer Wet Feed Mass | **18,390.278 kg/day** | **18,590.000 kg/day** | **+199.722 kg/day** (+1.09%) | Feed hopper & feeder sizing |
| **$M_{\text{ds,dryer}}$** | Pre-Dryer Dry Solids Mass | 13,241.000 kg/day | 13,241.000 kg/day | 0.000 kg/day | Conserved solids basis |
| **$M_{\text{w,dryer,in}}$** | Pre-Dryer Water Mass | 5,149.278 kg/day | 5,349.000 kg/day | +199.722 kg/day | Liquid load entering dryer |
| **$X_{\text{wb,dryer}}$** | Pre-Dryer Moisture (Wet Basis) | **28.0000% w/w** | **28.7735% w/w** | **+0.7735% w/w** | Mathematical source of error |
| **$X_{\text{db,dryer}}$** | Pre-Dryer Moisture (Dry Basis) | 38.8889% d.b. | 40.3973% d.b. | +1.5084% d.b. | Drying kinetics driving force |
| **$M_{\text{prod}}$** | Final Product Mass (10% WB) | 14,712.222 kg/day | 14,712.222 kg/day | 0.000 kg/day | Conserved product mass |
| **$M_{\text{w,prod}}$** | Final Product Water Mass | 1,471.222 kg/day | 1,471.222 kg/day | 0.000 kg/day | Conserved residual water |
| **$\dot{m}_{\text{evap}}$** | **Total Daily Water Evaporated** | **3,678.056 kg/day** | **3,877.778 kg/day** | **+199.722 kg/day** (+5.43%) | **Core Review Discrepancy** |
| $\dot{m}_{\text{evap,h}}$ | Hourly Evaporation (20 h/day) | 183.903 kg/h | 193.889 kg/h | +9.986 kg/h (+5.43%) | Dryer exhaust airflow sizing |
| $Q_{\text{th,latent}}$ | Latent Heat Duty ($\lambda=2400\text{ kJ/kg}$) | 122.602 kW_th | 129.259 kW_th | +6.657 kW_th (+5.43%) | Heating coil duty |
| $\dot{m}_{\text{steam}}$ | Saturated Steam Duty (3.0 bar) | 226.7 kg/h | 239.0 kg/h | +12.3 kg/h (+5.43%) | Boiler steam capacity requirement |

---

## 5. Root Cause of the 199.7 kg/day Discrepancy

1. **The Origin:** In preliminary engineering sketches, an author added an arbitrary **~200 kg/day surface liquid allowance** (undrained surface water film) to the calculated wet mass ($18,390.28\text{ kg} \to 18,590.00\text{ kg}$).
2. **The Defect:** When reporting the $18,590\text{ kg/day}$ stream, the author copied the label **"28.0% moisture"** from the earlier calculation without recalculating the ratio.
3. **The Proof:**
   $$\text{Moisture} = \frac{18{,}590 - 13{,}241}{18{,}590} = \frac{5{,}349}{18{,}590} = \mathbf{28.7735\%}$$
   An inlet mass of $18,590\text{ kg/day}$ with $13,241\text{ kg/day}$ dry solids represents **28.77% moisture, NOT 28.00%**.
4. **Engineering Disposition:** Both numbers are preserved in this audit. The parameter is classified as `UNRESOLVED — EMPIRICAL SOAK DRAINAGE TEST REQUIRED`. Final dryer surface area and blower motor sizing will be held provisional until bench-scale dewatering sieve trials determine actual moisture after 5 minutes of drainage.

---

## 6. Overall Mass Balance Closure & Verification

For both scenarios, overall mass balance closure is verified to six decimal places:

```text
========================================================================================================
MASS BALANCE CLOSURE AUDIT (SCENARIO B1: 28.0000% WB)
========================================================================================================
Input Streams:
  Pre-Dryer Wet Feed (Stream 05)                     = 18,390.277778 kg/day
Output Streams:
  Dried Finished Dal (Stream 06)                     = 14,712.222222 kg/day
  Dryer Water Vapor Loss (Stream 07)                 =  3,678.055556 kg/day
  Total Output (Stream 06 + 07)                      = 18,390.277778 kg/day
Balance Closure Delta                                =      0.000000 kg/day
Percentage Closure Error                             =      0.000000 % (EXACT 100.0% CONSERVATION)
========================================================================================================
```

```text
========================================================================================================
MASS BALANCE CLOSURE AUDIT (SCENARIO B2: 28.7735% WB)
========================================================================================================
Input Streams:
  Pre-Dryer Wet Feed (Stream 05)                     = 18,590.000000 kg/day
Output Streams:
  Dried Finished Dal (Stream 06)                     = 14,712.222222 kg/day
  Dryer Water Vapor Loss (Stream 07)                 =  3,877.777778 kg/day
  Total Output (Stream 06 + 07)                      = 18,590.000000 kg/day
Balance Closure Delta                                =      0.000000 kg/day
Percentage Closure Error                             =      0.000000 % (EXACT 100.0% CONSERVATION)
========================================================================================================
```
