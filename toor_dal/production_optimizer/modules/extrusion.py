"""
Extrusion Module
Simulates Cold Extrusion (Pasta Tech) vs Hot Extrusion (Snack Tech).
"""
import torch


class ExtrusionModule:
    """
    Models the extrusion process.
    Type 0: Cold Extrusion (Single Screw, Pasta-like) -> Low CapEx, High Binder Req
    Type 1: Hot Extrusion (Twin Screw) -> High CapEx, Low Binder Req (Thermal Gelatinization)
    """

    def __init__(self, device):
        self.device = device

    def simulate(self, flow_rate_kg_hr, extrusion_type):
        """
        Simulate extrusion physics and costs.
        """
        # Using flow_rate just for batch size shape context
        _ = flow_rate_kg_hr
        # batch_size = flow_rate_kg_hr.shape[0]

        # --- CAPEX ---
        # Cold Extruder (Modified Vermicelli Machine): INR 1.5 Lakhs
        # Hot Extruder (Twin Screw 20kW): INR 15.0 Lakhs
        capex = torch.where(extrusion_type == 0,
                            torch.tensor(150000.0, device=self.device),
                            torch.tensor(1500000.0, device=self.device))

        # --- POWER ---
        # Cold: 5 HP (3.7 kW)
        # Hot: 30 HP (22 kW) - heaters + motor
        power_kw = torch.where(extrusion_type == 0,
                               torch.tensor(3.7, device=self.device),
                               torch.tensor(22.0, device=self.device))

        # --- BINDER REQUIREMENT (Hidden Cost) ---
        # Cold extrusion needs Alginate/Guar Gum to hold shape (INR 650/kg)
        # Hot extrusion gelatinizes starch naturally, needs less binder.
        # Cost Delta in Formulation:
        # Cold: 1.5% Binder -> INR 9.75/kg extra
        # Hot: 0.2% Binder -> INR 1.30/kg extra
        binder_penalty_per_kg = torch.where(extrusion_type == 0,
                                            # 9.75 - 1.30
                                            torch.tensor(
                                                8.45, device=self.device),
                                            torch.tensor(0.0, device=self.device))

        # --- RELIABILITY ---
        # Cold Extruder (Simple mech): 98% reliability
        # Hot Extruder (Complex electronics): 95% reliability
        failure_prob = torch.where(extrusion_type == 0, 0.02, 0.05)

        return {
            "capex": capex,
            "power_kw": power_kw,
            "binder_cost_delta": binder_penalty_per_kg,
            "failure_prob": failure_prob
        }
