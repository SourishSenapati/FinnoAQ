import React, { useState } from 'react';
import { SCALEUP_PHASES } from '../data/micrositeData.js';

export default function Module5Roadmap() {
  const [selectedPhaseIdx, setSelectedPhaseIdx] = useState(1); // Default to Phase 1 (Active Target)

  const selectedPhase = SCALEUP_PHASES[selectedPhaseIdx];

  return (
    <section id="roadmap" className="w-full bg-[#0A0B0D] border-b border-[#222630]">
      <div className="max-w-[1440px] mx-auto border-x border-[#222630]">
        
        {/* Module Header */}
        <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [04 // SCALE-UP ROADMAP & DECISION GATES]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#F3F4F6]">
              Single Consolidated 5-Phase Scale-Up Roadmap
            </h2>
          </div>
          <span className="font-mono text-xs px-2 py-0.5 bg-[#1E222A] text-[#F59E0B] border border-[#2E3440] rounded-sm">
            ACTIVE TARGET: PHASE 1 BENCH SEED (₹33.0L)
          </span>
        </div>

        {/* 1. Horizontal Interactive Phase Selector Bar */}
        <div className="p-6 bg-[#0A0B0D] border-b border-[#222630]">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
            {SCALEUP_PHASES.map((p, idx) => {
              const isSelected = selectedPhaseIdx === idx;
              const isPhase0 = idx === 0;
              const isPhase1 = idx === 1;

              return (
                <button
                  key={p.phase}
                  onClick={() => setSelectedPhaseIdx(idx)}
                  className={`p-4 text-left border rounded-sm transition-all cursor-pointer relative ${
                    isSelected
                      ? 'bg-[#171A21] border-[#F59E0B] shadow-md'
                      : 'bg-[#111317] border-[#222630] hover:border-[#64748B]'
                  }`}
                >
                  <div className="flex justify-between items-center mb-1">
                    <span className={`font-mono text-xs font-bold ${
                      isPhase1 
                        ? 'text-[#F59E0B]' 
                        : isPhase0 
                        ? 'text-[#10B981]' 
                        : 'text-[#F3F4F6]'
                    }`}>
                      {p.phase}
                    </span>
                    <span className="font-mono text-[10px] text-[#64748B]">
                      ₹{p.budgetLakhs.toFixed(1)}L
                    </span>
                  </div>

                  <div className="text-xs font-medium text-[#F3F4F6] line-clamp-1 mb-1">
                    {p.name}
                  </div>

                  <div className="font-mono text-[11px] text-[#9CA3AF] mb-3 truncate">
                    {p.timeline}
                  </div>

                  <div className="pt-2 border-t border-[#222630] flex items-center justify-between">
                    <span className={`text-[10px] font-mono px-1.5 py-0.2 rounded-xs border ${
                      isPhase0 
                        ? 'bg-[#10B981]/10 text-[#10B981] border-[#10B981]/30' 
                        : isPhase1 
                        ? 'bg-[#F59E0B]/10 text-[#F59E0B] border-[#F59E0B]/30 font-semibold' 
                        : 'bg-[#1E222A] text-[#94A3B8] border-[#2E3440]'
                    }`}>
                      {isPhase0 ? 'COMPLETED' : isPhase1 ? 'ACTIVE SEED TARGET' : 'PLANNED'}
                    </span>
                    <span className="font-mono text-xs text-[#64748B]">
                      {isSelected ? '▼' : '→'}
                    </span>
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        {/* 2. Crisp Detail Bar for Selected Phase */}
        <div className="p-6 sm:p-8 bg-[#111317]">
          <div className="flex flex-wrap items-center justify-between gap-3 mb-6 pb-4 border-b border-[#222630]">
            <div>
              <div className="flex items-center space-x-2 mb-1">
                <span className="font-mono text-base font-bold text-[#F59E0B]">
                  {selectedPhase.phase}: {selectedPhase.name}
                </span>
                <span className="text-[#64748B] font-mono text-xs">//</span>
                <span className="font-mono text-xs text-[#9CA3AF]">
                  {selectedPhase.timeline}
                </span>
              </div>
              <div className="font-mono text-xs text-[#64748B]">
                Budget Allocation: <strong className="text-[#F3F4F6]">₹{selectedPhase.budgetLakhs.toFixed(1)} Lakhs</strong>
              </div>
            </div>

            <div className="px-3 py-1 bg-[#0A0B0D] border border-[#222630] rounded-sm font-mono text-xs text-[#9CA3AF]">
              Batch Scale: <strong className="text-[#F3F4F6]">{selectedPhase.batches}</strong>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            
            {/* Left 6 Cols: Engineering Objectives */}
            <div className="lg:col-span-6 p-4 bg-[#0A0B0D] border border-[#222630] rounded-sm flex flex-col justify-between">
              <div>
                <div className="font-mono text-xs text-[#64748B] uppercase tracking-wider mb-2">
                  ENGINEERING & EXECUTION OBJECTIVES
                </div>
                <p className="text-xs sm:text-sm text-[#F3F4F6] leading-relaxed">
                  {selectedPhase.objectives}
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-[#222630] font-mono text-[11px] text-[#64748B]">
                Lead Investigator: Sourish Senapati (FinnoaQ Agro-Industrial Technologies)
              </div>
            </div>

            {/* Right 6 Cols: Quantitative Gate Release Criteria */}
            <div className="lg:col-span-6 p-4 bg-[#0A0B0D] border border-[#F59E0B] rounded-sm flex flex-col justify-between">
              <div>
                <div className="font-mono text-xs text-[#F59E0B] uppercase font-semibold tracking-wider mb-2">
                  QUANTITATIVE GATE RELEASE CRITERIA
                </div>
                <div className="text-xs sm:text-sm text-[#F3F4F6] font-mono leading-relaxed">
                  {selectedPhase.gateDecision}
                </div>
              </div>
              <div className="mt-4 pt-3 border-t border-[#222630] font-mono text-[11px] text-[#10B981]">
                Zero commercial deployment without audited milestone sign-off
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>
  );
}

