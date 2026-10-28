# V8 Native Engineering Toolchain Status & Diagnostic Audit
**Document Ref:** FNQ-V8-TOOLCHAIN-001  
**Execution Mode:** Offline-First | Native Applications Verified | Zero Synthetic Emulation  
**Timestamp:** 2026-10-17 00:04:15 +0530  
**Lead Engineer:** Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)  
**Academic Guidance:** Technical Advisory Panel  

---

## 1. Executive Toolchain Health Summary

| Tool / Subsystem | Physical Executable / Target | Status | Verification Evidence / Diagnostics |
| :--- | :--- | :--- | :--- |
| **Python Runtime** | `C:\Python313\python.exe` (v3.13.7) | **ACTIVE** | `pywin32`, `torch` 2.6.0+cu124, `ezdxf` 1.4.4, `fitz` 1.27.2.2 verified |
| **SolidWorks 2025** | `C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS (2)\SLDWORKS.exe` (SP01.2) | **VERIFIED LOCAL** | Native 3D parts & assemblies open and rebuildable; `.SLDPRT` / `.SLDASM` active |
| **Aspen Plus V14** | `D:\Engineering Software\ASPENONE64bit\Aspen Plus V14.0\GUI\Xeq\AspenPlus.exe` | **VERIFIED LOCAL** | COM ProgID `Apwn.Document` available; converged simulation `FINNOAQ_15TPD_CONVERGED.bkp` |
| **AutoCAD 2025** | `C:\Program Files\Autodesk\AutoCAD 2025\acad.exe` | **VERIFIED LOCAL** | AutoCAD 2025 binaries installed; `accoreconsole.exe` available |
| **Word COM** | `win32com.client.Dispatch("Word.Application")` | **ACTIVE** | Microsoft Word COM automation fully functional for proposal DOCX/PDF export |

---

## 2. SolidWorks Automation Root-Cause Diagnostic

### 2.1 Observable Defect & Registry Architecture
1. **Registry Mapping:** Windows Registry `CLSID\{6af263bb-eb9f-4176-89e9-4f892eb0ca3d}\LocalServer32` points to `C:\PROGRA~1\SOLIDW~1\SOLIDW~1\SLDWORKS.exe`, which resolves in short-name notation to `C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS (2)\SLDWORKS.exe`.
2. **Execution Phenomenon:** Direct execution of `SLDWORKS.exe` initializes the process. However, calling `win32com.client.Dispatch("SldWorks.Application")` during an ongoing unattached subprocess triggers DCOM single-instance mutex conflict resulting in `0x80080005: CO_E_SERVER_EXEC_FAILURE`.
3. **Corrective Protocol (§1.2 Rule 9):**
   - SolidWorks automation must run in clean, single-process sessions.
   - Do not spawn detached subprocesses before calling COM dispatch.
   - Genuine associative drawings previously compiled (`DWG-FIN-15T-007_SOLIDWORKS_MODEL_DERIVED.pdf`) confirm that SolidWorks drawing view projection (`CreateDrawViewFromModelView3`) works reliably when the COM server starts in isolation.

---

## 3. Aspen Plus Thermodynamic Simulation Scope & Physics Boundary

1. **Simulation File:** `engineering/aspen/FINNOAQ_15TPD_CONVERGED.bkp` (157,811 bytes).
2. **Model Scope:**
   - Triple-effect falling film evaporator for spent soak liquor concentration.
   - Calandrias COIL-1 (310.5 kW), COIL-2 (268.4 kW), COIL-3 (224.6 kW).
   - Flash separators STAGE-1 (0.578 bar a, 85°C), STAGE-2 (0.312 bar a, 70°C), STAGE-3 (0.157 bar a, 55°C).
   - Fluid bed dryer steam air preheater HE-101 (512.4 kW).
   - Surface condenser COND-1 (138.2 kW).
3. **Thermodynamic Basis:**
   - Steam/water: `STEAM-TA` (ASME 1967 Steam Tables).
   - Soak liquor: `NRTL` (Non-Random Two-Liquid activity coefficient model).
4. **Mandatory Physics Boundary Statement:**
   > **CRITICAL BOUNDARY:** Aspen Plus V14 strictly models vapor-liquid equilibrium, latent heats, and convective air psychrometrics. Legume cellular hydration, pectin esterase cleavage, phytate-calcium chelation, and starch swelling kinetics are **NOT** represented in Aspen Plus and must be investigated empirically via wet-lab experimental screening in Phase 1.

---

## 4. Rejection of Synthetic Drawing Generator

The script `scratch/build_world_class_cad_drawing_suite.py` was subjected to forensic audit:
- It imported `PIL.Image`, `PIL.ImageDraw`, and `PIL.ImageFont`.
- It drew artificial coordinate boxes, dashed lines, and ASME title blocks directly onto blank pixel grids.
- It generated 7 raster images pretending to be CAD drawings and compiled them into `FINNOAQ_15TPD_ENGINEERING_DRAWINGS.pdf`.

**Official Disposition:**
- Script classified as: **PROHIBITED SYNTHETIC PROXY**.
- Output drawings classified as: **REJECTED—DO NOT ISSUE**.
- Excluded entirely from the client proposal package.
- Preserved solely in the audit archive for transparency.
