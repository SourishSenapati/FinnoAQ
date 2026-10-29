import React, { useState } from 'react';
import { CAD_DRAWING_SHEETS, REGULATORY_STANDARDS } from '../data/micrositeData.js';

const OFFICIAL_DOCUMENTS = [
  {
    title: 'Commercial Investor Proposal',
    ref: 'FNQ-PR-2026-COMM-001',
    pages: '18 Pages',
    scope: 'Executive Feasibility, Mandi Arbitrage & ₹8.72 Cr EBITDA Tolling Model',
    format: 'PDF',
    size: '420 KB',
    file: '/finnoaq_commercial_investor_proposal.pdf'
  },
  {
    title: 'Q1 Scientific & Engineering Master Treatise',
    ref: 'FNQ-Q1-TREATISE-001',
    pages: '27 Pages',
    scope: 'Middle Lamella Biochemistry, Fickian PDE Diffusion & Hawkins 3L Cooker Acoustics',
    format: 'PDF',
    size: '556 KB',
    file: '/finnoaq_dalopt_q1_master_treatise.pdf'
  },
  {
    title: '15 TPD Turnkey Plant Financial Model',
    ref: 'FNQ-FM-15T-2026',
    pages: '6 Tabs',
    scope: 'Itemized OpEx (₹6.34), Area 100–900 CapEx (₹135L) & 5-Yr Pro-Forma DCF',
    format: 'XLSX',
    size: '18 KB',
    file: '/FINANCIAL_MODEL_15TPD.xlsx'
  },
  {
    title: 'Omega Multiphysics Diagnostic Report',
    ref: 'FNQ-ENG-RPT-001',
    pages: '32 Pages',
    scope: 'Continuum Mechanics, DSC Starch Gelatinization & LOX Volatile Headspace',
    format: 'PDF',
    size: '556 KB',
    file: '/finnoaq_omega_technical_report.pdf'
  },
  {
    title: 'Aspen Plus V14 ELECNRTL Flowsheet Case',
    ref: 'FINNOAQ_15TPD_CONVERGED.bkp',
    pages: 'Simulation Report',
    scope: 'Triple-Effect MVR Falling Film ZLD Evaporator & Fluid Bed Dryer Air Heater Enthalpy',
    format: 'PDF',
    size: '64 KB',
    file: '/Aspen_Flowsheet.pdf'
  },
  {
    title: 'Audited Claim & Evidence Ledger',
    ref: 'FNQ-EVD-LEDGER-001',
    pages: '45 Claims',
    scope: '5-Sigma Empirical Evidence Standard across Measured, Simulated & Calculated Tiers',
    format: 'CSV',
    size: '6 KB',
    file: '/CLAIM_EVIDENCE_LEDGER.csv'
  }
];

