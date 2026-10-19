# -*- coding: utf-8 -*-
"""
V10 MASTER PROPOSAL GENERATOR
Generates: deliverables/PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.docx
Governed by: V10 Master Directive, AGENTS.md, and Phase1_Scope_of_Work_Toor_Dal.docx
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# Palette Constants
HEX_NAVY = "1A365D"       # Primary Corporate Navy
HEX_STEEL = "2B6CB0"      # Accent Blue
HEX_BODY = "2D3748"       # Dark Slate Charcoal
HEX_BG_ALT = "F7FAFC"     # Table Alternate Fill
HEX_BORDER = "CBD5E0"     # Border Grey
HEX_CALLOUT = "EDF2F7"    # Callout Box Fill
HEX_CALLOUT_BORDER = "3182CE"
HEX_WHITE = "FFFFFF"

COLOR_NAVY = RGBColor(26, 54, 93)
COLOR_STEEL = RGBColor(43, 108, 176)
COLOR_BODY = RGBColor(45, 55, 72)
COLOR_MUTED = RGBColor(113, 128, 150)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="CBD5E0", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_header_row(row, bg_hex=HEX_NAVY):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    for cell in row.cells:
        set_cell_shading(cell, bg_hex)
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.size = Pt(8.0)
                run.font.name = "Calibri"

def make_data_row(row, is_zebra=False, font_size=7.5):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    bg = HEX_BG_ALT if is_zebra else HEX_WHITE
    for cell in row.cells:
        if is_zebra:
            set_cell_shading(cell, bg)
        set_cell_margins(cell, top=65, bottom=65, left=100, right=100)
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.size = Pt(font_size)
                run.font.name = "Calibri"
                run.font.color.rgb = COLOR_BODY

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(13)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.0)
    run.font.bold = True
    run.font.color.rgb = COLOR_STEEL
    return p

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(9.0)
    run.font.bold = True
    run.font.color.rgb = COLOR_BODY
    return p

def add_p(doc, text, bold_prefix=None, space_after=3):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(8.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_NAVY
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_BODY
    return p

def add_callout(doc, text, heading="SCOPE SPECIFICATION & DIAGNOSTIC DIRECTIVE"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(7.0)
    
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, HEX_CALLOUT)
    set_cell_margins(cell, top=90, bottom=90, left=150, right=120)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_CALLOUT_BORDER}"/>'
        f'  <w:top w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:bottom w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    run_h = p.add_run(f"[{heading}]\n")
    run_h.font.bold = True
    run_h.font.size = Pt(8.0)
    run_h.font.color.rgb = COLOR_NAVY
    run_h.font.name = "Calibri"
    
    run_b = p.add_run(text)
    run_b.font.size = Pt(8.0)
    run_b.font.italic = True
    run_b.font.color.rgb = COLOR_BODY
    run_b.font.name = "Calibri"
    
def setup_page_header_footer(doc):
    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)
        
        # Header
        hdr = s.header
        p_hdr = hdr.paragraphs[0]
        p_hdr.text = "FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES  |  TECHNICAL & COMMERCIAL PROPOSAL  |  REV V10"
        p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_hdr.paragraph_format.space_after = Pt(4)
        for r in p_hdr.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(8.0)
            r.font.color.rgb = COLOR_MUTED
            
        # Footer
        ftr = s.footer
        p_ftr = ftr.paragraphs[0]
        p_ftr.text = "CONFIDENTIAL  —  PREPARED FOR HARAKUTIR (KOLKATA)  |  REF: FNQ-PR-2026-001"
        p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p_ftr.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(8.0)
            r.font.color.rgb = COLOR_MUTED

def populate_proposal(doc):
    # Metadata Block
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    run_t1 = p_title.add_run("FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES LTD.\n")
    run_t1.font.name = "Calibri"
    run_t1.font.size = Pt(11.0)
    run_t1.font.bold = True
    run_t1.font.color.rgb = COLOR_STEEL
    
    run_t2 = p_title.add_run("PHASE 1 SCOPE OF WORK & TECHNICAL-COMMERCIAL PROPOSAL\n")
    run_t2.font.name = "Calibri"
    run_t2.font.size = Pt(16.0)
    run_t2.font.bold = True
    run_t2.font.color.rgb = COLOR_NAVY
    
    run_t3 = p_title.add_run("Comparative Diagnostic R&D Study of Tanzanian Imported Split Toor Dal vs. Indian Benchmark Toor Dal")
    run_t3.font.name = "Calibri"
    run_t3.font.size = Pt(11.0)
    run_t3.font.color.rgb = COLOR_BODY
    
    # Metadata Table
    tbl_meta = doc.add_table(rows=7, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_meta.autofit = False
    set_table_borders(tbl_meta)
    tbl_meta.columns[0].width = Inches(2.2)
    tbl_meta.columns[1].width = Inches(4.8)
    
    meta_rows = [
        ("Project Reference & Document Ref:", "FNQ-PR-2026-001 | SOW Rev V10 (Evidence-Gated Baseline)"),
        ("Client Organization:", "Harakutir (53, Pathuriaghata Street, Kolkata – 700006, West Bengal, India)"),
        ("Client Project Contact & Principal:", "Dr. Archisman Ray (CEO & Director, Harakutir; Senior Research Fellow, IIT Kharagpur)"),
        ("Executing R&D Contractor:", "FinnoaQ Agro-Industrial Technologies Ltd."),
        ("Lead Chemical & Process Engineer:", "Sourish Senapati (Lead Process Engineer, FinnoaQ)"),
        ("Academic Guidance & Research Advisory:", "Dr. Archisman Ray (Department of Chemical Engineering, IIT Kharagpur)"),
        ("Issue Date & Commercial Status:", "19 October 2026 | Official Proposal Issued for Client Approval & Project Commissioning")
    ]
    for idx, (label, val) in enumerate(meta_rows):
        row = tbl_meta.rows[idx]
        row.cells[0].paragraphs[0].text = label
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = val
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=8.0)
    
    add_p(doc, "", space_after=4)

    # 1. Executive Decision Summary
    add_h1(doc, "1. Executive Decision Summary")
    add_p(doc, "This technical-commercial proposal is submitted by FinnoaQ Agro-Industrial Technologies Ltd. ('FinnoaQ') to Harakutir ('Client') to initiate a structured, evidence-gated Phase 1 Comparative Diagnostic R&D Study. The investigation addresses the commercial challenge of imported Tanzanian split pigeon pea (Cajanus cajan L. Millsp., 'toor dal'), which reportedly exhibits substantial cooking delay compared to domestic Indian benchmark dal under household preparation conditions.")
    add_p(doc, "The objective of Phase 1 is not to guarantee an immediate cooking-time reduction or to commercialize an unverified chemical treatment. Rather, Phase 1 establishes a rigorous, standardized scientific baseline to replace uncontrolled domestic observations with instrumented physical, chemical, microstructural, thermal, hydration, and cooking measurements. By systematically discriminating across ten competing hypotheses, Phase 1 isolates the primary rate-limiting barriers to softening and provides an objective technical foundation for subsequent Phase 2 formulation and process development.")
    
    # Executive Summary Highlights Table
    tbl_exec = doc.add_table(rows=6, cols=2)
    tbl_exec.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_exec.autofit = False
    set_table_borders(tbl_exec)
    tbl_exec.columns[0].width = Inches(2.2)
    tbl_exec.columns[1].width = Inches(4.8)
    
    exec_data = [
        ("Core Research Problem", "Tanzanian imported toor dal exhibits prolonged cooking latency (~6 household whistles vs ~3 whistles for Indian benchmark)."),
        ("Phase 1 Scientific Objective", "Standardized diagnostic comparison across 9 analytical modules to isolate rate-limiting mechanisms and discriminate 10 hypotheses."),
        ("Proposed Professional Fee", "₹1,73,000 plus applicable GST (fixed-price diagnostic scope; commercial ceiling up to ₹2,00,000 + GST)."),
        ("Indicative Turnaround", "20–25 business days across 5 structured operational stages upon sample receipt and project mobilization."),
        ("Key Deliverables", "14 discrete deliverables including 9 analytical reports, benchmark matrix, root-cause assessment, and Phase 2 roadmap."),
        ("Action Requested from Client", "Approve Phase 1 Scope of Work (Option 1 baseline or Option 2 multi-lot), authorize Milestone 1 advance (₹69,200 + GST), and dispatch sample lots.")
    ]
    for idx, (label, val) in enumerate(exec_data):
        row = tbl_exec.rows[idx]
        row.cells[0].paragraphs[0].text = label
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = val
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=8.0)

    add_callout(doc, 
        "Phase 1 is strictly a diagnostic R&D investigation. It does not promise, warrant, or guarantee a final fast-cooking commercial product, "
        "an optimized chemical treatment, or a construction-ready industrial facility. Phase 1 provides the empirical ground truth required to make "
        "defensible commercial and engineering decisions. All treatment development (Phase 2), pilot production (Phase 3), and commercial plant FEED "
        "(Phase 4) are separately scoped, budgeted, and approved future stages.",
        heading="MANDATORY SCOPE BOUNDARY & SCIENTIFIC PRINCIPLE")

    # 2. Problem Background & Commercial Context
    add_h1(doc, "2. Problem Background & Commercial Context")
    add_p(doc, "Imported pulses represent a critical raw material buffer for the Indian milling, processing, and retail industry. Tanzanian split pigeon pea offers significant logistical and raw material cost advantages. However, commercial millers, distributors, and consumers frequently report substantial cooking resistance in Tanzanian dal compared to traditional Indian benchmarks (such as Maharashtra Latur or Karnataka Gulbarga varieties). In domestic pressure-cooking observations, Tanzanian dal is reported to require approximately six whistles to achieve acceptable palatability, whereas Indian benchmark dal reaches softness in approximately three whistles.")
    add_p(doc, "Crucial Scientific Qualification on Whistle Count: In domestic cookers, a 'whistle' is a periodic pressure-relief event governed by steam generation rate, cooker volume, deadweight mass, stove heat flux, water-to-grain ratio, and venturi geometry. It is an uncalibrated, non-linear proxy that conflates heat transfer with intrinsic grain softening kinetics. While serving as valid commercial context, whistle count cannot serve as an engineering endpoint. Phase 1 replaces qualitative whistling with instrumented time-temperature-pressure logging and objective texture analyzer load-cell shear/compression measurements.")

    # 3. Objectives & Diagnostic Success Definition
    add_h1(doc, "3. Diagnostic Objectives & Success Definition")
    add_p(doc, "The Phase 1 R&D study is designed to achieve the following specific technical milestones:")
    add_p(doc, "• Standardized Comparative Profiling: Quantify physical geometry, proximate composition, starch pasting/gelatinization, hydration kinetics, microstructural integrity, pectin solubility, and mineral interactions for Tanzanian dal versus Indian benchmark.", bold_prefix="1. ")
    add_p(doc, "• Objective Cooking Protocol: Establish a reproducible, instrumented cooking protocol utilizing a calibrated compression/shear endpoint to measure exact softening kinetics and hard-core persistence rates.", bold_prefix="2. ")
    add_p(doc, "• Hypothesis Discrimination: Systematically test ten competing scientific hypotheses to isolate primary rate-limiting mechanisms from secondary statistical associations.", bold_prefix="3. ")
    add_p(doc, "• Commercial Gatekeeping: Deliver an auditable technical foundation and prioritized roadmap for Phase 2 treatment trials, protecting the client against premature capital investment in unproven processing technologies.", bold_prefix="4. ")
    add_p(doc, "Scientific Definition of Success: Under Section 33 of the source SOW, success in Phase 1 is defined by the quality, reproducibility, and defensibility of the diagnostic evidence. Phase 1 is successful when it delivers definitive comparative data, quantified measurement uncertainty, and prioritized root causes—regardless of whether the Tanzanian dal demonstrates fast cooking in its unconditioned state.")

    # 4. Phase Architecture & Scope Boundaries
    add_h1(doc, "4. Phase Architecture & Scope Boundaries")
    add_p(doc, "To protect project governance and ensure commercial clarity, the overall technology roadmap is structured into four distinct, sequentially gated phases. Only Phase 1 is offered for commissioning under this proposal.")
    
    tbl_phases = doc.add_table(rows=5, cols=4)
    tbl_phases.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_phases.autofit = False
    set_table_borders(tbl_phases)
    tbl_phases.columns[0].width = Inches(0.9)
    tbl_phases.columns[1].width = Inches(1.8)
    tbl_phases.columns[2].width = Inches(2.5)
    tbl_phases.columns[3].width = Inches(1.8)
    
    make_header_row(tbl_phases.rows[0])
    tbl_phases.rows[0].cells[0].paragraphs[0].text = "Phase"
    tbl_phases.rows[0].cells[1].paragraphs[0].text = "Designation & Scope"
    tbl_phases.rows[0].cells[2].paragraphs[0].text = "Core Technical Deliverables"
    tbl_phases.rows[0].cells[3].paragraphs[0].text = "Commercial Status"
    
    phase_rows = [
        ("Phase 1", "Comparative Diagnostic R&D Study", "Standardized baseline comparison, 9 analytical modules, objective cooking protocol, 10-hypothesis discrimination, Phase 2 roadmap.", "CURRENT OFFERING (₹1,73,000 + GST; 20–25 Days)"),
        ("Phase 2", "Treatment Development & Mechanistic Validation", "Bench-scale screening of conditioning formulations (bicarbonate, citrate, hydrothermal), dose-response, pH, washing, drying, storage stability.", "Gated Future Scope (Budget defined post-Phase 1)"),
        ("Phase 3", "Pilot Scale-Up & Shelf-Life Verification", "Continuous pilot trials, empirical effluent load, microbial hold-time validation, packaging qualification, commercial shelf-life testing.", "Gated Future Milestone (Contingent on Phase 2)"),
        ("Phase 4", "15,000 kg/day Plant Design & Execution", "Detailed FEED package, frozen PFD/P&IDs, equipment specifications, civil/structural layouts, procurement support, plant commissioning.", "Long-Term Investment (Provisional conceptual annexure)")
    ]
    for idx, (p_id, p_name, p_del, p_stat) in enumerate(phase_rows):
        row = tbl_phases.rows[idx + 1]
        row.cells[0].paragraphs[0].text = p_id
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = p_name
        row.cells[2].paragraphs[0].text = p_del
        row.cells[3].paragraphs[0].text = p_stat
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)

    add_p(doc, "Explicit Exclusions from Phase 1 Scope: Unless approved via written change order, Phase 1 strictly excludes: (1) Formulating, optimizing, or validating commercial chemical treatments; (2) Conducting pilot-scale processing or machinery fabrication; (3) Guaranteeing finished cooking-time reduction; (4) Packaging or multi-month shelf-life stability trials; (5) Issuing construction-ready drawings or detailed FEED for the 15 MT/day facility; (6) Filing regulatory or FSSAI product clearance applications.")

    # 5. Overall Technical Approach & Work Packages
    add_h1(doc, "5. Overall Technical Approach & Work Packages")
    add_p(doc, "The Phase 1 investigation is executed through five inter-dependent Work Packages (WPs) structured to move logically from raw material verification to advanced root-cause synthesis:")
    
    tbl_wp = doc.add_table(rows=6, cols=3)
    tbl_wp.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_wp.autofit = False
    set_table_borders(tbl_wp)
    tbl_wp.columns[0].width = Inches(1.1)
    tbl_wp.columns[1].width = Inches(2.2)
    tbl_wp.columns[2].width = Inches(3.7)
    
    make_header_row(tbl_wp.rows[0])
    tbl_wp.rows[0].cells[0].paragraphs[0].text = "Work Package"
    tbl_wp.rows[0].cells[1].paragraphs[0].text = "Title & Focus"
    tbl_wp.rows[0].cells[2].paragraphs[0].text = "Key Operational Activities & Methods"
    
    wp_data = [
        ("WP-01", "Sample Intake, Physical & Proximate Screening", "Visual inspection, foreign matter, 1000-grain weight, bulk density, seed-coat ratio, AOAC moisture, protein, fat, ash, and fibre."),
        ("WP-02", "Starch & Thermal Gelatinization Profiling", "Total starch, amylose/amylopectin ratio via Megazyme assay, Differential Scanning Calorimetry (DSC) for onset, peak, conclusion temp and enthalpy."),
        ("WP-03", "Hydration Kinetics & Absorption Modeling", "Gravimetric time-course water absorption at 25°C, 40°C, and 60°C (0–360 min), initial absorption rate, saturation capacity, and leaching losses."),
        ("WP-04", "Structural, Microstructural & Pectin Analysis", "Cotyledon cellular density, seed-coat thickness, chemical fractionation of water-, oxalate-, and alkali-soluble pectin, degree of esterification, ICP-OES mineral profiling."),
        ("WP-05", "Standardized Cooking, Texture & Root-Cause Synthesis", "Instrumented pressurized cooking trials, objective texture analyzer compression/shear force, hard-core rate scoring, multivariate correlation, Phase 2 roadmap.")
    ]
    for idx, (w_id, w_name, w_act) in enumerate(wp_data):
        row = tbl_wp.rows[idx + 1]
        row.cells[0].paragraphs[0].text = w_id
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = w_name
        row.cells[2].paragraphs[0].text = w_act
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)

    # 6. Comprehensive 10-Hypothesis Register
    add_h1(doc, "6. Comprehensive 10-Hypothesis Register")
    add_p(doc, "To correct the scientific deficiencies of prior drafts (Review Finding A), pectin–mineral interactions are no longer assumed to be the sole or established mechanism. Phase 1 investigates a comprehensive register of ten competing hypotheses. Each hypothesis defines observable predictions, discriminating tests, and experimental boundaries:")

    tbl_hypo = doc.add_table(rows=11, cols=4)
    tbl_hypo.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_hypo.autofit = False
    set_table_borders(tbl_hypo)
    tbl_hypo.columns[0].width = Inches(0.8)
    tbl_hypo.columns[1].width = Inches(1.8)
    tbl_hypo.columns[2].width = Inches(2.4)
    tbl_hypo.columns[3].width = Inches(2.0)
    
    make_header_row(tbl_hypo.rows[0])
    tbl_hypo.rows[0].cells[0].paragraphs[0].text = "Hypothesis"
    tbl_hypo.rows[0].cells[1].paragraphs[0].text = "Candidate Mechanism"
    tbl_hypo.rows[0].cells[2].paragraphs[0].text = "Observable Predictions & Test"
    tbl_hypo.rows[0].cells[3].paragraphs[0].text = "Discriminating Status & Limits"
    
    hypo_data = [
        ("H1", "Hydration Kinetics / Diffusion Barrier", "Slower water uptake curve, lower initial hydration rate (k), delayed moisture penetration into cotyledon core.", "WP-03 gravimetric time-course; separates diffusion limits from cooking limits."),
        ("H2", "Seed-Coat & Microstructural Resistance", "Residual seed-coat fragments, thicker hylar boundary, or dense outer cotyledon cell packing restricting fluid flow.", "WP-01 seed-coat ratio & WP-04 light microscopy; evaluates physical milling scouring."),
        ("H3", "Cell-Wall Pectin & Mineral Crosslinking", "Higher insoluble pectin fraction, elevated calcium/magnesium crosslinks, lower phytate-to-mineral molar ratio.", "WP-04 pectin fractions & ICP-OES minerals; plausible biochemical hypothesis."),
        ("H4", "Starch Gelatinization & Thermal Impedance", "Elevated DSC gelatinization peak temperature (Tp > 78°C) or higher transition enthalpy requiring prolonged heat input.", "WP-02 DSC thermal assay; identifies intrinsic starch cooking resistance."),
        ("H5", "Cultivar Genetics & Agronomic Origin", "Distinct genetic variety, protein matrix density, or soil mineral accumulation unique to East African agro-climates.", "Requires sample lot metadata; Phase 1 identifies phenotypic expression only."),
        ("H6", "Commercial Dehulling & Processing History", "Thermal case-hardening from dry milling, excessive frictional heat during emery scouring, or residual polishing oil.", "Surface lipid assay & microstructural examination; identifies commercial processing damage."),
        ("H7", "Storage Age & Hard-to-Cook (HTC) Defect", "Prolonged transit/storage under high temperature (>30°C) and RH (>70%) inducing phytase loss and pectin crosslinking.", "Standard legume aging marker; correlated with storage records and ion leakage."),
        ("H8", "Grain Physical Geometry & Split Uniformity", "Larger cotyledon thickness, lower surface-area-to-volume ratio, or higher broken grain fraction skewing water distribution.", "WP-01 caliper dimensions and 1000-grain mass; isolates geometric confounders."),
        ("H9", "Cooking Apparatus & Measurement Confounders", "Apparatus heat transfer, pressure vessel venting variability, or whistle-counting bias in domestic observation.", "WP-05 standardized cooking protocol eliminates domestic apparatus artefacts."),
        ("H10", "Multi-Factorial Synergistic Interaction", "Simultaneous interaction of slow hydration (H1) and cell-wall pectin resistance (H3) amplifying total cooking latency.", "Multivariate correlation & regression modeling in WP-05 final synthesis.")
    ]
    for idx, (h_id, h_name, h_pred, h_stat) in enumerate(hypo_data):
        row = tbl_hypo.rows[idx + 1]
        row.cells[0].paragraphs[0].text = h_id
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = h_name
        row.cells[2].paragraphs[0].text = h_pred
        row.cells[3].paragraphs[0].text = h_stat
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.2)

    add_p(doc, "Evidence Language Ladder: To maintain scientific integrity, Phase 1 conclusions strictly observe the following four-tier hierarchy: (1) Measured Difference: Directly observed analytical variance between samples; (2) Statistical Association: Correlation supported by data but not establishing directionality; (3) Plausible Hypothesis: Literature-compatible mechanism not yet causally proven for the target lot; (4) Controlled Causal Effect: Established only when controlled intervention trials isolate the mechanism in Phase 2.")

    # 7. Sample Requirements, Allocation Budget & Multi-Lot Options
    add_h1(doc, "7. Sample Requirements, Allocation Budget & Multi-Lot Options")
    add_p(doc, "Under Section 3 of the source SOW, the recommended sample mass is approximately 2.5–3.0 kg per lot. To address Review Finding D, a rigorous physical sample allocation budget was performed across all analytical modules:")

    tbl_mass = doc.add_table(rows=13, cols=4)
    tbl_mass.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mass.autofit = False
    set_table_borders(tbl_mass)
    tbl_mass.columns[0].width = Inches(1.2)
    tbl_mass.columns[1].width = Inches(3.0)
    tbl_mass.columns[2].width = Inches(1.4)
    tbl_mass.columns[3].width = Inches(1.4)
    
    make_header_row(tbl_mass.rows[0])
    tbl_mass.rows[0].cells[0].paragraphs[0].text = "Module / Allocation"
    tbl_mass.rows[0].cells[1].paragraphs[0].text = "Analytical Activity & Replicate Structure"
    tbl_mass.rows[0].cells[2].paragraphs[0].text = "Mass Budget (g)"
    tbl_mass.rows[0].cells[3].paragraphs[0].text = "Allocation Basis"
    
    mass_data = [
        ("MOD-01", "Physical & Preliminary Grain Integrity Characterization", "150 g", "3 batches x 3 repeats + reserve"),
        ("MOD-02", "Proximate Chemical Composition (Moisture, Protein, Fat, Ash, Fibre)", "250 g", "Triplicate AOAC external lab minimum"),
        ("MOD-03", "Starch & Amylose / Amylopectin Spectrophotometric Assay", "150 g", "Triplicate Megazyme assay + reserve"),
        ("MOD-04", "DSC Thermal Gelatinization & Transition Enthalpy", "150 g", "Triplicate micro-sample DSC runs"),
        ("MOD-05", "Hydration Kinetics & Time-Course Water Absorption (25°C, 40°C, 60°C)", "300 g", "Full kinetic curves across 3 temperatures"),
        ("MOD-06", "Pectin & Cell-Wall Chemical Fractionation", "150 g", "Triplicate chemical sequential extraction"),
        ("MOD-07", "Mineral & Phytate Profile (ICP-OES / AAS)", "150 g", "External accredited laboratory minimum"),
        ("MOD-08", "Grain Hardness & Structural Texture Analysis (Load Cell)", "150 g", "Raw & soaked texture profile runs"),
        ("MOD-09", "Standardized Pressurized Cooking Performance Study", "400 g", "Multiple pressurized cooking runs"),
        ("SEC-RET", "Sealed Archival Reference Retention Sample (Dispute & Verification)", "500 g", "Mandatory ISO 17025 climate archive"),
        ("SEC-CON", "Grinding Loss, Handling Contingency & Repeat Margin (~15%)", "300 g", "Milling hold-up and operational buffer"),
        ("TOTAL LOT BUDGET", "Total Requisite Sample Mass per Grain Lot", "2,550 g (2.55 kg)", "Strictly fits within 2.5–3.0 kg allocation")
    ]
    for idx, (m_id, m_act, m_wt, m_bas) in enumerate(mass_data):
        row = tbl_mass.rows[idx + 1]
        is_total = (idx == len(mass_data) - 1)
        row.cells[0].paragraphs[0].text = m_id
        if is_total:
            row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = m_act
        row.cells[2].paragraphs[0].text = m_wt
        row.cells[3].paragraphs[0].text = m_bas
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)
        if is_total:
            for cell in row.cells:
                set_cell_shading(cell, HEX_CALLOUT)
                for run in cell.paragraphs[0].runs:
                    run.font.bold = True

    add_p(doc, "Multi-Lot Commercial Options: The source SOW states that two independent lots of each sample should be evaluated where possible. However, arithmetic demonstrates that 2.5 kg of material covers exactly ONE lot evaluated across three preparation batches and technical triplicates. Subsampling a single commercial bag does NOT produce independent lots. To provide total commercial transparency, FinnoaQ offers two structured options for client approval:")
    add_p(doc, "• Option 1 (Baseline Scoped SOW — ₹1,73,000 + GST): Two traceable commercial samples (1 Tanzanian Lot + 1 Indian Benchmark Lot), 2.5–3.0 kg each. Provides rigorous, lot-specific diagnostic comparison within the original budget and 20–25 business day timeline.", bold_prefix="Option 1: ")
    add_p(doc, "• Option 2 (Multi-Lot Expanded Variation — ₹2,85,000 + GST): Four independently traceable commercial lots (2 Tanzanian import consignments + 2 Indian regional benchmarks), 2.5–3.0 kg each. Requires doubling analytical laboratory runs, expanding inter-lot statistical variance modeling, and an extended 30–35 business day timeline.", bold_prefix="Option 2: ")

    # 8. Technical Investigation Matrix
    add_h1(doc, "8. Technical Investigation Matrix")
    add_p(doc, "The multi-module experimental investigation matrix integrates all physical, chemical, structural, and cooking evaluations across the two comparative samples:")

    tbl_mat = doc.add_table(rows=10, cols=5)
    tbl_mat.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mat.autofit = False
    set_table_borders(tbl_mat)
    tbl_mat.columns[0].width = Inches(0.8)
    tbl_mat.columns[1].width = Inches(1.5)
    tbl_mat.columns[2].width = Inches(1.8)
    tbl_mat.columns[3].width = Inches(1.4)
    tbl_mat.columns[4].width = Inches(1.5)
    
    make_header_row(tbl_mat.rows[0])
    tbl_mat.rows[0].cells[0].paragraphs[0].text = "Module"
    tbl_mat.rows[0].cells[1].paragraphs[0].text = "Analytical Domain"
    tbl_mat.rows[0].cells[2].paragraphs[0].text = "Key Parameters Measured"
    tbl_mat.rows[0].cells[3].paragraphs[0].text = "Standard Method / Instrument"
    tbl_mat.rows[0].cells[4].paragraphs[0].text = "Decision Relevance"
    
    mat_data = [
        ("MOD-01", "Physical & Integrity", "Dimensions, 1000-grain weight, bulk density, broken grains, seed-coat %.", "IS 4333 / Caliper & Density Flask", "Identifies geometric barriers & milling quality."),
        ("MOD-02", "Proximate Composition", "Moisture (WB), crude protein, crude fat, crude fibre, total ash, carbohydrates.", "AOAC 925.10 / 920.87 / 922.06 / 923.03", "Establishes baseline chemical composition & dry matter."),
        ("MOD-03", "Starch Properties", "Total starch content, amylose percentage, amylopectin ratio.", "Megazyme K-AMYL / Spectrophotometry", "Assesses starch retrogradation & swelling potential."),
        ("MOD-04", "DSC Thermal Behavior", "Gelatinization onset (To), peak (Tp), conclusion (Tc), enthalpy (ΔHgel).", "AACC 56-11.02 / Differential Scanning Calorimeter", "Identifies if starch requires higher cooking temperature."),
        ("MOD-05", "Hydration Kinetics", "Water absorption rate (k), equilibrium capacity, leached solids at 25/40/60°C.", "AACC 56-20 / Gravimetric Kinetic Cell", "Isolates water penetration rate from cooking reactions."),
        ("MOD-06", "Pectin & Cell-Wall", "Water-, oxalate-, alkali-soluble pectin, degree of esterification (DE).", "Carbohydrate Polymers / Chemical Fractionation", "Tests middle lamella pectin solubility & crosslinking."),
        ("MOD-07", "Minerals & Phytate", "Calcium, magnesium, iron, phosphorus, potassium, phytic acid, Ca:phytate ratio.", "AOAC 999.11 / ICP-OES & Wade Reagent", "Quantifies divalent cation availability for pectate bridges."),
        ("MOD-08", "Hardness & Texture", "Raw grain puncture resistance, soaked firmness, peak compression force.", "TA.XT Plus Texture Analyzer / 50kg Load Cell", "Establishes objective mechanical firmness baseline."),
        ("MOD-09", "Standardized Cooking", "Cooking curve (0–60 min), objective time-to-softness, hard-core rate, solids loss.", "Pressurized Vessel / Instrumented Load Cell", "Replaces domestic whistle counting with objective kinetics.")
    ]
    for idx, (m_id, m_dom, m_par, m_met, m_dec) in enumerate(mat_data):
        row = tbl_mat.rows[idx + 1]
        row.cells[0].paragraphs[0].text = m_id
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = m_dom
        row.cells[2].paragraphs[0].text = m_par
        row.cells[3].paragraphs[0].text = m_met
        row.cells[4].paragraphs[0].text = m_dec
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.2)

    # 9. Experimental Design, Replication Hierarchy & Statistical Plan
    add_h1(doc, "9. Experimental Design, Replication Hierarchy & Statistical Plan")
    add_p(doc, "Under Review Finding D, prior conflation of experimental units is corrected. Experimental units adhere strictly to the following four-tier statistical governance hierarchy:")
    add_p(doc, "• Independent Commercial Grain Lot: A distinct physical consignment with separate origin, harvest, processing, or custody documentation.", bold_prefix="Tier 1: ")
    add_p(doc, "• Independent Preparation Batch: Material weighed, hydrated, or processed in separate vessels on separate occasions (n = 3 independent batches).", bold_prefix="Tier 2: ")
    add_p(doc, "• Technical Replicate: Repeated instrumental measurement of the same prepared batch to quantify instrument repeatability (n = 3 technical repeats).", bold_prefix="Tier 3: ")
    add_p(doc, "• Subsample: Analytical split of a single batch; subsamples are never treated as independent biological replicates.", bold_prefix="Tier 4: ")
    add_p(doc, "Standardized Cooking Protocol & Objective Endpoint: Pressurized cooking trials are conducted in a standardized, instrumented cooking chamber using a fixed 1:4 dal-to-water ratio (distilled water, TDS < 10 ppm) at a regulated internal pressure of 1.05 bar gauge (121°C). Samples are withdrawn at controlled intervals (10, 15, 20, 25, 30, 40 min). The primary endpoint is defined as the cooking duration required for 90% of grains to exhibit peak compression force <= 8.0 N on a calibrated texture analyzer. Residual ungelatinized hard-core percentage is quantified via optical glass plate compression.")
    add_p(doc, "Statistical Testing Discipline: All data are reported as Mean ± Standard Deviation with 95% Confidence Intervals. Differences between Tanzanian dal and Indian benchmark are evaluated using two-sample Welch's t-test (accounting for unequal variances) and one-way ANOVA with Tukey's HSD post-hoc test. No exaggerated statistical certainty or universal population claims are made from single-lot triplicates; Phase 1 observations establish baseline variance to power subsequent Phase 2 confirmatory trials.")

    # 10. Future Treatment-Candidate Pathway (Phase 2 Gated Scope)
    add_h1(doc, "10. Future Treatment-Candidate Pathway (Phase 2 Gated Scope)")
    add_p(doc, "To resolve Review Finding C, all chemical conditioning agents and physical treatments are rigorously segregated. Reagents are identified by precise chemical formula, CAS registry, food additive INS number, and concentration basis:")

    tbl_treat = doc.add_table(rows=8, cols=5)
    tbl_treat.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_treat.autofit = False
    set_table_borders(tbl_treat)
    tbl_treat.columns[0].width = Inches(0.9)
    tbl_treat.columns[1].width = Inches(1.8)
    tbl_treat.columns[2].width = Inches(1.5)
    tbl_treat.columns[3].width = Inches(1.4)
    tbl_treat.columns[4].width = Inches(1.4)
    
    make_header_row(tbl_treat.rows[0])
    tbl_treat.rows[0].cells[0].paragraphs[0].text = "Treatment ID"
    tbl_treat.rows[0].cells[1].paragraphs[0].text = "Reagent & Formula"
    tbl_treat.rows[0].cells[2].paragraphs[0].text = "Concentration & Dose"
    tbl_treat.rows[0].cells[3].paragraphs[0].text = "Process Parameters"
    tbl_treat.rows[0].cells[4].paragraphs[0].text = "Regulatory & Phase Status"
    
    treat_data = [
        ("TRT-00", "Untreated Control\n(Raw As-Received)", "0.00% chemical\n0.00% grain dose", "Ambient (25°C), 0 min;\nas-received 10.5% WB.", "FSSAI 2.4.6.15 compliant;\nPHASE 1 DIAGNOSTIC BASELINE"),
        ("TRT-01", "Water-Only Soak Control\n(Pure H₂O, CAS 7732-18-5)", "0.00% chemical\nLiquor ratio 3:1", "25°C, 60 min, RO rinse 1:1;\ntray dry 55°C to 10% WB.", "Pure potable water;\nPHASE 2 SCREENING CONTROL"),
        ("TRT-02", "Sodium Bicarbonate\n(NaHCO₃, CAS 144-55-8)", "0.25%–0.50% w/w bath\n(0.75%–1.50% as-fed grain)", "25°C, 60 min, pH 8.2–8.4;\nrinse 2:1, dry to 10% WB.", "INS 500(ii) food additive;\nPHASE 2 CANDIDATE — NOT TESTED"),
        ("TRT-03", "Trisodium Citrate\n(Na₃C₆H₅O₇·2H₂O, CAS 6132-04-3)", "0.50% w/w bath\n(1.50% w/w as-fed grain)", "25°C, 60 min, pH 7.9–8.2;\nrinse 2:1, dry to 10% WB.", "INS 331(iii) sequestering agent;\nPHASE 2 CANDIDATE — NOT TESTED"),
        ("TRT-04", "Citrate Buffer System\n(Citrate + Citric Acid)", "0.40% citrate + 0.05% acid\n(1.20% + 0.15% as-fed grain)", "25°C, 60 min, buffer pH 6.0;\nrinse 2:1, dry to 10% WB.", "INS 331(iii) + INS 330;\nPHASE 2 CANDIDATE — NOT TESTED"),
        ("TRT-05", "Sodium Carbonate (Segregated)\n(Na₂CO₃, CAS 497-19-8)", "0.20% w/w bath\n(0.60% w/w as-fed grain)", "25°C, 45 min, pH 10.6–10.9;\nrinse 2.5:1, dry to 10% WB.", "INS 500(i) alkaline salt;\nPHASE 2 CANDIDATE — NOT TESTED"),
        ("TRT-06", "Hydrothermal Pre-Steeping\n(Pure Water, Zero Chemical)", "0.00% chemical\nPhysical thermal process", "65°C, 20 min steeping;\nfluidized bed dry to 10% WB.", "100% clean-label physical process;\nPHASE 2 CANDIDATE — NOT TESTED")
    ]
    for idx, (t_id, t_rea, t_dos, t_par, t_reg) in enumerate(treat_data):
        row = tbl_treat.rows[idx + 1]
        row.cells[0].paragraphs[0].text = t_id
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = t_rea
        row.cells[2].paragraphs[0].text = t_dos
        row.cells[3].paragraphs[0].text = t_par
        row.cells[4].paragraphs[0].text = t_reg
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.2)

    add_p(doc, "Concentration Basis Distinction: Bath concentration (w/w of solution) is mathematically distinct from applied grain dose (w/w on as-fed grain basis). At a 3:1 liquor-to-grain ratio, a 0.50% w/w bath provides 1.50% w/w chemical relative to dal. In Phase 2, both bases will be tracked alongside post-treatment drying and mandatory 7-day storage conditioning to verify that softening effects survive packaging and storage.")

    # 11. Food Safety, Regulatory Separation & Product Acceptance Criteria
    add_h1(doc, "11. Food Safety, Regulatory Separation & Product Acceptance Criteria")
    add_p(doc, "Under Review Finding E, project quality acceptance criteria are formally distinguished from statutory food safety regulations. The commercial product falls under FSSAI Category 2.4.6.15 (Dehulled Split Pulses):")

    tbl_safe = doc.add_table(rows=6, cols=4)
    tbl_safe.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_safe.autofit = False
    set_table_borders(tbl_safe)
    tbl_safe.columns[0].width = Inches(1.5)
    tbl_safe.columns[1].width = Inches(1.8)
    tbl_safe.columns[2].width = Inches(1.8)
    tbl_safe.columns[3].width = Inches(1.9)
    
    make_header_row(tbl_safe.rows[0])
    tbl_safe.rows[0].cells[0].paragraphs[0].text = "Quality / Safety Parameter"
    tbl_safe.rows[0].cells[1].paragraphs[0].text = "Classification & Authority"
    tbl_safe.rows[0].cells[2].paragraphs[0].text = "Numerical Standard / Limit"
    tbl_safe.rows[0].cells[3].paragraphs[0].text = "Measurement Method & Stage"
    
    safe_data = [
        ("Moisture Content", "FSSAI Statutory Standard (Clause 2.4.6.15)", "Maximum 14.0% w/w (Wet Basis)", "AOAC 925.10 / Mandatory release check"),
        ("Broken Grains / Fines", "FSSAI Statutory Standard (Clause 2.4.6.15)", "Maximum 5.0% w/w broken dal", "IS 4333 Part 1 / Sieve analysis"),
        ("Project Broken Target", "Project Acceptance Target (Internal Quality)", "Maximum 2.0% w/w broken dal", "Stricter internal commercial specification"),
        ("Finished Sodium Content", "Project Acceptance Target (Commercial Quality)", "Maximum 150 mg / 100 g dry dal", "ICP-OES / Evaluated post-drying in Phase 2"),
        ("Water Activity (aw)", "Project Acceptance Target (Microbial Stability)", "aw < 0.60 at 10.0% ± 0.5% moisture", "Chilled mirror dew-point hygrometer")
    ]
    for idx, (s_par, s_cla, s_num, s_met) in enumerate(safe_data):
        row = tbl_safe.rows[idx + 1]
        row.cells[0].paragraphs[0].text = s_par
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = s_cla
        row.cells[2].paragraphs[0].text = s_num
        row.cells[3].paragraphs[0].text = s_met
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)

    add_p(doc, "Laboratory Safety Rule: No human sensory evaluation or tasting of uncharacterized experimental samples will occur during Phase 1. Formal organoleptic panels are restricted to Phase 2 under certified food-grade hygiene protocols.")

    # 12. Key Deliverables & Final Technical Report Structure
    add_h1(doc, "12. Key Deliverables & Final Technical Report Structure")
    add_p(doc, "FinnoaQ will provide the complete suite of 14 key deliverables defined in Section 21 of the source SOW:")

    tbl_deliv = doc.add_table(rows=8, cols=2)
    tbl_deliv.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_deliv.autofit = False
    set_table_borders(tbl_deliv)
    tbl_deliv.columns[0].width = Inches(3.5)
    tbl_deliv.columns[1].width = Inches(3.5)
    
    make_header_row(tbl_deliv.rows[0])
    tbl_deliv.rows[0].cells[0].paragraphs[0].text = "Deliverables 1 to 7 (Analytical Modules)"
    tbl_deliv.rows[0].cells[1].paragraphs[0].text = "Deliverables 8 to 14 (Synthesis & Reports)"
    
    deliv_pairs = [
        ("DEL-01: Sample Characterization Report", "DEL-08: Hardness & Texture Analysis Report"),
        ("DEL-02: Proximate Chemical Composition Report", "DEL-09: Standardized Cooking Performance Report"),
        ("DEL-03: Starch & Gelatinization Report", "DEL-10: Tanzanian vs. Indian Benchmarking Matrix"),
        ("DEL-04: Hydration & Water Absorption Report", "DEL-11: Integrated Root-Cause Analysis Dossier"),
        ("DEL-05: Structural & Seed-Coat Assessment", "DEL-12: Phase 2 Technology Recommendations"),
        ("DEL-06: Pectin & Cell-Wall Fractionation Report", "DEL-13: Executive Management Summary Briefing"),
        ("DEL-07: Mineral & Phytate Assessment Report", "DEL-14: Comprehensive Final Technical R&D Report")
    ]
    for idx, (d_left, d_right) in enumerate(deliv_pairs):
        row = tbl_deliv.rows[idx + 1]
        row.cells[0].paragraphs[0].text = d_left
        row.cells[1].paragraphs[0].text = d_right
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.8)

    add_p(doc, "Final Report Structure: The final deliverable comprises a 23-section technical dossier covering executive summary, background, experimental design, analytical methodologies, detailed results for all modules, benchmark matrices, statistical analyses, root-cause assessment, Phase 2 roadmap, study limitations, and raw data appendices.")

    # 13. Project Timeline & Operational Milestones
    add_h1(doc, "13. Project Timeline & Operational Milestones")
    add_p(doc, "The indicative turnaround is 20–25 business days across five operational stages (source SOW Section 27):")

    tbl_time = doc.add_table(rows=6, cols=4)
    tbl_time.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_time.autofit = False
    set_table_borders(tbl_time)
    tbl_time.columns[0].width = Inches(0.9)
    tbl_time.columns[1].width = Inches(1.3)
    tbl_time.columns[2].width = Inches(2.8)
    tbl_time.columns[3].width = Inches(2.0)
    
    make_header_row(tbl_time.rows[0])
    tbl_time.rows[0].cells[0].paragraphs[0].text = "Stage"
    tbl_time.rows[0].cells[1].paragraphs[0].text = "Timeline"
    tbl_time.rows[0].cells[2].paragraphs[0].text = "Key Operational Activities"
    tbl_time.rows[0].cells[3].paragraphs[0].text = "Dependencies & Deliverables"
    
    time_data = [
        ("Stage 1", "Days 1–3", "Sample intake, physical inspection, chain of custody coding, allocation to internal/external labs.", "Sample receipt + Milestone 1 advance"),
        ("Stage 2", "Days 4–14", "Proximate chemical analysis, starch/amylose assays, DSC thermal runs, mineral/phytate testing.", "Completion of Stage 1 preparation"),
        ("Stage 3", "Days 10–18", "Time-course hydration kinetics, standardized pressurized cooking runs, texture analyzer shear testing.", "Conducted in parallel with Stage 2"),
        ("Stage 4", "Days 18–22", "Data consolidation, statistical evaluation, cross-verification, multivariate correlation, root-cause synthesis.", "Receipt of all analytical data sheets"),
        ("Stage 5", "Days 22–25", "Final technical report compilation, executive briefing preparation, submission, and client presentation.", "Final report sign-off + Milestone 3")
    ]
    for idx, (t_stg, t_day, t_act, t_dep) in enumerate(time_data):
        row = tbl_time.rows[idx + 1]
        row.cells[0].paragraphs[0].text = t_stg
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = t_day
        row.cells[2].paragraphs[0].text = t_act
        row.cells[3].paragraphs[0].text = t_dep
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)

    # 14. Indicative Technical Cost Structure & Commercial Terms
    add_h1(doc, "14. Indicative Technical Cost Structure & Commercial Terms")
    add_p(doc, "The indicative professional fee totals exactly ₹1,73,000 plus applicable GST, matching Table 40 of the source SOW:")

    tbl_cost = doc.add_table(rows=13, cols=3)
    tbl_cost.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_cost.autofit = False
    set_table_borders(tbl_cost)
    tbl_cost.columns[0].width = Inches(0.8)
    tbl_cost.columns[1].width = Inches(4.7)
    tbl_cost.columns[2].width = Inches(1.5)
    
    make_header_row(tbl_cost.rows[0])
    tbl_cost.rows[0].cells[0].paragraphs[0].text = "Item"
    tbl_cost.rows[0].cells[1].paragraphs[0].text = "Analytical Module / Professional Service Component"
    tbl_cost.rows[0].cells[2].paragraphs[0].text = "Indicative Fee (INR)"
    
    cost_data = [
        ("01", "Sample Preparation & Physical Characterization (Dimensions, 1000-grain weight, density)", "₹20,000"),
        ("02", "Proximate Chemical Analysis (Moisture, protein, fat, fibre, ash, carbohydrates)", "₹7,000"),
        ("03", "Starch & Amylose Analysis (Total starch, amylose/amylopectin ratio)", "₹5,000"),
        ("04", "DSC Thermal / Gelatinization Characterization (To, Tp, Tc, ΔHgel)", "₹20,000"),
        ("05", "Hydration & Water Absorption Study (Kinetics at 25°C, 40°C, 60°C across 0–360 min)", "₹10,000"),
        ("06", "Pectin & Cell-Wall Characterization (Water-, oxalate-, alkali-soluble fractions, DE)", "₹18,000"),
        ("07", "Mineral & Phytate Profile (Ca, Mg, Fe, P, K by ICP-OES/AAS, phytic acid content)", "₹16,000"),
        ("08", "Hardness & Texture Analysis (Raw & soaked load-cell puncture, shear force)", "₹17,000"),
        ("09", "Standardized Cooking Performance Study (Pressurized kinetics, hard-core rate)", "₹20,000"),
        ("10", "Integrated Data Analysis & Root-Cause Assessment (Multivariate hypothesis testing)", "₹20,000"),
        ("11", "Final Technical R&D Report & Executive Management Summary Compilation", "₹20,000"),
        ("TOTAL", "TOTAL PHASE 1 INDICATIVE PROFESSIONAL FEE (EXCLUDING GST)", "₹1,73,000")
    ]
    for idx, (c_id, c_desc, c_amt) in enumerate(cost_data):
        row = tbl_cost.rows[idx + 1]
        is_total = (idx == len(cost_data) - 1)
        row.cells[0].paragraphs[0].text = c_id
        if is_total:
            row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = c_desc
        row.cells[2].paragraphs[0].text = c_amt
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.8)
        if is_total:
            for cell in row.cells:
                set_cell_shading(cell, HEX_CALLOUT)
                for run in cell.paragraphs[0].runs:
                    run.font.bold = True

    add_p(doc, "Commercial Notes: (1) Total professional fee is ₹1,73,000 plus applicable GST; (2) Commercial ceiling is up to ₹2,00,000 + GST; no additional charges will be incurred without prior written client approval; (3) Third-party specialized laboratory assays are coordinated within this budget framework; (4) GST is payable extra on actuals under SAC 998313.")

    # Payment Schedule Table
    add_h2(doc, "Milestone Payment Schedule (Source SOW Table 45)")
    tbl_pay = doc.add_table(rows=5, cols=4)
    tbl_pay.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_pay.autofit = False
    set_table_borders(tbl_pay)
    tbl_pay.columns[0].width = Inches(1.1)
    tbl_pay.columns[1].width = Inches(3.4)
    tbl_pay.columns[2].width = Inches(1.1)
    tbl_pay.columns[3].width = Inches(1.4)
    
    make_header_row(tbl_pay.rows[0])
    tbl_pay.rows[0].cells[0].paragraphs[0].text = "Milestone"
    tbl_pay.rows[0].cells[1].paragraphs[0].text = "Objective Deliverable Trigger"
    tbl_pay.rows[0].cells[2].paragraphs[0].text = "Percentage"
    tbl_pay.rows[0].cells[3].paragraphs[0].text = "Amount (INR)"
    
    pay_data = [
        ("Milestone 1", "Project Initiation: Formal confirmation & sample receipt protocol", "40.0%", "₹69,200 + GST"),
        ("Milestone 2", "Mid-Term Analytical Completion: Delivery of laboratory data sheets", "40.0%", "₹69,200 + GST"),
        ("Milestone 3", "Final Report Acceptance: Delivery of Final Technical Report & Briefing", "20.0%", "₹34,600 + GST"),
        ("TOTAL", "Consolidated Project Milestone Value", "100.0%", "₹1,73,000 + GST")
    ]
    for idx, (p_id, p_trig, p_pct, p_amt) in enumerate(pay_data):
        row = tbl_pay.rows[idx + 1]
        is_total = (idx == len(pay_data) - 1)
        row.cells[0].paragraphs[0].text = p_id
        if is_total:
            row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = p_trig
        row.cells[2].paragraphs[0].text = p_pct
        row.cells[3].paragraphs[0].text = p_amt
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.8)
        if is_total:
            for cell in row.cells:
                set_cell_shading(cell, HEX_CALLOUT)
                for run in cell.paragraphs[0].runs:
                    run.font.bold = True

    # 15. Assumptions, Exclusions & Risk Management
    add_h1(doc, "15. Assumptions, Exclusions & Risk Management")
    add_p(doc, "Key operational assumptions and risk mitigations governing execution:")
    add_p(doc, "• Sample Custody & Authenticity: Client is responsible for supplying genuine, traceable Tanzanian dal and Indian benchmark dal with completed Sample Metadata Forms. Delays in sample arrival will shift project milestones accordingly.", bold_prefix="Assumption 1: ")
    add_p(doc, "• External Laboratory Throughput: Specialized testing at candidate partner institutions is subject to instrument queue times. Any laboratory delays will be communicated immediately without cost escalation.", bold_prefix="Assumption 2: ")
    add_p(doc, "• Diagnostic Risk Control: If preliminary assays reveal anomalous composition (e.g. extreme moisture deviation or heavy mold infestation), testing will pause immediately for client review before exhausting budget.", bold_prefix="Risk Mitigation: ")

    # 16. Confidentiality, Data Ownership & Sample Retention
    add_h1(doc, "16. Confidentiality, Data Ownership & Sample Retention")
    add_p(doc, "• Client Data Ownership: Under Section 31 of the source SOW, all experimental data, laboratory test certificates, statistical models, and final reports generated under Phase 1 remain the exclusive intellectual and commercial property of Harakutir.")
    add_p(doc, "• Non-Disclosure Obligations: FinnoaQ treats all sample identities, commercial origins, pricing data, and technical findings as strict commercial-in-confidence material. No publication, presentation, or external dissemination will occur without prior written authorization from Harakutir.")
    add_p(doc, "• Sample Retention: Unused grain material and a 500 g sealed reference retention sample per lot will be retained under controlled climate storage (18–22°C, dry conditions) for six months following report submission for verification or dispute resolution.")

    # 17. Downstream Technology Roadmap (Phases 2, 3, and 4)
    add_h1(doc, "17. Downstream Technology Roadmap (Phases 2, 3, and 4)")
    add_p(doc, "Progressing from Phase 1 to subsequent phases is governed by strict stage-gate review criteria:")
    add_p(doc, "• Phase 2 Gate: Initiated if Phase 1 successfully isolates rate-limiting softening barriers and establishes that chemical or hydrothermal conditioning produces a statistically meaningful reduction in objective cooking hardness.", bold_prefix="Gate 1 (To Phase 2): ")
    add_p(doc, "• Phase 3 Gate: Initiated if Phase 2 establishes a stable treatment formulation that retains its cooking acceleration after post-drying, satisfies FSSAI product standards, and exhibits acceptable organoleptic properties.", bold_prefix="Gate 2 (To Phase 3): ")
    add_p(doc, "• Phase 4 Gate: Initiated only when pilot trials demonstrate robust yield, commercial shelf stability, verified effluent treatment economics, and reconciled continuous mass and energy balances.", bold_prefix="Gate 3 (To Phase 4): ")

    # 18. Project Acceptance & Client Onboarding Signature Block
    add_h1(doc, "18. Project Acceptance & Client Onboarding Signature Block")
    add_p(doc, "To initiate the Phase 1 Comparative Diagnostic R&D Study, please endorse the authorization block below and return a signed copy to FinnoaQ Agro-Industrial Technologies Ltd.")

    tbl_sign = doc.add_table(rows=6, cols=2)
    tbl_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_sign.autofit = False
    set_table_borders(tbl_sign)
    tbl_sign.columns[0].width = Inches(3.5)
    tbl_sign.columns[1].width = Inches(3.5)
    
    make_header_row(tbl_sign.rows[0])
    tbl_sign.rows[0].cells[0].paragraphs[0].text = "CLIENT ACCEPTANCE & AUTHORIZATION"
    tbl_sign.rows[0].cells[1].paragraphs[0].text = "EXECUTING R&D CONTRACTOR CONFIRMATION"
    
    sign_rows = [
        ("Client Organization: Harakutir", "Contractor: FinnoaQ Agro-Industrial Technologies Ltd."),
        ("Authorized Signatory: Dr. Archisman Ray", "Authorized Lead Engineer: Sourish Senapati"),
        ("Designation: CEO & Director, Harakutir", "Designation: Lead Chemical & Process Engineer"),
        ("Scope Selection: [  ] Option 1 (₹1.73L)  [  ] Option 2 (₹2.85L)", "Technical Guidance: Dr. Archisman Ray (IIT Kharagpur)"),
        ("Signature & Date: ____________________", "Signature & Date: ____________________")
    ]
    for idx, (s_left, s_right) in enumerate(sign_rows):
        row = tbl_sign.rows[idx + 1]
        row.cells[0].paragraphs[0].text = s_left
        row.cells[1].paragraphs[0].text = s_right
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=8.0)

    # ANNEXURES
    doc.add_page_break()
    
    # Annexure A
    add_h1(doc, "Annexure A: Laboratory Selection Criteria & Candidate Partner Institutions")
    add_p(doc, "Under Section 23 of the source SOW, specialized analytical modules requiring accredited analytical equipment will be coordinated with candidate institutions based on technical capability, method validity, turnaround time, and competitive quotation. These institutions are candidates for quotation and evaluation—not pre-committed subcontractors:")
    add_p(doc, "• Eureka Analytical Services Pvt. Ltd. (Kolkata / Bangalore): NABL accredited food testing facility; candidate for proximate composition, heavy metals, pesticide residues, and mineral profiling via ICP-OES.", bold_prefix="1. ")
    add_p(doc, "• Mitra S.K. Private Limited (Kolkata): NABL / FSSAI notified laboratory with extensive commodity testing infrastructure; candidate for proximate chemical analysis, fiber fractionation, and grain physical parameters.", bold_prefix="2. ")
    add_p(doc, "• CSIR-Central Glass & Ceramic Research Institute (CGCRI, Kolkata): Premier central research institute; candidate for advanced materials characterization, scanning electron microscopy (SEM), and thermal analysis.", bold_prefix="3. ")
    add_p(doc, "• Department of Chemical Engineering, IIT Kharagpur: Premier academic institution; candidate for advanced biophysical characterization, differential scanning calorimetry (DSC), and texture profile analysis under research collaboration protocols.", bold_prefix="4. ")

    # Annexure B: 15 MT/day Plant Concept & Mass Balance Reconciliation
    add_h1(doc, "Annexure B: Provisional 15,000 kg/day Plant Concept & Mass-Balance Reconciliation")
    add_p(doc, "To resolve Review Finding B and Finding F, this annexure provides the complete mathematical and thermodynamic derivation of the provisional 15,000 kg/day industrial processing concept. The plant concept is strictly a downstream conceptual scenario; final engineering sizing is gated upon Phase 1 and Phase 2 empirical data.")
    
    add_h2(doc, "B.1 Mathematical Derivation & Basis Reconciliation")
    add_p(doc, "Incoming Raw Grain: Total feed M_feed = 15,000.000 kg/day at 10.5% wet-basis moisture (X_wb = 0.105). Dry solids M_ds,in = 15,000 x (1 - 0.105) = 13,425.000 kg/day. Intrinsic grain water M_water,in = 1,575.000 kg/day.")
    add_p(doc, "Solids Loss Audit: One reported assumption states an absolute solids loss of 184.000 kg/day, leaving 13,241.000 kg/day dry solids. This loss represents exactly 1.370577% (approx. 1.3706%) of incoming dry solids. An alternate assumption in earlier notes stated a 1.46% solids loss, which would equal 13,425 x 0.0146 = 196.005 kg/day loss, leaving 13,228.995 kg/day dry solids. These two assumptions are mathematically distinct. For this reconciliation, the documented solids value of 13,241.000 kg/day is adopted.")
    add_p(doc, "Final Dried Product: Commercial product target moisture is 10.0% wet-basis (X_wb = 0.100). Total product mass M_prod = 13,241.000 / (1 - 0.100) = 14,712.222 kg/day, containing 1,471.222 kg/day water.")

    add_h2(doc, "B.2 Reconciled Pre-Dryer & Evaporation Scenarios")
    add_p(doc, "Because post-drainage surface liquid retention has not yet been measured for the target Tanzanian lot, two competing scenarios are reconciled:")

    tbl_b_scen = doc.add_table(rows=7, cols=3)
    tbl_b_scen.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_b_scen.autofit = False
    set_table_borders(tbl_b_scen)
    tbl_b_scen.columns[0].width = Inches(2.5)
    tbl_b_scen.columns[1].width = Inches(2.2)
    tbl_b_scen.columns[2].width = Inches(2.3)
    
    make_header_row(tbl_b_scen.rows[0])
    tbl_b_scen.rows[0].cells[0].paragraphs[0].text = "Mass & Moisture Parameter"
    tbl_b_scen.rows[0].cells[1].paragraphs[0].text = "Scenario B1 (True 28.0% WB)"
    tbl_b_scen.rows[0].cells[2].paragraphs[0].text = "Scenario B2 (Reported 18,590 kg/day)"
    
    scen_rows = [
        ("Pre-Dryer Total Wet Stream Mass", "18,390.278 kg/day", "18,590.000 kg/day"),
        ("Pre-Dryer Dry Solids Mass", "13,241.000 kg/day", "13,241.000 kg/day"),
        ("Pre-Dryer Water Content", "5,149.278 kg/day", "5,349.000 kg/day"),
        ("Pre-Dryer Wet-Basis Moisture Content", "28.0000% w/w", "28.7735% w/w (Implied)"),
        ("Final Product Water (10.0% WB)", "1,471.222 kg/day", "1,471.222 kg/day"),
        ("Dryer Water Evaporation Required", "3,678.056 kg/day (183.90 kg/h)", "3,877.778 kg/day (193.89 kg/h)")
    ]
    for idx, (p_lbl, p_b1, p_b2) in enumerate(scen_rows):
        row = tbl_b_scen.rows[idx + 1]
        row.cells[0].paragraphs[0].text = p_lbl
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = p_b1
        row.cells[2].paragraphs[0].text = p_b2
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)

    add_p(doc, "Thermodynamic Duty Impact: Scenario B2 requires evaporating 199.722 kg/day more water (+5.43%) than Scenario B1. At an effective heat of vaporization of 2,400 kJ/kg, continuous thermal drying duty increases from 122.60 kW_th (Scenario B1) to 129.26 kW_th (Scenario B2), increasing steam demand by 12.9 kg/h. Status of Finding B is UNRESOLVED — SCENARIOS SHOWN; final dryer sizing is held provisional until bench-scale hydration and drainage are measured.")

    # Annexure C
    add_h1(doc, "Annexure C: Sample Custody & Metadata Registration Form")
    add_p(doc, "Please complete and enclose this verification form with the dispatched sample consignments:")

    tbl_meta_form = doc.add_table(rows=8, cols=2)
    tbl_meta_form.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_meta_form.autofit = False
    set_table_borders(tbl_meta_form)
    tbl_meta_form.columns[0].width = Inches(2.5)
    tbl_meta_form.columns[1].width = Inches(4.5)
    
    meta_fields = [
        ("Sample Unique Identifier:", "[ To be assigned upon receipt at FinnoaQ Lab ]"),
        ("Commercial Origin & Cultivar:", "[ e.g. Tanzanian Arusha / Indian Latur Desi ]"),
        ("Consignment / Lot Number:", "[ Bill of Lading / Invoice Batch Number ]"),
        ("Date of Dehulling / Milling:", "[ DD/MM/YYYY or estimated month ]"),
        ("Import Date & Port of Entry:", "[ Applicable for imported consignments ]"),
        ("Polishing / Surface Treatment:", "[ e.g. Water polish / Oil polish / Unpolished ]"),
        ("Storage History & Packaging:", "[ e.g. 50 kg PP woven bags / Climate controlled ]"),
        ("Authorized Dispatch Contact:", "[ Name, Designation, Phone, Email ]")
    ]
    for idx, (f_lbl, f_val) in enumerate(meta_fields):
        row = tbl_meta_form.rows[idx]
        row.cells[0].paragraphs[0].text = f_lbl
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = f_val
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)

    # Annexure D
    add_h1(doc, "Annexure D: Scientific References & Regulatory Citations")
    add_p(doc, "1. AOAC International. (2019). Official Methods of Analysis of AOAC International (21st ed.). Gaithersburg, MD: AOAC International.")
    add_p(doc, "2. Bureau of Indian Standards. (2014). IS 4333: Methods of Analysis for Foodgrains. New Delhi: BIS.")
    add_p(doc, "3. Food Safety and Standards Authority of India (FSSAI). (2011). Food Safety and Standards (Food Products Standards and Food Additives) Regulations. Compendium of Food Additives & Standard 2.4.6.15 (Pulses).")
    add_p(doc, "4. Hincks, M. J., & Stanley, D. W. (1986). Multiple mechanisms for the hard-to-cook defect in dry beans. Journal of Food Science, 51(3), 738-742.")
    add_p(doc, "5. Jones, P. M. B., & Boulter, D. (1983). The cause of reduced cooking quality in stored cowpeas. Journal of Food Science, 48(2), 629-634.")
    add_p(doc, "6. Sefa-Dedeh, S., Stanley, D. W., & Voisey, P. W. (1979). Effect of storage conditions on cooking quality and microstructure of cowpeas. Journal of Food Science, 44(5), 1309-1314.")
    add_p(doc, "7. Tiwari, B. K., Gowen, A., & McKenna, B. (2011). Pulse Foods: Processing, Quality and Nutritive Value. Academic Press.")

    # Annexure E
    add_h1(doc, "Annexure E: Source SOW 36-Section Traceability & Concordance Matrix")
    add_p(doc, "Concordance audit verifying that all 36 numbered sections from the source SOW (Phase1_Scope_of_Work_Toor_Dal.docx) are substantively preserved:")

    tbl_e = doc.add_table(rows=10, cols=3)
    tbl_e.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_e.autofit = False
    set_table_borders(tbl_e)
    tbl_e.columns[0].width = Inches(1.5)
    tbl_e.columns[1].width = Inches(2.5)
    tbl_e.columns[2].width = Inches(3.0)
    
    make_header_row(tbl_e.rows[0])
    tbl_e.rows[0].cells[0].paragraphs[0].text = "Source Sections"
    tbl_e.rows[0].cells[1].paragraphs[0].text = "Source Scope Domain"
    tbl_e.rows[0].cells[2].paragraphs[0].text = "Revised Proposal Location & Status"
    
    e_rows = [
        ("Sections 1–3", "Background, Objectives, Samples", "Sections 1, 2, 3, 7 (Preserved 100%; whistle context qualified)"),
        ("Sections 4–7", "Approach, Physical, Proximate, Starch", "Sections 5, 8 (WP-01, WP-02, WP-03 incorporated)"),
        ("Sections 8–11", "Hydration, Structure, Pectin, Minerals", "Sections 8 (WP-04, WP-05, WP-06, WP-07 incorporated)"),
        ("Sections 12–15", "Texture, Standardized Cooking Design", "Sections 8, 9 (WP-08, WP-09, instrumented endpoint defined)"),
        ("Sections 16–18", "Root-Cause Pathway & Phase 2 Tech", "Sections 6, 10 (10-hypothesis register, distinct reagents)"),
        ("Sections 19–20", "QC, Statistics, Integrated Analysis", "Sections 8, 9 (Replication hierarchy, Welch's t-test, ANOVA)"),
        ("Sections 21–23", "Deliverables, Report Outline, Labs", "Section 12, Annexure A (All 14 deliverables mapped)"),
        ("Sections 24–29", "Fees, Ceiling, Timeline, Payments", "Sections 13, 14 (₹1,73,000 line items, ₹2L ceiling, 40/40/20%)"),
        ("Sections 30–36", "Retention, NDA, Limits, Contacts", "Sections 4, 15, 16, 18 (Client data ownership, Harakutir contact)")
    ]
    for idx, (e_sec, e_dom, e_loc) in enumerate(e_rows):
        row = tbl_e.rows[idx + 1]
        row.cells[0].paragraphs[0].text = e_sec
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].paragraphs[0].text = e_dom
        row.cells[2].paragraphs[0].text = e_loc
        make_data_row(row, is_zebra=(idx % 2 == 1), font_size=7.5)

    add_p(doc, "Concordance Summary: 36 of 36 sections mapped with zero substantive omission. All scope boundaries strictly protected.")

def main():
    doc = docx.Document()
    setup_page_header_footer(doc)
    populate_proposal(doc)
    
    out_dir = r"toor_dal_optimization\deliverables"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.docx")
    doc.save(out_path)
    print(f"Successfully generated proposal DOCX: {out_path}")
    
    # Also save to root deliverables/ for direct convenience
    root_out = r"deliverables\PHASE1_TOOR_DAL_DIAGNOSTIC_RND_PROPOSAL_REV_V10.docx"
    doc.save(root_out)
    print(f"Successfully saved copy to: {root_out}")

if __name__ == "__main__":
    main()
