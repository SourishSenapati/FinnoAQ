# FinnoAQ: Six Sigma Digital Twins for Natural Food Processing

Advanced Physics-Based Simulations and Machinery Optimization Engine for:

1. **Toor Dal Analogue** (Protein Thermodynamics)
2. **Atta Bio-Enzymatic** (Rheology & Enzyme Kinetics)
3. **Ghee Bilona** (Vessel Thermodynamics & Optimization)
4. **Mustard Oil Herbal** (Cold Press Physics & Oxidative Stability)
5. **Honey Value-Add** (Creaming & Fermentation)

## Key Features

- **GPU-Accelerated Optimization**: Automatically tunes process parameters (Extrusion Temp, Churning Temp) to minimize defects.
- **Machinery Monte Carlo**: Analyzes 10 Million scenarios to optimize "Make vs Buy" decisions for equipment.
- **Six Sigma Fidelity**: Targets < 3.4 DPMO quality levels.

## Reports

- [**Simulation Logs**](./SIMULATION_LOGS.md): Detailed output of the latest validation run.
- [**Machinery Optimization Report**](./machinery/MACHINERY_REPORT.md): Cost analysis for Tray Dryers, Cold Press, and Churners.
- [**Optimization Results**](./OPTIMIZATION_RESULTS.md): Summary of process parameter tuning.

## Usage

Run the full suite:

```bash
python run_all_simulations.py
```

(Requires `torch` with CUDA support)
