"""
Main Simulation Runner for Multigrain Atta (100M Iterations).
Integrates Formulation, Machinery, and Quality Physics.
"""
import time
import torch
from formulation_optimizer import MultigrainOptimizer
from machinery_specs import simulate_grinding_energy
from config import TARGETS, MAX_LIMITS


def run_simulation():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"--- MULTIGRAIN ATTA SIMULATION (GPU: {device}) ---")

    # Optimize Blend (Monte Carlo)
    optimizer = MultigrainOptimizer(device=device)

    # Loop Logic 100M (Batched)
    BATCH_SIZE = 5_000_000
    TOTAL = 100_000_000
    LOOPS = TOTAL // BATCH_SIZE

    total_valid_blends = 0
    best_blend = None
    min_cost_seen = float('inf')

    print(
        f"Phase 1: Formula Optimization ({TOTAL} Iterations in {LOOPS} chunks)...")

    start_t = time.time()
    for _ in range(LOOPS):
        # Generate 5M blends per loop
        # Check validity & Cost
        # Since generating 5M weights consumes ~500MB VRAM, safe.
        with torch.no_grad():
            # Minimal wrapper to use the class method effectively
            # Config now has 14 ingredients total (Wheat Soft/Hard + 12 others).
            # Wheat Soft, Wheat Hard (First 2)
            # Remaining 12 ingredients:
            # Maize, Bajra, Jowar, Ragi, Barley, Soybean, Chana, Vital_Gluten, Oats,
            # Turmeric, Fenugreek, Cumin

            wheat_soft = torch.rand(BATCH_SIZE, device=device) * 0.25 + 0.45
            wheat_hard = torch.rand(BATCH_SIZE, device=device) * 0.15 + 0.05
            remaining = 1.0 - (wheat_soft + wheat_hard)

            # Generate for remaining 12 ingredients with BIAS
            # Bias indices:
            # 0:Maize, 5:Soybean, 7:VitalWheatGluten, 10:Fenugreek
            bias_vector = torch.tensor(
                [5.0, 1.0, 1.0, 1.0, 1.0, 4.0, 1.0, 3.0, 1.0, 1.0, 5.0, 1.0], device=device)

            others = torch.rand(BATCH_SIZE, 12, device=device) * bias_vector
            others = (others / others.sum(dim=1, keepdim=True)) * \
                remaining.unsqueeze(1)

            w_tens = torch.cat([wheat_soft.unsqueeze(
                1), wheat_hard.unsqueeze(1), others], dim=1)

            # Physics Calculation (Nutrients)
            profiles = torch.matmul(w_tens, optimizer.nutrients)
            proteins = profiles[:, 0]
            fibers = profiles[:, 1]
            costs = profiles[:, 2]

            # Constraints (Nutrition & Cost)
            # Add minimal gluten requirement check if possible, or assume 2% bias handles it.
            # We strictly enforce gluten percent in sensory loop.
            valid = (costs < TARGETS["cost_per_kg"]) & \
                    (proteins > TARGETS["protein_min"]) & \
                    (fibers > TARGETS["fiber_min"])

            # Constraints (Sensory Limits)
            # Constraints (Sensory Limits)
            for g_name, limit in MAX_LIMITS.items():
                if g_name in optimizer.grains:
                    g_idx = optimizer.grains.index(g_name)
                    valid &= (w_tens[:, g_idx] <= limit)

            count = valid.sum().item()
            total_valid_blends += count

            if count > 0:
                # Find best in this batch
                batch_min_val, batch_min_idx = torch.min(costs[valid], dim=0)
                if batch_min_val < min_cost_seen:
                    min_cost_seen = batch_min_val.item()
                    # Map back to original index
                    real_idx = torch.nonzero(valid).squeeze()[batch_min_idx]
                    best_weights = w_tens[real_idx].cpu().tolist()
                    best_blend = dict(zip(optimizer.grains, best_weights))

    sim_time = time.time() - start_t

    print("--- RESULTS ---")
    print(f"Simulated Blends: {TOTAL}")
    print(
        f"Valid Blends Found: {total_valid_blends} ({total_valid_blends/TOTAL*100:.4f}%)")
    print(f"Execution Time: {sim_time:.2f}s")

    if best_blend:
        print("\n--- OPTIMAL 'JUGAAD' FORMULATION ---")
        print(f"Cost: INR {min_cost_seen:.2f}/kg (Target < 30)")
        print("Composition:")
        for grain, pct in best_blend.items():
            if pct > 0.001:  # Filter trace < 0.1%
                print(f"  - {grain.replace('_', ' ').title()}: {pct*100:.1f}%")

        # Calculate final macros
        w_tensor = torch.tensor(list(best_blend.values()), device=device)
        final_macros = torch.matmul(w_tensor, optimizer.nutrients)
        print("\n--- FINAL MACROS ---")
        print(f"Protein: {final_macros[0]:.1f}% (Target > 12%)")
        print(
            f"Fiber:   {final_macros[1]:.1f}% (Target > 10%) - Boosted by Spent Spices!")

        # Phase 2: Machinery Simulation
        print("\n--- MACHINERY ECONOMICS ---")
        lab_sim = simulate_grinding_energy("lab", 5.0)
        ind_sim = simulate_grinding_energy("industrial", 2000.0)

        print("Lab Scale (5kg/hr):")
        print(f"  - Power: {lab_sim['power_draw_kw']:.2f} kW")
        print(f"  - Cost:  INR {lab_sim['cost_inr_kg']:.2f}/kg")

        print("Industrial Scale (2000kg/hr):")
        print(f"  - Power: {ind_sim['power_draw_kw']:.1f} kW")
        print(f"  - Cost:  INR {ind_sim['cost_inr_kg']:.2f}/kg")

        total_verify = min_cost_seen + \
            ind_sim['cost_inr_kg'] + 1.5  # Packaging
        print("\n--- FINAL VERDICT ---")
        print(f"Total Factory Gate Cost: INR {total_verify:.2f}/kg")
        msg = (
            "POSSIBLE" if total_verify < 24.0
            else "TIGHT margin (Direct to Consumer only)"
        )
        print(f"Retail Feasibility @ 30 INR: {msg}")


if __name__ == "__main__":
    run_simulation()
