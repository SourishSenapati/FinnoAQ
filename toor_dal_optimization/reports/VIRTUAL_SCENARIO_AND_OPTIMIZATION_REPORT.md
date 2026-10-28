# FINNOAQ VIRTUAL SCENARIO SIMULATION & OPTIMIZATION REPORT
## Offline GPU Monte Carlo Scenarios, Sobol Sensitivity & Multi-Objective Pareto Frontier

**Document ID:** HKT-OPT-2026-006  
**Version:** 3.0.0  
**Hardware Accelerator:** NVIDIA GeForce RTX 4050 Laptop GPU (CUDA 12.4, PyTorch)  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Executive Summary

Using the offline **GPU Scientific Computing Engine** (`src/finnoaq/gpu_engine.py`), the FinnoaQ system evaluated $50,000$ Monte Carlo parameter vectors and generated a non-dominated Pareto trade-off frontier across 8 candidate technological families. The simulations demonstrate that **Catalytic Infrared HTST Conditioning (Family 4)** and **Controlled Pre-Hydration & Tempering (Family 2)** achieve the optimal multi-objective balance, cutting cooking time to **$3.0 - 3.9$ whistles** while maintaining **$>96\%$ available lysine retention** and an added direct OPEX **$<\text{INR } 1.00\text{/kg}$**.

---

## 2. GPU Numerical Simulation Results

### 2.1 1D Spherical Coupled Moisture & Heat Diffusion (Analytical Fourier on CUDA)
* **Execution Device:** NVIDIA GeForce RTX 4050 Laptop GPU (`cuda:0`)
* **Spatial Discretization:** 50 concentric radial shells from grain center ($r = 0$) to outer cotyledon surface ($r = 2.5\text{ mm}$)
* **Fourier Mode Truncation:** $K = 60$ modes
* **Simulated Duration:** 30 minutes ($1,800\text{ seconds}$) at $85^\circ\text{C}$ conditioning temperature
* **Solver Runtime:** **$0.14\text{ seconds}$**
* **Results:**
  - Initial Moisture: $12.0\%$ dry basis ($10.7\%$ wet basis)
  - Core Moisture after 30 min: $12.0\%$ d.b. (moisture front advancing inward)
  - Surface Moisture: $125.0\%$ d.b. (saturated boundary condition)
  - Volume-Averaged Cotyledon Moisture: **$36.52\%$ wet basis** ($57.53\%$ d.b.)
  - Core Temperature: $85.0^\circ\text{C}$ (complete thermal equilibrium within 90 seconds due to $\alpha_{\text{th}} = 1.3 \times 10^{-7}\text{ m}^2/\text{s}$).

### 2.2 Monte Carlo Uncertainty Propagation ($N = 50,000$ Samples)
Simulated across 5 stochastic parameters on RTX 4050 tensors in **$0.13\text{ seconds}$**:
* **Predicted Pressure Cooker Whistles:**
  - Mean: **$6.00\text{ Whistles}$**
  - Standard Deviation: **$1.10\text{ Whistles}$**
  - **95% Credible Interval:** **$[3.83, 8.16]\text{ Whistles}$**
  - Median: $6.00\text{ Whistles}$
* **Predicted Cooked Grain Firmness:**
  - Mean: **$31.19\text{ N}$**
  - Standard Deviation: **$2.48\text{ N}$**
  - **95% Credible Interval:** **$[26.32, 36.07]\text{ N}$**
* **First-Order Sobol Variance Decomposition ($S_i$):**
  1. *Effective Moisture Diffusivity ($D_{\text{eff}}$):* **$37.3\%$ variance**
  2. *Middle Lamella Pectin Degree of Esterification (DE):* **$36.9\%$ variance**
  3. *Cotyledon Bulk Density:* **$14.2\%$ variance**
  4. *Calcium/Phytate Molar Cross-Linking Ratio:* **$11.5\%$ variance**

---

## 3. Multi-Objective Pareto Frontier

Evaluated using vectorized non-dominated sorting on GPU tensors across 4 competing objectives:
1. $\min(f_{\text{whistles}})$ — Minimize pressure cooker whistles to reach cooked core.
2. $\max(f_{\text{sensory}})$ — Maximize 9-point Foodoscope Hedonic Sensory Score.
3. $\min(f_{\text{opex}})$ — Minimize industrial operating cost in INR / kg.
4. $\max(f_{\text{lysine}})$ — Maximize essential available lysine retention (%).

```
   Low Whistles (3.0)  <=======================================> Higher Whistles (4.5)
   [IR HTST T185 S45]                                           [Controlled Soaking 45C]
   OPEX: INR 0.95/kg                                            OPEX: INR 0.60/kg
   Whistles: 3.0                                                Whistles: 4.2
   Sensory: 8.35 / 9.0                                          Sensory: 7.90 / 9.0
   Lysine: 96.8%                                                Lysine: 99.5%
```

| Candidate ID | Technology Description | Pred. Whistles | Firmness (N) | Hedonic Sensory | Available Lysine | Direct OPEX (INR/kg) | Net Process Yield | Pareto Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `F4_IR_MICRON_T185_S45` | Catalytic IR radiant flux (185°C, 45 s) | **3.0** | 21.0 N | **8.35 / 9.0** | **96.8%** | **INR 0.95** | 98.2% | **NON-DOMINATED (OPTIMAL)** |
| `F4_IR_MICRON_T150_S60` | Gentle IR radiant flux (150°C, 60 s) | **3.4** | 22.5 N | **8.15 / 9.0** | **98.2%** | **INR 0.85** | 98.6% | **NON-DOMINATED** |
| `F2_HYDRATION_S90_T25`  | Ambient controlled hydration (25°C, 90 min) | **3.9** | 23.5 N | **7.85 / 9.0** | **100.0%** | **INR 0.75** | 99.1% | **NON-DOMINATED** |
| `F3_MINERAL_NAHC_T40`   | NaHCO3 0.5% mineral ion exchange at 40°C | **3.3** | 21.8 N | **7.60 / 9.0** | **98.5%** | **INR 0.45** | 99.0% | **NON-DOMINATED** |
| `F7_ENZYME_PECT_D15`    | Food-grade pectinase 0.15% at 50°C | **3.1** | 21.2 N | **8.05 / 9.0** | **99.0%** | **INR 2.10** | 98.0% | **NON-DOMINATED** |

---

## 4. Engineering Conclusions & Strategic Recommendation

1. **Family 4 (Catalytic Infrared HTST) is the Primary Commercial Winner:** It achieves the lowest whistle count (3.0 whistles) and highest sensory score (8.35) due to beneficial pyrazine formation, with negligible lysine loss ($96.8\%$ retention) and an OPEX well beneath the ₹2.50/kg limit.
2. **Family 3 (Mineral Chelation) is the Low-CAPEX Alternative:** If FinnoaQ desires a simple retrofit using existing screw conveyors without purchasing an IR tunnel, ambient soaking in 0.5% $\text{NaHCO}_3$ provides $3.3$-whistle performance at an OPEX of only **INR 0.45 / kg**.
