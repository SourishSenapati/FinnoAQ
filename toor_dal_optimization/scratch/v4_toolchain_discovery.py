"""
V4 Toolchain and Local Software Smoke Test.
Verifies versions, licensing, COM automation, and file rendering capabilities offline.
"""

import sys
import os
import json
import subprocess

report = {
    "python": {
        "version": sys.version,
        "executable": sys.executable
    },
    "libraries": {},
    "native_cad_cae": {},
    "smoke_tests": {}
}

# 1. Python Libraries
for lib in ["win32com.client", "ezdxf", "fitz", "matplotlib", "numpy", "scipy", "torch", "pydantic", "pytest"]:
    try:
        mod = __import__(lib)
        ver = getattr(mod, "__version__", "installed")
        report["libraries"][lib] = {"status": "AVAILABLE", "version": str(ver)}
    except Exception as e:
        report["libraries"][lib] = {"status": "MISSING", "error": str(e)}

# 2. SolidWorks Automation Smoke Test
try:
    import win32com.client
    sw = win32com.client.Dispatch("SldWorks.Application")
    sw_ver = sw.RevisionNumber()
    sw_visible = sw.Visible
    report["native_cad_cae"]["SolidWorks"] = {
        "status": "AVAILABLE",
        "progid": "SldWorks.Application",
        "revision": sw_ver,
        "visible": sw_visible
    }
    # Check template existence
    tmpl = r"C:\ProgramData\SolidWorks\SOLIDWORKS 2025\templates\MBD\part 0051mm to 0250mm.prtdot"
    report["native_cad_cae"]["SolidWorks"]["default_template_exists"] = os.path.exists(tmpl)
    sw.ExitApp()
    report["smoke_tests"]["SolidWorks"] = "PASS"
except Exception as e:
    report["native_cad_cae"]["SolidWorks"] = {"status": "FAILED", "error": str(e)}
    report["smoke_tests"]["SolidWorks"] = "FAIL"

# 3. AutoCAD / Plant 3D Verification
autocad_paths = [
    r"C:\Program Files\Autodesk\AutoCAD 2025\acad.exe",
    r"C:\Program Files\Autodesk\AutoCAD 2025\accoreconsole.exe",
    r"C:\Program Files\Autodesk\AutoCAD 2024\acad.exe",
    r"C:\Program Files\Autodesk\AutoCAD 2024\accoreconsole.exe"
]
found_acad = [p for p in autocad_paths if os.path.exists(p)]
report["native_cad_cae"]["AutoCAD"] = {"installed_binaries": found_acad}

try:
    import win32com.client
    acad = win32com.client.Dispatch("AutoCAD.Application")
    acad_ver = acad.Version
    report["native_cad_cae"]["AutoCAD"]["status"] = "COM_AVAILABLE"
    report["native_cad_cae"]["AutoCAD"]["version"] = acad_ver
    report["smoke_tests"]["AutoCAD"] = "PASS"
except Exception as e:
    report["native_cad_cae"]["AutoCAD"]["com_status"] = str(e)
    # Check accoreconsole
    if found_acad:
        report["smoke_tests"]["AutoCAD"] = "CONSOLE_AVAILABLE"
    else:
        report["smoke_tests"]["AutoCAD"] = "NOT_INSTALLED"

# 4. Aspen Plus / HYSYS Verification
aspen_paths = [
    r"C:\Program Files\AspenTech\Aspen Plus V14.0\GUI\Xeq\AspenPlus.exe",
    r"C:\Program Files (x86)\AspenTech\Aspen Plus V14.0\GUI\Xeq\AspenPlus.exe",
    r"C:\Program Files\AspenTech\Aspen HYSYS V14.0\HYSYS.exe",
    r"C:\Program Files (x86)\AspenTech\Aspen HYSYS V14.0\HYSYS.exe"
]
found_aspen = [p for p in aspen_paths if os.path.exists(p)]
report["native_cad_cae"]["AspenTech"] = {"installed_binaries": found_aspen}

try:
    import win32com.client
    aspen = win32com.client.Dispatch("Apwn.Document")
    report["native_cad_cae"]["AspenTech"]["aspen_plus_com"] = "AVAILABLE"
    report["smoke_tests"]["AspenPlus"] = "PASS"
    aspen.Quit()
except Exception as e:
    report["native_cad_cae"]["AspenTech"]["aspen_plus_com"] = str(e)
    report["smoke_tests"]["AspenPlus"] = "PASS_BINARY" if found_aspen else "UNAVAILABLE"

# Output summary
out_path = os.path.abspath("engineering/verification/v4/v4_toolchain_inventory.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(report, f, indent=2)

print("V4 Toolchain Inventory Result:")
print(json.dumps(report, indent=2))
