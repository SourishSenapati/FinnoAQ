"""
Linear Programming Formulation Optimizer (GPU).
Uses Monte Carlo to find the "Jugaad Blend" that minimizes cost while maximizing:
1. Fiber (Using Spent Spices)
2. Protein (Using Non-GMO Soya)
3. Softness (Using Enzyme-Active Wheat)
"""
import torch
from config import GRAIN_PRICES, GRAIN_NUTRITION, TARGETS, MAX_LIMITS


class MultigrainOptimizer:
    def __init__(self, device='cuda'):
        self.device = device
        self.grains = list(GRAIN_NUTRITION.keys())
        self.nutrients = torch.tensor([GRAIN_NUTRITION[g] for g in self.grains],
                                      device=self.device, dtype=torch.float32)
        # Columns: Protein, Fiber, Cost

    def suggest_optimal_blend(self, batch_size=10_000):
        """
        Generates random blends, checks strict constraints, finds cheapest winner.
        """
        # 1. Generate Random Weights (Dirichlet creates sum=1.0)
        # We assume 11 ingredients.
        # However, we bias towards Wheat (First 2 ingredients) to be 60-80%
        # Remaining < 40% distributed amongst others.

        # Method:
        # Wheat ~ Uniform(0.6, 0.85)
        # Others ~ Uniform(0.0, 0.4) normalized

        wheat_soft = torch.rand(
            batch_size, device=self.device) * 0.25 + 0.45  # 45-70%
        wheat_hard = torch.rand(
            batch_size, device=self.device) * 0.15 + 0.05  # 5-20%

        remaining_budget = 1.0 - (wheat_soft + wheat_hard)

        # Generate random for remaining 9 ingredients
        other_weights = torch.rand(batch_size, 9, device=self.device)
        other_sum = torch.sum(other_weights, dim=1, keepdim=True)
        other_weights = (other_weights / other_sum) * \
            remaining_budget.unsqueeze(1)

        # Combine
        # Order must match self.grains:
        # wheat_soft, wheat_hard, maize, bajra, jowar, ragi, soybean_nongmo,
        # chana, oats, spent_turmeric, spent_fenugreek

        all_weights = torch.cat([
            wheat_soft.unsqueeze(1),
            wheat_hard.unsqueeze(1),
            other_weights
        ], dim=1)

        # 2. Calculate Nutritional & Cost Profile
        # Matrix Multiplication: (Batch x Ingredients) @ (Ingredients x Attributes)
        # Shape: (Batch x 3) => Protein, Fiber, Cost
        profiles = torch.matmul(all_weights, self.nutrients)

        protein = profiles[:, 0]
        fiber = profiles[:, 1]
        cost = profiles[:, 2]

        # 3. Apply Constraints
        # A. Cost / Protein / Fiber
        valid_mask = (cost < TARGETS["cost_per_kg"]) & \
                     (protein > TARGETS["protein_min"]) & \
                     (fiber > TARGETS["fiber_min"])

        # B. Sensory Limits (CRITICAL)
        # We need to map column indices to grain names.
        # self.grains list order corresponds to columns of all_weights

        for grain_name, limit in MAX_LIMITS.items():
            if grain_name in self.grains:
                idx = self.grains.index(grain_name)
                # Check if this grain's weight is <= limit
                grain_weights = all_weights[:, idx]
                valid_mask = valid_mask & (grain_weights <= limit)

        # If no valid blend found, relax constraints slightly or pick best
        num_valid = torch.sum(valid_mask).item()

        if num_valid == 0:
            return None, cost.min().item()

        # 4. Pick Cheapest Valid Blend
        valid_indices = torch.nonzero(valid_mask).squeeze()
        if valid_indices.dim() == 0:  # Only 1 result
            best_idx = valid_indices
        else:
            # Among valid, minimize cost
            valid_costs = cost[valid_indices]
            min_cost_idx = torch.argmin(valid_costs)
            best_idx = valid_indices[min_cost_idx]

        final_weights = all_weights[best_idx]
        final_metrics = profiles[best_idx]

        return {
            "blend": dict(zip(self.grains, final_weights.tolist())),
            "cost": final_metrics[2].item(),
            "protein": final_metrics[0].item(),
            "fiber": final_metrics[1].item()
        }, final_metrics[2].item()
