"""
Formulation Module
Models the 'Dilution Hack': Substituting Tur Khanda with Broken Rice.
"""
import torch


class FormulationModule:
    """
    Optimizes the recipe matrix.
    Standard: 100% Tur Khanda (INR 65/kg)
    Hacked: 50% Tur + 50% Rice (INR 28/kg) + Flavor/Color adjustment
    """

    def __init__(self, device):
        self.device = device

    def simulate(self, batch_size, substitution_ratio):
        """
        Simulate formulation costs.
        substitution_ratio: 0.0 to 0.5 (Percentage of Rice)
        """
        # Costs
        cost_tur = 65.0
        cost_rice = 28.0

        # Base Material Cost
        # mix = (1 - ratio) * 65 + ratio * 28
        material_cost = (1.0 - substitution_ratio) * \
            cost_tur + (substitution_ratio) * cost_rice

        # Flavor Penalty (Need more MSG/Spices if diluted)
        # Linear approximation: + INR 2/kg for every 10% dilution
        flavor_cost = (substitution_ratio * 10.0) * 2.0

        # Quality Score Penalty (Protein Content Drop)
        # Tur: 22% Protein, Rice: 7% Protein
        # If protein drops too low, it's not 'Dal Analogue' anymore.
        protein_content = (1.0 - substitution_ratio) * \
            22.0 + (substitution_ratio) * 7.0

        # Binary feasibility: If Protein < 18%, it's a FAIL (Consumer rejects)
        # But for 'Street Food' grade, maybe 15% is okay?
        # Let's assume strict penalty if < 18%
        quality_penalty = torch.where(protein_content < 15.0,
                                      # 100% Penalty
                                      torch.tensor(1.0, device=self.device),
                                      torch.tensor(0.0, device=self.device))

        total_formulation_cost = material_cost + flavor_cost

        return {
            "d_material_cost": total_formulation_cost,
            "protein_pct": protein_content,
            "quality_fail": quality_penalty
        }
