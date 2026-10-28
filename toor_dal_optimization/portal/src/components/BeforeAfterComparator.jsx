import React, { useState, useEffect } from 'react';
import { Play, RotateCcw, AlertOctagon, CheckCircle2, Clock, Sparkles } from 'lucide-react';

export default function BeforeAfterComparator() {
  const [isRunning, setIsRunning] = useState(false);
  const [simStep, setSimStep] = useState(4); // default completed view (4 lines)

  const naiveLogs = [
    { t: "00:00", text: "Infeed: Tanzanian Aged HTC Dal (Moisture: 11.5% wb, Bound Ca²⁺: 12.4 mol/m³)", status: "WARN" },
    { t: "00:20", text: "Naive Water Steep @ 70°C: PME uninhibited; pectin de-esterification accelerates crosslinks", status: "FAIL" },
    { t: "00:45", text: "LOX Oxidation Triggered: Hexanal level surges to 0.185 ppm (Strong beany off-flavor blooming)", status: "FAIL" },
    { t: "01:10", text: "Single-Stage Flash Drying: Hoop stress spikes to 1.12 MPa; radial fissure breakage = 11.8%", status: "FAIL" },
    { t: "01:30", text: "Hawkins Cooker Test: Core shear force = 48.5 N (>18.0 N limit); 8 whistles required (FAILED)", status: "ERROR" }
  ];

  const omegaLogs = [
    { t: "00:00", text: "Infeed: Tanzanian Aged HTC Dal (Moisture: 11.5% wb, Bound Ca²⁺: 12.4 mol/m³)", status: "NOMINAL" },
    { t: "00:20", text: "S1-09 Chelation @ 48°C (pH 5.20): 40 kHz ultrasound thins BL 73%; 41.8% Ca²⁺ selectively extracted", status: "PASS" },
    { t: "00:45", text: "LOX Acid Denaturation: Steeping at pH 5.20 denatures 86.4% LOX; Hexanal capped at 0.025 ppm", status: "PASS" },
    { t: "01:10", text: "Two-Stage Tempered Drying: 20-min adiabatic deck holds hoop stress <0.38 MPa; breakage <0.35%", status: "PASS" },
    { t: "01:30", text: "Hawkins Cooker Test: Core shear force = 15.2 N (≤18.0 N limit); 2 whistles tenderized (VALIDATED)", status: "CONVERGED" }
  ];

  const runSimulation = () => {
    setIsRunning(true);
    setSimStep(0);
  };

  useEffect(() => {
    if (isRunning && simStep < 4) {
      const timer = setTimeout(() => {
        setSimStep(prev => prev + 1);
      }, 700);
      return () => clearTimeout(timer);
    } else if (simStep >= 4) {
      setIsRunning(false);
    }
  }, [isRunning, simStep]);

  return (
    <section id="comparator" className="border-b border-[#1E2230] bg-[#090A0F] py-14">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8 border-b border-[#1E2230] pb-6">
          <div>
            <div className="flex items-center gap-2">
              <span className="font-mono text-xs font-bold text-[#F59E0B] tracking-widest uppercase">[02 // DUAL COMPARATOR]</span>
              <span className="h-1 w-1 rounded-full bg-[#F59E0B]"></span>
              <span className="font-mono text-xs text-[#64748B]">NAIVE VS DETERMINISTIC OMEGA EXECUTION</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-bold text-[#F3F4F6] tracking-tight mt-1">
              Before vs. After: Physical Execution Trace
            </h2>
            <p className="text-sm text-[#94A3B8]">
              Witness line-by-line how conventional hydrothermal processing diverges while FinnoaQ OMEGA enforces thermodynamic constraints.
            </p>
          </div>

          {/* Run Simulation Trigger */}
          <button
            onClick={runSimulation}
            disabled={isRunning}
            className="flex items-center gap-2 bg-[#F3F4F6] hover:bg-white text-[#090A0F] font-mono text-xs font-bold px-4 py-2.5 rounded-sm transition-all shadow-md disabled:opacity-50 w-fit"
          >
            {isRunning ? (
              <>
                <Clock className="w-3.5 h-3.5 animate-spin" />
                <span>Simulating...</span>
              </>
            ) : (
              <>
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>▶ Run Simulation</span>
              </>
            )}
          </button>
        </div>

        {/* Side-by-Side Dual Terminal Comparison */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          
          {/* Left Side: Standard / Naive Execution */}
          <div className="border border-[#EF4444]/40 bg-[#11131A] rounded-sm p-5 flex flex-col gap-4 shadow-lg">
            <div className="flex items-center justify-between border-b border-[#1E2230] pb-3">
              <div className="flex items-center gap-2">
                <AlertOctagon className="w-4 h-4 text-[#EF4444]" />
                <span className="font-mono text-xs font-bold text-[#EF4444] uppercase tracking-wider">
                  STANDARD / NAIVE EXECUTION (TRADITIONAL MILL)
                </span>
              </div>
              <span className="font-mono text-[10px] bg-[#EF4444]/10 text-[#EF4444] px-2 py-0.5 rounded-sm border border-[#EF4444]/30">
                DISCOUNT: -₹20.00/kg
              </span>
            </div>

            {/* Terminal Window */}
            <div className="bg-[#050811] border border-[#1E2230] p-3 rounded-sm font-mono text-[11px] min-h-[220px] flex flex-col gap-2.5">
              {naiveLogs.slice(0, simStep + 1).map((log, i) => (
                <div key={i} className="flex items-start gap-2 leading-relaxed">
                  <span className="text-[#64748B] select-none tabular-nums">[{log.t}]</span>
                  <span className="text-[#EF4444] font-bold select-none">[{log.status}]</span>
                  <span className="text-[#CBD5E1]">{log.text}</span>
                </div>
              ))}
            </div>

            {/* Final Metrics Banner */}
            <div className="grid grid-cols-3 gap-2 pt-2 border-t border-[#1E2230] text-center font-mono">
              <div className="bg-[#090A0F] p-2 border border-[#1E2230] rounded-sm">
                <span className="text-[9px] text-[#64748B] block">BOILING TIME</span>
                <span className="text-sm font-bold text-[#EF4444]">65 min (8 Whistles)</span>
              </div>
              <div className="bg-[#090A0F] p-2 border border-[#1E2230] rounded-sm">
                <span className="text-[9px] text-[#64748B] block">BROKEN FINES</span>
                <span className="text-sm font-bold text-[#EF4444]">11.8% Loss</span>
              </div>
              <div className="bg-[#090A0F] p-2 border border-[#1E2230] rounded-sm">
                <span className="text-[9px] text-[#64748B] block">AFTERTASTE</span>
                <span className="text-sm font-bold text-[#EF4444]">Hexanal 0.18ppm</span>
              </div>
            </div>
          </div>

          {/* Right Side: FinnoaQ OMEGA Execution */}
          <div className="border border-[#10B981]/40 bg-[#11131A] rounded-sm p-5 flex flex-col gap-4 shadow-lg">
            <div className="flex items-center justify-between border-b border-[#1E2230] pb-3">
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#10B981]" />
                <span className="font-mono text-xs font-bold text-[#10B981] uppercase tracking-wider">
                  FINNOAQ OMEGA EXECUTION (BIO-CHELATION SKID)
                </span>
              </div>
              <span className="font-mono text-[10px] bg-[#10B981]/10 text-[#10B981] px-2 py-0.5 rounded-sm border border-[#10B981]/30">
                PROFIT LIFT: +₹8.00/kg
              </span>
            </div>

            {/* Terminal Window */}
            <div className="bg-[#050811] border border-[#1E2230] p-3 rounded-sm font-mono text-[11px] min-h-[220px] flex flex-col gap-2.5">
              {omegaLogs.slice(0, simStep + 1).map((log, i) => (
                <div key={i} className="flex items-start gap-2 leading-relaxed">
                  <span className="text-[#64748B] select-none tabular-nums">[{log.t}]</span>
                  <span className="text-[#10B981] font-bold select-none">[{log.status}]</span>
                  <span className="text-[#F3F4F6]">{log.text}</span>
                </div>
              ))}
            </div>

            {/* Final Metrics Banner */}
            <div className="grid grid-cols-3 gap-2 pt-2 border-t border-[#1E2230] text-center font-mono">
              <div className="bg-[#090A0F] p-2 border border-[#1E2230] rounded-sm">
                <span className="text-[9px] text-[#64748B] block">BOILING TIME</span>
                <span className="text-sm font-bold text-[#10B981]">14.8 min (2 Whistles)</span>
              </div>
              <div className="bg-[#090A0F] p-2 border border-[#1E2230] rounded-sm">
                <span className="text-[9px] text-[#64748B] block">BROKEN FINES</span>
                <span className="text-sm font-bold text-[#10B981]">&lt;0.35% Fines</span>
              </div>
              <div className="bg-[#090A0F] p-2 border border-[#1E2230] rounded-sm">
                <span className="text-[9px] text-[#64748B] block">AFTERTASTE</span>
                <span className="text-sm font-bold text-[#10B981]">Hexanal 0.025ppm</span>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
