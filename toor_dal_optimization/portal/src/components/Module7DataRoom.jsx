import React, { useState } from 'react';
import { CAD_DRAWING_SHEETS, REGULATORY_STANDARDS } from '../data/micrositeData.js';

const OFFICIAL_DOCUMENTS = [
  {
    title: 'Commercial Investor Proposal',
    ref: 'FNQ-PR-2026-COMM-001',
    pages: '18 Pages',
    scope: 'Executive Feasibility, Mandi Arbitrage & ₹8.72 Cr EBITDA Tolling Model',
    format: 'PDF',
    file: '/finnoaq_commercial_investor_proposal.pdf'
  },
  {
    title: 'Q1 Scientific & Engineering Master Treatise',
    ref: 'FNQ-Q1-TREATISE-001',
    pages: '27 Pages',
    scope: 'Middle Lamella Biochemistry, Fickian PDE Diffusion & Hawkins 3L Cooker Acoustics',
    format: 'PDF',
    file: '/finnoaq_dalopt_q1_master_treatise.pdf'
  },
  {
    title: '15 TPD Turnkey Plant Financial Model',
    ref: 'FNQ-FM-15T-2026',
    pages: '6 Tabs',
    scope: 'Itemized OpEx (₹6.34), Area 100–900 CapEx (₹135L) & 5-Yr Pro-Forma DCF',
    format: 'XLSX',
    file: '/FINANCIAL_MODEL_15TPD.xlsx'
  },
  {
    title: 'Omega Multiphysics Diagnostic Report',
    ref: 'FNQ-ENG-RPT-001',
    pages: '32 Pages',
    scope: 'Continuum Mechanics, DSC Starch Gelatinization & LOX Volatile Headspace',
    format: 'PDF',
    file: '/finnoaq_omega_technical_report.pdf'
  },
  {
    title: 'Aspen Plus V14 ELECNRTL Flowsheet Case',
    ref: 'FINNOAQ_15TPD_CONVERGED.bkp',
    pages: 'Simulation Report',
    scope: 'Triple-Effect MVR Falling Film ZLD Evaporator & Fluid Bed Dryer Air Heater Enthalpy',
    format: 'PDF',
    file: '/Aspen_Flowsheet.pdf'
  },
  {
    title: 'Audited Claim & Evidence Ledger',
    ref: 'FNQ-EVD-LEDGER-001',
    pages: '45 Claims',
    scope: '5-Sigma Empirical Evidence Standard across Measured, Simulated & Calculated Tiers',
    format: 'CSV',
    file: '/CLAIM_EVIDENCE_LEDGER.csv'
  }
];

