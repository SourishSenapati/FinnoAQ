import React from 'react';

export default function Footer() {
  return (
    <footer className="w-full bg-[#0C0E12] border-t border-[#1E232E] py-10 px-4 sm:px-6">
      <div className="max-w-[1440px] mx-auto space-y-6">
        
        {/* Top Line: Ref & Organization */}
        <div className="flex flex-wrap items-center justify-between gap-4 font-mono text-xs border-b border-[#1E232E] pb-6">
          <div className="flex items-center space-x-3">
            <span className="px-2 py-0.5 bg-[#151821] text-[#94A3B8] border border-[#232836] rounded-xs font-semibold">
              FNQ-PR-2026-COMM-001
            </span>
            <span className="text-[#E6E8EC] font-medium">
              FinnoaQ Agro-Industrial Technologies Ltd.
            </span>
          </div>
          <div className="text-[#5E6573]">
            Turnkey Commercial Model & Q1 Scientific Master Baseline // Rev V11
          </div>
        </div>

        {/* Middle Line: Engineering Attribution & Governing Codes */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 font-mono text-xs text-[#8E95A2]">
          <div>
            <div className="text-[10px] text-[#5E6573] uppercase mb-1">
              LEAD CHEMICAL & PROCESS ENGINEER
            </div>
            <div className="text-[#E6E8EC] font-medium">Sourish Senapati</div>
            <div className="text-[11px] text-[#5E6573]">FinnoaQ Agro-Industrial Technologies Ltd.</div>
          </div>

          <div>
            <div className="text-[10px] text-[#5E6573] uppercase mb-1">
              TECHNICAL ADVISORY & OVERSIGHT
            </div>
            <div className="text-[#E6E8EC] font-medium">Process Engineering Board</div>
            <div className="text-[11px] text-[#5E6573]">Industrial Advisory & Food Science Panel</div>
          </div>

          <div>
            <div className="text-[10px] text-[#5E6573] uppercase mb-1">
              GOVERNING STANDARDS & COMPLIANCE
            </div>
            <div className="text-[#E6E8EC] font-medium">ASME Sec VIII Div 1 / IS 2825 / NFPA 68</div>
            <div className="text-[11px] text-[#5E6573]">FSSAI Cat 06.0 & 14.1.4 / Codex CXS 171-1989 / ISO 11136:2014</div>
          </div>
        </div>

        {/* Bottom Line: Copyright & Operational Notice */}
        <div className="pt-6 border-t border-[#1E232E] flex flex-wrap items-center justify-between gap-2 font-mono text-[11px] text-[#5E6573]">
          <span>
            © 2026 FinnoaQ Agro-Industrial Technologies Ltd. All Rights Reserved. Commercial IP & Patent Pending.
          </span>
          <span className="text-[#10B981]">
            Deterministic Aspen Plus V14 ELECNRTL & Continuum Multiphysics Converged (0.000000% Closure)
          </span>
        </div>

      </div>
    </footer>
  );
}
