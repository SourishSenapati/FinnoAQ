"""
V4 Master Complete Conceptual FEED Drawing Package Generator (Sheets 1 to 12).
Governing Directive: V4 MASTER DIRECTIVE — PROFESSIONAL NATIVE ENGINEERING, OFFLINE-FIRST, EVIDENCE-LOCKED.

Produces the full 12-sheet conceptual FEED package in AutoCAD R2018 DXF and high-resolution vector PDF:
- Sheet 01: DWG-FIN-15T-001 - Process Flow Diagram (PFD)
- Sheet 02: DWG-FIN-15T-002 - Process Stream Table & Balance Schedule
- Sheet 03: DWG-FIN-15T-003 - P&ID: Soaking Battery & Chemical Dosing
- Sheet 04: DWG-FIN-15T-004 - Site Master Plot Plan & Hygienic Zoning
- Sheet 05: DWG-FIN-15T-005 - P&ID: Fluid Bed Dryer & Air Handling System
- Sheet 06: DWG-FIN-15T-006 - P&ID: Secondary Packaging & Cleanroom Dedusting
- Sheet 07: DWG-FIN-15T-007 - Equipment GA: Dal Soaking Vessel TK-101
- Sheet 08: DWG-FIN-15T-008 - Equipment GA: Continuous Fluid Bed Dryer DR-101
- Sheet 09: DWG-FIN-15T-009 - Equipment GA: Chemical Dosing Skid SK-100
- Sheet 10: DWG-FIN-15T-010 - P&ID: Triple-Effect ZLD Wastewater Evaporator EV-101A/B/C
- Sheet 11: DWG-FIN-15T-011 - Electrical Single-Line Diagram & 415V MCC Distribution
- Sheet 12: DWG-FIN-15T-012 - Hazardous Area Classification & Combustible Dust Zoning

All drawings use metric coordinates, standard engineering layers, authentic symbology,
and ColorPolicy.COLOR_SWAP_BW for crisp, high-density, professional CAD output.
"""

import os
import sys
import math
import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.config import Configuration, ColorPolicy
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import matplotlib.pyplot as plt
import fitz # PyMuPDF

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scripts"))

try:
    from scripts.build_v4_cad_exemplars import (
        SHEET_W, SHEET_H, MARGIN,
        setup_cad_document,
        draw_sheet_border_and_title_block,
        draw_isa_bubble,
        draw_valve,
        draw_arrow,
        draw_stream_flag,
        export_dxf_and_pdf,
        build_exemplar_1_pfd,
        build_exemplar_1b_stream_table,
        build_exemplar_2_pid,
        build_exemplar_3_plot_plan,
        build_exemplar_4_soak_tank_ga,
    )
except ImportError:
    from build_v4_cad_exemplars import (
        SHEET_W, SHEET_H, MARGIN,
        setup_cad_document,
        draw_sheet_border_and_title_block,
        draw_isa_bubble,
        draw_valve,
        draw_arrow,
        draw_stream_flag,
        export_dxf_and_pdf,
        build_exemplar_1_pfd,
        build_exemplar_1b_stream_table,
        build_exemplar_2_pid,
        build_exemplar_3_plot_plan,
        build_exemplar_4_soak_tank_ga,
    )

TOTAL_SHEETS = 12

