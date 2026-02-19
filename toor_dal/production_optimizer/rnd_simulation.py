"""
R&D Simulation Module
Optimizes the process for 1kg Laboratory Scales.
Focuses on transient thermal effects and manual variability.
"""
import torch
try:
    from .core.config import (
        SPECIFIC_HEAT_PULSE_KJ_KG_C,
        ACTIVATION_ENERGY_J_MOL,
        FREQUENCY_FACTOR_A,
        GAS_CONSTANT_J_MOL_K
    )
except ImportError:
    from core.config import (
        SPECIFIC_HEAT_PULSE_KJ_KG_C,
        ACTIVATION_ENERGY_J_MOL,
        FREQUENCY_FACTOR_A,
        GAS_CONSTANT_J_MOL_K
    )


class RndSimulationModule:
    """
    Simulates R&D Scale (1kg Batch) Physics.
    Focuses on Transient effects, Manual variability, and Experimental Feasibility.
    """

    def __init__(self, device):
        self.device = device
        # Enforce Double Precision for R&D module as requested
        # Note: This changes global state, but assuming single-threaded execution flow
        torch.set_default_dtype(torch.float64)

    def simulate_1kg_batch(self, num_samples):
        """Simulates a 1kg batch process."""
        # ---- CONSTANTS ----
        # R&D scale physics (Transient)
        # Heat capacity for small batch approx same per kg, but heat loss is different
        CP_J_KG_K = SPECIFIC_HEAT_PULSE_KJ_KG_C * 1000.0

        # Binding Energy / Mixing
        # CV = k / sqrt(t)
        MIXING_CONSTANT_K = 0.15  # Empirical

        # Drying Kinetics (Exponential Decay)
        # M(t) = M0 * exp(-k*t)

        # ---- STOCHASTIC INPUTS (Manual Variability) ---
        # 1. Grinding
        # Batch size is strictly 1kg Target, but manual weighing error +/- 2%
        mass_batch = torch.normal(
            1.0, 0.02, (num_samples,), device=self.device)

        # Mixie Power (Commercial 750W unit)
        # Real load power fluctuates
        power_watts = torch.normal(
            550.0, 50.0, (num_samples,), device=self.device)

        # Grinding Time (Manual control)
        # User tries to hit 30s, but varies
        grind_time_sec = torch.normal(
            30.0, 5.0, (num_samples,), device=self.device)

        # Ambient Temp (Lab conditions)
        ambient_temp_k = torch.normal(
            298.0, 2.0, (num_samples,), device=self.device)

        # 2. Mixing
        # Mixing Time (Manual)
        mix_time_sec = torch.normal(
            120.0, 20.0, (num_samples,), device=self.device)

        # 3. Drying
        # Drying Time (Set by timer, but unloading varies)
        drying_time_sec = torch.normal(
            1800.0, 200.0, (num_samples,), device=self.device)
        # Drying Rate Constant (k) depends on Airflow/Temp uniformity in Tray Dryer
        k_drying = torch.normal(
            0.02, 0.005, (num_samples,), device=self.device)

        # ---- PHYSICS CALCULATIONS ----

        # A. Thermal Rise (Adiabatic approx for short burst)
        # Delta T = (P * t) / (m * Cp)
        delta_t = (power_watts * grind_time_sec) / (mass_batch * CP_J_KG_K)
        final_temp_k = ambient_temp_k + delta_t

        # B. Protein Denaturation (Arrhenius)
        # k = A * exp(-Ea / RT)
        # P = 1 - exp(-k * t)
        exponent = -ACTIVATION_ENERGY_J_MOL / \
            (GAS_CONSTANT_J_MOL_K * final_temp_k)
        rate_k = FREQUENCY_FACTOR_A * torch.exp(exponent)
        denaturation = 1.0 - torch.exp(-rate_k * grind_time_sec)
        denaturation = torch.clamp(denaturation, 0.0, 1.0)

        # C. Mixing Quality (CV)
        # CV = K / sqrt(t)
        cv = MIXING_CONSTANT_K / torch.sqrt(mix_time_sec)

        # D. Moisture Content
        # Initial M0 = 0.35 (35%)
        # M(t) = M0 * exp(-kt)
        m0 = 0.35
        moisture_final = m0 * torch.exp(-k_drying * drying_time_sec)

        # ---- COST CALCULATION (Per Batch) ----
        # Material: 1kg * 55
        material_cost = mass_batch * 55.0

        # Energy: kW * hr * rate
        # Grinding Energy
        e_grind_kwh = (power_watts * grind_time_sec) / 3600000.0
        # Mixing Energy (200W motor)
        e_mix_kwh = (200.0 * mix_time_sec) / 3600000.0
        # Drying Energy (2kW Heater)
        e_dry_kwh = (2000.0 * drying_time_sec) / 3600000.0

        total_energy_kwh = e_grind_kwh + e_mix_kwh + e_dry_kwh
        energy_cost = total_energy_kwh * 12.0  # Rate

        # Labor (Researcher Time) - Fixed per batch
        rnd_labor_cost = 300.0

        total_batch_cost = material_cost + energy_cost + rnd_labor_cost

        return {
            "denaturation": denaturation,
            "cv": cv,
            "moisture_final": moisture_final,
            "total_cost_batch": total_batch_cost,
            "temp_rise_c": delta_t
        }

    def run_analysis(self, num_samples=100_000_000):
        """Runs the R&D analysis with Batching for 100M simulations."""
        BATCH_SIZE = 5_000_000  # 5M per chunk to be safe on 4050
        num_batches = (num_samples // BATCH_SIZE) + 1

        print(
            f"\nRunning R&D Simulation (1kg Batch) - {num_samples} Iterations ({num_batches} Chunks)...")

        # Aggregators
        total_denat = 0.0
        max_denat = 0.0
        total_cv = 0.0
        total_cost = 0.0
        total_temp = 0.0
        max_temp = 0.0

        processed_samples = 0

        for i in range(num_batches):
            current_batch = min(BATCH_SIZE, num_samples - processed_samples)
            if current_batch <= 0:
                break

            results = self.simulate_1kg_batch(current_batch)

            # Accumulate Means (Weighted)
            total_denat += torch.sum(results["denaturation"]).item()
            total_cv += torch.sum(results["cv"]).item()
            total_cost += torch.sum(results["total_cost_batch"]).item()
            total_temp += torch.sum(results["temp_rise_c"]).item()

            # Track Extremes
            max_denat = max(max_denat, torch.max(
                results["denaturation"]).item())
            max_temp = max(max_temp, torch.max(results["temp_rise_c"]).item())

            processed_samples += current_batch
            # print(f"   Chunk {i+1}/{num_batches} done...", end='\r')

        mean_denat = total_denat / processed_samples
        mean_cv = total_cv / processed_samples
        mean_cost = total_cost / processed_samples
        mean_temp_rise = total_temp / processed_samples

        print("\n=== R&D METRICS (1kg Scale - 100M Extreme Sim) ===")
        print(f"Mean Denaturation: {mean_denat*100:.4f}%")
        print(f"Worst-Case Denaturation Seen: {max_denat*100:.4f}%")
        print(f"Mean Mixing CV: {mean_cv*100:.2f}% (Target < 5%)")
        print(f"Mean Batch Cost: INR {mean_cost:.2f}")
        print(f"Mean Temp Rise: +{mean_temp_rise:.1f} C")
        print(f"Absolute Max Temp Rise: +{max_temp:.1f} C")

        return results  # Returns last batch results for structure compatibility


if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"R&D Simulation Engine Initialized on {device}")
    sim = RndSimulationModule(device)
    sim.run_analysis()
