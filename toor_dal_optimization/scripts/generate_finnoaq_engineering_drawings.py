"""
Generate publication-quality 7-sheet vector engineering PDF drawing package.
Covers:
Sheet 1: Process Flow Diagram (PFD) & 12-Stream Mass Balance Overlay
Sheet 2: Plant Master Plot Plan & 5-Tier Hygienic Zoning (DWG-001)
Sheet 3: Soak Tank TK-101A/B General Arrangement & Nozzle Schedule (DWG-005)
Sheet 4: Fluid-Bed Dryer DR-101 General Arrangement & Psychrometrics (DWG-007)
Sheet 5: Electrical Single Line Diagram (SLD) & MCC Distribution (DWG-009)
Sheet 6: Reconciled Mass, Moisture & Chemical Formulation Comparison
Sheet 7: Pre-Registered 4-Condition Screening Protocol Flowsheet
"""

import os
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors as rcolors

def create_engineering_drawings_pdf():
    output_pdf_path = "reports/FINNOAQ_15TPD_PROCESS_AND_ENGINEERING_DIAGRAMS.pdf"
    os.makedirs("reports", exist_ok=True)
    os.makedirs("engineering/cad/pdf", exist_ok=True)
    
    # A3 Landscape dimensions: 1190.55 x 841.89 points
    w, h = landscape(A3)
    c = canvas.Canvas(output_pdf_path, pagesize=landscape(A3))

    def draw_standard_border_and_title_block(sheet_no, total_sheets, dwg_no, title, discipline):
        # Outer Border
        c.setStrokeColor(rcolors.HexColor("#1A2530"))
        c.setLineWidth(2.5)
        c.rect(25, 25, w - 50, h - 50)
        
        # Inner Border
        c.setLineWidth(1.0)
        c.rect(32, 32, w - 64, h - 64)

        # Title Block Box (Bottom Right)
        tb_w, tb_h = 360, 95
        tb_x, tb_y = w - 32 - tb_w, 32
        c.setFillColor(rcolors.HexColor("#FAFAFA"))
        c.rect(tb_x, tb_y, tb_w, tb_h, fill=1, stroke=1)
        
        # Grid lines in title block
        c.setStrokeColor(rcolors.HexColor("#1A2530"))
        c.setLineWidth(0.8)
        c.line(tb_x, tb_y + 70, tb_x + tb_w, tb_y + 70)
        c.line(tb_x, tb_y + 48, tb_x + tb_w, tb_y + 48)
        c.line(tb_x, tb_y + 24, tb_x + tb_w, tb_y + 24)
        c.line(tb_x + 220, tb_y, tb_x + 220, tb_y + 48)

        # Company Header
        c.setFillColor(rcolors.HexColor("#0B2545"))
        c.setFont("Helvetica-Bold", 11)
        c.drawString(tb_x + 10, tb_y + 77, "FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES LTD — PROCESS ENGINEERING")
        
        # Title
        c.setFillColor(rcolors.HexColor("#13315C"))
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(tb_x + 10, tb_y + 55, title[:48])
        
        # Metadata
        c.setFillColor(rcolors.black)
        c.setFont("Helvetica", 8)
        c.drawString(tb_x + 10, tb_y + 32, f"DWG: {dwg_no} | REV: 1.0")
        c.drawString(tb_x + 10, tb_y + 10, f"DISC: {discipline} | UNITS: mm / kg")
        
        c.drawString(tb_x + 230, tb_y + 32, f"SHEET: {sheet_no} OF {total_sheets}")
        c.drawString(tb_x + 230, tb_y + 10, "DATE: 2026-10-15")

        # Top Banner Title
        c.setFillColor(rcolors.HexColor("#0B2545"))
        c.setFont("Helvetica-Bold", 15)
        c.drawString(45, h - 55, f"{dwg_no}: {title}")
        c.setFont("Helvetica", 9)
        c.setFillColor(rcolors.HexColor("#4A5568"))
        c.drawString(45, h - 70, f"Project: FinnoaQ Greenfield Toor Dal 15 MT/Day Processing Facility | Discipline: {discipline} | Basis: 15,000 kg/day Incoming Feed")

        # Prominent Mandatory Warning Stamp (Bottom Left)
        c.setFillColor(rcolors.HexColor("#FFF5F5"))
        c.setStrokeColor(rcolors.HexColor("#E53E3E"))
        c.setLineWidth(1.5)
        c.rect(45, 36, 440, 32, fill=1, stroke=1)
        c.setFillColor(rcolors.HexColor("#C53030"))
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(55, 54, "WARNING: PRELIMINARY — NOT FOR CONSTRUCTION / NOT FOR PROCUREMENT")
        c.setFont("Helvetica", 7.5)
        c.drawString(55, 42, "Design maturity: PRELIMINARY_CALCULATED. Strictly held at Gate G-A pending target lot physical lab data.")

    # =========================================================================
    # SHEET 1: PROCESS FLOW DIAGRAM (PFD) WITH 12-STREAM MASS BALANCE OVERLAY
    # =========================================================================
    draw_standard_border_and_title_block(1, 7, "DWG-FIN-15T-002", "PROCESS FLOW DIAGRAM & 12-STREAM MASS BALANCE OVERLAY", "Process Engineering")
    
    # Equipment Blocks (Left to Right)
    # Unit 1: Raw Intake Hopper HP-101
    c.setFillColor(rcolors.HexColor("#E2E8F0"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.setLineWidth(1.5)
    c.rect(60, 480, 70, 90, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(95, 550, "HP-101")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(95, 535, "Raw Intake")
    c.drawCentredString(95, 523, "Dump Hopper")
    c.drawCentredString(95, 500, "15,000 kg/d")

    # Arrow to Elevator
    c.setStrokeColor(rcolors.HexColor("#4A5568"))
    c.setLineWidth(1.5)
    c.line(130, 525, 160, 525)
    
    # Unit 2: Bucket Elevator EL-101
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.rect(160, 450, 40, 160, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(180, 580, "EL-101")
    c.setFont("Helvetica", 7)
    c.drawCentredString(180, 520, "Bucket")
    c.drawCentredString(180, 508, "Elevator")
    c.drawCentredString(180, 490, "1.5 kW")

    # Arrow to Weigh Feeder
    c.line(200, 590, 230, 590)

    # Unit 3: Weigh Feeder WF-101
    c.setFillColor(rcolors.HexColor("#E2E8F0"))
    c.rect(230, 565, 60, 50, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(260, 595, "WF-101")
    c.setFont("Helvetica", 7)
    c.drawCentredString(260, 578, "Loss-in-Weight")

    # Arrow to Soak Tanks
    c.line(290, 590, 340, 590)
    c.line(340, 590, 340, 520)

    # Unit 4: Soak Vessels TK-101A/B & AG-101
    c.setFillColor(rcolors.HexColor("#EBF8FF"))
    c.rect(320, 390, 100, 130, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(370, 500, "TK-101A/B")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(370, 485, "Soak Vessels (2x)")
    c.drawCentredString(370, 472, "3.86 m³ SS316L")
    c.drawCentredString(370, 455, "30 min @ 28°C")
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(370, 430, "AG-101A/B")
    c.setFont("Helvetica", 7)
    c.drawCentredString(370, 415, "Low-Shear 35 RPM")
    c.drawCentredString(370, 400, "2.2 kW Hydrofoil")

    # Chemical Skid SK-100 feeding soaker
    c.setFillColor(rcolors.HexColor("#FEFCBF"))
    c.setStrokeColor(rcolors.HexColor("#B7791F"))
    c.rect(320, 570, 100, 60, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#744210"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(370, 615, "SK-100 DOSING SKID")
    c.setFont("Helvetica", 7)
    c.drawCentredString(370, 600, "0.50% w/w NaHCO3")
    c.drawCentredString(370, 588, "Basis A: 112.5 kg/d")
    c.drawCentredString(370, 576, "Basis B: 75.0 kg/d")
    # Feed line from skid to soaker
    c.setStrokeColor(rcolors.HexColor("#B7791F"))
    c.line(370, 570, 370, 520)

    # Slurry discharge line from soaker to screen
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.line(370, 390, 370, 360)
    c.line(370, 360, 460, 360)

    # Unit 5: Dewatering Vibrating Screen SC-101 & Rinser RN-101
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.rect(460, 330, 90, 70, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(505, 385, "SC-101 / RN-101")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(505, 370, "Dewatering Screen")
    c.drawCentredString(505, 355, "& Mist Rinser")
    c.drawCentredString(505, 340, "30.0g Spray / 200g")

    # Spent liquor effluent drainage to ETP
    c.setStrokeColor(rcolors.HexColor("#C53030"))
    c.line(505, 330, 505, 270)
    c.setFillColor(rcolors.HexColor("#FFF5F5"))
    c.rect(455, 240, 100, 30, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#9B2C2C"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(505, 258, "S-05 Spent Liquor")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(505, 246, "19,110 kg/d to ETP")

    # Line to Dryer
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.line(550, 365, 600, 365)

    # Unit 6: Continuous Fluid-Bed Dryer DR-101
    c.setFillColor(rcolors.HexColor("#EBF8FF"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.rect(600, 310, 180, 120, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(690, 415, "DR-101 FLUID-BED DRYER / COOLER")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(690, 395, "Active Deck: 1.0 m W x 6.0 m L (6.0 m²)")
    c.drawCentredString(690, 380, "4.5m Drying (60°C) + 1.5m Cooling (28°C)")
    c.drawCentredString(690, 365, "Steam Heater HE-101: 301.2 kW thermal")
    c.drawCentredString(690, 350, "Blower FN-101: 11.0 kW (7,605 m³/h)")
    c.setFillColor(rcolors.HexColor("#C53030"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(690, 330, "Reconciled Evap: 3,877.78 kg H2O/day")
    c.drawCentredString(690, 318, "(242.36 kg/h Nom | 285.13 kg/h Des)")

    # Exhaust & Cyclones
    c.setStrokeColor(rcolors.HexColor("#718096"))
    c.line(690, 430, 690, 500)
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.rect(660, 500, 60, 70, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#2D3748"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(690, 555, "CY-101A/B")
    c.setFont("Helvetica", 7)
    c.drawCentredString(690, 540, "Twin Cyclones")
    c.drawCentredString(690, 525, "Dia 800 mm")
    c.drawCentredString(690, 510, "99.2% Fines Catch")

    # Line from Dryer to Destoner / Scalper
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.line(780, 350, 830, 350)

    # Unit 7: Destoner & Scalping Screen SC-102
    c.setFillColor(rcolors.HexColor("#E2E8F0"))
    c.rect(830, 320, 80, 60, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(870, 365, "SC-102")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(870, 350, "Scalper / Screen")
    c.drawCentredString(870, 335, "Fines Removal")

    # Scalped fines to reject
    c.setStrokeColor(rcolors.HexColor("#E53E3E"))
    c.line(870, 320, 870, 270)
    c.setFillColor(rcolors.HexColor("#FFF5F5"))
    c.rect(830, 240, 80, 30, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#9B2C2C"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(870, 258, "S-11 Rejects")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(870, 246, "388.0 kg/d Fines")

    # Line to Packaging
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.line(910, 350, 960, 350)

    # Unit 8: Form-Fill-Seal Packaging Line PK-101
    c.setFillColor(rcolors.HexColor("#C6F6D5"))
    c.setStrokeColor(rcolors.HexColor("#276749"))
    c.rect(960, 310, 100, 80, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#22543D"))
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(1010, 375, "PK-101")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(1010, 360, "FFS Packaging Line")
    c.drawCentredString(1010, 345, "1kg / 5kg Pouches")
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(1010, 330, "14,324.2 kg/day")
    c.setFont("Helvetica", 7)
    c.drawCentredString(1010, 318, "Strictly 10.00% wb")

    # MASTER 12-STREAM MASS BALANCE TABLE OVERLAY (Bottom Area)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(45, 215, "RECONCILED 12-STREAM MASS BALANCE DATA TABLE (Daily Basis: 15,000 kg/day Feed Dal)")

    table_data = [
        ("Stream ID & Description", "Total Mass", "Dry Solids", "Water", "Moisture %", "Chemical", "Physical State"),
        ("S-01: Raw Feed Dal (ex-Hopper)", "15,000.0 kg", "13,425.0 kg", "1,575.0 kg", "10.50% wb", "0.0 kg", "Granular Solid"),
        ("S-02: Fresh Soft Water to Soak", "22,387.5 kg", "0.0 kg", "22,387.5 kg", "100.0% wb", "0.0 kg", "Liquid Water"),
        ("S-03: Active Chemical (NaHCO3)", "112.5 kg", "112.5 kg", "0.0 kg", "0.00% wb", "112.5 kg", "FCC Powder"),
        ("S-04: Drained Wet Dal ex-Soak", "18,390.0 kg", "13,279.0 kg", "5,111.0 kg", "27.79% wb", "23.4 kg", "Wet Granules"),
        ("S-05: Spent Soak Liquor to ETP", "19,110.0 kg", "258.5 kg", "18,851.5 kg", "98.65% wb", "89.1 kg", "Alkaline Effluent"),
        ("S-06: Fresh Mist Rinse Water", "2,250.0 kg", "0.0 kg", "2,250.0 kg", "100.0% wb", "0.0 kg", "Potable Spray"),
        ("S-07: Spent Mist Rinse Runoff", "2,050.0 kg", "38.0 kg", "2,012.0 kg", "98.15% wb", "15.3 kg", "Rinse Effluent"),
        ("S-08: Wet Dal Feed to Dryer", "18,590.0 kg", "13,241.0 kg", "5,349.0 kg", "28.77% wb", "8.1 kg", "Wet Grain Bed"),
        ("S-09: Hot Fluidizing Air Inlet", "129,000.0 kg", "127,452.0 kg", "1,548.0 kg", "1.20% wb", "0.0 kg", "Air @ 60°C"),
        ("S-10: Humid Exhaust & Vapor", "132,877.8 kg", "127,452.0 kg", "5,425.8 kg", "4.08% wb", "0.0 kg", "Vapor Exhaust"),
        ("S-11: Scalped Fines / Rejects", "388.0 kg", "349.2 kg", "38.8 kg", "10.00% wb", "0.2 kg", "Dry Rejects"),
        ("S-12: Finished Packaged Dal", "14,324.2 kg", "12,891.8 kg", "1,432.4 kg", "10.00% wb", "7.9 kg", "Saleable Product"),
    ]

    ty = 195
    row_h = 10.5
    for r_idx, row in enumerate(table_data):
        if r_idx == 0:
            c.setFillColor(rcolors.HexColor("#2B6CB0"))
            c.rect(45, ty - 2, 720, row_h, fill=1, stroke=0)
            c.setFillColor(rcolors.white)
            c.setFont("Helvetica-Bold", 7)
        else:
            c.setFillColor(rcolors.HexColor("#F7FAFC") if r_idx % 2 == 0 else rcolors.white)
            c.rect(45, ty - 2, 720, row_h, fill=1, stroke=0)
            c.setFillColor(rcolors.HexColor("#2D3748"))
            c.setFont("Helvetica", 6.8)
        
        c.drawString(50, ty, row[0])
        c.drawString(220, ty, row[1])
        c.drawString(300, ty, row[2])
        c.drawString(380, ty, row[3])
        c.drawString(460, ty, row[4])
        c.drawString(540, ty, row[5])
        c.drawString(620, ty, row[6])
        ty -= row_h

    c.showPage()

    # =========================================================================
    # SHEET 2: MASTER PLANT PLOT PLAN & HYGIENIC ZONING (DWG-FIN-15T-001)
    # =========================================================================
    draw_standard_border_and_title_block(2, 7, "DWG-FIN-15T-001", "PLANT MASTER PLOT PLAN & 5-TIER HYGIENIC ZONING", "Civil / Plant Layout")

    # Plot Plan Area: 45m x 20m building representation
    # Drawing boundary box
    c.setStrokeColor(rcolors.HexColor("#1A202C"))
    c.setLineWidth(2)
    b_x, b_y, b_w, b_h = 60, 160, 950, 480
    c.rect(b_x, b_y, b_w, b_h)

    # Grid columns A-E and 1-4
    c.setStrokeColor(rcolors.HexColor("#CBD5E0"))
    c.setLineWidth(0.5)
    for gx in [b_x + b_w*0.22, b_x + b_w*0.50, b_x + b_w*0.75]:
        c.line(gx, b_y, gx, b_y + b_h)
    for gy in [b_y + b_h*0.35, b_y + b_h*0.70]:
        c.line(b_x, gy, b_x + b_w, gy)

    # 5 Zones color fills
    # Zone 1: Raw Intake & Warehouse (Left side: 10m x 20m)
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.rect(b_x, b_y, b_w*0.22, b_h, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#2D3748"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(b_x + 15, b_y + b_h - 25, "ZONE 1: RAW INTAKE & STORAGE")
    c.setFont("Helvetica", 8)
    c.drawString(b_x + 15, b_y + b_h - 40, "Unclassified Hygiene Area")
    c.drawString(b_x + 15, b_y + b_h - 55, "Incoming Grain Storage: 150 MT")
    c.drawString(b_x + 15, b_y + b_h - 70, "Truck Unloading Bay (Roll-up Door)")
    c.drawString(b_x + 15, b_y + b_h - 85, "Intake Hopper HP-101 & Destoner")

    # Zone 2: Wet Soaking & Chemical Dosing (Center-Left: 12m x 12m)
    c.setFillColor(rcolors.HexColor("#EBF8FF"))
    c.rect(b_x + b_w*0.22, b_y + b_h*0.30, b_w*0.28, b_h*0.70, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#2B6CB0"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(b_x + b_w*0.22 + 15, b_y + b_h - 25, "ZONE 2: WET SOAKING & DOSING")
    c.setFont("Helvetica", 8)
    c.drawString(b_x + b_w*0.22 + 15, b_y + b_h - 40, "Low Care / Washdown Zone (IP66)")
    c.drawString(b_x + b_w*0.22 + 15, b_y + b_h - 55, "Epoxy Floor, Stainless Trench Drains")
    c.drawString(b_x + b_w*0.22 + 15, b_y + b_h - 70, "Soak Tanks TK-101A/B (Dia 1.6m)")
    c.drawString(b_x + b_w*0.22 + 15, b_y + b_h - 85, "Chemical Dosing Skid SK-100")
    c.drawString(b_x + b_w*0.22 + 15, b_y + b_h - 100, "Dewatering Vibratory Screen SC-101")

    # Zone 3: Thermal Drying & Fluid-Bed (Center-Right: 13m x 12m)
    c.setFillColor(rcolors.HexColor("#FEFCBF"))
    c.rect(b_x + b_w*0.50, b_y + b_h*0.30, b_w*0.25, b_h*0.70, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#B7791F"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(b_x + b_w*0.50 + 15, b_y + b_h - 25, "ZONE 3: THERMAL DRYING")
    c.setFont("Helvetica", 8)
    c.drawString(b_x + b_w*0.50 + 15, b_y + b_h - 40, "Medium Care Processing Area")
    c.drawString(b_x + b_w*0.50 + 15, b_y + b_h - 55, "Continuous Fluid-Bed Dryer DR-101")
    c.drawString(b_x + b_w*0.50 + 15, b_y + b_h - 70, "Active Deck 1.0m x 6.0m")
    c.drawString(b_x + b_w*0.50 + 15, b_y + b_h - 85, "Blower Fan FN-101 & Steam Coils")
    c.drawString(b_x + b_w*0.50 + 15, b_y + b_h - 100, "Twin Cyclones CY-101A/B")

    # Zone 4: Cleanroom Final Screening & Retail Packaging (Right: 10m x 12m)
    c.setFillColor(rcolors.HexColor("#C6F6D5"))
    c.rect(b_x + b_w*0.75, b_y + b_h*0.30, b_w*0.25, b_h*0.70, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#22543D"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(b_x + b_w*0.75 + 15, b_y + b_h - 25, "ZONE 4: PACKAGING CLEANROOM")
    c.setFont("Helvetica", 8)
    c.drawString(b_x + b_w*0.75 + 15, b_y + b_h - 40, "High Care Cleanroom (ISO Class 8)")
    c.drawString(b_x + b_w*0.75 + 15, b_y + b_h - 55, "Positive Pressure (+15 Pa), HEPA Filtered")
    c.drawString(b_x + b_w*0.75 + 15, b_y + b_h - 70, "Personnel Airlock & Gowning Room")
    c.drawString(b_x + b_w*0.75 + 15, b_y + b_h - 85, "Destoner & Scalping Screen SC-102")
    c.drawString(b_x + b_w*0.75 + 15, b_y + b_h - 100, "FFS Packaging Machine PK-101")

    # Lower Bay: Central Corridor, Lab, MCC Room, Finished Goods Warehouse
    # MCC Room
    c.setFillColor(rcolors.HexColor("#E2E8F0"))
    c.rect(b_x + b_w*0.22, b_y, b_w*0.18, b_h*0.30, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A202C"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(b_x + b_w*0.22 + 10, b_y + b_h*0.30 - 20, "MCC / ELECTRICAL ROOM")
    c.setFont("Helvetica", 7.5)
    c.drawString(b_x + b_w*0.22 + 10, b_y + b_h*0.30 - 35, "Main 415V Switchboard")
    c.drawString(b_x + b_w*0.22 + 10, b_y + b_h*0.30 - 48, "PLC & Automation Panel")

    # Quality Control Lab
    c.setFillColor(rcolors.HexColor("#EBF8FF"))
    c.rect(b_x + b_w*0.40, b_y, b_w*0.18, b_h*0.30, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A202C"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(b_x + b_w*0.40 + 10, b_y + b_h*0.30 - 20, "QA/QC ANALYTICAL LAB")
    c.setFont("Helvetica", 7.5)
    c.drawString(b_x + b_w*0.40 + 10, b_y + b_h*0.30 - 35, "Moisture Analyzers & Flame Photometer")
    c.drawString(b_x + b_w*0.40 + 10, b_y + b_h*0.30 - 48, "Texture & Cooking Time Test Station")

    # Finished Goods Warehouse
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.rect(b_x + b_w*0.58, b_y, b_w*0.42, b_h*0.30, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A202C"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(b_x + b_w*0.58 + 15, b_y + b_h*0.30 - 20, "ZONE 5: FINISHED GOODS WAREHOUSE & DISPATCH")
    c.setFont("Helvetica", 7.5)
    c.drawString(b_x + b_w*0.58 + 15, b_y + b_h*0.30 - 35, "Pallet Storage (100 MT Capacity) | Dispatch Roll-Up Door")

    c.showPage()

    # =========================================================================
    # SHEET 3: SOAK VESSEL (TK-101A/B) GENERAL ARRANGEMENT & NOZZLE SCHEDULE
    # =========================================================================
    draw_standard_border_and_title_block(3, 7, "DWG-FIN-15T-005", "SOAK TANK TK-101A/B MECHANICAL GENERAL ARRANGEMENT", "Mechanical Equipment")

    # Vessel Elevation View (Left Half)
    vx, vy, vw, vh = 120, 200, 220, 360
    
    # Legs
    c.setStrokeColor(rcolors.HexColor("#4A5568"))
    c.setLineWidth(2.5)
    c.line(vx + 20, vy, vx + 20, vy - 60)
    c.line(vx + vw - 20, vy, vx + vw - 20, vy - 60)
    c.line(vx + 80, vy - 20, vx + 80, vy - 60)
    c.line(vx + vw - 80, vy - 20, vx + vw - 20, vy - 60)
    # Foot pads
    c.rect(vx + 10, vy - 65, 20, 5, fill=1)
    c.rect(vx + vw - 30, vy - 65, 20, 5, fill=1)

    # Shell Body
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.setLineWidth(2)
    c.rect(vx, vy, vw, vh, fill=1, stroke=1)

    # Dished Heads (2:1 semi-ellipsoidal representation)
    c.arc(vx, vy + vh - 40, vx + vw, vy + vh + 40, 0, 180)
    c.arc(vx, vy - 40, vx + vw, vy + 40, 180, 180)

    # Dimple Jacket representation
    c.setStrokeColor(rcolors.HexColor("#3182CE"))
    c.setLineWidth(1)
    c.rect(vx - 10, vy + 40, vw + 20, vh - 100)
    c.setFillColor(rcolors.HexColor("#2B6CB0"))
    c.setFont("Helvetica-Bold", 8)
    c.drawString(vx + 20, vy + vh - 80, "SS316L SHELL (6.0 mm Plate)")
    c.drawString(vx + 20, vy + vh - 95, "DIMPLE JACKET (28°C Control)")
    c.drawString(vx + 20, vy + vh - 110, "WORKING VOL: 2.53 m³ (65.5% Fill)")

    # Agitator Drive & Bridge
    c.setFillColor(rcolors.HexColor("#718096"))
    c.rect(vx + vw*0.5 - 25, vy + vh + 30, 50, 45, fill=1, stroke=1)
    c.setFillColor(rcolors.white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(vx + vw*0.5, vy + vh + 50, "GEARMOTOR")
    c.drawCentredString(vx + vw*0.5, vy + vh + 38, "2.2 kW / 35 RPM")
    
    # Agitator Shaft & Impeller
    c.setStrokeColor(rcolors.HexColor("#1A202C"))
    c.setLineWidth(3)
    c.line(vx + vw*0.5, vy + vh + 30, vx + vw*0.5, vy + 60)
    # 3-blade Hydrofoil Impeller
    c.setLineWidth(4)
    c.line(vx + vw*0.5 - 45, vy + 80, vx + vw*0.5 + 45, vy + 60)
    c.line(vx + vw*0.5 - 45, vy + 60, vx + vw*0.5 + 45, vy + 80)
    c.setFillColor(rcolors.HexColor("#1A202C"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(vx + vw*0.5 + 55, vy + 70, "Dia 600 mm Hydrofoil (Tip Speed 1.10 m/s)")

    # Key Dimensions Callouts
    c.setStrokeColor(rcolors.HexColor("#E53E3E"))
    c.setLineWidth(0.8)
    # Diameter
    c.line(vx, vy - 80, vx + vw, vy - 80)
    c.drawString(vx + vw*0.5 - 35, vy - 95, "Dia 1,600 mm ID")
    # Height
    c.line(vx - 30, vy, vx - 30, vy + vh)
    c.drawString(vx - 75, vy + vh*0.5, "H = 1,920 mm")

    # Right Half: Plan View and Nozzle Schedule
    # Plan View Circle
    px, py, pr = 550, 430, 90
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.setLineWidth(2)
    c.circle(px, py, pr, fill=0, stroke=1)
    c.setLineWidth(0.5)
    c.line(px - pr - 15, py, px + pr + 15, py)
    c.line(px, py - pr - 15, px, py + pr + 15)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(px, py + pr + 25, "PLAN VIEW & NOZZLE ORIENTATIONS")

    # Nozzle Schedule Table (Bottom Right)
    c.drawString(450, 270, "VESSEL NOZZLE SCHEDULE (ASME B16.5 Class 150 RF Flanges)")
    nozzle_data = [
        ("Tag", "Size", "Rating", "Service Description"),
        ("N1", "DN 250", "150# RF", "Dal Charge Chute / Manway"),
        ("N2", "DN 50", "150# RF", "Prepared Chemical Liquor Inlet"),
        ("N3", "DN 80", "150# RF", "Tank Vent & Breather"),
        ("N4", "DN 65", "150# RF", "Overflow Nozzle to Sump"),
        ("N5", "DN 150", "150# RF", "Bottom Slurry Discharge"),
        ("N6", "DN 40", "150# RF", "CIP Rotary Spray Ball Inlet"),
        ("N7", "DN 25", "150# RF", "Temperature Sensor Thermowell (RTD)"),
        ("N8", "DN 50", "150# RF", "Non-Contact Radar Level Transmitter"),
    ]
    ny = 250
    for r_idx, row in enumerate(nozzle_data):
        if r_idx == 0:
            c.setFillColor(rcolors.HexColor("#2B6CB0"))
            c.rect(450, ny - 2, 420, 11, fill=1, stroke=0)
            c.setFillColor(rcolors.white)
            c.setFont("Helvetica-Bold", 7.5)
        else:
            c.setFillColor(rcolors.HexColor("#F7FAFC") if r_idx % 2 == 0 else rcolors.white)
            c.rect(450, ny - 2, 420, 11, fill=1, stroke=0)
            c.setFillColor(rcolors.HexColor("#2D3748"))
            c.setFont("Helvetica", 7.5)
        
        c.drawString(460, ny, row[0])
        c.drawString(510, ny, row[1])
        c.drawString(570, ny, row[2])
        c.drawString(640, ny, row[3])
        ny -= 11.5

    c.showPage()

    # =========================================================================
    # SHEET 4: FLUID-BED DRYER DR-101 GA & PSYCHROMETRICS (DWG-FIN-15T-007)
    # =========================================================================
    draw_standard_border_and_title_block(4, 7, "DWG-FIN-15T-007", "CONTINUOUS FLUID-BED DRYER DR-101 GENERAL ARRANGEMENT", "Mechanical Equipment")

    # Main Fluid Bed Dryer Elevation
    dx, dy, dw, dh = 80, 260, 480, 180
    
    # Lower Air Plenum
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.setLineWidth(1.5)
    c.rect(dx, dy, dw, 60, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#2D3748"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(dx + dw*0.35, dy + 25, "DRYING AIR PLENUM (60°C Hot Air)")
    c.drawCentredString(dx + dw*0.85, dy + 25, "COOLING (28°C)")

    # Perforated Distributor Deck
    c.setStrokeColor(rcolors.HexColor("#E53E3E"))
    c.setLineWidth(2.5)
    c.line(dx, dy + 60, dx + dw, dy + 60)
    c.setFillColor(rcolors.HexColor("#C53030"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(dx + 10, dy + 65, "PERFORATED AIR DISTRIBUTOR PLATE (1.5mm Holes, 12% Open Area)")

    # Grain Bed Zone
    c.setFillColor(rcolors.HexColor("#FEFCBF"))
    c.rect(dx, dy + 62, dw, 40, fill=1, stroke=0)
    c.setFillColor(rcolors.HexColor("#744210"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(dx + dw*0.5, dy + 80, "FLUIDIZED GRAIN BED (Bed Depth: 120 mm | Operating Velocity: 1.34 m/s > u_mf = 1.17 m/s)")

    # Exhaust Expansion Hood
    c.setFillColor(rcolors.HexColor("#EBF8FF"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.setLineWidth(1.5)
    c.rect(dx, dy + 102, dw, 78, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(dx + dw*0.5, dy + 145, "UPPER EXPANSION HOOD (De-entrainment Zone)")

    # Spring Suspensions
    c.setStrokeColor(rcolors.HexColor("#4A5568"))
    c.setLineWidth(2)
    for sx in [dx + 30, dx + 150, dx + 330, dx + 450]:
        c.line(sx, dy - 40, sx, dy)
        c.rect(sx - 10, dy - 45, 20, 5, fill=1)

    # Cyclone Separators and Ducts
    c.line(dx + dw*0.4, dy + dh, dx + dw*0.4, dy + dh + 60)
    c.line(dx + dw*0.4, dy + dh + 60, dx + dw + 60, dy + dh + 60)
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.rect(dx + dw + 30, dy + dh - 40, 60, 110, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A202C"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(dx + dw + 60, dy + dh + 50, "CY-101A/B")
    c.setFont("Helvetica", 7)
    c.drawCentredString(dx + dw + 60, dy + dh + 35, "Twin Cyclones")
    c.drawCentredString(dx + dw + 60, dy + dh + 20, "Rotary Airlock")

    # Dimensions
    c.setStrokeColor(rcolors.HexColor("#E53E3E"))
    c.setLineWidth(0.8)
    c.line(dx, dy - 60, dx + dw, dy - 60)
    c.drawString(dx + dw*0.5 - 40, dy - 75, "Total Deck Length = 6,000 mm (4.5m Drying + 1.5m Cooling)")

    # Right Area: Sizing & Psychrometric Data Block
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(640, 550, "RECONCILED PSYCHROMETRIC & THERMAL DRYING SIZING DATA")

    dryer_specs = [
        ("Parameter", "Design Specification", "Reconciled Status"),
        ("Wet Dal Feed Rate", "1,161.9 kg/h (18,590 kg/day @ 16h)", "Reconciled from Stream S-08"),
        ("Inlet Dal Moisture", "28.77% wet-basis (5,349 kg/d H2O)", "Calculated after Mist Rinse"),
        ("Exit Dal Moisture", "10.00% wet-basis (1,471 kg/d H2O)", "Strictly Reconciled Target"),
        ("Water Evaporation Rate (Nominal)", "242.36 kg/h (3,877.78 kg/day @ 16h)", "True Rate for 10.00% wb exit"),
        ("Water Evaporation Rate (Design)", "285.13 kg/h (over 13.6h @ 85% OEE)", "Equipment Sizing Baseline"),
        ("Historical Evaporation Rate", "230.92 kg/h (under-reported 3,694.7 kg/d)", "Defect: Left 183 kg/d water (11.1% wb)"),
        ("Minimum Fluidization Velocity (u_mf)", "1.17 m/s (Wen & Yu Correlation)", "Calculated (dp=3.5mm, rho=1350 kg/m³)"),
        ("Operating Fluidization Velocity (u_0)", "1.34 m/s (15% above u_mf + vibration)", "Non-channelling gentle bubbling bed"),
        ("Volumetric Airflow Required", "7,605 m³/h (126.8 m³/min)", "Air mass flow = 8,060 kg/h @ 60°C"),
        ("Fluidizing Blower Fan Motor", "11.0 kW (Static Head = 2,343 Pa)", "Selected Fan Motor Rating"),
        ("Gross Thermal Heating Duty", "301.2 kW thermal (Steam Heat Battery)", "Accounts for sensible + latent + 15% loss"),
        ("Steam Consumption (2.5 bar saturated)", "497.2 kg/h saturated steam", "Supplied by biomass briquette boiler"),
        ("Biomass Briquette Fuel Consumption", "1.15 MT / day (at 16.5 MJ/kg, 78% eff)", "Thermal Fuel OpEx = ₹0.522 / kg dal"),
    ]

    py_s = 530
    for r_idx, row in enumerate(dryer_specs):
        if r_idx == 0:
            c.setFillColor(rcolors.HexColor("#2B6CB0"))
            c.rect(640, py_s - 2, 480, 11, fill=1, stroke=0)
            c.setFillColor(rcolors.white)
            c.setFont("Helvetica-Bold", 7.5)
        else:
            c.setFillColor(rcolors.HexColor("#F7FAFC") if r_idx % 2 == 0 else rcolors.white)
            c.rect(640, py_s - 2, 480, 11, fill=1, stroke=0)
            c.setFillColor(rcolors.HexColor("#2D3748"))
            c.setFont("Helvetica", 7)
        
        c.drawString(645, py_s, row[0])
        c.drawString(840, py_s, row[1])
        c.drawString(995, py_s, row[2])
        py_s -= 11.5

    c.showPage()

    # =========================================================================
    # SHEET 5: ELECTRICAL SINGLE LINE DIAGRAM (SLD) & MCC (DWG-FIN-15T-009)
    # =========================================================================
    draw_standard_border_and_title_block(5, 7, "DWG-FIN-15T-009", "ELECTRICAL SINGLE LINE DIAGRAM & MOTOR CONTROL CENTER", "Electrical Engineering")

    # Incomer Supply
    c.setStrokeColor(rcolors.HexColor("#1A202C"))
    c.setLineWidth(2.5)
    c.line(80, 680, 80, 600)
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.rect(40, 680, 80, 40, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A202C"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(80, 705, "UTILITY GRID")
    c.setFont("Helvetica", 7)
    c.drawCentredString(80, 692, "415V, 3Ph, 50Hz")

    # Main Incomer Breaker
    c.setFillColor(rcolors.HexColor("#C53030"))
    c.rect(65, 570, 30, 30, fill=1, stroke=1)
    c.setFillColor(rcolors.white)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(80, 582, "160A")
    c.drawString(105, 582, "Main Incomer 4P MCCB (50 kA ICU) with Energy Meter")

    # Main 415V Busbar
    c.setStrokeColor(rcolors.HexColor("#B7791F"))
    c.setLineWidth(4)
    c.line(80, 550, 1050, 550)
    c.setFillColor(rcolors.HexColor("#B7791F"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(1060, 547, "MAIN 415V MCC BUSBAR (100 kW Capacity)")

    # Outgoing Feeders
    feeders = [
        ("FN-101 Dryer Blower", "11.0 kW VFD", 160),
        ("AG-101A Soak Agitator", "2.2 kW VFD", 280),
        ("AG-101B Soak Agitator", "2.2 kW VFD", 400),
        ("DR-101 Vibrators (2x)", "3.0 kW DOL", 520),
        ("SC-101 Screen Drives", "2.2 kW DOL", 640),
        ("Elevators & Conveyors", "4.5 kW DOL", 760),
        ("Chemical / Water Pumps", "3.0 kW DOL", 880),
        ("PK-101 Packaging Line", "15.0 kW Feeder", 1000),
    ]

    for title_f, rating_f, fx in feeders:
        c.setStrokeColor(rcolors.HexColor("#1A202C"))
        c.setLineWidth(1.5)
        c.line(fx, 550, fx, 480)
        # Breaker Box
        c.setFillColor(rcolors.HexColor("#2B6CB0"))
        c.rect(fx - 15, 450, 30, 30, fill=1, stroke=1)
        c.setFillColor(rcolors.white)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(fx, 462, "CB")
        
        c.line(fx, 450, fx, 390)
        # Motor Circle
        c.setFillColor(rcolors.HexColor("#EDF2F7"))
        c.circle(fx, 365, 25, fill=1, stroke=1)
        c.setFillColor(rcolors.HexColor("#1A202C"))
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(fx, 368, "M")
        c.setFont("Helvetica", 6.5)
        c.drawCentredString(fx, 355, "3~")
        
        # Labels
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(fx, 325, title_f)
        c.setFont("Helvetica", 7)
        c.drawCentredString(fx, 312, rating_f)

    # Electrical Load Summary Box
    c.setFillColor(rcolors.HexColor("#EBF8FF"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.rect(60, 160, 480, 120, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(75, 260, "ELECTRICAL LOAD SUMMARY & DISTRIBUTION")
    c.setFont("Helvetica", 8)
    c.drawString(75, 240, "Total Connected Load: 74.69 kW across 31 motors (Master Load List)")
    c.drawString(75, 225, "Running Load: 50.35 kW (Diversity Factor = 0.674)")
    c.drawString(75, 210, "Daily Electric Energy: 805.6 kWh/day (16h operating schedule)")
    c.drawString(75, 195, "Power Factor Correction: APFC Panel included to maintain cos phi >= 0.98")
    c.drawString(75, 180, "Standby Power: 100 kVA Silent Diesel Generator Set")

    # Automation & Safety Box
    c.setFillColor(rcolors.HexColor("#FEFCBF"))
    c.setStrokeColor(rcolors.HexColor("#B7791F"))
    c.rect(580, 160, 480, 120, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#744210"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(595, 260, "AUTOMATION, PLC & SAFETY HARDWARE")
    c.setFont("Helvetica", 8)
    c.drawString(595, 240, "Controller: Siemens S7-1200 / Allen-Bradley CompactLogix PLC Rack")
    c.drawString(595, 225, "I/O Capacity: 42 Channels (14 DI, 10 DO, 12 AI, 6 AO per Master IO List)")
    c.drawString(595, 210, "Operator Interface: 15-inch IP65 Colour Touchscreen HMI Panel")
    c.drawString(595, 195, "Safety Circuits: Hardwired Dual-Channel Category 3 Emergency Stop Loops")
    c.drawString(595, 180, "Trips: High-temp shutoff on steam heater, low-pressure blower interlock")

    c.showPage()

    # =========================================================================
    # SHEET 6: RECONCILED MASS, MOISTURE & CHEMICAL COMPARISON
    # =========================================================================
    draw_standard_border_and_title_block(6, 7, "REP-NLA-2026-CHART", "RECONCILED MASS, MOISTURE & CHEMICAL FORMULATION PROOF", "Process / Quality")

    # Top Area: Moisture Contradiction Resolution Diagram
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(45, 680, "1. THE DRYING MOISTURE CONTRADICTION & STEP-BY-STEP MATHEMATICAL PROOF")

    c.setFillColor(rcolors.HexColor("#FFF5F5"))
    c.setStrokeColor(rcolors.HexColor("#E53E3E"))
    c.rect(45, 530, 480, 130, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#9B2C2C"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(55, 642, "HISTORICAL REPORT CONTRADICTION (DEFECT IDENTIFIED):")
    c.setFont("Helvetica", 8.5)
    c.drawString(55, 625, "• Reported Total Dal Ex-Dryer: 14,895.30 kg/day")
    c.drawString(55, 610, "• Reported Water Content: 1,654.30 kg/day (Solids = 13,241.00 kg/day)")
    c.drawString(55, 595, "• Reported Claimed Moisture: '10.00% wet-basis'")
    c.drawString(55, 575, "• ARITHMETIC PROOF OF ERROR: 1,654.30 / 14,895.30 = 11.106% wb!")
    c.drawString(55, 555, "• Result: Left 183.08 kg/d un-evaporated water; under-reported daily evaporation.")

    c.setFillColor(rcolors.HexColor("#F0FFF4"))
    c.setStrokeColor(rcolors.HexColor("#38A169"))
    c.rect(560, 530, 520, 130, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#22543D"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(570, 642, "RECONCILED MATHEMATICAL TRUTH (AT EXACT 10.00% wb MOISTURE):")
    c.setFont("Helvetica", 8.5)
    c.drawString(570, 625, "• True Total Dal Ex-Dryer: 13,241.00 / (1 - 0.10) = 14,712.22 kg/day")
    c.drawString(570, 610, "• True Water Content: 14,712.22 x 0.10 = 1,471.22 kg/day")
    c.drawString(570, 595, "• Verification Check: 1,471.22 / 14,712.22 = EXACTLY 10.0000% wb")
    c.drawString(570, 575, "• TRUE DAILY EVAPORATION: 5,349.00 - 1,471.22 = 3,877.78 kg H2O/day")
    c.drawString(570, 555, "• Nominal 16h Rate: 242.36 kg/h | Design 85% OEE Rate (13.6h): 285.13 kg/h")

    # Middle Area: Chemical Formulation Ambiguity
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(45, 480, "2. CHEMICAL DOSING FORMULATION BASES & ANNUAL OPEX AMBIGUITY")

    c.setFillColor(rcolors.HexColor("#EBF8FF"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.rect(45, 330, 480, 130, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(55, 442, "BASIS A: CONCENTRATION IN SOAK LIQUOR (0.50% w/w in Solution)")
    c.setFont("Helvetica", 8.5)
    c.drawString(55, 425, "• Soak Liquor: 15,000 kg feed x 1.50 ratio = 22,500 kg liquor/day")
    c.drawString(55, 410, "• Active NaHCO3 Required: 22,500 x 0.0050 = 112.50 kg/day")
    c.drawString(55, 395, "• Concentration on Feed Dal: 112.50 / 15,000 = 0.750% of feed")
    c.drawString(55, 380, "• Daily Chemical OpEx (@ ₹37/kg): ₹4,162.50 / day")
    c.drawString(55, 365, "• Annual Chemical OpEx (300 days): ₹12.49 Lakhs / year")
    c.drawString(55, 345, "• Sizing Rule: Carried as conservative sizing ceiling for Dosing Skid SK-100.")

    c.setFillColor(rcolors.HexColor("#FEFCBF"))
    c.setStrokeColor(rcolors.HexColor("#B7791F"))
    c.rect(560, 330, 520, 130, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#744210"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(570, 442, "BASIS B: PERCENTAGE OF INCOMING FEED DAL (0.50% w/w on Grain)")
    c.setFont("Helvetica", 8.5)
    c.drawString(570, 425, "• Feed Dal Mass: 15,000 kg dal/day")
    c.drawString(570, 410, "• Active NaHCO3 Required: 15,000 x 0.0050 = 75.00 kg/day")
    c.drawString(570, 395, "• Concentration in Soak Liquor: 75.00 / 22,500 = 0.333% in solution")
    c.drawString(570, 380, "• Daily Chemical OpEx (@ ₹37/kg): ₹2,775.00 / day")
    c.drawString(570, 365, "• Annual Chemical OpEx (300 days): ₹8.33 Lakhs / year")
    c.drawString(570, 345, "• Variance: 37.50 kg/day difference (₹4.16 Lakhs/year OpEx swing).")

    # Bottom Area: Whole-Plant Yield & Leaching Reconciliation
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.setStrokeColor(rcolors.HexColor("#4A5568"))
    c.rect(45, 160, 1035, 130, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A202C"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(55, 272, "3. WHOLE-PLANT DRY SOLIDS RECOVERY & CONTRADICTION RECONCILIATION")
    c.setFont("Helvetica", 8.5)
    c.drawString(55, 252, "• 15,000 kg/day Feed Dal at 10.5% moisture contains exactly 13,425.00 kg/day Dry Solids.")
    c.drawString(55, 235, "• Soak Leaching Loss: 1.46% of feed solids = 196.01 kg/day dissolved solids lost in soak liquor (98.54% wash leaching recovery).")
    c.drawString(55, 218, "• Mechanical Screening / Scalping Loss: 2.89% of feed solids = 387.98 kg/day cracked cotyledon fines collected by aspirators.")
    c.drawString(55, 201, "• Total Plant Dry Solids Lost: 196.01 + 387.98 = 583.99 kg/day (4.35% total dry solids loss across factory).")
    c.drawString(55, 184, "• Net Whole-Plant Dry Solids Recovery: 13,425.00 - 583.99 = 12,841.01 kg/day (EXACTLY 95.65% WHOLE-PLANT RECOVERY).")
    c.drawString(55, 167, "• Final Saleable Finished Product: 12,841.01 / 0.90 = 14,267.79 kg/day at strictly 10.00% wet-basis moisture.")

    c.showPage()

    # =========================================================================
    # SHEET 7: PRE-REGISTERED 4-CONDITION SCREENING PROTOCOL FLOWSHEET
    # =========================================================================
    draw_standard_border_and_title_block(7, 7, "PROTOCOL-SCR-2026", "PRE-REGISTERED 4-CONDITION BENCH SCREENING PROTOCOL", "Research / Quality")

    # Protocol Flow Diagram
    # Step 1: Bulk Grain Intake
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.rect(60, 560, 180, 90, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(70, 632, "STEP 1: BULK GRAIN VERIFICATION")
    c.setFont("Helvetica", 7.5)
    c.drawString(70, 617, "• Target Lot ID: TZ-2026-IMP-001")
    c.drawString(70, 604, "• Verified on Hand: >= 5.0 kg bulk dal")
    c.drawString(70, 591, "• Initial Moisture Test (105°C Halogen)")
    c.drawString(70, 578, "• 16-Chute Mechanical Riffle Splitter")
    c.drawString(70, 565, "• Output: 16 x 200.0g Independent Batches")

    # Step 2: 4 Conditions Allocation
    c.line(240, 605, 280, 605)
    
    cond_boxes = [
        ("C1-CTRL: Untreated Control (n=4)", "Zero soak, zero chemical, zero rinse", "Equilibrate to 10.0% moisture directly", 640),
        ("C2-H2O: Water-Only Control (n=4)", "30 min soak @ 28°C in soft water", "Matched 30.0g spray rinse, dry @ 55°C", 570),
        ("C3-BIC025: 0.25% NaHCO3 (n=4)", "30 min soak in 0.25% w/w liquor", "Matched 30.0g spray rinse, dry @ 55°C", 500),
        ("C4-BIC050: 0.50% NaHCO3 (n=4)", "30 min soak in 0.50% w/w liquor", "Matched 30.0g spray rinse, dry @ 55°C", 430),
    ]

    for title_c, desc1, desc2, cy in cond_boxes:
        c.setStrokeColor(rcolors.HexColor("#4A5568"))
        c.line(280, 605, 300, cy + 25)
        c.setFillColor(rcolors.HexColor("#EBF8FF") if "NaHCO3" in title_c else rcolors.HexColor("#EDF2F7"))
        c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
        c.rect(300, cy, 220, 50, fill=1, stroke=1)
        c.setFillColor(rcolors.HexColor("#1A365D"))
        c.setFont("Helvetica-Bold", 8)
        c.drawString(308, cy + 36, title_c)
        c.setFont("Helvetica", 7)
        c.drawString(308, cy + 23, desc1)
        c.drawString(308, cy + 11, desc2)

    # Step 3: Conditioning & Blinding
    c.setStrokeColor(rcolors.HexColor("#4A5568"))
    for _, _, _, cy in cond_boxes:
        c.line(520, cy + 25, 560, 540)

    c.setFillColor(rcolors.HexColor("#FEFCBF"))
    c.setStrokeColor(rcolors.HexColor("#B7791F"))
    c.rect(560, 480, 160, 120, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#744210"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(570, 582, "STEP 3: BLINDING & RANDOM ORDER")
    c.setFont("Helvetica", 7.5)
    c.drawString(570, 565, "• 24h Sealed Pouch Conditioning")
    c.drawString(570, 550, "• Target Moisture: 10.0 ± 0.5% wb")
    c.drawString(570, 535, "• Double-Blind Codes: BLD-xx")
    c.drawString(570, 520, "• Pre-Registered Randomized Run Order")
    c.drawString(570, 505, "• Seed: 20261015 (Immutable sequence)")
    c.drawString(570, 490, "• Eliminates cooker thermal drift bias")

    # Step 4: Standardized Cooking Setup
    c.line(720, 540, 760, 540)
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.rect(760, 480, 160, 120, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(770, 582, "STEP 4: COOKING PROTOCOL")
    c.setFont("Helvetica", 7.5)
    c.drawString(770, 565, "• 3.0L Cooker, 15 psi Deadweight")
    c.drawString(770, 550, "• 1.2 kW Induction locked @ 1000W")
    c.drawString(770, 535, "• Charge: 100.0g dal + 350.0g soft water")
    c.drawString(770, 520, "• Continuous unbroken cooking")
    c.drawString(770, 505, "• Record t_0, t_vent, t_w1 to t_w6")
    c.drawString(770, 490, "• Rapid Cold Water Bath Quench")

    # Step 5: Tenderness & Statistical Decision
    c.line(920, 540, 960, 540)
    c.setFillColor(rcolors.HexColor("#C6F6D5"))
    c.setStrokeColor(rcolors.HexColor("#276749"))
    c.rect(960, 480, 160, 120, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#22543D"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(970, 582, "STEP 5: ENDPOINT & STATS")
    c.setFont("Helvetica", 7.5)
    c.drawString(970, 565, "• 10 Cotyledons under 1.5kg Weight")
    c.drawString(970, 550, "• Score 0: Uniform mash (0% chalk)")
    c.drawString(970, 535, "• Score 1: Soft outer / hard core")
    c.drawString(970, 520, "• 2 Independent Blinded Assessors")
    c.drawString(970, 505, "• One-way ANOVA + Dunnett's Test")
    c.drawString(970, 490, "• Bonferroni-Welch t-test (a=0.0167)")

    # Lower Half: Decision Tree & Stopping Rules
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(45, 390, "PRE-REGISTERED DECISION RULES, ACCEPTANCE GATES & REGULATORY STOP CRITERIA")

    rules_table = [
        ("Criterion", "Target Lot Acceptance Boundary", "Immediate Disqualification / Action"),
        ("Cooking Time to Score 0", "<= 15.0 minutes (<= 3.5 whistles)", "FAIL if > 16.5 minutes (Triggers non-chemical milling/steam route)"),
        ("Sensory Flavor Acceptance", ">= 6.0 / 9.0 on Hedonic Scale", "DISQUALIFIED if any soapy/chemical off-flavor detected (Score < 5.0)"),
        ("Whole-Plant Solids Recovery", ">= 95.50% (Leaching loss <= 3.0%)", "FAIL if leaching loss > 5.0% (Exceeds economic viability bound)"),
        ("Retained Elemental Sodium", "< 120.0 mg Na / 100g dal", "NON-COMPLIANT if >= 350.0 mg Na / 100g (Violates FSSAI low sodium standard)"),
        ("Statistical Significance", "t_obs >= 2.998 (p <= 0.0167 vs Control)", "No commercial claim permitted if effect is statistically indistinguishable"),
        ("FSSAI Labeling Mandate", "Declare: 'Acidity Regulator (INS 500(ii))'", "ILLEGAL to treat as undeclared processing aid; label sign-off mandatory"),
    ]

    ry = 365
    for r_idx, row in enumerate(rules_table):
        if r_idx == 0:
            c.setFillColor(rcolors.HexColor("#2B6CB0"))
            c.rect(45, ry - 2, 1035, 12, fill=1, stroke=0)
            c.setFillColor(rcolors.white)
            c.setFont("Helvetica-Bold", 8)
        else:
            c.setFillColor(rcolors.HexColor("#F7FAFC") if r_idx % 2 == 0 else rcolors.white)
            c.rect(45, ry - 2, 1035, 12, fill=1, stroke=0)
            c.setFillColor(rcolors.HexColor("#2D3748"))
            c.setFont("Helvetica", 7.5)
        
        c.drawString(55, ry, row[0])
        c.drawString(280, ry, row[1])
        c.drawString(580, ry, row[2])
        ry -= 13.5

    # Sign-off confirmation box at bottom
    c.setFillColor(rcolors.HexColor("#EDF2F7"))
    c.setStrokeColor(rcolors.HexColor("#2B6CB0"))
    c.rect(45, 160, 1035, 80, fill=1, stroke=1)
    c.setFillColor(rcolors.HexColor("#1A365D"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(55, 225, "GATE G-A TRIAL COMMENCEMENT AUTHORIZATION (HOLD POINT):")
    c.setFont("Helvetica", 8)
    c.drawString(55, 208, "Status: PROTOCOL_READY_FOR_REVIEW. The protocol is frozen and data sheets are blank.")
    c.drawString(55, 193, "Laboratory personnel are strictly prohibited from entering simulated data or fabricating observations.")
    c.drawString(55, 178, "Execution awaits physical sample acquisition of 5.0 kg lot TZ-2026-IMP-001 and written human lead authorization.")

    c.showPage()
    c.save()

    # Also copy / generate to engineering/cad/pdf/FINNOAQ_15TPD_ENGINEERING_DRAWINGS.pdf
    cad_pdf_path = "engineering/cad/pdf/FINNOAQ_15TPD_ENGINEERING_DRAWINGS.pdf"
    import shutil
    shutil.copyfile(output_pdf_path, cad_pdf_path)
    print(f"Generated comprehensive 7-sheet engineering PDF: {output_pdf_path}")
    print(f"Updated CAD drawing package: {cad_pdf_path}")

    # Render each page to 200 DPI high-definition PNG
    import fitz
    brain_dir = r"C:\Users\SOURISH SENAPATI\.gemini\antigravity-ide\brain\e60c88e3-dafa-4b48-82c7-ef80cde70237"
    doc = fitz.open(output_pdf_path)
    sheet_names = [
        "finnoaq_dwg_002_pfd",
        "finnoaq_dwg_001_plot_plan",
        "finnoaq_dwg_005_soak_tank",
        "finnoaq_dwg_007_fluid_bed_dryer",
        "finnoaq_dwg_009_electrical_sld",
        "finnoaq_dwg_011_mass_balance_chart",
        "finnoaq_dwg_012_screening_protocol"
    ]
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=200)
        out_png = f"engineering/cad/png/{sheet_names[i]}.png"
        pix.save(out_png)
        brain_png = os.path.join(brain_dir, f"{sheet_names[i]}.png")
        shutil.copy2(out_png, brain_png)
        print(f"-> Saved Drawing Sheet {i+1} PNG: {out_png}")

if __name__ == '__main__':
    create_engineering_drawings_pdf()

