# Machinery Optimization Report

**Method:** GPU-Accelerated Monte Carlo Simulation (10 Million Scenarios)
**Objective:** Minimize Capital Expenditure (CapEx) via "Make vs Buy".

## 1. Industrial Tray Dryer (500kg/Batch)

- **Problem:** Process requires 100kg/hr avg throughput.
- **Solution:** Large 96-Tray Dryer (500kg Batch x 2 Shifts).
- **Analysis:**
  - **Market Price:** ~₹4.5 Lakhs.
  - **DIY Build Cost:** ~₹3.3 Lakhs (P50).
  - **Decision:** **BUILD (DIY)**.
  - **Critical Components:**
    - SS304 Sheet 18G (450kg)
    - 2x 2HP IE2 Motors (1440 RPM)
    - 12x 1.5kW Fin Heaters
    - PID Controller

## 2. Cold Press Expeller (Mustard Oil)

- **Problem:** "Kachi Ghani" requires <45°C.
- **Analysis:**
  - **Market Price:** ~₹1.8 Lakhs.
  - **DIY Build Cost:** ~₹1.35 Lakhs.
  - **Constraint:** Wooden mortar latency and gearbox alignment is complex. Risk of failure > Cost savings.
  - **Decision:** **BUY (Market)** (Standard Wooden Ghani).

## 3. Bilona Churner (500L SS316)

- **Problem:** Bi-directional slow churning.
- **Analysis:**
  - **Market Price:** ~₹1.2 Lakhs.
  - **DIY Build Cost:** ~₹60k.
  - **Decision:** **BUILD (DIY)**.
  - **Savings:** 50% Flat.

## System Performance

- **Optimization Time:** 0.16s (NVIDIA RTX 4050).
- **Total Simulations:** 10,000,000 Scenarios.
