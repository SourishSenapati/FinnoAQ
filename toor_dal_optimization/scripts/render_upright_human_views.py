"""
Render all authentic SolidWorks STEP models and joined assembly in proper human viewing orientation.
Coordinate System Ground Truth:
  Y-axis = Vertical Elevation (UP) [0, 1, 0]
  X-axis = Lateral Width
  Z-axis = Longitudinal Process Flow
"""

import os
import trimesh
import pyvista as pv
import numpy as np

WORKSPACE_ROOT = r"d:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization"
STEP_DIR = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "step")
PNG_DIR = os.path.join(WORKSPACE_ROOT, "engineering", "cad", "png")

pv.set_plot_theme("document")

def render_mesh_upright(mesh, out_png, view_type="iso", zoom=1.15, color="#a0c2de", title=""):
    pv_mesh = pv.wrap(mesh)
    b = mesh.bounds
    center = mesh.centroid
    dx = b[1][0] - b[0][0]
    dy = b[1][1] - b[0][1]
    dz = b[1][2] - b[0][2]
    diag = np.sqrt(dx**2 + dy**2 + dz**2)
    
    plotter = pv.Plotter(off_screen=True, window_size=[2400, 1800])
    plotter.set_background("white")
    
    plotter.add_mesh(
        pv_mesh,
        color=color,
        specular=0.55,
        specular_power=25,
        smooth_shading=True,
        show_edges=True,
        edge_color="#2b4766",
        line_width=0.4
    )
    
    focal_point = [center[0], center[1], center[2]]
    view_up = [0, 1, 0] # Y IS ALWAYS UP
    
    if view_type == "iso":
        # Elevated front-right 3D perspective
        cam_pos = [
            center[0] + 1.2 * diag,
            center[1] + 0.8 * diag,
            center[2] + 1.2 * diag
        ]
    elif view_type == "iso_reverse":
        # Elevated back-left 3D perspective
        cam_pos = [
            center[0] - 1.2 * diag,
            center[1] + 0.9 * diag,
            center[2] - 1.1 * diag
        ]
    elif view_type == "front":
        # Direct front elevation (looking towards -Z)
        cam_pos = [
            center[0],
            center[1],
            center[2] + 1.6 * diag
        ]
    elif view_type == "side":
        # Direct side elevation (looking towards -X)
        cam_pos = [
            center[0] + 1.6 * diag,
            center[1],
            center[2]
        ]
    elif view_type == "top":
        # Direct top plan (looking straight down from +Y)
        cam_pos = [
            center[0],
            center[1] + 1.6 * diag,
            center[2]
        ]
        view_up = [0, 0, -1]
    elif view_type == "mezzanine_close":
        # Close-up on Mezzanine operating deck
        focal_point = [0.0, 4.5, 0.0]
        cam_pos = [6.0, 6.2, 5.5]
    elif view_type == "dryer_close":
        # Close-up on Fluid Bed Dryer and Cyclone
        focal_point = [1.0, 1.8, -5.5]
        cam_pos = [7.5, 3.8, -1.5]
    elif view_type == "evap_close":
        # Close-up on Evaporator Skid & Chemical Dosing Skid
        focal_point = [-4.5, 1.5, -2.8]
        cam_pos = [-13.0, 5.0, 3.2]
    else:
        cam_pos = [center[0] + diag, center[1] + diag, center[2] + diag]
        
    plotter.camera_position = [cam_pos, focal_point, view_up]
    plotter.camera.zoom(zoom)
    
    plotter.screenshot(out_png)
    plotter.close()
    print(f"Rendered [{view_type:15s}] -> {out_png} ({os.path.getsize(out_png):,} B)")


