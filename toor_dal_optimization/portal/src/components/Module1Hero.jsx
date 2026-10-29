import React, { useState } from 'react';
import { CORE_QUESTIONS } from '../data/micrositeData.js';

export default function Module1Hero() {
  const [selectedQuestion, setSelectedQuestion] = useState(0);
  const [activeHotspot, setActiveHotspot] = useState(null);

  const hotspots = [
    { id: 'tk101', tag: 'TK-101A/B', label: 'Ultrasonic Steeping Battery', top: '38%', left: '32%', spec: 'Twin 2,500L SS316L // 48°C // 40 kHz' },
    { id: 'sc101', tag: 'SC-101', label: 'High-Freq Dewatering Screen', top: '52%', left: '50%', spec: '12s Deluge Wash // 28.0% Exit Moisture' },
    { id: 'dr101', tag: 'DR-101A/B', label: 'Two-Stage Fluid Bed Dryer', top: '44%', left: '72%', spec: '195 kWth Duty // 20m Adiabatic Tempering' },
    { id: 'ev101', tag: 'EV-101', label: 'MVR ZLD Evaporator Skid', top: '65%', left: '84%', spec: '250 kg/h MVR Vapor Compressor // 45% Solids' }
  ];

  const scrollTo = (id) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section id="hero" className="w-full bg-[#090A0E] border-b border-[#1E2330] relative overflow-hidden scroll-mt-20">
      {/* Ambient Radial Illumination for Wealth/Prestige Atmosphere */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[1200px] h-[500px] bg-gradient-to-b from-[#F59E0B]/[0.07] via-transparent to-transparent blur-3xl pointer-events-none"></div>

      {/* 12-Column Swiss Grid Hero Layout */}
      <div className="max-w-[1440px] mx-auto grid grid-cols-1 lg:grid-cols-12 border-x border-[#1E2330]">
        
        {/* Left 7 Columns: Executive Eyebrow, Main Headline, Download Strip & Value Proposition */}
        <div className="lg:col-span-7 p-6 sm:p-10 lg:p-12 border-b lg:border-b-0 lg:border-r border-[#1E2330] flex flex-col justify-between">
          <div>
            {/* Prestige Architectural Eyebrow */}
            <div className="flex flex-wrap items-center gap-2.5 mb-5">
              <span className="px-3 py-1 bg-[#141720] text-[#94A3B8] border border-[#262C3D] font-mono text-xs rounded tracking-wider font-medium">
                [FNQ-PR-2026-COMM-001 // REV V11]
              </span>
              <span className="font-mono text-xs text-[#64748B] tracking-wider uppercase">
                15 TPD TURNKEY COMMERCIAL PLATFORM
              </span>
              <span className="font-mono text-[11px] px-2.5 py-0.5 bg-[#10B981]/10 text-[#10B981] border border-[#10B981]/30 rounded tracking-wide font-medium flex items-center space-x-1">
                <span className="w-1.5 h-1.5 rounded-full bg-[#10B981] inline-block animate-pulse"></span>
                <span>0.000000% CLOSURE ERROR</span>
              </span>
            </div>

            {/* High-Impact Headline */}
            <h1 className="text-3xl sm:text-5xl lg:text-[52px] font-semibold tracking-tight text-white mb-5 leading-[1.12]">
              Turnkey Pulse Tenderization & 15 TPD Commercial Plant Engineering
            </h1>

            {/* Engineering Sub-Copy */}
            <p className="text-[#94A3B8] text-base sm:text-lg leading-relaxed mb-8 max-w-2xl font-normal">
              Unlocking <span className="text-[#F59E0B] font-mono font-semibold">₹20.00/kg Mandi Arbitrage</span> on 
              Hard-to-Cook (HTC) imported African and Myanmar split pigeon peas via closed-loop S1-09 ultrasonic bio-chelation. 
              Reducing domestic cooking time from 8+ whistles (50–70 min) down to <span className="text-white font-mono font-semibold">2 whistles (7.0 min)</span> at an audited 
              direct operating cost of <span className="text-white font-mono font-semibold">₹6.34/kg</span> with 85% liquor recycling.
            </p>

            {/* Fast Quantitative Metrics Strip */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8 font-mono text-xs">
              <div className="p-3.5 bg-[#12141A] border border-[#222630] rounded hover:border-[#10B981]/40 transition-colors">
                <div className="text-[10px] text-[#64748B] uppercase tracking-wider">COOK TIME</div>
                <div className="text-lg font-bold text-[#10B981] my-0.5 tabular-nums">2 Whistles</div>
                <div className="text-[11px] text-[#94A3B8]">7.0 min (vs 8+ wh)</div>
              </div>
              <div className="p-3.5 bg-[#12141A] border border-[#222630] rounded hover:border-white/20 transition-colors">
                <div className="text-[10px] text-[#64748B] uppercase tracking-wider">DRY SOLIDS YIELD</div>
                <div className="text-lg font-bold text-white my-0.5 tabular-nums">97.37%</div>
                <div className="text-[11px] text-[#94A3B8]">14,360 kg/d finished</div>
              </div>
              <div className="p-3.5 bg-[#12141A] border border-[#222630] rounded hover:border-white/20 transition-colors">
                <div className="text-[10px] text-[#64748B] uppercase tracking-wider">DIRECT OPEX</div>
                <div className="text-lg font-bold text-white my-0.5 tabular-nums">₹6.34 / kg</div>
                <div className="text-[11px] text-[#10B981]">85% closed recycle</div>
              </div>
              <div className="p-3.5 bg-[#12141A] border border-[#222630] rounded hover:border-[#F59E0B]/40 transition-colors">
                <div className="text-[10px] text-[#64748B] uppercase tracking-wider">MILLER NET LIFT</div>
                <div className="text-lg font-bold text-[#F59E0B] my-0.5 tabular-nums">+₹8.00 / kg</div>
                <div className="text-[11px] text-[#F59E0B] font-semibold">+₹8,000 / MT profit</div>
              </div>
            </div>

            {/* Primary Action Button */}
            <div className="flex flex-wrap items-center gap-4 mb-8">
              <button
                onClick={() => scrollTo('scoping')}
                className="px-6 py-3.5 bg-gradient-to-r from-[#F59E0B] to-[#D97706] hover:from-[#FBBF24] hover:to-[#F59E0B] text-black font-bold text-sm tracking-wide uppercase rounded shadow-[0_0_20px_rgba(245,158,11,0.4)] hover:shadow-[0_0_30px_rgba(245,158,11,0.6)] transition-all transform hover:-translate-y-0.5 cursor-pointer font-mono"
              >
                Request 48-Hr Grain Trial →
              </button>
              <button
                onClick={() => scrollTo('solidworks-cad')}
                className="px-5 py-3.5 bg-[#141720] hover:bg-[#1C212E] text-white border border-[#262C3D] hover:border-[#F59E0B]/50 font-mono text-xs rounded transition-all cursor-pointer flex items-center space-x-2"
              >
                <span>Launch Interactive 3D CAD Studio</span>
                <span className="text-[#F59E0B]">↗</span>
              </button>
            </div>
          </div>

          {/* Unified 3-Button Monospace Architectural Download Strip with Real Working Files */}
          <div className="pt-6 border-t border-[#1E2330]">
            <div className="flex justify-between items-center mb-3">
              <span className="text-xs font-mono text-[#64748B] uppercase tracking-wider">
                OFFICIAL REPOSITORY DELIVERABLES & VERIFIED FINANCIAL MODELS
              </span>
              <span className="font-mono text-[11px] text-[#10B981] font-medium flex items-center space-x-1">
                <span>✓</span>
                <span>VERIFIED DIRECT DOWNLOADS (HTTP 200)</span>
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
              <a 
                href="/finnoaq_commercial_investor_proposal.pdf" 
                download="finnoaq_commercial_investor_proposal.pdf"
                className="flex items-center justify-between p-3.5 bg-[#12141A] hover:bg-[#181B24] border border-[#222630] hover:border-[#F59E0B] transition-all rounded group"
              >
                <div>
                  <div className="font-mono text-xs text-white group-hover:text-[#F59E0B] transition-colors font-medium">
                    Investor Proposal
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">PDF // 18-Pg // 420 KB</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B] font-bold">↓</span>
              </a>

              <a 
                href="/finnoaq_dalopt_q1_master_treatise.pdf" 
                download="finnoaq_dalopt_q1_master_treatise.pdf"
                className="flex items-center justify-between p-3.5 bg-[#12141A] hover:bg-[#181B24] border border-[#222630] hover:border-[#F59E0B] transition-all rounded group"
              >
                <div>
                  <div className="font-mono text-xs text-white group-hover:text-[#F59E0B] transition-colors font-medium">
                    Q1 Master Treatise
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">PDF // 27-Pg // 556 KB</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B] font-bold">↓</span>
              </a>

              <a 
                href="/FINANCIAL_MODEL_15TPD.xlsx" 
                download="FINANCIAL_MODEL_15TPD.xlsx"
                className="flex items-center justify-between p-3.5 bg-[#12141A] hover:bg-[#181B24] border border-[#222630] hover:border-[#F59E0B] transition-all rounded group"
              >
                <div>
                  <div className="font-mono text-xs text-white group-hover:text-[#F59E0B] transition-colors font-medium">
                    15 TPD Financial Model
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">XLSX // 6-Tab Pro-Forma</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B] font-bold">↓</span>
              </a>
            </div>
          </div>
        </div>

        {/* Right 5 Columns: Authentic Transparent 3D Plant Model Viewport with Interactive Telemetry Hotspots */}
        <div className="lg:col-span-5 bg-[#090A0E] flex flex-col justify-between border-t lg:border-t-0">
          
          {/* 3D Plant Assembly Viewport */}
          <div className="p-6 sm:p-8 relative bg-gradient-to-b from-[#12141A] to-[#0D0F14] border-b border-[#1E2330] flex-1 flex flex-col justify-center">
            <div className="flex justify-between items-center mb-3 font-mono text-xs text-[#64748B]">
              <span className="text-[#94A3B8]">SOLIDWORKS 2025 SP01.2 // PLANT-15T</span>
              <span className="text-[#F59E0B] font-medium">INTERACTIVE MEZZANINE (+4.2m FFL)</span>
            </div>

            {/* Seamless 3D Render Canvas with Radial Glow (NO WHITE BOXES) */}
            <div 
              className="relative border border-[#222630] rounded overflow-hidden p-4 min-h-[320px] flex items-center justify-center"
              style={{
                background: 'radial-gradient(circle at 50% 50%, rgba(245, 158, 11, 0.12) 0%, rgba(10, 11, 14, 0.98) 75%)'
              }}
            >
              <img
                src="/drawings/PLANT-15T_Joined_Iso_HumanView_transparent.png"
                alt="FinnoaQ 15 TPD Plant General Arrangement"
                className="w-full h-auto max-h-[300px] object-contain mx-auto filter drop-shadow-[0_15px_30px_rgba(0,0,0,0.8)] transition-transform duration-500 hover:scale-[1.02]"
                onError={(e) => {
                  e.target.src = '/drawings/PLANT-15T_Joined_Iso_HumanView.png';
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
                      className={`w-7 h-7 rounded-full flex items-center justify-center font-mono text-xs font-bold border transition-all cursor-pointer ${
                        isActive
                          ? 'bg-[#F59E0B] text-black border-[#F59E0B] scale-125 shadow-[0_0_15px_#F59E0B]'
                          : 'bg-[#12141A]/90 text-[#F59E0B] border-[#F59E0B] hover:scale-115 hover:shadow-[0_0_10px_#F59E0B]'
                      }`}
                    >
                      +
                    </button>

                    {/* Popover Card */}
                    {isActive && (
                      <div className="absolute left-1/2 -translate-x-1/2 bottom-full mb-3 w-64 p-3 bg-[#0D0F14]/95 backdrop-blur-md border border-[#F59E0B] rounded shadow-[0_10px_30px_rgba(0,0,0,0.9)] z-30 font-mono text-left">
                        <div className="text-[#F59E0B] font-bold text-xs flex items-center justify-between">
                          <span>{spot.tag}</span>
                          <span className="text-[10px] text-[#10B981]">● ACTIVE DCS</span>
                        </div>
                        <div className="text-white text-xs font-medium my-1">{spot.label}</div>
                        <div className="text-[#94A3B8] text-[11px] leading-tight">{spot.spec}</div>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <div className="flex justify-between items-center font-mono text-[11px] text-[#64748B] mt-3">
              <span>Hover or tap pins (+) to inspect major unit operations</span>
              <span className="text-[#94A3B8]">10.7m x 7.5m Industrial Footprint</span>
            </div>
          </div>

          {/* 2x2 High-Contrast Financial Yield Matrix */}
          <div className="grid grid-cols-2 bg-[#090A0E]">
            <div className="p-5 border-r border-b border-[#1E2330] bg-[#12141A]">
              <div className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">DAILY CAPACITY</div>
              <div className="font-mono text-2xl sm:text-3xl font-bold text-white tabular-nums my-1">15,000 kg</div>
              <div className="font-mono text-xs text-[#94A3B8]">Raw Intake Basis (15 TPD)</div>
            </div>
            <div className="p-5 border-b border-[#1E2330] bg-[#12141A]">
              <div className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">MANDI SPREAD</div>
              <div className="font-mono text-2xl sm:text-3xl font-bold text-[#F59E0B] tabular-nums my-1">₹20.00 / kg</div>
              <div className="font-mono text-xs text-[#F59E0B]">African ₹85 → Desi ₹105</div>
            </div>
            <div className="p-5 border-r border-[#1E2330] bg-[#12141A]">
              <div className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">TURNKEY CAPEX</div>
              <div className="font-mono text-2xl sm:text-3xl font-bold text-white tabular-nums my-1">₹135.0L</div>
              <div className="font-mono text-xs text-[#94A3B8]">Areas 100 to 900 Complete</div>
            </div>
            <div className="p-5 bg-[#12141A]">
              <div className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">PROJECT RETURNS</div>
              <div className="font-mono text-2xl sm:text-3xl font-bold text-[#10B981] tabular-nums my-1">78.4% IRR</div>
              <div className="font-mono text-xs text-[#10B981]">1.12-Yr Capital Payback</div>
            </div>
          </div>

        </div>

      </div>

      {/* Executive Investment Memo: 2-Column Master-Detail Accordion */}
      <div className="max-w-[1440px] mx-auto border-x border-[#1E2330] bg-[#090A0E]">
        <div className="p-5 sm:p-6 border-b border-[#1E2330] bg-[#12141A] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-3 py-1 bg-[#1A1F2C] text-[#94A3B8] border border-[#2E374D] font-mono text-xs rounded font-medium">
              [EXECUTIVE INVESTMENT BRIEFING]
            </span>
            <span className="text-xs sm:text-sm font-mono text-[#94A3B8]">
              The 6 Core Strategic & Investor Questions
            </span>
          </div>
          <span className="font-mono text-xs text-[#64748B]">
            Interactive Master-Detail Inspector
          </span>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 min-h-[400px]">
          {/* Left Column: 6 Question Selectors */}
          <div className="lg:col-span-5 border-b lg:border-b-0 lg:border-r border-[#1E2330] divide-y divide-[#1E2330]">
            {CORE_QUESTIONS.map((q, idx) => {
              const isSelected = selectedQuestion === idx;
              return (
                <button
                  key={q.num}
                  onClick={() => setSelectedQuestion(idx)}
                  className={`w-full text-left p-4 sm:p-5 transition-all cursor-pointer flex items-start justify-between ${
                    isSelected 
                      ? 'bg-[#181C26] border-l-4 border-[#F59E0B]' 
                      : 'bg-[#090A0E] hover:bg-[#12141A]'
                  }`}
                >
                  <div className="pr-4">
                    <div className="flex items-center space-x-2.5 mb-1.5">
                      <span className="font-mono text-xs text-[#F59E0B] font-bold">
                        {q.num}
                      </span>
                      <span className="font-mono text-[10px] px-2 py-0.5 bg-[#1A1F2C] text-[#94A3B8] border border-[#2E374D] rounded">
                        {q.status}
                      </span>
                    </div>
                    <div className={`text-sm sm:text-base font-medium ${isSelected ? 'text-white' : 'text-[#94A3B8]'}`}>
                      {q.title}
                    </div>
                  </div>
                  <span className={`font-mono text-sm pt-1 ${isSelected ? 'text-[#F59E0B] font-bold' : 'text-[#64748B]'}`}>
                    →
                  </span>
                </button>
              );
            })}
          </div>

          {/* Right Column: Full Evidence-Grounded Inspection Pane */}
          <div className="lg:col-span-7 p-6 sm:p-10 bg-[#12141A] flex flex-col justify-between">
            {CORE_QUESTIONS[selectedQuestion] && (
              <div>
                <div className="flex flex-wrap items-center justify-between gap-3 mb-6 pb-4 border-b border-[#222630]">
                  <div className="flex items-center space-x-3">
                    <span className="font-mono text-sm sm:text-base font-bold text-[#F59E0B]">
                      QUESTION {CORE_QUESTIONS[selectedQuestion].num}
                    </span>
                    <span className="text-[#64748B] font-mono text-sm">//</span>
                    <span className="font-mono text-xs sm:text-sm text-[#94A3B8]">
                      {CORE_QUESTIONS[selectedQuestion].title}
                    </span>
                  </div>
                  <span className="font-mono text-xs px-2.5 py-1 bg-[#1A1F2C] text-[#10B981] border border-[#2E374D] rounded font-semibold">
                    {CORE_QUESTIONS[selectedQuestion].status}
                  </span>
                </div>

                <div className="text-base sm:text-lg text-[#F3F4F6] leading-relaxed mb-8 font-normal">
                  {CORE_QUESTIONS[selectedQuestion].summary}
                </div>

                <div className="p-5 bg-[#090A0E] border border-[#222630] rounded">
                  <div className="font-mono text-xs text-[#64748B] uppercase tracking-wider mb-2 font-medium">
                    AUDITED ENGINEERING & EMPIRICAL BASIS
                  </div>
                  <div className="font-mono text-xs sm:text-sm text-[#94A3B8] leading-relaxed">
                    {CORE_QUESTIONS[selectedQuestion].basis}
                  </div>
                </div>
              </div>
            )}

            <div className="pt-6 mt-8 border-t border-[#222630] flex flex-wrap items-center justify-between gap-3 font-mono text-xs text-[#64748B]">
              <span>LEAD CHEMICAL & PROCESS ENGINEER: <strong className="text-[#94A3B8]">SOURISH SENAPATI</strong></span>
              <span className="text-[#94A3B8]">FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES LTD.</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
