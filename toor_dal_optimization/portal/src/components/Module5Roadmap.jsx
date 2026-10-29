import React, { useState } from 'react';
import { SCALEUP_PHASES } from '../data/micrositeData.js';

export default function Module5Roadmap() {
  const [selectedPhaseIdx, setSelectedPhaseIdx] = useState(1); // Default to Phase 1 (Active Target)

  const selectedPhase = SCALEUP_PHASES[selectedPhaseIdx];

  return (
    <section id="roadmap" className="w-full bg-[#0C0E12] border-b border-[#1E232E] scroll-mt-20">
      <div className="max-w-[1440px] mx-auto border-x border-[#1E232E]">
        
        {/* Module Header */}
        <div className="p-6 border-b border-[#1E232E] bg-[#111319] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#151821] text-[#94A3B8] border border-[#232836] font-mono text-xs rounded-xs font-medium">
              [04 // SCALE-UP ROADMAP & DECISION GATES]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#E6E8EC]">
              Single Consolidated 5-Phase Scale-Up Roadmap
            </h2>
          </div>
          <span className="font-mono text-xs px-2 py-0.5 bg-[#151821] text-[#D97706] border border-[#232836] rounded-xs font-medium">
            ACTIVE TARGET: PHASE 1 BENCH SEED (₹33.0L)
          </span>
        </div>

        {/* 1. Horizontal Interactive Phase Selector Bar */}
        <div className="p-6 bg-[#0C0E12] border-b border-[#1E232E]">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
            {SCALEUP_PHASES.map((p, idx) => {
              const isSelected = selectedPhaseIdx === idx;
              const isPhase0 = idx === 0;
              const isPhase1 = idx === 1;

              return (
                <button
                  key={p.phase}
                  onClick={() => setSelectedPhaseIdx(idx)}
                  className={`p-4 text-left border rounded-xs transition-all cursor-pointer relative ${
                    isSelected
                      ? 'bg-[#151821] border-[#D97706]'
                      : 'bg-[#111319] border-[#1E232E] hover:border-[#5E6573]'
                  }`}
                >
                  <div className="flex justify-between items-center mb-1">
                    <span className={`font-mono text-xs font-bold ${
                      isPhase1 
                        ? 'text-[#D97706]' 
                        : isPhase0 
                        ? 'text-[#10B981]' 
                        : 'text-[#E6E8EC]'
                    }`}>
                      {p.phase}
                    </span>
                    <span className="font-mono text-[10px] text-[#5E6573]">
                      ₹{p.budgetLakhs.toFixed(1)}L
                    </span>
                  </div>

                  <div className="text-xs font-medium text-[#E6E8EC] line-clamp-1 mb-1">
                    {p.name}
                  </div>

                  <div className="font-mono text-[11px] text-[#8E95A2] mb-3 truncate">
                    {p.timeline}
                  </div>

                  <div className="pt-2 border-t border-[#1E232E] flex items-center justify-between">
                    <span className={`text-[10px] font-mono px-1.5 py-0.2 rounded-xs border ${
                      isPhase0 
                        ? 'bg-[#10B981]/10 text-[#10B981] border-[#10B981]/30' 
                        : isPhase1 
                        ? 'bg-[#D97706]/10 text-[#D97706] border-[#D97706]/30 font-semibold' 
                        : 'bg-[#151821] text-[#94A3B8] border-[#232836]'
                    }`}>
                      {isPhase0 ? 'COMPLETED' : isPhase1 ? 'ACTIVE SEED TARGET' : 'PLANNED'}
                    </span>
                    <span className="font-mono text-xs text-[#5E6573]">
                      {isSelected ? '▼' : '→'}
                    </span>
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        {/* 2. Crisp Detail Bar for Selected Phase */}
        <div className="p-6 sm:p-8 bg-[#111319]">
          <div className="flex flex-wrap items-center justify-between gap-3 mb-6 pb-4 border-b border-[#1E232E]">
            <div>
              <div className="flex items-center space-x-2 mb-1">
                <span className="font-mono text-base font-bold text-[#D97706]">
                  {selectedPhase.phase}: {selectedPhase.name}
                </span>
                <span className="text-[#5E6573] font-mono text-xs">//</span>
                <span className="font-mono text-xs text-[#8E95A2]">
                  {selectedPhase.timeline}
                </span>
              </div>
              <div className="font-mono text-xs text-[#5E6573]">
                Budget Allocation: <strong className="text-[#E6E8EC]">₹{selectedPhase.budgetLakhs.toFixed(1)} Lakhs</strong>
              </div>
            </div>

            <div className="px-3 py-1 bg-[#0C0E12] border border-[#1E232E] rounded-xs font-mono text-xs text-[#8E95A2]">
              Batch Scale: <strong className="text-[#E6E8EC]">{selectedPhase.batches}</strong>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            
            {/* Left 6 Cols: Engineering Objectives */}
            <div className="lg:col-span-6 p-4 bg-[#0C0E12] border border-[#1E232E] rounded-xs flex flex-col justify-between">
              <div>
                <div className="font-mono text-xs text-[#5E6573] uppercase tracking-wider mb-2">
                  ENGINEERING & EXECUTION OBJECTIVES
                </div>
                <p className="text-xs sm:text-sm text-[#E6E8EC] leading-relaxed">
                  {selectedPhase.objectives}
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-[#1E232E] font-mono text-[11px] text-[#5E6573]">
                Lead Investigator: Sourish Senapati (FinnoaQ Agro-Industrial Technologies)
              </div>
            </div>

            {/* Right 6 Cols: Quantitative Gate Release Criteria */}
            <div className="lg:col-span-6 p-4 bg-[#0C0E12] border border-[#D97706]/40 rounded-xs flex flex-col justify-between">
              <div>
                <div className="font-mono text-xs text-[#D97706] uppercase font-semibold tracking-wider mb-2">
                  QUANTITATIVE GATE RELEASE CRITERIA
                </div>
                <div className="text-xs sm:text-sm text-[#E6E8EC] font-mono leading-relaxed">
                  {selectedPhase.gateDecision}
                </div>
              </div>
              <div className="mt-4 pt-3 border-t border-[#1E232E] font-mono text-[11px] text-[#10B981]">
                Zero commercial deployment without audited milestone sign-off
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>
  );
}
