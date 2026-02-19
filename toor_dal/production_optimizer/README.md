# Tur Dal Production Optimizer

This module provides a robust, GPU-accelerated Monte Carlo simulation engine for optimizing Tur Dal production lines.

## Architecture

- **core/**: Contains the fundamental logic.
  - `config.py`: Centralized configuration constants (Physics, Costs, Machinery).
  - `gpu_engine.py`: Handles CUDA variables and tensor generation.
  - `physics_models.py`: Arrhenius kinetics, Thermodynamics.
  - `cost_model.py`: Financial calculations (OpEx, CapEx, Amortization).
  - `objective.py`: The unified objective function (Output/Cost \* Reliability).
- **modules/**: Component simulations.
  - `grinding.py`: Detailed grinding physics (Ball Mill vs Hammer Mill vs Mixie Cluster).
  - `drying.py`: Drying energetics (Electric vs Heat Pump).
- **optimization/**:
  - `monte_carlo.py`: The main simulation loop using vectorized operations.
- **logging/**: Stores simulation results.

## Usage

Run the main optimizer from the project root:

```bash
python main_optimizer.py
```

## Key Features

- **Vectorized Simulation**: Runs 1,000,000+ iterations in seconds on GPU.
- **Modular Physics**: Temperature rise and protein denaturation modeled explicitly.
- **Risk-Weighted**: Includes catastrophic failure probabilities in the objective.
- **Cost-Benefit Analysis**: Amortizes R&D and Capital expenses correctly.

## Phase 1 Screening (Formulation Optimization)

To run the formulation screening simulation:

```bash
python -m production_optimizer.phase1_screening
```

This module targets the optimal recipe balance (Cost < ₹57/kg, Protein > 15%, Binding Score > 3.0).

## Phase 2 Bench Validation (Manual Process Variability)

To simulate manual bench trial conditions (mixing inconsistency, drying defects):

```bash
python -m production_optimizer.phase2_bench
```

This module identifies failure points (18% risk of disintegration) due to manual handling, leading to a safer recommended formulation for physical trials.

## Phase 3 Contract Extrusion (Virtual Process Window)

To validate industrial feasibility without buying a machine:

```bash
python -m production_optimizer.phase3_extrusion
```

Simulates 1,000,000 machine runs to find "Safe Operating Parameters" for a rented extruder (~350 RPM, 123°C).
