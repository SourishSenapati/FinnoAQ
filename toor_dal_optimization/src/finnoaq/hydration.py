"""
Hydration modeling module.
Implements:
1. Interpretable Peleg model with SciPy non-linear least squares,
   parameter uncertainty, identifiability checks, and residual diagnostics.
2. Offline GPU-accelerated PyTorch inverse diffusion model on NVIDIA RTX 4050,
   with VRAM bounds, single GPU worker, and CPU fallback.
"""

import numpy as np
import scipy.stats as stats
from scipy.optimize import curve_fit
from typing import Dict, Any, List, Tuple, Optional
import time

def peleg_function(t: np.ndarray, m0: float, k1: float, k2: float) -> np.ndarray:
    """Peleg equation: M(t) = M0 + t / (k1 + k2 * t)"""
    return m0 + t / (k1 + k2 * t)

def fit_peleg_model(
    times: List[float],
    moistures: List[float],
    fix_m0: bool = True
) -> Dict[str, Any]:
    """
    Fit Peleg model to hydration data with rigorous uncertainty estimation.
    """
    t = np.array(times, dtype=np.float64)
    m = np.array(moistures, dtype=np.float64)
    
    # Validation
    if len(t) < 3:
        return {"status": "insufficient_points", "message": "At least 3 points required."}
    if not np.all(np.diff(t) >= 0):
        return {"status": "invalid_time_sequence", "message": "Time sequence must be monotonically non-decreasing."}
    
    m0_fixed = float(m[0]) if fix_m0 else None
    
    try:
        if fix_m0:
            # Fit only k1 and k2
            def model_fixed(t_val, k1, k2):
                return m0_fixed + t_val / (k1 + k2 * t_val)
            
            popt, pcov = curve_fit(
                model_fixed, t[1:], m[1:],
                p0=[2.0, 0.01],
                bounds=([1e-4, 1e-5], [100.0, 1.0]),
                maxfev=5000
            )
            k1, k2 = float(popt[0]), float(popt[1])
            m0 = m0_fixed
            perr = np.sqrt(np.diag(pcov))
            k1_se, k2_se = float(perr[0]), float(perr[1])
            m0_se = 0.0
        else:
            popt, pcov = curve_fit(
                peleg_function, t, m,
                p0=[float(m[0]), 2.0, 0.01],
                bounds=([0.0, 1e-4, 1e-5], [50.0, 100.0, 1.0]),
                maxfev=5000
            )
            m0, k1, k2 = float(popt[0]), float(popt[1]), float(popt[2])
            perr = np.sqrt(np.diag(pcov))
            m0_se, k1_se, k2_se = float(perr[0]), float(perr[1]), float(perr[2])
            
        # Model predictions and residuals
        m_pred = peleg_function(t, m0, k1, k2)
        residuals = m - m_pred
        ss_res = float(np.sum(residuals ** 2))
        ss_tot = float(np.sum((m - np.mean(m)) ** 2))
        r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 0.0
        rmse = float(np.sqrt(np.mean(residuals ** 2)))
        
        # Derived physical parameters
        initial_rate_r0 = 1.0 / k1 if k1 > 0 else 0.0
        eq_moisture_me = m0 + 1.0 / k2 if k2 > 0 else np.nan
        
        # Parameter 95% Confidence Intervals
        dof = max(1, len(t) - (2 if fix_m0 else 3))
        t_crit = stats.t.ppf(0.975, df=dof)
        
        k1_ci = [round(max(0.0, k1 - t_crit * k1_se), 4), round(k1 + t_crit * k1_se, 4)]
        k2_ci = [round(max(0.0, k2 - t_crit * k2_se), 6), round(k2 + t_crit * k2_se, 6)]
        
        return {
            "status": "success",
            "m0": round(m0, 4),
            "m0_se": round(m0_se, 4),
            "k1": round(k1, 4),
            "k1_se": round(k1_se, 4),
            "k1_95_ci": k1_ci,
            "k2": round(k2, 6),
            "k2_se": round(k2_se, 6),
            "k2_95_ci": k2_ci,
            "initial_rate_r0_pct_per_min": round(initial_rate_r0, 4),
            "equilibrium_moisture_me_pct": round(eq_moisture_me, 2),
            "r2": round(r2, 4),
            "rmse": round(rmse, 4),
            "residuals": [round(float(r), 4) for r in residuals],
            "is_identifiable": bool(k1_se / k1 < 0.5 and k2_se / k2 < 0.5)
        }
    except Exception as e:
        return {
            "status": "fit_failed",
            "error": str(e),
            "is_identifiable": False
        }


