"""
Harakutir 5-Sigma Multiphysics Engine.
Implements the full Model A-F hierarchy:
- Model A: Empirical Peleg Hydration with non-linear least squares & covariance.
- Model B: Analytical Diffusion (Crank 1975) & Geometric Comparison (Sphere vs Slab vs Disc).
- Model C: Transient Heat Conduction & Biot Number Scaling.
- Model D: Temperature-dependent Arrhenius Mass Diffusion.
- Model E: Starch Gelatinization & Competing Structural Softening Kinetics.
- Model F: Coupled Multi-Tensor GPU Vectorized Solver across Parameter Grids.
"""

import os
import sys
import time
import math
from typing import Dict, Any, List, Tuple, Optional

import numpy as np

try:
    import torch
except ImportError:
    torch = None

try:
    from scipy.optimize import curve_fit
except ImportError:
    curve_fit = None


# ==============================================================================
# Model A: Empirical Peleg Hydration Model
# ==============================================================================
class ModelA_EmpiricalHydration:
    """
    Peleg's equation: M(t) = M0 + t / (k1 + k2 * t)
    k1: Peleg rate constant (min / % moisture)
    k2: Peleg capacity constant (1 / % moisture)
    Equilibrium moisture: M_eq = M0 + 1 / k2
    """
    @staticmethod
    def peleg_equation(t: np.ndarray, M0: float, k1: float, k2: float) -> np.ndarray:
        return M0 + t / (k1 + k2 * t)

    @classmethod
    def fit(cls, times_min: List[float], moisture_db: List[float]) -> Dict[str, Any]:
        t = np.array(times_min, dtype=float)
        M = np.array(moisture_db, dtype=float)
        M0_init = float(M[0])

        if len(t) < 3:
            raise ValueError("At least 3 time points required for Peleg fit.")

        # Linearized estimate: t / (M - M0) = k1 + k2 * t
        dM = np.maximum(M - M0_init, 1e-4)
        y_lin = t / dM
        p_lin = np.polyfit(t, y_lin, 1)
        k2_init = max(1e-4, float(p_lin[0]))
        k1_init = max(1e-4, float(p_lin[1]))

        def model_func(t_val, k1_val, k2_val):
            return cls.peleg_equation(t_val, M0_init, k1_val, k2_val)

        popt, pcov = curve_fit(model_func, t, M, p0=[k1_init, k2_init], maxfev=5000)
        k1_fit, k2_fit = popt

        M_pred = model_func(t, k1_fit, k2_fit)
        residuals = M - M_pred
        ss_res = np.sum(residuals ** 2)
        ss_tot = np.sum((M - np.mean(M)) ** 2)
        r2 = 1.0 - (ss_res / max(1e-8, ss_tot))
        rmse = np.sqrt(np.mean(residuals ** 2))

        # 95% Confidence Intervals from covariance matrix
        perr = np.sqrt(np.diag(pcov))
        k1_ci = [k1_fit - 1.96 * perr[0], k1_fit + 1.96 * perr[0]]
        k2_ci = [k2_fit - 1.96 * perr[1], k2_fit + 1.96 * perr[1]]

        return {
            "model_name": "Peleg_Hydration_Model_A",
            "M0": M0_init,
            "k1": round(float(k1_fit), 6),
            "k2": round(float(k2_fit), 6),
            "k1_95_ci": [round(float(v), 6) for v in k1_ci],
            "k2_95_ci": [round(float(v), 6) for v in k2_ci],
            "M_equilibrium_db": round(float(M0_init + 1.0 / k2_fit), 4),
            "r2": round(float(r2), 5),
            "rmse": round(float(rmse), 6),
            "ss_res": round(float(ss_res), 6)
        }


