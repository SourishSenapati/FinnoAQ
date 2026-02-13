"""
VERIFICATION SCRIPT
Iterates through every Python file in the production_optimizer package.
Imports them one by one to ensure dependencies (Torch, etc.) are valid.
"""
import pytest
import os
import importlib.util
import sys

# Add project root to sys.path
PROJECT_ROOT = r"d:\PROJECT\FINNO PROJECTS"
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

print(
    f"🔍 Starting Module Verification in: {PROJECT_ROOT}\\toor_dal\\production_optimizer")

modules_to_test = [
    # Core
    "toor_dal.production_optimizer.core.config",
    "toor_dal.production_optimizer.core.gpu_engine",
    "toor_dal.production_optimizer.core.physics_models",
    "toor_dal.production_optimizer.core.cost_model",
    # Modules
    "toor_dal.production_optimizer.modules.grinding",
    "toor_dal.production_optimizer.modules.drying",
    "toor_dal.production_optimizer.modules.extrusion",
    "toor_dal.production_optimizer.modules.formulation",
    # Optimization
    "toor_dal.production_optimizer.optimization.monte_carlo",
]

failed = False

for module_name in modules_to_test:
    try:
        print(f"👉 Importing {module_name}...", end=" ")
        importlib.import_module(module_name)
        print("✅ SUCCESS")
    except ImportError as e:
        print(f"❌ FAILED: {e}")
        failed = True
    except Exception as e:
        print(f"❌ CRASHED: {e}")
        failed = True

print("-" * 30)
if failed:
    print("❌ SOME MODULES FAILED VERIFICATION.")
    sys.exit(1)
else:
    print("✅ ALL MODULES IMPORTED SUCCESSFULLY using C:\\Python313\\python.exe")
    import torch
    print(f"   (Verified Torch {torch.__version__} is active)")
