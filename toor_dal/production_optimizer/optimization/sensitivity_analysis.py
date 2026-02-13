"""
Sensitivity Analysis Engine
Perfoms Global Sensitivity Analysis (Sobol approximation) and Stress Testing.
"""
import torch
from .monte_carlo import MonteCarloOptimizer
from ..core.gpu_engine import get_device, set_precision


class SensitivityEngine:
    """
    Engine for conducting sensitivity analysis and stress testing on the optimization model.
    """

    def __init__(self):
        set_precision(True)
        self.optimizer = MonteCarloOptimizer()
        self.device = self.optimizer.device
        # Ensure results are populated
        if not self.optimizer.results:
            self.optimizer.run_simulation()

    def run_global_sensitivity(self):
        """
        Runs correlation analysis to determine parameter dominance.
        """
        print("\n=== GLOBAL SENSITIVITY ANALYSIS (SOBOL APPROX) ===")
        # Run standard simulation with all random variations enabled
        # Note: If optimizer already ran in init, we use those results for baseline
        results = self.optimizer.results

        # Target: Unit Cost (we want to know what drives Cost)
        target = "unit_cost"
        y = results[target]

        # Features to check
        features = {
            "Raw Material Price": results["p_material_cost"],
            "Electricity Tariff": results["p_electricity_rate"],
            "Unit Failure Rate": results["p_unit_failure"],
            "Ambient Temp": results["p_ambient_temp"],
            "Heat Pump COP": results["p_cop"],
            # Dependent but useful
            "System Downtime": results["p_sys_failure_prob"]
        }

        # Correlation Analysis
        print(f"Parameter Dominance Ranking (Correlation with {target}):")
        correlations = []
        for name, x in features.items():
            # Pearson correlation
            # Stack and corrcoef
            stack = torch.stack([x, y])
            corr = torch.corrcoef(stack)[0, 1].item()
            correlations.append((name, abs(corr), corr))

        # Sort by abs correlation
        correlations.sort(key=lambda x: x[1], reverse=True)

        for name, _, raw in correlations:
            impact = "POSITIVE" if raw > 0 else "NEGATIVE"
            print(f"  {name}: {raw:.4f} ({impact})")

        print("\nInterpretation:")
        print("  > 0.5: Dominant Driver")
        print("  0.2 - 0.5: Moderate Driver")
        print("  < 0.2: Minor Driver")

    def run_stress_tests(self):
        """
        Runs hard stress tests (Case A, B, C, D) to verify model robustness.
        """
        print("\n=== HARD STRESS TESTS ===")

        # 1. Stress Case A: Unit Failure = 3%
        print("\n[Stress Case A] High Failure Rate (3% per Mixie)")
        # Override unit_failure_rate to be Mean 0.03
        fail_tensor = torch.normal(0.03, 0.005, (1000000,), device=self.device)
        fail_tensor = torch.clamp(fail_tensor, 0.0, 1.0)

        res_a = self.optimizer.run_simulation(
            custom_params={'unit_failure_rate': fail_tensor})
        self._print_winner(res_a, "Case A")

        # 2. Stress Case B: Electricity Doubles (24 INR/kWh)
        print("\n[Stress Case B] Electricity Price Shock (24 INR/kWh)")
        elec_tensor = torch.normal(24.0, 2.0, (1000000,), device=self.device)
        res_b = self.optimizer.run_simulation(
            custom_params={'electricity_rate': elec_tensor})
        self._print_winner(res_b, "Case B")

        # 3. Stress Case C: Ambient 40C
        print("\n[Stress Case C] Heat Wave (Ambient 40C)")
        # 40C = 313K
        amb_tensor = torch.normal(
            313.0, 2.0, (1000000,), device=self.device)
        res_c = self.optimizer.run_simulation(
            custom_params={'ambient_temp_k': amb_tensor})
        self._print_winner(res_c, "Case C")

        # 4. Stress Case D: Material Price Spike (INR 65)
        print("\n[Stress Case D] Material Inflation (INR 65/kg)")
        mat_tensor = torch.normal(65.0, 5.0, (1000000,), device=self.device)
        res_d = self.optimizer.run_simulation(
            custom_params={'material_cost': mat_tensor})
        self._print_winner(res_d, "Case D")

    def _print_winner(self, res, case_name):
        # Group by Grinder Type
        g_types = res["grinder_type"]
        unit_costs = res["unit_cost"]
        downtime = res["downtime"]

        print(f"  Results for {case_name}:")
        names = ["Ball Mill", "Hammer Mill", "Mixie Cluster"]

        for i in [0, 2]:  # Compare Ball vs Mixie
            mask = g_types == i
            # Handle empty mask edge case
            if mask.sum() == 0:
                print(f"    {names[i]}: No samples.")
                continue

            cost = unit_costs[mask].mean().item()
            down = downtime[mask].mean().item()
            print(
                f"    {names[i]}: Cost = INR {cost:.2f}/kg | Downtime = {down:.2%}")

        # Determine Winner
        mask_bm = g_types == 0
        mask_mx = g_types == 2
        cost_bm = unit_costs[mask_bm].mean().item()
        cost_mx = unit_costs[mask_mx].mean().item()

        winner = "Ball Mill" if cost_bm < cost_mx else "Mixie Cluster"
        diff = abs(cost_bm - cost_mx)
        print(f"  >> WINNER: {winner} (Margin: INR {diff:.2f}/kg)")

    def calculate_confidence_intervals(self):
        """
        Calculates and prints 95% Confidence Intervals for Unit Cost.
        """
        print("\n=== CONFIDENCE INTERVALS (Baseline) ===")
        res = self.optimizer.results  # From last run
        if not res:
            res = self.optimizer.run_simulation()

        cost = res["unit_cost"]
        mean = cost.mean().item()
        std = cost.std().item()
        ci_low = mean - 1.96 * std
        ci_high = mean + 1.96 * std

        p95 = torch.quantile(cost, 0.95).item()

        print(f"  Unit Cost Mean: INR {mean:.2f}")
        print(f"  Std Dev:        INR {std:.2f}")
        print(f"  95% CI:         [{ci_low:.2f}, {ci_high:.2f}]")
        print(f"  95% Worst Case: INR {p95:.2f}")


if __name__ == "__main__":
    engine = SensitivityEngine()
    engine.run_global_sensitivity()
    engine.calculate_confidence_intervals()
    engine.run_stress_tests()
