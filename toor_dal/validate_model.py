import sys
from production_optimizer.optimization.sensitivity_analysis import SensitivityEngine


def main():
    print("=== FINAL VALIDATION & STRESS TEST PROTOCOL ===\n")
    engine = SensitivityEngine()

    # 1. Global Sensitivity
    engine.run_global_sensitivity()

    # 2. Confidence Intervals
    engine.calculate_confidence_intervals()

    # 3. Hard Stress Tests
    engine.run_stress_tests()


if __name__ == "__main__":
    main()