# ==============================================================================
# Model B: Analytical Diffusion & Geometric Model Comparison
# ==============================================================================
class ModelB_AnalyticalDiffusion:
    """
    Analytical solutions (Crank 1975) for constant diffusivity D_eff:
    1. Sphere: (M - M0)/(M_inf - M0) = 1 - 6/pi^2 sum(1/n^2 exp(-n^2 pi^2 D t / R^2))
    2. Infinite Slab (thickness 2L): = 1 - 8/pi^2 sum(1/(2n+1)^2 exp(-(2n+1)^2 pi^2 D t / (4 L^2)))
    3. Lenticular Disc / Finite Cylinder (Newman product rule)
    """
    @staticmethod
    def sphere_solution(t_sec: float, D: float, R: float, n_terms: int = 50) -> float:
        if t_sec <= 0.0 or D <= 0.0:
            return 0.0
        n = np.arange(1, n_terms + 1)
        exp_terms = np.exp(- (n ** 2) * (np.pi ** 2) * D * t_sec / (R ** 2))
        return float(1.0 - (6.0 / (np.pi ** 2)) * np.sum(exp_terms / (n ** 2)))

    @staticmethod
    def slab_solution(t_sec: float, D: float, L_half: float, n_terms: int = 50) -> float:
        if t_sec <= 0.0 or D <= 0.0:
            return 0.0
        n = np.arange(0, n_terms)
        denom = (2 * n + 1) ** 2
        exp_terms = np.exp(- denom * (np.pi ** 2) * D * t_sec / (4.0 * (L_half ** 2)))
        return float(1.0 - (8.0 / (np.pi ** 2)) * np.sum(exp_terms / denom))

    @classmethod
    def compare_geometries(cls, t_sec: float, D: float, R_vol_equiv: float = 2.6e-3) -> Dict[str, float]:
        """
        Quantifies model-form discrepancy between Sphere, Slab, and Disc approximations.
        For a split cotyledon of equivalent volume radius R = 2.6 mm:
        Thickness L ~ 2.0 mm (half-thickness L_half = 1.0 mm), disc radius R_disc ~ 3.1 mm.
        """
        f_sphere = cls.sphere_solution(t_sec, D, R_vol_equiv)
        f_slab = cls.slab_solution(t_sec, D, L_half=1.0e-3)
        # Finite disc (Newman product of radial cylinder and axial slab)
        f_disc = 1.0 - (1.0 - f_sphere) * (1.0 - f_slab)

        return {
            "time_sec": t_sec,
            "fraction_sphere": round(f_sphere, 4),
            "fraction_slab": round(f_slab, 4),
            "fraction_disc": round(f_disc, 4),
            "discrepancy_disc_vs_sphere_pct": round(abs(f_disc - f_sphere) * 100.0, 2)
        }


# ==============================================================================
# Model C: Transient Heat Conduction & Biot Number Scaling
# ==============================================================================
class ModelC_HeatTransfer:
    """
    Thermal properties for split legume cotyledon:
    rho = 1350 kg/m^3, cp = 1800 J/(kg*K), k_th = 0.35 W/(m*K)
    alpha_th = k_th / (rho * cp) = 1.44e-7 m^2/s
    Convective heat transfer coefficient in boiling water: h ~ 1000 - 2500 W/(m^2*K)
    Biot Number: Bi = h * (V/A) / k_th
    """
    @staticmethod
    def calculate_biot_number(R: float = 2.6e-3, h: float = 1200.0, k_th: float = 0.35) -> float:
        L_c = R / 3.0  # characteristic length for sphere
        return (h * L_c) / k_th

    @staticmethod
    def core_temperature_time(t_sec: float, R: float = 2.6e-3, alpha_th: float = 1.15e-7,
                              T0: float = 25.0, T_bath: float = 100.0, n_terms: int = 30) -> float:
        """Transient center temperature for sphere with isothermal surface (Bi -> inf)."""
        if t_sec <= 0.0:
            return T0
        n = np.arange(1, n_terms + 1)
        series = np.sum(((-1) ** (n + 1)) * np.exp(- (n ** 2) * (np.pi ** 2) * alpha_th * t_sec / (R ** 2)))
        T_core = T_bath - 2.0 * (T_bath - T0) * series
        return float(np.clip(T_core, T0, T_bath))


