"""
Benchmark script for GPU-accelerated Monte Carlo uncertainty propagation.
Evaluates CPU vs RTX 4050 CUDA performance across N = 100 to 250,000 scenarios.
"""
import sys
import json
import numpy as np
sys.path.insert(0, '.')
from src.finnoaq.gpu_accelerator import GPUBatchMonteCarloEngine

def run_benchmark():
    print("=================================================================")
    print("FINNOAQ GPU VS CPU MONTE CARLO BENCHMARK (NVIDIA RTX 4050 CUDA)")
    print("=================================================================")

    engine = GPUBatchMonteCarloEngine(device_str="cuda:0")
    print(f"Engine PyTorch Available: {engine.torch_available}")
    print(f"Engine CUDA Available: {engine.cuda_available}")
    print(f"Selected Device: {engine.device}")

    # Benchmark workload sizes
    sizes = [100, 1000, 10000, 50000, 100000, 250000]
    print(f"\nRunning benchmark across workload sizes: {sizes}")
    
    results = engine.benchmark_workload_scaling(sizes)
    
    print("\nBENCHMARK RESULTS TABLE:")
    print(f"{'Scenarios (N)':<15} | {'CPU Time (s)':<13} | {'GPU Time (s)':<13} | {'Speedup':<9} | {'Max Abs Err':<12} | {'VRAM (MB)':<10}")
    print("-" * 85)
    for r in results:
        scenarios = r['scenarios_count']
        t_cpu = f"{r['cpu_time_sec']:.5f}"
        t_gpu = f"{r['gpu_time_sec']:.5f}" if r['gpu_time_sec'] is not None else "N/A"
        speedup = f"{r['speedup_ratio']:.2f}x" if r['speedup_ratio'] is not None else "N/A"
        err = f"{r['max_abs_error_evap_kg']:.2e}" if 'max_abs_error_evap_kg' in r else "N/A"
        vram = f"{r['peak_vram_mb']:.2f}" if 'peak_vram_mb' in r else "N/A"
        print(f"{scenarios:<15} | {t_cpu:<13} | {t_gpu:<13} | {speedup:<9} | {err:<12} | {vram:<10}")

    # Inspect 100,000 scenarios summary statistics
    scenarios_100k = engine.generate_random_scenarios(100000)
    res_100k = engine.run_gpu_tensorized(scenarios_100k)
    
    evap = res_100k['evaporation_kg_day']
    duty = res_100k['thermal_duty_kw']
    t90 = res_100k['t90_cooking_min']
    
    print("\n100,000-SCENARIO MONTE CARLO UNCERTAINTY DISTRIBUTION:")
    print(f"  Dryer Evaporation (kg/day): Mean = {evap.mean():.2f}, 5th %ile = {float(np.percentile(evap, 5)):.2f}, 95th %ile = {float(np.percentile(evap, 95)):.2f}")
    print(f"  Thermal Drying Duty (kW_th): Mean = {duty.mean():.2f}, 5th %ile = {float(np.percentile(duty, 5)):.2f}, 95th %ile = {float(np.percentile(duty, 95)):.2f}")
    print(f"  Predicted Cooking T90 (min): Mean = {t90.mean():.2f}, 5th %ile = {float(np.percentile(t90, 5)):.2f}, 95th %ile = {float(np.percentile(t90, 95)):.2f}")

    # Save benchmark payload
    payload = {
        'benchmark_summary': results,
        'uncertainty_distribution_100k': {
            'evaporation_kg_day': {'mean': float(evap.mean()), 'p5': float(np.percentile(evap, 5)), 'p95': float(np.percentile(evap, 95))},
            'thermal_duty_kw': {'mean': float(duty.mean()), 'p5': float(np.percentile(duty, 5)), 'p95': float(np.percentile(duty, 95))},
            't90_cooking_min': {'mean': float(t90.mean()), 'p5': float(np.percentile(t90, 5)), 'p95': float(np.percentile(t90, 95))}
        }
    }
    with open('artifacts/gpu_monte_carlo_benchmark_results.json', 'w') as f:
        json.dump(payload, f, indent=2)
    print("\nSaved benchmark results to: artifacts/gpu_monte_carlo_benchmark_results.json")

if __name__ == '__main__':
    run_benchmark()
