"""
Render front elevation and top plan 3D views for key equipment.
"""

import os
import trimesh
import pyvista as pv

WORKSPACE_ROOT = r"d:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization"
STEP_DIR = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "step")
PNG_DIR = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "png")

pv.set_plot_theme("document")

ADDITIONAL_VIEWS = [
    ("TK-101_Soak_Tank.step", "TK-101_SolidWorks_3D_Front.png", "#a3c4e0", "xz", 1.20),
    ("TK-101_Soak_Tank.step", "TK-101_SolidWorks_3D_Top.png", "#a3c4e0", "xy", 1.20),
    ("DR-101_Fluid_Bed_Dryer.step", "DR-101_SolidWorks_3D_Front.png", "#9ec1db", "xz", 1.20),
    ("DR-101_Fluid_Bed_Dryer.step", "DR-101_SolidWorks_3D_Top.png", "#9ec1db", "xy", 1.20),
    ("SK-100_Dosing_Skid.step", "SK-100_SolidWorks_3D_Front.png", "#adcfe6", "xz", 1.20),
    ("EV-101_ZLD_Evaporator.step", "EV-101_SolidWorks_3D_Front.png", "#9dbed6", "xz", 1.20),
    ("CY-101_Cyclone_Separator.step", "CY-101_SolidWorks_3D_Front.png", "#a8c6de", "xz", 1.20),
    ("PLANT-15T_General_Arrangement.step", "PLANT-15T_SolidWorks_3D_Front.png", "#9bbcd8", "xz", 1.10),
    ("PLANT-15T_General_Arrangement.step", "PLANT-15T_SolidWorks_3D_Top.png", "#9bbcd8", "xy", 1.10),
]

for step_name, out_name, color, cam_pos, zoom in ADDITIONAL_VIEWS:
    step_file = os.path.join(STEP_DIR, step_name)
    out_file = os.path.join(PNG_DIR, out_name)
    print(f"Rendering {step_name} [{cam_pos}] -> {out_name}...")
    try:
        scene = trimesh.load(step_file)
        geom = scene.to_geometry()
        mesh = trimesh.util.concatenate(list(geom.values())) if isinstance(geom, dict) else geom
        pv_mesh = pv.wrap(mesh)
        plotter = pv.Plotter(off_screen=True, window_size=[2000, 1500])
        plotter.set_background("white")
        plotter.add_mesh(pv_mesh, color=color, specular=0.55, specular_power=25, smooth_shading=True, show_edges=True, edge_color="#2b4766", line_width=0.4)
        plotter.camera_position = cam_pos
        plotter.camera.zoom(zoom)
        plotter.screenshot(out_file)
        plotter.close()
        print(f"  -> Saved: {out_file} ({os.path.getsize(out_file):,} B)")
    except Exception as e:
        print(f"  Error: {e}")

print("Additional 3D views complete!")
