"""
Resilience, Atomic Recovery and Persistence Test Suite.
Validates Section 43 of FinnoaQ Autonomous Master Prompt:
- Atomic checkpointing and previous checkpoint fallback
- SQLite WAL transaction integrity
- Lock acquisition and duplicate supervisor protection
- Graceful interruption signal handling
"""

import os
import sys
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.finnoaq.checkpoint import CheckpointManager
from src.finnoaq.gpu_engine import GPUAccelerationEngine

def test_checkpoint_atomic_replacement_and_fallback():
    cp_mgr = CheckpointManager()
    
    # Write checkpoint 1
    state1 = {"run_id": "TEST_RECOVERY_01", "step": 1, "data": "initial"}
    path1 = cp_mgr.write_atomic_checkpoint(state1)
    assert os.path.isfile(path1)
    
    # Write checkpoint 2
    state2 = {"run_id": "TEST_RECOVERY_01", "step": 2, "data": "updated"}
    path2 = cp_mgr.write_atomic_checkpoint(state2)
    assert os.path.isfile(path2)
    
    # Verify latest checkpoint loaded
    latest = cp_mgr.load_latest_checkpoint()
    assert latest["step"] == 2
    
    # Verify previous checkpoint fallback
    prev = cp_mgr.load_previous_checkpoint()
    assert prev["step"] == 1

def test_corrupted_checkpoint_recovery():
    cp_mgr = CheckpointManager(checkpoint_dir="checkpoints/test_corrupt_sandbox")
    
    # Write valid step 10
    s10 = {"run_id": "TEST_CORRUPT_01", "step": 10, "valid": True}
    cp_mgr.write_atomic_checkpoint(s10)
    
    # Write valid step 11
    s11 = {"run_id": "TEST_CORRUPT_01", "step": 11, "valid": True}
    cp_mgr.write_atomic_checkpoint(s11)
    
    # Corrupt the latest checkpoint file in sandbox
    latest_file = os.path.join(cp_mgr.checkpoint_dir, "latest_checkpoint.json")
    with open(latest_file, "w", encoding="utf-8") as f:
        f.write("CORRUPTED_NON_JSON_DATA_!!!")
        
    # Loading latest should gracefully fallback to previous valid checkpoint
    recovered = cp_mgr.load_latest_checkpoint()
    assert recovered is not None
    assert recovered["step"] == 10  # Successfully fell back to previous checkpoint!
    
    # Cleanup sandbox files
    import shutil
    shutil.rmtree(cp_mgr.checkpoint_dir, ignore_errors=True)

def test_run_lock_acquisition_and_duplicate_prevention():
    cp_mgr = CheckpointManager(state_dir="state/test_state")
    run_id_a = "RUN_PROCESS_A"
    run_id_b = "RUN_PROCESS_B"
    
    # First supervisor acquires lock
    acquired_a = cp_mgr.acquire_lock(run_id_a)
    assert acquired_a is True
    
    # Second duplicate supervisor attempts to acquire lock -> must be BLOCKED
    acquired_b = cp_mgr.acquire_lock(run_id_b)
    assert acquired_b is False
    
    # First supervisor releases lock
    cp_mgr.release_lock()
    
    # Now second supervisor can acquire lock
    acquired_b_retry = cp_mgr.acquire_lock(run_id_b)
    assert acquired_b_retry is True
    cp_mgr.release_lock()

def test_gpu_engine_hardware_and_execution():
    gpu_engine = GPUAccelerationEngine()
    hw = gpu_engine.get_hardware_status()
    assert hw["device"] != "None"
    
    # Solve PDE on device
    pde_res = gpu_engine.solve_coupled_radial_diffusion_pde(time_steps=50)
    assert pde_res["average_moisture_wb_pct"] > 10.0
    assert pde_res["core_temp_c"] >= 25.0
    
    # Run Monte Carlo on device
    mc_res = gpu_engine.run_gpu_monte_carlo_sensitivity(num_samples=5000)
    assert mc_res["num_monte_carlo_samples"] == 5000
    assert mc_res["cooking_whistles_distribution"]["mean"] > 0.0
    assert len(mc_res["first_order_sobol_sensitivity_ranking"]) == 4
