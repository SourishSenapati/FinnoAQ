"""
FinnoaQ Engineering Workspace — Offline GPU-Accelerated Monte Carlo & Uncertainty Engine.
Project Reference: FNQ-PR-2026-001 | Toor Dal Cooking-Time Optimization
Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

This module implements:
1. Massive parallel Monte Carlo parameter sweep across uncertain inputs (feed moisture, solids loss,
   dryer inlet moisture, drying temperature, Peleg hydration kinetics, and cooking softening).
2. Dual-backend execution: Vectorized CPU Reference Path (NumPy) vs Tensorized GPU Path (PyTorch CUDA).
3. Rigorous benchmarking using CUDA Events, memory tracking, and numerical equivalence verification.
4. Workload scaling study (N = 100 to 250,000) to identify the crossover threshold where GPU execution dominates.
"""

import time
import numpy as np
from typing import Dict, Any, Tuple, List, Optional
import os

class GPUBatchMonteCarloEngine:
    """
    Solves coupled material, moisture, thermal energy, and hydration kinetics across massive scenario ensembles.
    """
    def __init__(self, device_str: str = "cuda:0"):
        self.device_str = device_str
        self.torch_available = False
        self.cuda_available = False
        self.device = None
        self._init_backend()

    def _init_backend(self):
        try:
            import torch
            self.torch_available = True
            if "cuda" in self.device_str and torch.cuda.is_available():
                self.cuda_available = True
                self.device = torch.device(self.device_str)
            else:
                self.device = torch.device("cpu")
        except ImportError:
            self.torch_available = False
            self.cuda_available = False

    def generate_random_scenarios(self, n_scenarios: int, seed: int = 42) -> Dict[str, np.ndarray]:
        """
        Generates N parameter sets across plausible physical intervals.
        """
        np.random.seed(seed)
        return {
            'feed_total': np.full(n_scenarios, 15000.0, dtype=np.float32),
            'w_in': np.random.uniform(0.095, 0.125, n_scenarios).astype(np.float32),
            'solids_loss': np.random.uniform(120.0, 250.0, n_scenarios).astype(np.float32),
            'w_dryer': np.random.uniform(0.260, 0.320, n_scenarios).astype(np.float32),
            't_air_in': np.random.uniform(55.0, 75.0, n_scenarios).astype(np.float32),
            'k1': np.random.uniform(1.20, 4.50, n_scenarios).astype(np.float32),
            'k2': np.random.uniform(0.008, 0.022, n_scenarios).astype(np.float32),
            'soak_time': np.full(n_scenarios, 30.0, dtype=np.float32),
            'target_w_out': np.full(n_scenarios, 0.100, dtype=np.float32)
        }

    def run_cpu_vectorized(self, scenarios: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Vectorized CPU reference path using NumPy.
        """
        start = time.perf_counter()

        feed_total = scenarios['feed_total']
        w_in = scenarios['w_in']
        solids_loss = scenarios['solids_loss']
        w_dryer = scenarios['w_dryer']
        t_air_in = scenarios['t_air_in']
        k1 = scenarios['k1']
        k2 = scenarios['k2']
        soak_time = scenarios['soak_time']
        w_out = scenarios['target_w_out']

        # 1. Mass balance
        feed_dry_solids = feed_total * (1.0 - w_in)
        prod_dry_solids = feed_dry_solids - solids_loss
        prod_total = prod_dry_solids / (1.0 - w_out)
        prod_water = prod_total * w_out

        dryer_inlet_total = prod_dry_solids / (1.0 - w_dryer)
        dryer_inlet_water = dryer_inlet_total * w_dryer
        evaporation_kg_day = dryer_inlet_water - prod_water
        evaporation_kg_h = evaporation_kg_day / 20.0

        # 2. Thermal duty
        # Latent heat: h_fg = 2406.86 kJ/kg
        # Sensible solids: prod_dry_solids/20 * 1.60 * (45 - 25)
        # Sensible water: prod_water/20 * 4.184 * (45 - 25)
        # Sensible evap: evap/20 * (4.184*15 + 2406.86 + 1.88*5) = evap/20 * 2479.0 kJ/kg
        q_kj_h = (prod_dry_solids / 20.0) * 1.60 * 20.0 + \
                 (prod_water / 20.0) * 4.184 * 20.0 + \
                 evaporation_kg_h * 2479.0
        thermal_duty_kw = q_kj_h / 3600.0
        air_flow_kg_h = evaporation_kg_h / 0.0125

        # 3. Hydration absorption at 30 min (Peleg)
        m0_pct = (w_in / (1.0 - w_in)) * 100.0  # db
        m30_pct = m0_pct + soak_time / (k1 + k2 * soak_time)

        # 4. Cooking softening T90 (min)
        k_soft = 0.075 * (2.0 / k1) ** 0.5
        t90_min = np.log(100.0 / 10.0) / k_soft

        elapsed_sec = time.perf_counter() - start

        return {
            'evaporation_kg_day': evaporation_kg_day,
            'dryer_inlet_total_kg_day': dryer_inlet_total,
            'thermal_duty_kw': thermal_duty_kw,
            'air_flow_kg_h': air_flow_kg_h,
            'm30_pct_db': m30_pct,
            't90_cooking_min': t90_min,
            'runtime_seconds': elapsed_sec
        }

    def run_gpu_tensorized(self, scenarios: Dict[str, np.ndarray]) -> Dict[str, Any]:
        """
        Tensorized GPU path using PyTorch CUDA.
        """
        if not (self.torch_available and self.cuda_available):
            return {'error': 'CUDA GPU is not available on this host'}

        import torch

        # Warmup GPU
        dummy = torch.randn(100, 100, device=self.device)
        torch.cuda.synchronize()

        # Start CUDA timing
        start_event = torch.cuda.Event(enable_timing=True)
        end_event = torch.cuda.Event(enable_timing=True)

        torch.cuda.reset_peak_memory_stats(self.device)
        start_event.record()

        # Transfer tensors to GPU
        feed_total = torch.tensor(scenarios['feed_total'], device=self.device, dtype=torch.float32)
        w_in = torch.tensor(scenarios['w_in'], device=self.device, dtype=torch.float32)
        solids_loss = torch.tensor(scenarios['solids_loss'], device=self.device, dtype=torch.float32)
        w_dryer = torch.tensor(scenarios['w_dryer'], device=self.device, dtype=torch.float32)
        k1 = torch.tensor(scenarios['k1'], device=self.device, dtype=torch.float32)
        k2 = torch.tensor(scenarios['k2'], device=self.device, dtype=torch.float32)
        soak_time = torch.tensor(scenarios['soak_time'], device=self.device, dtype=torch.float32)
        w_out = torch.tensor(scenarios['target_w_out'], device=self.device, dtype=torch.float32)

        # 1. Mass balance
        feed_dry_solids = feed_total * (1.0 - w_in)
        prod_dry_solids = feed_dry_solids - solids_loss
        prod_total = prod_dry_solids / (1.0 - w_out)
        prod_water = prod_total * w_out

        dryer_inlet_total = prod_dry_solids / (1.0 - w_dryer)
        dryer_inlet_water = dryer_inlet_total * w_dryer
        evaporation_kg_day = dryer_inlet_water - prod_water
        evaporation_kg_h = evaporation_kg_day / 20.0

        # 2. Thermal duty
        q_kj_h = (prod_dry_solids / 20.0) * 1.60 * 20.0 + \
                 (prod_water / 20.0) * 4.184 * 20.0 + \
                 evaporation_kg_h * 2479.0
        thermal_duty_kw = q_kj_h / 3600.0
        air_flow_kg_h = evaporation_kg_h / 0.0125

        # 3. Hydration absorption at 30 min (Peleg)
        m0_pct = (w_in / (1.0 - w_in)) * 100.0
        m30_pct = m0_pct + soak_time / (k1 + k2 * soak_time)

        # 4. Cooking softening T90
        k_soft = 0.075 * torch.sqrt(2.0 / k1)
        t90_min = torch.log(torch.tensor(10.0, device=self.device)) / k_soft

        end_event.record()
        torch.cuda.synchronize()

        elapsed_ms = start_event.elapsed_time(end_event)
        elapsed_sec = elapsed_ms / 1000.0
        peak_vram_mb = torch.cuda.max_memory_allocated(self.device) / (1024 * 1024)

        return {
            'evaporation_kg_day': evaporation_kg_day.cpu().numpy(),
            'dryer_inlet_total_kg_day': dryer_inlet_total.cpu().numpy(),
            'thermal_duty_kw': thermal_duty_kw.cpu().numpy(),
            'air_flow_kg_h': air_flow_kg_h.cpu().numpy(),
            'm30_pct_db': m30_pct.cpu().numpy(),
            't90_cooking_min': t90_min.cpu().numpy(),
            'runtime_seconds': elapsed_sec,
            'runtime_ms': elapsed_ms,
            'peak_vram_mb': peak_vram_mb,
            'device_name': torch.cuda.get_device_name(self.device)
        }

    def benchmark_workload_scaling(self, sizes: List[int] = [100, 1000, 10000, 50000, 100000, 250000]) -> List[Dict[str, Any]]:
        """
        Executes scaling study across workload sizes to benchmark CPU vs GPU performance.
        """
        benchmark_results = []
        for n in sizes:
            scenarios = self.generate_random_scenarios(n)
            cpu_res = self.run_cpu_vectorized(scenarios)
            t_cpu = cpu_res['runtime_seconds']

            if self.cuda_available:
                gpu_res = self.run_gpu_tensorized(scenarios)
                t_gpu = gpu_res['runtime_seconds']
                speedup = (t_cpu / t_gpu) if t_gpu > 0 else 1.0

                # Numerical equivalence check
                max_abs_err_evap = float(np.max(np.abs(cpu_res['evaporation_kg_day'] - gpu_res['evaporation_kg_day'])))
                max_abs_err_duty = float(np.max(np.abs(cpu_res['thermal_duty_kw'] - gpu_res['thermal_duty_kw'])))
                max_abs_err_t90 = float(np.max(np.abs(cpu_res['t90_cooking_min'] - gpu_res['t90_cooking_min'])))

                is_equivalent = bool(max_abs_err_evap < 1e-3 and max_abs_err_duty < 1e-3 and max_abs_err_t90 < 1e-3)

                benchmark_results.append({
                    'scenarios_count': n,
                    'cpu_time_sec': round(t_cpu, 5),
                    'gpu_time_sec': round(t_gpu, 5),
                    'speedup_ratio': round(speedup, 2),
                    'is_gpu_faster': bool(speedup > 1.0),
                    'max_abs_error_evap_kg': max_abs_err_evap,
                    'max_abs_error_duty_kw': max_abs_err_duty,
                    'is_numerically_equivalent': is_equivalent,
                    'peak_vram_mb': round(gpu_res['peak_vram_mb'], 2)
                })
            else:
                benchmark_results.append({
                    'scenarios_count': n,
                    'cpu_time_sec': round(t_cpu, 5),
                    'gpu_time_sec': None,
                    'speedup_ratio': None,
                    'is_gpu_faster': False,
                    'status': 'CUDA_UNAVAILABLE'
                })

        return benchmark_results
