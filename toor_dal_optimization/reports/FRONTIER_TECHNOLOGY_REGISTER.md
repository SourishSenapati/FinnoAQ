# HARAKUTIR TOOR DAL — FRONTIER TECHNOLOGY REGISTER

**Document ID:** HKT-TECH-2026-001  
**Project Architecture:** Hybrid Multiscale Biophysical Discovery Platform  
**Host Target:** AMD Ryzen AI 9 365 + NVIDIA GeForce RTX 4050 Laptop GPU (Offline CUDA 12.4)  
**Date:** 2026-10-14  

---

## 1. Master Technology Stack Matrix

| Technology Component | Scientific & Engineering Use | Open Source / Access Status | Hardware Demands | Offline Viability | Limitations & Failure Modes | Acceptance Test |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Physics-Informed Neural Network (PINN)** | Inverse parameter estimation ($\ln D_{\text{eff}}, \ln k_{\text{soft}}$) from sparse boundary data. | Open-Source (`torch.nn`, autograd) | 27.5 MB VRAM on RTX 4050; 2.5s training | **100% Offline** (local weights) | Slower than analytical solver for pure forward solve; soft boundary enforcement. | `test_pinn_coupled_transport_and_inverse_estimation` |
| **Scientific Transformer Surrogate** | Sequence-to-metric mapping; candidate screening with OOD detection. | Open-Source (`nn.TransformerEncoder`) | 6.4 $\mu$s / candidate; 0.6 MB weights | **100% Offline** | Pure interpolator within training bounds; flags unphysical extrapolation. | `test_transformer_surrogate_and_ood_detection` |
| **8192×8192 2D Spatial Solver** | Asymptotic zero-discretization continuum truth model ($67.11\text{M}$ nodes). | Open-Source (`torch` CUDA / FVM) | 64 MB VRAM (chunked); 5.1 ms runtime | **100% Offline** | Over-resolved for bulk sweeps; memory-safe chunking required. | `test_high_res_spatial_8192_grid_convergence` |
| **Analytical Fourier Eigenfunction Series** | Canonical ground truth for transient Robin boundary conduction. | Closed-form exact equations (`gpu_engine.py`) | 0.4 $\mu$s / candidate; negligible memory | **100% Offline** | Requires regular geometry (infinite slab / cylinder approximation). | `test_omega_heat_transfer_fourier_analytical_benchmark` |
| **Rohsenow Boiling Hydrodynamics** | Two-phase pool boiling convective boundary coupling ($h = 2,895\text{ W/m}^2\text{K}$). | Open-Source Python (`navier_stokes_boiling.py`) | Negligible CPU/GPU load | **100% Offline** | Calibrated for atmospheric/115 kPa pool water. | `test_navier_stokes_convective_heat_transfer_coefficient` |
| **Goal-Locked Dream-RSI Engine** | 8-stage autonomous scientific discovery and candidate ranking. | Custom deterministic discovery layer (`dream_rsi.py`) | SQLite persistence; negligible RAM | **100% Offline** | Requires objective physical truth metrics to avoid circular loops. | `test_omega_dream_rsi_replay_determinism` |
| **DoseCalculator Multi-Basis Engine** | Separates liquor basis (112.5 kg) from feed basis (75 kg); 98.54% recovery. | Python 3.13 (`dose_calculator.py`) | Pure CPU arithmetic (< 1 ms) | **100% Offline** | Requires accurate target-lot incoming moisture input. | `test_dose_calculator_multi_basis_separation` |