# =============================================================================
# SHEET 05: P&ID - Continuous Vibrating Fluid Bed Dryer & Air Handling System
# =============================================================================
def build_sheet_05_pid_dryer():
    print("Generating Sheet 05: P&ID Fluid Bed Dryer DR-101 (DWG-FIN-15T-005)...")
    doc = setup_cad_document()
    msp = doc.modelspace()
    draw_sheet_border_and_title_block(msp, "DWG-FIN-15T-005", "P&ID - FLUID BED DRYER & AIR SYSTEM", 5, TOTAL_SHEETS, "PIPING")

    # 1. Continuous Fluid Bed Dryer DR-101 (Center: X = 150 to 380, Y = 180 to 250)
    dr_x, dr_y = 170.0, 190.0
    dr_w, dr_h = 190.0, 50.0

    # Upper Expansion Hood
    msp.add_lwpolyline([(dr_x, dr_y + 20), (dr_x + dr_w, dr_y + 20), (dr_x + dr_w - 10, dr_y + dr_h), (dr_x + 10, dr_y + dr_h), (dr_x, dr_y + 20)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 50})
    # Lower Air Plenum
    msp.add_lwpolyline([(dr_x, dr_y + 20), (dr_x + dr_w, dr_y + 20), (dr_x + dr_w - 5, dr_y), (dr_x + 5, dr_y), (dr_x, dr_y + 20)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 50})
    # Perforated Distributor Deck (Dashed Line)
    msp.add_line((dr_x, dr_y + 20), (dr_x + dr_w, dr_y + 20), dxfattribs={'layer': 'EQUIPMENT', 'linetype': 'DASHED', 'lineweight': 35})
    
    msp.add_text("CONTINUOUS VIBRATING FLUID BED DRYER DR-101", height=2.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((dr_x + 25, dr_y + dr_h + 5))
    msp.add_text("DECK AREA: 14.0 m2 (14.0m L x 1.0m W) | SS304 PERFORATED PLATE", height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((dr_x + 20, dr_y + dr_h + 1))
    
    # Vibration Springs & Exciter Motors M-101A/B
    for sp_x in [dr_x + 15, dr_x + 65, dr_x + 125, dr_x + 175]:
        msp.add_lwpolyline([(sp_x - 4, dr_y), (sp_x + 4, dr_y), (sp_x, dr_y - 12), (sp_x - 4, dr_y)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
        msp.add_lwpolyline([(sp_x - 7, dr_y - 12), (sp_x + 7, dr_y - 12), (sp_x + 7, dr_y - 15), (sp_x - 7, dr_y - 15), (sp_x - 7, dr_y - 12)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
    # Unbalance Motors
    msp.add_circle((dr_x + 85, dr_y - 6), 6.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_circle((dr_x + 105, dr_y - 6), 6.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("M-101A/B (2x3.0kW)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((dr_x + 75, dr_y - 18))

    # Product Infeed Chute (from SC-101)
    msp.add_line((dr_x - 30, dr_y + 60), (dr_x + 10, dr_y + 25), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 50})
    msp.add_line((dr_x - 25, dr_y + 65), (dr_x + 15, dr_y + 30), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 50})
    draw_arrow(msp, dr_x - 10, dr_y + 44, 'RIGHT')
    msp.add_text("MOIST DAL INFEED (1,334 kg/h @ 37% wb)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((dr_x - 65, dr_y + 55))
    draw_valve(msp, dr_x - 5, dr_y + 40, vtype='ROTARY', tag='RV-102')

    # Product Discharge Chute & Rotary Airlock RV-103
    msp.add_line((dr_x + dr_w - 5, dr_y + 20), (dr_x + dr_w + 15, dr_y - 15), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 50})
    msp.add_line((dr_x + dr_w, dr_y + 15), (dr_x + dr_w + 20, dr_y - 20), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 50})
    draw_valve(msp, dr_x + dr_w + 10, dr_y - 8, vtype='ROTARY', tag='RV-103')
    draw_arrow(msp, dr_x + dr_w + 18, dr_y - 22, 'DOWN')
    msp.add_text("DRIED TENDER DAL TO PACKAGING", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((dr_x + dr_w - 10, dr_y - 28))
    msp.add_text("926.9 kg/h @ 10.0% wb", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((dr_x + dr_w - 10, dr_y - 33))

    # 2. Fresh Air Intake, Blower BL-101, and Steam Heater HE-101 (Left: X = 30 to 140, Y = 60 to 160)
    # Air Intake Filter AF-101
    msp.add_lwpolyline([(35, 115), (50, 115), (50, 145), (35, 145), (35, 115)], dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_line((35, 115), (50, 145), dxfattribs={'layer': 'EQUIPMENT', 'linetype': 'DASHED'})
    msp.add_text("AIR FILTER AF-101", height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((28, 150))
    msp.add_text("EU-7 / F7 GRADE", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((30, 108))

    # Fluidizing Air Blower BL-101
    msp.add_circle((75, 130), 12.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_line((50, 130), (63, 130), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_text("BL-101", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((70, 128))
    msp.add_text("55.0 kW (VFD)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((66, 112))
    
    # Steam Air Heater HE-101 (Finned Tube Heat Exchanger)
    msp.add_lwpolyline([(105, 110), (135, 110), (135, 150), (105, 150), (105, 110)], dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_line((75 + 12, 130), (105, 130), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    # Steam Coil zig-zag
    for z in range(3):
        msp.add_line((112 + z * 8, 115), (116 + z * 8, 145), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
    msp.add_text("STEAM HEATER HE-101", height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((102, 154))
    msp.add_text("512.4 kWth (785 kg/h Steam)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((100, 104))

    # Steam Supply Line (3.5 bar g) & Modulating Control Valve TCV-201
    msp.add_line((120, 175), (120, 150), dxfattribs={'layer': 'UTILITY_PIPING', 'lineweight': 35})
    draw_valve(msp, 120, 162, vtype='CONTROL', fail_pos='FC', tag='TCV-201', horizontal=False)
    msp.add_text("3\"-STM-201 (3.5 bar g)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((90, 172))

    # Condensate Return Line & Steam Trap ST-201
    msp.add_line((120, 110), (120, 85), dxfattribs={'layer': 'UTILITY_PIPING', 'lineweight': 35})
    msp.add_circle((120, 95), 4.0, dxfattribs={'layer': 'EQUIPMENT'})
    msp.add_text("ST-201", height=1.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((125, 95))
    msp.add_text("CONDENSATE RETURN", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((95, 80))

    # Hot Air Supply Duct from HE-101 to DR-101 Plenum
    msp.add_line((135, 130), (dr_x + 40, 130), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((dr_x + 40, 130), (dr_x + 40, dr_y + 5), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    draw_arrow(msp, dr_x + 40, dr_y - 5, 'UP')
    msp.add_text("HOT DRYING AIR (14,150 kg/h @ 85 deg C)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((145, 133))

    # 3. Exhaust Air Handling: Cyclone CY-101, Baghouse BF-102 & ID Fan BL-102 (Right: X = 410 to 560, Y = 130 to 320)
    # Exhaust Duct from Dryer Hood to Cyclone
    msp.add_line((dr_x + dr_w - 30, dr_y + dr_h), (dr_x + dr_w - 30, 280), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((dr_x + dr_w - 30, 280), (425, 280), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    draw_arrow(msp, 415, 280, 'RIGHT')
    msp.add_text("HUMID EXHAUST AIR @ 52 deg C", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((355, 284))

    # Cyclone Separator CY-101
    cy_x, cy_y = 440.0, 260.0
    msp.add_lwpolyline([(cy_x - 12, cy_y + 30), (cy_x + 12, cy_y + 30), (cy_x + 12, cy_y + 10), (cy_x + 4, cy_y - 15), (cy_x - 4, cy_y - 15), (cy_x - 12, cy_y + 10), (cy_x - 12, cy_y + 30)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_text("CYCLONE CY-101", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cy_x - 18, cy_y + 35))
    # Cyclone Rotary Valve RV-104
    draw_valve(msp, cy_x, cy_y - 20, vtype='ROTARY', tag='RV-104', horizontal=False)
    msp.add_text("RECOVERED FINES (1.5 kg/h)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cy_x - 15, cy_y - 32))

    # Secondary Baghouse Dust Collector BF-102
    bf_x, bf_y = 485.0, 255.0
    msp.add_line((cy_x, cy_y + 30), (cy_x, cy_y + 40), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    msp.add_line((cy_x, cy_y + 40), (bf_x - 15, cy_y + 40), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    msp.add_line((bf_x - 15, cy_y + 40), (bf_x - 15, bf_y + 20), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    draw_arrow(msp, bf_x - 15, bf_y + 25, 'DOWN')

    msp.add_lwpolyline([(bf_x - 15, bf_y + 35), (bf_x + 15, bf_y + 35), (bf_x + 15, bf_y), (bf_x + 5, bf_y - 18), (bf_x - 5, bf_y - 18), (bf_x - 15, bf_y), (bf_x - 15, bf_y + 35)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_text("BAG FILTER BF-102", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((bf_x - 18, bf_y + 40))
    msp.add_text("PULSE-JET CLEANED", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((bf_x - 16, bf_y + 25))

    # Induced Draft Fan BL-102 & Exhaust Stack ST-101
    msp.add_line((bf_x, bf_y + 35), (bf_x, bf_y + 50), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    msp.add_line((bf_x, bf_y + 50), (535, bf_y + 50), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    
    # Fan BL-102
    msp.add_circle((535, bf_y + 50), 10.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("BL-102 (30kW)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((522, bf_y + 36))
    
    # Stack ST-101 venting up
    msp.add_line((535 + 10, bf_y + 50), (555, bf_y + 50), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    msp.add_line((555, bf_y + 50), (555, 360), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    draw_arrow(msp, 555, 355, 'UP')
    msp.add_text("EXHAUST STACK ST-101 (15m AGL)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((495, 365))

    # 4. ISA-5.1 Control Loops & Instrumentation
    # Bed Temperature Transmitters along the dryer
    draw_isa_bubble(msp, dr_x + 35, dr_y + 70, "TIT", "201", lead_to=(dr_x + 35, dr_y + 22))
    draw_isa_bubble(msp, dr_x + 95, dr_y + 70, "TIT", "202", lead_to=(dr_x + 95, dr_y + 22))
    draw_isa_bubble(msp, dr_x + 155, dr_y + 70, "TIT", "203", lead_to=(dr_x + 155, dr_y + 22))
    
    # Hot Air Inlet Temperature & Pressure
    draw_isa_bubble(msp, 120, 195, "TIC", "201", lead_to=(120, 166))
    draw_isa_bubble(msp, 160, 150, "PIT", "201", lead_to=(160, 130))
    draw_isa_bubble(msp, 180, 150, "FIT", "201", lead_to=(180, 130))

    # Differential Pressure Transmitter across Baghouse
    draw_isa_bubble(msp, bf_x + 25, bf_y + 15, "PDIT", "202", lead_to=(bf_x + 15, bf_y + 15))

    # 5. Interlock & Control Philosophy Schedule (Bottom Left-Center)
    cx0, cy0 = 35.0, 75.0
    msp.add_lwpolyline([(cx0, cy0), (cx0 + 260, cy0), (cx0 + 260, cy0 - 45), (cx0, cy0 - 45), (cx0, cy0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
    msp.add_text("DRYER CONTROL PHILOSOPHY & SAFETY INTERLOCK MATRIX (ISA-84 / SIL-1):", height=2.2,
                 dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx0 + 4, cy0 - 7))
    msp.add_line((cx0, cy0 - 10), (cx0 + 260, cy0 - 10), dxfattribs={'layer': 'BORDER_TITLE'})
    d_notes = [
        "1. TIC-201: Modulates 3\" steam valve TCV-201 to maintain fluidizing inlet air at 85 deg C +/- 1.5 deg C.",
        "2. I-02 Interlock: Low airflow (FIT-201 < 10,000 kg/h) or Blower BL-101 trip immediately closes steam valve TCV-201.",
        "3. I-03 Interlock: High-High bed temperature (TIT-202 > 95 deg C) trips infeed rotary valve RV-102 and alerts operator.",
        "4. PDIT-202: Differential pressure across baghouse triggers sequential reverse pulse-jet cleaning @ 5.0 bar g air.",
        "5. Vibration Interlock: High vibration switch VSH-101 trips exciter motors M-101A/B upon mechanical resonance.",
    ]
    for idx, txt in enumerate(d_notes):
        msp.add_text(txt, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx0 + 4, cy0 - 17 - idx * 7.0))

    dxf_out = os.path.abspath("engineering/cad/dxf/DWG-FIN-15T-005.dxf")
    pdf_out = os.path.abspath("engineering/cad/pdf/DWG-FIN-15T-005_PID_DRYER.pdf")
    export_dxf_and_pdf(doc, dxf_out, pdf_out)


# =============================================================================
# SHEET 06: P&ID - Secondary Packaging & Cleanroom Dedusting
# =============================================================================
def build_sheet_06_pid_packaging():
    print("Generating Sheet 06: P&ID Packaging Line PK-101 (DWG-FIN-15T-006)...")
    doc = setup_cad_document()
    msp = doc.modelspace()
    draw_sheet_border_and_title_block(msp, "DWG-FIN-15T-006", "P&ID - PACKAGING LINE & CLEANROOM DEDUSTING", 6, TOTAL_SHEETS, "PIPING")

    # 1. Product Infeed Conveyor & Dedusting Vibrating Screen SC-102 (Left: X = 35 to 130, Y = 200 to 320)
    # Bucket Elevator / Z-Conveyor CV-103
    msp.add_line((40, 220), (80, 290), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_line((45, 215), (85, 285), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("CV-103 Z-CONVEYOR", height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((35, 300))
    draw_arrow(msp, 70, 275, 'RIGHT')

    # Dedusting Screen SC-102
    sc_x, sc_y = 110.0, 270.0
    msp.add_lwpolyline([(sc_x - 18, sc_y + 12), (sc_x + 18, sc_y), (sc_x + 18, sc_y - 12), (sc_x - 18, sc_y), (sc_x - 18, sc_y + 12)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_text("DEDUSTING SCREEN SC-102", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((sc_x - 22, sc_y + 18))
    msp.add_text("FINES REMOVAL (1.5mm MESH)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((sc_x - 20, sc_y - 18))

    # 2. Storage Surge Hopper BH-101 (Center-Left: X = 150 to 220, Y = 180 to 290)
    bh_x, bh_y = 180.0, 230.0
    msp.add_line((sc_x + 18, sc_y), (bh_x, sc_y), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((bh_x, sc_y), (bh_x, bh_y + 40), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    draw_arrow(msp, bh_x, bh_y + 45, 'DOWN')

    msp.add_lwpolyline([(bh_x - 16, bh_y + 40), (bh_x + 16, bh_y + 40), (bh_x + 16, bh_y + 10), (bh_x - 16, bh_y + 10), (bh_x - 16, bh_y + 40)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_lwpolyline([(bh_x - 16, bh_y + 10), (bh_x + 16, bh_y + 10), (bh_x + 5, bh_y - 10), (bh_x - 5, bh_y - 10), (bh_x - 16, bh_y + 10)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_text("SURGE HOPPER BH-101", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((bh_x - 22, bh_y + 45))
    msp.add_text("CAPACITY: 2,500 kg (SS304)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((bh_x - 20, bh_y + 22))

    # Level Instrumentation on Hopper
    draw_isa_bubble(msp, bh_x - 28, bh_y + 30, "LSH", "301", lead_to=(bh_x - 16, bh_y + 30))
    draw_isa_bubble(msp, bh_x - 28, bh_y + 15, "LSL", "301", lead_to=(bh_x - 16, bh_y + 15))
    draw_valve(msp, bh_x, bh_y - 20, vtype='ROTARY', tag='RV-301', horizontal=False)

    # 3. Form-Fill-Seal Packaging Machine PK-101 (Center: X = 240 to 350, Y = 130 to 250)
    pk_x, pk_y = 290.0, 180.0
    msp.add_line((bh_x, bh_y - 28), (bh_x, bh_y - 38), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((bh_x, bh_y - 38), (pk_x, bh_y - 38), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((pk_x, bh_y - 38), (pk_x, pk_y + 35), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    draw_arrow(msp, pk_x, pk_y + 40, 'DOWN')

    msp.add_lwpolyline([(pk_x - 25, pk_y + 35), (pk_x + 25, pk_y + 35), (pk_x + 25, pk_y - 25), (pk_x - 25, pk_y - 25), (pk_x - 25, pk_y + 35)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 50})
    msp.add_text("PACKAGING MACHINE PK-101", height=2.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((pk_x - 26, pk_y + 40))
    msp.add_text("DUAL LINE: 5 kg POUCH & 30 kg BULK", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((pk_x - 24, pk_y + 15))
    msp.add_text("NITROGEN FLUSH SYSTEM", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((pk_x - 20, pk_y + 5))
    msp.add_text("RATE: 926.9 kg/h", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((pk_x - 16, pk_y - 12))

    # 4. In-line Metal Detector MD-301 & Dynamic Checkweigher CW-301 (Right: X = 370 to 520, Y = 130 to 220)
    # Belt Conveyor out of packaging
    msp.add_line((pk_x + 25, pk_y - 15), (510, pk_y - 15), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_line((pk_x + 25, pk_y - 20), (510, pk_y - 20), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    draw_arrow(msp, pk_x + 45, pk_y - 17, 'RIGHT')

    # Metal Detector MD-301
    md_x = 380.0
    msp.add_lwpolyline([(md_x - 10, pk_y - 5), (md_x + 10, pk_y - 5), (md_x + 10, pk_y - 30), (md_x - 10, pk_y - 30), (md_x - 10, pk_y - 5)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("METAL DETECTOR", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((md_x - 15, pk_y + 2))
    msp.add_text("MD-301 (Fe/Non-Fe/SS)", height=1.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((md_x - 16, pk_y - 38))
    draw_isa_bubble(msp, md_x, pk_y + 18, "XI", "301", lead_to=(md_x, pk_y - 5))

    # Reject Station Flap XV-302
    draw_valve(msp, md_x + 25, pk_y - 17, vtype='GATE', fail_pos='FC', tag='XV-302')
    msp.add_text("REJECT DUMP", height=1.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((md_x + 18, pk_y - 28))

    # Checkweigher CW-301
    cw_x = 450.0
    msp.add_lwpolyline([(cw_x - 12, pk_y - 5), (cw_x + 12, pk_y - 5), (cw_x + 12, pk_y - 30), (cw_x - 12, pk_y - 30), (cw_x - 12, pk_y - 5)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("CHECKWEIGHER", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cw_x - 14, pk_y + 2))
    msp.add_text("CW-301 (+/- 2g)", height=1.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cw_x - 14, pk_y - 38))
    draw_isa_bubble(msp, cw_x, pk_y + 18, "WIC", "302", lead_to=(cw_x, pk_y - 5))

    # To Palletizing & Finished Goods Warehouse
    draw_arrow(msp, 505, pk_y - 17, 'RIGHT')
    msp.add_text("TO PALLETIZER & WAREHOUSE", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((475, pk_y - 5))

    # 5. Cleanroom Dedusting HVAC & Bag Filter BF-101 (Top-Right: X = 330 to 480, Y = 270 to 360)
    bf1_x, bf1_y = 390.0, 310.0
    msp.add_lwpolyline([(bf1_x - 14, bf1_y + 25), (bf1_x + 14, bf1_y + 25), (bf1_x + 14, bf1_y), (bf1_x + 5, bf1_y - 15), (bf1_x - 5, bf1_y - 15), (bf1_x - 14, bf1_y), (bf1_x - 14, bf1_y + 25)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_text("CLEANROOM DUST COLLECTOR BF-101", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((bf1_x - 28, bf1_y + 30))
    msp.add_text("HEPA H-13 POLICING FILTER", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((bf1_x - 22, bf1_y + 10))

    # Cleanroom Overpressure Monitoring (+15 Pa)
    draw_isa_bubble(msp, 270, 320, "PDIT", "303")
    msp.add_text("ROOM OVERPRESSURE: +15 Pa (ISO CLASS 8)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((230, 335))

    # Quality & CCP Summary Schedule
    cx0, cy0 = 35.0, 140.0
    msp.add_lwpolyline([(cx0, cy0), (cx0 + 200, cy0), (cx0 + 200, cy0 - 55), (cx0, cy0 - 55), (cx0, cy0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
    msp.add_text("PACKAGING HACCP CRITICAL CONTROL POINTS (CCP-1 & CCP-2):", height=2.2,
                 dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx0 + 4, cy0 - 7))
    msp.add_line((cx0, cy0 - 10), (cx0 + 200, cy0 - 10), dxfattribs={'layer': 'BORDER_TITLE'})
    p_notes = [
        "1. CCP-1 (Metal Detection): MD-301 tested every 2h with test wands (1.5mm Fe, 2.0mm Non-Fe, 2.5mm SS).",
        "2. Any metal detection immediately triggers pneumatic reject flap XV-302 and alarms packaging operator.",
        "3. CCP-2 (Moisture Verification): Final packaged product moisture locked @ 10.0% +/- 0.5% wet-basis.",
        "4. Nitrogen Gas Flush: Residual headspace oxygen < 2.0% to guarantee 12-month shelf life without oxidation.",
        "5. ISO Class 8 Cleanroom: Differential pressure > +15 Pa maintained against raw warehouse to prevent cross-contamination.",
    ]
    for idx, txt in enumerate(p_notes):
        msp.add_text(txt, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx0 + 4, cy0 - 17 - idx * 7.5))

    dxf_out = os.path.abspath("engineering/cad/dxf/DWG-FIN-15T-006.dxf")
    pdf_out = os.path.abspath("engineering/cad/pdf/DWG-FIN-15T-006_PID_PACKAGING.pdf")
    export_dxf_and_pdf(doc, dxf_out, pdf_out)


# =============================================================================
# SHEET 08: Equipment GA - Continuous Vibrating Fluid Bed Dryer DR-101
# =============================================================================
def build_sheet_08_dryer_ga():
    print("Generating Sheet 08: Equipment GA Fluid Bed Dryer DR-101 (DWG-FIN-15T-008)...")
    doc = setup_cad_document()
    msp = doc.modelspace()
    draw_sheet_border_and_title_block(msp, "DWG-FIN-15T-008", "EQUIPMENT GENERAL ARRANGEMENT - FLUID BED DRYER DR-101", 8, TOTAL_SHEETS, "MECHANICAL")

    # Front Elevation View (Centered: X = 190, Y = 260)
    # Scale: 1:50 (14,000 mm -> 280 mm on drawing, 2,800 mm H -> 56 mm on drawing)
    s = 1.0 / 50.0
    vx, vy = 40.0, 240.0
    dw, dh = 14000.0 * s, 2800.0 * s # 280.0 mm x 56.0 mm

    # Base Skid & 8 Coil Springs
    msp.add_lwpolyline([(vx, vy), (vx + dw, vy), (vx + dw, vy - 10), (vx, vy - 10), (vx, vy)], dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    for i in range(8):
        sx = vx + 15 + i * 36
        msp.add_lwpolyline([(sx - 4, vy), (sx + 4, vy), (sx, vy - 8), (sx - 4, vy)], dxfattribs={'layer': 'EQUIPMENT'})
    msp.add_text("8x HEAVY DUTY COIL SPRING VIBRATION ISOLATORS (>96% EFFICIENCY)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((vx + 40, vy - 16))

    # Lower Fluidizing Air Plenum (Tapered bottom)
    msp.add_lwpolyline([(vx, vy + 22), (vx + dw, vy + 22), (vx + dw - 10, vy + 4), (vx + 10, vy + 4), (vx, vy + 22)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    # Dual Hot Air Inlet Nozzles N2A/B (DN600)
    for in_x in [vx + 60, vx + 180]:
        msp.add_lwpolyline([(in_x - 8, vy + 4), (in_x + 8, vy + 4), (in_x + 8, vy - 6), (in_x - 8, vy - 6), (in_x - 8, vy + 4)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
        msp.add_text("N2 (DN600 AIR INLET)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((in_x - 14, vy - 10))

    # Perforated Deck Level (3mm SS304 Perforated Sheet)
    msp.add_line((vx, vy + 22), (vx + dw, vy + 22), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 50, 'linetype': 'DASHED'})
    msp.add_text("FLUIDIZING DECK ELEVATION (+1,100 mm AGL)", height=1.8, dxfattribs={'layer': 'DIMENSIONS'}).set_placement((vx + dw + 5, vy + 22))

    # Upper Disengagement Hood (Expanded cross-section)
    msp.add_lwpolyline([(vx, vy + 22), (vx + dw, vy + 22), (vx + dw - 15, vy + dh), (vx + 15, vy + dh), (vx, vy + 22)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 50})
    
    # Three Exhaust Air Outlets N3A/B/C (DN500)
    for ex_idx, ex_x in enumerate([vx + 50, vx + 140, vx + 230]):
        msp.add_lwpolyline([(ex_x - 6, vy + dh), (ex_x + 6, vy + dh), (ex_x + 6, vy + dh + 10), (ex_x - 6, vy + dh + 10), (ex_x - 6, vy + dh)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
        msp.add_text(f"N3{chr(ord('A') + ex_idx)} (DN500)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((ex_x - 8, vy + dh + 13))

    # Infeed Chute N1 and Discharge Chute N4
    msp.add_lwpolyline([(vx + 5, vy + dh), (vx + 5, vy + dh + 14), (vx + 18, vy + dh + 14), (vx + 18, vy + dh), (vx + 5, vy + dh)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("N1 INFEED", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((vx - 2, vy + dh + 17))

    msp.add_lwpolyline([(vx + dw - 15, vy + 22), (vx + dw, vy + 5), (vx + dw + 10, vy + 5), (vx + dw - 5, vy + 22)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("N4 DISCHARGE", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((vx + dw + 2, vy + 12))

    # Twin Unbalance Exciter Motors M-101A/B (2 x 3.0 kW @ 45 deg thrust angle)
    msp.add_circle((vx + 130, vy + 8), 7.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_circle((vx + 150, vy + 8), 7.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_line((vx + 125, vy + 3), (vx + 155, vy + 13), dxfattribs={'layer': 'EQUIPMENT', 'linetype': 'DASHDOT'})
    msp.add_text("TWIN UNBALANCE MOTORS (45 DEG DRIVE)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((vx + 110, vy + 28))

    # Overall Dimensions Callouts
    msp.add_text("14,000 mm OVERALL DRYER LENGTH", height=2.5, dxfattribs={'layer': 'DIMENSIONS'}).set_placement((vx + 80, vy - 26))
    msp.add_text("2,800 mm OVERALL HEIGHT", height=2.5, dxfattribs={'layer': 'DIMENSIONS'}).set_placement((vx - 28, vy + 25))

    # -------------------------------------------------------------------------
    # Lower Section: Nozzle Schedule Table & Mechanical Specification Table
    # -------------------------------------------------------------------------
    # Nozzle Schedule (X = 35 to 280, Y = 70 to 180)
    tx0, ty0 = 35.0, 180.0
    col_w = [18, 45, 25, 30, 45, 60]
    n_headers = ["MARK", "SERVICE", "SIZE", "RATING", "FACING", "LOCATION"]
    cur_x = tx0
    for w, h_text in zip(col_w, n_headers):
        msp.add_lwpolyline([(cur_x, ty0), (cur_x + w, ty0), (cur_x + w, ty0 - 11), (cur_x, ty0 - 11), (cur_x, ty0)],
                           dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
        msp.add_text(h_text, height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cur_x + 2, ty0 - 8))
        cur_x += w
    
    n_rows = [
        ("N1", "Moist Dal Infeed", "400x300", "FLANGED", "FLAT FACE", "Top Hood Infeed End"),
        ("N2A/B", "Hot Air Supply", "2x DN600", "150#", "RAISED FACE", "Bottom Plenum Underside"),
        ("N3A-C", "Exhaust Air Outlets", "3x DN500", "150#", "FLAT FACE", "Top Hood Crown"),
        ("N4", "Dry Dal Discharge", "DN300", "150#", "RAISED FACE", "Discharge End Weir"),
        ("N5", "Plenum Fines Drain", "DN100", "150#", "RAISED FACE", "Plenum Invert Low Point"),
        ("M1-M4", "Inspection Doors", "4x 500x400", "HINGED", "FOOD GASKET", "Drive & Non-Drive Sides"),
    ]
    row_y = ty0 - 11
    for r in n_rows:
        cur_x = tx0
        for w, val in zip(col_w, r):
            msp.add_lwpolyline([(cur_x, row_y), (cur_x + w, row_y), (cur_x + w, row_y - 10), (cur_x, row_y - 10), (cur_x, row_y)],
                               dxfattribs={'layer': 'TABLE_GRID', 'lineweight': 18})
            msp.add_text(val, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cur_x + 2, row_y - 7))
            cur_x += w
        row_y -= 10

    # Mechanical Specification Schedule (X = 270 to 570, Y = 70 to 180)
    sx0, sy0 = 270.0, 180.0
    sw = 300.0
    sh = 110.0
    msp.add_lwpolyline([(sx0, sy0), (sx0 + sw, sy0), (sx0 + sw, sy0 - sh), (sx0, sy0 - sh), (sx0, sy0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
    msp.add_text("MECHANICAL & PROCESS DESIGN SPECIFICATION - DR-101:", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((sx0 + 4, sy0 - 8))
    msp.add_line((sx0, sy0 - 12), (sx0 + sw, sy0 - 12), dxfattribs={'layer': 'BORDER_TITLE'})
    spec_notes = [
        "1. Equipment Tag: DR-101 | Service: Continuous Vibrating Fluid Bed Dal Conditioning & Drying.",
        "2. Effective Deck Dimensions: 14,000 mm Length x 1,000 mm Width (Effective Area: 14.0 m2).",
        "3. Material of Construction: All product contact parts SS304 (Ra < 0.8 um sanitary polish). Non-contact IS2062 CS.",
        "4. Fluidizing Air Rate: 14,150 kg/h (11,800 m3/h @ 85 deg C) | Superficial Velocity: 1.15 m/s (Umf = 0.85 m/s).",
        "5. Water Evaporation Duty: 401.31 kg/h H2O | Thermal Heating Duty: 512.4 kWth via Steam Coil HE-101.",
        "6. Vibration Dynamics: Stroke amplitude 3.5 mm @ 16 Hz (960 RPM); Twin unbalance motors 2 x 3.0 kW @ 45 deg.",
        "7. Isolation Efficiency: 8x Heavy-duty helical coil springs with rubber snubbers (>96% dynamic isolation).",
        "8. Residence Time: 18.0 - 22.0 minutes plug-flow with adjustable discharge overflow retention weir.",
        "9. CIP / Washdown: Complete internal spray ball system with sanitary drain valves for wet cleaning cycles.",
        "10. Safety Hold: Final dynamic balancing, spring resonance validation and FAT testing required prior to site release.",
    ]
    for idx, txt in enumerate(spec_notes):
        msp.add_text(txt, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((sx0 + 4, sy0 - 20 - idx * 8.8))

    dxf_out = os.path.abspath("engineering/cad/dxf/DWG-FIN-15T-008.dxf")
    pdf_out = os.path.abspath("engineering/cad/pdf/DWG-FIN-15T-008_DRYER_GA.pdf")
    export_dxf_and_pdf(doc, dxf_out, pdf_out)


# =============================================================================
# SHEET 09: Equipment GA - Chemical Reagent Dosing Skid SK-100
# =============================================================================
def build_sheet_09_dosing_skid_ga():
    print("Generating Sheet 09: Equipment GA Dosing Skid SK-100 (DWG-FIN-15T-009)...")
    doc = setup_cad_document()
    msp = doc.modelspace()
    draw_sheet_border_and_title_block(msp, "DWG-FIN-15T-009", "EQUIPMENT GENERAL ARRANGEMENT - CHEMICAL DOSING SKID SK-100", 9, TOTAL_SHEETS, "MECHANICAL")

    # Front Elevation View (Left-Center: X = 50, Y = 190)
    # Skid Dimensions: 2,400 mm L x 1,200 mm W x 1,900 mm H (Scale: 1:15 -> 160 mm x 126 mm)
    s = 1.0 / 15.0
    vx, vy = 50.0, 190.0
    sk_w, sk_h = 2400.0 * s, 1900.0 * s # 160.0 mm x 126.7 mm

    # Structural Base Frame & Secondary Containment Bund (110% Volume SS304)
    msp.add_lwpolyline([(vx, vy), (vx + sk_w, vy), (vx + sk_w, vy + 20), (vx + sk_w - 5, vy + 20), (vx + sk_w - 5, vy + 5), (vx + 5, vy + 5), (vx + 5, vy + 20), (vx, vy + 20), (vx, vy)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 50})
    msp.add_text("SECONDARY CONTAINMENT BUND (110% SPILL VOLUME)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((vx + 15, vy - 6))

    # Dual 500L HDPE Solution Tanks TK-102A & TK-102B
    for t_idx, t_name in enumerate(["TK-102A (DUTY)", "TK-102B (STANDBY)"]):
        tx = vx + 15 + t_idx * 55
        msp.add_lwpolyline([(tx, vy + 20), (tx + 45, vy + 20), (tx + 45, vy + 95), (tx, vy + 95), (tx, vy + 20)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
        msp.add_text(t_name, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx + 2, vy + 100))
        msp.add_text("500L HDPE", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx + 12, vy + 55))
        # Top High-Shear Agitator AG-102A/B
        msp.add_lwpolyline([(tx + 18, vy + 95), (tx + 27, vy + 95), (tx + 27, vy + 115), (tx + 18, vy + 115), (tx + 18, vy + 95)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
        msp.add_line((tx + 22.5, vy + 95), (tx + 22.5, vy + 35), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
        msp.add_line((tx + 14, vy + 35), (tx + 31, vy + 35), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
        msp.add_text(f"AG-102{chr(ord('A') + t_idx)}", height=1.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx + 12, vy + 118))

    # Dosing Pumps P-102A & P-102B (Duty/Standby Diaphragm Metering Pumps)
    px = vx + 125
    for p_idx, p_name in enumerate(["P-102A", "P-102B"]):
        py = vy + 35 + p_idx * 35
        msp.add_lwpolyline([(px, py), (px + 25, py), (px + 25, py + 22), (px, py + 22), (px, py)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
        msp.add_text(p_name, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((px + 2, py + 25))
        msp.add_text("DIAPHRAGM", height=1.4, dxfattribs={'layer': 'ANNOTATION'}).set_placement((px + 2, py + 14))

    # Calibration Column (1,000 mL Borosilicate Glass)
    cx = vx + 112
    msp.add_lwpolyline([(cx, vy + 20), (cx + 8, vy + 20), (cx + 8, vy + 85), (cx, vy + 85), (cx, vy + 20)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
    msp.add_text("CALIB", height=1.4, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx, vy + 90))
    msp.add_text("COL", height=1.4, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx + 1, vy + 83))

    # Skid Dimensions Callouts
    msp.add_text("2,400 mm OVERALL SKID LENGTH", height=2.2, dxfattribs={'layer': 'DIMENSIONS'}).set_placement((vx + 45, vy - 15))
    msp.add_text("1,900 mm OVERALL HEIGHT", height=2.2, dxfattribs={'layer': 'DIMENSIONS'}).set_placement((vx - 28, vy + 60))

    # Technical Specifications & Skid Bill of Materials (Right Side: X = 230 to 570)
    tx0, ty0 = 230.0, 340.0
    tw = 340.0
    th = 265.0
    msp.add_lwpolyline([(tx0, ty0), (tx0 + tw, ty0), (tx0 + tw, ty0 - th), (tx0, ty0 - th), (tx0, ty0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
    msp.add_text("CHEMICAL REAGENT DOSING SKID SPECIFICATION & BILL OF MATERIALS (SK-100):", height=2.2,
                 dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx0 + 4, ty0 - 8))
    msp.add_line((tx0, ty0 - 12), (tx0 + tw, ty0 - 12), dxfattribs={'layer': 'BORDER_TITLE'})

    sk_bom = [
        "ITEM 01: Solution Preparation Tanks TK-102A/B (2 Units, Duty / Standby)",
        "  - Net Volume: 500 Liters each | Material: UV-Stabilized Food-Grade Cross-Linked HDPE.",
        "  - Tank Dimensions: 800 mm Dia x 1,100 mm Straight Height | Conical bottom with 1.5\" drain.",
        "  - Accessories: Hinged loading hatch, dust screen, level gauge glass with ultrasonic transmitter.",
        "ITEM 02: High-Shear Agitator Mixers AG-102A/B (2 Units)",
        "  - Motor: 0.75 kW, 415V, 3-Phase, IP55, TEFC | Shaft & Impeller: SS316L 4-Blade Marine Propeller.",
        "  - Duty: Rapid dissolution of food-grade Sodium Bicarbonate / Citrate salts @ 25-35 deg C.",
        "ITEM 03: Precision Metering Chemical Pumps P-102A/B (2 Units, Duty / Standby)",
        "  - Type: Positive Displacement Mechanically Actuated PTFE Diaphragm Pumps.",
        "  - Flow Range: 5.0 to 50.0 L/h (Design Operating Point: 9.38 L/h for 0.50 wt% liquor recipe).",
        "  - Turndown: 10:1 Turndown ratio with stroke length micrometer + 4-20mA VFD speed modulation.",
        "  - Wetted Materials: PVDF Liquid End, Ceramic Double Ball Check Valves, PTFE Diaphragm.",
        "ITEM 04: Skid Piping, Instrumentation & Safety System",
        "  - Process Piping: 1\" NB Schedule 10S SS316L piping with sanitary tri-clamp connections.",
        "  - Safety Relief Valves PSV-102A/B: Set @ 4.0 bar g with full recirculation return to suction tank.",
        "  - Pulsation Dampener: Bladder-type 0.5L dampener smoothing discharge flow pulsation to < +/-3%.",
        "  - Calibration Column: 1,000 mL Borosilicate glass cylinder with 3-way isolation valve for flow QA.",
        "  - Containment: 110% Bund capacity (600L) with optical liquid leakage switch LS-102 interlocked to ESD.",
    ]
    for idx, txt in enumerate(sk_bom):
        msp.add_text(txt, height=1.7, dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx0 + 4, ty0 - 20 - idx * 7.5))

    dxf_out = os.path.abspath("engineering/cad/dxf/DWG-FIN-15T-009.dxf")
    pdf_out = os.path.abspath("engineering/cad/pdf/DWG-FIN-15T-009_DOSING_SKID_GA.pdf")
    export_dxf_and_pdf(doc, dxf_out, pdf_out)


# =============================================================================
# SHEET 10: P&ID - Triple-Effect ZLD Wastewater Evaporator EV-101A/B/C
# =============================================================================
def build_sheet_10_pid_evaporator():
    print("Generating Sheet 10: P&ID ZLD Evaporator EV-101 (DWG-FIN-15T-010)...")
    doc = setup_cad_document()
    msp = doc.modelspace()
    draw_sheet_border_and_title_block(msp, "DWG-FIN-15T-010", "P&ID - TRIPLE-EFFECT ZLD WASTEWATER EVAPORATOR", 10, TOTAL_SHEETS, "PIPING")

    # 1. Spent Liquor Feed Buffer Tank TK-104 & Feed Pump P-104 (Left: X = 35 to 110, Y = 180 to 290)
    msp.add_lwpolyline([(40, 200), (75, 200), (75, 260), (40, 260), (40, 200)], dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_text("EFFLUENT EQUALIZATION", height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((35, 268))
    msp.add_text("TK-104 (50 m3 FRP)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((40, 230))
    
    # Feed Pump P-104
    msp.add_circle((95, 215), 8.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_line((75, 215), (87, 215), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    msp.add_line((103, 215), (120, 215), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    msp.add_text("P-104 (5.5kW)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((85, 200))

    # 2. Triple-Effect Evaporator Stages: EV-101A, EV-101B, EV-101C (X = 130 to 390, Y = 160 to 320)
    effects = [
        ("1ST EFFECT EV-101A", "85 deg C / 0.58 bar abs", 150.0),
        ("2ND EFFECT EV-101B", "70 deg C / 0.31 bar abs", 240.0),
        ("3RD EFFECT EV-101C", "55 deg C / 0.16 bar abs", 330.0),
    ]

    for eff_title, eff_cond, ex in effects:
        # Calandria (Vertical Shell & Tube)
        msp.add_lwpolyline([(ex, 180), (ex + 25, 180), (ex + 25, 250), (ex, 250), (ex, 180)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
        # Tubes inside calandria
        for t in range(3):
            msp.add_line((ex + 6 + t * 6, 185), (ex + 6 + t * 6, 245), dxfattribs={'layer': 'EQUIPMENT', 'linetype': 'DASHED'})
        # Vapor Separator Head
        msp.add_arc((ex + 12.5, 250), 18.0, 0, 180, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
        msp.add_text(eff_title, height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((ex - 5, 275))
        msp.add_text(eff_cond, height=1.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((ex - 5, 172))

        # Forced Circulation Pump
        msp.add_circle((ex + 12.5, 145), 7.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
        msp.add_line((ex + 12.5, 180), (ex + 12.5, 152), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 35})
        msp.add_line((ex + 19.5, 145), (ex + 32, 145), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 35})
        msp.add_line((ex + 32, 145), (ex + 32, 215), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 35})
        msp.add_line((ex + 32, 215), (ex + 25, 215), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 35})

    # Inter-Effect Vapor Piping
    # 1st to 2nd Effect Vapor
    msp.add_line((150 + 12.5, 268), (150 + 12.5, 290), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((150 + 12.5, 290), (240, 230), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    draw_arrow(msp, 205, 255, 'RIGHT')
    # 2nd to 3rd Effect Vapor
    msp.add_line((240 + 12.5, 268), (240 + 12.5, 290), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((240 + 12.5, 290), (330, 230), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    draw_arrow(msp, 295, 255, 'RIGHT')

    # Motive Steam to 1st Effect (3.0 bar g)
    msp.add_line((120, 230), (150, 230), dxfattribs={'layer': 'UTILITY_PIPING', 'lineweight': 45})
    draw_valve(msp, 135, 230, vtype='CONTROL', fail_pos='FC', tag='TCV-401')
    msp.add_text("STEAM 3.0 bar g (520 kg/h)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((90, 235))

    # 3. Barometric Surface Condenser HE-103 & Vacuum Pump VP-101 (Right: X = 410 to 520, Y = 180 to 320)
    # 3rd Effect Vapor to Condenser
    msp.add_line((330 + 12.5, 268), (330 + 12.5, 295), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((330 + 12.5, 295), (425, 295), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((425, 295), (425, 270), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    draw_arrow(msp, 425, 280, 'DOWN')

    # Condenser HE-103
    msp.add_lwpolyline([(410, 220), (440, 220), (440, 270), (410, 270), (410, 220)], dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 45})
    msp.add_text("SURFACE CONDENSER", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((405, 275))
    msp.add_text("HE-103", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((418, 245))

    # Water Vacuum Pump VP-101
    msp.add_circle((480, 245), 8.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_line((440, 245), (472, 245), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 35})
    msp.add_text("VP-101 (7.5kW)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((468, 230))

    # Distillate Recovery to Tank TK-105 & Return to Soak Process
    msp.add_line((425, 220), (425, 180), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    draw_arrow(msp, 425, 175, 'DOWN')
    msp.add_text("CLEAN DISTILLATE RECOVERY (490 kg/h)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((375, 168))
    msp.add_text("RECYCLED TO PROCESS SOAK WATER (ZLD LOOP)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((365, 162))

    # Concentrate Bleed Pump P-105 from 3rd Effect
    msp.add_line((330 + 12.5, 145), (330 + 12.5, 110), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 40})
    draw_valve(msp, 330 + 12.5, 125, vtype='CONTROL', fail_pos='FC', tag='LCV-401', horizontal=False)
    draw_arrow(msp, 330 + 12.5, 105, 'DOWN')
    msp.add_text("ZLD CONCENTRATE SLURRY (40 wt% SOLIDS)", height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((280, 98))
    msp.add_text("TO DRYING PANS / MINERAL SALT BAGGING", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((280, 92))

    # 4. ZLD & Evaporator Design Basis Schedule
    cx0, cy0 = 35.0, 140.0
    msp.add_lwpolyline([(cx0, cy0), (cx0 + 230, cy0), (cx0 + 230, cy0 - 55), (cx0, cy0 - 55), (cx0, cy0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
    msp.add_text("ZLD EVAPORATOR OPERATING CONDITIONS & PERFORMANCE:", height=2.2,
                 dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx0 + 4, cy0 - 7))
    msp.add_line((cx0, cy0 - 10), (cx0 + 230, cy0 - 10), dxfattribs={'layer': 'BORDER_TITLE'})
    ev_notes = [
        "1. Feed Rate: 1,018.75 kg/h spent soak liquor @ 0.63 wt% dissolved mineral/organic solids.",
        "2. Evaporation Capacity: 980.0 kg/h clean distillate recovery (96.2% volumetric water recovery).",
        "3. Steam Economy: 2.38 kg H2O evaporated per kg 3.0 bar g motive steam supplied.",
        "4. Specific Energy Consumption: 0.42 kg steam / kg H2O evaporated (Energy optimized triple-effect).",
        "5. Distillate Quality: Total Dissolved Solids (TDS) < 25 ppm, Conductivity < 40 uS/cm (Food-grade reuse).",
        "6. Concentrate Discharge: 38.75 kg/h heavy slurry (40% total solids) to solar crystallization pan.",
    ]
    for idx, txt in enumerate(ev_notes):
        msp.add_text(txt, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((cx0 + 4, cy0 - 17 - idx * 7.2))

    dxf_out = os.path.abspath("engineering/cad/dxf/DWG-FIN-15T-010.dxf")
    pdf_out = os.path.abspath("engineering/cad/pdf/DWG-FIN-15T-010_PID_EVAPORATOR.pdf")
    export_dxf_and_pdf(doc, dxf_out, pdf_out)


# =============================================================================
# SHEET 11: Electrical Single-Line Diagram (SLD) & 415V MCC Distribution
# =============================================================================
def build_sheet_11_electrical_sld():
    print("Generating Sheet 11: Electrical SLD & MCC (DWG-FIN-15T-011)...")
    doc = setup_cad_document()
    msp = doc.modelspace()
    draw_sheet_border_and_title_block(msp, "DWG-FIN-15T-011", "ELECTRICAL SINGLE-LINE DIAGRAM & 415V MCC", 11, TOTAL_SHEETS, "ELECTRICAL")

    # 1. 11 kV Grid Supply, Step-Down Transformer TR-01 & Standby DG-01 (Top Left: X = 40 to 180, Y = 280 to 380)
    msp.add_line((50, 360), (90, 360), dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 50})
    msp.add_text("11 kV, 3-PHASE, 50 Hz GRID INCOMER", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((40, 365))
    
    # Transformer TR-01 (Dyn11 500 kVA, 11kV / 415V)
    msp.add_circle((70, 340), 9.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_circle((70, 326), 9.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_line((70, 360), (70, 349), dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("TRANSFORMER TR-01", height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((85, 338))
    msp.add_text("500 kVA, 11kV / 415V, Dyn11", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((85, 330))
    msp.add_text("ONAN, %Z = 4.5%", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((85, 322))

    # Standby DG-01 (250 kVA)
    msp.add_circle((160, 333), 12.0, dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
    msp.add_text("G", height=3.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((158, 330))
    msp.add_text("STANDBY DG-01", height=2.0, dxfattribs={'layer': 'ANNOTATION'}).set_placement((145, 350))
    msp.add_text("250 kVA, 415V DIESEL GEN", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((140, 315))

    # Automatic Transfer Switch (ATS) / Interlock
    msp.add_line((70, 317), (70, 290), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((160, 321), (160, 290), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_line((70, 290), (160, 290), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 45})
    msp.add_lwpolyline([(110, 295), (120, 295), (120, 285), (110, 285), (110, 295)], dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
    msp.add_text("ATS INTERLOCK", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((102, 300))

    # 2. Main 415V 3-Phase Busbar (800A, 50kA 1-sec Rated Busbar)
    bus_y = 265.0
    msp.add_line((40, bus_y), (540, bus_y), dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 70})
    msp.add_line((115, 285), (115, bus_y), dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 50})
    msp.add_text("MAIN 415V, 3-PHASE, 4-WIRE, 50 Hz BUSBAR (800A TPN, 50 kA 1-SEC)", height=2.5,
                 dxfattribs={'layer': 'ANNOTATION'}).set_placement((140, bus_y + 4))

    # 3. Motor Control Center (MCC-01) Feeders Dropping from Bus
    feeders = [
        ("F01", "BL-101 Fluid Blower", "55.0 kW", "VFD (4-20mA)", 60),
        ("F02", "BL-102 ID Exhaust Fan", "30.0 kW", "Soft Starter", 110),
        ("F03", "P-105 Evap Circ Pump", "18.5 kW", "DOL Starter", 160),
        ("F04", "PK-101 Packaging Line", "15.0 kW", "MCCB Feeder", 210),
        ("F05", "AG-101A/B Soak Mixers", "8.0 kW", "DOL Dual Fwd/Rev", 260),
        ("F06", "M-101A/B Dryer Exciters", "6.0 kW", "Synchronized DOL", 310),
        ("F07", "SC-100 Dal Cleaner", "5.5 kW", "DOL Starter", 360),
        ("F08", "SC-101 Dewater Screen", "3.7 kW", "DOL Starter", 410),
        ("F09", "CV-101 Bucket Elevator", "3.0 kW", "DOL Starter", 460),
        ("F10", "APFC Capacitor Bank", "60 kVAR", "Automatic 6-Stage", 510),
    ]

    for f_tag, f_desc, f_kw, f_type, fx in feeders:
        msp.add_line((fx, bus_y), (fx, bus_y - 25), dxfattribs={'layer': 'PROCESS_PIPING', 'lineweight': 35})
        # Circuit Breaker Symbol
        msp.add_lwpolyline([(fx - 3, bus_y - 8), (fx + 3, bus_y - 8), (fx + 3, bus_y - 14), (fx - 3, bus_y - 14), (fx - 3, bus_y - 8)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
        # Starter Box
        msp.add_lwpolyline([(fx - 15, bus_y - 25), (fx + 15, bus_y - 25), (fx + 15, bus_y - 55), (fx - 15, bus_y - 55), (fx - 15, bus_y - 25)],
                           dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 40})
        msp.add_text(f_tag, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((fx - 8, bus_y - 32))
        msp.add_text(f_kw, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((fx - 12, bus_y - 42))
        msp.add_text(f_desc, height=1.4, dxfattribs={'layer': 'ANNOTATION'}).set_placement((fx - 18, bus_y - 62))
        msp.add_text(f_type, height=1.3, dxfattribs={'layer': 'ANNOTATION'}).set_placement((fx - 18, bus_y - 68))

    # 4. Electrical Load & Distribution Summary Table (Bottom Half)
    tx0, ty0 = 35.0, 160.0
    tw = 525.0
    th = 85.0
    msp.add_lwpolyline([(tx0, ty0), (tx0 + tw, ty0), (tx0 + tw, ty0 - th), (tx0, ty0 - th), (tx0, ty0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
    msp.add_text("ELECTRICAL LOAD SUMMARY, TRANSFORMER SIZING & POWER FACTOR CORRECTION:", height=2.2,
                 dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx0 + 4, ty0 - 8))
    msp.add_line((tx0, ty0 - 12), (tx0 + tw, ty0 - 12), dxfattribs={'layer': 'BORDER_TITLE'})

    elec_notes = [
        "1. Total Plant Connected Load: 184.5 kW | Operating Diversity Factor: 0.70 | Maximum Running Demand: 129.2 kW.",
        "2. Operating Power Factor: 0.85 uncorrected -> Corrected to 0.98 lag via 60 kVAR Automatic Power Factor Capacitor Bank.",
        "3. Apparent Power Demand: 131.8 kVA @ 0.98 PF | 500 kVA Transformer Utilization: 26.4% (Generous margin for phase 2 expansion).",
        "4. Standby Generator DG-01: 250 kVA (200 kW @ 0.8 PF) rating provides 100% emergency running capacity during grid outage.",
        "5. Motor Protection: Class 10/20 bimetallic overload relays, phase failure protection, thermistor inputs for blower motors.",
        "6. Earthing System: Combined TN-S earthing grid with dedicated chemical earthing pits (<1.0 ohm overall resistance).",
        "7. Lightning Protection: Early Streamer Emission (ESE) air terminal per IS/IEC 62305 with 45m protection radius.",
    ]
    for idx, txt in enumerate(elec_notes):
        msp.add_text(txt, height=1.8, dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx0 + 4, ty0 - 20 - idx * 9.0))

    dxf_out = os.path.abspath("engineering/cad/dxf/DWG-FIN-15T-011.dxf")
    pdf_out = os.path.abspath("engineering/cad/pdf/DWG-FIN-15T-011_ELECTRICAL_SLD.pdf")
    export_dxf_and_pdf(doc, dxf_out, pdf_out)


# =============================================================================
# SHEET 12: Hazardous Area Classification & Combustible Dust Zoning
# =============================================================================
def build_sheet_12_dust_zoning():
    print("Generating Sheet 12: Hazardous Area & Dust Zoning (DWG-FIN-15T-012)...")
    doc = setup_cad_document()
    msp = doc.modelspace()
    draw_sheet_border_and_title_block(msp, "DWG-FIN-15T-012", "HAZARDOUS AREA CLASSIFICATION & DUST ZONING", 12, TOTAL_SHEETS, "SAFETY")

    # Facility Plan Outline (Center: X = 40 to 360, Y = 160 to 340)
    bx0, by0 = 50.0, 160.0
    bw, bh = 300.0, 160.0
    msp.add_lwpolyline([(bx0, by0), (bx0 + bw, by0), (bx0 + bw, by0 + bh), (bx0, by0 + bh), (bx0, by0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 50})
    msp.add_text("PROCESSING BUILDING - PLAN VIEW COMBUSTIBLE DUST ZONING (NFPA 652 / IEC 60079-10-2)", height=2.5,
                 dxfattribs={'layer': 'ANNOTATION'}).set_placement((bx0 + 10, by0 + bh + 6))

    # Zone 20 Regions (Continuous Cloud - Red Hatch/Border)
    # Silos (X = 65 to 110, Y = 240 to 290)
    msp.add_circle((75, 270), 15.0, dxfattribs={'layer': 'VALVES', 'lineweight': 40})
    msp.add_circle((110, 270), 15.0, dxfattribs={'layer': 'VALVES', 'lineweight': 40})
    msp.add_text("ZONE 20", height=2.0, dxfattribs={'layer': 'VALVES'}).set_placement((68, 270))
    msp.add_text("ZONE 20", height=2.0, dxfattribs={'layer': 'VALVES'}).set_placement((103, 270))
    msp.add_text("RAW GRAIN SILOS (INTERIOR)", height=1.6, dxfattribs={'layer': 'ANNOTATION'}).set_placement((65, 290))

    # Dryer Interior (X = 180 to 280, Y = 240 to 275)
    msp.add_lwpolyline([(180, 245), (280, 245), (280, 275), (180, 275), (180, 245)], dxfattribs={'layer': 'VALVES', 'lineweight': 40})
    msp.add_text("ZONE 20 (FLUID BED DRYER DR-101 INTERIOR)", height=1.8, dxfattribs={'layer': 'VALVES'}).set_placement((185, 258))

    # Cyclone & Baghouse Interior (X = 295 to 335, Y = 240 to 285)
    msp.add_lwpolyline([(295, 240), (335, 240), (335, 285), (295, 285), (295, 240)], dxfattribs={'layer': 'VALVES', 'lineweight': 40})
    msp.add_text("ZONE 20", height=1.8, dxfattribs={'layer': 'VALVES'}).set_placement((305, 265))
    msp.add_text("DUST COLLECTOR BF-102", height=1.5, dxfattribs={'layer': 'ANNOTATION'}).set_placement((290, 290))

    # Zone 21 Regions (1.5m Envelope around Chutes & Transfers - Yellow/Dashed)
    # Around Infeed Hopper
    msp.add_circle((140, 260), 22.0, dxfattribs={'layer': 'INSTRUMENTATION', 'lineweight': 35, 'linetype': 'DASHED'})
    msp.add_text("ZONE 21 (1.5m)", height=1.8, dxfattribs={'layer': 'INSTRUMENTATION'}).set_placement((125, 260))

    # Around Packaging Machine PK-101
    msp.add_lwpolyline([(240, 180), (310, 180), (310, 230), (240, 230), (240, 180)],
                       dxfattribs={'layer': 'INSTRUMENTATION', 'lineweight': 35, 'linetype': 'DASHED'})
    msp.add_text("ZONE 21 (PACKAGING & WEIGHING)", height=1.8, dxfattribs={'layer': 'INSTRUMENTATION'}).set_placement((242, 205))

    # Zone 22 (General Dry Processing Hall - Cyan/Light Dash)
    msp.add_text("ZONE 22: ENTIRE UNCONTROLLED DRY PROCESSING HALL (3.0m RADIUS FROM DUST SOURCES)", height=2.0,
                 dxfattribs={'layer': 'DIMENSIONS'}).set_placement((bx0 + 8, by0 + 12))

    # Safe Zone / Non-Hazardous (Wet Processing Zone 2 & Electrical Room)
    msp.add_lwpolyline([(bx0 + 70, by0 + 20), (bx0 + 140, by0 + 20), (bx0 + 140, by0 + 70), (bx0 + 70, by0 + 70), (bx0 + 70, by0 + 20)],
                       dxfattribs={'layer': 'EQUIPMENT', 'lineweight': 35})
    msp.add_text("NON-HAZARDOUS", height=2.0, dxfattribs={'layer': 'EQUIPMENT'}).set_placement((bx0 + 75, by0 + 48))
    msp.add_text("(WET WASHDOWN AREA)", height=1.6, dxfattribs={'layer': 'EQUIPMENT'}).set_placement((bx0 + 72, by0 + 40))

    # Dust Explosion Protection Schedule (Right Side: X = 365 to 570)
    tx0, ty0 = 365.0, 340.0
    tw = 205.0
    th = 250.0
    msp.add_lwpolyline([(tx0, ty0), (tx0 + tw, ty0), (tx0 + tw, ty0 - th), (tx0, ty0 - th), (tx0, ty0)],
                       dxfattribs={'layer': 'BORDER_TITLE', 'lineweight': 35})
    msp.add_text("DUST HAZARD DATA & COMPLIANCE:", height=2.2, dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx0 + 4, ty0 - 8))
    msp.add_line((tx0, ty0 - 12), (tx0 + tw, ty0 - 12), dxfattribs={'layer': 'BORDER_TITLE'})

    dust_notes = [
        "1. Material: Toor Dal (Pigeon Pea) Grain Dust",
        "2. Dust Deflagration Class: St 1 (Kst: 85 bar-m/s)",
        "3. Maximum Explosion Pressure Pmax: 7.6 bar g",
        "4. Minimum Ignition Energy (MIE): > 30 mJ",
        "5. Minimum Ignition Temp (MIT - Cloud): 430 deg C",
        "6. Layer Ignition Temperature (LIT - 5mm): 260 deg C",
        "7. Permissible Equipment Surface Temp: T120 deg C",
        "   (Max 2/3 of LIT per IEC 60079-0)",
        "8. Zone 20 Enclosures: IP65 Ex tb IIIC T120 deg C",
        "9. Zone 21/22 Enclosures: IP55 Ex tc IIIC T120 deg C",
        "10. Explosion Relief: Flameless explosion vents",
        "    on Baghouse BF-102 and Cyclone CY-101",
        "    certified per NFPA 68 / EN 14491.",
        "11. Static Bonding: All pipes, ductwork, filter",
        "    cages and vessels bonded to earth (< 10 ohms).",
        "12. Housekeeping: Scheduled dry vacuum cleaning",
        "    preventing dust layer buildup > 1.0 mm.",
    ]
    for idx, txt in enumerate(dust_notes):
        msp.add_text(txt, height=1.7, dxfattribs={'layer': 'ANNOTATION'}).set_placement((tx0 + 4, ty0 - 20 - idx * 7.8))

    dxf_out = os.path.abspath("engineering/cad/dxf/DWG-FIN-15T-012.dxf")
    pdf_out = os.path.abspath("engineering/cad/pdf/DWG-FIN-15T-012_DUST_ZONING.pdf")
    export_dxf_and_pdf(doc, dxf_out, pdf_out)


# =============================================================================
# MASTER RUNNER: Build All 12 Conceptual FEED Drawings
# =============================================================================
def build_all_12_feed_drawings():
    print("=" * 65)
    print("STARTING COMPLETE 12-SHEET V4 CONCEPTUAL FEED DRAWING GENERATION...")
    print("=" * 65)
    # Sheets 1 to 4 and 7 (Existing Exemplars with standardized 12-sheet titles)
    build_exemplar_1_pfd()
    build_exemplar_1b_stream_table()
    build_exemplar_2_pid()
    build_exemplar_3_plot_plan()
    build_sheet_05_pid_dryer()
    build_sheet_06_pid_packaging()
    build_exemplar_4_soak_tank_ga()
    build_sheet_08_dryer_ga()
    build_sheet_09_dosing_skid_ga()
    build_sheet_10_pid_evaporator()
    build_sheet_11_electrical_sld()
    build_sheet_12_dust_zoning()
    print("=" * 65)
    print("ALL 12 V4 CONCEPTUAL FEED DRAWINGS SUCCESSFULLY GENERATED!")
    print("=" * 65)

if __name__ == "__main__":
    build_all_12_feed_drawings()
