import React, { useState } from 'react';
import { CORE_QUESTIONS, PROJECT_INFO } from '../data/micrositeData.js';

export default function Module1Hero() {
  const [selectedQuestion, setSelectedQuestion] = useState(0);
  const [activeHotspot, setActiveHotspot] = useState(null);

  const hotspots = [
    { id: 'tk101', tag: 'TK-101A/B', label: 'Ultrasonic Steeping Battery', top: '38%', left: '32%', spec: 'Twin 2,500L SS316L // 48°C // 40 kHz' },
    { id: 'sc101', tag: 'SC-101', label: 'High-Freq Dewatering Screen', top: '52%', left: '50%', spec: '12s Deluge Wash // 28.0% Exit Moisture' },
    { id: 'dr101', tag: 'DR-101A/B', label: 'Two-Stage Fluid Bed Dryer', top: '44%', left: '72%', spec: '195 kWth Duty // 20m Adiabatic Tempering' },
    { id: 'ev101', tag: 'EV-101', label: 'MVR ZLD Evaporator Skid', top: '65%', left: '84%', spec: '250 kg/h MVR Vapor Compressor // 45% Solids' }
  ];

  return (
    <section id="hero" className="w-full bg-[#0A0B0D] border-b border-[#222630]">
      {/* 12-Column Swiss Grid Hero Layout */}
      <div className="max-w-[1440px] mx-auto grid grid-cols-1 lg:grid-cols-12 border-x border-[#222630]">
        
        {/* Left 7 Columns: Executive Eyebrow, Main Headline, Download Strip & Value Proposition */}
        <div className="lg:col-span-7 p-6 sm:p-8 lg:p-10 border-b lg:border-b-0 lg:border-r border-[#222630] flex flex-col justify-between">
          <div>
            {/* Architectural Eyebrow */}
            <div className="flex flex-wrap items-center gap-2 mb-4">
              <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm tracking-wide">
                [FNQ-PR-2026-COMM-001 // REV V11]
              </span>
              <span className="font-mono text-xs text-[#64748B] tracking-wider">
                15 TPD TURNKEY COMMERCIAL PLATFORM
              </span>
              <span className="font-mono text-[11px] px-2 py-0.5 bg-[#10B981]/10 text-[#10B981] border border-[#10B981]/30 rounded-xs">
                ● 0.000000% CLOSURE
              </span>
            </div>

            {/* Impact Headline */}
            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight text-[#F3F4F6] mb-4 leading-tight">
              Turnkey Pulse Tenderization & 15 TPD Commercial Plant Engineering
            </h1>

            {/* Engineering Sub-Copy */}
            <p className="text-[#9CA3AF] text-sm sm:text-base leading-relaxed mb-6 max-w-2xl font-normal">
              Unlocking <span className="text-[#F59E0B] font-mono font-medium">₹20.00/kg Mandi Arbitrage</span> on 
              Hard-to-Cook (HTC) imported African and Myanmar split pigeon peas via closed-loop S1-09 ultrasonic bio-chelation. 
              Reducing domestic cooking time from 8+ whistles (50–70 min) down to 2 whistles (7.0 min) at an audited 
              direct operating cost of <span className="text-[#F3F4F6] font-mono">₹6.34/kg</span> with 85% liquor recycling.
            </p>

            {/* Fast Quantitative Metrics Strip */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-6 font-mono text-xs">
              <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm">
                <div className="text-[10px] text-[#64748B] uppercase">COOK TIME</div>
                <div className="text-base font-semibold text-[#10B981] my-0.5 tabular-nums">2 Whistles</div>
                <div className="text-[10px] text-[#9CA3AF]">7.0 min (vs 8+ wh)</div>
              </div>
              <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm">
                <div className="text-[10px] text-[#64748B]">DRY SOLIDS YIELD</div>
                <div className="text-base font-semibold text-[#F3F4F6] my-0.5 tabular-nums">97.37%</div>
                <div className="text-[10px] text-[#9CA3AF]">14,360 kg/d finished</div>
              </div>
              <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm">
                <div className="text-[10px] text-[#64748B]">DIRECT OPEX</div>
                <div className="text-base font-semibold text-[#F3F4F6] my-0.5 tabular-nums">₹6.34 / kg</div>
                <div className="text-[10px] text-[#10B981]">85% closed recycle</div>
              </div>
              <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm">
                <div className="text-[10px] text-[#64748B]">MILLER NET LIFT</div>
                <div className="text-base font-semibold text-[#F59E0B] my-0.5 tabular-nums">+₹8.00 / kg</div>
                <div className="text-[10px] text-[#F59E0B]">+₹8,000 / MT profit</div>
              </div>
            </div>
          </div>

          {/* Unified 3-Button Monospace Architectural Download Strip with Real Working Files */}
          <div className="pt-6 border-t border-[#222630]">
            <div className="flex justify-between items-center mb-2">
              <span className="text-xs font-mono text-[#64748B] uppercase tracking-wider">
                OFFICIAL REPOSITORY DELIVERABLES & MODELS
              </span>
              <span className="font-mono text-[10px] text-[#10B981]">
                ✓ VERIFIED DIRECT DOWNLOADS
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
              <a 
                href="/finnoaq_commercial_investor_proposal.pdf" 
                download="finnoaq_commercial_investor_proposal.pdf"
                className="flex items-center justify-between p-3 bg-[#111317] hover:bg-[#171A21] border border-[#222630] hover:border-[#F59E0B] transition-colors rounded-sm group"
              >
                <div>
                  <div className="font-mono text-xs text-[#F3F4F6] group-hover:text-[#F59E0B] transition-colors font-medium">
                    Investor Proposal
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">PDF // 18-Pg // 420 KB</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B]">↓</span>
              </a>

              <a 
                href="/finnoaq_dalopt_q1_master_treatise.pdf" 
                download="finnoaq_dalopt_q1_master_treatise.pdf"
                className="flex items-center justify-between p-3 bg-[#111317] hover:bg-[#171A21] border border-[#222630] hover:border-[#F59E0B] transition-colors rounded-sm group"
              >
                <div>
                  <div className="font-mono text-xs text-[#F3F4F6] group-hover:text-[#F59E0B] transition-colors font-medium">
                    Q1 Master Treatise
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">PDF // 27-Pg // 556 KB</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B]">↓</span>
              </a>

              <a 
                href="/FINANCIAL_MODEL_15TPD.xlsx" 
                download="FINANCIAL_MODEL_15TPD.xlsx"
                className="flex items-center justify-between p-3 bg-[#111317] hover:bg-[#171A21] border border-[#222630] hover:border-[#F59E0B] transition-colors rounded-sm group"
              >
                <div>
                  <div className="font-mono text-xs text-[#F3F4F6] group-hover:text-[#F59E0B] transition-colors font-medium">
                    15 TPD Financial Model
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">XLSX // 6-Tab Pro-Forma</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B]">↓</span>
              </a>
            </div>
          </div>
        </div>

        {/* Right 5 Columns: Authentic 3D Plant Model Viewport with Interactive Telemetry Hotspots */}
        <div className="lg:col-span-5 bg-[#0A0B0D] flex flex-col justify-between border-t lg:border-t-0">
          
          {/* 3D Plant Assembly Viewport */}
          <div className="p-6 relative bg-[#111317] border-b border-[#222630] flex-1 flex flex-col justify-center">
            <div className="flex justify-between items-center mb-2 font-mono text-[11px] text-[#64748B]">
              <span>SOLIDWORKS 2025 SP01.2 // PLANT-15T ASSEMBLY</span>
              <span className="text-[#F59E0B]">INTERACTIVE MEZZANINE (+4.2m FFL)</span>
            </div>

            {/* 3D Render Image with Hotspots */}
            <div className="relative border border-[#222630] rounded-sm overflow-hidden bg-[#0A0B0D] p-2">
              <img
                src="/drawings/PLANT-15T_Joined_Iso_HumanView.png"
                alt="FinnoaQ 15 TPD Plant General Arrangement"
                className="w-full h-auto max-h-[300px] object-contain mx-auto"
                onError={(e) => {
                  e.target.style.display = 'none';
                }}
              />

              {/* Interactive Telemetry Hotspot Pins */}
              {hotspots.map((spot) => {
                const isActive = activeHotspot === spot.id;
                return (
                  <div
                    key={spot.id}
                    style={{ top: spot.top, left: spot.left }}
                    className="absolute -translate-x-1/2 -translate-y-1/2 z-20"
                  >
                    <button
                      onClick={() => setActiveHotspot(isActive ? null : spot.id)}
                      onMouseEnter={() => setActiveHotspot(spot.id)}
                      className={`w-6 h-6 rounded-full flex items-center justify-center font-mono text-[10px] font-bold border transition-transform cursor-pointer ${
                        isActive
                          ? 'bg-[#F59E0B] text-black border-[#F59E0B] scale-125'
                          : 'bg-[#111317]/90 text-[#F59E0B] border-[#F59E0B] hover:scale-110'
                      }`}
                    >
                      +
                    </button>

                    {/* Popover Card */}
                    {isActive && (
                      <div className="absolute left-1/2 -translate-x-1/2 bottom-full mb-2 w-56 p-2.5 bg-[#0A0B0D] border border-[#F59E0B] rounded-sm shadow-2xl z-30 font-mono text-left">
                        <div className="text-[#F59E0B] font-bold text-xs">{spot.tag}</div>
                        <div className="text-[#F3F4F6] text-[11px] font-medium mb-1">{spot.label}</div>
                        <div className="text-[#9CA3AF] text-[10px]">{spot.spec}</div>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <div className="flex justify-between items-center font-mono text-[10px] text-[#64748B] mt-2">
              <span>Hover or tap pins (+) to inspect major unit operations</span>
              <span>10.7m x 7.5m Industrial Footprint</span>
            </div>
          </div>

          {/* 2x2 High-Contrast Financial Yield Matrix */}
          <div className="grid grid-cols-2 bg-[#0A0B0D]">
            <div className="p-4 border-r border-b border-[#222630] bg-[#111317]">
              <div className="font-mono text-[10px] text-[#64748B] uppercase">DAILY CAPACITY</div>
              <div className="font-mono text-2xl font-bold text-[#F3F4F6] tabular-nums my-0.5">15,000 kg</div>
              <div className="font-mono text-[10px] text-[#9CA3AF]">Raw Intake Basis (15 TPD)</div>
            </div>
            <div className="p-4 border-b border-[#222630] bg-[#111317]">
              <div className="font-mono text-[10px] text-[#64748B] uppercase">MANDI SPREAD</div>
              <div className="font-mono text-2xl font-bold text-[#F59E0B] tabular-nums my-0.5">₹20.00 / kg</div>
              <div className="font-mono text-[10px] text-[#F59E0B]">African ₹85 → Desi ₹105</div>
            </div>
            <div className="p-4 border-r border-[#222630] bg-[#111317]">
              <div className="font-mono text-[10px] text-[#64748B] uppercase">TURNKEY CAPEX</div>
              <div className="font-mono text-2xl font-bold text-[#F3F4F6] tabular-nums my-0.5">₹135.0L</div>
              <div className="font-mono text-[10px] text-[#9CA3AF]">Areas 100 to 900 Complete</div>
            </div>
            <div className="p-4 bg-[#111317]">
              <div className="font-mono text-[10px] text-[#64748B] uppercase">PROJECT RETURNS</div>
              <div className="font-mono text-2xl font-bold text-[#10B981] tabular-nums my-0.5">78.4% IRR</div>
              <div className="font-mono text-[10px] text-[#10B981]">1.12-Yr Capital Payback</div>
            </div>
          </div>

        </div>

      </div>

      {/* Executive Investment Memo: 2-Column Master-Detail Accordion */}
      <div className="max-w-[1440px] mx-auto border-x border-[#222630] bg-[#0A0B0D]">
        <div className="p-4 sm:p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [EXECUTIVE INVESTMENT BRIEFING]
            </span>
            <span className="text-xs font-mono text-[#9CA3AF]">
              The 6 Core Strategic & Investor Questions
            </span>
          </div>
          <span className="font-mono text-[11px] text-[#64748B]">
            Interactive Master-Detail Inspector
          </span>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 min-h-[380px]">
          {/* Left Column: 6 Question Selectors */}
          <div className="lg:col-span-5 border-b lg:border-b-0 lg:border-r border-[#222630] divide-y divide-[#222630]">
            {CORE_QUESTIONS.map((q, idx) => {
              const isSelected = selectedQuestion === idx;
              return (
                <button
                  key={q.num}
                  onClick={() => setSelectedQuestion(idx)}
                  className={`w-full text-left p-4 sm:p-5 transition-colors cursor-pointer flex items-start justify-between ${
                    isSelected 
                      ? 'bg-[#171A21] border-l-2 border-[#F59E0B]' 
                      : 'bg-[#0A0B0D] hover:bg-[#111317]'
                  }`}
                >
                  <div className="pr-4">
                    <div className="flex items-center space-x-2 mb-1">
                      <span className="font-mono text-xs text-[#F59E0B] font-semibold">
                        {q.num}
                      </span>
                      <span className="font-mono text-[10px] px-1.5 py-0.2 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] rounded-sm">
                        {q.status}
                      </span>
                    </div>
                    <div className={`text-xs sm:text-sm font-medium ${isSelected ? 'text-[#F3F4F6]' : 'text-[#9CA3AF]'}`}>
                      {q.title}
                    </div>
                  </div>
                  <span className={`font-mono text-xs ${isSelected ? 'text-[#F59E0B]' : 'text-[#64748B]'}`}>
                    →
                  </span>
                </button>
              );
            })}
          </div>

          {/* Right Column: Full Evidence-Grounded Inspection Pane */}
          <div className="lg:col-span-7 p-6 sm:p-8 bg-[#111317] flex flex-col justify-between">
            {CORE_QUESTIONS[selectedQuestion] && (
              <div>
                <div className="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-[#222630]">
                  <div className="flex items-center space-x-2">
                    <span className="font-mono text-sm font-semibold text-[#F59E0B]">
                      QUESTION {CORE_QUESTIONS[selectedQuestion].num}
                    </span>
                    <span className="text-[#64748B] font-mono text-xs">//</span>
                    <span className="font-mono text-xs text-[#9CA3AF]">
                      {CORE_QUESTIONS[selectedQuestion].title}
                    </span>
                  </div>
                  <span className="font-mono text-xs px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm">
                    {CORE_QUESTIONS[selectedQuestion].status}
                  </span>
                </div>

                <div className="text-sm sm:text-base text-[#F3F4F6] leading-relaxed mb-6 font-normal">
                  {CORE_QUESTIONS[selectedQuestion].summary}
                </div>

                <div className="p-4 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                  <div className="font-mono text-[11px] text-[#64748B] uppercase mb-1">
                    AUDITED ENGINEERING & EMPIRICAL BASIS
                  </div>
                  <div className="font-mono text-xs text-[#9CA3AF]">
                    {CORE_QUESTIONS[selectedQuestion].basis}
                  </div>
                </div>
              </div>
            )}

            <div className="pt-6 mt-6 border-t border-[#222630] flex flex-wrap items-center justify-between gap-2 font-mono text-xs text-[#64748B]">
              <span>LEAD CHEMICAL ENGINEER: SOURISH SENAPATI</span>
              <span>FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