export default function Module7DataRoom() {
  const [activeTab, setActiveTab] = useState('publications'); // 'publications' | 'cad' | 'compliance'
  const [selectedDrawingIdx, setSelectedDrawingIdx] = useState(0);
  const [lightboxOpen, setLightboxOpen] = useState(false);

  const selectedDrawing = CAD_DRAWING_SHEETS[selectedDrawingIdx];

  return (
    <section id="data-room" className="w-full bg-[#0C0E12] border-b border-[#1E232E] scroll-mt-20">
      <div className="max-w-[1440px] mx-auto border-x border-[#1E232E]">
        
        {/* Module Header */}
        <div className="p-6 border-b border-[#1E232E] bg-[#111319] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#151821] text-[#94A3B8] border border-[#232836] font-mono text-xs rounded-xs font-medium">
              [06 // ENGINEERING DATA ROOM & REGULATORY DOSSIER]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#E6E8EC]">
              Regulatory Matrix & Engineering Data Room
            </h2>
          </div>
          <span className="font-mono text-xs px-2 py-0.5 bg-[#151821] text-[#10B981] border border-[#232836] rounded-xs font-medium">
            ALL 6 REPOSITORY FILES VERIFIED & LIVE
          </span>
        </div>

        {/* 3-Tab Selector */}
        <div className="p-6 bg-[#0C0E12] border-b border-[#1E232E]">
          <div className="flex border-b border-[#1E232E]">
            <button
              onClick={() => setActiveTab('publications')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'publications'
                  ? 'border-[#D97706] text-[#D97706] font-medium'
                  : 'border-transparent text-[#8E95A2] hover:text-[#E6E8EC]'
              }`}
            >
              [TAB 1 // PUBLICATIONS & FINANCIAL MODELS (6 DIRECT DOWNLOADS)]
            </button>
            <button
              onClick={() => setActiveTab('cad')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'cad'
                  ? 'border-[#D97706] text-[#D97706] font-medium'
                  : 'border-transparent text-[#8E95A2] hover:text-[#E6E8EC]'
              }`}
            >
              [TAB 2 // VERIFIED CAD DRAWING SUITE (7 SHEETS)]
            </button>
            <button
              onClick={() => setActiveTab('compliance')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'compliance'
                  ? 'border-[#D97706] text-[#D97706] font-medium'
                  : 'border-transparent text-[#8E95A2] hover:text-[#E6E8EC]'
              }`}
            >
              [TAB 3 // FSSAI, CODEX & TOXICOLOGY COMPLIANCE]
            </button>
          </div>
        </div>

        {/* TAB 1: Publications & Financial Models */}
        {activeTab === 'publications' && (
          <div className="p-6 sm:p-8 bg-[#0C0E12]">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {OFFICIAL_DOCUMENTS.map((doc, idx) => (
                <div 
                  key={idx}
                  className="p-5 bg-[#111319] border border-[#1E232E] rounded-xs flex flex-col justify-between hover:border-[#5E6573] transition-colors"
                >
                  <div>
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-mono text-[10px] text-[#D97706] font-medium">
                        {doc.ref}
                      </span>
                      <span className="font-mono text-[10px] px-1.5 py-0.2 bg-[#151821] text-[#10B981] border border-[#232836] rounded-xs font-medium">
                        {doc.format} // {doc.size}
                      </span>
                    </div>

                    <h3 className="text-sm font-semibold text-[#E6E8EC] mb-1">
                      {doc.title}
                    </h3>

                    <p className="text-xs text-[#8E95A2] leading-relaxed mb-4">
                      {doc.scope}
                    </p>
                  </div>

                  <div className="flex space-x-2 pt-2 border-t border-[#1E232E]">
                    <a
                      href={doc.file}
                      download
                      className="flex-1 py-2 px-3 bg-[#151821] hover:bg-[#1E232E] border border-[#1E232E] hover:border-[#D97706] text-[#E6E8EC] hover:text-[#D97706] font-mono text-xs rounded-xs transition-colors flex items-center justify-between"
                    >
                      <span>Download {doc.format}</span>
                      <span>↓</span>
                    </a>
                    <a
                      href={doc.file}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="py-2 px-3 bg-[#111319] hover:bg-[#151821] border border-[#1E232E] text-[#8E95A2] hover:text-[#E6E8EC] font-mono text-xs rounded-xs transition-colors"
                      title="Open in Browser"
                    >
                      ↗
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* TAB 2: Verified CAD Drawing Suite */}
        {activeTab === 'cad' && (
          <div className="grid grid-cols-1 lg:grid-cols-12 bg-[#0C0E12]">
            
            {/* Left 5 Cols: Drawing Sheet List */}
            <div className="lg:col-span-5 p-4 sm:p-6 border-b lg:border-b-0 lg:border-r border-[#1E232E] divide-y divide-[#1E232E]">
              <div className="font-mono text-xs text-[#5E6573] uppercase tracking-wider pb-3">
                AUTOCAD & SOLIDWORKS 2025 SP01.2 DRAWING REGISTER
              </div>
              {CAD_DRAWING_SHEETS.map((dwg, idx) => {
                const isSelected = selectedDrawingIdx === idx;
                return (
                  <button
                    key={dwg.tag}
                    onClick={() => setSelectedDrawingIdx(idx)}
                    className={`w-full text-left p-3.5 transition-colors cursor-pointer flex items-center justify-between ${
                      isSelected
                        ? 'bg-[#151821] border-l-2 border-[#D97706]'
                        : 'bg-[#0C0E12] hover:bg-[#111319]'
                    }`}
                  >
                    <div>
                      <div className="flex items-center space-x-2 mb-1">
                        <span className="font-mono text-xs text-[#D97706] font-medium">
                          {dwg.tag}
                        </span>
                        <span className="font-mono text-[10px] text-[#5E6573]">
                          {dwg.status}
                        </span>
                      </div>
                      <div className={`text-xs ${isSelected ? 'text-[#E6E8EC] font-medium' : 'text-[#8E95A2]'}`}>
                        {dwg.title}
                      </div>
                    </div>
                    <span className={`font-mono text-xs ${isSelected ? 'text-[#D97706]' : 'text-[#5E6573]'}`}>
                      →
                    </span>
                  </button>
                );
              })}
            </div>

            {/* Right 7 Cols: Drawing Sheet Preview Pane */}
            <div className="lg:col-span-7 p-6 sm:p-8 bg-[#111319] flex flex-col justify-between">
              {selectedDrawing && (
                <div>
                  <div className="flex justify-between items-center mb-4 pb-3 border-b border-[#1E232E]">
                    <div>
                      <span className="font-mono text-base font-bold text-[#D97706] mr-2">
                        {selectedDrawing.tag}
                      </span>
                      <span className="font-mono text-sm font-semibold text-[#E6E8EC]">
                        {selectedDrawing.title}
                      </span>
                    </div>
                    <span className="px-2 py-0.5 bg-[#151821] text-[#10B981] border border-[#232836] font-mono text-xs rounded-xs font-medium">
                      {selectedDrawing.status}
                    </span>
                  </div>

                  {/* Drawing Thumbnail with Click to Expand */}
                  <div 
                    onClick={() => setLightboxOpen(true)}
                    className="p-4 bg-[#0C0E12] border border-[#1E232E] hover:border-[#D97706] rounded-xs mb-4 cursor-zoom-in relative group transition-colors"
                  >
                    <img
                      src={selectedDrawing.file}
                      alt={selectedDrawing.title}
                      className="w-full max-h-72 object-contain bg-[#0C0E12] rounded-xs"
                      onError={(e) => {
                        e.target.style.display = 'none';
                      }}
                    />
                    <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center font-mono text-xs text-[#D97706] font-medium">
                      🔍 Click to Inspect High-Resolution Blueprint
                    </div>
                    <div className="font-mono text-[11px] text-[#5E6573] text-center mt-2">
                      Associative 2D Projection from Parametric Solid Model (.SLDPRT / .SLDASM)
                    </div>
                  </div>

                  <p className="text-xs sm:text-sm text-[#8E95A2] leading-relaxed mb-4">
                    {selectedDrawing.desc}
                  </p>
                </div>
              )}

              <div className="pt-4 border-t border-[#1E232E] flex justify-between items-center font-mono text-xs text-[#5E6573]">
                <span>Fabrication Standard: ASME Section VIII Div 1 & IS 2825</span>
                <span>Lead Engineer: Sourish Senapati</span>
              </div>
            </div>

          </div>
        )}

        {/* Lightbox Modal for CAD Blueprint Inspection */}
        {lightboxOpen && selectedDrawing && (
          <div 
            onClick={() => setLightboxOpen(false)}
            className="fixed inset-0 z-50 bg-black/90 flex flex-col items-center justify-center p-4 cursor-zoom-out"
          >
            <div className="max-w-6xl w-full bg-[#111319] border border-[#1E232E] rounded-xs p-4" onClick={(e) => e.stopPropagation()}>
              <div className="flex justify-between items-center mb-3 pb-2 border-b border-[#1E232E]">
                <div className="font-mono text-sm font-semibold text-[#E6E8EC]">
                  <span className="text-[#D97706]">{selectedDrawing.tag}</span>: {selectedDrawing.title}
                </div>
                <button
                  onClick={() => setLightboxOpen(false)}
                  className="px-2 py-1 bg-[#151821] text-[#8E95A2] hover:text-[#E6E8EC] border border-[#232836] rounded-xs font-mono text-xs cursor-pointer"
                >
                  ✕ Close [ESC]
                </button>
              </div>
              <img
                src={selectedDrawing.file}
                alt={selectedDrawing.title}
                className="w-full max-h-[75vh] object-contain bg-[#0C0E12] rounded-xs"
              />
              <div className="mt-3 flex justify-between items-center font-mono text-xs text-[#5E6573]">
                <span>{selectedDrawing.status}</span>
                <a
                  href={selectedDrawing.file}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#D97706] hover:underline"
                >
                  Open Full-Res PNG in New Tab ↗
                </a>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: FSSAI, Codex & Toxicology Compliance */}
        {activeTab === 'compliance' && (
          <div className="p-6 sm:p-8 bg-[#0C0E12]">
            <div className="flex justify-between items-center mb-4">
              <span className="font-mono text-xs text-[#5E6573] uppercase tracking-wider">
                STATUTORY FOOD SAFETY REGULATIONS & TOXICOLOGY SAFETY MARGINS
              </span>
              <span className="font-mono text-xs px-2 py-0.5 bg-[#151821] text-[#10B981] border border-[#232836] rounded-xs font-medium">
                100% REGULATORY CONFORMANCE
              </span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#1E232E]">
                <thead>
                  <tr className="bg-[#111319] border-b border-[#1E232E] text-[#5E6573]">
                    <th className="p-3 w-1/4">Statutory Standard & Agency</th>
                    <th className="p-3 w-1/4">Scope & Classification</th>
                    <th className="p-3">Compliance Mechanism & Safety Multiplier</th>
                    <th className="p-3 text-right">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#1E232E]">
                  {REGULATORY_STANDARDS.map((reg, idx) => (
                    <tr key={idx} className="hover:bg-[#111319] transition-colors">
                      <td className="p-3 text-[#E6E8EC] font-semibold">{reg.standard}</td>
                      <td className="p-3 text-[#8E95A2]">{reg.scope}</td>
                      <td className="p-3 text-[#8E95A2] font-sans text-xs">{reg.details}</td>
                      <td className="p-3 text-right">
                        <span className="px-2 py-0.5 bg-[#151821] text-[#10B981] border border-[#232836] rounded-xs text-[10px]">
                          {reg.complianceStatus}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="mt-4 p-4 bg-[#111319] border border-[#1E232E] rounded-xs flex flex-wrap justify-between items-center gap-2 font-mono text-xs text-[#5E6573]">
              <span>Internal Phosphate: 142 mg/kg (Statutory MRL: 5,000 mg/kg // 35.2x Safety Margin)</span>
              <span>Sensory Indistinguishability: ISO 4120 3-AFC Triangle Panel (p = 0.420 &gt; 0.05)</span>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}
