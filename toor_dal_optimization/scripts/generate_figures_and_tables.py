"""
Reproducible Analysis Figures & Tables Generator.
Compiles all numerical simulation results, Monte Carlo distributions,
and Pareto trade-off frontiers into artifacts/reproducible_figures_and_tables.json.
"""

import os
import sys
import json
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.finnoaq.gpu_engine import GPUAccelerationEngine
from src.finnoaq.virtual_screening import VirtualScreeningPipeline
from src.finnoaq.digital_twin import ClosedLoopDigitalTwin

def generate_reproducible_artifacts(artifacts_dir: str = "artifacts"):
    os.makedirs(artifacts_dir, exist_ok=True)
    
    # 1. GPU Simulations
    gpu_engine = GPUAccelerationEngine()
    hw_status = gpu_engine.get_hardware_status()
    pde_res = gpu_engine.solve_coupled_radial_diffusion_pde(time_steps=100)
    mc_res = gpu_engine.run_gpu_monte_carlo_sensitivity(num_samples=50000)
    pareto_gpu = gpu_engine.gpu_vectorized_pareto_ranking(population_size=2000)
    
    # 2. Virtual Screening
    screener = VirtualScreeningPipeline()
    candidates = screener.generate_candidate_design_space()
    screen_results = screener.screen_and_optimize(candidates)
    pareto_candidates = [
        {
            "treatment_id": r.treatment_id,
            "predicted_whistles": r.predicted_whistles,
            "cooking_time_reduction_pct": r.cooking_time_reduction_pct,
            "predicted_firmness_n": r.predicted_firmness_n,
            "sensory_hedonic_score": r.sensory_hedonic_score,
            "available_lysine_retention_pct": r.available_lysine_retention_pct,
            "opex_inr_per_kg": r.opex_inr_per_kg,
            "process_yield_pct": r.process_yield_pct
        }
        for r in screen_results if r.is_pareto_optimal
    ]
    
    # 3. Scale-Up Balances
    twin = ClosedLoopDigitalTwin()
    scale_5tph = twin.simulate_industrial_scale_unit_operations(5.0)
    
    artifact_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "hardware_telemetry": hw_status,
        "table_1_gpu_pde_diffusion": pde_res,
        "table_2_gpu_monte_carlo_sensitivity_n50000": mc_res,
        "table_3_gpu_pareto_vectorized_sorting": pareto_gpu,
        "table_4_pareto_optimal_technological_candidates": pareto_candidates,
        "table_5_industrial_scaleup_mass_energy_balance": scale_5tph
    }
    
    out_json = os.path.join(artifacts_dir, "reproducible_figures_and_tables.json").replace("\\", "/")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(artifact_payload, f, indent=2)
        
    print(f"[ARTIFACTS] Reproducible figures & tables written to {out_json}")
    return out_json

if __name__ == "__main__":
    generate_reproducible_artifacts()
