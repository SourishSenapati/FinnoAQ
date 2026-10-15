import sys
import os
sys.path.insert(0, os.path.abspath("."))
import torch
import time
import numpy as np
from src.harakutir.high_res_spatial_solver import HighResSpatialSolver
from src.harakutir.spatial_3d_engine import Spatial8192TensorGPUEngine
from src.harakutir.pinn_solver import PINNSolver
from src.harakutir.scientific_transformer import TransformerBenchmarkSuite, ScientificTransformerSurrogate
from src.harakutir.molecular_biophysics import CellularTissueTwin, MolecularToContinuumTransfer

print("=== 1. REAL 8192x8192 PDE STENCIL BENCHMARK DISTRIBUTION ===")
solver = HighResSpatialSolver()
# Warmup
solver.benchmark_real_2d_pde_stencil(N=8192, steps=2)
# 5 repeated runs of 10 steps each
timings = []
for i in range(5):
    res = solver.benchmark_real_2d_pde_stencil(N=8192, steps=10)
    timings.append(res["ms_per_step"])
    print(f"Run {i+1}: {res['ms_per_step']:.2f} ms/step | Peak VRAM: {res['peak_vram_mb']:.2f} MB")
print(f"Distribution: Mean = {np.mean(timings):.2f} ms/step, Std = {np.std(timings):.2f} ms/step, Min = {np.min(timings):.2f}, Max = {np.max(timings):.2f}")

print("\n=== 2. SPATIAL 8,192 NODES/GRAIN BATCH BENCHMARK ===")
if torch.cuda.is_available():
    engine = Spatial8192TensorGPUEngine(device="cuda:0")
    res_batch = engine.execute_8192_spatial_batch(batch_size=1000)
    print(f"1,000 grains batch time: {res_batch['elapsed_sec']:.2f} s | VRAM: {res_batch['telemetry']['vram_allocated_mb']:.2f} MB")

print("\n=== 3. PINN SOLVER BENCHMARK ===")
pinn = PINNSolver()
res_pinn = pinn.train_and_benchmark(num_iterations=100, batch_size=256)
print(f"PINN time: {res_pinn['wall_clock_time_s']} s | PDE residual: {res_pinn['pde_residual_l2']} | Dm err: {res_pinn['parameter_estimation']['diffusivity_estimation_error_pct']}% | ksoft err: {res_pinn['parameter_estimation']['softening_rate_estimation_error_pct']}%")

print("\n=== 4. TRANSFORMER & OOD BENCHMARK ===")
suite = TransformerBenchmarkSuite()
res_trans = suite.run_benchmark(num_samples=500)
print(f"Transformer MAE: {res_trans['scientific_transformer']['mae_overall']} | Latency: {res_trans['scientific_transformer']['inference_latency_us']:.2f} us | OOD flagged: {res_trans['scientific_transformer']['unphysical_input_flagged']}")

print("\n=== 5. CELLULAR TISSUE TWIN PREDICTION FOR CAND-004 ===")
twin = CellularTissueTwin()
res_twin_raw = twin.evaluate_tissue_softening(soak_treatment_conc=0.0, cooking_time_min=22.0)
res_twin_treated = twin.evaluate_tissue_softening(soak_treatment_conc=0.5, cooking_time_min=13.8)
print(f"Raw Dal at 22 min: Cohesion = {res_twin_raw['intercellular_cohesion_stress_kpa']} kPa, Cooked = {res_twin_raw['is_cooked_endpoint_reached']}")
print(f"Treated Dal at 13.8 min: Cohesion = {res_twin_treated['intercellular_cohesion_stress_kpa']} kPa, Cooked = {res_twin_treated['is_cooked_endpoint_reached']}")

print("\n=== 6. OOD FALSE-POSITIVE / FALSE-NEGATIVE AUDIT ===")
model = ScientificTransformerSurrogate()
# Test in-distribution points (50 random valid samples)
X_in = torch.from_numpy(np.random.uniform(
    low=[0.0, 0.0, 1.0, 20.0, 15.0, 0.1, 50.0, 1.0],
    high=[2.0, 1.5, 2.0, 40.0, 60.0, 0.5, 80.0, 1.6],
    size=(50, 8)
).astype(np.float32))
_, ood_in = model(X_in)
# Current heuristic: flagged if ood > 0.65 or ood < 0.35
fp_count = sum(bool(v > 0.65 or v < 0.35) for v in ood_in.detach().numpy())
print(f"In-distribution samples: {len(X_in)} | False Positives Flagged as OOD: {fp_count} ({fp_count/len(X_in)*100:.1f}%)")

# Test out-of-distribution points (50 extreme samples)
X_out = torch.from_numpy(np.random.uniform(
    low=[10.0, 15.0, 10.0, 150.0, 300.0, 0.9, 150.0, 5.0],
    high=[20.0, 30.0, 20.0, 250.0, 600.0, 1.0, 250.0, 10.0],
    size=(50, 8)
).astype(np.float32))
_, ood_out = model(X_out)
fn_count = sum(not bool(v > 0.65 or v < 0.35) for v in ood_out.detach().numpy())
print(f"Out-of-distribution samples: {len(X_out)} | False Negatives (Missed OOD): {fn_count} ({fn_count/len(X_out)*100:.1f}%)")
