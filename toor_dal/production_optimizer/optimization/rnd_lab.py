import sys
import os
import pandas as pd
import torch

from toor_dal.production_optimizer.core.config import (
    AMBIENT_TEMP_KELVIN,
    HEAT_CONVERSION_EFFICIENCY,
    CONVECTION_COEFF_W_M2K,
    CASING_AREA_M2,
    MIXIE_UNIT_POWER_KW_PEAK
)
from toor_dal.production_optimizer.core.physics_models import (
    calculate_temp_rise_convection,
    calculate_arrhenius_denaturation_phys
)
from toor_dal.production_optimizer.core.gpu_engine import get_device, get_uniform_tensor

# Ensure project root is in path for direct execution
project_root = r"d:\PROJECT\FINNO PROJECTS"
if project_root not in sys.path:
    sys.path.append(project_root)


class RndLabOptimizer:
    def __init__(self):
        self.device = get_device()
        self.num_samples = 1_000_000

    def run_1kg_simulation(self):
        """
        Simulates processing EXACTLY 1kg batch in a Mixie.
        Optimizes Pulse Protocol (ON Time vs OFF Time) to minimize Total Process Time
        while keeping Protein Denaturation = 0.
        """
        print(
            f"Running R&D Simulation: 1kg Batch Optimization ({self.num_samples} iterations)")

        # --- Variables ---
        # Pulse ON Duration: 1s to 30s
        pulse_on_time = get_uniform_tensor(
            1.0, 30.0, self.num_samples, self.device)

        # Pulse OFF Duration: 1s to 60s
        pulse_off_time = get_uniform_tensor(
            1.0, 60.0, self.num_samples, self.device)

        # Total Required Grinding Time (Effective) for 1kg
        # 1kg usually takes ~60-90s of *active* grinding in a mixie to get flour?
        required_active_time = 90.0  # seconds of pure grinding needed

        # Number of Pulses needed = Required Time / Pulse ON Time
        num_pulses = torch.ceil(required_active_time / pulse_on_time)

        # --- Physics Loop (Step-by-Step for Sensitivity) ---
        # We model the temperature accumulation over the pulses.
        # Temp Rise during ON + Temp Decay during OFF.

        # Max Temp reached in strict convective cooling model
        # Simplification: Calculate Equilibrium Temp or Peak Temp of first few pulses?
        # Rigorous: T_peak = T_ambient + Delta_T_accumulated

        # Single Pulse Rise
        # We reuse the physics model:
        # delta_t_rise = ...

        # Mass is smaller (1kg) vs continuous flow
        mass_batch = torch.tensor(1.0, device=self.device)
        power_watts = torch.tensor(
            MIXIE_UNIT_POWER_KW_PEAK * 1000.0, device=self.device)  # 750W

        # -- Physics Check --
        # Rise during ON
        t_rise = calculate_temp_rise_convection(power_watts, pulse_on_time, mass_batch,
                                                torch.tensor(
                                                    AMBIENT_TEMP_KELVIN, device=self.device),
                                                self.device)

        # Decay during OFF (Newton's Law of Cooling)
        # T_final = T_env + (T_initial - T_env) * exp(-rate * t)
        # We approximate decay rate from the convection parameters
        # Rate k_cool = hA / mCp
        cp_j = 1800.0 * 1.0  # m*Cp
        hA = CONVECTION_COEFF_W_M2K * CASING_AREA_M2
        k_cool = hA / cp_j

        cooling_factor = torch.exp(-k_cool * pulse_off_time)

        # Accumulation Model (Geometric Series/Equilibrium Limit)
        # T_peak_steady = T_rise * (1 / (1 - cooling_factor)) ?
        # Approx: If pulses are infinite, does it run away?
        # T_n+1 = (T_n * cool) + Rise
        # Limit T = Rise / (1 - cool)

        temp_limit_rise = t_rise / (1.0 - cooling_factor)
        peak_temp_k = AMBIENT_TEMP_KELVIN + temp_limit_rise

        # --- Constraints ---
        # Protein Denaturation Check at Peak Temp
        # Assume peak temp is held for the duration of the last pulse (conservatively)
        denaturation = calculate_arrhenius_denaturation_phys(
            peak_temp_k, pulse_on_time, self.device)

        # Total Process Time = (ON + OFF) * Pulses
        total_process_time_sec = (pulse_on_time + pulse_off_time) * num_pulses

        # --- Objective: Minimize Time s.t. Denaturation < 0.1% ---
        # Penalty for damage
        penalty = torch.where(denaturation > 0.001, 1e6, 0.0)  # Huge penalty

        score_time = total_process_time_sec + penalty

        best_idx = torch.argmin(score_time)

        # --- Results ---
        best_on = pulse_on_time[best_idx].item()
        best_off = pulse_off_time[best_idx].item()
        best_time = total_process_time_sec[best_idx].item()
        best_temp = peak_temp_k[best_idx].item() - 273.15
        best_dmg = denaturation[best_idx].item()

        results = {
            "on_time_sec": best_on,
            "off_time_sec": best_off,
            "duty_cycle": best_on / (best_on + best_off),
            "total_batch_time_min": best_time / 60.0,
            "peak_temp_c": best_temp,
            "protein_damage": best_dmg
        }

        return results

    def export_results(self, results):
        print("\n--- R&D SIMULATION RESULTS (1kg Batch) ---")
        print("Optimal 'Mixie Hack' Protocol for Lab:")
        print(f"  Pulse ON Time:  {results['on_time_sec']:.2f} seconds")
        print(f"  Pulse OFF Time: {results['off_time_sec']:.2f} seconds")
        print(f"  Duty Cycle:     {results['duty_cycle']:.1%}")
        print(
            f"  Total Process Time: {results['total_batch_time_min']:.1f} minutes")
        print(f"  Peak Temperature:   {results['peak_temp_c']:.1f} C")
        print(f"  Protein Damage:     {results['protein_damage']*100:.6f} %")

        # Save simple log
        base_dir = r"d:/PROJECT/FINNO PROJECTS/toor_dal/production_optimizer/logging"
        log_path = os.path.join(base_dir, "rnd_1kg_results.csv")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("metric,value\n")
            for k, v in results.items():
                f.write(f"{k},{v}\n")
