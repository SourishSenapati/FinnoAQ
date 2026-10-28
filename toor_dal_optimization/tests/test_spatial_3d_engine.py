"""
Unit tests for FinnoaQ 8,192-Node 2D/3D Axisymmetric Spatial Multi-Tensor Engine.
Governing Standard: FinnoaQ Omega Persistent Autonomous R&D Constitution.
"""

import pytest
import torch
from src.finnoaq.spatial_3d_engine import Spatial8192TensorGPUEngine


def test_spatial_8192_tensor_allocation():
    if not torch.cuda.is_available():
        pytest.skip("CUDA GPU required for 8,192-node spatial tensor test")

    engine = Spatial8192TensorGPUEngine(device="cuda:0", nr=64, nz=128)
    assert engine.nodes_per_grain == 8192

    # Run on a test batch of 1,000 grains = 8,192,000 voxels
    res = engine.execute_8192_spatial_batch(batch_size=1000, solution_conc_w_w=0.50)
    assert res["spatial_nodes_per_grain"] == 8192
    assert res["total_spatial_voxels_simulated"] == 8192000
    assert res["telemetry"]["vram_allocated_mb"] > 200.0  # Verifies high-VRAM tensor usage
    assert res["spatial_solubility"]["whole_grain_mean_theta_sol"] > 0.50
