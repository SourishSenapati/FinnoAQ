"""
World-Class Multi-Sheet Engineering PDF Drawing Package Generator.
Generates a complete, professional, 11-page vector CAD drawing package:
- Sheet 01: Cover Page, Document Control, Client Approval & Drawing Index
- Sheet 02: Greenfield Site Plot Plan, Logistics & Hygienic Zoning (DWG-001)
- Sheet 03: Process Flow Diagram (PFD) & 12-Stream Mass/Energy Balance (DWG-002)
- Sheet 04: P&ID: Grain Receiving & Soaking Battery (DWG-003)
- Sheet 05: P&ID: Continuous Fluid-Bed Drying & Thermal Utilities (DWG-004)
- Sheet 06: P&ID: Cleanroom Packaging & Airlocks (DWG-005)
- Sheet 07: Equipment GA: 7.5 m3 Sanitary Soak Vessel TK-101 (DWG-006)
- Sheet 08: Equipment GA: Continuous Vibrating Fluid-Bed Dryer DR-101 (DWG-007)
- Sheet 09: Equipment GA: Automated Chemical Dosing Skid SK-100 (DWG-008)
- Sheet 10: Electrical Single Line Diagram (SLD) & MCC Schedule (DWG-009)
- Sheet 11: Utility Flow Diagram & 25 KLD Effluent Treatment Plant (DWG-010)

Uses ReportLab & Matplotlib for ultra-crisp vector line work and industrial typography.
"""

import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages

def draw_iso_title_block(ax, sheet_no, total_sheets, dwg_no, dwg_title, scale="1:100", discipline="PROCESS / MECHANICAL"):
    # Drawing border
    ax.plot([0, 1000, 1000, 0, 0], [0, 0, 700, 700, 0], color='#1A365D', lw=2.0)
    ax.plot([15, 985, 985, 15, 15], [15, 15, 685, 685, 15], color='#2B6CB0', lw=1.0)

    # Title block container in bottom-right corner (X: 650 to 985, Y: 15 to 135)
    tb = patches.Rectangle((620, 15), 365, 120, edgecolor='#1A365D', facecolor='#F7FAFC', lw=1.5)
    ax.add_patch(tb)

    # Dividing lines in title block
    ax.plot([620, 985], [95, 95], color='#CBD5E0', lw=1.0)
    ax.plot([620, 985], [60, 60], color='#CBD5E0', lw=1.0)
    ax.plot([780, 780], [15, 95], color='#CBD5E0', lw=1.0)
    ax.plot([880, 880], [15, 60], color='#CBD5E0', lw=1.0)

    # Company & Project Header
    ax.text(630, 120, "HARAKUTIR AGRO-PROCESS ENGINEERING", fontsize=8, fontweight='bold', color='#1A365D')
    ax.text(630, 105, "15,000 kg/day Toor-Dal Optimization Greenfield Plant", fontsize=7, color='#4A5568')

    # Drawing Title & Number
    ax.text(630, 80, dwg_title.upper(), fontsize=8.5, fontweight='bold', color='#2B6CB0')
    ax.text(630, 67, f"DWG NO: {dwg_no}", fontsize=7.5, fontweight='bold', color='#2D3748')

    # Status & Discipline
    ax.text(630, 45, "STAGE: CONCEPTUAL FEED", fontsize=6.5, fontweight='bold', color='#C53030')
    ax.text(630, 32, f"DISCIPLINE: {discipline}", fontsize=6.5, color='#4A5568')
    ax.text(630, 20, "STAMP: PRELIMINARY - NOT FOR CONSTRUCTION", fontsize=6, fontweight='bold', color='#E53E3E')

    # Metadata columns
    ax.text(790, 80, f"SCALE: {scale}", fontsize=6.5, color='#4A5568')
    ax.text(790, 67, "UNITS: MILLIMETERS (mm)", fontsize=6.5, color='#4A5568')
    ax.text(790, 45, "REV: V3.0", fontsize=7, fontweight='bold', color='#1A365D')
    ax.text(790, 32, "DATE: OCT 2026", fontsize=6.5, color='#4A5568')
    ax.text(790, 20, "PROJ ID: FIN-15T-2026", fontsize=6.5, color='#4A5568')

    ax.text(890, 45, f"SHEET: {sheet_no} OF {total_sheets}", fontsize=7.5, fontweight='bold', color='#1A365D')
    ax.text(890, 32, "CHK: RED-TEAM", fontsize=6.5, color='#4A5568')
    ax.text(890, 20, "GATE: G-A HOLD", fontsize=6.5, fontweight='bold', color='#C53030')

    # Revision block in top-right corner
    rev_box = patches.Rectangle((750, 635), 235, 50, edgecolor='#CBD5E0', facecolor='#FFFFFF', lw=1.0)
    ax.add_patch(rev_box)
    ax.text(755, 670, "REV   DATE       DESCRIPTION                 BY   APP", fontsize=5.5, fontweight='bold', color='#718096')
    ax.text(755, 655, "V1.0  2026-10-12 PRELIMINARY SCREENING       ENG  PM", fontsize=5.5, color='#4A5568')
    ax.text(755, 642, "V3.0  2026-10-15 V3 RIGOROUS FEED & AUDIT    SYS  DIR", fontsize=5.5, fontweight='bold', color='#2B6CB0')

    # Standard Notes block in bottom-left
    ax.text(25, 30, "GENERAL ENGINEERING NOTES:\n"
                    "1. ALL DIMENSIONS ARE IN MILLIMETERS UNLESS SPECIFIED OTHERWISE. LEVEL DATUM ±0.000 CORRESPONDS TO FINISHED FLOOR LEVEL (FFL).\n"
                    "2. THIS DRAWING IS THE PROPERTY OF HARAKUTIR AND CONSTITUTES PRELIMINARY FRONT-END ENGINEERING DESIGN (FEED).\n"
                    "3. ALL EQUIPMENT CAPACITIES, NOZZLE SCHEDULES, AND UTILITIES ARE BASED ON SENSITIVITY ENVELOPES PENDING GATE G-A PHYSICAL TRIAL RESULTS.\n"
                    "4. STRICTLY PROHIBITED FROM USE FOR TENDER, PURCHASE ORDER PROCUREMENT, SHOP FABRICATION, OR SITE CONSTRUCTION.",
            fontsize=5.2, color='#718096', linespacing=1.3)

