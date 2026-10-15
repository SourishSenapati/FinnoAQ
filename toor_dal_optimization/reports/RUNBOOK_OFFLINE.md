# HARAKUTIR TOOR DAL — OFFLINE OPERATIONS RUNBOOK

**Document ID:** HKT-RBK-2026-002  
**Version:** 5.0.0 (Master Build Directive & Complete 15 TPD Plant Engineering)  
**Host Environment:** AMD Ryzen AI 9 365 + NVIDIA GeForce RTX 4050 Laptop GPU (Windows 11)  
**Directive Date:** 15 October 2026  

---

## 1. Operating Philosophy

This engineering system is designed for **reproducible, 100% offline, evidence-traceable execution**. All models, deterministic mass/energy balance engines, psychrometric drying solvers, machine sizing calculations, parametric CAD generators, and statistical validation suites run locally with zero external network dependencies.

---

## 2. Environment Verification & Quickstart

Before executing computational workflows or regenerating reports, verify the hardware environment and regression test suite:

```powershell
# 1. Navigate to workspace root
cd d:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization

# 2. Interrogate hardware and local GPU stack
& "C:\Python313\python.exe" scratch/discover_hardware.py

# 3. Execute full automated unit, integration, and engineering test suite (80 tests)
& "C:\Python313\python.exe" -m pytest tests/ -v
```

---

## 3. Core Operational Workflows

### Workflow A: 15 MT/day Detailed Machine Sizing & ASME Mechanical Calculations
Run the first-principles sizing calculator for soak tanks, hydrofoil agitator shaft, fluid bed psychrometrics, and packaging line:
```powershell
& "C:\Python313\python.exe" src/harakutir/detailed_machine_and_plant_engineering.py
```

### Workflow B: Generate Editable 2D DXF CAD Drawings, 3D STEP Models, and Vector PDF
Regenerate all 10 DXF CAD drawings, 4 STEP AP214 models, OBJ 3D meshes, and the multi-page vector PDF drawing package:
```powershell
& "C:\Python313\python.exe" scripts/generate_cad_and_drawings.py
```

### Workflow C: 15 MT/day Industrial Plant Design & Stream Tables
Calculate throughput across 8h, 16h, 24h schedules, dual feed/output bases, rigorous mass balance, drying thermodynamics, and low/base/high OpEx:
```powershell
& "C:\Python313\python.exe" -c "from src.harakutir.plant_design_15tpd import PlantDesign15TPD; p = PlantDesign15TPD(); print('Mass Bal:', p.calculate_rigorous_mass_balance()['overall_closure']); print('OpEx:', p.calculate_techno_economics('base'))"
```

### Workflow D: Benchmark True GPU 2D Finite-Difference Stencil
Run the empirical 2D diffusion-reaction stencil across mesh sizes from $512^2$ to $8192^2$ ($67.1\text{M nodes}$) on the local RTX 4050 Laptop GPU:
```powershell
& "C:\Python313\python.exe" -c "from src.harakutir.high_res_spatial_solver import benchmark_real_2d_pde_stencil; print(benchmark_real_2d_pde_stencil(n=8192, steps=10))"
```

### Workflow E: Chemical Dosing & Formulation Multi-Basis Separation
Compare $0.50\%$ w/w in soak liquor ($112.5\text{ kg/day}$) against $0.50\%$ of dal feed ($75.0\text{ kg/day}$):
```powershell
& "C:\Python313\python.exe" -c "from src.harakutir.plant_design_15tpd import PlantDesign15TPD; p = PlantDesign15TPD(); print(p.calculate_chemical_dosing_bases(0.50))"
```

### Workflow F: Physical Kitchen Trial Data Entry & Hypothesis Testing
When physical timestamps are recorded in `data/kitchen_data_template.csv`, execute the two-sample Welch's t-test and gate evaluation:
```powershell
& "C:\Python313\python.exe" -c "from scipy import stats; ctrl = [22.0, 22.2, 21.8, 22.1]; trt = [13.8, 14.0, 13.7, 13.9]; t_stat, p_val = stats.ttest_ind(ctrl, trt, equal_var=False); print(f't={t_stat:.3f}, p={p_val:.4e}')"
```

---

## 4. Digital Engineering Directory Structure

```text
engineering/
  design_basis/           # design_basis.yaml (Machine-readable inputs with evidence tags)
  process/                # Mass/Energy balances, stream tables, PFD definitions
  equipment/              # Detailed sizing calculations and datasheets
  mechanical/             # ASME vessel calculations, shaft torque and deflection
  cad/
    dxf/                  # 10x 2D editable CAD drawings (DWG-FIN-15T-001 to 010.dxf)
    step/                 # 4x 3D ISO 10303-21 STEP AP214 solid exchange models
    obj/                  # 3D Wavefront OBJ polygon meshes
    pdf/                  # Multi-page vector PDF engineering drawing package
  piping_instrumentation/ # P&IDs, piping specs, sanitary Tri-Clamp headers
  electrical_controls/    # SLD, motor load list, PLC I/O list, cause-and-effect matrix
  civil_structural/       # Layout, equipment base loading plan, drainage trenches
  utilities_environment/  # Water softening, steam boiler, ETP neutralization package
  safety_hygiene/         # HAZOP worksheet, FSSAI Schedule 4 matrix, HACCP CCPs
  procurement/            # Itemized Bill of Materials (BOM), RFQ package specs
  commissioning/          # FAT/SAT protocols, IQ/OQ/PQ plans, Standard Operating Procedures
  registers/              # Master equipment register, line list, valve list, instrument index
```

---

## 5. Resource Governance & Guardrails

1. **No Endless Daemons:** Endless background exploration daemons without specific stopping criteria are prohibited under project governance.
2. **VRAM Ceiling:** Keep local GPU tensor allocations under $4,500\text{ MB}$ to preserve headroom on the 6,141 MB RTX 4050 GPU.
3. **Synthetic Data Quarantine:** Synthetic training vectors must remain strictly quarantined in `runs/synthetic/` and must never contaminate physical candidate rankings or client reports.
4. **Stage 2 Lock:** The 15 MT/day detailed engineering and equipment procurement remains strictly locked until Gate G-A kitchen testing and Gate G-B pilot runs pass with signed physical laboratory certificates.
5. **Non-Negotiable Disclaimer:** All drawings and design models are marked `PRELIMINARY—NOT FOR CONSTRUCTION` until approved by qualified licensed professional engineers.
