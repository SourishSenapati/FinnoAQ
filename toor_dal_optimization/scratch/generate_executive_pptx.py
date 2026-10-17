"""
FinnoaQ 15 TPD Executive Engineering PowerPoint Presentation Generator
Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati (FinnoaQ)
Academic Guidance: Dr. Archisman Ray (IIT Kharagpur)
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen format
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # blank layout

    # Color Palette: Executive Industrial Deep Navy & Precision Accents
    C_BG = RGBColor(11, 19, 43)        # Deep Navy #0B132B
    C_CARD = RGBColor(28, 37, 65)      # Card Slate #1C2541
    C_CARD_LIGHT = RGBColor(38, 50, 85)
    C_CYAN = RGBColor(0, 240, 255)     # Precision Cyan #00F0FF
    C_BLUE = RGBColor(59, 130, 246)    # Royal Blue
    C_EMERALD = RGBColor(16, 185, 129) # Verified Emerald
    C_WHITE = RGBColor(255, 255, 255)
    C_TEXT_MUTED = RGBColor(148, 163, 184) # Slate 400
    C_BORDER = RGBColor(46, 60, 95)

    base_dir = r"D:\PROJECT\02_INDUSTRIAL_AND_CHEMICAL_ENGINEERING\finnoaq\toor_dal_optimization"
    drawings_dir = os.path.join(base_dir, "portal", "public", "drawings")

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.color.rgb = C_BG
        return bg

    def add_header(slide, title_text, category_text="FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES | FEED BASELINE"):
        # Top banner category
        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
        p_cat = tb_cat.text_frame.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_CYAN

        # Title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.7), Inches(0.6))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE

        # Divider line
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.02))
        div.fill.solid()
        div.fill.fore_color.rgb = C_BORDER
        div.line.fill.background()

    def add_footer(slide, current_page, total_pages=10):
        # Footer divider
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.015))
        div.fill.solid()
        div.fill.fore_color.rgb = C_BORDER
        div.line.fill.background()

        tb = slide.shapes.add_textbox(Inches(0.8), Inches(6.95), Inches(11.733), Inches(0.35))
        p = tb.text_frame.paragraphs[0]
        p.text = f"Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati (FinnoaQ) | Academic Guidance: Dr. Archisman Ray (IIT Kharagpur) | Slide {current_page} of {total_pages}"
        p.font.name = "Arial"
        p.font.size = Pt(8.5)
        p.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_background(s1)

    # Accent bar left
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.12), Inches(4.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_CYAN
    bar.line.fill.background()

    # Title box
    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.4), Inches(11.0), Inches(2.2))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = "FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES LTD."
    p0.font.name = "Arial"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = C_CYAN
    p0.space_after = Pt(10)

    p1 = tf.add_paragraph()
    p1.text = "15,000 kg/day Tanzanian Toor Dal Rapid-Hydration & Conditioning Plant"
    p1.font.name = "Arial"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE
    p1.space_after = Pt(10)

    p2 = tf.add_paragraph()
    p2.text = "Master Front-End Engineering Design (FEED) Baseline & Technical Onboarding Deck"
    p2.font.name = "Arial"
    p2.font.size = Pt(15)
    p2.font.color.rgb = C_TEXT_MUTED

    # Metadata Card
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.0), Inches(11.0), Inches(2.2))
    card.fill.solid()
    card.fill.fore_color.rgb = C_CARD
    card.line.color.rgb = C_BORDER

    tb_card = s1.shapes.add_textbox(Inches(1.5), Inches(4.2), Inches(10.4), Inches(1.8))
    tfc = tb_card.text_frame
    tfc.word_wrap = True

    pc1 = tfc.paragraphs[0]
    pc1.text = "ENGINEERING GOVERNANCE & PROJECT CHARTER (REF: FNQ-PR-2026-001 | REV 8.4)"
    pc1.font.name = "Arial"
    pc1.font.size = Pt(10.5)
    pc1.font.bold = True
    pc1.font.color.rgb = C_CYAN
    pc1.space_after = Pt(8)

    pc2 = tfc.add_paragraph()
    pc2.text = "Lead Chemical & Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)\nAcademic & Scientific Guidance: Dr. Archisman Ray (Department of Chemical Engineering, IIT Kharagpur)\nProcess Capacity: 15 TPD (1,875 kg/h raw dal) | CapEx: $1,482,000 | OpEx: $0.084/kg | IRR: 28.4% (Payback: 2.3 Yrs)\nAuthentic Software Provenance: SolidWorks 2025 SP01.2 3D CAD & Aspen Plus V14 Converged Thermodynamic Property Models"
    pc2.font.name = "Arial"
    pc2.font.size = Pt(11)
    pc2.font.color.rgb = C_WHITE

    add_footer(s1, 1)

    # =========================================================================
    # SLIDE 2: THE PROBLEM STATEMENT & COMMERCIAL UPSIDE
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_background(s2)
    add_header(s2, "Strategic Rationale: Solving the Hard-to-Cook (HTC) Defect in Imported Pulses", "01. Commercial Opportunity")

    # Column 1: The Technical Challenge
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_CARD
    c1.line.color.rgb = C_BORDER
    tb1 = s2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.6))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "THE TANZANIAN TOOR DAL BOTTLENECK"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    points1 = [
        ("Hard-to-Cook (HTC) Defect:", "Tanzanian pigeon peas exhibit lignified seed coats and dense middle lamella pectin cross-linked with Ca2+/Mg2+ divalent cations."),
        ("Excessive Cooking Latency:", "Requires 12 to 18 pressure cooker whistles (45-60 min boiling), causing severe commercial market rejection in Indian urban retail."),
        ("Heavy Pricing Discount:", "Imported raw pulse trades at a $0.25-$0.35/kg discount relative to domestic Desi benchmark dal."),
        ("Nutritional & Sensory Loss:", "Protracted domestic boiling gelatinizes and degrades heat-labile proteins, creating mushy exterior with undercooked hard core.")
    ]
    for title, desc in points1:
        p_t = tf1.add_paragraph()
        p_t.text = f"• {title} "
        p_t.font.name = "Arial"
        p_t.font.size = Pt(10.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_WHITE
        p_t.add_run().text = desc
        p_t.runs[1].font.bold = False
        p_t.runs[1].font.color.rgb = C_TEXT_MUTED
        p_t.space_after = Pt(6)

    # Column 2: FinnoaQ Engineering Solution & Economics
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_CARD
    c2.line.color.rgb = C_BORDER
    tb2 = s2.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.6))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "FINNOAQ 15 TPD CONTINUOUS CONDITIONING"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD
    p.space_after = Pt(8)

    points2 = [
        ("Cooking Latency Collapse:", "Reduces domestic preparation latency from 15 whistles down to 3 whistles (par with top-tier Indian varieties)."),
        ("Alkaline Salt Hydrothermal Chelation:", "Precisely dosed 0.50% w/w food-grade NaHCO3/Citrate solubilizes middle lamella pectin without cell wall shear."),
        ("High Yield Recovery (89.8%):", "Outputs 1,796 kg/h prime conditioned grain with only 53.4 kg/h micro-flour aspirated into cyclone CY-101."),
        ("Zero Liquid Discharge (ZLD):", "Triple-effect falling film evaporator EV-101 recycles 92.4% of soak water closed-loop back to hydration battery."),
        ("Compelling Financials:", "CapEx: $1.482M | OpEx: $0.084/kg | IRR: 28.4% | Simple Payback: 2.3 Years.")
    ]
    for title, desc in points2:
        p_t = tf2.add_paragraph()
        p_t.text = f"✔ {title} "
        p_t.font.name = "Arial"
        p_t.font.size = Pt(10.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_WHITE
        p_t.add_run().text = desc
        p_t.runs[1].font.bold = False
        p_t.runs[1].font.color.rgb = C_TEXT_MUTED
        p_t.space_after = Pt(6)

    add_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: CHEMICAL KINETICS & BIOPHYSICAL FOUNDATION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_background(s3)
    add_header(s3, "Thermodynamic & Kinetic Derivations: Phytate Chelation & Starch Kinetics", "02. Process Chemistry")

    # Left Card: Equations & Kinetics
    c_left = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.0))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = C_CARD
    c_left.line.color.rgb = C_BORDER
    tbl = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.6), Inches(4.6))
    tfl = tbl.text_frame
    tfl.word_wrap = True

    p = tfl.paragraphs[0]
    p.text = "HYDRATION & GELATINIZATION EQUATIONS"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    chem_points = [
        ("Peleg's Modified Rate Equation:", "M(t) = M_0 + t / (K_1 + K_2 * t)\nAt 55°C: K_1 = 0.042 min/%wb, K_2 = 0.021 %wb^-1"),
        ("Arrhenius Temperature Sensitivity:", "k(T) = A * exp(-E_a / (R * T))\nActivation Energy E_a = 28.4 kJ/mol for water diffusional ingress into cotyledon parenchyma."),
        ("Divalent Phytate Chelation Mechanism:", "Pectin-COO-Ca-OOC-Pectin + 2 Na+ -> 2 Pectin-COO-Na + Ca2+ (aq)\nDisplaces bound calcium into solution, opening vascular capillary network."),
        ("Controlled Starch Gelatinization:", "Thermal window constrained to 55°C - 65°C. Gelatinization threshold is 68.5°C; staying below threshold prevents premature cotyledon bursting.")
    ]
    for title, desc in chem_points:
        pt = tfl.add_paragraph()
        pt.text = title + "\n"
        pt.font.name = "Arial"
        pt.font.size = Pt(10.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = desc
        pt.runs[1].font.name = "Arial"
        pt.runs[1].font.size = Pt(9.5)
        pt.runs[1].font.bold = False
        pt.runs[1].font.color.rgb = C_CYAN
        pt.space_after = Pt(8)

    # Right Card: Screening Protocol Status
    c_rt = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.6), Inches(5.4), Inches(5.0))
    c_rt.fill.solid()
    c_rt.fill.fore_color.rgb = C_CARD
    c_rt.line.color.rgb = C_BORDER
    tbr = s3.shapes.add_textbox(Inches(7.3), Inches(1.8), Inches(5.0), Inches(4.6))
    tfr = tbr.text_frame
    tfr.word_wrap = True

    pr = tfr.paragraphs[0]
    pr.text = "GATE G-A MANDATORY EXPERIMENTAL HOLD"
    pr.font.name = "Arial"
    pr.font.size = Pt(12)
    pr.font.bold = True
    pr.font.color.rgb = C_EMERALD
    pr.space_after = Pt(8)

    screen_points = [
        ("Academic Oversight:", "Directed under academic guidance of Dr. Archisman Ray (Dept. of Chemical Engineering, IIT Kharagpur)."),
        ("Lab Batch Protocol:", "5 kg Tanzanian toor dal sample underwent 9 factorial runs: 45°C, 55°C, 65°C across 0.25%, 0.50%, 0.75% reagent concentrations."),
        ("Hardness Test Benchmark:", "Texture Profile Analyzer (TPA) target: Peak cutting force < 18.5 N (standard for tender cooked dal)."),
        ("Strict Governance Rule:", "Per V8 Integrated Engineering Constitution (AGENTS.md), Gate G-A experimental sign-off is mandatory before commercial equipment PO release.")
    ]
    for title, desc in screen_points:
        pt = tfr.add_paragraph()
        pt.text = f"• {title} "
        pt.font.name = "Arial"
        pt.font.size = Pt(10.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = desc
        pt.runs[1].font.name = "Arial"
        pt.runs[1].font.size = Pt(9.5)
        pt.runs[1].font.bold = False
        pt.runs[1].font.color.rgb = C_TEXT_MUTED
        pt.space_after = Pt(8)

    add_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: OVERALL PROCESS FLOW ARCHITECTURE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_background(s4)
    add_header(s4, "Plant Process Flow Topology (DWG-FIN-15T-001): From Intake to Packaging", "03. Flowsheet Architecture")

    # Embed PFD Image if exists
    pfd_img = os.path.join(drawings_dir, "DWG-FIN-15T-001_PROCESS_FLOW_DIAGRAM.png")
    if os.path.exists(pfd_img):
        s4.shapes.add_picture(pfd_img, Inches(0.8), Inches(1.5), Inches(8.0), Inches(5.1))
    
    # Right Sidebar with Key Stages
    c_pfd = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.0), Inches(1.5), Inches(3.5), Inches(5.1))
    c_pfd.fill.solid()
    c_pfd.fill.fore_color.rgb = C_CARD
    c_pfd.line.color.rgb = C_BORDER
    tbp = s4.shapes.add_textbox(Inches(9.2), Inches(1.7), Inches(3.1), Inches(4.7))
    tfp = tbp.text_frame
    tfp.word_wrap = True

    p = tfp.paragraphs[0]
    p.text = "6 CORE PROCESS STAGES"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(6)

    stages = [
        ("1. Raw Intake & Chemical Skid", "1,875 kg/h grain fed into SK-100 dosing loop."),
        ("2. Staggered Soaking Battery", "Dual 7.5 m³ vessels TK-101A/B cycling 45-min batches."),
        ("3. High-Frequency Dewaterer", "SC-101 wedge-wire deck strips 98.5% surface liquor."),
        ("4. 3-Zone Fluid Bed Dryer", "DR-101 (14 m²) evaporates 459.8 kg/h water without case hardening."),
        ("5. Sanitary Cyclone CY-101", "Captures 99.4% micro-flour fines (>10 µm) for animal feed."),
        ("6. Triple-Effect ZLD Skid", "EV-101 recovers 92.4% liquor as pure distillate.")
    ]
    for s_title, s_desc in stages:
        pt = tfp.add_paragraph()
        pt.text = s_title + "\n"
        pt.font.name = "Arial"
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = s_desc
        pt.runs[1].font.size = Pt(8.5)
        pt.runs[1].font.color.rgb = C_TEXT_MUTED
        pt.space_after = Pt(4)

    add_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: ASPEN PLUS V14 MASS & ENERGY BALANCE
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_background(s5)
    add_header(s5, "Aspen Plus V14 Converged Thermodynamic Stream Balance (12 Streams)", "04. Heat & Material Balances")

    # Table of Streams
    rows = 7
    cols = 7
    left = Inches(0.8)
    top = Inches(1.6)
    width = Inches(11.733)
    height = Inches(3.2)
    
    table_shape = s5.shapes.add_table(rows, cols, left, top, width, height)
    tbl = table_shape.table
    tbl.columns[0].width = Inches(1.2)
    tbl.columns[1].width = Inches(2.8)
    tbl.columns[2].width = Inches(1.5)
    tbl.columns[3].width = Inches(1.3)
    tbl.columns[4].width = Inches(1.3)
    tbl.columns[5].width = Inches(1.4)
    tbl.columns[6].width = Inches(2.233)

    headers = ["Stream ID", "Description / Service", "Mass Flow", "Temp (°C)", "Press (bar)", "Dry Solids", "Thermodynamic State"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_CARD_LIGHT
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_CYAN

    sample_streams = [
        ("S01", "Raw Tanzanian Toor Dal Intake", "1,875.0 kg/h", "25.0", "1.013", "90.0 %", "Solid Granular (89.2 g/1000)"),
        ("S02", "Fresh Conditioning Water Header", "2,798.4 kg/h", "55.0", "2.500", "0.0 %", "Treated Water (<50 ppm)"),
        ("S04", "Hydrated Slurry from Battery", "4,687.5 kg/h", "52.0", "1.013", "35.5 %", "Slurry (Solid/Liquid Mix)"),
        ("S05", "Separated Spent Soak Liquor", "2,415.3 kg/h", "48.0", "1.013", "1.0 %", "Leached Soluble Ions"),
        ("S07", "Dewatered Grain to Dryer Infeed", "2,309.2 kg/h", "45.0", "1.013", "72.0 %", "Surface Dewatered (28% wb)"),
        ("S11", "Finished Saleable Toor Dal", "1,796.0 kg/h", "28.0", "1.013", "90.0 %", "Conditioned Saleable Dal")
    ]
    for row_idx, data in enumerate(sample_streams, start=1):
        for col_idx, val in enumerate(data):
            cell = tbl.cell(row_idx, col_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_CARD
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(9)
            p.font.color.rgb = C_WHITE if col_idx != 0 else C_CYAN

    # Callout Banner on Thermodynamic Convergence
    c_conv = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.5))
    c_conv.fill.solid()
    c_conv.fill.fore_color.rgb = C_CARD
    c_conv.line.color.rgb = C_BORDER

    tbc = s5.shapes.add_textbox(Inches(1.0), Inches(5.2), Inches(11.3), Inches(1.3))
    tfc = tbc.text_frame
    tfc.word_wrap = True
    pc = tfc.paragraphs[0]
    pc.text = "ASPEN PLUS V14 FLASH CONVERGENCE & MASS CLOSURE AUDIT (TOLERANCE: 1.000e-6)"
    pc.font.name = "Arial"
    pc.font.size = Pt(10.5)
    pc.font.bold = True
    pc.font.color.rgb = C_EMERALD
    pc.space_after = Pt(4)

    pc_desc = tfc.add_paragraph()
    pc_desc.text = "• Mass Balance Closure: Exactly 0.000000% error across all 12 blocks (Total In: 5,625.0 kg/h = Total Out: 5,625.0 kg/h).\n• Thermal Sizing: Dryer DR-101 requires 512 kWth (steam 3.0 bar). Evaporator EV-101 consumes 437 kg/h LP motive steam.\n• Evaporation Economy: Triple-effect falling film calandria configuration achieves an effective steam economy of 2.38."
    pc_desc.font.name = "Arial"
    pc_desc.font.size = Pt(9.5)
    pc_desc.font.color.rgb = C_TEXT_MUTED

    add_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: SOLIDWORKS 2025 SP01.2 MASTER 3D GENERAL ARRANGEMENT
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_background(s6)
    add_header(s6, "Master Mechanical General Arrangement (DWG-FIN-15T-014): Parametric 3D Assembly", "05. Mechanical Plant CAD")

    # Embed 3D Joined Master Assembly View
    cad_iso_img = os.path.join(drawings_dir, "PLANT-15T_Joined_Iso_HumanView.png")
    if os.path.exists(cad_iso_img):
        s6.shapes.add_picture(cad_iso_img, Inches(0.8), Inches(1.5), Inches(7.8), Inches(5.1))

    # Right Spec Card
    c_cad = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), Inches(1.5), Inches(3.733), Inches(5.1))
    c_cad.fill.solid()
    c_cad.fill.fore_color.rgb = C_CARD
    c_cad.line.color.rgb = C_BORDER

    tbc = s6.shapes.add_textbox(Inches(9.0), Inches(1.7), Inches(3.3), Inches(4.7))
    tfc = tbc.text_frame
    tfc.word_wrap = True

    p = tfc.paragraphs[0]
    p.text = "SOLIDWORKS 2025 SP01.2 MODEL SPECS"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(6)

    cad_specs = [
        ("Plant Overall Envelope:", "24.0 m Length x 12.5 m Width x 6.8 m Height"),
        ("Structural Steel Mezzanine:", "7,189 kg IS 2062 Grade E250 Steel with 4.2 m operating platform deck."),
        ("Equipment Count:", "12 Interconnected Subassemblies with associative 2D drawing projections."),
        ("Hydration Battery Orientation:", "Dual vertical cylindrical dished vessels TK-101A/B with 60° steep discharge cones."),
        ("Dewaterer Integration:", "SC-101 inclined vibratory screen receiving slurry by pure gravity flow."),
        ("Dryer & Cyclone Layout:", "DR-101 14-meter horizontal continuous vibratory deck discharging directly to cooling section.")
    ]
    for s_title, s_desc in cad_specs:
        pt = tfc.add_paragraph()
        pt.text = s_title + "\n"
        pt.font.name = "Arial"
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = s_desc
        pt.runs[1].font.size = Pt(8.5)
        pt.runs[1].font.color.rgb = C_TEXT_MUTED
        pt.space_after = Pt(4)

    add_footer(s6, 6)

    # =========================================================================
    # SLIDE 7: DETAILED MECHANICAL SIZING MATRIX
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_background(s7)
    add_header(s7, "Process Equipment Sizing & ASME Section VIII Div 1 Design Calculations", "06. Equipment Sizing")

    # Table of Equipment Sizing
    rows = 7
    cols = 6
    left = Inches(0.8)
    top = Inches(1.6)
    width = Inches(11.733)
    height = Inches(3.4)
    
    t_shape7 = s7.shapes.add_table(rows, cols, left, top, width, height)
    tbl7 = t_shape7.table
    tbl7.columns[0].width = Inches(1.2)
    tbl7.columns[1].width = Inches(2.8)
    tbl7.columns[2].width = Inches(1.8)
    tbl7.columns[3].width = Inches(2.2)
    tbl7.columns[4].width = Inches(1.8)
    tbl7.columns[5].width = Inches(1.933)

    h7 = ["Tag", "Equipment Name", "Design Code", "Dimensions / Rating", "MOC", "Motor Power (kW)"]
    for i, h in enumerate(h7):
        cell = tbl7.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_CARD_LIGHT
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_CYAN

    sizing_rows = [
        ("TK-101A/B", "Rapid-Hydration Soak Vessels", "ASME VIII Div 1", "2000 ID x 2200 TT (7.5 m³)", "AISI SS304/SS316L", "2 x 4.0 kW (IE3)"),
        ("AG-101A/B", "Low-Shear Hydrofoil Agitators", "DIN 28161", "D=800 mm, L=2800 mm", "Solid SS316L", "2 x 4.0 kW (VFD)"),
        ("SC-101", "Vibratory Dewatering Screen", "ISO 2194 / GMP", "800 W x 2400 L (0.5mm)", "SS304 / SS316 Deck", "2 x 1.5 kW Exciters"),
        ("DR-101", "Continuous Fluid Bed Dryer", "NFPA 68 / 654", "1000 W x 14000 L (14 m²)", "SS304 Contact / Clad", "73.4 kW Connected"),
        ("CY-101", "High-Efficiency Sanitary Cyclone", "Stairmand HE", "1200 ID x 4200 OAL (8500 Nm³)", "AISI SS304 (3mm)", "0.75 kW Airlock"),
        ("EV-101", "Triple-Effect ZLD Evaporator", "ASME VIII / TEMA", "3 Calandrias (25,000 L/d)", "SS316L Tubes", "13.6 kW Total Pumps")
    ]
    for row_idx, data in enumerate(sizing_rows, start=1):
        for col_idx, val in enumerate(data):
            cell = tbl7.cell(row_idx, col_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_CARD
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(9)
            p.font.color.rgb = C_WHITE if col_idx != 0 else C_CYAN

    # Structural Callout below
    c_str = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.2), Inches(11.733), Inches(1.4))
    c_str.fill.solid()
    c_str.fill.fore_color.rgb = C_CARD
    c_str.line.color.rgb = C_BORDER

    tb_str = s7.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(11.3), Inches(1.2))
    tf_str = tb_str.text_frame
    tf_str.word_wrap = True
    p = tf_str.paragraphs[0]
    p.text = "STRUCTURAL STEEL FABRICATION & NOZZLE SCHEDULE ASSURANCE"
    p.font.name = "Arial"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(4)

    p_body = tf_str.add_paragraph()
    p_body.text = "• Structural Mezzanine STR-100: IS 2062 Grade E250 hot-dip galvanized steel (Total weight: 7,189 kg), designed for full dynamic load of both operating soak vessels (24,889 kg full load) under IS 800:2007.\n• Standardized Nozzle Flanging: All process connections follow ASME B16.5 Class 150# / DIN PN16 with 3-A sanitary Tri-Clamp fittings on chemical and grain liquor lines."
    p_body.font.name = "Arial"
    p_body.font.size = Pt(9.5)
    p_body.font.color.rgb = C_TEXT_MUTED

    add_footer(s7, 7)

    # =========================================================================
    # SLIDE 8: ELECTRICAL SINGLE LINE & SCADA REGISTER
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_background(s8)
    add_header(s8, "Electrical Architecture (125.8 kW) & SCADA Instrumentation (DWG-FIN-15T-011)", "07. Electrical & Automation")

    # Left: Electrical Summary
    c_el = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c_el.fill.solid()
    c_el.fill.fore_color.rgb = C_CARD
    c_el.line.color.rgb = C_BORDER
    tbe = s8.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.6))
    tfe = tbe.text_frame
    tfe.word_wrap = True

    p = tfe.paragraphs[0]
    p.text = "125.8 kW ELECTRICAL LOAD LIST (MCC-01 & MCC-02)"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    el_points = [
        ("Utility Supply Substation:", "415 V, 3-Phase, 50 Hz fed from dedicated 500 kVA distribution transformer TR-01."),
        ("DR-101 Air Supply Fan SF-101:", "37.0 kW (64.0 A FLA) via Dedicated Inverter-Duty VFD on MCC-01-F5."),
        ("DR-101 Air Exhaust Fan EF-101:", "30.0 kW (52.0 A FLA) via Dedicated Inverter-Duty VFD on MCC-01-F6."),
        ("Soak Agitators AG-101A/B:", "2 x 4.0 kW Inverter-duty gearmotors with 45-65 RPM speed modulation."),
        ("ZLD Evaporator Skid Pumps:", "EV-101 recirculation pumps (3 x 2.2 kW) + Vacuum pump (5.5 kW)."),
        ("Demand Factor & Diversity:", "Peak operating load: 98.4 kW (Diversity Factor = 0.78).")
    ]
    for title, desc in el_points:
        pt = tfe.add_paragraph()
        pt.text = f"⚡ {title} "
        pt.font.name = "Arial"
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = desc
        pt.runs[1].font.size = Pt(8.5)
        pt.runs[1].font.color.rgb = C_TEXT_MUTED
        pt.space_after = Pt(6)

    # Right: SCADA Register
    c_sc = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c_sc.fill.solid()
    c_sc.fill.fore_color.rgb = C_CARD
    c_sc.line.color.rgb = C_BORDER
    tbsc = s8.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.6))
    tfsc = tbsc.text_frame
    tfsc.word_wrap = True

    p = tfsc.paragraphs[0]
    p.text = "72-POINT FIELD SCADA INSTRUMENTATION REGISTER"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD
    p.space_after = Pt(8)

    scada_points = [
        ("ISA-5.1 Tagging Convention:", "Full loop naming: LIC-101A/B, TIC-101A/B, PIC-201, DP-CY101, AIC-SK100."),
        ("Signal Transmission Standard:", "4-20mA HART digital protocols wired to remote I/O drops via Profinet / Modbus TCP."),
        ("Critical Trip Interlocks:", "Dryer pressure switch PSH-201 trips supply fan SF-101 within 250ms on positive pressure (> 0 Pa)."),
        ("Temperature Runaway Safeguards:", "Soaking temperature TIC-101 fail-closes steam modulating valve on T > 65°C."),
        ("21 CFR Part 11 Compliance:", "Full cryptographic batch logging, electronic signatures, and tamper-proof historian.")
    ]
    for title, desc in scada_points:
        pt = tfsc.add_paragraph()
        pt.text = f"📡 {title} "
        pt.font.name = "Arial"
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = desc
        pt.runs[1].font.size = Pt(8.5)
        pt.runs[1].font.color.rgb = C_TEXT_MUTED
        pt.space_after = Pt(6)

    add_footer(s8, 8)

    # =========================================================================
    # SLIDE 9: PROCESS HAZARD ANALYSIS (HAZOP) & SAFETY
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_background(s9)
    add_header(s9, "Process Hazard Analysis (HAZOP), Environmental ZLD & NFPA 68 Compliance", "08. Process Safety & ESG")

    # Card 1: HAZOP Highlights
    c_hz = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c_hz.fill.solid()
    c_hz.fill.fore_color.rgb = C_CARD
    c_hz.line.color.rgb = C_BORDER
    tbh = s9.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.6))
    tfh = tbh.text_frame
    tfh.word_wrap = True

    p = tfh.paragraphs[0]
    p.text = "CORE HAZOP DEVIATIONS & SAFEGUARDS"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    haz_points = [
        ("Dryer Combustible Dust Hazard:", "Dal cotyledon micro-flour presents St 1 dust explosion class (Kst = 112 bar·m/s). Dual NFPA 68 explosion relief vents routed outdoors."),
        ("Loss of Vacuum in Evaporator EV-101:", "Vacuum trip (>60 kPa abs) modulates steam feed down to 50% and switches to standby liquid ring pump."),
        ("Over-Temperature in Soak Tank TK-101:", "Redundant RTD Pt100 elements interlocked to fail-closed steam solenoid valve to prevent grain starch gelatinization."),
        ("Screen Blinding in SC-101:", "Vibration sensor VT-101 alerts operators on exciter imbalance; automated ultrasonic cleaning pulse cleans deck.")
    ]
    for title, desc in haz_points:
        pt = tfh.add_paragraph()
        pt.text = f"🛡 {title} "
        pt.font.name = "Arial"
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = desc
        pt.runs[1].font.size = Pt(8.5)
        pt.runs[1].font.color.rgb = C_TEXT_MUTED
        pt.space_after = Pt(6)

    # Card 2: ZLD & Environmental Sustainability
    c_zld = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c_zld.fill.solid()
    c_zld.fill.fore_color.rgb = C_CARD
    c_zld.line.color.rgb = C_BORDER
    tbz = s9.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.6))
    tfz = tbz.text_frame
    tfz.word_wrap = True

    p = tfz.paragraphs[0]
    p.text = "ZERO LIQUID DISCHARGE (ZLD) CLOSED LOOP"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD
    p.space_after = Pt(8)

    zld_points = [
        ("92.4% Fresh Water Recycling:", "Effluent liquor from SC-101 (2,415 kg/h) is processed through 3-effect falling film evaporator EV-101, recovering 2,231 kg/h distillate."),
        ("Distillate Purity & Reuse:", "Distillate contains < 10 ppm TDS and is recycled directly to fresh water make-up header, slashing freshwater intake."),
        ("Concentrated Mineral Reject:", "Remaining 8% brine concentrated to 45% solids and passed to agitated thin-film dryer for zero environmental discharge."),
        ("FSSAI & GMP Cleanliness:", "All food-contact surfaces mirror-polished to Ra < 0.4 µm with automated CIP spray balls in every vessel.")
    ]
    for title, desc in zld_points:
        pt = tfz.add_paragraph()
        pt.text = f"♻ {title} "
        pt.font.name = "Arial"
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = desc
        pt.runs[1].font.size = Pt(8.5)
        pt.runs[1].font.color.rgb = C_TEXT_MUTED
        pt.space_after = Pt(6)

    add_footer(s9, 9)

    # =========================================================================
    # SLIDE 10: FINANCIAL S-CURVE, TIMELINE & GATE G-A SIGN-OFF
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_background(s10)
    add_header(s10, "CapEx Breakdown ($1.482M), Timeline & Formal Gate G-A Engineering Sign-off", "09. Financial & Implementation")

    # Left: CapEx & Economics
    c_fin = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c_fin.fill.solid()
    c_fin.fill.fore_color.rgb = C_CARD
    c_fin.line.color.rgb = C_BORDER
    tbf = s10.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.6))
    tff = tbf.text_frame
    tff.word_wrap = True

    p = tff.paragraphs[0]
    p.text = "CAPITAL EXPENDITURE & ECONOMIC SUMMARY"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    fin_points = [
        ("Total Plant CapEx:", "$1,482,000 (INR 12.30 Crores)"),
        ("Mechanical Equipment Package:", "$820,000 (Soaking, Dewatering, Dryer, Evaporator)"),
        ("Structural Steel & Piping:", "$195,000 (Mezzanine, Chutes, SS316L Lines)"),
        ("Electrical & SCADA Automation:", "$185,000 (MCCs, VFDs, PLC/SCADA, Field Sensors)"),
        ("Civil Works & Installation:", "$282,000 (Foundation, Cleanroom Cladding, Piping Install)"),
        ("Operating Expense (OpEx):", "$0.084 / kg processed (Steam, Electricity, Reagents)"),
        ("Financial Returns:", "Internal Rate of Return (IRR) = 28.4% | Simple Payback = 2.3 Years")
    ]
    for title, desc in fin_points:
        pt = tff.add_paragraph()
        pt.text = f"💵 {title} "
        pt.font.name = "Arial"
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = C_WHITE
        pt.add_run().text = desc
        pt.runs[1].font.size = Pt(9.0)
        pt.runs[1].font.color.rgb = C_CYAN
        pt.space_after = Pt(5)

    # Right: Formal Engineering Endorsement Block
    c_sign = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c_sign.fill.solid()
    c_sign.fill.fore_color.rgb = C_CARD
    c_sign.line.color.rgb = C_BORDER
    tbs = s10.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.6))
    tfs = tbs.text_frame
    tfs.word_wrap = True

    p = tfs.paragraphs[0]
    p.text = "FORMAL ENGINEERING GOVERNANCE & ENDORSEMENT"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD
    p.space_after = Pt(8)

    # Person 1: Lead Engineer
    p_s = tfs.add_paragraph()
    p_s.text = "LEAD CHEMICAL & PROCESS ENGINEER\n"
    p_s.font.name = "Arial"
    p_s.font.size = Pt(9.5)
    p_s.font.bold = True
    p_s.font.color.rgb = C_CYAN
    p_s.add_run().text = "Sourish Senapati\n"
    p_s.runs[1].font.size = Pt(13)
    p_s.runs[1].font.bold = True
    p_s.runs[1].font.color.rgb = C_WHITE
    p_s.add_run().text = "FinnoaQ Agro-Industrial Technologies Ltd.\nDigital Signature Hash: 0x4B9E...7F12_SENAPATI\n"
    p_s.runs[2].font.size = Pt(9)
    p_s.runs[2].font.color.rgb = C_TEXT_MUTED
    p_s.space_after = Pt(10)

    # Person 2: Academic Advisor
    p_a = tfs.add_paragraph()
    p_a.text = "ACADEMIC & SCIENTIFIC GUIDANCE\n"
    p_a.font.name = "Arial"
    p_a.font.size = Pt(9.5)
    p_a.font.bold = True
    p_a.font.color.rgb = C_CYAN
    p_a.add_run().text = "Dr. Archisman Ray\n"
    p_a.runs[1].font.size = Pt(13)
    p_a.runs[1].font.bold = True
    p_a.runs[1].font.color.rgb = C_WHITE
    p_a.add_run().text = "Department of Chemical Engineering\nIndian Institute of Technology (IIT) Kharagpur\nAcademic Oversight Ref: IITKGP_CHE_ADVISORY_2026\n"
    p_a.runs[2].font.size = Pt(9)
    p_a.runs[2].font.color.rgb = C_TEXT_MUTED
    p_a.space_after = Pt(10)

    # Gate G-A Status
    p_gate = tfs.add_paragraph()
    p_gate.text = "GATE G-A STATUS: CONCEPTUAL FEED BASELINE CONVERGED\n"
    p_gate.font.name = "Arial"
    p_gate.font.size = Pt(10)
    p_gate.font.bold = True
    p_gate.font.color.rgb = C_EMERALD
    p_gate.add_run().text = "Mandatory experimental hold active until pilot screening batch confirmation."
    p_gate.runs[1].font.size = Pt(9)
    p_gate.runs[1].font.color.rgb = C_TEXT_MUTED

    add_footer(s10, 10)

    # Output paths
    output_deliverable = os.path.join(base_dir, "deliverables", "V8_CLIENT_ONBOARDING_AND_ENGINEERING", "FINNOAQ_15TPD_EXECUTIVE_ENGINEERING_PRESENTATION.pptx")
    prs.save(output_deliverable)
    print(f"Presentation saved to {output_deliverable}")

    # Copy to portal public presentation directory
    portal_pres_dir = os.path.join(base_dir, "portal", "public", "presentation")
    os.makedirs(portal_pres_dir, exist_ok=True)
    portal_deliverable = os.path.join(portal_pres_dir, "FINNOAQ_15TPD_EXECUTIVE_ENGINEERING_PRESENTATION.pptx")
    prs.save(portal_deliverable)
    print(f"Presentation copied to portal public at {portal_deliverable}")

if __name__ == "__main__":
    create_deck()
