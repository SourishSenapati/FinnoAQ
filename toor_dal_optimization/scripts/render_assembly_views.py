"""
Render high-resolution isometric, front, and perspective views of the
connected PLANT-15T SolidWorks Master Assembly to PNG image files.
"""

import os
import win32com.client
import pythoncom

WORKSPACE_ROOT = r"d:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization"
SLDASM_PATH = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "native", "PLANT-15T_General_Arrangement.SLDASM")
RENDER_DIR = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "png")
os.makedirs(RENDER_DIR, exist_ok=True)

def render_assembly_views():
    sw = win32com.client.Dispatch("SldWorks.Application")
    sw.Visible = True  # Must be visible to initialize OpenGL viewport for image capture

    err = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    warn = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    doc = sw.OpenDoc6(SLDASM_PATH, 2, 1, "", err, warn) # 2 = swDocASSEMBLY

    if not doc:
        print("Failed to open assembly document for rendering.")
        return

    title = doc.GetTitle

    # Setup Viewport
    doc.ViewZoomtofit2()
    
    # 1. Isometric View
    try:
        doc.ShowNamedView2("*Isometric", 7) # 7 = swIsometricView
        doc.ViewZoomtofit2()
    except Exception:
        pass
    
    iso_png = os.path.join(RENDER_DIR, "PLANT-15T_Isometric_HighDef.png")
    doc.SaveAs(iso_png)
    print(f"Saved: {iso_png} ({os.path.getsize(iso_png) if os.path.exists(iso_png) else 0} bytes)")

    # 2. Front View
    try:
        doc.ShowNamedView2("*Front", 1) # 1 = swFrontView
        doc.ViewZoomtofit2()
    except Exception:
        pass
    front_png = os.path.join(RENDER_DIR, "PLANT-15T_Front_Elevation_HighDef.png")
    doc.SaveAs(front_png)
    print(f"Saved: {front_png} ({os.path.getsize(front_png) if os.path.exists(front_png) else 0} bytes)")

    # 3. Top View
    try:
        doc.ShowNamedView2("*Top", 5) # 5 = swTopView
        doc.ViewZoomtofit2()
    except Exception:
        pass
    top_png = os.path.join(RENDER_DIR, "PLANT-15T_Top_Plan_HighDef.png")
    doc.SaveAs(top_png)
    print(f"Saved: {top_png} ({os.path.getsize(top_png) if os.path.exists(top_png) else 0} bytes)")

    sw.CloseDoc(title)
    sw.Visible = False

if __name__ == "__main__":
    render_assembly_views()
