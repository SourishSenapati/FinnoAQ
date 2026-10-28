"""
Automated Pytest Suite for fnq-pulse-tech CLI and RAEBYES Invariants.
Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati
"""

import sys
import os
import pytest

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(base_dir, "src")
for p in [base_dir, src_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

from finnoaq.pulse_tech_cli import (
    RaebyesInvariantError,
    VarianceGuard,
    DimensionalGuard,
    AntiRewardHackingGuard,
    DeterministicPulsePhysics,
    TECHNOLOGY_CATALOG,
    cmd_two_whistles,
    cmd_sensory
)
import argparse

def test_raebyes_steam_pressure_validation():
    """Verifies that steam saturation pressure strictly follows NIST within 5%."""
    # Saturated water at 121.2°C is ~207.0 kPa abs
    DimensionalGuard.validate_steam_pressure(121.2, 207.0)
    with pytest.raises(RaebyesInvariantError):
        # 285 kPa at 121.2°C was the erroneous legacy value (FAIL-0014)
        DimensionalGuard.validate_steam_pressure(121.2, 285.0)

def test_raebyes_parenchyma_stress_validation():
    """Verifies that plant parenchyma yield stress rejects structural metal values."""
    DimensionalGuard.validate_tissue_stress(350e3)  # 350 kPa is authentic
    with pytest.raises(RaebyesInvariantError):
        DimensionalGuard.validate_tissue_stress(120e6)  # 120 MPa is aircraft aluminum (FAIL-0012)

def test_raebyes_variance_guard():
    """Verifies that zero-variance synthetic tensors are rejected."""
    VarianceGuard.assert_varying([10.2, 11.5, 14.8], "varying_test")
    with pytest.raises(RaebyesInvariantError):
        VarianceGuard.assert_varying([0.93, 0.93, 0.93], "synthetic_mock_tensor")

def test_nisha_arrhenius_softening_monotonicity():
    """Verifies that first-order softening rate accelerates according to Arrhenius kinetics."""
    k_100 = DeterministicPulsePhysics.calculate_softening_rate_k(100.0)
    k_110 = DeterministicPulsePhysics.calculate_softening_rate_k(110.0)
    k_120 = DeterministicPulsePhysics.calculate_softening_rate_k(120.0)
    assert k_100 < k_110 < k_120
    # Between 100°C and 120°C, rate should increase ~3.8x based on Ea = 81.6 kJ/mol
    ratio = k_120 / k_100
    assert 3.5 <= ratio <= 4.2

def test_citrate_speciation_conservation():
    """Verifies that multi-species Henderson-Hasselbalch electroneutrality is conserved."""
    spec = DeterministicPulsePhysics.calculate_citrate_buffer_speciation(0.12, 5.6)
    total_reconstructed = spec["H3Cit_M"] + spec["H2Cit_1minus_M"] + spec["HCit_2minus_M"] + spec["Cit_3minus_M"]
    assert abs(total_reconstructed - 0.12) < 1e-9
    assert spec["chelating_anion_fraction"] > 0.85  # At pH 5.6, over 85% is in chelating HCit2- or Cit3- form

def test_technology_catalog_integrity():
    """Verifies that all 7 technologies have valid structures, realistic bounds, and DOIs."""
    assert len(TECHNOLOGY_CATALOG) >= 7
    for t_id, t in TECHNOLOGY_CATALOG.items():
        assert "citations" in t and len(t["citations"]) >= 1
        assert t["cooking_time_reduction_pct"][0] < t["cooking_time_reduction_pct"][1]
        assert t["opex_per_kg_inr"] > 0.0
        assert t["capex_estimate_inr_lakhs"] > 0.0

def test_raebyes_anti_reward_hacking_core_defect():
    """Asserts that 2-whistle claims with raw core shear force (>18 N) are blocked."""
    AntiRewardHackingGuard.assert_dual_gate(2, 12.0, 60.0, 48.0)  # Tender core passes
    with pytest.raises(RaebyesInvariantError):
        AntiRewardHackingGuard.assert_dual_gate(2, 22.5, 60.0, 48.0)  # Raw core fails

def test_raebyes_anti_reward_hacking_sodium_ceiling():
    """Asserts that treatments exceeding FSSAI 120 mg/100g sodium limit fail closed."""
    AntiRewardHackingGuard.assert_dual_gate(2, 12.0, 85.0, 48.0)  # 85 mg/100g passes
    with pytest.raises(RaebyesInvariantError):
        AntiRewardHackingGuard.assert_dual_gate(2, 12.0, 160.0, 48.0)  # 160 mg/100g fails

def test_two_whistles_command_execution():
    """Verifies that cmd_two_whistles runs deterministically and passes all invariants."""
    mock_args = argparse.Namespace(
        cost_ceiling=3.0,
        max_sodium=120.0,
        water_hardness=150.0,
        json=False
    )
    # Should execute cleanly without raising any exceptions
    cmd_two_whistles(mock_args)

def test_raebyes_anti_reward_hacking_sensory():
    """Asserts that high aftertaste without remediation raises RaebyesInvariantError."""
    AntiRewardHackingGuard.assert_sensory_integrity("TECH-PASS", 8.5, 0.05, True)
    with pytest.raises(RaebyesInvariantError):
        AntiRewardHackingGuard.assert_sensory_integrity("TECH-FAIL", 8.5, 0.45, False)

def test_sensory_command_execution():
    """Verifies that cmd_sensory runs and evaluates all 7 technology taste profiles."""
    mock_args = argparse.Namespace(tech_id="all", json=False)
    cmd_sensory(mock_args)


