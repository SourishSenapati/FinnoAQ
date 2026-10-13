# HARAKUTIR MATHEMATICAL MODEL REGISTER & SCIENTIFIC CITATIONS
## Computational Hierarchy (Levels 1–5), Governing Equations & Validation Boundaries

**Document ID:** HKT-MOD-2026-004  
**Version:** 3.0.0  
**Implementation Modules:** `src/harakutir/hydration.py`, `src/harakutir/gpu_engine.py`, `src/harakutir/foodoscope.py`, `src/harakutir/digital_twin.py`  
**System System of Record:** Local Workspace (`toor_dal_optimization/`)  

---

## 1. Computational Model Hierarchy

The modeling architecture follows a progressive hierarchy of physical and computational fidelity:

```
[Level 1: Baseline Analytics & Regressions]
      |
      v
[Level 2: Empirical & Mechanistic Physics Models (Peleg Hydration, Arrhenius LOX)]
      |
      v
[Level 3: GPU-Accelerated Numerical PDE Solvers (Spherical Radial Diffusion on CUDA)]
      |
      v
[Level 4: Coupled Foodoscope Sensory-Nutritional Kinetics (Maillard vs Lysine)]
      |
      v
[Level 5: Integrated Industrial Process Simulation (5.0 T/hr Mass/Energy Balances)]
```

---

## 2. Model Register & Governing Equations

### Model M-01: Hyperbolic Hydration Kinetics (Peleg Model)
* **Model ID:** `MOD_HYDRATION_PELEG_01`
* **Governing Equation:**
  $$M(t) = M_0 + \frac{t}{k_1 + k_2 t}$$
* **Parameters:**
  - $M(t)$: Moisture content at time $t$ (% dry basis)
  - $M_0$: Initial moisture content (% dry basis)
  - $k_1$: Peleg initial hydration rate constant ($\text{min / \%}$)
  - $k_2$: Peleg capacity constant ($\%^{-1}$)
* **Derived Metrics:** Initial hydration rate $R_0 = 1/k_1$ (%/min); Equilibrium moisture $M_e = M_0 + 1/k_2$ (%).
* **Fitting Algorithm:** Non-Linear Least Squares (SciPy Levenberg-Marquardt) with 95% asymptotic confidence intervals and parameter covariance identifiability checks.
* **Code Implementation:** `src/harakutir/hydration.py::fit_peleg_model()`
* **Validation Status:** Numerically identified ($R^2 = 1.000$, $RMSE = 0.0022$ on benchmark test curve).

### Model M-02: GPU Spherical Fickian Moisture & Heat Diffusion Solver
* **Model ID:** `MOD_GPU_DIFFUSION_PDE_02`
* **Governing Equation:**
  $$\frac{\partial M}{\partial t} = \frac{1}{r^2} \frac{\partial}{\partial r}\left(r^2 D_{\text{eff}}(T) \frac{\partial M}{\partial r}\right), \quad D_{\text{eff}}(T) = D_0 \exp\left(-\frac{E_a}{R T}\right)$$
  $$\frac{\partial T}{\partial t} = \frac{\alpha_{\text{th}}}{r^2} \frac{\partial}{\partial r}\left(r^2 \frac{\partial T}{\partial r}\right)$$
* **Boundary Conditions:**
  - Radial symmetry at core: $\left.\frac{\partial M}{\partial r}\right|_{r=0} = 0$, $\left.\frac{\partial T}{\partial r}\right|_{r=0} = 0$
  - Surface saturation: $M(R, t) = M_{\text{eq}}$, $T(R, t) = T_{\text{ambient}}$
* **Analytical Fourier Solution on GPU:**
  $$M(r, t) = M_{\text{eq}} + (M_0 - M_{\text{eq}}) \frac{2 R}{\pi r} \sum_{n=1}^{K} \frac{(-1)^{n+1}}{n} \sin\left(\frac{n \pi r}{R}\right) \exp\left(-\frac{n^2 \pi^2 D_{\text{eff}} t}{R^2}\right)$$
* **Hardware Execution:** Vectorized tensor calculation running on NVIDIA GeForce RTX 4050 Laptop GPU (`cuda:0`).
* **Code Implementation:** `src/harakutir/gpu_engine.py::solve_coupled_radial_diffusion_pde()`
* **Performance:** Executes 50 shells $\times$ 60 modes in **$0.14\text{ seconds}$** on RTX 4050.

