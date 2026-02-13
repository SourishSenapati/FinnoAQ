"""
Grinding Module
Simulates the grinding stage, modeling Ball Mills, Hammer Mills, and Mixie Clusters.
Includes physics for temperature rise, protein denaturation, and reliability.
"""
import torch
from ..core.physics_models import (
    calculate_temp_rise_convection,
    calculate_arrhenius_denaturation_phys
)
from ..core.config import (
    AMBIENT_TEMP_KELVIN,
    BALL_MILL_CAPEX, BALL_MILL_POWER_KW, BALL_MILL_WEAR_INR_HR, BALL_MILL_FAILURE_PROB,
    HAMMER_MILL_CAPEX, HAMMER_MILL_POWER_KW, HAMMER_MILL_WEAR_INR_HR, HAMMER_MILL_FAILURE_PROB,
    MIXIE_UNIT_CAPEX, MIXIE_UNIT_POWER_KW_PEAK, MIXIE_UNIT_WEAR_INR_HR, MIXIE_UNIT_FAILURE_PROB,
    MIXIE_CLUSTER_SIZE
)


class GrindingModule:
    """
    Simulates the Grinding Process including thermal physics and reliability logic.
    """

    def __init__(self, device):
        self.device = device

    def simulate(self, feed_rate_kg_hr, grinder_type, duty_cycle, params=None):
        """
        Simulates the Grinding Process.

        Args:
            feed_rate_kg_hr (torch.Tensor): Throughput.
            grinder_type (torch.Tensor): 0=Ball Mill, 1=Hammer Mill, 2=Mixie Cluster.
            duty_cycle (torch.Tensor): Duty cycle (0.0 to 1.0).
            params (dict, optional): Sensitivity overrides.

        Returns:
            dict: Simulation results (capex, power, temps, denaturation, failure_prob).
        """
        batch_size = feed_rate_kg_hr.shape[0]

        # Retrieve Overrides if present
        if params:
            p_ambient_k = params.get('ambient_temp_k', AMBIENT_TEMP_KELVIN)
            p_unit_failure = params.get(
                'unit_failure_rate', MIXIE_UNIT_FAILURE_PROB)
        else:
            p_ambient_k = AMBIENT_TEMP_KELVIN
            p_unit_failure = MIXIE_UNIT_FAILURE_PROB

        # Ensure p_ambient_k is tensor
        if isinstance(p_ambient_k, float):
            ambient_t = torch.normal(
                p_ambient_k, 2.0, (batch_size,), device=self.device)
        else:
            ambient_t = p_ambient_k  # Already tensor

        # Initialize Output Tensors
        capex = torch.zeros(batch_size, device=self.device)
        power_watts = torch.zeros(batch_size, device=self.device)
        wear_cost_hr = torch.zeros(batch_size, device=self.device)
        system_failure_prob = torch.zeros(batch_size, device=self.device)

        # --- Ball Mill (Type 0) ---
        mask_bm = grinder_type == 0
        capex[mask_bm] = BALL_MILL_CAPEX
        power_watts[mask_bm] = BALL_MILL_POWER_KW * 1000.0
        wear_cost_hr[mask_bm] = BALL_MILL_WEAR_INR_HR
        # Single unit assumption
        system_failure_prob[mask_bm] = BALL_MILL_FAILURE_PROB

        # --- Hammer Mill (Type 1) ---
        mask_hm = grinder_type == 1
        capex[mask_hm] = HAMMER_MILL_CAPEX
        power_watts[mask_hm] = HAMMER_MILL_POWER_KW * 1000.0
        wear_cost_hr[mask_hm] = HAMMER_MILL_WEAR_INR_HR
        system_failure_prob[mask_hm] = HAMMER_MILL_FAILURE_PROB

        # --- Mixie Cluster (Type 2) ---
        mask_mx = grinder_type == 2
        cluster_size = MIXIE_CLUSTER_SIZE

        capex[mask_mx] = MIXIE_UNIT_CAPEX * cluster_size
        power_watts[mask_mx] = (
            MIXIE_UNIT_POWER_KW_PEAK * 1000.0) * duty_cycle[mask_mx] * cluster_size
        wear_cost_hr[mask_mx] = MIXIE_UNIT_WEAR_INR_HR * cluster_size

        # Reliability: P_sys = 1 - (1 - p)^N
        # Use p_unit_failure (Simulated or param)
        if isinstance(p_unit_failure, float):
            p_unit_sample = torch.normal(
                p_unit_failure, 0.005, (batch_size,), device=self.device)
        else:
            # If tensor passed, use it directly (already distributed)
            p_unit_sample = p_unit_failure

        p_unit_sample = torch.clamp(p_unit_sample, 0.0, 1.0)

        sys_fail = 1.0 - torch.pow((1.0 - p_unit_sample), cluster_size)
        system_failure_prob[mask_mx] = sys_fail[mask_mx]

        # --- Physics Simulation ---
        mass_per_charge = torch.normal(
            0.5, 0.05, (batch_size,), device=self.device)
        power_per_unit = torch.where(
            mask_mx, MIXIE_UNIT_POWER_KW_PEAK * 1000.0, power_watts)

        cycle_time = 60.0
        on_time = cycle_time * duty_cycle

        # Temp Rise
        delta_t = calculate_temp_rise_convection(
            power_per_unit, on_time, mass_per_charge, ambient_t, self.device)
        final_temp_k = ambient_t + delta_t

        # Denaturation
        denaturation = calculate_arrhenius_denaturation_phys(
            final_temp_k, on_time, self.device)

        # Override for mills
        denaturation[mask_bm] = 0.0
        denaturation[mask_hm] = 0.12

        final_temp_c = final_temp_k - 273.15

        return {
            "capex": capex,
            "power_kw": power_watts / 1000.0,
            "wear_cost": wear_cost_hr,
            "temp_c": final_temp_c,
            "denaturation": denaturation,
            "system_failure_prob": system_failure_prob
        }
