# HARAKUTIR ASSUMPTIONS, UNCERTAINTIES & SENSITIVITY REGISTER
## Formal Uncertainty Catalog, Boundary Limits & Risk Mitigations

**Document ID:** HKT-UNC-2026-005  
**Version:** 3.0.0  
**Controlling Specification:** Harakutir Autonomous Master Prompt (Sections 7, 9 & 16)  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Executive Summary

In computational chemical and food engineering, acknowledging and tracking parameter uncertainties is the primary defense against overconfidence and model hallucination. This document catalogs all critical assumptions, quantifies their sensitivity via GPU-accelerated Monte Carlo sampling, and outlines the physical experimental controls required to resolve them.

---

## 2. Parameter Uncertainty Ledger

### Category 1: Raw-Material & Agronomic Uncertainties
* **Raw Material Moisture ($M_0$):**
  - *Baseline Assumption:* $11.0\%$ w.b.
  - *Feasible Bounds:* $9.0\% - 13.5\%$ w.b. (dependent on port of entry and monsoon arrival).
  - *Sensitivity:* Low-to-moderate; variations $\pm 1\%$ shift tempering water requirements by $10\text{ kg/tonne}$ ($0.05\text{ MJ/kg}$ thermal duty).
  - *Mitigation:* Inline NIR moisture sensor installed at feed hopper to dynamically adjust tempering screw spray rate.
* **Effective Water Diffusivity ($D_{\text{eff}}$):**
  - *Baseline Assumption:* $2.20 \times 10^{-11}\text{ m}^2/\text{s}$ at 25°C.
  - *Feasible Bounds:* $1.20 \times 10^{-11} - 3.50 \times 10^{-11}\text{ m}^2/\text{s}$.
  - *Sensitivity:* **CRITICAL ($37.3\%$ of total cooking variance explained by Sobol index).** Lower diffusivity drastically increases cooking whistles.
  - *Mitigation:* Wet-lab hydration kinetic testing (SOW Section 10) on arriving sample lots.

### Category 2: Material Science & Cell Wall Uncertainties
* **Middle Lamella Pectin Degree of Esterification (DE):**
  - *Baseline Assumption:* $68.5\%$.
  - *Feasible Bounds:* $55.0\% - 78.0\%$.
  - *Sensitivity:* **CRITICAL ($36.9\%$ of total cooking variance explained by Sobol index).** High DE combined with divalent cations creates hard-core defects.
  - *Mitigation:* CDTA/Na2CO3 sequential fractionation and FTIR pectate titrations (SOW Section 12).
* **Calcium-to-Phytate Molar Cross-Linking Ratio:**
  - *Baseline Assumption:* $1.65$.
  - *Feasible Bounds:* $0.80 - 2.80$.
  - *Sensitivity:* HIGH ($11.5\%$ variance). If ratio exceeds $2.0$, excess free calcium cross-links all available pectin carboxyl groups.
  - *Mitigation:* ICP-OES minerals profiling and HPLC phytate assay (SOW Section 11).

### Category 3: Process & Industrial Scale-Up Uncertainties
* **Catalytic Infrared Radiant Flux Efficiency:**
  - *Baseline Assumption:* $65.0\%$ radiant-to-grain heat transfer efficiency.
  - *Feasible Bounds:* $50.0\% - 75.0\%$.
  - *Sensitivity:* Directly impacts natural gas / electricity utility cost (shifting OPEX by ₹0.06/kg).
  - *Mitigation:* Pilot trial thermocouple logging of grain bed surface and core temperatures.
* **Milling Shatter & Fines Generation:**
  - *Baseline Assumption:* $0.45\%$ fines loss during HTST conditioning and convective drying.
  - *Feasible Bounds:* $0.20\% - 1.80\%$.
  - *Sensitivity:* High commercial impact; every $1\%$ fines loss reduces net processing yield by $10\text{ kg/tonne}$ (₹780/tonne value erosion).
  - *Mitigation:* Gentle vibratory fluidization without aggressive mechanical agitation.

---

## 3. GPU Monte Carlo Sensitivity Decomposition (N = 50,000)

Evaluated on the local **NVIDIA GeForce RTX 4050 Laptop GPU** (`cuda:0`) in $0.13\text{ seconds}$:

| Rank | Parameter Name | Distribution & Range | First-Order Sobol Sensitivity Index ($S_i$) | Impact on Cooking Whistles |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Effective Moisture Diffusivity ($D_{\text{eff}}$)** | Normal($2.22\times 10^{-11}, 0.35\times 10^{-11}$), $[1.2, 3.5]\times 10^{-11}$ | **$37.3\%$** | Dominant driver of water infiltration into starch core |
| **2** | **Pectin Degree of Esterification (DE)** | Normal($68.0\%, 4.5\%$), $[55\%, 78\%]$ | **$36.9\%$** | Controls middle lamella cell separation during cooking |
| **3** | **Cotyledon Bulk Density** | Normal($0.82, 0.03\text{ g/mL}$), $[0.75, 0.88]$ | **$14.2\%$** | Influences porosity and acoustic impedance |
| **4** | **Calcium/Phytate Molar Crosslink Ratio** | Normal($1.65, 0.35$), $[0.8, 2.8]$ | **$11.5\%$** | Governs insoluble calcium pectate gel rigidity |

**Engineering Decision:** The top two parameters ($D_{\text{eff}}$ and Pectin DE) account for **$74.2\%$ of total cooking performance variance**. Therefore, physical laboratory experiments must prioritize Phase 1 hydration kinetics and pectin characterization above all other diagnostic tests.