def main():
    print("=================================================================")
    print("RENDERING ALL CAD MODELS IN PROPER HUMAN VIEWING ORIENTATION (Y=UP)")
    print("=================================================================")
    
    # 1. Master Joined Plant Assembly (PLANT-15T_General_Arrangement.step)
    plant_step = os.path.join(STEP_DIR, "PLANT-15T_General_Arrangement.step")
    print("Loading Joined Plant Master Assembly...")
    sc_plant = trimesh.load(plant_step)
    geom_plant = sc_plant.to_geometry()
    m_plant = trimesh.util.concatenate(list(geom_plant.values())) if isinstance(geom_plant, dict) else geom_plant
    print(f"Loaded Master Joined Mesh: {len(m_plant.vertices):,} vertices, {len(m_plant.faces):,} faces")
    
    # Render Master Joined Plant from multiple human viewing perspectives
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Iso_HumanView.png"), "iso", 1.15, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Reverse_HumanView.png"), "iso_reverse", 1.15, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Front_HumanView.png"), "front", 1.15, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Side_HumanView.png"), "side", 1.15, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Top_HumanView.png"), "top", 1.10, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Mezzanine_Detail.png"), "mezzanine_close", 1.25, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Dryer_Cyclone_Detail.png"), "dryer_close", 1.25, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_Joined_Evaporator_Detail.png"), "evap_close", 1.25, "#9bbcd8")
    
    # Overwrite the standard SolidWorks Iso render with the upright human viewing render
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_SolidWorks_3D_Iso.png"), "iso", 1.15, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_SolidWorks_3D_Front.png"), "front", 1.15, "#9bbcd8")
    render_mesh_upright(m_plant, os.path.join(PNG_DIR, "PLANT-15T_SolidWorks_3D_Top.png"), "top", 1.10, "#9bbcd8")
    
    # 2. Individual Component Models (Standing Upright, Y=UP)
    components = [
        ("TK-101_Soak_Tank.step", "TK-101_SolidWorks_3D_Iso.png", "TK-101_SolidWorks_3D_Front.png", "TK-101_SolidWorks_3D_Top.png", "#a3c4e0"),
        ("AG-101_Agitator.step", "AG-101_SolidWorks_3D_Iso.png", None, None, "#c0d0e0"),
        ("SC-101_Dewatering_Screen.step", "SC-101_SolidWorks_3D_Iso.png", None, None, "#b0c8d8"),
        ("DR-101_Fluid_Bed_Dryer.step", "DR-101_SolidWorks_3D_Iso.png", "DR-101_SolidWorks_3D_Front.png", "DR-101_SolidWorks_3D_Top.png", "#9ec1db"),
        ("CY-101_Cyclone_Separator.step", "CY-101_SolidWorks_3D_Iso.png", "CY-101_SolidWorks_3D_Front.png", None, "#a8c6de"),
        ("SK-100_Dosing_Skid.step", "SK-100_SolidWorks_3D_Iso.png", "SK-100_SolidWorks_3D_Front.png", None, "#adcfe6"),
        ("EV-101_ZLD_Evaporator.step", "EV-101_SolidWorks_3D_Iso.png", "EV-101_SolidWorks_3D_Front.png", None, "#9dbed6"),
        ("STR-100_Mezzanine_Platform.step", "STR-100_SolidWorks_3D_Iso.png", None, None, "#b8c4ce"),
        ("CHU-100_Transfer_Chutes.step", "CHU-100_SolidWorks_3D_Iso.png", None, None, "#b0c8d8"),
        ("PIP-100_Interconnecting_Piping.step", "PIP-100_SolidWorks_3D_Iso.png", None, None, "#a0c0d8"),
    ]
    
    for step_file, iso_png, front_png, top_png, color in components:
        step_path = os.path.join(STEP_DIR, step_file)
        if not os.path.exists(step_path):
            continue
        sc = trimesh.load(step_path)
        geom = sc.to_geometry()
        m = trimesh.util.concatenate(list(geom.values())) if isinstance(geom, dict) else geom
        
        render_mesh_upright(m, os.path.join(PNG_DIR, iso_png), "iso", 1.15, color)
        if front_png:
            render_mesh_upright(m, os.path.join(PNG_DIR, front_png), "front", 1.20, color)
        if top_png:
            render_mesh_upright(m, os.path.join(PNG_DIR, top_png), "top", 1.15, color)

    print("=================================================================")
    print("ALL 3D CAD MODELS SUCCESSFULLY RENDERED IN UPRIGHT HUMAN ORIENTATION!")
    print("=================================================================")

if __name__ == "__main__":
    main()
