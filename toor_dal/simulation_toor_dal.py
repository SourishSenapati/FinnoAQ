"""
Advanced Digital Twin for Toor Dal Manufacturability.
Simulates detailed physico-chemical parameters to ensure Six Sigma reliability.
Includes GPU-Accelerated SME Optimization.
"""
import time
import math
import torch


class ToorDalSixSigmaSimulator:
    """
    Simulates hydration, texture, moisture control, and full proximate composition.
    Includes Optimization Engine.
    """

    def __init__(self, num_batches=1_000_000):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        self.num_batches = num_batches
        print(f"Toor Dal Physics Engine Initialized on {self.device}")

        # Process Constants
        self.drying_coeff = 0.15
        self.target_moisture = 10.0
        self.usl_moisture = 11.0
        self.lsl_moisture = 9.0

        # Optimized Parameter
        self.extrusion_temp_setpoint = 85.0

    def optimize_extrusion_process(self):
        """
        Uses GPU to sweep Extrusion Temperature/SME to optimize Cooking Time.
        Cooking Time < 15 mins is target. High Temp = High Gelatinization = Fast Cook.
        But High Temp > 90C degrades Protein.
        """
        print("   [GPU OPTIMIZATION] Tuning Extrusion Thermodynamics...")

        # Sweep Temp 80C to 95C
        temps = torch.linspace(80.0, 95.0, 100, device=self.device)

        # Gelatinization % = (Temp - 60) * 1.5
        gelatinization = (temps - 60.0) * 1.5

        # Cooking Time ~ 1 / Gelatinization
        # Base cook time at 85C (37.5% Gel) is ~15 mins?
        # Let's say CookTime = 560 / Gelatinization
        cook_time = 560.0 / gelatinization

        # Protein Damage Risk (Exponential above 85C)
        protein_damage = torch.exp((temps - 85.0) / 2.0) - 1.0
        protein_damage = torch.clamp(protein_damage, min=0.0)

        # Objective: Minimize Cook Time + Penalty for Protein Damage
        loss = cook_time + (protein_damage * 5.0)

        min_idx = torch.argmin(loss)
        best_temp = temps[min_idx].item()

        print(
            f"      - [FAULT] Standard Temp 85C (Cook Time ~ {560/((85-60)*1.5):.1f}m).")
        print(
            f"      - [SWEEP] Balancing Cook Speed vs Protein Denaturation...")
        print(f"      - [OPTIMAL] Detected Optimal Extrusion Temp: {best_temp:.1f}C "
              f"(Predicted Cook Time: {cook_time[min_idx]:.1f}m)")

        self.extrusion_temp_setpoint = best_temp

    def _generate_normal(self, mean, std):
        return torch.normal(mean=mean, std=std, size=(self.num_batches,), device=self.device)

    def simulate_organoleptic_properties(self):
        """Simulates Taste, Aroma, and Dispersibility."""
        print("   [SENS] Simulating Organoleptic & Integrity Metrics...")

        # Use Optimized Temp
        extrusion_temp = torch.normal(
            self.extrusion_temp_setpoint, 2.0, (self.num_batches,), device=self.device)
        residence_time_sec = torch.normal(
            45.0, 5.0, (self.num_batches,), device=self.device)

        lox_survival = torch.exp(-(extrusion_temp - 70.0)
                                 * residence_time_sec / 100.0)
        beany_flavor_score = lox_survival * 10.0

        gelatinization = (extrusion_temp - 60.0) * 1.5
        gelatinization = torch.clamp(gelatinization, min=10.0, max=90.0)

        calcium_bonding = self._generate_normal(0.6, 0.05) * 15.0
        cooking_loss = 20.0 - calcium_bonding
        cooking_loss = torch.clamp(cooking_loss, min=2.0)

        print(f"      - Mean Beany Flavor: {torch.mean(beany_flavor_score):.2f}/10 "
              f"(Target < 2.0: {torch.mean((beany_flavor_score < 2.0).float())*100:.1f}%)")
        print(f"      - Gelatinization (Creaminess): {torch.mean(gelatinization):.1f}% "
              f"(Target 40-50%)")
        print(f"      - Cooking Integrity (Solids Loss): {torch.mean(cooking_loss):.2f}% "
              f"(Target < 10%: {torch.mean((cooking_loss < 10.0).float())*100:.1f}%)")

    def simulate_composition_physics(self):
        """
        Simulates the full Proximate Composition and Physical Properties.
        Ensure nutritional compliance and physical mimicry of natural dal.
        """
        print("   [COMP] Simulating Proximate Analysis & Physical Properties...")

        # 1. PROTEIN CONTENT (Target: 22-24%)
        # Variation due to raw material (Pea Protein/Soy Isolate blending)
        protein_content = self._generate_normal(23.5, 0.5)

        # 2. STARCH PROFILE (Amylose/Amylopectin)
        # Affects Gelatinization. Target Amylose ~30% for firm texture.
        amylose_content = self._generate_normal(30.0, 1.2)

        # 3. DENSITY (Bulk Density)
        # Natural Toor Dal ~ 0.85 g/cc. Analogue must match to avoid "floating" or "sinking" weirdness.
        # Density depends on extrusion expansion (Poiseuille Flow in die).
        expansion_index = self._generate_normal(1.15, 0.05)
        bulk_density = 1.0 / expansion_index  # Approx.

        # 4. COOKING TIME PREDICTION (Thermodynamics)
        # Cook time should drop if we increased temp.
        # But here 'porosity' is expansion.
        porosity = (1.0 - bulk_density) * 100.0
        diffusivity = (0.5e-9) * (1.0 + porosity/50.0)
        thickness_mm = 1.5
        cooking_time_mins = (thickness_mm**2) / (diffusivity * 1e8)

        # Validation
        valid_protein = (torch.sum((protein_content > 22.0) &
                                   (protein_content < 25.0)).item() / self.num_batches) * 100
        valid_density = (torch.sum((bulk_density > 0.80) &
                                   (bulk_density < 0.90)).item() / self.num_batches) * 100
        quick_cook = (torch.sum(cooking_time_mins <
                                15.0).item() / self.num_batches) * 100

        print(f"      - Mean Protein: {torch.mean(protein_content):.2f}% "
              f"(Pass: {valid_protein:.2f}%)")
        print(f"      - Mean Amylose: {torch.mean(amylose_content):.2f}% "
              f"(Texture Driver)")
        print(f"      - Mean Density: {torch.mean(bulk_density):.3f} g/cc "
              f"(Natural mimicry: {valid_density:.2f}%)")
        print(f"      - Avg Cooking Time: {torch.mean(cooking_time_mins):.1f} mins "
              f"(Quick Cook: {quick_cook:.2f}%)")

    def test_hydration_kinetics(self):
        """Test 1: Hydration Uniformity."""
        diffusion_rate = self._generate_normal(1.2e-9, 0.1e-9)
        particle_radius = 1500.0
        hydration_time_sec = (particle_radius**2) / (4 * diffusion_rate * 1e12)
        success_rate = (torch.sum(hydration_time_sec <
                                  1200.0).item() / self.num_batches) * 100
        print(f"   [CHEM] Hydration Kinetics Pass Rate: {success_rate:.4f}% "
              f"(Target 99.99%)")
        return success_rate

    def test_textural_integrity(self):
        """Test 2: Rheological Stress Test."""
        calcium_concentration = self._generate_normal(0.6, 0.05)
        binding_efficiency = torch.clamp(
            calcium_concentration * 150.0, max=100.0)
        shear_stress_mpa = binding_efficiency * 0.05
        in_spec = (shear_stress_mpa > 3.0) & (shear_stress_mpa < 5.0)
        sigma_score = self._calculate_sigma(in_spec)
        print(f"   [PHYS] Texture/Shear Stress Sigma: {sigma_score:.2f} Sigma")

    def test_moisture_control_loop(self):
        """Test 3: Thermodynamics of Drying."""
        input_moisture = self._generate_normal(14.0, 0.8)
        sensor_noise = self._generate_normal(0.0, 0.015)
        heater_variance = self._generate_normal(0.0, 0.1)
        measured = input_moisture + sensor_noise
        clean_delta = measured - self.target_moisture
        moisture_removed = clean_delta + heater_variance
        final_moisture = input_moisture - moisture_removed

        sigma = torch.std(final_moisture).item()
        mean = torch.mean(final_moisture).item()
        cpu = (self.usl_moisture - mean) / (3 * sigma)
        cpl = (mean - self.lsl_moisture) / (3 * sigma)
        cpk = min(cpu, cpl)
        print(f"   [ENG]  Drying Process Cpk: {cpk:.3f} "
              f"(Target > 1.67 for 5-Sigma)")
        return cpk

    def _calculate_sigma(self, boolean_tensor):
        """Calculates Six Sigma Level."""
        success_count = torch.sum(boolean_tensor).item()
        yield_rate = success_count / self.num_batches
        if yield_rate >= 0.999999999:
            return 6.0
        defects_per_million = (1.0 - yield_rate) * 1_000_000
        try:
            return 0.8406 + math.sqrt(29.37 - 2.221 *
                                      math.log(defects_per_million + 1e-9))
        except ValueError:
            return 0.0

    def run_full_validation(self):
        """Executes full validation protocol."""
        print("\n--- INITIATING TOOR DAL SIX SIGMA VALIDATION PROTOCOL ---")
        t0 = time.time()
        self.optimize_extrusion_process()
        self.simulate_organoleptic_properties()
        self.simulate_composition_physics()
        self.test_hydration_kinetics()
        self.test_textural_integrity()
        self.test_moisture_control_loop()
        print(f"   [PERF] Simulation Time: {time.time()-t0:.4f}s")
        print("---------------------------------------------------------")


if __name__ == "__main__":
    sim = ToorDalSixSigmaSimulator(num_batches=1_000_000)
    sim.run_full_validation()