### Model M-03: Foodoscope Coupled Volatile & Nutrient Retention Kinetics
* **Model ID:** `MOD_FLAVOR_NUTRIENT_KIN_03`
* **Governing Equations:**
  1. *Lipoxygenase (LOX) Inactivation Kinetics:*
     $$\frac{d[\text{LOX}]}{dt} = -k_{\text{LOX}}(T) [\text{LOX}], \quad k_{\text{LOX}}(T) = 1.919 \exp\left(-\frac{65.0}{R}\left(\frac{1}{T} - \frac{1}{348.15}\right)\right)$$
  2. *Beany Off-Note Suppression Index (BOSI):*
     $$\text{BOSI} = 1.0 - \frac{[\text{Hexanal}]_t + 1.5 [\text{1-Octen-3-ol}]_t}{[\text{Hexanal}]_0 + 1.5 [\text{1-Octen-3-ol}]_0}$$
  3. *Available Lysine Degradation Kinetics:*
     $$\frac{d[\text{Lys}]}{dt} = -k_{\text{lys}}(T, M) [\text{Lys}], \quad k_{\text{lys}}(T) = 0.00025 \exp\left(-\frac{88.0}{R}\left(\frac{1}{T} - \frac{1}{373.15}\right)\right) \left(\frac{M}{12.0}\right)^{0.8}$$
* **Code Implementation:** `src/harakutir/foodoscope.py::simulate_thermal_flavor_and_nutrient_kinetics()`
* **Validation Boundary:** Validated for grain temperatures between $40^\circ\text{C}$ and $200^\circ\text{C}$, moisture $8\% - 30\%$.

### Model M-04: Industrial Scale Unit Operations Mass & Energy Balance
* **Model ID:** `MOD_SCALEUP_5TPH_04`
* **Governing Balances:**
  - Overall Mass: $\dot{m}_{\text{grain, in}} + \dot{m}_{\text{water, temper}} = \dot{m}_{\text{grain, out}} + \dot{m}_{\text{evap}} + \dot{m}_{\text{fines}}$
  - Specific Heat Duty:
    $$q_{\text{thermal}} = \frac{\dot{m}_{\text{grain}} C_p \Delta T + \dot{m}_{\text{evap}} L_v}{\eta_{\text{thermal}} \cdot \dot{m}_{\text{grain}}}$$
* **Code Implementation:** `src/harakutir/digital_twin.py::simulate_industrial_scale_unit_operations()`
* **Throughput Basis:** $5.0\text{ Tonnes/hour}$ continuous commercial line.

---

## 3. Assumptions and Uncertainties Register

| Item ID | Parameter / Assumption | Assumed Value / Range | Grounding Source | Sensitivity & Impact | Uncertainty Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **UNC-01** | Initial Cotyledon Diffusivity ($D_{\text{eff}}$) | $2.20 \times 10^{-11}\text{ m}^2/\text{s}$ ($\pm 0.5\times 10^{-11}$) | Inverse solver on test curve | HIGH: Explains 37.3% of cooking variance | `HIGH_PRIORITY_FOR_WET_LAB` |
| **UNC-02** | Pectin Degree of Esterification | $68.5\%$ ($\pm 5.0\%$) | Legume HTC literature | HIGH: Explains 36.9% of cooking variance | `HIGH_PRIORITY_FOR_WET_LAB` |
| **UNC-03** | Phytate-to-Calcium Molar Ratio | $1.65$ ($\pm 0.35$) | Pigeon pea literature | MEDIUM: Influences middle lamella gelation | `HIGH_PRIORITY_FOR_WET_LAB` |
| **UNC-04** | Natural Gas Thermal Efficiency ($\eta$) | $65.0\%$ | Industrial IR/Dryer specs | LOW: Direct OPEX varies by ₹0.04/kg | `ENGINEERING_ESTIMATE` |
| **UNC-05** | Cotyledon Thermal Diffusivity ($\alpha_{\text{th}}$) | $1.30 \times 10^{-7}\text{ m}^2/\text{s}$ | Food thermophysical tables | LOW: Grain reaches equilibrium in < 90 s | `LITERATURE_VERIFIED` |
| **UNC-06** | Commercial Arbitrage Price Spread | ₹19.65 / kg (₹98 - ₹78.35) | Indian APMC mandi averages | HIGH: Drives project payback period | `MARKET_BENCHMARK` |
