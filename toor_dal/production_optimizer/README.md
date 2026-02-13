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
