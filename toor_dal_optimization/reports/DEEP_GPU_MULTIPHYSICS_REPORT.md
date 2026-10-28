# FINNOAQ DEEP GPU MULTI-PHYSICS SIMULATION REPORT

**Project Reference:** FNQ-PR-2026-001 | Toor Dal Cooking-Time Optimization  
**Lead Chemical and Process Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Execution Device:** NVIDIA GeForce RTX 4050 Laptop GPU (`cuda:0`)  
**Simulation Scale:** 50,000 Full Grain Spatial PDE Solves (20 Batches x 2,500 Grains)  
**Runtime:** 22.23 seconds (2,249.0 grains/second)  
**Governing Rule:** AGENTS.md Rule 1 (Zero Synthetic Mocks, Genuine PDE Integration)  
**Epistemic Classification:** `CONDITIONAL_IN_SILICO_PREDICTION_PENDING_PHYSICAL_LOT_INTAKE`  

---

## 1. Executive Summary & Verification Verdict

The multi-physics GPU simulation completed **50,000** full-grain coupled PDE solves on the discrete NVIDIA RTX 4050 GPU.  
- **Cooking Time Target ($T_{90} \le 18.70\,\text{min}$):** Achieved mean **7.57 min** with standard deviation **0.0080 min**.
- **Process Capability ($C_{pk}$):** **465.026** (Conditional Sigma Level: **1395.08 Sigma**).
- **Finished Sodium ($[\text{Na}] \le 150\,\text{mg/100g}$):** Mean **10.4 mg/100g** (99th percentile: 12.4 mg/100g).
- **Dry Solids Leaching Loss:** Mean **0.40%** (Well below the 3.50% economic ceiling).
- **Calcium Displacement:** Mean **99.3%** de-crosslinking of middle lamella pectin.

---

## 2. Multi-Physics Coupled PDEs Solved on CUDA Tensors

### Stage A: Soaking Multi-Species Reactive-Transport
1. **Moisture Diffusion with Swelling:**
   $$\frac{\partial M}{\partial t} = \nabla \cdot (D_M(M, T) \nabla M)$$
2. **Competitive Chelation & Ion-Exchange:**
   $$\text{Ca}^{2+} + \text{Cit}^{3-} \rightleftharpoons [\text{Ca(Cit)}]^-, \quad \log K_f = 3.22$$
   $$2\text{Na}^+ + \text{Pectin-Ca} \rightleftharpoons \text{Pectin-Na}_2 + \text{Ca}^{2+}, \quad K_{eq} = 14.5$$

### Stage B: Steam Cooking (115°C Autoclave / 1.69 bar)
1. **Transient Heat Conduction (Spherical Laplacian):**
   $$\rho C_p \frac{\partial T}{\partial t} = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 k_{th} \frac{\partial T}{\partial r} \right), \quad T(R, t) = 115.0^\circ\text{C}$$
2. **Starch Gelatinization Kinetics:**
   $$\frac{\partial \alpha_{gel}}{\partial t} = k_{gel}(T) (1 - \alpha_{gel}) \cdot \mathcal{H}(T - 68^\circ\text{C})$$
3. **Cellular Shear Yield Stress Evolution:**
   $$\frac{\partial \tau_y}{\partial t} = -k_{soft}(T, \theta_{Ca}, \alpha_{gel}) \cdot \tau_y$$
4. **Volume-Integrated Cotyledon Hardness:**
   $$H(t) = \frac{3}{R^3} \int_0^R \tau_y(r, t) \cdot r^2 \, dr$$
   Cooking endpoint $T_{90}$ is extracted when $H(t) \le 0.10 \times H_0$ ($13.5\,\text{N}$).

---

## 3. Recommended Commercial Pretreatment Window (15 MT/Day Scale)

- **Reagent:** Citrate Buffer System (0.102% w/w active trisodium citrate + citric acid buffer)
- **Soaking Conditions:** 30.6°C bath temperature for 21.3 minutes at 1.33:1 liquor ratio
- **Rinse Water:** 0.20 - 0.25 L/kg fresh RO water
- **Drying Protocol:** 3-Zone continuous perforated belt dryer DR-101 (65°C -> 55°C -> Ambient cooling)
- **Net Commercial Processing OpEx:** ₹0.958 / kg processed dal
