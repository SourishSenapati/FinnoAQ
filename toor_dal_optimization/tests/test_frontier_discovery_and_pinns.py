"""
FinnoaQ Toor Dal — Unit and Integration Tests for Frontier Discovery Engine.
Tests:
1. High-Resolution 2D Spatial Solver & Grid Convergence
2. Physics-Informed Neural Network (PINN) Forward & Inverse Solver
3. Scientific Transformer Surrogate & Out-of-Distribution (OOD) Guardrail
4. Molecular-to-Continuum Biophysical Architecture
5. Goal-Locked Two-Stage Project Objectives & Stage 2 Lock
"""

import os
import yaml
import pytest
from src.finnoaq.high_res_spatial_solver import HighResSpatialSolver
from src.finnoaq.pinn_solver import PINNSolver
from src.finnoaq.scientific_transformer import TransformerBenchmarkSuite
from src.finnoaq.molecular_biophysics import CellularTissueTwin, MolecularToContinuumTransfer


def test_high_res_spatial_mesh_refinement():
    solver = HighResSpatialSolver()
    # Evaluate across representative grid subset [64, 128, 256, 512]
    res = solver.run_mesh_refinement_study(candidate_resolutions=[64, 128, 256, 512])
    assert "refinement_levels" in res
    assert len(res["refinement_levels"]) == 4
    finest = res["refinement_levels"][-1]
    assert finest["grid_dim"] == 512
    assert finest["mass_conservation_error_pct"] <= 0.01
    assert finest["core_temp_c"] >= 95.0


def test_pinn_coupled_transport_and_inverse_estimation():
    pinn = PINNSolver()
    res = pinn.train_and_benchmark(num_iterations=25, batch_size=256)
    assert res["pinn_status"] == "TRAINED_AND_BENCHMARKED"
    assert "pde_residual_l2" in res
    assert "parameter_estimation" in res
    assert res["parameter_estimation"]["true_diffusivity_Deff"] == 2.40e-11
    assert res["parameter_estimation"]["true_softening_rate_ksoft"] == 0.0035


def test_transformer_surrogate_and_ood_detection():
    suite = TransformerBenchmarkSuite()
    res = suite.run_benchmark(num_samples=200)
    assert res["benchmark_status"] == "COMPLETED"
    assert "scientific_transformer" in res
    assert "mlp_surrogate" in res
    assert res["scientific_transformer"]["ood_detection_capable"] is True
    assert res["scientific_transformer"]["unphysical_input_flagged"] is True


def test_molecular_to_continuum_biophysical_twin():
    transfer = MolecularToContinuumTransfer()
    k_untreated = transfer.compute_effective_softening_rate(temperature_c=100.0, sodium_displacement_fraction=0.0, calcium_bridge_density=0.75)
    k_treated = transfer.compute_effective_softening_rate(temperature_c=100.0, sodium_displacement_fraction=1.0, calcium_bridge_density=0.225)
    
    # Monovalent ion exchange must accelerate softening rate by > 5x
    assert k_treated > 5.0 * k_untreated
    
    twin = CellularTissueTwin()
    soft_res = twin.evaluate_tissue_softening(soak_treatment_conc=0.50, cooking_time_min=15.0)
    assert soft_res["softening_progress_pct"] > 50.0
    assert soft_res["molecular_calcium_bridge_density"] < 0.30


def test_immutable_project_objectives_stage_lock():
    obj_file = "configs/IMMUTABLE_PROJECT_OBJECTIVES.yaml"
    assert os.path.isfile(obj_file)
    with open(obj_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        
    assert config["two_stage_lock_governance"]["stage_1_discovery_and_proof"]["status"] == "ACTIVE"
    assert config["two_stage_lock_governance"]["stage_1_discovery_and_proof"]["preregistered_acceptance_criteria"]["current_stage_1_decision"] == "PROMISING_UNCONFIRMED"
    assert config["two_stage_lock_governance"]["stage_2_industrial_scaleup"]["status"] == "LOCKED"
    assert "strictly LOCKED until Stage 1 passes" in config["two_stage_lock_governance"]["stage_2_industrial_scaleup"]["lock_condition"]
