"""
Drying Module
Simulates the drying stage of Toor Dal production, comparing Electric vs Heat Pump dryers.
"""
import torch
from ..core.config import (
    HEAT_PUMP_COP, ELECTRIC_HEATER_COP,
    LATENT_HEAT_WATER_KJ_KG
)


class DryingModule:
    """
    Simulates energy consumption and physics of the drying process.
    """

    def __init__(self, device):
        self.device = device

    def simulate(self, feed_rate_kg_hr, initial_moisture_pct, target_moisture_pct, dryer_type, params=None):
        """
        Simulates Drying Process.

        Args:
            feed_rate_kg_hr (torch.Tensor): Feed rate in kg/hr.
            initial_moisture_pct (float): Starting moisture %.
            target_moisture_pct (float): Target moisture %.
            dryer_type (torch.Tensor): 0.0=Electric, 1.0=Heat Pump.
            params (dict, optional): Sensitivity analysis parameter overrides.

        Returns:
            dict: Contains 'capex', 'power_kw', 'wear_cost', 'catastrophic_prob'.
        """
        batch_size = feed_rate_kg_hr.shape[0]

        # Water Calc
        # Evaporation load
        water_evap_kg_hr = feed_rate_kg_hr * \
            (initial_moisture_pct - target_moisture_pct) / 100.0

        # Energy Requirement (Latent Heat)
        energy_req_kj_hr = water_evap_kg_hr * LATENT_HEAT_WATER_KJ_KG

        # COP Handling with Overrides
        if params and 'heat_pump_cop' in params:
            hp_cop_tensor = params['heat_pump_cop']
        else:
            hp_cop_tensor = torch.full(
                (batch_size,), HEAT_PUMP_COP, device=self.device)

        # Electric Heater COP usually constant ~1.0 or 0.9
        elec_cop = ELECTRIC_HEATER_COP

        # Select COP
        cop = torch.where(dryer_type == 0.0, elec_cop, hp_cop_tensor)

        # Power Calculation (kW)
        # Power = Energy / (3600 * COP)
        power_kw = (energy_req_kj_hr / 3600.0) / cop

        # CapEx (Static or Varied?)
        # Let's keep CapEx static for now unless requested
        capex = torch.where(dryer_type == 0.0, 150000.0, 450000.0)

        # Failure Prob
        # Electric heaters moderate risk, HP low risk
        prob_failure = torch.where(dryer_type == 0.0, 0.005, 0.001)

        return {
            "capex": capex,
            "power_kw": power_kw,
            "wear_cost": torch.zeros(batch_size, device=self.device),
            "catastrophic_prob": prob_failure
        }
