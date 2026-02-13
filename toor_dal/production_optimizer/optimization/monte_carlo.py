"""
Monte Carlo Optimizer
Orchestrates the large-scale simulation of the production line.
"""
import torch
from ..core.gpu_engine import get_device, get_uniform_tensor, set_precision
from ..core.cost_model import calculate_total_cost, calculate_effective_output
from ..modules.grinding import GrindingModule
from ..modules.drying import DryingModule
from ..modules.extrusion import ExtrusionModule
from ..modules.formulation import FormulationModule
from ..core.config import (
    NUM_BATCHES, RAW_MATERIAL_COST_INR_KG, ELECTRICITY_RATE_INR_KWH,
    HEAT_PUMP_COP, AMBIENT_TEMP_KELVIN, MIXIE_UNIT_FAILURE_PROB
)


class MonteCarloOptimizer:
    """
    Main engine for running Monte Carlo simulations of the manufacturing process.
    """

    def __init__(self):
        # Enforce Double Precision for Arrhenius stability
        set_precision(True)
        self.device = get_device()
        self.grinder = GrindingModule(self.device)
        self.dryer = DryingModule(self.device)
        self.extruder = ExtrusionModule(self.device)
        self.formulator = FormulationModule(self.device)
        self.n_samples = NUM_BATCHES
        self.results = {}

    def run_simulation(self, custom_params=None):
        """
        Runs the MC Simulation.

        Args:
            custom_params (dict): Dict of parameter overrides (Tensors or Scalars) 
                                  to inject for sensitivity analysis.

        Returns:
            dict: Simulation results and sensitivity parameter tracking.
        """
        # If no custom params, run standard baseline logic

        # 1. Generate Input Parameters (Baseline)
        feed_rate = get_uniform_tensor(50.0, 500.0, NUM_BATCHES, self.device)
        grinder_type = torch.randint(
            0, 3, (NUM_BATCHES,), device=self.device).double()
        duty_cycle = get_uniform_tensor(0.05, 0.5, NUM_BATCHES, self.device)
        dryer_type = torch.randint(
            0, 2, (NUM_BATCHES,), device=self.device).double()

        actual_duty_cycle = torch.where(
            grinder_type < 2, torch.tensor(1.0, device=self.device), duty_cycle)

        # --- Handle Sensitivity Parameters ---
        # We prepare a 'params' dict to pass down
        params = {}

        # 1. Material Cost ~ N(55, 7)
        if custom_params and 'material_cost' in custom_params:
            p_mat_cost = custom_params['material_cost']
        else:
            p_mat_cost = torch.normal(
                RAW_MATERIAL_COST_INR_KG, 7.0, (NUM_BATCHES,), device=self.device)
        params['material_cost'] = p_mat_cost

        # 2. Electricity ~ N(12, 1.5)
        if custom_params and 'electricity_rate' in custom_params:
            p_elec = custom_params['electricity_rate']
        else:
            p_elec = torch.normal(ELECTRICITY_RATE_INR_KWH,
                                  1.5, (NUM_BATCHES,), device=self.device)
        params['electricity_rate'] = p_elec

        # 3. Ambient Temp ~ N(298, 5)
        if custom_params and 'ambient_temp_k' in custom_params:
            p_amb = custom_params['ambient_temp_k']
        else:
            p_amb = torch.normal(AMBIENT_TEMP_KELVIN, 5.0,
                                 (NUM_BATCHES,), device=self.device)
        params['ambient_temp_k'] = p_amb

        # 4. Unit Failure ~ N(0.02, 0.005)
        if custom_params and 'unit_failure_rate' in custom_params:
            p_fail = custom_params['unit_failure_rate']
        else:
            p_fail = torch.normal(MIXIE_UNIT_FAILURE_PROB,
                                  0.005, (NUM_BATCHES,), device=self.device)
            p_fail = torch.clamp(p_fail, 0.0, 1.0)
        params['unit_failure_rate'] = p_fail

        # 5. COP ~ N(3.5, 0.4)
        if custom_params and 'heat_pump_cop' in custom_params:
            p_cop = custom_params['heat_pump_cop']
        else:
            p_cop = torch.normal(HEAT_PUMP_COP, 0.4,
                                 (NUM_BATCHES,), device=self.device)
        params['heat_pump_cop'] = p_cop

        # 3. Extrusion Strategy (0: Cold/Pasta, 1: Hot/TwinScrew)
        extrusion_type = torch.randint(
            0, 2, (self.n_samples,), device=self.device).float()

        # 4. Formulation Hack (Rice Substitution Ratio 0% to 50%)
        # Uniform distribution between 0.0 and 0.5
        rice_ratio = torch.rand((self.n_samples,), device=self.device) * 0.5

        # --- Run Simulations with Params ---
        # A. Formulation
        f_results = self.formulator.simulate(self.n_samples, rice_ratio)

        # B. Machinery
        g_results = self.grinder.simulate(
            feed_rate, grinder_type, actual_duty_cycle, params)

        e_results = self.extruder.simulate(feed_rate, extrusion_type)

        d_results = self.dryer.simulate(
            feed_rate, 35.0, 10.0, dryer_type, params)

        # --- Aggregation ---
        # CAPEX: Grinder + Extruder + Dryer + Ancillary(50k)
        total_capex = g_results['capex'] + \
            e_results['capex'] + d_results['capex'] + 50000.0

        # POWER
        total_power = g_results['power_kw'] + \
            e_results['power_kw'] + d_results['power_kw']

        # WEAR
        total_wear = g_results['wear_cost']

        # OPEX PENALTIES (Binder cost from cold extrusion)
        binder_cost = e_results['binder_cost_delta']

        rnd_cost = torch.where(grinder_type == 2.0, 500000.0, 100000.0)

        # Total Defect Probability
        # Protein damage + Quality fail from low protein
        total_defect = g_results['denaturation'] + \
            f_results['quality_fail'] + 0.005

        # Reliability
        grinder_fail = g_results['system_failure_prob']
        extruder_fail = e_results['failure_prob']
        dryer_fail = d_results['catastrophic_prob']

        # Union of failures: P(Total) = 1 - (1-Pg)(1-Pe)(1-Pd)
        # Using product of survival probabilities
        p_survival = (1.0 - grinder_fail) * \
            (1.0 - extruder_fail) * (1.0 - dryer_fail)
        total_downtime = 1.0 - p_survival

        # Clamp to 1.0max (though formula guarantees <=1)
        total_downtime = torch.clamp(total_downtime, 0.0, 1.0)

        # Effective Output
        effective_output = calculate_effective_output(
            feed_rate, total_defect, total_downtime)

        # Update Params with optimized material cost
        params['material_cost'] = f_results['d_material_cost'] + binder_cost

        total_cost_hr = calculate_total_cost(
            total_capex,
            total_power,
            feed_rate,
            total_defect,
            rnd_cost,
            total_wear,
            params  # Includes formulation & binder costs
        )

        # Objective Score
        score = effective_output / (total_cost_hr + 1e-6)
        unit_cost = total_cost_hr / (effective_output + 1e-6)

        self.results = {
            "feed_rate": feed_rate,
            "grinder_type": grinder_type,
            "dryer_type": dryer_type,
            "extrusion_type": extrusion_type,
            "rice_ratio": rice_ratio,
            "duty_cycle": actual_duty_cycle,
            "score": score,
            "unit_cost": unit_cost,
            "downtime": total_downtime,
            "protein_damage": g_results['denaturation'],
            "final_protein_content": f_results['protein_pct'],
            # Stored Params for Sensitivity Analysis
            "p_material_cost": params['material_cost'],
            "p_electricity_rate": params['electricity_rate'],
            "p_ambient_temp": params['ambient_temp_k'],
            "p_unit_failure": params['unit_failure_rate'],
            "p_sys_failure_prob": grinder_fail,
            "p_cop": params['heat_pump_cop']
        }

        return self.results

    def analyze_robustness(self):
        """
        Analyzes results by Equipment Group to find the Robust Winner.
        """
        r = self.results

        print("\n--- ROBUSTNESS ANALYSIS (Mean Performance) ---")
        g_names = ["Ball Mill", "Hammer Mill", "Mixie Cluster"]

        for g_idx in [0, 1, 2]:
            mask = (r["grinder_type"] == g_idx)
            count = mask.sum().item()
            if count == 0:
                continue

            avg_score = r["score"][mask].mean().item()
            avg_cost = r["unit_cost"][mask].mean().item()
            avg_downtime = r["downtime"][mask].mean().item()
            avg_damage = r["protein_damage"][mask].mean().item()

            print(f"\nConfiguration: {g_names[g_idx]}")
            print(f"  Samples: {count}")
            print(f"  Mean Score: {avg_score:.4f}")
            print(f"  Mean Unit Cost: INR {avg_cost:.2f} / kg")
            print(f"  Resultant Downtime: {avg_downtime:.2%}")
            print(f"  Protein Damage: {avg_damage:.6%}")

        print("\n--- STRESS TEST: HIGH FAILURE RATE SCENARIO ---")
        mask_mixie = (r["grinder_type"] == 2)
        worst_case_downtime = torch.quantile(
            r["downtime"][mask_mixie], 0.95).item()
        print(
            f"  Mixie Cluster 95% Worst-Case Downtime: {worst_case_downtime:.2%}")

    def get_sensitivity_data(self):
        """Returns the result dict."""
        return self.results
