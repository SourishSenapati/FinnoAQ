import React, { useState } from 'react';
import { CORE_QUESTIONS, PROJECT_INFO } from '../data/micrositeData.js';

export default function Module1Hero() {
  const [selectedQuestion, setSelectedQuestion] = useState(0);

  return (
    <section id="hero" className="w-full bg-[#0A0B0D] border-b border-[#222630]">
      {/* 12-Column Swiss Grid Hero Layout */}
      <div className="max-w-[1440px] mx-auto grid grid-cols-1 lg:grid-cols-12 border-x border-[#222630]">
        
        {/* Left 7 Columns: Executive Eyebrow, Headline, Sub-copy & Monospace Download Strip */}
        <div className="lg:col-span-7 p-6 sm:p-8 lg:p-10 border-b lg:border-b-0 lg:border-r border-[#222630] flex flex-col justify-between">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-4">
              <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
                [00 // EXECUTIVE SUMMARY]
              </span>
              <span className="font-mono text-xs text-[#64748B] tracking-wider">
                15 TPD TURNKEY COMMERCIAL PLATFORM
              </span>
            </div>

            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-semibold tracking-tight text-[#F3F4F6] mb-4 leading-tight">
              Turnkey Pulse Tenderization & 15 TPD Commercial Plant Engineering
            </h1>

            <p className="text-[#9CA3AF] text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
              Unlocking <span className="text-[#F59E0B] font-mono font-medium">₹20.00/kg Mandi Arbitrage</span> on 
              Hard-to-Cook (HTC) imported African pulses via closed-loop S1-09 ultrasonic bio-chelation. 
              Reducing domestic cooking time from 8+ whistles (50–70 min) down to 2 whistles (7.0 min) at an audited 
              direct operating cost of <span className="text-[#F3F4F6] font-mono">₹6.34/kg</span> with 85% liquor recycling.
            </p>
          </div>

          {/* Unified 3-Button Monospace Architectural Download Strip */}
          <div className="pt-6 border-t border-[#222630]">
            <div className="text-xs font-mono text-[#64748B] mb-2 uppercase tracking-wider">
              [OFFICIAL REPOSITORY DELIVERABLES]
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
              <a 
                href="/finnoaq_commercial_investor_proposal.pdf" 
                download
                className="flex items-center justify-between px-3 py-2 bg-[#111317] hover:bg-[#171A21] border border-[#222630] hover:border-[#F59E0B] transition-colors rounded-sm text-left group"
              >
                <div>
                  <div className="font-mono text-xs text-[#F3F4F6] group-hover:text-[#F59E0B] transition-colors font-medium">
                    18-Pg Investor Proposal
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">PDF // ₹8.72 Cr EBITDA</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B]">↓</span>
              </a>

              <a 
                href="/finnoaq_dalopt_q1_master_treatise.pdf" 
                download
                className="flex items-center justify-between px-3 py-2 bg-[#111317] hover:bg-[#171A21] border border-[#222630] hover:border-[#F59E0B] transition-colors rounded-sm text-left group"
              >
                <div>
                  <div className="font-mono text-xs text-[#F3F4F6] group-hover:text-[#F59E0B] transition-colors font-medium">
                    27-Pg Q1 Monograph
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">PDF // Physics & Treatises</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B]">↓</span>
              </a>

              <a 
                href="/FINANCIAL_MODEL_15TPD.xlsx" 
                download
                className="flex items-center justify-between px-3 py-2 bg-[#111317] hover:bg-[#171A21] border border-[#222630] hover:border-[#F59E0B] transition-colors rounded-sm text-left group"
              >
                <div>
                  <div className="font-mono text-xs text-[#F3F4F6] group-hover:text-[#F59E0B] transition-colors font-medium">
                    15 TPD Excel Model
                  </div>
                  <div className="font-mono text-[11px] text-[#64748B]">XLSX // 5-Yr Pro-Forma</div>
                </div>
                <span className="font-mono text-xs text-[#64748B] group-hover:text-[#F59E0B]">↓</span>
              </a>
            </div>
          </div>
        </div>

        {/* Right 5 Columns: 2x2 High-Contrast KPI Matrix */}
        <div className="lg:col-span-5 grid grid-cols-2 bg-[#0A0B0D]">
          
          {/* KPI 1 */}
          <div className="p-6 border-b sm:border-r border-[#222630] bg-[#111317] flex flex-col justify-between">
            <span className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">
              DAILY THROUGHPUT
            </span>
            <div className="my-4">
              <div className="font-mono text-2xl sm:text-3xl font-semibold text-[#F3F4F6] tabular-nums">
                15,000
              </div>
              <div className="font-mono text-xs text-[#9CA3AF]">kg / day Raw Intake</div>
            </div>
            <div className="font-mono text-[11px] text-[#64748B]">
              Finished: 14,360 kg/d (97.37% Yield)
            </div>
          </div>

          {/* KPI 2 */}
          <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-col justify-between">
            <span className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">
              MANDI SPREAD ARBITRAGE
            </span>
            <div className="my-4">
              <div className="font-mono text-2xl sm:text-3xl font-semibold text-[#F59E0B] tabular-nums">
                ₹20.00
              </div>
              <div className="font-mono text-xs text-[#9CA3AF]">per kg Gross Value Pool</div>
            </div>
            <div className="font-mono text-[11px] text-[#F59E0B]">
              African ₹85.00 → Desi ₹105.00 Parity
            </div>
          </div>

          {/* KPI 3 */}
          <div className="p-6 sm:border-r border-b lg:border-b-0 border-[#222630] bg-[#111317] flex flex-col justify-between">
            <span className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">
              CAPEX & OPEX RATIO
            </span>
            <div className="my-4">
              <div className="font-mono text-2xl sm:text-3xl font-semibold text-[#F3F4F6] tabular-nums">
                ₹135.0L
              </div>
              <div className="font-mono text-xs text-[#9CA3AF]">CapEx // ₹6.34/kg OpEx</div>
            </div>
            <div className="font-mono text-[11px] text-[#10B981]">
              85% Liquor Recycle Active
            </div>
          </div>

          {/* KPI 4 */}
          <div className="p-6 bg-[#111317] flex flex-col justify-between">
            <span className="font-mono text-[11px] text-[#64748B] uppercase tracking-wider">
              RETURNS & PAYBACK
            </span>
            <div className="my-4">
              <div className="font-mono text-2xl sm:text-3xl font-semibold text-[#10B981] tabular-nums">
                78.4%
              </div>
              <div className="font-mono text-xs text-[#9CA3AF]">5-Year Audited IRR</div>
            </div>
            <div className="font-mono text-[11px] text-[#64748B]">
              Payback: 1.12 Yrs // ₹378.2L NPV
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