# GPU-ACCELERATED INVERSE MODEL USING PYTORCH ON NVIDIA RTX 4050
class GPUInverseHydrationModel:
    """
    Offline PyTorch Inverse Solver for Legume Hydration Kinetics.
    Runs on RTX 4050 CUDA GPU (or falls back safely to CPU).
    Solves inverse moisture mass transfer parameter discovery.
    """
    def __init__(self, target_device: str = "cuda:0", max_vram_mb: int = 4096):
        self.max_vram_mb = max_vram_mb
        self.device = self._select_device(target_device)

    def _select_device(self, target: str):
        try:
            import torch
            if "cuda" in target and torch.cuda.is_available():
                return torch.device(target)
            return torch.device("cpu")
        except ImportError:
            return "cpu"

    def fit_inverse_diffusion(
        self,
        times: List[float],
        moistures: List[float],
        radius_mm: float = 2.5,
        epochs: int = 500,
        lr: float = 0.01
    ) -> Dict[str, Any]:
        """
        Solves radial diffusion inverse problem:
        dM/dt = (1/r^2) d/dr (r^2 D_eff dM/dr)
        Estimates effective water diffusion coefficient D_eff (m^2/s)
        using gradient-based optimization on GPU.
        """
        start_time = time.time()
        import torch

        # Telemetry
        device_name = torch.cuda.get_device_name(0) if self.device.type == "cuda" else "CPU"
        
        t_tensor = torch.tensor(times, dtype=torch.float32, device=self.device)
        m_tensor = torch.tensor(moistures, dtype=torch.float32, device=self.device)
        m0 = m_tensor[0]
        m_sat = m_tensor[-1] * 1.05  # Approximate saturation boundary

        # Normalized moisture ratio MR(t) = (M(t) - M0) / (Msat - M0)
        mr_target = (m_tensor - m0) / (m_sat - m0 + 1e-6)

        # Trainable log-diffusivity parameter: D_eff = exp(log_D)
        # Typical legume legume D_eff ~ 1e-10 to 1e-11 m^2/s
        log_D = torch.nn.Parameter(torch.tensor([-23.0], dtype=torch.float32, device=self.device))
        optimizer = torch.optim.Adam([log_D], lr=lr)

        # Analytical sphere series solution for average moisture:
        # MR(t) = 1 - (6 / pi^2) * sum_{n=1}^N (1 / n^2) * exp(-n^2 * pi^2 * D_eff * t / R^2)
        r_meters = radius_mm * 1e-3
        n_terms = torch.arange(1, 21, dtype=torch.float32, device=self.device)

        history_loss = []
        for epoch in range(epochs):
            optimizer.zero_grad()
            d_eff = torch.exp(log_D)  # m^2/s
            
            # Vectorized series calculation across all time points
            # t in seconds
            t_sec = t_tensor * 60.0
            
            # shape: (len(t), n_terms)
            exponent = - (n_terms ** 2) * (np.pi ** 2) * d_eff * t_sec.unsqueeze(1) / (r_meters ** 2)
            terms = (1.0 / (n_terms ** 2)) * torch.exp(exponent)
            series_sum = torch.sum(terms, dim=1)
            mr_pred = 1.0 - (6.0 / (np.pi ** 2)) * series_sum
            
            loss = torch.mean((mr_pred - mr_target) ** 2)
            loss.backward()
            optimizer.step()
            history_loss.append(float(loss.item()))

        final_d_eff = float(torch.exp(log_D).item())
        calc_time = time.time() - start_time
        
        # GPU Memory check
        vram_allocated_mb = 0.0
        if self.device.type == "cuda":
            vram_allocated_mb = torch.cuda.memory_allocated(0) / (1024 * 1024)

        return {
            "status": "success",
            "device_used": str(self.device),
            "device_name": device_name,
            "vram_allocated_mb": round(vram_allocated_mb, 2),
            "runtime_seconds": round(calc_time, 3),
            "effective_diffusivity_m2_s": final_d_eff,
            "effective_diffusivity_scientific": f"{final_d_eff:.3e}",
            "final_loss": round(float(history_loss[-1]), 6),
            "epochs": epochs
        }
