import React from 'react';
import { Shield, FileCheck, Layers } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="border-t border-[#1E2230] bg-[#050811] py-12 text-[#64748B] font-mono text-xs">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 flex flex-col gap-8">
        
        {/* Top Row: Engineering Attributions & Credentials */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-8 pb-8 border-b border-[#1E2230]">
          
          <div className="md:col-span-6 flex flex-col gap-2">
            <div className="flex items-center gap-2 text-[#F3F4F6] font-bold text-sm tracking-wide">
              <span>FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES LTD.</span>
            </div>
            <p className="text-[#94A3B8] text-xs leading-relaxed max-w-lg font-sans">
              Commercial platform for adaptive conditioning and bioprocess tenderization of hard-to-cook imported pulses. Turnkey 15 MT/day conceptual plant engineering with 85% closed-loop bleed-and-feed liquor recycling.
            </p>
            <div className="text-[11px] text-[#38BDF8] pt-1">
              Project Reference: FNQ-PR-2026-001 | Revision: V12 Production Baseline
            </div>
          </div>

          <div className="md:col-span-3 flex flex-col gap-1.5">
            <span className="text-[#F3F4F6] font-bold text-xs">LEAD PROCESS ENGINEER</span>
            <span className="text-[#CBD5E1]">Sourish Senapati</span>
            <span className="text-[11px] text-[#64748B]">FinnoaQ Agro-Industrial Technologies Ltd.</span>
            <span className="text-[11px] text-[#64748B]">Process Engineering & Modeling</span>
          </div>

          <div className="md:col-span-3 flex flex-col gap-1.5">
            <span className="text-[#F3F4F6] font-bold text-xs">GOVERNING STANDARDS</span>
            <span className="text-[#CBD5E1]">ASME Sec VIII Div 1 & NFPA 68</span>
            <span className="text-[#CBD5E1]">FSSAI Section 22 / Cat 06.0</span>
            <span className="text-[#CBD5E1]">Codex Stan 171-1989 & ISO 11136:2014</span>
          </div>

        </div>

        {/* Bottom Row: Legal & Non-Fabrication Guarantee */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px]">
          <p>
            © 2026 FinnoaQ Agro-Industrial Technologies Ltd. All rights reserved. Zero-fabrication scientific and financial integrity standard enforced.
          </p>
          <div className="flex items-center gap-4 text-[#94A3B8]">
            <a href="#architecture" className="hover:text-[#F3F4F6] transition-colors">[Architecture]</a>
            <a href="#pipeline" className="hover:text-[#F3F4F6] transition-colors">[Pipeline]</a>
            <a href="#comparator" className="hover:text-[#F3F4F6] transition-colors">[Comparator]</a>
            <a href="#benchmarks" className="hover:text-[#F3F4F6] transition-colors">[Benchmarks]</a>
            <a href="#vault" className="hover:text-[#F3F4F6] transition-colors">[Publications]</a>
          </div>
        </div>

      </div>
    </footer>
  );
}