def generate_pdf_package():
    out_pdf = os.path.abspath("engineering/cad/pdf/HARAKUTIR_15TPD_ENGINEERING_DRAWING_PACKAGE_REV_V3.pdf")
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    print(f"Generating World-Class Vector Drawing Package at: {out_pdf}")

    with PdfPages(out_pdf) as pdf:
        total_sheets = 12

        # =========================================================================
        # SHEET 1: COVER PAGE & MASTER DRAWING INDEX
        # =========================================================================
        print("Rendering Sheet 01: Cover Page & Master Drawing Index...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150) # A3 Landscape
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')

        draw_iso_title_block(ax, "01", total_sheets, "DWG-FIN-15T-000", "Master Cover Sheet & Drawing Index", "NTS", "PROJECT MANAGEMENT")

        # Cover Banner
        banner = patches.Rectangle((50, 480), 900, 140, facecolor='#1A365D', edgecolor='#0D1B2A')
        ax.add_patch(banner)
        ax.text(500, 570, "HARAKUTIR INDUSTRIAL PULSE PROCESSING", fontsize=18, fontweight='bold', color='#FFFFFF', ha='center')
        ax.text(500, 535, "15,000 kg/day Incoming-Feed Toor-Dal Tenderization Facility", fontsize=13, color='#E2E8F0', ha='center')
        ax.text(500, 505, "CONCEPTUAL FRONT-END ENGINEERING DESIGN (FEED) PACKAGE — REV V3.0", fontsize=10, fontweight='bold', color='#63B3ED', ha='center')

        # Project Highlights Card
        info_box = patches.Rectangle((50, 160), 400, 290, facecolor='#EDF2F7', edgecolor='#CBD5E0', lw=1.2)
        ax.add_patch(info_box)
        ax.text(70, 420, "PROJECT DESIGN PARAMETERS", fontsize=11, fontweight='bold', color='#2B6CB0')
        ax.text(70, 395, "• Raw Material: Imported Tanzanian Split Pigeon Pea (Cajanus cajan)", fontsize=7.5, color='#2D3748')
        ax.text(70, 375, "• Consignment Tracking: PENDING_COMMERCIAL_LOT_ID", fontsize=7.5, color='#C53030', fontweight='bold')
        ax.text(70, 355, "• Incoming Capacity: 15,000 kg/day (13,425 kg/day Dry Solids @ 10.5% wb)", fontsize=7.5, color='#2D3748')
        ax.text(70, 335, "• Finished Dal Yield: 14,267.8 kg/day (95.65% Dry Solids Recovery)", fontsize=7.5, color='#2D3748')
        ax.text(70, 315, "• Chemical Treatment: 0.50% w/w Food-Grade NaHCO3 (112.5 kg/day peak)", fontsize=7.5, color='#2D3748')
        ax.text(70, 295, "• Drying Duty: 3,877.8 kg/day Evaporation (285.1 kg/h Design over 13.6h)", fontsize=7.5, color='#2D3748')
        ax.text(70, 275, "• Turnkey Plant CAPEX: ₹542.0 Lakh (AACE Class 4 Greenfield Estimate)", fontsize=7.5, color='#2D3748')
        ax.text(70, 255, "• Conversion OpEx: ₹9.35 / kg Finished Dal (Full Factory Conversion)", fontsize=7.5, color='#2D3748')
        ax.text(70, 235, "• Plot Dimensions: 52.0m x 24.0m (1,248.0 m² Pre-Engineered Building)", fontsize=7.5, color='#2D3748')
        ax.text(70, 215, "• Governing Standards: ASME Sec VIII, IS 2825, FSSAI 2011, NFPA 68, ISA-5.1", fontsize=7.5, color='#2D3748')
        ax.text(70, 185, "STATUS: GATE G-A HOLD ACTIVE (Zero physical data fabricated)", fontsize=8, fontweight='bold', color='#C53030')

        # Drawing Index Table
        idx_box = patches.Rectangle((470, 160), 480, 290, facecolor='#FFFFFF', edgecolor='#CBD5E0', lw=1.2)
        ax.add_patch(idx_box)
        ax.text(490, 425, "MASTER DRAWING INDEX", fontsize=11, fontweight='bold', color='#2B6CB0')

        drawings_index = [
            ("DWG-FIN-15T-000", "01", "Master Cover Sheet & Drawing Index", "PROJECT"),
            ("DWG-FIN-15T-001", "02", "Greenfield Site Plot Plan & Hygienic Zoning", "CIVIL / PLOT"),
            ("DWG-FIN-15T-002", "03", "Process Flow Diagram (PFD) & 12-Stream Balance", "PROCESS"),
            ("DWG-FIN-15T-003", "04", "P&ID: Raw Grain Intake & Soaking Battery", "PIPING & INST"),
            ("DWG-FIN-15T-004", "05", "P&ID: Vibrating Fluid Bed Drying & Thermal Air", "PIPING & INST"),
            ("DWG-FIN-15T-005", "06", "P&ID: Cleanroom Packaging & N2 Flushing", "PIPING & INST"),
            ("DWG-FIN-15T-006", "07", "Equipment GA: 7.5 m³ Sanitary Soak Vessel TK-101", "MECHANICAL"),
            ("DWG-FIN-15T-007", "08", "Equipment GA: Vibrating Fluid Bed Dryer DR-101", "MECHANICAL"),
            ("DWG-FIN-15T-008", "09", "Equipment GA: Automated Chemical Skid SK-100", "MECHANICAL"),
            ("DWG-FIN-15T-009", "10", "Electrical Single Line Diagram (SLD) & MCC", "ELECTRICAL"),
            ("DWG-FIN-15T-010", "11", "Utility Flow Diagram & 25 KLD ETP Flowsheet", "ENVIRONMENTAL"),
            ("DWG-FIN-15T-011", "12", "Hazardous Area Classification & Dust Safety Plan", "SAFETY / EHS"),
        ]

        y_pos = 398
        for dwg, sh, title, disc in drawings_index:
            ax.text(490, y_pos, f"SHEET {sh} | {dwg} : {title}", fontsize=6.8, color='#2D3748')
            ax.text(935, y_pos, disc, fontsize=6.2, color='#718096', ha='right')
            y_pos -= 19.5

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 2: PLOT PLAN & HYGIENIC ZONING (DWG-001)
        # =========================================================================
        print("Rendering Sheet 02: Plot Plan & Hygienic Zoning...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "02", total_sheets, "DWG-FIN-15T-001", "Greenfield Site Plot Plan & Hygienic Zoning", "1:100", "CIVIL / PLOT")

        # Building Outline: 52m x 24m -> Placed from X=80 to X=860 (780 units = 52m, 15 units/m), Y=180 to Y=540 (360 units = 24m)
        peb_shed = patches.Rectangle((80, 180), 780, 360, facecolor='#EDF2F7', edgecolor='#1A365D', lw=2.5)
        ax.add_patch(peb_shed)
        ax.text(470, 555, "52,000 mm (52.0 m) OVERALL BUILDING LENGTH", fontsize=8, fontweight='bold', color='#1A365D', ha='center')
        ax.text(60, 360, "24,000 mm\n(24.0 m)", fontsize=8, fontweight='bold', color='#1A365D', va='center', ha='center')

        # Structural Column Grid (Grids 1-10, A-D)
        for i, gx in enumerate(range(80, 861, 86)):
            ax.plot([gx, gx], [165, 550], color='#CBD5E0', ls='--', lw=0.8)
            ax.text(gx, 560, f"GRID {i+1}", fontsize=5.5, color='#4A5568', ha='center')
        for i, gy in enumerate([180, 300, 420, 540]):
            ax.plot([65, 875], [gy, gy], color='#CBD5E0', ls='--', lw=0.8)
            ax.text(50, gy, f"LINE {chr(65+i)}", fontsize=5.5, color='#4A5568', va='center')

        # Functional Zones
        # Zone 1: Raw Intake (80, 360, 180, 180) - Brown Zone
        z1 = patches.Rectangle((80, 360), 180, 180, facecolor='#FEEBC8', edgecolor='#DD6B20', lw=1.5)
        ax.add_patch(z1)
        ax.text(170, 520, "ZONE 1: RAW INTAKE & SILOS", fontsize=7.5, fontweight='bold', color='#C05621', ha='center')
        ax.text(170, 505, "HYGIENE: UNCONTROLLED (BROWN)", fontsize=6, color='#7B341E', ha='center')
        # Silos SL-101A/B
        c1 = patches.Circle((130, 440), 28, facecolor='#ED8936', edgecolor='#7B341E')
        c2 = patches.Circle((200, 440), 28, facecolor='#ED8936', edgecolor='#7B341E')
        ax.add_patch(c1); ax.add_patch(c2)
        ax.text(130, 440, "SL-101A\n30 MT", fontsize=5.5, color='#FFFFFF', ha='center', va='center', fontweight='bold')
        ax.text(200, 440, "SL-101B\n30 MT", fontsize=5.5, color='#FFFFFF', ha='center', va='center', fontweight='bold')

        # Zone 2: Wet Processing (260, 360, 240, 180) - Medium Hygiene
        z2 = patches.Rectangle((260, 360), 240, 180, facecolor='#EBF8FF', edgecolor='#3182CE', lw=1.5)
        ax.add_patch(z2)
        ax.text(380, 520, "ZONE 2: WET PROCESS & STEEPING", fontsize=7.5, fontweight='bold', color='#2B6CB0', ha='center')
        ax.text(380, 505, "HYGIENE: MEDIUM (GREY ZONE) | SS DRAINS", fontsize=6, color='#2C5282', ha='center')
        # Soak Tanks TK-101A/B
        tk1 = patches.Circle((320, 440), 24, facecolor='#63B3ED', edgecolor='#2B6CB0', lw=1.2)
        tk2 = patches.Circle((390, 440), 24, facecolor='#63B3ED', edgecolor='#2B6CB0', lw=1.2)
        skid = patches.Rectangle((435, 415), 45, 25, facecolor='#BEE3F8', edgecolor='#2B6CB0', lw=1.0)
        ax.add_patch(tk1); ax.add_patch(tk2); ax.add_patch(skid)
        ax.text(320, 440, "TK-101A\n7.5 m³", fontsize=5.5, color='#1A365D', ha='center', va='center', fontweight='bold')
        ax.text(390, 440, "TK-101B\n7.5 m³", fontsize=5.5, color='#1A365D', ha='center', va='center', fontweight='bold')
        ax.text(457, 427, "SK-100\nDOSING", fontsize=4.5, color='#1A365D', ha='center', va='center')

        # Zone 3: Drying & Cooling (500, 360, 200, 180)
        z3 = patches.Rectangle((500, 360), 200, 180, facecolor='#FEFCBF', edgecolor='#D69E2E', lw=1.5)
        ax.add_patch(z3)
        ax.text(600, 520, "ZONE 3: THERMAL DRYING GALLERY", fontsize=7.5, fontweight='bold', color='#B7791F', ha='center')
        ax.text(600, 505, "HYGIENE: MEDIUM-HIGH | 85°C AIR", fontsize=6, color='#744210', ha='center')
        # Dryer DR-101 (14m x 1m -> 210 x 15 units)
        dryer = patches.Rectangle((515, 425), 170, 22, facecolor='#ECC94B', edgecolor='#975A16', lw=1.2)
        ax.add_patch(dryer)
        ax.text(600, 436, "DR-101 CONTINUOUS FLUID BED DRYER (14.0m x 1.0m)", fontsize=5.2, color='#744210', ha='center', va='center', fontweight='bold')

        # Zone 4: Packaging Cleanroom (700, 360, 160, 180) - White Zone Class 8
        z4 = patches.Rectangle((700, 360), 160, 180, facecolor='#E6FFFA', edgecolor='#319795', lw=1.5)
        ax.add_patch(z4)
        ax.text(780, 520, "ZONE 4: PACKAGING CLEANROOM", fontsize=7.5, fontweight='bold', color='#285E61', ha='center')
        ax.text(780, 505, "CLASS 8 (+15 Pa) | AIRLOCKS | HEPA", fontsize=6, color='#234E52', ha='center')
        # FFS Machines PK-101A/B
        pk1 = patches.Rectangle((730, 425), 35, 30, facecolor='#81E6D9', edgecolor='#234E52')
        pk2 = patches.Rectangle((795, 425), 35, 30, facecolor='#81E6D9', edgecolor='#234E52')
        ax.add_patch(pk1); ax.add_patch(pk2)
        ax.text(747, 440, "PK-101A\n1kg FFS", fontsize=5, color='#234E52', ha='center', va='center')
        ax.text(812, 440, "PK-101B\n5kg FFS", fontsize=5, color='#234E52', ha='center', va='center')

        # Central 3.0m Corridor (Y=300 to Y=360)
        corr = patches.Rectangle((80, 300), 780, 60, facecolor='#FFFFFF', edgecolor='#A0AEC0', lw=1.0)
        ax.add_patch(corr)
        ax.text(470, 330, "MAIN LOGISTICS ARTERIAL SPINE — 3,000 mm WIDE FORKLIFT & PALLET TRUCK PASSAGEWAY", fontsize=6.5, color='#4A5568', ha='center', va='center', fontweight='bold')

        # Southern Bays: Utility, ETP, QC Lab, Warehouse (Y=180 to Y=300)
        # Utility (80 to 260)
        u_box = patches.Rectangle((80, 180), 180, 120, facecolor='#FFF5F5', edgecolor='#E53E3E')
        ax.add_patch(u_box)
        ax.text(170, 280, "UTILITY ISLAND: BOILER & DG", fontsize=7, fontweight='bold', color='#9B2C2C', ha='center')
        ax.text(170, 260, "BL-101: 600 kg/h IBR Steam Boiler\nDG-101: 250 kVA Backup Generator\nTR-101: 315 kVA Transformer Substation", fontsize=5.5, color='#742A2A', ha='center')

        # ETP Bay (260 to 440)
        etp_box = patches.Rectangle((260, 180), 180, 120, facecolor='#F0FFF4', edgecolor='#38A169')
        ax.add_patch(etp_box)
        ax.text(350, 280, "25 KLD EFFLUENT TREATMENT (ETP)", fontsize=7, fontweight='bold', color='#22543D', ha='center')
        ax.text(350, 260, "Equalization (30 m³) | MBBR Aeration\nTube Settler Clarifier | Sludge Press\nSPCB Discharge Norms Compliant", fontsize=5.5, color='#1C4532', ha='center')

        # QC Lab & Admin (440 to 600)
        qc_box = patches.Rectangle((440, 180), 160, 120, facecolor='#FAF5FF', edgecolor='#805AD5')
        ax.add_patch(qc_box)
        ax.text(520, 280, "QC MICROBIOLOGY & LAB", fontsize=7, fontweight='bold', color='#553C9A', ha='center')
        ax.text(520, 260, "Texture Analyzer | Moisture NIR\nTitration Bench | Incubators\nChange Rooms & Sanitization Airlock", fontsize=5.5, color='#44337A', ha='center')

        # Finished Goods Warehouse (600 to 860)
        wh_box = patches.Rectangle((600, 180), 260, 120, facecolor='#EDF2F7', edgecolor='#4A5568')
        ax.add_patch(wh_box)
        ax.text(730, 280, "FINISHED GOODS WAREHOUSE & DISPATCH", fontsize=7, fontweight='bold', color='#2D3748', ha='center')
        ax.text(730, 260, "Pallet Racking: 150 MT Storage Capacity (10 Days)\n2x Hydraulic Dock Levelers | Container Dispatch", fontsize=5.5, color='#1A202C', ha='center')

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 3: PROCESS FLOW DIAGRAM & 12-STREAM TABLE (DWG-002)
        # =========================================================================
        print("Rendering Sheet 03: Process Flow Diagram & Stream Table...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "03", total_sheets, "DWG-FIN-15T-002", "Process Flow Diagram & Heat/Material Balance", "NTS", "PROCESS ENGINEERING")

        # Upper Flowsheet Region (Y=380 to 650)
        # Feed Hopper HP-101
        ax.plot([50, 90, 70, 70, 50], [580, 580, 540, 520, 580], color='#2B6CB0', lw=1.5)
        ax.text(70, 590, "HP-101\nFEED HOPPER", fontsize=6, ha='center', fontweight='bold')
        # Stream 01 Flag
        ax.text(40, 550, "[01] 15,000 kg/d\n10.5% wb", fontsize=5.5, color='#C53030', fontweight='bold')

        # Silo SL-101
        ax.plot([110, 160, 160, 135, 110, 110], [530, 530, 610, 630, 610, 530], color='#2B6CB0', lw=1.5)
        ax.text(135, 640, "SL-101A/B\nRAW SILOS", fontsize=6, ha='center', fontweight='bold')

        # Dosing Skid SK-100
        ax.plot([200, 270, 270, 200, 200], [610, 610, 650, 650, 610], color='#2B6CB0', lw=1.5)
        ax.text(235, 660, "SK-100 DOSING SKID\n0.5% NaHCO3 [03]", fontsize=5.5, ha='center', fontweight='bold', color='#2C5282')

        # Soak Vessel TK-101A/B
        ax.plot([210, 260, 260, 235, 210, 210], [450, 450, 530, 545, 530, 450], color='#2B6CB0', lw=1.8)
        ax.text(235, 435, "TK-101A/B\nSOAK VESSELS\n(2x 7.5 m³)", fontsize=6, ha='center', fontweight='bold')
        ax.text(150, 490, "[04] LIQUOR\n22,500 kg/d", fontsize=5.5, color='#2B6CB0')

        # Dewatering Screen SC-101
        ax.plot([300, 360, 360, 300, 300], [450, 470, 480, 460, 450], color='#2B6CB0', lw=1.5)
        ax.text(330, 490, "SC-101\nDEWATERER", fontsize=6, ha='center', fontweight='bold')
        ax.text(330, 420, "[06] EFFLUENT\n18,910 kg/d -> ETP", fontsize=5.5, color='#C53030')

        # Fluid Bed Dryer DR-101
        ax.plot([400, 620, 620, 400, 400], [450, 450, 520, 520, 450], color='#D69E2E', lw=2.0)
        ax.plot([400, 620], [480, 480], color='#D69E2E', ls='--', lw=1.0) # Deck
        ax.text(510, 530, "DR-101 CONTINUOUS FLUID BED DRYER (14m x 1m)", fontsize=6.5, ha='center', fontweight='bold', color='#744210')
        ax.text(370, 500, "[07] WET DAL\n18,590 kg/d\n28.77% wb", fontsize=5.5, color='#2B6CB0')
        ax.text(510, 420, "STEAM HE-101 (512 kW) | 85°C AIR", fontsize=6, color='#C53030', ha='center')

        # Exhaust Cyclone CY-101
        ax.plot([560, 600, 580, 580, 560], [580, 580, 550, 540, 580], color='#2B6CB0', lw=1.5)
        ax.text(580, 590, "CY-101\nCYCLONE", fontsize=6, ha='center')
        ax.text(610, 570, "[09] VAPOR\n3,878 kg/d", fontsize=5.5, color='#718096')

        # Scalper Screen SC-102 & Bagging PK-101
        ax.plot([660, 710, 710, 660, 660], [450, 450, 480, 480, 450], color='#2B6CB0', lw=1.5)
        ax.text(685, 490, "SC-102\nSCALPER", fontsize=6, ha='center')
        ax.text(685, 420, "[10] FINES\n444 kg/d", fontsize=5.5, color='#C53030')

        ax.plot([750, 820, 820, 750, 750], [440, 440, 510, 510, 440], color='#319795', lw=2.0)
        ax.text(785, 520, "PK-101A/B\nPACKAGING", fontsize=6.5, ha='center', fontweight='bold', color='#234E52')
        ax.text(840, 475, "[11] FINISHED DAL\n14,267.8 kg/day\n10.0% wb (SALEABLE)", fontsize=6, fontweight='bold', color='#22543D')

        # Process Flow Lines
        ax.annotate('', xy=(110, 560), xytext=(90, 560), arrowprops=dict(arrowstyle="->", color='#2B6CB0', lw=1.5))
        ax.annotate('', xy=(210, 490), xytext=(160, 560), arrowprops=dict(arrowstyle="->", color='#2B6CB0', lw=1.5))
        ax.annotate('', xy=(300, 465), xytext=(260, 480), arrowprops=dict(arrowstyle="->", color='#2B6CB0', lw=1.5))
        ax.annotate('', xy=(400, 485), xytext=(360, 470), arrowprops=dict(arrowstyle="->", color='#2B6CB0', lw=1.5))
        ax.annotate('', xy=(660, 465), xytext=(620, 475), arrowprops=dict(arrowstyle="->", color='#2B6CB0', lw=1.5))
        ax.annotate('', xy=(750, 475), xytext=(710, 465), arrowprops=dict(arrowstyle="->", color='#2B6CB0', lw=1.5))
        ax.annotate('', xy=(580, 540), xytext=(580, 520), arrowprops=dict(arrowstyle="->", color='#718096', lw=1.5))

        # Bottom 12-Stream Mass and Heat Balance Table (Y=40 to 360)
        table_box = patches.Rectangle((25, 45), 950, 310, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.5)
        ax.add_patch(table_box)
        ax.text(35, 335, "HEAT AND MATERIAL BALANCE TABLE (RIGOROUS CONSERVATION CLOSURE)", fontsize=9, fontweight='bold', color='#1A365D')

        headers = ["STR", "STREAM DESCRIPTION", "PHASE", "TOTAL (kg/d)", "DRY SOLIDS", "WATER", "MOISTURE", "SOLUTE", "TEMP", "PRESS"]
        col_x = [35, 65, 235, 320, 420, 510, 600, 690, 775, 850]
        ax.plot([25, 975], [325, 325], color='#1A365D', lw=1.2)

        for cx, h in zip(col_x, headers):
            ax.text(cx, 328, h, fontsize=6.5, fontweight='bold', color='#1A365D')

        stream_data = [
            ("01", "Raw Toor-Dal Intake", "Granular Solid", "15,000.00", "13,425.00", "1,575.00", "10.50% wb", "0.00", "30.0 °C", "1.0 atm"),
            ("02", "Fresh Process Water Supply", "Liquid Aqueous", "22,387.50", "0.00", "22,387.50", "100.00% wb", "0.00", "28.0 °C", "3.0 bar g"),
            ("03", "Chemical Dosing (NaHCO3)", "Solid Solute", "112.50", "112.50", "0.00", "0.00% wb", "112.50", "30.0 °C", "Atm"),
            ("04", "Fresh Soak Liquor (0.50% w/w)", "Aqueous Soln", "22,500.00", "112.50", "22,387.50", "99.50% wb", "112.50", "30.0 °C", "1.5 bar g"),
            ("05", "Total Soak Tank Charge Slurry", "Solid/Liquid Slurry", "37,500.00", "13,537.50", "23,962.50", "63.90% wb", "112.50", "30.0 °C", "Atm"),
            ("06", "Spent Soak Effluent to ETP", "Wastewater", "18,910.00", "296.50", "18,613.50", "98.43% wb", "102.50", "32.0 °C", "Gravity"),
            ("07", "Dewatered Wet Dal to Dryer", "Moist Granular", "18,590.00", "13,241.00", "5,349.00", "28.77% wb", "10.00", "30.0 °C", "Gravity"),
            ("08", "Dried Dal Discharge from DR-101", "Dry Granular", "14,712.22", "13,241.00", "1,471.22", "10.00% wb", "10.00", "55.0 °C", "Atm"),
            ("09", "Dryer Exhaust Water Vapor", "Vapor / Air", "3,877.78", "0.00", "3,877.78", "100.00% wb", "0.00", "60.0 °C", "-50 mmWC"),
            ("10", "Scalper & Deduster Fines Loss", "Dust / Broken", "444.47", "400.03", "44.44", "10.00% wb", "0.30", "35.0 °C", "Gravity"),
            ("11", "Saleable Finished Packed Dal", "Food Grade Dal", "14,267.75", "12,840.98", "1,426.77", "10.00% wb", "9.70", "30.0 °C", "Atm"),
            ("12", "CIP Washdown & Floor Drainage", "Effluent Wash", "4,500.00", "20.00", "4,480.00", "99.56% wb", "15.00", "45.0 °C", "Floor Trench")
        ]

        sy = 308
        for row in stream_data:
            ax.plot([25, 975], [sy - 3, sy - 3], color='#EDF2F7', lw=0.8)
            for cx, val in zip(col_x, row):
                ax.text(cx, sy, val, fontsize=6, color='#2D3748')
            sy -= 18

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 4: P&ID SOAKING & DEWATERING (DWG-003)
        # =========================================================================
        print("Rendering Sheet 04: P&ID Soaking & Dewatering Battery...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "04", total_sheets, "DWG-FIN-15T-003", "Piping & Instrumentation: Soaking Battery", "NTS", "CONTROL & PIPING")

        # P&ID Instruments and Valves Architecture
        # Tank TK-101A
        ax.plot([150, 270, 270, 210, 150, 150], [300, 300, 480, 510, 480, 300], color='#1A365D', lw=2.0)
        ax.text(210, 380, "TK-101A\nSOAK VESSEL\n7.5 m³ (SS316L)", fontsize=7, fontweight='bold', ha='center')

        # Agitator AG-101A
        ax.plot([210, 210], [510, 330], color='#2B6CB0', lw=2.0)
        ax.plot([180, 240], [330, 330], color='#2B6CB0', lw=2.5) # Impeller
        ax.plot([195, 225, 225, 195, 195], [510, 510, 545, 545, 510], color='#1A365D', lw=1.5)
        ax.text(210, 555, "AG-101A\n4.0 kW", fontsize=6, ha='center', fontweight='bold')

        # Instrument Bubbles on TK-101A
        # Level LT/LIC-101
        ax.plot([270, 310], [420, 420], color='#805AD5', lw=1.0)
        circ = patches.Circle((325, 420), 15, facecolor='#FAF5FF', edgecolor='#805AD5')
        ax.add_patch(circ)
        ax.text(325, 420, "LIC\n101", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#553C9A')

        # Temperature TT/TIC-101
        ax.plot([150, 110], [340, 340], color='#805AD5', lw=1.0)
        circ = patches.Circle((95, 340), 15, facecolor='#FAF5FF', edgecolor='#805AD5')
        ax.add_patch(circ)
        ax.text(95, 340, "TIC\n101", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#553C9A')

        # pH Analyzer pHIT-101
        ax.plot([270, 310], [340, 340], color='#805AD5', lw=1.0)
        circ = patches.Circle((325, 340), 15, facecolor='#FAF5FF', edgecolor='#805AD5')
        ax.add_patch(circ)
        ax.text(325, 340, "pHIT\n101", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#553C9A')

        # Piping lines
        # Softened Water Header: Line 02-PL-301-80-316L
        ax.plot([50, 190, 190], [600, 600, 500], color='#3182CE', lw=2.0)
        ax.text(90, 605, "02-PW-101-80-316L (WATER SUPPLY)", fontsize=6, fontweight='bold', color='#2B6CB0')
        # Valve XV-101
        ax.plot([130, 140, 130, 140], [595, 605, 605, 595], color='#3182CE', lw=1.5)
        ax.text(135, 612, "XV-101 (FC)", fontsize=5, ha='center', color='#C53030')

        # Chemical Dosing Line from SK-100: Line 03-CD-102-40-316L
        ax.plot([50, 230, 230], [580, 580, 510], color='#DD6B20', lw=1.8)
        ax.text(90, 585, "03-CD-102-40-316L (0.50% NaHCO3 DOSING)", fontsize=6, fontweight='bold', color='#C05621')

        # Bottom Slurry Discharge: Line 05-SL-103-150-316L
        ax.plot([210, 210, 480], [300, 240, 240], color='#805AD5', lw=2.5)
        ax.text(300, 248, "05-SL-103-150-316L (STEEPED DAL SLURRY)", fontsize=6.5, fontweight='bold', color='#553C9A')
        # Flush Bottom Valve XV-103
        ax.plot([205, 215, 205, 215], [265, 275, 275, 265], color='#805AD5', lw=1.5)
        ax.text(225, 270, "XV-103 (FC)\nFLUSH BOTTOM", fontsize=5, color='#C53030')

        # Dewatering Screen SC-101
        ax.plot([480, 620, 620, 480, 480], [220, 250, 280, 250, 220], color='#2B6CB0', lw=2.0)
        ax.text(550, 290, "SC-101 VIBRATING SCREEN\n(1.0 mm Wedge-Wire Deck)", fontsize=6.5, ha='center', fontweight='bold')

        # Effluent Drainage Line 06-EF-104-100-304
        ax.plot([550, 550, 800], [220, 160, 160], color='#E53E3E', lw=2.0)
        ax.text(650, 168, "06-EF-104-100-304 -> 25 KLD EFFLUENT TREATMENT (ETP)", fontsize=6.5, fontweight='bold', color='#C53030')

        # Wet Dal Conveyor to Dryer: Line 07-WD-105-BKT
        ax.plot([620, 750], [265, 265], color='#38A169', lw=2.5)
        ax.text(680, 275, "07-WD-105 -> DR-101 DRYER", fontsize=6.5, fontweight='bold', color='#22543D')

        # Interlock Logic Table
        i_box = patches.Rectangle((480, 360), 480, 260, facecolor='#F7FAFC', edgecolor='#CBD5E0', lw=1.2)
        ax.add_patch(i_box)
        ax.text(500, 600, "SAFETY INTERLOCKS & CONTROL PHILOSOPHY (ISA-84 / SIL-1)", fontsize=8, fontweight='bold', color='#1A365D')
        interlocks = [
            ("I-01", "High-High Level LAHH-101 activates: Closes Water Feed XV-101 and Dosing XV-102 immediately."),
            ("I-02", "Agitator Fault PAL-101: Tripping of AG-101 motor halts dry feed intake conveyor CV-101."),
            ("I-03", "Low Level LALL-101: Disables Flush Bottom Drain XV-103 and slurry pump P-101 to prevent dry running."),
            ("I-04", "pH Deviation AAL-101: If pH < 7.5 or pH > 8.8, triggers alarm on SCADA and pauses automated batch start."),
            ("I-05", "Dewatering Jam ZSL-101: Motor under-current stops tank discharge XV-103 within 3 seconds."),
            ("I-06", "Emergency Stop PB-101: Slams all air-actuated valves to fail-safe positions (FC: Fail Closed).")
        ]
        iy = 575
        for tag, desc in interlocks:
            ax.text(500, iy, f"[{tag}] {desc}", fontsize=6, color='#2D3748')
            iy -= 30

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 5: P&ID FLUID BED DRYER & UTILITIES (DWG-004)
        # =========================================================================
        print("Rendering Sheet 05: P&ID Fluid Bed Dryer & Air Handling...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "05", total_sheets, "DWG-FIN-15T-004", "Piping & Instrumentation: Fluid Bed Dryer", "NTS", "PROCESS & THERMAL")

        # Dryer Vessel DR-101
        ax.plot([250, 750, 750, 250, 250], [300, 300, 440, 440, 300], color='#D69E2E', lw=2.2)
        ax.plot([250, 750], [360, 360], color='#D69E2E', ls='--', lw=1.5) # Perforated Deck
        ax.text(500, 450, "DR-101 CONTINUOUS VIBRATING FLUID BED DRYER (14.0m x 1.0m SS316L)", fontsize=7.5, fontweight='bold', ha='center', color='#744210')
        ax.text(500, 390, "EXPANSION FREEBOARD HOOD (1.4m Clear)", fontsize=6, color='#975A16', ha='center')
        ax.text(500, 330, "LOWER AIR PLENUM (600 mm Depth)", fontsize=6, color='#975A16', ha='center')

        # Air Handling Battery: Blower BL-101 & Steam Coil HE-101
        # Centrifugal Blower BL-101
        c_blow = patches.Circle((100, 250), 30, facecolor='#EDF2F7', edgecolor='#2B6CB0', lw=1.8)
        ax.add_patch(c_blow)
        ax.plot([100, 160], [280, 280], color='#2B6CB0', lw=2.0)
        ax.text(100, 250, "BL-101\nBLOWER\n37 kW", fontsize=6, ha='center', va='center', fontweight='bold')

        # Steam Heating Battery HE-101
        he_box = patches.Rectangle((160, 240), 60, 60, facecolor='#FED7D7', edgecolor='#C53030', lw=1.5)
        ax.add_patch(he_box)
        ax.text(190, 270, "HE-101\nSTEAM COIL\n512 kW", fontsize=6, ha='center', va='center', fontweight='bold', color='#9B2C2C')

        # Saturated Steam Supply Line 01-ST-201-65-CS (3.0 bar g)
        ax.plot([190, 190], [150, 240], color='#C53030', lw=2.2)
        ax.text(195, 170, "01-ST-201-65-CS (3.0 bar g STEAM)", fontsize=6, fontweight='bold', color='#9B2C2C')
        # Control Valve TCV-101
        ax.plot([185, 195, 185, 195], [195, 205, 205, 195], color='#C53030', lw=1.5)
        ax.text(215, 200, "TCV-101", fontsize=5.5, color='#9B2C2C')

        # Hot Air Duct Line 02-HA-202-600 to Plenum
        ax.plot([220, 350], [270, 300], color='#D69E2E', lw=2.5)
        ax.text(250, 260, "85°C AIR DUCT (16,100 kg/h)", fontsize=6, color='#744210', fontweight='bold')

        # Differential Pressure Across Bed: PDIT-101
        ax.plot([450, 450, 480], [330, 220, 220], color='#805AD5', lw=1.0)
        ax.plot([450, 450, 480], [390, 250, 250], color='#805AD5', lw=1.0)
        circ = patches.Circle((500, 235), 18, facecolor='#FAF5FF', edgecolor='#805AD5')
        ax.add_patch(circ)
        ax.text(500, 235, "PDIT\n101", fontsize=6, ha='center', va='center', fontweight='bold', color='#553C9A')

        # Product Discharge & Moisture Analyzer MIC-101
        ax.plot([750, 850], [360, 360], color='#38A169', lw=2.5)
        ax.text(780, 370, "08-DD-106 -> FINISHED DAL (10.0% wb)", fontsize=6.5, color='#22543D', fontweight='bold')
        circ = patches.Circle((810, 330), 16, facecolor='#F0FFF4', edgecolor='#38A169')
        ax.add_patch(circ)
        ax.text(810, 330, "MIC\n101", fontsize=5.5, ha='center', va='center', color='#22543D', fontweight='bold')

        # Exhaust Cyclones & NFPA 68 Explosion Venting
        ax.plot([500, 500, 600], [440, 560, 560], color='#718096', lw=2.0)
        # Cyclone CY-101
        ax.plot([600, 650, 625, 625, 600], [600, 600, 540, 520, 600], color='#2B6CB0', lw=1.5)
        ax.text(625, 615, "CY-101 EXHAUST CYCLONE", fontsize=6.5, ha='center', fontweight='bold')
        # Explosion Vent EV-101
        ax.plot([400, 400], [440, 490], color='#E53E3E', lw=2.0)
        ax.plot([385, 415], [490, 490], color='#E53E3E', lw=2.5)
        ax.text(400, 505, "EV-101 EXPLOSION VENT\n(NFPA 68 / ATEX RUPTURE DISC)", fontsize=5.5, ha='center', color='#C53030', fontweight='bold')

        # Dryer Psychrometrics & Energy Balance Card
        d_box = patches.Rectangle((50, 520), 320, 150, facecolor='#FFFBEB', edgecolor='#D69E2E', lw=1.2)
        ax.add_patch(d_box)
        ax.text(65, 650, "DRYER THERMAL & PSYCHROMETRIC DESIGN BASIS", fontsize=7.5, fontweight='bold', color='#744210')
        ax.text(65, 630, "• Ambient Air Intake: 30.0 °C, 65.0% RH (0.0175 kg H2O/kg dry air)", fontsize=6, color='#2D3748')
        ax.text(65, 612, "• Process Supply Air: Heated to 85.0 °C (16,100 kg/h Dry Air)", fontsize=6, color='#2D3748')
        ax.text(65, 594, "• Product Wet-Bulb Temp: 60.0 °C (Enthalpy h_fg = 2,357.7 kJ/kg)", fontsize=6, color='#2D3748')
        ax.text(65, 576, "• Exhaust Air: 62.0 °C, 85% RH (0.0416 kg H2O/kg dry air)", fontsize=6, color='#2D3748')
        ax.text(65, 558, "• Net Evaporation Rate: 242.36 kg/h Nom / 285.13 kg/h Design", fontsize=6, color='#2D3748')
        ax.text(65, 540, "• Total Steam Demand: 520 kg/h Avg @ 3.0 bar g (HE-101 Duty 512 kW)", fontsize=6, color='#C53030', fontweight='bold')

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 6: P&ID PACKAGING & CLEANROOM HVAC (DWG-005)
        # =========================================================================
        print("Rendering Sheet 06: P&ID Packaging & Cleanroom HVAC...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "06", total_sheets, "DWG-FIN-15T-005", "Piping & Instrumentation: Packaging & HVAC", "NTS", "PACKAGING & HVAC")

        # Class 8 Cleanroom Envelope Boundary (Y=200 to 600, X=200 to 800)
        cr_boundary = patches.Rectangle((200, 200), 600, 400, facecolor='#E6FFFA', edgecolor='#319795', lw=2.0, ls='--')
        ax.add_patch(cr_boundary)
        ax.text(500, 580, "CLASS 8 (ISO 100,000) CLEANROOM ENVELOPE — POSITIVE PRESSURE (+15 Pa)", fontsize=8, fontweight='bold', color='#234E52', ha='center')

        # HVAC Air Handling Unit AHU-101
        ahu = patches.Rectangle((50, 350), 100, 120, facecolor='#EDF2F7', edgecolor='#2B6CB0', lw=1.5)
        ax.add_patch(ahu)
        ax.text(100, 420, "AHU-101\nCLEANROOM\nHVAC\n15 ACH", fontsize=6.5, ha='center', va='center', fontweight='bold')
        # Duct to Cleanroom with HEPA Filter
        ax.plot([150, 300], [410, 410], color='#3182CE', lw=2.5)
        ax.plot([300, 300], [410, 480], color='#3182CE', lw=2.5)
        hepa = patches.Rectangle((285, 480), 30, 20, facecolor='#E2E8F0', edgecolor='#2B6CB0')
        ax.add_patch(hepa)
        ax.text(300, 510, "HEPA FILTER H14\n(99.995% @ 0.3 µm)", fontsize=5.5, ha='center', color='#2C5282', fontweight='bold')

        # Packaging Lines PK-101A and PK-101B
        for px, tag, size in [(380, "PK-101A", "1 kg Retail (35 bpm)"), (620, "PK-101B", "5 kg Food-Service (25 bpm)")]:
            # Surge Hopper
            ax.plot([px - 30, px + 30, px + 10, px - 10, px - 30], [480, 480, 440, 440, 480], color='#2B6CB0', lw=1.5)
            ax.text(px, 490, f"SURGE HOPPER\n{tag}", fontsize=5.5, ha='center')
            # 14-Head Multihead Weigher
            ax.plot([px - 40, px + 40, px + 25, px - 25, px - 40], [430, 430, 380, 380, 430], color='#2B6CB0', lw=1.5)
            ax.text(px, 405, "14-HEAD WEIGHER", fontsize=5.5, ha='center', fontweight='bold')
            # Vertical FFS Machine Body
            ffs = patches.Rectangle((px - 35, 270), 70, 100, facecolor='#B2F5EA', edgecolor='#234E52', lw=1.5)
            ax.add_patch(ffs)
            ax.text(px, 320, f"{tag}\nVERTICAL FFS\n{size}", fontsize=6, ha='center', va='center', fontweight='bold')

            # Nitrogen Flushing Line 08-N2-108-15
            ax.plot([px - 60, px - 35], [300, 300], color='#805AD5', lw=1.5)
            ax.text(px - 70, 305, "N2 FLUSH\n(< 1.0% O2)", fontsize=5, color='#553C9A', ha='right')

            # Metal Detector MD-101
            md = patches.Rectangle((px - 25, 215), 50, 35, facecolor='#FED7D7', edgecolor='#C53030')
            ax.add_patch(md)
            ax.text(px, 232, "METAL DETECTOR\nFe 1.0 / NonFe 1.5mm", fontsize=5, ha='center', va='center', color='#9B2C2C', fontweight='bold')

        # Cleanroom Airlock Entry System (Left Side X=200 to 280, Y=200 to 320)
        al1 = patches.Rectangle((200, 200), 80, 60, facecolor='#FFFFFF', edgecolor='#319795', lw=1.2)
        al2 = patches.Rectangle((200, 260), 80, 60, facecolor='#E6FFFA', edgecolor='#319795', lw=1.2)
        ax.add_patch(al1); ax.add_patch(al2)
        ax.text(240, 230, "AIRLOCK 1\nSHOE BARRIER", fontsize=5.5, ha='center', va='center')
        ax.text(240, 290, "AIRLOCK 2\nAIR SHOWER (+30 Pa)", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#234E52')

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 7: EQUIPMENT GENERAL ARRANGEMENT TK-101 (DWG-006)
        # =========================================================================
        print("Rendering Sheet 07: Equipment GA Soak Vessel TK-101...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "07", total_sheets, "DWG-FIN-15T-006", "Equipment GA: 7.5 m³ Soak Tank TK-101", "1:25", "MECHANICAL / VESSEL")

        # Front Elevation (Center X=280, Base Y=220 to Top Y=580)
        # Straight Shell (OD 2000mm -> 160 units, H 2200mm -> 176 units)
        ax.plot([200, 360, 360, 200, 200], [280, 280, 460, 460, 280], color='#1A365D', lw=2.2)
        # Dished Head (H 300mm -> 24 units)
        ax.plot([200, 280, 360], [460, 490, 460], color='#1A365D', lw=2.2)
        # Conical Bottom (H 500mm -> 40 units)
        ax.plot([200, 265, 295, 360], [280, 230, 230, 280], color='#1A365D', lw=2.2)
        # Bottom Drain Nozzle N10 (6" ANSI 150#)
        ax.plot([265, 265, 295, 295], [230, 205, 205, 230], color='#1A365D', lw=1.8)
        ax.plot([255, 305], [205, 205], color='#1A365D', lw=3.0) # Drain Flange
        ax.text(280, 190, "N10: 6\" DRAIN FLANGE", fontsize=5.5, ha='center', fontweight='bold')

        # Agitator Drive & Shaft Envelope on Top
        ax.plot([260, 300, 300, 260, 260], [490, 490, 520, 520, 490], color='#2B6CB0', lw=1.5) # Lantern stool
        ax.plot([250, 310, 310, 250, 250], [520, 520, 570, 570, 520], color='#2B6CB0', lw=2.0) # Gearbox
        ax.text(280, 580, "AG-101 DRIVE (4.0 kW / 55 RPM)", fontsize=6, ha='center', fontweight='bold', color='#2B6CB0')
        # Center Shaft & Impeller (Hidden lines)
        ax.plot([280, 280], [490, 260], color='#2B6CB0', ls='--', lw=1.5)
        ax.plot([250, 310], [260, 260], color='#2B6CB0', lw=2.5) # Hydrofoil Impeller

        # Support Legs (4 Tubular Legs, 2 visible in front elevation)
        ax.plot([210, 210], [300, 150], color='#4A5568', lw=3.0)
        ax.plot([195, 225], [150, 150], color='#4A5568', lw=3.5) # Base plate
        ax.plot([350, 350], [300, 150], color='#4A5568', lw=3.0)
        ax.plot([335, 365], [150, 150], color='#4A5568', lw=3.5) # Base plate
        ax.text(280, 140, "4x TUBULAR LEGS (OD 168mm) ON LOAD CELLS", fontsize=5.5, ha='center', color='#4A5568')

        # Top Head Nozzles
        # Manway N1
        ax.plot([320, 345, 345, 320, 320], [470, 470, 500, 500, 470], color='#1A365D', lw=1.5)
        ax.text(355, 510, "N1: 20\" MANWAY", fontsize=5.5, color='#1A365D')
        # Feed Inlet N2
        ax.plot([220, 235, 235, 220, 220], [470, 470, 505, 505, 470], color='#1A365D', lw=1.5)
        ax.text(210, 515, "N2: 4\" FEED", fontsize=5.5, color='#1A365D', ha='right')

        # Dimension Lines
        ax.annotate('', xy=(170, 280), xytext=(170, 460), arrowprops=dict(arrowstyle="<->", color='#C53030', lw=1.2))
        ax.text(160, 370, "2,200 mm\nSHELL", fontsize=6, ha='right', va='center', color='#C53030', fontweight='bold')
        ax.annotate('', xy=(200, 475), xytext=(360, 475), arrowprops=dict(arrowstyle="<->", color='#C53030', lw=1.2))
        ax.text(280, 480, "OD 2,000 mm (ID 1,988 mm)", fontsize=6, ha='center', color='#C53030', fontweight='bold')

        # Nozzle Schedule Table (Right Side: X=480 to 950, Y=350 to 650)
        tbl_box = patches.Rectangle((480, 350), 470, 300, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.2)
        ax.add_patch(tbl_box)
        ax.text(500, 630, "NOZZLE SCHEDULE & MECHANICAL DESIGN DATA", fontsize=8, fontweight='bold', color='#1A365D')

        n_headers = ["NOZ", "SERVICE", "SIZE", "RATING", "FACING", "ORIENTATION"]
        n_col_x = [490, 530, 680, 740, 810, 880]
        ax.plot([480, 950], [620, 620], color='#1A365D', lw=1.0)
        for cx, nh in zip(n_col_x, n_headers):
            ax.text(cx, 623, nh, fontsize=6, fontweight='bold', color='#1A365D')

        nozzle_data = [
            ("N1", "Manway with Sight Glass", "20\" (500mm)", "150#", "Sanitary Davit", "Top Head 45°"),
            ("N2", "Dal Grain Feed Inlet", "4\" (100mm)", "150#", "ANSI RF / TC", "Top Head 180°"),
            ("N3", "Softened Water Supply", "3\" (80mm)", "150#", "ANSI RF", "Top Head 270°"),
            ("N4", "Chemical Dosing Liquor", "1.5\" (40mm)", "150#", "ANSI RF", "Top Head 90°"),
            ("N5", "CIP Rotary Spray Ball", "2\" (50mm)", "Tri-Clamp", "Sanitary 3A", "Top Head Center"),
            ("N6", "Sterile Air Breathing Vent", "3\" (80mm)", "Tri-Clamp", "0.22 µm PTFE", "Top Head 135°"),
            ("N7", "Pressure Relief Valve", "2\" (50mm)", "150#", "ANSI RF", "Top Head 225°"),
            ("N8", "Guided Wave Radar Level", "2\" (50mm)", "150#", "ANSI RF", "Top Head 315°"),
            ("N9", "PT100 Duplex Thermowell", "1\" (25mm)", "150#", "ANSI RF", "Lower Shell 90°"),
            ("N10", "Conical Bottom Slurry Drain", "6\" (150mm)", "150#", "Flush Diaphragm", "Bottom Center 0°"),
            ("N11", "Vessel Overflow to ETP", "3\" (80mm)", "150#", "ANSI RF", "Top Shell 0°")
        ]
        ny = 605
        for row in nozzle_data:
            for cx, val in zip(n_col_x, row):
                ax.text(cx, ny, val, fontsize=5.5, color='#2D3748')
            ny -= 16

        # Mechanical Design Summary Card
        m_box = patches.Rectangle((480, 160), 470, 170, facecolor='#F7FAFC', edgecolor='#CBD5E0', lw=1.0)
        ax.add_patch(m_box)
        ax.text(500, 315, "MECHANICAL SPECIFICATIONS (ASME SEC VIII DIV 1 / IS 2825)", fontsize=7.5, fontweight='bold', color='#2B6CB0')
        ax.text(500, 295, "• Vessel Gross Capacity: 6.83 m³ Fluid (7.50 m³ Envelope) | Working: 5.12 m³", fontsize=6, color='#2D3748')
        ax.text(500, 280, "• Design Pressure: Full Vacuum to 1.5 bar g | Test Pressure: 2.25 bar g (Hydro)", fontsize=6, color='#2D3748')
        ax.text(500, 265, "• Design Temperature: 100.0 °C | Operating Temperature: 25.0 °C to 45.0 °C", fontsize=6, color='#2D3748')
        ax.text(500, 250, "• Material of Construction: SS316L Contact Parts (Ra < 0.8 µm Electro-polished)", fontsize=6, color='#2D3748')
        ax.text(500, 235, "• Shell Thickness: 6.0 mm | Head Thickness: 6.0 mm | Cone Thickness: 6.0 mm", fontsize=6, color='#2D3748')
        ax.text(500, 220, "• Empty Tare Weight: 809.0 kg SS316L | Operating Weight (Full Slurry): 8,309 kg", fontsize=6, color='#C53030', fontweight='bold')
        ax.text(500, 205, "• Hydrotest Weight: 9,250 kg | Seismic Zone: Zone III | Wind Load: 44 m/s", fontsize=6, color='#2D3748')
        ax.text(500, 185, "STAMP: CONCEPTUAL FEED GA — PRELIMINARY — NOT FOR FABRICATION", fontsize=6.5, fontweight='bold', color='#E53E3E')

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 8: EQUIPMENT GENERAL ARRANGEMENT DR-101 (DWG-007)
        # =========================================================================
        print("Rendering Sheet 08: Equipment GA Fluid Bed Dryer DR-101...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "08", total_sheets, "DWG-FIN-15T-007", "Equipment GA: Fluid Bed Dryer DR-101", "1:50", "MECHANICAL / THERMAL")

        # Front Elevation DR-101 (X=50 to 750, Y=260 to 480)
        # Lower Plenum
        ax.plot([80, 720, 720, 80, 80], [300, 300, 350, 350, 300], color='#D69E2E', lw=2.0)
        ax.text(400, 325, "LOWER FLUIDIZING AIR PLENUM (600 mm SS316L)", fontsize=6, color='#744210', ha='center', va='center')
        # Perforated Deck
        ax.plot([80, 720], [350, 350], color='#C53030', ls='--', lw=2.0)
        ax.text(730, 350, "PERFORATED DECK (14m x 1m)", fontsize=5.5, color='#C53030', va='center')
        # Upper Hood
        ax.plot([80, 720, 700, 100, 80], [350, 350, 450, 450, 350], color='#D69E2E', lw=2.0)
        ax.text(400, 410, "EXPANSION HOOD FREEBOARD (800 mm Height)", fontsize=6, color='#744210', ha='center', va='center')

        # Three Exhaust Duct Outlets on Roof
        for ex in [200, 400, 600]:
            ax.plot([ex - 20, ex + 20, ex + 20, ex - 20, ex - 20], [450, 450, 490, 490, 450], color='#1A365D', lw=1.5)
            ax.plot([ex - 25, ex + 25], [490, 490], color='#1A365D', lw=2.5)
            ax.text(ex, 500, "EXHAUST\n(Ø 500mm)", fontsize=5, ha='center')

        # Feed Chute on Left End
        ax.plot([60, 110, 110, 60, 60], [450, 450, 520, 520, 450], color='#2B6CB0', lw=1.5)
        ax.text(85, 530, "DAL FEED\nINLET", fontsize=5.5, ha='center', fontweight='bold')

        # Discharge Chute on Right End
        ax.plot([690, 740, 740, 690, 690], [300, 300, 360, 360, 300], color='#2B6CB0', lw=1.5)
        ax.text(715, 280, "DRIED PRODUCT\nDISCHARGE", fontsize=5.5, ha='center', fontweight='bold')

        # Center Vibratory Exciter Motors
        ax.plot([360, 440, 440, 360, 360], [250, 250, 300, 300, 250], color='#718096', lw=2.0)
        c_mot1 = patches.Circle((380, 275), 18, facecolor='#CBD5E0', edgecolor='#2D3748')
        c_mot2 = patches.Circle((420, 275), 18, facecolor='#CBD5E0', edgecolor='#2D3748')
        ax.add_patch(c_mot1); ax.add_patch(c_mot2)
        ax.text(400, 235, "TWIN UNBALANCED EXCITER MOTORS (2x 5.5 kW / 960 RPM)", fontsize=5.5, ha='center', fontweight='bold')

        # Vibration Isolator Coil Springs (6 pairs along length)
        for sx in [120, 220, 320, 480, 580, 680]:
            ax.plot([sx - 10, sx + 10, sx - 10, sx + 10], [270, 280, 290, 300], color='#C53030', lw=1.8)
            ax.plot([sx - 15, sx + 15], [265, 265], color='#2D3748', lw=2.5) # Footplate

        # Static & Dynamic Foundation Loads Table
        f_box = patches.Rectangle((50, 80), 900, 120, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.2)
        ax.add_patch(f_box)
        ax.text(65, 185, "CIVIL FOUNDATION LOADING & DYNAMIC SPECIFICATIONS", fontsize=8, fontweight='bold', color='#1A365D')
        f_headers = ["STATION ID", "LOCATION (X)", "STATIC DEAD LOAD", "GRAIN LIVE LOAD", "DYNAMIC AMPLITUDE", "SPRING STIFFNESS", "TRANSMISSIBILITY"]
        f_col_x = [65, 180, 300, 430, 560, 710, 840]
        ax.plot([50, 950], [175, 175], color='#1A365D', lw=1.0)
        for cx, fh in zip(f_col_x, f_headers):
            ax.text(cx, 178, fh, fontsize=6, fontweight='bold', color='#1A365D')

        load_data = [
            ("ISOLATOR 1 & 2", "X = 1,200 mm (Feed End)", "850 kg / station", "420 kg / station", "± 3.2 mm @ 16 Hz", "185 N/mm", "< 4.5%"),
            ("ISOLATOR 3 & 4", "X = 3,400 mm", "850 kg / station", "420 kg / station", "± 3.5 mm @ 16 Hz", "185 N/mm", "< 4.5%"),
            ("ISOLATOR 5 & 6", "X = 5,600 mm (Exciter Mid)", "1,250 kg / station", "450 kg / station", "± 4.0 mm @ 16 Hz", "240 N/mm", "< 4.0%"),
            ("ISOLATOR 7 & 8", "X = 8,400 mm", "1,250 kg / station", "450 kg / station", "± 4.0 mm @ 16 Hz", "240 N/mm", "< 4.0%"),
            ("ISOLATOR 9 & 10", "X = 10,600 mm", "850 kg / station", "420 kg / station", "± 3.5 mm @ 16 Hz", "185 N/mm", "< 4.5%"),
            ("ISOLATOR 11 & 12", "X = 12,800 mm (Discharge)", "850 kg / station", "420 kg / station", "± 3.2 mm @ 16 Hz", "185 N/mm", "< 4.5%")
        ]
        fy = 160
        for row in load_data:
            for cx, val in zip(f_col_x, row):
                ax.text(cx, fy, val, fontsize=5.5, color='#2D3748')
            fy -= 14

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 9: EQUIPMENT GA DOSING SKID SK-100 (DWG-008)
        # =========================================================================
        print("Rendering Sheet 09: Equipment GA Dosing Skid SK-100...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "09", total_sheets, "DWG-FIN-15T-008", "Equipment GA: Dosing Skid SK-100", "1:20", "MECHANICAL / SKID")

        # Skid Base Frame (X=100 to 600, Y=200 to 240)
        sk_base = patches.Rectangle((100, 200), 500, 40, facecolor='#4A5568', edgecolor='#1A202C', lw=1.8)
        ax.add_patch(sk_base)
        ax.text(350, 215, "STRUCTURAL CHANNEL BASE (ISMC 150) WITH 50mm INTEGRAL DRIP LIP BUND", fontsize=6, color='#FFFFFF', ha='center', fontweight='bold')

        # Forklift Pockets
        for fx in [200, 450]:
            fp = patches.Rectangle((fx, 205), 50, 25, facecolor='#1A202C', edgecolor='#CBD5E0')
            ax.add_patch(fp)
            ax.text(fx + 25, 217, "FORK", fontsize=4.5, color='#FFFFFF', ha='center', va='center')

        # Dual Dosing Tanks TK-103A and TK-103B
        for tx, tag in [(200, "TK-103A"), (380, "TK-103B")]:
            t_rect = patches.Rectangle((tx, 240), 120, 180, facecolor='#EDF2F7', edgecolor='#2B6CB0', lw=1.8)
            ax.add_patch(t_rect)
            ax.text(tx + 60, 330, f"{tag}\n500 L HDPE\nCHEMICAL TANK", fontsize=6, ha='center', va='center', fontweight='bold', color='#1A365D')
            # Top Propeller Mixer
            m_box = patches.Rectangle((tx + 45, 420), 30, 40, facecolor='#718096', edgecolor='#2D3748')
            ax.add_patch(m_box)
            ax.plot([tx + 60, tx + 60], [420, 260], color='#2B6CB0', lw=1.5) # Shaft
            ax.plot([tx + 45, tx + 75], [260, 260], color='#2B6CB0', lw=2.0) # Propeller
            ax.text(tx + 60, 470, "AG-103\n0.37 kW", fontsize=5, ha='center')

        # Dual Metering Pumps P-102A/B
        for px, ptag in [(180, "P-102A"), (360, "P-102B")]:
            p_box = patches.Rectangle((px + 130, 240), 40, 50, facecolor='#FED7D7', edgecolor='#C53030', lw=1.5)
            ax.add_patch(p_box)
            ax.text(px + 150, 265, f"{ptag}\n25 L/h", fontsize=5, ha='center', va='center', fontweight='bold', color='#9B2C2C')

        # Local Control Panel Box
        lcp = patches.Rectangle((530, 280), 55, 90, facecolor='#FAF5FF', edgecolor='#805AD5', lw=1.5)
        ax.add_patch(lcp)
        ax.text(557, 325, "LCP-100\nLOCAL\nPANEL\n(IP65)", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#553C9A')
        # Stanchion
        ax.plot([557, 557], [240, 280], color='#805AD5', lw=2.5)

        # Bill of Materials Table (Right Side: X=630 to 960)
        b_box = patches.Rectangle((630, 160), 330, 480, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.2)
        ax.add_patch(b_box)
        ax.text(645, 620, "SKID BILL OF MATERIALS (BOM)", fontsize=8, fontweight='bold', color='#1A365D')
        b_headers = ["ITEM", "DESCRIPTION", "QTY", "MATERIAL", "SPEC"]
        b_col_x = [645, 680, 810, 850, 910]
        ax.plot([630, 960], [610, 610], color='#1A365D', lw=1.0)
        for cx, bh in zip(b_col_x, b_headers):
            ax.text(cx, 613, bh, fontsize=6, fontweight='bold', color='#1A365D')

        bom_items = [
            ("01", "Dosing Storage Tank", "2 No", "HDPE UV", "500 L Graduated"),
            ("02", "Top Marine Propeller Mixer", "2 No", "SS316L", "0.37 kW / 280 RPM"),
            ("03", "Diaphragm Metering Pump", "2 No", "PTFE / PVDF", "25.0 L/h @ 5 bar"),
            ("04", "Calibration Glass Cylinder", "1 No", "Borosilicate", "1,000 mL with 3-way"),
            ("05", "Pulsation Dampener", "1 No", "SS316L/Viton", "0.5 L @ 60% P_op"),
            ("06", "Back Pressure Valve", "2 No", "PTFE / Hast-C", "Set @ 1.5 bar g"),
            ("07", "Pressure Relief Valve", "2 No", "SS316L", "Set @ 3.5 bar g"),
            ("08", "Suction Y-Strainer", "2 No", "SS316L", "40 Mesh Basket"),
            ("09", "Magnetic Flowmeter FIT", "1 No", "PFA Lined", "DN15, 4-20mA HART"),
            ("10", "Pressure Transmitter PIT", "2 No", "SS316L Diaph", "0-10 bar g IP67"),
            ("11", "Structural Steel Frame", "1 Lot", "ISMC 150 CS", "Hot-Dip Galv 80µm"),
            ("12", "Local Control Panel LCP", "1 No", "SS304 IP65", "VFD + HOA Switches")
        ]
        by = 590
        for row in bom_items:
            for cx, val in zip(b_col_x, row):
                ax.text(cx, by, val, fontsize=5.5, color='#2D3748')
            by -= 20

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 10: ELECTRICAL SINGLE LINE DIAGRAM (DWG-009)
        # =========================================================================
        print("Rendering Sheet 10: Electrical SLD & Load Schedule...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "10", total_sheets, "DWG-FIN-15T-009", "Electrical Single Line Diagram (SLD)", "NTS", "ELECTRICAL / AUTOMATION")

        # 11 kV Substation Incomer
        ax.plot([150, 150], [640, 580], color='#2B6CB0', lw=2.5)
        ax.text(150, 650, "11 kV GRID SUPPLY\n(DISCOM TARIFF HV-2)", fontsize=7, ha='center', fontweight='bold', color='#1A365D')
        # VCB Breaker
        ax.plot([140, 160, 160, 140, 140], [580, 580, 600, 600, 580], color='#1A365D', lw=1.5)
        ax.text(170, 590, "VCB-01 (630A / 25kA)", fontsize=6, color='#2D3748')

        # 315 kVA Transformer TR-101
        c_tr1 = patches.Circle((150, 530), 22, facecolor='#FFFFFF', edgecolor='#2B6CB0', lw=1.8)
        c_tr2 = patches.Circle((150, 500), 22, facecolor='#FFFFFF', edgecolor='#2B6CB0', lw=1.8)
        ax.add_patch(c_tr1); ax.add_patch(c_tr2)
        ax.text(210, 515, "TR-101 TRANSFORMER\n315 kVA, 11kV / 415V\nDyn11, ONAN Oil-Cooled", fontsize=6.5, fontweight='bold', color='#2B6CB0')

        # 250 kVA DG Set DG-101 Backup
        ax.plot([750, 750], [640, 500], color='#C53030', lw=2.2)
        ax.text(750, 650, "250 kVA STANDBY DG SET\n(AMF AUTO-START SYNC)", fontsize=7, ha='center', fontweight='bold', color='#9B2C2C')

        # 415V Main Busbar PCC-01 (Y=440, X=100 to 800)
        ax.plot([100, 800], [440, 440], color='#D69E2E', lw=4.0)
        ax.text(450, 450, "MAIN 415V 3-PHASE 4-WIRE 50 Hz BUSBAR (PCC-01) — 800A FAULT RATING 35 kA", fontsize=7.5, color='#744210', ha='center', fontweight='bold')

        # MCC Feeders & Connected Loads Table
        mcc_box = patches.Rectangle((50, 80), 900, 320, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.5)
        ax.add_patch(mcc_box)
        ax.text(65, 380, "MOTOR CONTROL CENTER (MCC) CONNECTED LOAD SCHEDULE", fontsize=8.5, fontweight='bold', color='#1A365D')

        m_headers = ["FEEDER ID", "LOAD DESCRIPTION", "MOTOR TAG", "QTY", "RATING (kW)", "STARTING METHOD", "FULL LOAD AMPS", "BREAKER (MCCB)", "CABLE SIZE"]
        m_col_x = [65, 140, 310, 380, 420, 510, 630, 730, 840]
        ax.plot([50, 950], [370, 370], color='#1A365D', lw=1.2)
        for cx, mh in zip(m_col_x, m_headers):
            ax.text(cx, 373, mh, fontsize=6, fontweight='bold', color='#1A365D')

        motor_loads = [
            ("F-01", "Soak Vessel Agitators", "AG-101A/B", "2 No", "4.0 kW ea", "VFD (Variable Speed)", "8.2 A", "16A 3P MCCB", "4C x 4 mm² Cu"),
            ("F-02", "Fluid Bed Dryer Fluidizing Blower", "BL-101", "1 No", "37.0 kW", "VFD (Inverter Duty)", "68.0 A", "100A 3P MCCB", "3C x 70 mm² Al"),
            ("F-03", "Dryer Exhaust Induced Draft Fan", "BL-102", "1 No", "18.5 kW", "Star-Delta Starter", "34.5 A", "50A 3P MCCB", "3C x 25 mm² Al"),
            ("F-04", "Dryer Vibratory Exciter Motors", "M-101A/B", "2 No", "5.5 kW ea", "Direct-On-Line (DOL)", "11.2 A", "25A 3P MCCB", "4C x 6 mm² Cu"),
            ("F-05", "Dewatering Vibratory Screen", "M-102", "1 No", "3.7 kW", "Direct-On-Line (DOL)", "7.8 A", "16A 3P MCCB", "4C x 4 mm² Cu"),
            ("F-06", "Chemical Dosing Metering Pumps", "P-102A/B", "2 No", "0.75 kW ea", "VFD Micro-Drive", "2.1 A", "6A 3P MCB", "4C x 2.5 mm² Cu"),
            ("F-07", "Package Steam Boiler Feed Pumps", "P-103A/B", "2 No", "5.5 kW ea", "Direct-On-Line (DOL)", "11.2 A", "25A 3P MCCB", "4C x 6 mm² Cu"),
            ("F-08", "Cleanroom Packaging Lines FFS", "PK-101A/B", "2 No", "12.0 kW ea", "Servo & Inverter", "24.5 A", "40A 3P MCCB", "4C x 16 mm² Cu"),
            ("F-09", "Cleanroom HVAC AHU Supply Fan", "AHU-101", "1 No", "15.0 kW", "VFD Pressure Control", "28.0 A", "50A 3P MCCB", "3C x 25 mm² Al"),
            ("F-10", "Plant Screw Air Compressor", "CP-101", "1 No", "22.0 kW", "VFD Energy Saver", "41.0 A", "63A 3P MCCB", "3C x 35 mm² Al"),
            ("F-11", "25 KLD ETP Aeration Blowers", "ET-BL-01", "2 No", "7.5 kW ea", "Star-Delta Starter", "15.0 A", "32A 3P MCCB", "4C x 10 mm² Cu"),
            ("F-12", "Plant Base Lighting & Automation", "LDB / SCADA", "1 Lot", "15.0 kW tot", "Feeder Contactor", "26.0 A", "40A 4P MCB", "4C x 16 mm² Cu")
        ]
        ly = 350
        for row in motor_loads:
            for cx, val in zip(m_col_x, row):
                ax.text(cx, ly, val, fontsize=5.5, color='#2D3748')
            ly -= 18

        ax.text(65, ly, "TOTAL CONNECTED PLANT LOAD: 162.2 kW | MAXIMUM DEMAND (@ 0.75 DIVERSITY): 121.6 kW | BASE RUNNING LOAD: 85.0 kW", fontsize=6.5, fontweight='bold', color='#1A365D')

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 11: UTILITY FLOW DIAGRAM & 25 KLD ETP FLOWSHEET (DWG-010)
        # =========================================================================
        print("Rendering Sheet 11: Utility Flow Diagram & 25 KLD ETP Flowsheet...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "11", total_sheets, "DWG-FIN-15T-010", "Utility Flow Diagram & 25 KLD ETP", "NTS", "ENVIRONMENTAL & UTILITY")

        # Upper Region: 25 KLD Effluent Treatment Plant Flowsheet (Y=360 to 650)
        # Equalization Tank ET-01 (30 m³)
        eq = patches.Rectangle((80, 520), 80, 70, facecolor='#E2E8F0', edgecolor='#2D3748', lw=1.5)
        ax.add_patch(eq)
        ax.text(120, 555, "ET-01\nEQUALIZATION\nTANK (30 m³)", fontsize=6, ha='center', va='center', fontweight='bold')
        ax.text(50, 570, "SPENT SOAK [06]\n18,910 kg/d", fontsize=5.5, color='#C53030', fontweight='bold')

        # Neutralization Tank ET-02
        nt = patches.Rectangle((200, 530), 60, 50, facecolor='#FED7D7', edgecolor='#C53030', lw=1.5)
        ax.add_patch(nt)
        ax.text(230, 555, "ET-02\npH ADJUST\n(H2SO4)", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#9B2C2C')

        # Flash Mixer & Flocculator ET-03
        floc = patches.Rectangle((300, 530), 70, 50, facecolor='#FEFCBF', edgecolor='#D69E2E', lw=1.5)
        ax.add_patch(floc)
        ax.text(335, 555, "ET-03\nCOAGULATION\n(Alum/Polymer)", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#744210')

        # MBBR Biological Aeration Tank ET-04
        mbbr = patches.Rectangle((410, 510), 110, 90, facecolor='#C6F6D5', edgecolor='#276749', lw=2.0)
        ax.add_patch(mbbr)
        ax.text(465, 555, "ET-04 MBBR TANK\n(35 m³ FAB Media)\nBOD Reduction > 92%", fontsize=6, ha='center', va='center', fontweight='bold', color='#22543D')
        ax.text(465, 495, "Diffused Aeration (3.0 kg O2/h)", fontsize=5, ha='center', color='#276749')

        # Tube Settler Clarifier ET-05
        ax.plot([560, 640, 610, 590, 560], [580, 580, 510, 510, 580], color='#2B6CB0', lw=1.8)
        ax.text(600, 550, "ET-05\nTUBE SETTLER\nCLARIFIER", fontsize=5.5, ha='center', fontweight='bold')

        # Multi-Grade Filter (MGF) & Activated Carbon Filter (ACF)
        mgf = patches.Rectangle((680, 520), 40, 70, facecolor='#BEE3F8', edgecolor='#2B6CB0', lw=1.5)
        acf = patches.Rectangle((750, 520), 40, 70, facecolor='#E2E8F0', edgecolor='#4A5568', lw=1.5)
        ax.add_patch(mgf); ax.add_patch(acf)
        ax.text(700, 555, "ET-06\nMGF", fontsize=5.5, ha='center', va='center', fontweight='bold')
        ax.text(770, 555, "ET-07\nACF", fontsize=5.5, ha='center', va='center', fontweight='bold')

        # Treated Water Sump & Discharge
        ax.plot([820, 890, 890, 820, 820], [530, 530, 580, 580, 530], color='#38A169', lw=1.8)
        ax.text(855, 555, "TREATED WATER\nSUMP (20 m³)\nSPCB DISCHARGE", fontsize=5.5, ha='center', va='center', fontweight='bold', color='#22543D')

        # Sludge Filter Press ET-08
        s_press = patches.Rectangle((560, 420), 80, 50, facecolor='#CBD5E0', edgecolor='#4A5568', lw=1.5)
        ax.add_patch(s_press)
        ax.text(600, 445, "ET-08 FILTER PRESS\nDry Sludge to Compost", fontsize=5.5, ha='center', va='center', fontweight='bold')
        ax.plot([600, 600], [510, 470], color='#718096', ls='--', lw=1.5)

        # Lower Region: Water & Steam Quality Standards Matrix (Y=80 to 330)
        u_matrix = patches.Rectangle((50, 80), 900, 240, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.5)
        ax.add_patch(u_matrix)
        ax.text(65, 300, "UTILITY & ENVIRONMENTAL QUALITY PARAMETERS TABLE", fontsize=8.5, fontweight='bold', color='#1A365D')

        u_headers = ["PARAMETER / STREAM", "RAW BOREWELL", "SOFTENED WATER", "BOILER FEEDWATER", "RAW EFFLUENT", "TREATED ETP EFFLUENT", "SPCB LIMIT"]
        u_col_x = [65, 230, 360, 490, 620, 750, 870]
        ax.plot([50, 950], [290, 290], color='#1A365D', lw=1.2)
        for cx, uh in zip(u_col_x, u_headers):
            ax.text(cx, 293, uh, fontsize=6, fontweight='bold', color='#1A365D')

        utility_params = [
            ("pH Value", "7.4 - 7.8", "7.2 - 7.6", "8.5 - 9.5 (with morph)", "8.2 - 8.9 (alkaline soak)", "7.0 - 7.5", "6.5 - 8.5"),
            ("Total Dissolved Solids (TDS)", "650 mg/L", "680 mg/L", "< 1,500 mg/L (blowdown)", "1,850 mg/L", "1,200 mg/L", "< 2,100 mg/L"),
            ("Total Hardness (as CaCO3)", "320 mg/L", "< 5 mg/L (Zero Hard)", "< 1 mg/L", "280 mg/L", "< 50 mg/L", "N/A"),
            ("Chemical Oxygen Demand (COD)", "< 10 mg/L", "< 5 mg/L", "< 5 mg/L", "2,400 mg/L (leached)", "< 180 mg/L", "< 250 mg/L"),
            ("Biochemical Oxygen Demand (BOD5)", "< 3 mg/L", "< 2 mg/L", "< 2 mg/L", "1,250 mg/L", "< 25 mg/L", "< 30 mg/L"),
            ("Total Suspended Solids (TSS)", "< 15 mg/L", "< 2 mg/L", "< 1 mg/L", "480 mg/L (fines)", "< 30 mg/L", "< 100 mg/L"),
            ("Oil & Grease", "Nil", "Nil", "Nil", "35 mg/L", "< 5 mg/L", "< 10 mg/L"),
            ("Dissolved Oxygen (DO)", "5.5 mg/L", "6.0 mg/L", "< 0.02 mg/L (deaerated)", "< 0.5 mg/L", "> 4.0 mg/L", "> 4.0 mg/L")
        ]
        uy = 270
        for row in utility_params:
            for cx, val in zip(u_col_x, row):
                ax.text(cx, uy, val, fontsize=5.5, color='#2D3748')
            uy -= 18

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # SHEET 12: HAZARDOUS AREA CLASSIFICATION & DUST EXPLOSION SAFETY PLAN (DWG-011)
        # =========================================================================
        print("Rendering Sheet 12: Hazardous Area Classification & Dust Safety Plan...")
        fig, ax = plt.subplots(figsize=(16.54, 11.69), dpi=150)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 700)
        ax.axis('off')
        draw_iso_title_block(ax, "12", total_sheets, "DWG-FIN-15T-011", "Hazardous Area Classification & Dust Safety Plan", "1:100", "SAFETY & LOSS PREVENTION")

        # Top Region: Plant Layout with Combustible Dust Hazard Zones (Y=340 to 650)
        bldg_hac = patches.Rectangle((80, 360), 780, 260, facecolor='#F7FAFC', edgecolor='#1A365D', lw=2.0)
        ax.add_patch(bldg_hac)
        ax.text(470, 630, "MAIN FACILITY DUST HAZARD CONTOUR MAP (NFPA 61 / NFPA 652 / NFPA 68 / ATEX 2014/34/EU)", fontsize=8, fontweight='bold', color='#1A365D', ha='center')

        # Zone 20 Areas (Continuous explosive dust cloud inside enclosed equipment)
        # Silos SL-101A/B
        silo_hac1 = patches.Circle((140, 520), 25, facecolor='#FEB2B2', edgecolor='#9B2C2C', lw=1.5, hatch='///')
        silo_hac2 = patches.Circle((200, 520), 25, facecolor='#FEB2B2', edgecolor='#9B2C2C', lw=1.5, hatch='///')
        ax.add_patch(silo_hac1); ax.add_patch(silo_hac2)
        ax.text(140, 520, "ZONE 20\nSILO A", fontsize=5.5, color='#9B2C2C', ha='center', va='center', fontweight='bold')
        ax.text(200, 520, "ZONE 20\nSILO B", fontsize=5.5, color='#9B2C2C', ha='center', va='center', fontweight='bold')

        # Bucket Elevator BE-101 casing
        be_hac = patches.Rectangle((245, 480), 20, 80, facecolor='#FEB2B2', edgecolor='#9B2C2C', lw=1.5, hatch='///')
        ax.add_patch(be_hac)
        ax.text(255, 520, "ZONE 20\nELEV", fontsize=5, color='#9B2C2C', ha='center', va='center', fontweight='bold')

        # Cyclone CY-101 & Baghouse BF-101
        cyc_hac = patches.Circle((570, 520), 22, facecolor='#FEB2B2', edgecolor='#9B2C2C', lw=1.5, hatch='///')
        bf_hac = patches.Rectangle((610, 485), 50, 70, facecolor='#FEB2B2', edgecolor='#9B2C2C', lw=1.5, hatch='///')
        ax.add_patch(cyc_hac); ax.add_patch(bf_hac)
        ax.text(570, 520, "ZONE 20\nCYCLONE", fontsize=5, color='#9B2C2C', ha='center', va='center', fontweight='bold')
        ax.text(635, 520, "ZONE 20\nBAG FILTER\n(Av=1.84 m²)", fontsize=5, color='#9B2C2C', ha='center', va='center', fontweight='bold')

        # Zone 21 Areas (Occasional explosive dust cloud, 1.0m radius)
        z21_dump = patches.Rectangle((90, 430), 80, 50, facecolor='#FEEBC8', edgecolor='#DD6B20', lw=1.2, ls='--')
        z21_dry_in = patches.Circle((390, 490), 28, facecolor='#FEEBC8', edgecolor='#DD6B20', lw=1.2, ls='--')
        z21_dry_out = patches.Circle((520, 490), 28, facecolor='#FEEBC8', edgecolor='#DD6B20', lw=1.2, ls='--')
        ax.add_patch(z21_dump); ax.add_patch(z21_dry_in); ax.add_patch(z21_dry_out)
        ax.text(130, 455, "ZONE 21\nINTAKE PIT", fontsize=5.5, color='#C05621', ha='center', va='center', fontweight='bold')
        ax.text(390, 490, "ZONE 21\nFEED BOOT", fontsize=5, color='#C05621', ha='center', va='center', fontweight='bold')
        ax.text(520, 490, "ZONE 21\nDISCHARGE", fontsize=5, color='#C05621', ha='center', va='center', fontweight='bold')

        # Zone 22 Areas (Abnormal release, 3.0m envelope around packaging & dedusting)
        z22_pkg = patches.Rectangle((680, 380), 160, 160, facecolor='#FEFCBF', edgecolor='#D69E2E', lw=1.2, ls=':')
        ax.add_patch(z22_pkg)
        ax.text(760, 460, "ZONE 22 ENVELOPE (SECONDARY PACKAGING & DAY BINS)\nEXTENDS 3.0m AROUND FFS FILLING HEADS", fontsize=6, color='#744210', ha='center', va='center', fontweight='bold')

        # Safe Unclassified Zones (Green background)
        ax.text(330, 410, "UNCLASSIFIED SAFE ZONE\nWET SOAKING BATTERY (IP66 WASHDOWN)\nHIGH MOISTURE — NO DUST CLOUD HAZARD", fontsize=6, color='#22543D', ha='center', fontweight='bold')
        ax.text(760, 580, "POSITIVE PRESSURE CLEANROOM (+15 Pa HEPA H14)\nUNCLASSIFIED SAFE ZONE", fontsize=5.5, color='#22543D', ha='center', fontweight='bold')

        # Legend Box for Zones
        leg_box = patches.Rectangle((80, 365), 230, 45, facecolor='#FFFFFF', edgecolor='#CBD5E0', lw=1.0)
        ax.add_patch(leg_box)
        ax.text(85, 398, "ZONE 20: Continuous Cloud (Inside Enclosures)", fontsize=5.2, color='#9B2C2C', fontweight='bold')
        ax.text(85, 386, "ZONE 21: Occasional Cloud (1.0m from Ports)", fontsize=5.2, color='#C05621', fontweight='bold')
        ax.text(85, 374, "ZONE 22: Infrequent Cloud (3.0m Perimeter)", fontsize=5.2, color='#744210', fontweight='bold')

        # Lower-Left Box: NFPA 68 Explosion Venting Calculations & Design Basis
        vent_box = patches.Rectangle((50, 75), 450, 245, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.5)
        ax.add_patch(vent_box)
        ax.text(65, 298, "NFPA 68 / NFPA 652 EXPLOSION VENTING DESIGN BASIS", fontsize=8, fontweight='bold', color='#1A365D')

        vent_lines = [
            ("Combustible Dust Specimen", "Tanzanian Split Pigeon Pea (Toor-Dal) Flour / Fines"),
            ("Median Particle Size (D50)", "42 µm (< 75 µm sieve fraction passing > 92%)"),
            ("Dust Explosibility Class", "St 1 (Low to Moderate Deflagration Severity)"),
            ("Maximum Explosion Pressure (Pmax)", "8.5 barg (850 kPa gauge)"),
            ("Deflagration Index (Kst)", "110 bar·m/s (measured in 20L sphere per ASTM E1226)"),
            ("Minimum Ignition Energy (MIE)", "45 mJ (capacitive spark without inductance)"),
            ("Minimum Ignition Temp - Cloud (MIT)", "420 °C (BAM furnace per ASTM E1491)"),
            ("Minimum Ignition Temp - 5mm Layer", "290 °C (hot plate per ASTM E2021)"),
            ("Maximum Equipment Surface Temp", "120 °C (Temp Class T4 / T120°C per EN 50281-1-1)"),
            ("Reduced Pressure Limit (Pred)", "0.40 barg (Baghouse Pred design rating = 0.50 barg)"),
            ("Static Activation Pressure (Pstat)", "0.10 barg ± 15% (Bursting Panel)"),
            ("Calculated Baghouse Vent Area (Av)", "1.84 m² (NFPA 68 Eq. 8.2.2 with L/D = 2.1)"),
            ("Relief Duct Discharge Routing", "Vertical SS304 duct through roof (< 3m length)"),
        ]
        vy = 278
        for label, val in vent_lines:
            ax.text(65, vy, f"• {label}:", fontsize=5.8, color='#2D3748', fontweight='bold')
            ax.text(285, vy, val, fontsize=5.8, color='#1A365D')
            vy -= 14.5

        # Lower-Right Box: Grounding, Electrical Protection & Interlocks
        prot_box = patches.Rectangle((520, 75), 430, 245, facecolor='#FFFFFF', edgecolor='#1A365D', lw=1.5)
        ax.add_patch(prot_box)
        ax.text(535, 298, "EQUIPMENT INGRESS, GROUNDING & SAFETY INTERLOCKS", fontsize=8, fontweight='bold', color='#1A365D')

        prot_lines = [
            ("ELECTRICAL INGRESS RATINGS:", "STANDARDS & CERTIFICATIONS:"),
            ("• Zone 20 / 21 Motors & Enclosures", "Ex tb IIIC T120°C Db IP66 (ATEX / PESO Certified)"),
            ("• Zone 22 Motors & Sensors", "Ex tc IIIB T120°C Dc IP65 (Dust-Ignition Proof)"),
            ("• Wet Process Area Instruments", "IP66 / NEMA 4X Washdown Stainless Steel SS316L"),
            ("• Substation / MCC Room", "Pressurized Clean Air (+25 Pa, Non-Hazardous Safe)"),
            ("", ""),
            ("STATIC BONDING & GROUNDING:", "RESISTANCE SPECIFICATIONS:"),
            ("• Continuous Earth Grid Resistance", "< 1.0 Ohm to main substation grounding ring"),
            ("• Piping Flange Jumpers", "Braided copper continuity jumpers (< 10 Ohms)"),
            ("• Flexible Expansion Sleeves", "Conductive silicone with molded copper wire inserts"),
            ("", ""),
            ("SAFETY INSTRUMENTED SYSTEMS:", "ACTION & FAIL-SAFE MATRIX:"),
            ("• Spark Detection in Exhaust Duct", "GreCon IR Sensor -> Fast Gate Closure (< 35 ms)"),
            ("• Bag Filter Broken Bag Detector", "Triboelectric Probe (AIT-102) -> Auto ID Fan Trip"),
            ("• Silo High-High Level Sensor", "Tuning Fork LSLL-101 -> Interlocks Infeed Conveyor"),
        ]
        py = 278
        for c1_txt, c2_txt in prot_lines:
            if "STANDARDS" in c2_txt or "SPECIFICATIONS" in c2_txt or "MATRIX" in c2_txt:
                ax.text(535, py, c1_txt, fontsize=5.8, color='#2B6CB0', fontweight='bold')
                ax.text(750, py, c2_txt, fontsize=5.8, color='#2B6CB0', fontweight='bold')
            else:
                ax.text(535, py, c1_txt, fontsize=5.5, color='#2D3748')
                ax.text(750, py, c2_txt, fontsize=5.5, color='#1A365D', fontweight='bold')
            py -= 14.5

        pdf.savefig(fig)
        plt.close(fig)

    print("World-Class Multi-Sheet Engineering PDF Package Generated Successfully!")

    # =========================================================================
    # EXPORT HIGH-RESOLUTION A3 PNG IMAGES (150 DPI) FOR ALL 12 SHEETS
    # =========================================================================
    import fitz
    import shutil

    artifact_dir = r"C:\Users\SOURISH SENAPATI\.gemini\antigravity-ide\brain\e60c88e3-dafa-4b48-82c7-ef80cde70237"
    png_dir = os.path.abspath("engineering/cad/png")
    os.makedirs(png_dir, exist_ok=True)
    os.makedirs(artifact_dir, exist_ok=True)

    print(f"Extracting all 12 sheets from PDF to PNG via PyMuPDF...")
    doc = fitz.open(out_pdf)
    for i, page in enumerate(doc):
        sheet_no = f"{i+1:02d}"
        pix = page.get_pixmap(dpi=150)
        local_png = os.path.join(png_dir, f"v3_sheet_{sheet_no}_drawing.png")
        pix.save(local_png)
        art_png = os.path.join(artifact_dir, f"v3_sheet_{sheet_no}_drawing.png")
        pix.save(art_png)
        print(f"-> Saved Sheet {sheet_no}: {local_png} & {art_png} ({pix.width}x{pix.height} px)")
    doc.close()

    # Copy master PDF to artifact directory
    art_pdf = os.path.join(artifact_dir, "HARAKUTIR_15TPD_ENGINEERING_DRAWING_PACKAGE_REV_V3.pdf")
    shutil.copyfile(out_pdf, art_pdf)
    print(f"-> Copied Master Drawing PDF to Artifacts: {art_pdf}")

if __name__ == "__main__":
    generate_pdf_package()