# ==============================================================================
# Model F: Vectorized Multi-Tensor Coupled Multiphysics Engine (GPU & CPU)
# ==============================================================================
class MultiphysicsCoupledEngine:
    """
    Solves coupled state u = [T, M, alpha_gel, Firmness] across a grid of parameter cases.
    Vectorized over N_cases x N_shells.
    Evaluates:
    - Mass conservation (moisture diffusion with Arrhenius D(T))
    - Energy conservation (heat conduction)
    - Starch gelatinization kinetics
    - Competing middle-lamella pectin dissolution vs physical matrix models
    """
    def __init__(self, device: str = "cuda:0", num_shells: int = 25):
        self.requested_device = device
        self.device = self._resolve_device(device)
        self.num_shells = num_shells
        self.dr = 1.0 / (num_shells - 1)

    def _resolve_device(self, requested: str) -> str:
        if torch is not None and torch.cuda.is_available() and requested.startswith("cuda"):
            return requested
        return "cpu"

    def run_parameter_sweep(
        self,
        parameter_cases: List[Dict[str, float]],
        total_time_sec: float = 1800.0,
        dt_macro_sec: float = 2.0
    ) -> Dict[str, Any]:
        """
        Runs full coupled transient simulation across a batch of distinct physical cases.

        Each case specifies:
        - R_m: radius (m)
        - D0: pre-exponential diffusivity (m^2/s)
        - Ea_diff: activation energy for diffusion (J/mol)
        - alpha_th: thermal diffusivity (m^2/s)
        - k_soft: pectin softening rate (1/s)
        - T_bath_c: bath temperature (deg C)
        - M0: initial moisture dry basis
        """
        t0 = time.time()
        N_cases = len(parameter_cases)

        if torch is None:
            raise RuntimeError("PyTorch is required for multi-tensor coupled simulation.")

        dev = self.device

        # 1. Pack parameters into CUDA tensors
        radii = torch.tensor([c["R_m"] for c in parameter_cases], dtype=torch.float32, device=dev).unsqueeze(1)
        D0_vals = torch.tensor([c["D0"] for c in parameter_cases], dtype=torch.float32, device=dev).unsqueeze(1)
        Ea_vals = torch.tensor([c["Ea_diff"] for c in parameter_cases], dtype=torch.float32, device=dev).unsqueeze(1)
        alpha_th_vals = torch.tensor([c["alpha_th"] for c in parameter_cases], dtype=torch.float32, device=dev).unsqueeze(1)
        k_soft_vals = torch.tensor([c["k_soft"] for c in parameter_cases], dtype=torch.float32, device=dev)
        T_bath_vals = torch.tensor([c["T_bath_c"] for c in parameter_cases], dtype=torch.float32, device=dev).unsqueeze(1)
        M0_vals = torch.tensor([c["M0"] for c in parameter_cases], dtype=torch.float32, device=dev).unsqueeze(1)

        # 2. Allocate state tensors (N_cases x num_shells)
        r_grid = torch.linspace(0.02, 1.0, self.num_shells, device=dev).unsqueeze(0)  # 1 x N_shells
        r_coords = radii * r_grid  # N_cases x N_shells
        dr_phys = radii / (self.num_shells - 1)  # N_cases x 1

        T = torch.full((N_cases, self.num_shells), 25.0, dtype=torch.float32, device=dev)
        M = M0_vals.expand(-1, self.num_shells).clone()
        alpha_gel = torch.zeros((N_cases, self.num_shells), dtype=torch.float32, device=dev)
        firmness = torch.full((N_cases,), 135.0, dtype=torch.float32, device=dev)
        pectin_sol = torch.full((N_cases,), 0.10, dtype=torch.float32, device=dev)

        # 3. Dynamic CFL calculation (Physical maximum thermal diffusivity)
        R_gas = 8.314
        dr_min = float(dr_phys.min().item())
        max_diff = float(alpha_th_vals.max().item())
        dt_cfl = 0.35 * (dr_min ** 2) / max_diff
        sub_steps = max(1, int(math.ceil(dt_macro_sec / dt_cfl)))
        dt_sub = dt_macro_sec / sub_steps

        steps = int(total_time_sec / dt_macro_sec)

        # Precompute constants and geometric factors
        T_gel_onset = 68.0
        A_gel = 0.08
        Ea_gel = 28500.0
        T_surface = T_bath_vals.squeeze(1)

        inv_dr2 = 1.0 / (dr_phys ** 2)
        inv_2dr = 1.0 / (2.0 * dr_phys)
        two_over_r = 2.0 / r_coords[:, 1:-1]
        dt_alpha_th = dt_sub * alpha_th_vals

        for step in range(steps):
            for _ in range(sub_steps):
                # A. Temperature-dependent diffusivity (Arrhenius)
                T_kelvin = T + 273.15
                D_eff = D0_vals * torch.exp(-Ea_vals / (R_gas * T_kelvin))

                # B. Heat Conduction (Spherical Laplacian)
                d2T = (T[:, 2:] - 2.0 * T[:, 1:-1] + T[:, :-2]) * inv_dr2
                dT_dr = (T[:, 2:] - T[:, :-2]) * inv_2dr
                lap_T = d2T + two_over_r * dT_dr

                T[:, 1:-1] = torch.clamp(T[:, 1:-1] + dt_alpha_th * lap_T, 20.0, 115.0)
                T[:, 0] = T[:, 1]
                T[:, -1] = T_surface

                # C. Moisture Diffusion (Spherical Laplacian)
                d2M = (M[:, 2:] - 2.0 * M[:, 1:-1] + M[:, :-2]) * inv_dr2
                dM_dr = (M[:, 2:] - M[:, :-2]) * inv_2dr
                lap_M = d2M + two_over_r * dM_dr

                M[:, 1:-1] = torch.clamp(M[:, 1:-1] + (dt_sub * D_eff[:, 1:-1]) * lap_M, 0.08, 1.45)
                M[:, 0] = M[:, 1]
                M[:, -1] = 1.25

            # D. Starch Gelatinization Kinetics
            T_kelvin = T + 273.15
            gel_mask = (T > T_gel_onset).float()
            k_gel = A_gel * torch.exp(-Ea_gel / (R_gas * T_kelvin)) * gel_mask
            alpha_gel = torch.clamp(alpha_gel + dt_macro_sec * k_gel * (1.0 - alpha_gel), 0.0, 1.0)

            # E. Pectin Degradation & Softening Kinetics
            T_core = T[:, :3].mean(dim=1)
            alpha_avg = alpha_gel.mean(dim=1)
            temp_accel = torch.clamp(torch.exp((T_core - 80.0) / 15.0), 0.1, 8.0)
            pectin_sol = torch.clamp(pectin_sol + dt_macro_sec * 0.0008 * k_soft_vals * temp_accel * (0.85 - pectin_sol), 0.1, 0.85)

            soft_rate = 0.0015 * (1.0 + 1.2 * alpha_avg) * (pectin_sol / 0.50)
            firmness = torch.clamp(firmness - dt_macro_sec * soft_rate * (firmness - 20.0), 20.0, 135.0)

        if dev.startswith("cuda"):
            torch.cuda.synchronize()

        elapsed_sec = time.time() - t0

        # Reductions
        firmness_np = firmness.cpu().numpy()
        moisture_avg = M.mean(dim=1).cpu().numpy()
        gel_avg = alpha_gel.mean(dim=1).cpu().numpy()

        # Estimated full cooking time (firmness reaches <= 24 N)
        # Softening fraction completed at t = total_time_sec
        soft_frac = (135.0 - firmness_np) / (135.0 - 20.0)
        t_sim_min = total_time_sec / 60.0
        projected_cook_time_min = t_sim_min / np.maximum(0.01, soft_frac)

        return {
            "device": dev,
            "num_cases": N_cases,
            "simulated_duration_min": t_sim_min,
            "wall_clock_elapsed_sec": round(elapsed_sec, 4),
            "cases_per_second": round(N_cases / max(1e-4, elapsed_sec), 1),
            "projected_cook_times_min": [round(float(v), 2) for v in projected_cook_time_min],
            "final_firmness_n": [round(float(v), 2) for v in firmness_np],
            "final_moisture_db": [round(float(v), 4) for v in moisture_avg],
            "final_gelatinization_pct": [round(float(v * 100.0), 1) for v in gel_avg]
        }
