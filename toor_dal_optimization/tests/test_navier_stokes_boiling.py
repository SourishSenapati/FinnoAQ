"""
Unit tests for FinnoaQ Navier-Stokes & Chemical Engineering Boiling Kinetics Engine.
Governing Standard: FinnoaQ Omega Persistent Autonomous R&D Constitution.
"""

import pytest
from src.finnoaq.navier_stokes_boiling import NavierStokesBoilingEngine


def test_navier_stokes_convective_heat_transfer_coefficient():
    engine = NavierStokesBoilingEngine()
    
    # 1. Natural convection regime (pre-boiling subcooled fluid at 60°C)
    h_nat, Bi_nat, regime_nat = engine.compute_navier_stokes_convective_coefficient(
        T_surface_c=25.0,
        T_fluid_bulk_c=60.0
    )
    assert 200.0 <= h_nat <= 3500.0
    assert regime_nat == "NATURAL_CONVECTION_BOUSSINESQ"

    # 2. Nucleate pool boiling regime at 121°C saturation
    h_boil, Bi_boil, regime_boil = engine.compute_navier_stokes_convective_coefficient(
        T_surface_c=100.0,
        T_fluid_bulk_c=121.1
    )
    assert 2000.0 <= h_boil <= 5500.0
    assert regime_boil == "NUCLEATE_POOL_BOILING"
    assert Bi_boil > 5.0  # Conduction-limited pulse matrix


def test_coupled_navier_stokes_cooking_simulation():
    engine = NavierStokesBoilingEngine()

    # Pre-soaked treated dal (0.50% NaHCO3)
    res_treated = engine.simulate_coupled_boiling_cooking(theta_sol=0.85, pre_soaked_moisture_wb=0.52)
    assert res_treated["cooking_outcome"]["cooking_time_minutes"] <= 15.0
    assert res_treated["cooking_outcome"]["pressure_cooker_whistles"] <= 4.0
    assert res_treated["cooking_outcome"]["tenderness_reached"] is True

    # Raw untreated dal
    res_raw = engine.simulate_coupled_boiling_cooking(theta_sol=0.10, pre_soaked_moisture_wb=0.105)
    assert res_raw["cooking_outcome"]["cooking_time_minutes"] > 45.0
    assert res_raw["cooking_outcome"]["pressure_cooker_whistles"] > 12.0