export default function Module7DataRoom() {
  const [activeTab, setActiveTab] = useState('publications'); // 'publications' | 'cad' | 'compliance'
  const [selectedDrawingIdx, setSelectedDrawingIdx] = useState(0);

  const selectedDrawing = CAD_DRAWING_SHEETS[selectedDrawingIdx];

  return (
    <section id="data-room" className="w-full bg-[#0A0B0D] border-b border-[#222630]">
      <div className="max-w-[1440px] mx-auto border-x border-[#222630]">
        
        {/* Module Header */}
        <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [06 // ENGINEERING DATA ROOM & REGULATORY DOSSIER]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#F3F4F6]">
              Regulatory Matrix & Engineering Data Room
            </h2>
          </div>
          <span className="font-mono text-xs text-[#64748B]">
            ASME / FSSAI / CODEX AUDITED REPOSITORY
          </span>
        </div>

        {/* 3-Tab Selector */}
        <div className="p-6 bg-[#0A0B0D] border-b border-[#222630]">
          <div className="flex border-b border-[#222630]">
            <button
              onClick={() => setActiveTab('publications')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'publications'
                  ? 'border-[#F59E0B] text-[#F59E0B] font-semibold'
                  : 'border-transparent text-[#9CA3AF] hover:text-[#F3F4F6]'
              }`}
            >
              [TAB 1 // PUBLICATIONS & FINANCIAL MODELS (6 EXPORTS)]
            </button>
            <button
              onClick={() => setActiveTab('cad')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'cad'
                  ? 'border-[#F59E0B] text-[#F59E0B] font-semibold'
                  : 'border-transparent text-[#9CA3AF] hover:text-[#F3F4F6]'
              }`}
            >
              [TAB 2 // VERIFIED CAD DRAWING SUITE (7 SHEETS)]
            </button>
            <button
              onClick={() => setActiveTab('compliance')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'compliance'
                  ? 'border-[#F59E0B] text-[#F59E0B] font-semibold'
                  : 'border-transparent text-[#9CA3AF] hover:text-[#F3F4F6]'
              }`}
            >
              [TAB 3 // FSSAI, CODEX & TOXICOLOGY COMPLIANCE]
            </button>
          </div>
        </div>

        {/* TAB 1: Publications & Financial Models */}
        {activeTab === 'publications' && (
          <div className="p-6 sm:p-8 bg-[#0A0B0D]">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {OFFICIAL_DOCUMENTS.map((doc, idx) => (
                <div 
                  key={idx}
                  className="p-5 bg-[#111317] border border-[#222630] rounded-sm flex flex-col justify-between hover:border-[#64748B] transition-colors"
                >
                  <div>
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-mono text-[10px] text-[#F59E0B] font-semibold">
                        {doc.ref}
                      </span>
                      <span className="font-mono text-[10px] px-1.5 py-0.2 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] rounded-xs">
                        {doc.format} // {doc.pages}
                      </span>
                    </div>

                    <h3 className="text-sm font-semibold text-[#F3F4F6] mb-1">
                      {doc.title}
                    </h3>

                    <p className="text-xs text-[#9CA3AF] leading-relaxed mb-4">
                      {doc.scope}
                    </p>
                  </div>

                  <a
                    href={doc.file}
                    download
                    className="w-full py-2 px-3 bg-[#171A21] hover:bg-[#222630] border border-[#222630] hover:border-[#F59E0B] text-[#F3F4F6] hover:text-[#F59E0B] font-mono text-xs rounded-sm transition-colors flex items-center justify-between"
                  >
                    <span>Download {doc.format} File</span>
                    <span>↓</span>
                  </a>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* TAB 2: Verified CAD Drawing Suite */}
        {activeTab === 'cad' && (
          <div className="grid grid-cols-1 lg:grid-cols-12 bg-[#0A0B0D]">
            
            {/* Left 5 Cols: Drawing Sheet List */}
            <div className="lg:col-span-5 p-4 sm:p-6 border-b lg:border-b-0 lg:border-r border-[#222630] divide-y divide-[#222630]">
              <div className="font-mono text-xs text-[#64748B] uppercase tracking-wider pb-3">
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
                        ? 'bg-[#171A21] border-l-2 border-[#F59E0B]'
                        : 'bg-[#0A0B0D] hover:bg-[#111317]'
                    }`}
                  >
                    <div>
                      <div className="flex items-center space-x-2 mb-1">
                        <span className="font-mono text-xs text-[#F59E0B] font-semibold">
                          {dwg.tag}
                        </span>
                        <span className="font-mono text-[10px] text-[#64748B]">
                          {dwg.status}
                        </span>
                      </div>
                      <div className={`text-xs ${isSelected ? 'text-[#F3F4F6] font-medium' : 'text-[#9CA3AF]'}`}>
                        {dwg.title}
                      </div>
                    </div>
                    <span className={`font-mono text-xs ${isSelected ? 'text-[#F59E0B]' : 'text-[#64748B]'}`}>
                      →
                    </span>
                  </button>
                );
              })}
            </div>

            {/* Right 7 Cols: Drawing Sheet Preview Pane */}
            <div className="lg:col-span-7 p-6 sm:p-8 bg-[#111317] flex flex-col justify-between">
              {selectedDrawing && (
                <div>
                  <div className="flex justify-between items-center mb-4 pb-3 border-b border-[#222630]">
                    <div>
                      <span className="font-mono text-base font-bold text-[#F59E0B] mr-2">
                        {selectedDrawing.tag}
                      </span>
                      <span className="font-mono text-sm font-semibold text-[#F3F4F6]">
                        {selectedDrawing.title}
                      </span>
                    </div>
                    <span className="px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] font-mono text-xs rounded-sm">
                      {selectedDrawing.status}
                    </span>
                  </div>

                  {/* Drawing Thumbnail / Schematic Box */}
                  <div className="p-4 bg-[#0A0B0D] border border-[#222630] rounded-sm mb-4">
                    <img
                      src={selectedDrawing.file}
                      alt={selectedDrawing.title}
                      className="w-full max-h-72 object-contain bg-[#0A0B0D] rounded-xs"
                      onError={(e) => {
                        e.target.style.display = 'none';
                      }}
                    />
                    <div className="font-mono text-[11px] text-[#64748B] text-center mt-2">
                      Associative 2D Projection from Parametric Solid Model (.SLDPRT / .SLDASM)
                    </div>
                  </div>

                  <p className="text-xs sm:text-sm text-[#9CA3AF] leading-relaxed mb-4">
                    {selectedDrawing.desc}
                  </p>
                </div>
              )}

              <div className="pt-4 border-t border-[#222630] flex justify-between items-center font-mono text-xs text-[#64748B]">
                <span>Fabrication Standard: ASME Section VIII Div 1 & IS 2825</span>
                <span>Lead Engineer: Sourish Senapati</span>
              </div>
            </div>

          </div>
        )}

        {/* TAB 3: FSSAI, Codex & Toxicology Compliance */}
        {activeTab === 'compliance' && (
          <div className="p-6 sm:p-8 bg-[#0A0B0D]">
            <div className="flex justify-between items-center mb-4">
              <span className="font-mono text-xs text-[#64748B] uppercase tracking-wider">
                STATUTORY FOOD SAFETY REGULATIONS & TOXICOLOGY SAFETY MARGINS
              </span>
              <span className="font-mono text-xs px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm">
                100% REGULATORY CONFORMANCE
              </span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#222630]">
                <thead>
                  <tr className="bg-[#111317] border-b border-[#222630] text-[#64748B]">
                    <th className="p-3 w-1/4">Statutory Standard & Agency</th>
                    <th className="p-3 w-1/4">Scope & Classification</th>
                    <th className="p-3">Compliance Mechanism & Safety Multiplier</th>
                    <th className="p-3 text-right">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#222630]">
                  {REGULATORY_STANDARDS.map((reg, idx) => (
                    <tr key={idx} className="hover:bg-[#111317] transition-colors">
                      <td className="p-3 text-[#F3F4F6] font-semibold">{reg.standard}</td>
                      <td className="p-3 text-[#9CA3AF]">{reg.scope}</td>
                      <td className="p-3 text-[#9CA3AF] font-sans text-xs">{reg.details}</td>
                      <td className="p-3 text-right">
                        <span className="px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm text-[10px]">
                          {reg.complianceStatus}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="mt-4 p-4 bg-[#111317] border border-[#222630] rounded-sm flex flex-wrap justify-between items-center gap-2 font-mono text-xs text-[#64748B]">
              <span>Internal Phosphate: 142 mg/kg (Statutory MRL: 5,000 mg/kg // 35.2x Safety Margin)</span>
              <span>Sensory Indistinguishability: ISO 4120 3-AFC Triangle Panel (p = 0.420 &gt; 0.05)</span>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}
