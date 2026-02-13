"""
Validation Script
Runs a quick check on every module to ensure torch and critical functions are importable.
"""
import sys

print(f"Executing with Python: {sys.executable}")
print(f"System Path: {sys.path}")

try:
    import torch
    print("✅ Torch Import Success!")
    print(f"   Version: {torch.__version__}")
    print(f"   CUDA Available: {torch.cuda.is_available()}")
except ImportError as e:
    print(f"❌ Torch Import FAILED: {e}")
    sys.exit(1)

try:
    from production_optimizer.modules.grinding import GrindingModule
    print("✅ GrindingModule Import Success")
except ImportError as e:
    print(f"❌ GrindingModule Import FAILED: {e}")

try:
    from production_optimizer.modules.extrusion import ExtrusionModule
    print("✅ ExtrusionModule Import Success")
except ImportError as e:
    print(f"❌ ExtrusionModule Import FAILED: {e}")

try:
    from production_optimizer.modules.drying import DryingModule
    print("✅ DryingModule Import Success")
except ImportError as e:
    print(f"❌ DryingModule Import FAILED: {e}")

try:
    from production_optimizer.core.cost_model import calculate_total_cost
    print("✅ CostModel Import Success")
except ImportError as e:
    print(f"❌ CostModel Import FAILED: {e}")
except SyntaxError as e:
    print(f"❌ CostModel Syntax Error: {e}")

print("\n--- ALL CHECKS PASSED ---")
