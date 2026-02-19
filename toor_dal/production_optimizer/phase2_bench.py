"""
Phase 2: Low-Cost Bench Validation Simulation
Objective: Validate Structural Feasibility, Boiling Stability, and Cost Reproducibility
Simulates 100,000 "Bench Batches" (Manual Mixing, Tray Drying)
"""
import torch
import time


def run_phase2_bench_validation(num_batches=100_000_000, device=None):
    # Auto-detect device
    if device is None:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

    BATCH_SIZE = 5_000_000
    total_chunks = (num_batches // BATCH_SIZE) + 1

    print(
        f"\nRunning Phase 2 Bench Validation on {device.upper()} with {num_batches} batches ({total_chunks} Chunks)...")

    if device == 'cuda':
        d = torch.device('cuda')
    else:
        d = torch.device('cpu')

    start_time_t = time.time()

    # Aggregators
    total_failures = 0
    total_boil_fails = 0
    total_texture_fails = 0
    processed_count = 0

    for i in range(total_chunks):
        current_batch_size = min(BATCH_SIZE, num_batches - processed_count)
        if current_batch_size <= 0:
            break

        # --- 1. SET INPUTS (From Phase 1 Results) ---
        target_tur = 53.3
        target_starch = 42.3
        target_alginate = 0.72
        target_calcium = 0.60

        # --- 2. SIMULATE MANUAL PROCESS VARIABILITY ---
        mix_cv = 0.20  # 20% variance due to manual mixing
        mixing_efficiency = torch.normal(
            mean=1.0, std=mix_cv, size=(current_batch_size,), device=d)
        mixing_efficiency = torch.clamp(mixing_efficiency, 0.1, 1.5)

        local_alginate = target_alginate * mixing_efficiency
        local_calcium = target_calcium * mixing_efficiency

        hydration_water = torch.normal(
            mean=300.0, std=15.0, size=(current_batch_size,), device=d)

        drying_stress = torch.normal(
            mean=1.2, std=0.1, size=(current_batch_size,), device=d)

        # --- 3. PHYSICS MODELS (Boiling Stability) ---
        p_swell_base = (target_starch / 42.3) * (300.0 / hydration_water)
        gel_strength = (local_alginate / 1.2) * 2.5 * (1.0 / drying_stress)

        # --- 4. FAILURE ANALYSIS ---
        failed_boil = p_swell_base > gel_strength
        failed_texture = (hydration_water > 330.0) | (gel_strength < 0.8)
        failed_hard = (hydration_water < 270.0)
        any_failure = failed_boil | failed_texture | failed_hard

        # Accumulate
        total_failures += torch.sum(any_failure).item()
        total_boil_fails += torch.sum(failed_boil).item()
        total_texture_fails += torch.sum(failed_texture).item()
        processed_count += current_batch_size

        # Explicit Memory Cleanup
        del mixing_efficiency, hydration_water, drying_stress, p_swell_base, gel_strength
        del failed_boil, failed_texture, failed_hard, any_failure
        # torch.cuda.empty_cache() # Optional, slows down if called too often

    # --- 5. COST VALIDATION (Bench Scale Reality) ---
    cost_material_bench = 56.02 * 1.05
    cost_labor_bench = 200.0
    total_cost_per_batch = cost_material_bench + cost_labor_bench

    # --- Report ---
    success_rate = 100.0 * (1.0 - (total_failures / processed_count))

    print(f"\n--- BENCH VALIDATION RESULTS ({processed_count} Batches) ---")
    print(f"Simulation of Manual Mixing, Tray Drying, & Boiling")
    # 4 decimals for 6 Sigma precision
    print(f"Success Rate:   {success_rate:.4f}%")
    print(
        f"Boil Failures:  {int(total_boil_fails)} ({total_boil_fails/processed_count*100:.4f}%) - 'Soup' Risk")
    print(
        f"Texture Fails:  {int(total_texture_fails)} - 'Mushy/Sticky'")

    print(f"\n[CRITICAL INSIGHTS]")
    if success_rate < 99.0:  # Stricter for high volume
        print("WARNING: Manual variability is too high for 6 Sigma standards.")
        print("Recommendation: Increase Alginate to 0.85% or improve Mixing CV.")
    else:
        print("PASS: Formulation is robust enough for manual bench trials.")

    print(f"\n[R&D BUDGET CHECK]")
    print(f"Cost per Trial Batch (1kg): INR {total_cost_per_batch:.2f}")
    print(f"Est. 200 Trials Cost: INR {total_cost_per_batch * 200:.2f}")

    print(f"Compute Time: {time.time() - start_time_t:.4f}s")


if __name__ == "__main__":
    run_phase2_bench_validation()
