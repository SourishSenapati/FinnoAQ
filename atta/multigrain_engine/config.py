"""
Configuration for Multigrain Atta Project.
Defines:
1. Non-GMO Grain Prices & Nutrition.
2. Spent Spice (Zero-Waste) Integration.
3. 6 Sigma Quality Targets.
"""

# --- 1. PRICING (INR/kg) - NON-GMO SOURCING ---
# Prices verified vs Mandi Rates (Feb 2026)
GRAIN_PRICES = {
    # Base
    "wheat_soft": 25.0,  # Lokwan (Market corrected from 22.5)
    "wheat_hard": 28.0,  # Sharbati (Premium)

    # Cheap Fillers (Non-GMO)
    "maize": 19.5,       # Makka
    "bajra": 23.0,       # Pearl Millet

    # Mid-Range Millets
    "jowar": 32.0,       # Sorghum
    "ragi": 28.0,
    "barley": 35.0,

    # Premium / Functional
    "oats": 45.0,
    "soybean_nongmo": 55.0,
    "chana": 60.0,
    "vital_wheat_gluten": 100.0,  # CRITICAL: Texture fixer

    # "Jugaad" Innovation (SENSORY CORRECTED)
    "spent_turmeric": 12.0,   # Food grade extraction waste
    "spent_cumin": 10.0,
    "spent_fenugreek": 25.0   # DE-BITTERIZED Fiber (Premium processing)
}

# --- 1.B SENSORY LIMITS (Max % in blend) ---
# Critical for taste acceptability
MAX_LIMITS = {
    "spent_fenugreek": 0.06,  # Max 6% (Reduced from 8% for bitterness)
    "spent_turmeric": 0.03,   # Max 3%
    "maize": 0.20,            # Max 20%
    "soybean_nongmo": 0.10,   # Max 10%
    "spent_cumin": 0.01,      # Max 1% (NO Masala Roti!)
    "vital_wheat_gluten": 0.02  # Max 2% (Costly but effective)
}

# --- 2. NUTRITIONAL PROFILES (Per 100g) ---
# Used for Linear Programming Optimization
GRAIN_NUTRITION = {
    #                 Prot,  Fib,  Cost (Verified)
    "wheat_soft":    (10.0, 2.5,  25.0),
    "wheat_hard":    (13.0, 2.8,  28.0),
    "maize":         (9.0,  2.0,  19.5),
    "bajra":         (11.0, 3.0,  23.0),
    "jowar":         (10.0, 2.0,  32.0),
    "ragi":          (7.0,  3.6,  28.0),
    "barley":        (11.0, 16.0, 35.0),
    "soybean_nongmo": (36.0, 5.0,  55.0),
    "chana":         (20.0, 4.0,  60.0),
    "vital_wheat_gluten": (75.0, 0.0, 100.0),  # Pure Protein
    "oats":          (12.0, 10.0, 45.0),
    "spent_turmeric": (8.0, 12.0, 12.0),
    "spent_fenugreek": (28.0, 32.0, 25.0),
    "spent_cumin": (18.0, 10.0, 10.0)
}

# --- 3. MACHINERY SPECIFICATIONS (Energy & CAPEX) ---
MACHINERY_SPECS = {
    "lab": {
        "scale": "5kg/hr",
        "grinder": "Stone Burr Mill (Chakki) 1HP",
        "mixer": "Planetary Mixer 10L",
        "sifter": "Vibratory Sifter (Manual Feed)",
        "capex": 85000,  # INR
        "power_kw": 1.5
    },
    "industrial": {
        "scale": "2000kg/hr",
        "cleaning": "Destoner + Scourer + Magnetic Separator",
        "conditioning": "Water Dampener + Tempering Bins (12hr)",
        "milling": "4-Pass Roller Mill (Break) + 2-Pass Reduction",
        "sieving": "8-Channel Plansifter",
        "blending": "Ribbon Blender 1000L",
        "packing": "FFS Pneumatic Packer",
        "capex": 15000000,  # 1.5 Cr INR
        "power_kw": 180.0
    }
}

# --- 4. 6-SIGMA QUALITY TARGETS ---
TARGETS = {
    "cost_per_kg": 30.0,       # INR (Strict Upper Limit)
    "protein_min": 11.5,       # % (Realistic given 10% Soya cap)
    "fiber_min": 4.0,          # % (High Fiber = 2x Wheat Base, not 10%)
    "water_absorption": 75.0,  # % (Soft Roti indicator)
    "particle_size_d90": 150.0  # microns (Non-gritty)
}
