from production_optimizer.optimization.monte_carlo import MonteCarloOptimizer
from production_optimizer.rnd_simulation import RndSimulationModule
from production_optimizer.core.gpu_engine import set_precision
import sys

# Industrial Stress Testing


def run_industrial_stress_test():
    print("=== INDUSTRIAL OPTIMIZER (ROBUST MODE) ===")
    try:
        optimizer = MonteCarloOptimizer()
        optimizer.run_simulation()
        optimizer.analyze_robustness()
    except Exception as e:
        print(f"Industrial Error: {e}")
        import traceback
        traceback.print_exc()

# R&D Double Precision Check


def run_rnd_check():
    print("\n\n=== R&D LAB OPTIMIZER (Doubles Precision) ===")
    try:
        from production_optimizer.core.gpu_engine import get_device
        device = get_device()

        # Enforce doubles
        set_precision(True)

        rnd_sim = RndSimulationModule(device)
        rnd_sim.run_analysis(100_000)
    except Exception as e:
        print(f"R&D Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_industrial_stress_test()
    run_rnd_check()
