# FinnoaQ Single-Project Engineering Demonstration Microsite
**Project Reference:** FNQ-PR-2026-001 | Gate G-A Baseline Rev 8.4  
**Project Title:** Imported Split Pigeon Pea Cooking-Time Reduction & 15 MT/day Conceptual Plant Engineering  
**Lead Chemical & Process Engineer:** Sourish Senapati (*FinnoaQ Agro-Industrial Technologies Ltd.*)  
**Academic Guidance:** Technical Advisory Panel  

---

## Overview

This repository hosts the client-facing demonstration microsite built specifically for an Indian industrial pulse milling stakeholder to evaluate the Phase 1 diagnostic programme and conceptual 15 MT/day tenderization plant architecture.

### Truth Status
- **Treatment Discovery:** Chemical tenderization conditions are currently in discovery and screening. Physical validation is strictly **PENDING** physical sample intake and controlled testing on target imported lots.
- **Plant Sizing:** The 15,000 kg/day facility represents a **TARGET CONCEPTUAL DESIGN BASIS** derived from Aspen Plus V14 property simulations (NRTL / STEAM-TA, 0.000000% error closure) and ASME Section VIII sizing, not an operating or commissioned plant.

---

## Getting Started

### Prerequisites
- Node.js >= 18.0.0 (Node.js v24.11.1 verified)
- Modern web browser (Chrome, Edge, Firefox, Safari)

### Installation
```bash
npm install
```

### Local Development Server
```bash
npm run dev -- --host 127.0.0.1 --port 5174
```
Access the application at `http://127.0.0.1:5174/`.

### Production Build
```bash
npm run build
```
Generates optimized static assets in `portal/dist/` with zero runtime errors.

### Multi-Viewport Visual QA Capture
```bash
node scripts/capture_qa_screenshots.js
```
Captures desktop (1440px, 1280px), tablet (768px), and mobile (390px, 360px) raster captures directly into `../docs/project-demo/screenshots/`.

---

## Governance & Verification Registers
- Baseline Audit: `../docs/project-demo/BASELINE_AUDIT.md`
- Content Claim Register: `../docs/project-demo/CONTENT_CLAIM_REGISTER.csv`
- Disclosable Asset Register: `../docs/project-demo/ASSET_REGISTER.csv`
- Reference Design Audit: `../docs/project-demo/REFERENCE_AUDIT.md`
- Website QA & Acceptance Report: `../docs/project-demo/WEBSITE_QA_REPORT.md`
