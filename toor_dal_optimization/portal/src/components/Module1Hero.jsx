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
    <section id="hero" className="w-full bg-[#0C0E12] border-b border-[#1E232E] relative overflow-hidden scroll-mt-20">
      
      {/* 12-Column Swiss Grid Hero Layout */}
      <div className="max-w-[1440px] mx-auto grid grid-cols-1 lg:grid-cols-12 border-x border-[#1E232E]">
        
        {/* Left 7 Columns: Architectural Eyebrow, Main Headline, Download Strip & Value Proposition */}
        <div className="lg:col-span-7 p-6 sm:p-10 lg:p-12 border-b lg:border-b-0 lg:border-r border-[#1E232E] flex flex-col justify-between">
          <div>
            {/* Engineering Eyebrow */}
            <div className="flex flex-wrap items-center gap-2.5 mb-5">
              <span className="px-2.5 py-1 bg-[#151821] text-[#94A3B8] border border-[#232836] font-mono text-xs rounded-xs tracking-wider font-medium">
                [FNQ-PR-2026-COMM-001 // REV V11]
              </span>
              <span className="font-mono text-xs text-[#64748B] tracking-wider uppercase">
                15 TPD COMMERCIAL PULSE PLATFORM
              </span>
              <span className="font-mono text-[11px] px-2 py-0.5 bg-[#10B981]/10 text-[#10B981] border border-[#10B981]/30 rounded-xs tracking-wide font-medium flex items-center space-x-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-[#10B981] inline-block"></span>
                <span>0.000000% CLOSURE ERROR</span>
              </span>
            </div>

            {/* Factual Technical Headline */}
            <h1 className="text-3xl sm:text-4xl lg:text-[44px] font-semibold tracking-tight text-[#E6E8EC] mb-5 leading-[1.18]">
              Turnkey Pulse Tenderization & 15 TPD Commercial Plant Engineering
            </h1>

            {/* Direct Engineering Summary */}
            <p className="text-[#8E95A2] text-sm sm:text-base leading-relaxed mb-8 max-w-2xl font-normal">
              Industrial bio-chelation conditioning for imported Hard-to-Cook (HTC) African and Myanmar split pigeon peas. 
              Captures the <span className="text-[#D97706] font-mono font-medium">₹20.00/kg Mandi price differential</span> by 
              reducing domestic cooking time from 8+ whistles (50–70 min) down to <span className="text-[#E6E8EC] font-mono font-medium">2 whistles (7.0 min)</span> at an audited 
              direct operating cost of <span className="text-[#E6E8EC] font-mono font-medium">₹6.34/kg</span> with 85% steep liquor recycling.
            </p>

            {/* Quantitative Baseline Metrics */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 mb-8 font-mono text-xs">
              <div className="p-3 bg-[#13151B] border border-[#1E232E] rounded-xs">
                <div className="text-[10px] text-[#5E6573] uppercase tracking-wider">COOK TIME</div>
                <div className="text-base font-bold text-[#10B981] my-0.5 tabular-nums">2 Whistles</div>
                <div className="text-[11px] text-[#8E95A2]">7.0 min (vs 8+ wh)</div>
              </div>
              <div className="p-3 bg-[#13151B] border border-[#1E232E] rounded-xs">
                <div className="text-[10px] text-[#5E6573] uppercase tracking-wider">DRY SOLIDS YIELD</div>
                <div className="text-base font-bold text-[#E6E8EC] my-0.5 tabular-nums">97.37%</div>
                <div className="text-[11px] text-[#8E95A2]">14,360 kg/d finished</div>
              </div>
              <div className="p-3 bg-[#13151B] border border-[#1E232E] rounded-xs">
                <div className="text-[10px] text-[#5E6573] uppercase tracking-wider">DIRECT OPEX</div>
                <div className="text-base font-bold text-[#E6E8EC] my-0.5 tabular-nums">₹6.34 / kg</div>
                <div className="text-[11px] text-[#10B981]">85% closed recycle</div>
              </div>
              <div className="p-3 bg-[#13151B] border border-[#1E232E] rounded-xs">
                <div className="text-[10px] text-[#5E6573] uppercase tracking-wider">MILLER NET LIFT</div>
                <div className="text-base font-bold text-[#D97706] my-0.5 tabular-nums">+₹8.00 / kg</div>
                <div className="text-[11px] text-[#D97706]">+₹8,000 / MT profit</div>
              </div>
            </div>

            {/* Engineering Action Buttons */}
            <div className="flex flex-wrap items-center gap-3.5 mb-8">
              <button
                onClick={() => scrollTo('scoping')}
                className="px-5 py-2.5 bg-[#D97706] hover:bg-[#B45309] text-black font-semibold text-xs tracking-wider uppercase rounded-xs transition-colors cursor-pointer font-mono"
              >
                Request 48-Hr Grain Trial →
              </button>
              <button
                onClick={() => scrollTo('solidworks-cad')}
                className="px-4 py-2.5 bg-[#151821] hover:bg-[#1E222D] text-[#D4D4D8] border border-[#262C3A] hover:border-[#3D4559] font-mono text-xs rounded-xs transition-colors cursor-pointer flex items-center space-x-2"
              >
                <span>Interactive 3D CAD Studio</span>
                <span className="text-[#D97706]">↗</span>
              </button>
            </div>
          </div>

          {/* Repository Deliverables Strip */}
          <div className="pt-5 border-t border-[#1E232E]">
            <div className="flex justify-between items-center mb-2.5">
              <span className="text-xs font-mono text-[#5E6573] uppercase tracking-wider">
                ENGINEERING DELIVERABLES & FINANCIAL MODELS
              </span>
              <span className="font-mono text-[11px] text-[#10B981] font-medium flex items-center space-x-1">
                <span>✓</span>
                <span>DIRECT DOWNLOADS (HTTP 200)</span>
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
              <a 
                href="/finnoaq_commercial_investor_proposal.pdf" 
                download="finnoaq_commercial_investor_proposal.pdf"
                className="flex items-center justify-between p-3 bg-[#13151B] hover:bg-[#171B24] border border-[#1E232E] hover:border-[#D97706] transition-colors rounded-xs group"
              >
                <div>
                  <div className="font-mono text-xs text-[#E6E8EC] group-hover:text-[#D97706] transition-colors font-medium">
                    Investor Proposal
                  </div>
                  <div className="font-mono text-[10px] text-[#5E6573]">PDF // 18-Pg // 420 KB</div>
                </div>
                <span className="font-mono text-xs text-[#5E6573] group-hover:text-[#D97706]">↓</span>
              </a>

              <a 
                href="/finnoaq_dalopt_q1_master_treatise.pdf" 
                download="finnoaq_dalopt_q1_master_treatise.pdf"
                className="flex items-center justify-between p-3 bg-[#13151B] hover:bg-[#171B24] border border-[#1E232E] hover:border-[#D97706] transition-colors rounded-xs group"
              >
                <div>
                  <div className="font-mono text-xs text-[#E6E8EC] group-hover:text-[#D97706] transition-colors font-medium">
                    Q1 Master Treatise
                  </div>
                  <div className="font-mono text-[10px] text-[#5E6573]">PDF // 27-Pg // 556 KB</div>
                </div>
                <span className="font-mono text-xs text-[#5E6573] group-hover:text-[#D97706]">↓</span>
              </a>

              <a 
                href="/FINANCIAL_MODEL_15TPD.xlsx" 
                download="FINANCIAL_MODEL_15TPD.xlsx"
                className="flex items-center justify-between p-3 bg-[#13151B] hover:bg-[#171B24] border border-[#1E232E] hover:border-[#D97706] transition-colors rounded-xs group"
              >
                <div>
                  <div className="font-mono text-xs text-[#E6E8EC] group-hover:text-[#D97706] transition-colors font-medium">
                    15 TPD Financial Model
                  </div>
                  <div className="font-mono text-[10px] text-[#5E6573]">XLSX // 6-Tab Pro-Forma</div>
                </div>
                <span className="font-mono text-xs text-[#5E6573] group-hover:text-[#D97706]">↓</span>
              </a>
            </div>
          </div>
        </div>

        {/* Right 5 Columns: Transparent 3D Plant Model Viewport with Direct Telemetry Hotspots */}
        <div className="lg:col-span-5 bg-[#0C0E12] flex flex-col justify-between border-t lg:border-t-0">
          
          {/* 3D Plant Assembly Viewport */}
          <div className="p-6 sm:p-8 relative bg-[#111319] border-b border-[#1E232E] flex-1 flex flex-col justify-center">
            <div className="flex justify-between items-center mb-3 font-mono text-xs text-[#5E6573]">
              <span className="text-[#8E95A2]">SOLIDWORKS 2025 SP01.2 // PLANT-15T</span>
              <span className="text-[#D97706] font-medium">MEZZANINE (+4.2m FFL)</span>
            </div>

            {/* Alpha-Channel 3D Render Canvas */}
            <div className="relative border border-[#1E232E] rounded-xs overflow-hidden p-4 min-h-[300px] flex items-center justify-center bg-[#0C0E12]">
              <img
                src="/drawings/PLANT-15T_Joined_Iso_HumanView_transparent.png"
                alt="FinnoaQ 15 TPD Plant General Arrangement"
                className="w-full h-auto max-h-[290px] object-contain mx-auto"
                onError={(e) => {
                  e.target.src = '/drawings/PLANT-15T_Joined_Iso_HumanView.png';
                }}
              />

              {/* Hotspot Pins */}
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
                      className={`w-6 h-6 rounded-full flex items-center justify-center font-mono text-[10px] font-bold border transition-all cursor-pointer ${
                        isActive
                          ? 'bg-[#D97706] text-black border-[#D97706] scale-110'
                          : 'bg-[#151821] text-[#D97706] border-[#D97706]/70 hover:scale-105'
                      }`}
                    >
                      +
                    </button>

                    {/* Popover Card */}
                    {isActive && (
                      <div className="absolute left-1/2 -translate-x-1/2 bottom-full mb-2.5 w-60 p-3 bg-[#13151B] border border-[#D97706] rounded-xs shadow-xl z-30 font-mono text-left">
                        <div className="text-[#D97706] font-bold text-xs flex items-center justify-between">
                          <span>{spot.tag}</span>
                          <span className="text-[10px] text-[#10B981]">DCS LINKED</span>
                        </div>
                        <div className="text-[#E6E8EC] text-xs font-medium my-1">{spot.label}</div>
                        <div className="text-[#8E95A2] text-[11px] leading-tight">{spot.spec}</div>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <div className="flex justify-between items-center font-mono text-[10px] text-[#5E6573] mt-3">
              <span>Hover or tap pins (+) to inspect unit operations</span>
              <span className="text-[#8E95A2]">10.7m x 7.5m Envelope</span>
            </div>
          </div>

          {/* 2x2 Financial Yield Matrix */}
          <div className="grid grid-cols-2 bg-[#0C0E12]">
            <div className="p-4 sm:p-5 border-r border-b border-[#1E232E] bg-[#111319]">
              <div className="font-mono text-[10px] text-[#5E6573] uppercase tracking-wider">DAILY CAPACITY</div>
              <div className="font-mono text-2xl font-bold text-[#E6E8EC] tabular-nums my-1">15,000 kg</div>
              <div className="font-mono text-xs text-[#8E95A2]">Raw Intake Basis (15 TPD)</div>
            </div>
            <div className="p-4 sm:p-5 border-b border-[#1E232E] bg-[#111319]">
              <div className="font-mono text-[10px] text-[#5E6573] uppercase tracking-wider">MANDI SPREAD</div>
              <div className="font-mono text-2xl font-bold text-[#D97706] tabular-nums my-1">₹20.00 / kg</div>
              <div className="font-mono text-xs text-[#D97706]">African ₹85 → Desi ₹105</div>
            </div>
            <div className="p-4 sm:p-5 border-r border-[#1E232E] bg-[#111319]">
              <div className="font-mono text-[10px] text-[#5E6573] uppercase tracking-wider">TURNKEY CAPEX</div>
              <div className="font-mono text-2xl font-bold text-[#E6E8EC] tabular-nums my-1">₹135.0L</div>
              <div className="font-mono text-xs text-[#8E95A2]">Areas 100 to 900 Complete</div>
            </div>
            <div className="p-4 sm:p-5 bg-[#111319]">
              <div className="font-mono text-[10px] text-[#5E6573] uppercase tracking-wider">PROJECT RETURNS</div>
              <div className="font-mono text-2xl font-bold text-[#10B981] tabular-nums my-1">78.4% IRR</div>
              <div className="font-mono text-xs text-[#10B981]">1.12-Yr Capital Payback</div>
            </div>
          </div>

        </div>

      </div>

      {/* Executive Technical Briefing: 2-Column Master-Detail Layout */}
      <div className="max-w-[1440px] mx-auto border-x border-[#1E232E] bg-[#0C0E12]">
        <div className="p-4 sm:p-5 border-b border-[#1E232E] bg-[#111319] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-1 bg-[#151821] text-[#94A3B8] border border-[#232836] font-mono text-xs rounded-xs font-medium">
              [COMMERCIAL & TECHNICAL EVALUATION]
            </span>
            <span className="text-xs sm:text-sm font-mono text-[#8E95A2]">
              6 Core Engineering & Commercial Clarifications
            </span>
          </div>
          <span className="font-mono text-xs text-[#5E6573]">
            Master-Detail Inspector
          </span>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 min-h-[380px]">
          {/* Left Column: Question Selectors */}
          <div className="lg:col-span-5 border-b lg:border-b-0 lg:border-r border-[#1E232E] divide-y divide-[#1E232E]">
            {CORE_QUESTIONS.map((q, idx) => {
              const isSelected = selectedQuestion === idx;
              return (
                <button
                  key={q.num}
                  onClick={() => setSelectedQuestion(idx)}
                  className={`w-full text-left p-4 sm:p-4.5 transition-colors cursor-pointer flex items-start justify-between ${
                    isSelected 
                      ? 'bg-[#151821] border-l-2 border-[#D97706]' 
                      : 'bg-[#0C0E12] hover:bg-[#111319]'
                  }`}
                >
                  <div className="pr-4">
                    <div className="flex items-center space-x-2.5 mb-1">
                      <span className="font-mono text-xs text-[#D97706] font-semibold">
                        {q.num}
                      </span>
                      <span className="font-mono text-[10px] px-1.5 py-0.2 bg-[#171B24] text-[#94A3B8] border border-[#232836] rounded-xs">
                        {q.status}
                      </span>
                    </div>
                    <div className={`text-xs sm:text-sm font-medium ${isSelected ? 'text-[#E6E8EC]' : 'text-[#8E95A2]'}`}>
                      {q.title}
                    </div>
                  </div>
                  <span className={`font-mono text-sm pt-0.5 ${isSelected ? 'text-[#D97706] font-bold' : 'text-[#5E6573]'}`}>
                    →
                  </span>
                </button>
              );
            })}
          </div>

          {/* Right Column: Evidence & Technical Basis */}
          <div className="lg:col-span-7 p-6 sm:p-8 bg-[#111319] flex flex-col justify-between">
            {CORE_QUESTIONS[selectedQuestion] && (
              <div>
                <div className="flex flex-wrap items-center justify-between gap-3 mb-5 pb-3 border-b border-[#1E232E]">
                  <div className="flex items-center space-x-2.5">
                    <span className="font-mono text-sm font-semibold text-[#D97706]">
                      SECTION {CORE_QUESTIONS[selectedQuestion].num}
                    </span>
                    <span className="text-[#5E6573] font-mono text-xs">//</span>
                    <span className="font-mono text-xs text-[#8E95A2]">
                      {CORE_QUESTIONS[selectedQuestion].title}
                    </span>
                  </div>
                  <span className="font-mono text-xs px-2 py-0.5 bg-[#151821] text-[#10B981] border border-[#232836] rounded-xs font-medium">
                    {CORE_QUESTIONS[selectedQuestion].status}
                  </span>
                </div>

                <div className="text-sm sm:text-base text-[#D4D4D8] leading-relaxed mb-6 font-normal">
                  {CORE_QUESTIONS[selectedQuestion].summary}
                </div>

                <div className="p-4 bg-[#0C0E12] border border-[#1E232E] rounded-xs">
                  <div className="font-mono text-xs text-[#5E6573] uppercase tracking-wider mb-1.5 font-medium">
                    TECHNICAL & EMPIRICAL BASIS
                  </div>
                  <div className="font-mono text-xs text-[#8E95A2] leading-relaxed">
                    {CORE_QUESTIONS[selectedQuestion].basis}
                  </div>
                </div>
              </div>
            )}

            <div className="pt-5 mt-6 border-t border-[#1E232E] flex flex-wrap items-center justify-between gap-3 font-mono text-xs text-[#5E6573]">
              <span>LEAD CHEMICAL & PROCESS ENGINEER: <strong className="text-[#8E95A2]">SOURISH SENAPATI</strong></span>
              <span className="text-[#8E95A2]">FINNOAQ AGRO-INDUSTRIAL TECHNOLOGIES LTD.</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
