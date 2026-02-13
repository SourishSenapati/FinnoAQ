"""
Script to debug import paths and verification for finno_visuals.
"""

import sys
import os
print("CWD:", os.getcwd())
print("SYS.PATH:", sys.path)
try:
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    print("SYS.PATH AFTER:", sys.path)
    # Check if file exists
    target = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "finno_visuals.py")
    print(f"Checking {target}: {os.path.exists(target)}")

    import finno_visuals
    print("SUCCESS importing finno_visuals")
    print("Dir:", dir(finno_visuals))
except (ImportError, ModuleNotFoundError) as e:
    print("FAIL:", e)
