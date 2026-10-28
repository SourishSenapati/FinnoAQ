import React, { useState } from 'react';
import { BarChart3, CheckCircle2, TrendingUp, Filter } from 'lucide-react';

export default function BenchmarkMatrix() {
  const [activeMetric, setActiveMetric] = useState('throughput'); // 'throughput', 'latency', 'energy', 'yield'

  const metricsConfig = {
    throughput: {
      label: "Raw Processing Throughput",
      unit: "kg/h finished dal",
      max: 700,
      higherBetter: true,
      desc: "Mass flow rate of tenderized finished split toor dal discharged from plant battery."
    },
    latency: {
      label: "P99 Cooking Whistle Latency",
      unit: "minutes in Hawkins pressure cooker",
      max: 75,
      higherBetter: false,
      desc: "Hawkins pressure cooker boiling time to reach soft cotyledon texture (Fwb ≤ 18.0 N)."
    },
    energy: {
      label: "Specific Thermal Duty",
      unit: "MJ / kg finished product",
      max: 4.5,
      higherBetter: false,
      desc: "Combined steeping, fluid-bed drying, and evaporation thermal enthalpy required per kg product."
    },
    yield: {
      label: "Finished Dry Solids Yield",
      unit: "% dry matter retained",
      max: 100,
      higherBetter: true,
      desc: "Percentage of pulse dry solids preserved after steeping, washing, drying, and optical grading."
    }
  };

  const systems = [
    {
      name: "Traditional Atmospheric Steep (Naive)",
      type: "Baseline 01",
      throughput: 120,
      latency: 65.0,
      energy: 3.85,
      yield: 88.2,
      note: "Severe 8-whistle boiling; 11.8% fines loss"
    },
    {
      name: "High-Temperature Pressure Autoclave",
      type: "Baseline 02",
      throughput: 350,
      latency: 35.0,
      energy: 4.10,
      yield: 91.5,
      note: "Thermal degradation of pulse proteins; cooked flavor"
    },
    {
      name: "Superheated Steam Dehydration",
      type: "Baseline 03",
      throughput: 410,
      latency: 28.0,
      energy: 3.40,
      yield: 93.8,
      note: "High equipment CapEx (>₹2.8 Cr); case hardening"
    },
    {
      name: "Industrial Microwave Cavitation",
      type: "Baseline 04",
      throughput: 420,
      latency: 22.0,
      energy: 2.95,
      yield: 94.6,
      note: "Non-uniform electromagnetic field hot spots"
    },
    {
      name: "FinnoaQ OMEGA Deterministic Skid",
      type: "FinnoaQ Standard",
      isFinnoaq: true,
      throughput: 625,
      latency: 14.8,
      energy: 1.82,
      yield: 97.37,
      note: "2-whistle Hawkins passing (15.2 N); S1-09 bio-buffer"
    }
  ];

  const currentMetric = metricsConfig[activeMetric];

  return (
    <section id="benchmarks" className="border-b border-[#1E2230] bg-[#090A0F] py-14">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8 border-b border-[#1E2230] pb-6">
          <div>
            <div className="flex items-center gap-2">
              <span className="font-mono text-xs font-bold text-[#38BDF8] tracking-widest uppercase">[04 // BENCHMARK MATRIX]</span>
              <span className="h-1 w-1 rounded-full bg-[#38BDF8]"></span>
              <span className="font-mono text-xs text-[#64748B]">MULTI-VARIABLE PERFORMANCE AUDIT</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-bold text-[#F3F4F6] tracking-tight mt-1">
              Rigorous Industrial Benchmark Matrix
            </h2>
            <p className="text-sm text-[#94A3B8]">
              Comparing the FinnoaQ OMEGA deterministic engine against 4 legacy legume processing architectures.
            </p>
          </div>

          {/* Metric Selector Buttons */}
          <div className="flex flex-wrap items-center gap-1.5 bg-[#11131A] p-1 border border-[#1E2230] rounded-sm">
            <button
              onClick={() => setActiveMetric('throughput')}
              className={`font-mono text-xs px-3 py-1.5 rounded-xs transition-all ${
                activeMetric === 'throughput' ? 'bg-[#38BDF8] text-[#090A0F] font-bold' : 'text-[#94A3B8] hover:text-[#F3F4F6]'
              }`}
            >
              Throughput
            </button>
            <button
              onClick={() => setActiveMetric('latency')}
              className={`font-mono text-xs px-3 py-1.5 rounded-xs transition-all ${
                activeMetric === 'latency' ? 'bg-[#38BDF8] text-[#090A0F] font-bold' : 'text-[#94A3B8] hover:text-[#F3F4F6]'
              }`}
            >
              P99 Latency
            </button>
            <button
              onClick={() => setActiveMetric('energy')}
              className={`font-mono text-xs px-3 py-1.5 rounded-xs transition-all ${
                activeMetric === 'energy' ? 'bg-[#38BDF8] text-[#090A0F] font-bold' : 'text-[#94A3B8] hover:text-[#F3F4F6]'
              }`}
            >
              Energy Duty
            </button>
            <button
              onClick={() => setActiveMetric('yield')}
              className={`font-mono text-xs px-3 py-1.5 rounded-xs transition-all ${
                activeMetric === 'yield' ? 'bg-[#38BDF8] text-[#090A0F] font-bold' : 'text-[#94A3B8] hover:text-[#F3F4F6]'
              }`}
            >
              Solids Yield
            </button>
          </div>
        </div>

        {/* Filterable Tabular Benchmark Display */}
        <div className="border border-[#1E2230] bg-[#11131A] rounded-sm overflow-hidden shadow-lg">
          <div className="px-5 py-3 border-b border-[#1E2230] bg-[#0D111A] flex justify-between items-center text-xs font-mono text-[#64748B]">
            <span>METRIC: <strong className="text-[#F3F4F6] uppercase">{currentMetric.label}</strong> ({currentMetric.unit})</span>
            <span>{currentMetric.higherBetter ? "▲ HIGHER VALUE IS SUPERIOR" : "▼ LOWER VALUE IS SUPERIOR"}</span>
          </div>

          <div className="divide-y divide-[#1E2230]">
            {systems.map((s, idx) => {
              const val = s[activeMetric];
              const pct = Math.min(100, (val / currentMetric.max) * 100);
              const isBest = s.isFinnoaq;

              return (
                <div
                  key={idx}
                  className={`p-4 sm:p-5 flex flex-col md:flex-row md:items-center justify-between gap-4 transition-colors ${
                    isBest ? 'bg-[#10B981]/5 border-l-4 border-l-[#10B981]' : 'hover:bg-[#0D111A]'
                  }`}
                >
                  <div className="md:w-1/3">
                    <div className="flex items-center gap-2">
                      <span className={`font-mono text-[10px] px-2 py-0.5 rounded-sm border ${
                        isBest ? 'border-[#10B981] bg-[#10B981]/10 text-[#10B981] font-bold' : 'border-[#1E2230] text-[#64748B]'
                      }`}>
                        {s.type}
                      </span>
                      {isBest && <CheckCircle2 className="w-3.5 h-3.5 text-[#10B981]" />}
                    </div>
                    <h3 className={`text-sm sm:text-base font-bold mt-1 ${isBest ? 'text-[#F3F4F6]' : 'text-[#CBD5E1]'}`}>
                      {s.name}
                    </h3>
                    <p className="text-xs text-[#64748B] mt-0.5 font-mono">{s.note}</p>
                  </div>

                  {/* Animated Progress Bar */}
                  <div className="md:w-1/2 flex flex-col gap-1.5">
                    <div className="flex justify-between items-center font-mono text-xs">
                      <span className="text-[#64748B] text-[11px]">{currentMetric.label}</span>
                      <span className={`font-bold tabular-nums text-sm ${isBest ? 'text-[#10B981]' : 'text-[#F3F4F6]'}`}>
                        {val} {currentMetric.unit}
                      </span>
                    </div>
                    <div className="w-full h-2.5 bg-[#090A0F] border border-[#1E2230] rounded-xs overflow-hidden">
                      <div
                        className={`h-full transition-all duration-700 rounded-xs ${
                          isBest ? 'bg-[#10B981]' : 'bg-[#38BDF8]'
                        }`}
                        style={{ width: `${pct}%` }}
                      ></div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          <div className="p-4 bg-[#090A0F] border-t border-[#1E2230] text-xs font-mono text-[#94A3B8] flex justify-between items-center">
            <span><strong>Audited Empirical Basis:</strong> Laboratory micro-press texture measurements (n=40) paired with Hawkins pressure cooker whistle sensors.</span>
            <span className="text-[#10B981] font-bold">97.37% RECOVERED MASS</span>
          </div>
        </div>

      </div>
    </section>
  );
}
