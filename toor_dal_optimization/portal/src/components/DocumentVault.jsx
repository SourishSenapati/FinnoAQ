import React from 'react';
import { Download, FileText, Table, ShieldCheck, ExternalLink, Lock } from 'lucide-react';

export default function DocumentVault() {
  const documents = [
    {
      title: "Commercial Business Proposal & Scale-Up Dossier",
      tag: "18-PAGE INVESTOR FEASIBILITY",
      file: "/pdf/finnoaq_commercial_investor_proposal.pdf",
      format: "PDF",
      size: "420 kB",
      ref: "FNQ-PR-2026-COMM-001",
      accent: "#38BDF8",
      desc: "Turnkey 15 TPD investor pitch: ₹20.00/kg mandi arbitrage waterfall, S1-09 bio-chelation chemistry, ₹135L CapEx schedule, ₹6.34/kg OpEx, and audited 5-year financial returns (78.4% IRR, 1.12-year payback)."
    },
    {
      title: "Master Scientific Monograph & Physics Treatise",
      tag: "27-PAGE Q1 MONOGRAPH",
      file: "/pdf/finnoaq_dalopt_q1_master_treatise.pdf",
      format: "PDF",
      size: "556 kB",
      ref: "FNQ-PR-2026-Q1-TREATISE",
      accent: "#10B981",
      desc: "Exhaustive first-principles food engineering treatise: middle lamella calcium pectate bio-chelation thermodynamics, transient Fickian transport, Hawkins cooker acoustics (C100 = 28.4 min), and fluid-bed drying hoop stress mechanics."
    },
    {
      title: "15 TPD Multi-Tab Interactive Financial Model",
      tag: "6-TAB DYNAMIC SPREADSHEET",
      file: "/data/FINANCIAL_MODEL_15TPD.xlsx",
      format: "XLSX",
      size: "18.1 kB",
      ref: "FNQ-15TPD-FIN-MOD",
      accent: "#F59E0B",
      desc: "Audited Excel model with dynamic formula-driven tabs: Macro Assumptions, Turnkey CapEx Schedule (₹135.0L), Itemized OpEx (₹6.34/kg), 5-Year Cash Flow Projections, Multi-Variable Sensitivity Matrix, and Breakeven Capacity."
    },
    {
      title: "Front-End Engineering Design (FEED) Report",
      tag: "10-PAGE ENGINEERING DOSSIER",
      file: "/pdf/FINNOAQ_15TPD_FEED_REPORT.pdf",
      format: "PDF",
      size: "1.3 MB",
      ref: "FNQ-FEED-REP-001",
      accent: "#94A3B8",
      desc: "First-principles engineering design covering Peleg hydration equations, Page drying kinetics, Aspen Plus V14 stream balances, ASME Section VIII vessel sizing, and balance-of-plant utility schedules."
    }
  ];

  return (
    <section id="vault" className="border-b border-[#1E2230] bg-[#090A0F] py-14">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col gap-2 mb-10 border-b border-[#1E2230] pb-6">
          <div className="flex items-center gap-2">
            <span className="font-mono text-xs font-bold text-[#10B981] tracking-widest uppercase">[06 // DOCUMENT VAULT]</span>
            <span className="h-1 w-1 rounded-full bg-[#10B981]"></span>
            <span className="font-mono text-xs text-[#64748B]">AUTHENTIC AUDITED DELIVERABLES</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold text-[#F3F4F6] tracking-tight">
            Institutional Engineering & Investor Publications
          </h2>
          <p className="text-sm text-[#94A3B8] max-w-3xl">
            Direct access to official PDF treatises, dynamic financial spreadsheets, and verified front-end engineering design packages.
          </p>
        </div>

        {/* 4-Card Publications Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {documents.map((doc, idx) => (
            <div
              key={idx}
              className="border border-[#1E2230] bg-[#11131A] rounded-sm p-6 flex flex-col justify-between shadow-xl hover:border-[#38BDF8]/50 transition-colors"
            >
              <div>
                <div className="flex items-center justify-between text-xs font-mono mb-2">
                  <span
                    className="px-2 py-0.5 rounded-sm border font-bold"
                    style={{ borderColor: doc.accent, color: doc.accent, backgroundColor: `${doc.accent}15` }}
                  >
                    {doc.tag}
                  </span>
                  <span className="text-[#64748B]">{doc.ref}</span>
                </div>

                <h3 className="text-lg font-bold text-[#F3F4F6] mt-1">
                  {doc.title}
                </h3>
                
                <p className="text-xs text-[#94A3B8] mt-2.5 leading-relaxed">
                  {doc.desc}
                </p>
              </div>

              <div className="pt-5 mt-4 border-t border-[#1E2230] flex items-center justify-between">
                <div className="font-mono text-[11px] text-[#64748B]">
                  <span>{doc.format}</span> &bull; <span>{doc.size}</span>
                </div>

                <a
                  href={doc.file}
                  download={doc.file.split('/').pop()}
                  className="inline-flex items-center gap-1.5 font-mono text-xs font-bold px-4 py-2 rounded-sm border transition-all"
                  style={{
                    borderColor: doc.accent,
                    color: doc.accent,
                    backgroundColor: `${doc.accent}10`
                  }}
                >
                  <Download className="w-3.5 h-3.5" />
                  <span>Download File</span>
                </a>
              </div>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}

