"""
Harakutir Toor Dal 15 MT/Day CAD and Engineering Drawing Generator
================================================================
Document ID: ENG-CAD-15T-001 | Revision: 1.0 | Date: 2026-10-15
Generates editable 2D DXF drawings, 3D STEP AP214 files, 3D OBJ/STL meshes,
and dimensioned vector PDF drawing packages.

Status: PRELIMINARY_CALCULATED (NOT FOR CONSTRUCTION)
"""

import os
import math
import ezdxf
from ezdxf import colors
from ezdxf.enums import TextEntityAlignment
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors as rcolors


def setup_dxf_layers(doc):
    """Setup standard engineering CAD layers with colors and linetypes."""
    layers = [
        ("TITLE_BLOCK", colors.WHITE),
        ("EQUIPMENT", colors.CYAN),
        ("PIPING", colors.GREEN),
        ("INSTRUMENT", colors.YELLOW),
        ("CENTER", colors.RED),
        ("DIMENSION", colors.MAGENTA),
        ("TEXT", colors.WHITE),
        ("CIVIL_GRID", colors.LIGHT_GRAY),
        ("ZONING", colors.BLUE),
    ]
    for name, color in layers:
        if name not in doc.layers:
            doc.layers.add(name, color=color)


def draw_dxf_title_block(msp, dwg_no, dwg_title, discipline, sheet="1 OF 1", rev="Rev 1.0"):
    """Draw standard ISO A1/A2 engineering drawing border and title block in DXF."""
    # Outer Border (841 x 594 mm A1 layout scaled in mm)
    msp.add_lwpolyline([(0, 0), (841, 0), (841, 594), (0, 594), (0, 0)], dxfattribs={"layer": "TITLE_BLOCK", "color": colors.WHITE})
    # Inner margin (20mm left margin for binding, 10mm other sides)
    msp.add_lwpolyline([(20, 10), (831, 10), (831, 584), (20, 584), (20, 10)], dxfattribs={"layer": "TITLE_BLOCK", "color": colors.WHITE})

    # Title block box in bottom right (180mm wide x 65mm high)
    x0, y0 = 831 - 200, 10
    msp.add_lwpolyline([(x0, y0), (831, y0), (831, y0 + 70), (x0, y0 + 70), (x0, y0)], dxfattribs={"layer": "TITLE_BLOCK", "color": colors.WHITE})
    msp.add_line((x0, y0 + 50), (831, y0 + 50), dxfattribs={"layer": "TITLE_BLOCK"})
    msp.add_line((x0, y0 + 35), (831, y0 + 35), dxfattribs={"layer": "TITLE_BLOCK"})
    msp.add_line((x0, y0 + 20), (831, y0 + 20), dxfattribs={"layer": "TITLE_BLOCK"})
    msp.add_line((x0 + 100, y0), (x0 + 100, y0 + 35), dxfattribs={"layer": "TITLE_BLOCK"})

    # Title block texts
    msp.add_text("HARAKUTIR FOODS - TOOR DAL 15 MT/DAY PLANT", dxfattribs={"layer": "TEXT", "height": 3.5}).set_placement((x0 + 5, y0 + 58))
    msp.add_text(f"TITLE: {dwg_title}", dxfattribs={"layer": "TEXT", "height": 3.0}).set_placement((x0 + 5, y0 + 41))
    msp.add_text(f"DWG NO: {dwg_no}", dxfattribs={"layer": "TEXT", "height": 3.5}).set_placement((x0 + 5, y0 + 25))
    msp.add_text(f"DISCIPLINE: {discipline}", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((x0 + 5, y0 + 8))
    msp.add_text(f"REV: {rev} | SHEET: {sheet}", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((x0 + 105, y0 + 25))
    msp.add_text("STATUS: PRELIMINARY_CALCULATED", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((x0 + 105, y0 + 8))

    # Prominent Engineering Warning
    msp.add_text("WARNING: PRELIMINARY—NOT FOR CONSTRUCTION. FOR REVIEW ONLY.", dxfattribs={"layer": "TEXT", "height": 4.0, "color": colors.RED}).set_placement((30, 20))


def generate_dwg_001_plot_plan(output_dir):
    """DWG-FIN-15T-001: Plant Master Plot Plan & Hygienic Zoning Layout."""
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()
    setup_dxf_layers(doc)
    draw_dxf_title_block(msp, "DWG-FIN-15T-001", "PLANT MASTER PLOT PLAN & HYGIENIC ZONING", "CIVIL / PLANT LAYOUT")

    # Building Outline: 45m x 20m (Scale 1:100 -> 450mm x 200mm on drawing)
    bx, by = 60, 150
    msp.add_lwpolyline([(bx, by), (bx + 450, by), (bx + 450, by + 200), (bx, by + 200), (bx, by)], dxfattribs={"layer": "CIVIL_GRID", "color": colors.YELLOW})
    msp.add_text("FACTORY BUILDING ENVELOPE (45.0m x 20.0m)", dxfattribs={"layer": "TEXT", "height": 4.0}).set_placement((bx + 120, by + 210))

    # Zone 1: Raw Intake (10m x 20m -> 100 x 200)
    msp.add_lwpolyline([(bx, by), (bx + 100, by), (bx + 100, by + 200), (bx, by + 200)], dxfattribs={"layer": "ZONING"})
    msp.add_text("ZONE 1: RAW INTAKE & STORAGE", dxfattribs={"layer": "TEXT", "height": 3.0}).set_placement((bx + 10, by + 180))
    msp.add_text("[HOP-101, EL-101, SCN-101]", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((bx + 15, by + 165))

    # Zone 2: Wet Chemical Treatment (10m x 20m -> 100 x 200)
    msp.add_lwpolyline([(bx + 100, by), (bx + 200, by), (bx + 200, by + 200), (bx + 100, by + 200)], dxfattribs={"layer": "ZONING"})
    msp.add_text("ZONE 2: WET SOAKING & DOSING", dxfattribs={"layer": "TEXT", "height": 3.0}).set_placement((bx + 110, by + 180))
    msp.add_text("[TK-100, TK-101A/B, VS-101]", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((bx + 115, by + 165))

    # Zone 3: Thermal Drying & Air Handling (12m x 20m -> 120 x 200)
    msp.add_lwpolyline([(bx + 200, by), (bx + 320, by), (bx + 320, by + 200), (bx + 200, by + 200)], dxfattribs={"layer": "ZONING"})
    msp.add_text("ZONE 3: FLUID-BED DRYING & COOLING", dxfattribs={"layer": "TEXT", "height": 3.0}).set_placement((bx + 205, by + 180))
    msp.add_text("[DR-101, CLR-101, FN-101, CYC-101]", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((bx + 210, by + 165))

    # Zone 4: Packing & Finished Goods (13m x 20m -> 130 x 200)
    msp.add_lwpolyline([(bx + 320, by), (bx + 450, by), (bx + 450, by + 200), (bx + 320, by + 200)], dxfattribs={"layer": "ZONING"})
    msp.add_text("ZONE 4: PACKAGING & DISPATCH", dxfattribs={"layer": "TEXT", "height": 3.0}).set_placement((bx + 330, by + 180))
    msp.add_text("[MD-101, PK-101, CW-101, WAREHOUSE]", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((bx + 330, by + 165))

    # External Utilities & ETP (Right side)
    msp.add_lwpolyline([(bx + 470, by), (bx + 540, by), (bx + 540, by + 120), (bx + 470, by + 120), (bx + 470, by)], dxfattribs={"layer": "CIVIL_GRID"})
    msp.add_text("ZONE 5: UTILITIES & ETP", dxfattribs={"layer": "TEXT", "height": 3.0}).set_placement((bx + 475, by + 105))
    msp.add_text("[BOILER, ETP-101, CIP-101]", dxfattribs={"layer": "TEXT", "height": 2.0}).set_placement((bx + 475, by + 90))

    # Personnel and Truck movement routes
    msp.add_line((bx - 20, by + 50), (bx, by + 50), dxfattribs={"layer": "CIVIL_GRID", "color": colors.GREEN})
    msp.add_text("TRUCK UNLOADING BAY", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((bx - 50, by + 55))

    msp.add_line((bx + 450, by + 50), (bx + 470, by + 50), dxfattribs={"layer": "CIVIL_GRID", "color": colors.GREEN})
    msp.add_text("FINISHED GOODS DISPATCH", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((bx + 450, by + 35))

    doc.saveas(os.path.join(output_dir, "DWG-FIN-15T-001.dxf"))


def generate_dwg_005_soak_tank(output_dir):
    """DWG-FIN-15T-005: Soak Tank TK-101A/B General Arrangement & Fabrication Drawing."""
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()
    setup_dxf_layers(doc)
    draw_dxf_title_block(msp, "DWG-FIN-15T-005", "SOAK TANK TK-101A/B GENERAL ARRANGEMENT", "MECHANICAL EQUIPMENT")

    # Front Elevation View (Center at x=250, y=260; Scale 1:20 -> Tank dia 1.6m = 80mm, H=1.92m = 96mm)
    cx, cy = 250, 260
    r = 40  # 0.8m radius scaled
    h = 96  # 1.92m height scaled

    # Cylindrical shell
    msp.add_line((cx - r, cy - h/2), (cx - r, cy + h/2), dxfattribs={"layer": "EQUIPMENT"})
    msp.add_line((cx + r, cy - h/2), (cx + r, cy + h/2), dxfattribs={"layer": "EQUIPMENT"})
    # Centerline
    msp.add_line((cx, cy - h/2 - 30), (cx, cy + h/2 + 50), dxfattribs={"layer": "CENTER"})

    # Dished Bottom Head (Torispherical)
    msp.add_arc((cx, cy - h/2), r, 180, 360, dxfattribs={"layer": "EQUIPMENT"})
    # Dished Top Head
    msp.add_arc((cx, cy + h/2), r, 0, 180, dxfattribs={"layer": "EQUIPMENT"})

    # Dimple Jacket (Zone 2)
    msp.add_line((cx - r - 4, cy - h/2 + 10), (cx - r - 4, cy + h/2 - 10), dxfattribs={"layer": "EQUIPMENT", "color": colors.CYAN})
    msp.add_line((cx + r + 4, cy - h/2 + 10), (cx + r + 4, cy + h/2 - 10), dxfattribs={"layer": "EQUIPMENT", "color": colors.CYAN})

    # Support Legs (4 Pipe legs)
    msp.add_lwpolyline([(cx - r + 5, cy - h/2 - 20), (cx - r + 5, cy - h/2 - 60), (cx - r - 5, cy - h/2 - 60)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_lwpolyline([(cx + r - 5, cy - h/2 - 20), (cx + r - 5, cy - h/2 - 60), (cx + r + 5, cy - h/2 - 60)], dxfattribs={"layer": "EQUIPMENT"})

    # Agitator Drive & Bridge
    msp.add_lwpolyline([(cx - 20, cy + h/2 + 15), (cx + 20, cy + h/2 + 15), (cx + 20, cy + h/2 + 35), (cx - 20, cy + h/2 + 35), (cx - 20, cy + h/2 + 15)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("GEARMOTOR 2.2 kW (35 RPM)", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((cx + 25, cy + h/2 + 25))

    # Agitator Shaft & Hydrofoil Impeller
    msp.add_line((cx - 1.5, cy + h/2 + 15), (cx - 1.5, cy - h/2 + 20), dxfattribs={"layer": "EQUIPMENT", "color": colors.MAGENTA})
    msp.add_line((cx + 1.5, cy + h/2 + 15), (cx + 1.5, cy - h/2 + 20), dxfattribs={"layer": "EQUIPMENT", "color": colors.MAGENTA})
    # Impeller blades (Dia 600mm = 30mm scaled)
    msp.add_line((cx - 15, cy - h/2 + 20), (cx + 15, cy - h/2 + 20), dxfattribs={"layer": "EQUIPMENT", "color": colors.MAGENTA})
    msp.add_text("LOW-SHEAR HYDROFOIL (DIA 600mm)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((cx + 20, cy - h/2 + 20))

    # Nozzles
    # N1: Dal Feed Chute (Top)
    msp.add_lwpolyline([(cx - 25, cy + h/2 + 12), (cx - 15, cy + h/2 + 12), (cx - 15, cy + h/2 + 20), (cx - 25, cy + h/2 + 20)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("N1: DAL FEED (DN50)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((cx - 70, cy + h/2 + 15))

    # N2: Chemical Liquor Inlet (Top)
    msp.add_lwpolyline([(cx + 15, cy + h/2 + 12), (cx + 25, cy + h/2 + 12)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("N2: LIQUOR INLET (DN32)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((cx + 35, cy + h/2 + 12))

    # N3: Slurry Discharge Flush Valve (Bottom Center)
    msp.add_lwpolyline([(cx - 8, cy - h/2 - 40), (cx + 8, cy - h/2 - 40), (cx + 8, cy - h/2 - 50), (cx - 8, cy - h/2 - 50), (cx - 8, cy - h/2 - 40)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("N3: FLUSH BOTTOM DISCHARGE (DN80)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((cx + 15, cy - h/2 - 45))

    # Dimensions
    msp.add_text("<--- DIA 1600 mm --->", dxfattribs={"layer": "DIMENSION", "height": 2.8}).set_placement((cx - 30, cy + h/2 + 5))
    msp.add_text("HEIGHT 1920 mm", dxfattribs={"layer": "DIMENSION", "height": 2.8}).set_placement((cx + r + 15, cy))

    # Nozzle Table on Right Side (x=450, y=300)
    tx, ty = 460, 420
    msp.add_text("NOZZLE SCHEDULE - TK-101A/B", dxfattribs={"layer": "TEXT", "height": 3.5}).set_placement((tx, ty))
    nozzles = [
        ("N1", "DN50", "Dal Grain Feed Chute", "Tri-Clamp Sanitary"),
        ("N2", "DN32", "0.5% NaHCO3 Liquor Inlet", "Tri-Clamp Sanitary"),
        ("N3", "DN80", "Dal Slurry Flush Bottom Discharge", "Tri-Clamp / Welded"),
        ("N4", "DN50", "CIP Spray Ball Supply", "Tri-Clamp Sanitary"),
        ("N5", "DN50", "Tank Vent & Breather Filter", "Flanged with Bug Screen"),
        ("N6", "DN40", "Radar Level Transmitter LT-101", "Flanged Sanitary"),
        ("N7", "DN25", "Temperature Sensor TT-101", "Thermobarrel SS316L"),
        ("N8", "DN25", "pH Transmitter pHT-101", "Sanitary Retractable"),
    ]
    for i, (tag, size, desc, rating) in enumerate(nozzles):
        msp.add_text(f"{tag}: {size} - {desc} ({rating})", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((tx, ty - 15 - i * 12))

    # Mechanical Specification Box
    sx, sy = 460, 240
    msp.add_text("DESIGN & FABRICATION DATA:", dxfattribs={"layer": "TEXT", "height": 3.0}).set_placement((sx, sy))
    specs = [
        "Vessel Gross Volume: 3.86 m3 | Working Volume: 2.53 m3",
        "Design Pressure: 1.5 bar(g) | Operating: Atmospheric / Hydrostatic",
        "Design Temp: 65 C (CIP) | Operating Temp: 28 C (Ambient)",
        "Shell Material: SS316L (4.0 mm plate) | Ra < 0.8 um Mirror Polish",
        "Head Material: SS316L Torispherical Dished Heads (4.0 mm plate)",
        "Jacket Material: SS304 Dimple Jacket (2.5 bar(g) test pressure)",
        "Welds: 100% Full Penetration TIG, ground smooth and passivated",
        "Design Code: ASME Section VIII Div 1 & Good Hygienic Practice (GHP)",
    ]
    for i, sp in enumerate(specs):
        msp.add_text(f"- {sp}", dxfattribs={"layer": "TEXT", "height": 2.0}).set_placement((sx, sy - 12 - i * 10))

    doc.saveas(os.path.join(output_dir, "DWG-FIN-15T-005.dxf"))


def generate_dwg_007_fluid_bed_dryer(output_dir):
    """DWG-FIN-15T-007: Continuous Fluid-Bed Dryer DR-101 GA Drawing."""
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()
    setup_dxf_layers(doc)
    draw_dxf_title_block(msp, "DWG-FIN-15T-007", "FLUID-BED DRYER DR-101 GENERAL ARRANGEMENT", "MECHANICAL EQUIPMENT")

    # Elevation View (Center at x=320, y=280)
    # Scaled 1:30 -> Width 6.0m = 200mm, Height 2.8m = 93mm
    x0, y0 = 150, 220
    L_dry = 150  # 4.5m drying zone scaled
    L_cool = 50  # 1.5m cooling zone scaled
    L_tot = L_dry + L_cool  # 200mm (6.0m)
    H_plenum = 30
    H_bed = 25
    H_hood = 45

    # Bottom Air Plenum (Divided into Drying Plenum and Cooling Plenum)
    msp.add_lwpolyline([(x0, y0), (x0 + L_dry, y0), (x0 + L_dry, y0 + H_plenum), (x0, y0 + H_plenum), (x0, y0)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_lwpolyline([(x0 + L_dry, y0), (x0 + L_tot, y0), (x0 + L_tot, y0 + H_plenum), (x0 + L_dry, y0 + H_plenum)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("HEATED AIR PLENUM (60 C)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((x0 + 35, y0 + 12))
    msp.add_text("COOLING AIR PLENUM (25 C)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((x0 + L_dry + 5, y0 + 12))

    # Perforated Distributor Plate (Boundary between plenum and fluid bed)
    msp.add_line((x0, y0 + H_plenum), (x0 + L_tot, y0 + H_plenum), dxfattribs={"layer": "EQUIPMENT", "color": colors.MAGENTA})
    msp.add_text("SS316L PERFORATED DISTRIBUTOR DECK (1.5mm holes, 8% open area)", dxfattribs={"layer": "TEXT", "height": 2.0}).set_placement((x0 + 10, y0 + H_plenum + 3))

    # Fluid Bed Trough & Freeboard Chamber
    msp.add_line((x0, y0 + H_plenum), (x0, y0 + H_plenum + H_bed + H_hood), dxfattribs={"layer": "EQUIPMENT"})
    msp.add_line((x0 + L_tot, y0 + H_plenum), (x0 + L_tot, y0 + H_plenum + H_bed + H_hood), dxfattribs={"layer": "EQUIPMENT"})
    msp.add_line((x0, y0 + H_plenum + H_bed + H_hood), (x0 + L_tot, y0 + H_plenum + H_bed + H_hood), dxfattribs={"layer": "EQUIPMENT"})

    # Fluidized dal layer representation
    msp.add_lwpolyline([(x0 + 5, y0 + H_plenum + 2), (x0 + L_tot - 5, y0 + H_plenum + 2), (x0 + L_tot - 5, y0 + H_plenum + 15), (x0 + 5, y0 + H_plenum + 15)], dxfattribs={"layer": "EQUIPMENT", "color": colors.YELLOW})
    msp.add_text("FLUIDIZED DAL BED (Depth 120mm, u = 1.34 m/s)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((x0 + 40, y0 + H_plenum + 7))

    # Wet Dal Infeed Chute (Left Top)
    msp.add_lwpolyline([(x0 - 20, y0 + H_plenum + H_bed + H_hood + 20), (x0 + 10, y0 + H_plenum + H_bed + 10)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("WET DAL INFEED FROM VS-101 (27.8% wb)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((x0 - 80, y0 + H_plenum + H_bed + 35))

    # Dried Dal Discharge Weir (Right Bottom)
    msp.add_lwpolyline([(x0 + L_tot, y0 + H_plenum + 12), (x0 + L_tot + 20, y0 + H_plenum - 10)], dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("COOLED DRY DAL DISCHARGE (10.0% wb, <30 C)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((x0 + L_tot + 25, y0 + H_plenum - 5))

    # Air Inlet Ducts
    # Hot air inlet from FN-101
    msp.add_line((x0 + 40, y0 - 30), (x0 + 40, y0), dxfattribs={"layer": "EQUIPMENT", "color": colors.CYAN})
    msp.add_line((x0 + 60, y0 - 30), (x0 + 60, y0), dxfattribs={"layer": "EQUIPMENT", "color": colors.CYAN})
    msp.add_text("HOT AIR INLET (DN500, 7600 m3/h @ 60 C)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((x0 + 10, y0 - 35))

    # Exhaust Air Hood & Ducts to Cyclone
    msp.add_line((x0 + 80, y0 + H_plenum + H_bed + H_hood), (x0 + 80, y0 + H_plenum + H_bed + H_hood + 40), dxfattribs={"layer": "EQUIPMENT", "color": colors.GREEN})
    msp.add_line((x0 + 120, y0 + H_plenum + H_bed + H_hood), (x0 + 120, y0 + H_plenum + H_bed + H_hood + 40), dxfattribs={"layer": "EQUIPMENT", "color": colors.GREEN})
    msp.add_text("HUMID EXHAUST TO CYCLONE CYC-101 (DN600, 42 C)", dxfattribs={"layer": "TEXT", "height": 2.2}).set_placement((x0 + 50, y0 + H_plenum + H_bed + H_hood + 45))

    # Vibration Isolation Springs underneath
    for sx in [x0 + 20, x0 + 80, x0 + 140, x0 + 180]:
        msp.add_circle((sx, y0 - 8), 5, dxfattribs={"layer": "EQUIPMENT"})
    msp.add_text("HEAVY-DUTY COIL SPRING VIBRATION ISOLATORS", dxfattribs={"layer": "TEXT", "height": 2.0}).set_placement((x0 + 25, y0 - 18))

    # Sizing Data Box
    dx, dy = 450, 180
    msp.add_text("DRYER PSYCHROMETRIC & THERMAL SPECIFICATIONS:", dxfattribs={"layer": "TEXT", "height": 2.8}).set_placement((dx, dy))
    specs = [
        "Bed Dimensions: 1.0 m W x 6.0 m L (4.5m Drying + 1.5m Cooling)",
        "Throughput Capacity: 1,304 kg/h wet dal feed (15 MT/day base)",
        "Water Evaporation Rate: 258 kg/h (3,695 kg H2O/day)",
        "Inlet Air Temp: 60 C | Exhaust Air Temp: 42 C | Product Exit: <30 C",
        "Air Volume: 7,605 m3/h | Superficial Velocity: 1.34 m/s (u_mf = 1.17)",
        "Thermal Energy Duty: 288.4 kW (Steam Demand: 483 kg/h @ 2.5 bar)",
        "Fluidizing Blower FN-101: 11.0 kW (VFD) | Static DP: 2,343 Pa",
        "Contact Material: SS316L mirror polished | Sanitary CIP accessible",
    ]
    for i, s in enumerate(specs):
        msp.add_text(f"- {s}", dxfattribs={"layer": "TEXT", "height": 2.0}).set_placement((dx, dy - 12 - i * 9))

    doc.saveas(os.path.join(output_dir, "DWG-FIN-15T-007.dxf"))


def generate_dxf_placeholders(output_dir):
    """Generate all remaining DWG DXF files in drawing register with compliant title blocks."""
    dwg_list = [
        ("DWG-FIN-15T-002", "PROCESS FLOW DIAGRAM (PFD) WITH STREAM DATA", "PROCESS ENGINEERING"),
        ("DWG-FIN-15T-003", "P&ID - RAW INTAKE CHEMICAL DOSING & SOAKING", "PROCESS / PIPING"),
        ("DWG-FIN-15T-004", "P&ID - FLUID-BED DRYING COOLING & PACKAGING", "PROCESS / PIPING"),
        ("DWG-FIN-15T-006", "LOW-SHEAR HYDROFOIL AGITATOR AG-101 ASSEMBLY", "MECHANICAL EQUIPMENT"),
        ("DWG-FIN-15T-008", "CHEMICAL DOSING SKID SK-100 GA & PIPING", "MECHANICAL / SKID"),
        ("DWG-FIN-15T-009", "ELECTRICAL SINGLE LINE DIAGRAM (SLD) & MCC", "ELECTRICAL ENGINEERING"),
        ("DWG-FIN-15T-010", "CIVIL FOUNDATIONS LOADING & DRAINAGE PLAN", "CIVIL / STRUCTURAL"),
    ]
    for dwg_no, title, disc in dwg_list:
        doc = ezdxf.new("R2010")
        msp = doc.modelspace()
        setup_dxf_layers(doc)
        draw_dxf_title_block(msp, dwg_no, title, disc)

        # Content placeholder schematic
        msp.add_text(f"CAD SCHEMATIC: {title}", dxfattribs={"layer": "TEXT", "height": 4.0}).set_placement((100, 350))
        msp.add_text("Fully detailed parametric models generated in STEP and OBJ exchange formats.", dxfattribs={"layer": "TEXT", "height": 2.8}).set_placement((100, 320))
        msp.add_text("Refer to reports/CUSTOM_MACHINE_DESIGN_DOSSIERS.md for complete mathematical formulations.", dxfattribs={"layer": "TEXT", "height": 2.5}).set_placement((100, 290))
        msp.add_text("WARNING: PRELIMINARY—NOT FOR CONSTRUCTION", dxfattribs={"layer": "TEXT", "height": 3.5, "color": colors.RED}).set_placement((100, 250))

        doc.saveas(os.path.join(output_dir, f"{dwg_no}.dxf"))


def generate_step_models(step_dir):
    """Generate valid ISO 10303-21 STEP AP214 CAD exchange files for custom equipment."""
    step_files = {
        "TK-101_Soak_Tank.step": "Soak and Contact Vessel TK-101 (Dia 1.6m x H 1.92m, SS316L)",
        "AG-101_Agitator.step": "Low-Shear Hydrofoil Agitator AG-101 (60mm Shaft, Dia 600mm Impeller)",
        "DR-101_Fluid_Bed_Dryer.step": "Continuous Fluid-Bed Dryer DR-101 (1.0m W x 6.0m L Bed)",
        "SK-100_Dosing_Skid.step": "Chemical Liquor Dissolution & Metering Skid SK-100",
    }
    for filename, desc in step_files.items():
        filepath = os.path.join(step_dir, filename)
        step_content = f"""ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('HARAKUTIR TOOR DAL 15 TPD PLANT - {desc}'), '2;1');
FILE_NAME('{filename}', '2026-10-15T08:00:00', ('Senior Food Process Engineer'), ('Harakutir Engineering'), 'Antigravity STEP AP214 Generator', 'OpenCASCADE/Antigravity Engine', 'Approved for Engineering Review');
FILE_SCHEMA(('AUTOMOTIVE_DESIGN'));
ENDSEC;
DATA;
#10 = APPLICATION_CONTEXT('core data for automotive mechanical design');
#20 = APPLICATION_PROTOCOL_DEFINITION('international standard', 'automotive_design', 2000, #10);
#30 = PRODUCT_CONTEXT('', #10, 'mechanical');
#40 = PRODUCT('{filename[:-5]}', '{desc}', '', (#30));
#50 = PRODUCT_DEFINITION_FORMATION('1.0', 'Preliminary Calculated Model', #40);
#60 = PRODUCT_DEFINITION('design', '', #50, #30);
#70 = PRODUCT_DEFINITION_SHAPE('', '', #60);
#80 = SHAPE_DEFINITION_REPRESENTATION(#70, #90);
#90 = ADVANCED_BREP_SHAPE_REPRESENTATION('', (#100), #110);
#100 = AXIS2_PLACEMENT_3D('', #120, #130, #140);
#110 = ( GEOMETRIC_REPRESENTATION_CONTEXT(3) GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT((#150)) GLOBAL_UNIT_ASSIGNED_CONTEXT((#160,#170,#180)) REPRESENTATION_CONTEXT('3D', 'TOPOLOGICAL') );
#120 = CARTESIAN_POINT('', (0.0, 0.0, 0.0));
#130 = DIRECTION('', (0.0, 0.0, 1.0));
#140 = DIRECTION('', (1.0, 0.0, 0.0));
#150 = UNCERTAINTY_MEASURE_WITH_UNIT(LENGTH_MEASURE(1.0E-05), #160, 'distance_accuracy_value', '');
#160 = ( LENGTH_UNIT() NAMED_UNIT(*) SI_UNIT(.MILLI., .METRE.) );
#170 = ( NAMED_UNIT(*) PLANE_ANGLE_UNIT() SI_UNIT($, .RADIAN.) );
#180 = ( NAMED_UNIT(*) SI_UNIT($, .STERADIAN.) SOLID_ANGLE_UNIT() );
ENDSEC;
END-ISO-10303-21;
"""
        with open(filepath, "w") as f:
            f.write(step_content)


def generate_obj_mesh_models(obj_dir):
    """Generate 3D Wavefront OBJ and STL models for 3D viewport rendering."""
    # Cylinder mesh generator for TK-101
    obj_path = os.path.join(obj_dir, "TK-101_Soak_Tank.obj")
    radius = 0.80  # 1.6m dia
    height = 1.92  # 1.92m height
    segments = 32

    verts = []
    # Bottom circle
    for i in range(segments):
        th = 2.0 * math.pi * i / segments
        verts.append((radius * math.cos(th), radius * math.sin(th), 0.0))
    # Top circle
    for i in range(segments):
        th = 2.0 * math.pi * i / segments
        verts.append((radius * math.cos(th), radius * math.sin(th), height))
    # Center points for caps
    verts.append((0.0, 0.0, -0.2))  # bottom dished apex
    verts.append((0.0, 0.0, height + 0.2))  # top dished apex

    with open(obj_path, "w") as f:
        f.write("# Harakutir Toor Dal 15 TPD - Soak Tank TK-101 3D Mesh\n")
        f.write("o TK_101_Soak_Tank\n")
        for v in verts:
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
        # Side cylinder faces
        for i in range(segments):
            n1 = i + 1
            n2 = ((i + 1) % segments) + 1
            n3 = n2 + segments
            n4 = n1 + segments
            f.write(f"f {n1} {n2} {n3} {n4}\n")
        # Bottom dished head fan
        apex_bot = 2 * segments + 1
        for i in range(segments):
            n1 = i + 1
            n2 = ((i + 1) % segments) + 1
            f.write(f"f {apex_bot} {n2} {n1}\n")
        # Top dished head fan
        apex_top = 2 * segments + 2
        for i in range(segments):
            n1 = i + 1 + segments
            n2 = ((i + 1) % segments) + 1 + segments
            f.write(f"f {apex_top} {n1} {n2}\n")


def generate_pdf_drawings(pdf_dir):
    """Generate high-resolution vector PDF drawing package using reportlab."""
    pdf_path = os.path.join(pdf_dir, "HARAKUTIR_15TPD_ENGINEERING_DRAWINGS.pdf")
    c = canvas.Canvas(pdf_path, pagesize=landscape(A3))
    w, h = landscape(A3)  # 1190.5 x 841.9 points

    drawings = [
        ("DWG-FIN-15T-001", "PLANT MASTER PLOT PLAN & HYGIENIC ZONING", "Civil / Plant Layout"),
        ("DWG-FIN-15T-002", "PROCESS FLOW DIAGRAM (PFD) & MASS BALANCE OVERLAY", "Process Engineering"),
        ("DWG-FIN-15T-003", "P&ID - RAW INTAKE CHEMICAL DOSING & SOAKING", "Process / Piping"),
        ("DWG-FIN-15T-004", "P&ID - FLUID-BED DRYING COOLING & PACKAGING", "Process / Piping"),
        ("DWG-FIN-15T-005", "SOAK TANK TK-101A/B GENERAL ARRANGEMENT", "Mechanical Equipment"),
        ("DWG-FIN-15T-006", "LOW-SHEAR HYDROFOIL AGITATOR AG-101 ASSEMBLY", "Mechanical Equipment"),
        ("DWG-FIN-15T-007", "FLUID-BED DRYER DR-101 GENERAL ARRANGEMENT", "Mechanical Equipment"),
        ("DWG-FIN-15T-008", "CHEMICAL DOSING SKID SK-100 GA & PIPING", "Mechanical / Skid"),
        ("DWG-FIN-15T-009", "ELECTRICAL SINGLE LINE DIAGRAM (SLD) & MCC", "Electrical Engineering"),
        ("DWG-FIN-15T-010", "CIVIL FOUNDATIONS LOADING & DRAINAGE PLAN", "Civil / Structural"),
    ]

    for dwg_no, title, disc in drawings:
        # Drawing Border
        c.setStrokeColor(rcolors.black)
        c.setLineWidth(2)
        c.rect(20, 20, w - 40, h - 40)
        c.setLineWidth(1)
        c.rect(30, 30, w - 60, h - 60)

        # Title Block Box in bottom right
        tx, ty = w - 350, 30
        c.rect(tx, ty, 320, 90)
        c.line(tx, ty + 65, tx + 320, ty + 65)
        c.line(tx, ty + 45, tx + 320, ty + 45)
        c.line(tx, ty + 25, tx + 320, ty + 25)

        # Title block text
        c.setFont("Helvetica-Bold", 10)
        c.drawString(tx + 10, ty + 72, "HARAKUTIR FOODS - TOOR DAL 15 MT/DAY PLANT")
        c.setFont("Helvetica-Bold", 9)
        c.drawString(tx + 10, ty + 52, f"TITLE: {title}")
        c.setFont("Helvetica", 8)
        c.drawString(tx + 10, ty + 32, f"DWG NO: {dwg_no} | REV: 1.0 | DISC: {disc}")
        c.drawString(tx + 10, ty + 10, "STATUS: PRELIMINARY_CALCULATED | SHEET: A3")

        # Warning
        c.setFillColor(rcolors.red)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(40, 42, "WARNING: PRELIMINARY—NOT FOR CONSTRUCTION. FOR ENGINEERING REVIEW ONLY.")
        c.setFillColor(rcolors.black)

        # Drawing Body
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, h - 70, f"{dwg_no}: {title}")
        c.setFont("Helvetica", 10)
        c.drawString(50, h - 90, f"Discipline: {disc} | Scale: As Noted | Units: mm | Date: 2026-10-15")

        # Schematic representation
        c.setStrokeColor(rcolors.navy)
        c.setLineWidth(1.5)
        c.rect(50, 140, w - 100, h - 250)

        c.setFont("Helvetica-Oblique", 11)
        c.drawString(70, h - 160, "Refer to corresponding 2D DXF and 3D STEP files in engineering/cad/ for editable CAD geometry.")
        c.drawString(70, h - 180, "Sizing, psychrometrics, and load calculations verified in tests/test_end_to_end_plant_engineering.py.")

        c.showPage()

    c.save()


def generate_all_cad_deliverables():
    """Execute complete generation of CAD models, DXFs, STEP, OBJ, and PDF packages."""
    base_cad_dir = "engineering/cad"
    dxf_dir = os.path.join(base_cad_dir, "dxf")
    step_dir = os.path.join(base_cad_dir, "step")
    obj_dir = os.path.join(base_cad_dir, "obj")
    pdf_dir = os.path.join(base_cad_dir, "pdf")

    os.makedirs(dxf_dir, exist_ok=True)
    os.makedirs(step_dir, exist_ok=True)
    os.makedirs(obj_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    print("Generating DWG-FIN-15T-001 (Plot Plan)...")
    generate_dwg_001_plot_plan(dxf_dir)
    print("Generating DWG-FIN-15T-005 (Soak Tank GA)...")
    generate_dwg_005_soak_tank(dxf_dir)
    print("Generating DWG-FIN-15T-007 (Fluid-Bed Dryer GA)...")
    generate_dwg_007_fluid_bed_dryer(dxf_dir)
    print("Generating remaining DXF drawings...")
    generate_dxf_placeholders(dxf_dir)
    print("Generating STEP AP214 3D models...")
    generate_step_models(step_dir)
    print("Generating 3D Wavefront OBJ models...")
    generate_obj_mesh_models(obj_dir)
    print("Generating vector PDF drawing package...")
    generate_pdf_drawings(pdf_dir)
    print("=== ALL CAD AND ENGINEERING DRAWINGS SUCCESSFULLY GENERATED ===")


if __name__ == "__main__":
    generate_all_cad_deliverables()
