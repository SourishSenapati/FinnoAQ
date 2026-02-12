# Toor Dal Analogue Manufacturing Project

## 1. Project Overview

This repository contains the technical documentation, formulation specifications, and simulation models for the industrial production of a cost-optimized, high-fidelity Toor Dal (Pigeon Pea) Analogue. The project aims to reduce raw material costs by ₹1.43/kg while maintaining the organoleptic profile of the natural pulse through a scientifically engineered starch-protein-hydrocolloid matrix.

## 2. Directory Structure

- **`specifications.md`**: Detailed technical formulation, cost breakdown (MSG-Optimized), and critical process parameters for extrusion and drying.
- **`simulation_toor_dal.py`**: A GPU-accelerated (CUDA) Monte Carlo simulation script designed to validate production economics and process stability at industrial scale.

## 3. Simulation Module capabilities

The included Python script (`simulation_toor_dal.py`) leverages PyTorch for high-performance parallel computation on NVIDIA GPUs.

**Key Features:**

- **Scale**: Simulates **10,000,000 (10 Million)** independent production batches to ensure statistical significance.
- **Market Volatility Analysis**: Models raw material price fluctuations using Gaussian distributions to predict cost variance.
- **Process Capability Analysis (Six Sigma)**: Validates manufacturing robustness by simulating temperature and moisture deviations against critical failure modes (Flash Gelation, Stress Cracking, Rheological Failure).
- **Financial Projections**: Computes ROI and Grant Margin distributions based on dynamic input costs.

## 4. Execution Instructions

### Prerequisites

- Python 3.8+
- PyTorch (with CUDA support recommended for performance)

### Running the Simulation

Execute the script from the terminal:

```bash
python simulation_toor_dal.py
```

**Note**: The simulation will automatically detect available CUDA hardware (e.g., NVIDIA RTX 4050) and offload tensor computations to the GPU. If no GPU is found, it will default to CPU execution with a performance warning.
