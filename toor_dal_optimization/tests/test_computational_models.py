"""
Comprehensive automated test suite for FinnoaQ computational models.
Verifies Acceptance Gates A through G per Engineering Directive Section 15.
"""

import unittest
import os
import sys
import json
import numpy as np

sys.path.insert(0, '.')
from src.finnoaq.deterministic_balances import DeterministicMassBalance, wb_to_db, db_to_wb
from src.finnoaq.hydration_kinetics import HydrationModelEngine, peleg_equation, fickian_sphere_mr
from src.finnoaq.cooking_model import CookingPerformanceModel
from src.finnoaq.hypothesis_discrimination import HypothesisDiscriminationEngine
from src.finnoaq.gpu_accelerator import GPUBatchMonteCarloEngine

class TestFinnoaQComputationalEngineering(unittest.TestCase):

    # GATE A: SOURCE AND DESIGN-BASIS INTEGRITY
    def test_gate_a_design_basis_register(self):
        reg_path = "configs/design_basis_register.json"
        self.assertTrue(os.path.exists(reg_path), "Design basis register file must exist.")
        with open(reg_path, 'r', encoding='utf-8') as f:
            register = json.load(f)
        self.assertGreaterEqual(len(register), 10, "Register must contain at least 10 audited inputs.")

        allowed_states = [
            'MEASURED', 'SOURCE_REPORTED', 'OFFICIAL_SOURCE', 'LITERATURE_SUPPORTED',
            'CALCULATED', 'SIMULATED', 'ASSUMPTION', 'HYPOTHESIS', 'NOT_VERIFIED', 'BLOCKED'
        ]
        for item in register:
            self.assertIn('id', item)
            self.assertIn('value', item)
            self.assertIn('units', item)
            self.assertIn('evidence_state', item)
            self.assertIn(item['evidence_state'], allowed_states, f"Invalid evidence state in {item['id']}")

    # GATE B: BALANCE CORRECTNESS & MATHEMATICAL CLOSURE
    def test_gate_b_deterministic_balances(self):
        # Reference test: 15,000 kg/day, 10.5% WB, 184 kg loss
        mb = DeterministicMassBalance(15000.0, 0.105, 0.100, 184.0, 20.0)
        self.assertAlmostEqual(mb.feed_dry_solids, 13425.0, places=3)
        self.assertAlmostEqual(mb.feed_water, 1575.0, places=3)
        self.assertAlmostEqual(mb.product_dry_solids, 13241.0, places=3)

        # Scenario B1
        b1 = mb.solve_scenario_b1(0.2800)
        self.assertAlmostEqual(b1['dryer_inlet_mass_kg_day'], 18390.2778, places=2)
        self.assertAlmostEqual(b1['dryer_inlet_water_kg_day'], 5149.2778, places=2)
        self.assertAlmostEqual(b1['evaporation_kg_day'], 3678.0556, places=2)
        self.assertAlmostEqual(b1['closure_error_pct'], 0.0, places=6)
        self.assertTrue(b1['mathematical_closure'])

        # Scenario B2
        b2 = mb.solve_scenario_b2(18590.0)
        self.assertAlmostEqual(b2['dryer_inlet_mass_kg_day'], 18590.0, places=3)
        self.assertAlmostEqual(b2['dryer_inlet_water_kg_day'], 5349.0, places=3)
        self.assertAlmostEqual(b2['inlet_moisture_wb'], 0.287735, places=5)
        self.assertAlmostEqual(b2['evaporation_kg_day'], 3877.7778, places=2)
        self.assertAlmostEqual(b2['closure_error_pct'], 0.0, places=6)
        self.assertTrue(b2['mathematical_closure'])

        # Physical discrepancy delta
        delta_water = b2['evaporation_kg_day'] - b1['evaporation_kg_day']
        self.assertAlmostEqual(delta_water, 199.7222, places=2)

        # Competing loss scenario 196.01 kg remains distinct
        mb_l2 = DeterministicMassBalance(15000.0, 0.105, 0.100, 196.01, 20.0)
        self.assertAlmostEqual(mb_l2.product_dry_solids, 13228.99, places=2)
        self.assertNotEqual(mb_l2.product_dry_solids, mb.product_dry_solids)

        # Conversions
        self.assertAlmostEqual(wb_to_db(0.20), 0.25, places=4)
        self.assertAlmostEqual(db_to_wb(0.25), 0.20, places=4)

        # Limiting cases & validation
        with self.assertRaises(ValueError):
            DeterministicMassBalance(0.0, 0.10, 0.10, 100.0)
        with self.assertRaises(ValueError):
            wb_to_db(1.0)
        with self.assertRaises(ValueError):
            db_to_wb(-0.1)

    # GATE C: MODEL IMPLEMENTATION & PARAMETER IDENTIFIABILITY
    def test_gate_c_hydration_and_cooking_models(self):
        engine = HydrationModelEngine("dry_basis")
        times = [0.0, 5.0, 10.0, 15.0, 20.0, 30.0, 45.0, 60.0, 90.0, 120.0, 180.0]
        # Exact Peleg synthetic curve
        m_true = peleg_equation(np.array(times), 11.73, 2.50, 0.012)
        fit = engine.fit_peleg(times, m_true.tolist(), fix_m0=True)
        self.assertEqual(fit['status'], 'CONVERGED')
        self.assertAlmostEqual(fit['k1'], 2.50, places=2)
        self.assertAlmostEqual(fit['k2'], 0.012, places=4)
        self.assertTrue(fit['is_identifiable'])

        # Cooking model
        cook = CookingPerformanceModel()
        eval_res = cook.evaluate_models(0.105, water_absorption_rate_k1=2.50, cooking_temp_c=115.0)
        self.assertEqual(eval_res['model1_baseline_thermal']['maturity_state'], 'M2 — NUMERICALLY_VERIFIED')
        self.assertIn('NOT_VALIDATED', eval_res['target_dal_validation_status'])

    # GATE D: GPU VERIFICATION & NUMERICAL EQUIVALENCE
    def test_gate_d_gpu_acceleration(self):
        gpu_engine = GPUBatchMonteCarloEngine(device_str="cuda:0")
        scenarios = gpu_engine.generate_random_scenarios(5000)

        cpu_out = gpu_engine.run_cpu_vectorized(scenarios)
        self.assertIn('evaporation_kg_day', cpu_out)

        if gpu_engine.cuda_available:
            gpu_out = gpu_engine.run_gpu_tensorized(scenarios)
            self.assertIn('evaporation_kg_day', gpu_out)
            # Check numerical equivalence (< 1e-3 tolerance for single precision)
            max_err_evap = np.max(np.abs(cpu_out['evaporation_kg_day'] - gpu_out['evaporation_kg_day']))
            max_err_duty = np.max(np.abs(cpu_out['thermal_duty_kw'] - gpu_out['thermal_duty_kw']))
            self.assertLess(max_err_evap, 1e-3, f"CPU-GPU evaporation error too large: {max_err_evap}")
            self.assertLess(max_err_duty, 1e-3, f"CPU-GPU duty error too large: {max_err_duty}")
            self.assertGreater(gpu_out['peak_vram_mb'], 0.0)

    # GATE E: OFFLINE VERIFICATION
    def test_gate_e_offline_execution(self):
        # Verify that all required files and modules are local
        self.assertTrue(os.path.exists("configs/design_basis_register.json"))
        self.assertTrue(os.path.exists("src/finnoaq/deterministic_balances.py"))
        self.assertTrue(os.path.exists("src/finnoaq/hydration_kinetics.py"))
        self.assertTrue(os.path.exists("src/finnoaq/cooking_model.py"))
        self.assertTrue(os.path.exists("src/finnoaq/hypothesis_discrimination.py"))
        self.assertTrue(os.path.exists("src/finnoaq/gpu_accelerator.py"))

    # GATE F: SCIENTIFIC VALIDITY & SYNTHETIC DATA ISOLATION
    def test_gate_f_scientific_validity(self):
        synth_file = "data/synthetic/synthetic_hydration_test_dataset.csv"
        if os.path.exists(synth_file):
            with open(synth_file, 'r', encoding='utf-8') as f:
                header_lines = [f.readline() for _ in range(4)]
            # Header must have explicit synthetic banner
            header_text = "".join(header_lines)
            self.assertIn("SYNTHETIC — NOT EXPERIMENTAL DATA", header_text)

        # Hypothesis discrimination check
        oed = HypothesisDiscriminationEngine()
        cov = oed.get_hypothesis_coverage()
        self.assertEqual(cov['hypotheses_count'], 10)
        self.assertEqual(cov['total_fee_inr'], 173000.0)
        self.assertTrue(cov['is_fully_covered'])

    # GATE G: DELIVERY QUALITY
    def test_gate_g_delivery_quality(self):
        oed = HypothesisDiscriminationEngine()
        priorities = oed.evaluate_diagnostic_priorities()
        self.assertEqual(len(priorities), 11)
        self.assertGreater(priorities[0]['cost_efficiency_bits_per_kinr'], 0.0)

if __name__ == '__main__':
    unittest.main()
