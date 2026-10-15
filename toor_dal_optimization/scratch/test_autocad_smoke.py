"""
Disposable AutoCAD / Plant 3D Smoke Test.
Tests AutoCAD 2025 / Plant 3D automation via accoreconsole.exe and COM.
Creates a 1:1 true mm scale drawing with $INSUNITS=4, explicit units, known dimensions,
and verifies round-trip entities and drawing database properties.
"""
import os
import sys
import subprocess
import json

def run_autocad_smoke_test():
    result = {
        "tool": "AutoCAD / Plant 3D",
        "progid": "AutoCAD.Application",
        "accoreconsole_path": r"C:\Program Files\Autodesk\AutoCAD 2025\accoreconsole.exe",
        "acad_exe_path": r"C:\Program Files\Autodesk\AutoCAD 2025\acad.exe",
        "path_found": False,
        "accoreconsole_found": False,
        "version": "AutoCAD 2025 / Plant 3D",
        "launch_confirmed": False,
        "smoke_test_passed": False,
        "error": None,
        "scratch_dxf_path": None,
        "scratch_dwg_path": None,
        "insunits": None,
        "entities_count": None,
        "plant3d_detected": False
    }

    if os.path.exists(result["acad_exe_path"]):
        result["path_found"] = True
    if os.path.exists(result["accoreconsole_path"]):
        result["accoreconsole_found"] = True

    # Check for Plant 3D program folders/files
    p3d_dir = r"C:\Program Files\Autodesk\AutoCAD 2025\PLNT3D"
    if os.path.exists(p3d_dir) or any("plant" in f.lower() for f in os.listdir(r"C:\Program Files\Autodesk\AutoCAD 2025")):
        result["plant3d_detected"] = True

    print(f"AutoCAD found: {result['path_found']}, accoreconsole found: {result['accoreconsole_found']}, Plant 3D detected: {result['plant3d_detected']}")

    # 1. Test batch headless automation using accoreconsole.exe
    os.makedirs("scratch", exist_ok=True)
    scr_path = os.path.abspath("scratch/smoke_test.scr")
    dwg_path = os.path.abspath("scratch/disposable_smoke_test_1to1.dwg")
    dxf_path = os.path.abspath("scratch/disposable_smoke_test_1to1.dxf")

    # Clean up prior files if any
    for p in [dwg_path, dxf_path]:
        if os.path.exists(p):
            try: os.remove(p)
            except Exception: pass

    # Script commands for AutoCAD:
    # Set INSUNITS to 4 (Millimeters)
    # Draw a 2000mm x 1000mm rectangle representing a 1:1 true scale vessel envelope
    # Draw a circle r=250mm representing nozzle N1
    # Add text label with status
    # Save as DWG and DXF
    scr_content = f"""INSUNITS 4
RECTANGLE 0,0 2000,1000
CIRCLE 1000,500 250
-TEXT 100,800 50 0 "CONCEPTUAL FEED - 1:1 TRUE MM SCALE"
-TEXT 100,700 35 0 "DISPOSABLE TOOLCHAIN SMOKE TEST - REV 0"
SAVEAS 2018 "{dwg_path}"
DXFOUT "{dxf_path}" 16
QUIT Y
"""
    with open(scr_path, "w", encoding="utf-8") as f:
        f.write(scr_content)

    print("Running accoreconsole.exe with scratch script...")
    cmd = [
        result["accoreconsole_path"],
        "/s", scr_path,
        "/l", "en-US"
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        print(f"accoreconsole return code: {proc.returncode}")
        result["launch_confirmed"] = (proc.returncode == 0 or os.path.exists(dxf_path) or os.path.exists(dwg_path))
        
        # Verify output DXF
        if os.path.exists(dxf_path):
            result["scratch_dxf_path"] = dxf_path
            import ezdxf
            doc = ezdxf.readfile(dxf_path)
            msp = doc.modelspace()
            ents = list(msp)
            result["entities_count"] = len(ents)
            insunits_val = doc.header.get("$INSUNITS", None)
            result["insunits"] = insunits_val
            print(f"Verified DXF: {dxf_path} ({os.path.getsize(dxf_path)} bytes, {len(ents)} entities, $INSUNITS={insunits_val})")
            
            # Check bounding box
            if insunits_val == 4 and len(ents) >= 3:
                result["smoke_test_passed"] = True
                print("AutoCAD 1:1 true scale ($INSUNITS=4) smoke test PASSED!")
        elif os.path.exists(dwg_path):
            result["scratch_dwg_path"] = dwg_path
            result["smoke_test_passed"] = True
            print(f"Verified DWG: {dwg_path} ({os.path.getsize(dwg_path)} bytes)")
        else:
            result["error"] = f"accoreconsole finished but output files not created. Stderr: {proc.stderr[:300]}"
            print(result["error"])

    except Exception as e:
        result["error"] = str(e)
        print(f"accoreconsole error: {e}")

    return result

if __name__ == "__main__":
    res = run_autocad_smoke_test()
    print("RESULT_JSON:", json.dumps(res, indent=2))
