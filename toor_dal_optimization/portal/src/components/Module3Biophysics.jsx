import React, { useState } from 'react';
import { BIOPHYSICAL_SOLUTION, FORENSIC_FAILURE_ANALYSIS } from '../data/micrositeData.js';

export default function Module3Biophysics() {
  const [activeView, setActiveView] = useState('viewA'); // 'viewA' | 'viewB'
  
  // View A: Mechanism Selector
  const [activeMechanism, setActiveMechanism] = useState('pathology');
  
  // Interactive Time Scrubber for Kinetics Curve (0 to 30 min)
  const [timeMin, setTimeMin] = useState(24);

  // Before vs After Comparator Slider (0 = Untreated, 100 = FinnoaQ Treated)
  const [compareSplit, setCompareSplit] = useState(50);

  // Kinetic Calculations based on time:
  const caExtraction = +(41.8 * (1 - Math.exp(-timeMin / 10.5)) / (1 - Math.exp(-24 / 10.5))).toFixed(1);
  const shearForce = +(26.4 - ((26.4 - 15.2) * (timeMin / 24))).toFixed(1);
  const boundaryLayerUm = timeMin >= 2 ? 8 : 42;
  const whistleCount = shearForce <= 18.0 ? '2 Whistles (7.0 min)' : shearForce <= 22.0 ? '4 Whistles (14.0 min)' : '8+ Whistles (HTC Failure)';

  return (
    <section id="biophysics" className="w-full bg-[#0C0E12] border-b border-[#1E232E] scroll-mt-20">
      <div className="max-w-[1440px] mx-auto border-x border-[#1E232E]">
        
        {/* Module Header with 2-View Toggle */}
        <div className="p-6 border-b border-[#1E232E] bg-[#111319] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#151821] text-[#94A3B8] border border-[#232836] font-mono text-xs rounded-xs">
              [02 // BIOPHYSICS & FAILURE FORENSICS]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#E6E8EC]">
              Interactive Biophysics & Failure Forensics Workbench
            </h2>
          </div>

          {/* 2-View Interactive Segmented Toggle */}
          <div className="flex items-center bg-[#0C0E12] p-1 border border-[#1E232E] rounded-xs">
            <button
              onClick={() => setActiveView('viewA')}
              className={`px-3 py-1.5 font-mono text-xs rounded-xs transition-colors cursor-pointer ${
                activeView === 'viewA'
                  ? 'bg-[#151821] text-[#D97706] border border-[#D97706] font-semibold'
                  : 'text-[#8E95A2] hover:text-[#E6E8EC] border border-transparent'
              }`}
            >
              [View A: S1-09 Chelation Kinetics & Physics]
            </button>
            <button
              onClick={() => setActiveView('viewB')}
              className={`px-3 py-1.5 font-mono text-xs rounded-xs transition-colors cursor-pointer ${
                activeView === 'viewB'
                  ? 'bg-[#151821] text-[#D97706] border border-[#D97706] font-semibold'
                  : 'text-[#8E95A2] hover:text-[#E6E8EC] border border-transparent'
              }`}
            >
              [View B: Forensic Industry Failure Analysis]
            </button>
          </div>
        </div>

        {/* VIEW A: S1-09 Chelation Kinetics & Physics */}
        {activeView === 'viewA' && (
          <div>
            {/* 1. Interactive Before vs After Split Comparator */}
            <div className="p-6 sm:p-8 bg-[#111319] border-b border-[#1E232E]">
              <div className="flex flex-wrap justify-between items-center gap-3 mb-5">
                <div>
                  <span className="font-mono text-xs text-[#5E6573] uppercase tracking-wider block mb-1">
                    CELLULAR ULTRASTRUCTURE EVALUATION
                  </span>
                  <h3 className="text-base sm:text-lg font-semibold text-[#E6E8EC] tracking-tight">
                    Untreated Hard-to-Cook Matrix vs. S1-09 Conditioned Grain
                  </h3>
                </div>
                <div className="flex items-center space-x-2">
                  <span className="font-mono text-xs text-[#D97706] bg-[#151821] px-2.5 py-1 border border-[#262C3A] rounded-xs">
                    Progress: <strong className="text-[#E6E8EC]">{compareSplit}%</strong>
                  </span>
                </div>
              </div>

              {/* State Presets */}
              <div className="flex flex-wrap items-center gap-2 mb-4 font-mono text-xs">
                <span className="text-[#5E6573]">PRESETS:</span>
                <button
                  onClick={() => setCompareSplit(0)}
                  className={`px-2.5 py-1 rounded-xs border transition-colors cursor-pointer ${
                    compareSplit === 0 
                      ? 'bg-[#DC2626]/10 border-[#DC2626]/50 text-[#DC2626] font-medium' 
                      : 'bg-[#151821] border-[#1E232E] text-[#8E95A2] hover:text-[#E6E8EC]'
                  }`}
                >
                  [0% Untreated HTC 8-Whistles]
                </button>
                <button
                  onClick={() => setCompareSplit(50)}
                  className={`px-2.5 py-1 rounded-xs border transition-colors cursor-pointer ${
                    compareSplit === 50 
                      ? 'bg-[#D97706]/10 border-[#D97706]/50 text-[#D97706] font-medium' 
                      : 'bg-[#151821] border-[#1E232E] text-[#8E95A2] hover:text-[#E6E8EC]'
                  }`}
                >
                  [50% Reaction Progression]
                </button>
                <button
                  onClick={() => setCompareSplit(100)}
                  className={`px-2.5 py-1 rounded-xs border transition-colors cursor-pointer ${
                    compareSplit === 100 
                      ? 'bg-[#10B981]/10 border-[#10B981]/50 text-[#10B981] font-medium' 
                      : 'bg-[#151821] border-[#1E232E] text-[#8E95A2] hover:text-[#E6E8EC]'
                  }`}
                >
                  [100% S1-09 Conditioned (2 Whistles)]
                </button>
              </div>

              {/* Split Comparator Visual Container */}
              <div className="relative border border-[#1E232E] rounded-xs overflow-hidden bg-[#0C0E12] p-4 sm:p-5 mb-4">
                
                {/* Cellular Cross-Section Visual Bar */}
                <div className="w-full h-20 mb-5 rounded-xs bg-[#13151B] border border-[#1E232E] relative overflow-hidden flex items-center justify-between px-5">
                  <div 
                    className="absolute inset-y-0 left-0 bg-[#DC2626]/10 transition-all duration-200"
                    style={{ width: `${100 - compareSplit}%` }}
                  />
                  <div 
                    className="absolute inset-y-0 right-0 bg-[#10B981]/10 transition-all duration-200"
                    style={{ width: `${compareSplit}%` }}
                  />

                  {/* Left Label */}
                  <div className="relative z-10 font-mono text-xs">
                    <span className="text-[#DC2626] font-medium block">UNTREATED GRAIN</span>
                    <span className="text-[#8E95A2] text-[11px]">Insoluble Ca-Pectate (33.5 mol/m³)</span>
                  </div>

                  {/* Center Node */}
                  <div className="relative z-10 px-2 py-0.5 rounded-xs border border-[#232836] bg-[#151821] font-mono text-[11px] text-[#D97706] font-medium">
                    {compareSplit}%
                  </div>

                  {/* Right Label */}
                  <div className="relative z-10 font-mono text-xs text-right">
                    <span className="text-[#10B981] font-medium block">S1-09 CONDITIONED</span>
                    <span className="text-[#8E95A2] text-[11px]">41.8% Ca²⁺ Extracted // 15.2 N</span>
                  </div>
                </div>

                {/* Data Comparison Cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                  
                  {/* State 1: Untreated Raw Hard-to-Cook Dal */}
                  <div className={`p-4 rounded-xs border transition-all ${
                    compareSplit <= 50 ? 'bg-[#13151B] border-[#DC2626]/50' : 'bg-[#0C0E12] border-[#1E232E] opacity-70'
                  }`}>
                    <div className="flex justify-between items-center mb-2.5">
                      <span className="font-mono text-xs font-semibold text-[#DC2626] tracking-wide">
                        UNTREATED IMPORTED TOOR DAL
                      </span>
                      <span className="px-2 py-0.5 bg-[#DC2626]/10 text-[#DC2626] border border-[#DC2626]/30 font-mono text-[10px] rounded-xs font-medium">
                        8+ WHISTLES (60–70 MIN)
                      </span>
                    </div>
                    <div className="space-y-2 font-mono text-xs">
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Core Shear Force:</span>
                        <span className="text-[#DC2626] font-medium">26.4 N (Rock Hard)</span>
                      </div>
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Middle Lamella:</span>
                        <span className="text-[#8E95A2]">33.5 mol/m³ Ca-Pectate</span>
                      </div>
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Lipoxygenase (LOX):</span>
                        <span className="text-[#DC2626]">100% Active</span>
                      </div>
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Headspace Hexanal:</span>
                        <span className="text-[#DC2626]">0.380 ppm</span>
                      </div>
                      <div className="flex justify-between pt-0.5">
                        <span className="text-[#5E6573]">Mandi Valuation:</span>
                        <span className="text-[#DC2626] font-medium">₹85.00 / kg (-₹20 discount)</span>
                      </div>
                    </div>
                  </div>

                  {/* State 2: FinnoaQ S1-09 Conditioned Dal */}
                  <div className={`p-4 rounded-xs border transition-all ${
                    compareSplit > 50 ? 'bg-[#13151B] border-[#10B981]/50' : 'bg-[#0C0E12] border-[#1E232E] opacity-70'
                  }`}>
                    <div className="flex justify-between items-center mb-2.5">
                      <span className="font-mono text-xs font-semibold text-[#10B981] tracking-wide">
                        FINNOAQ S1-09 CONDITIONED DAL
                      </span>
                      <span className="px-2 py-0.5 bg-[#10B981]/10 text-[#10B981] border border-[#10B981]/30 font-mono text-[10px] rounded-xs font-medium">
                        2 WHISTLES (7.0 MIN)
                      </span>
                    </div>
                    <div className="space-y-2 font-mono text-xs">
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Core Shear Force:</span>
                        <span className="text-[#10B981] font-medium">15.2 N (≤ 18.0 N limit)</span>
                      </div>
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Middle Lamella:</span>
                        <span className="text-[#10B981]">41.8% Ca2+ Extracted</span>
                      </div>
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Lipoxygenase (LOX):</span>
                        <span className="text-[#10B981]">86.4% Denatured (pH 5.20)</span>
                      </div>
                      <div className="flex justify-between border-b border-[#1E232E] pb-1">
                        <span className="text-[#5E6573]">Headspace Hexanal:</span>
                        <span className="text-[#10B981]">0.025 ppm (OAV = 0.84 &lt; 1.0)</span>
                      </div>
                      <div className="flex justify-between pt-0.5">
                        <span className="text-[#5E6573]">Mandi Valuation:</span>
                        <span className="text-[#10B981] font-medium">₹105.00 / kg (Desi Parity)</span>
                      </div>
                    </div>
                  </div>

                </div>

                {/* Range Slider Controller */}
                <div className="mt-4 pt-3 border-t border-[#1E232E]">
                  <div className="flex justify-between text-[11px] font-mono text-[#5E6573] mb-1.5">
                    <span>◀ Untreated Grain State</span>
                    <span className="text-[#D97706]">Scrub Transition Level</span>
                    <span>Conditioned Grain State ▶</span>
                  </div>
                  <input
                    type="range"
                    min="0"
                    max="100"
                    value={compareSplit}
                    onChange={(e) => setCompareSplit(Number(e.target.value))}
                    className="w-full h-1.5 bg-[#171B24] rounded-xs appearance-none cursor-pointer accent-[#D97706]"
                  />
                </div>
              </div>
            </div>
            {/* 2. Main Kinetics & Mechanism Workbench */}
            <div className="grid grid-cols-1 lg:grid-cols-12 border-b border-[#1E232E]">
              
              {/* Left 6 Columns: Interactive 24-Minute Kinetic Curve & Scrubber */}
              <div className="lg:col-span-6 p-6 sm:p-8 bg-[#0C0E12] border-b lg:border-b-0 lg:border-r border-[#1E232E] flex flex-col justify-between">
                <div>
                  <div className="flex justify-between items-center mb-3">
                    <span className="font-mono text-xs text-[#5E6573] uppercase tracking-wider">
                      24-MIN CALCIUM EXTRACTION & TEXTURE KINETICS
                    </span>
                    <span className="font-mono text-xs text-[#10B981]">
                      T = 48.0°C // 17 W/L UAE
                    </span>
                  </div>

                  {/* SVG Kinetics Chart */}
                  <div className="p-4 bg-[#111319] border border-[#1E232E] rounded-xs mb-4">
                    <svg viewBox="0 0 400 200" className="w-full h-48 overflow-visible">
                      {/* Grid Lines */}
                      <line x1="40" y1="20" x2="380" y2="20" stroke="#1E232E" strokeDasharray="2,2" />
                      <line x1="40" y1="60" x2="380" y2="60" stroke="#1E232E" strokeDasharray="2,2" />
                      <line x1="40" y1="100" x2="380" y2="100" stroke="#1E232E" strokeDasharray="2,2" />
                      <line x1="40" y1="140" x2="380" y2="140" stroke="#1E232E" strokeDasharray="2,2" />
                      <line x1="40" y1="170" x2="380" y2="170" stroke="#1E232E" />

                      {/* 18.0 N Threshold Line */}
                      <line x1="40" y1="120" x2="380" y2="120" stroke="#D97706" strokeDasharray="4,4" strokeWidth="1.5" />
                      <text x="375" y="115" fill="#D97706" fontSize="9" textAnchor="end" fontFamily="monospace">
                        18.0 N (2-Whistle Tenderness Limit)
                      </text>

                      {/* Curve 1: Calcium Extraction % (Amber) */}
                      <path
                        d="M 40 170 Q 120 70 380 40"
                        fill="none"
                        stroke="#D97706"
                        strokeWidth="2.5"
                      />

                      {/* Curve 2: Shear Force (Emerald) */}
                      <path
                        d="M 40 30 Q 160 110 380 145"
                        fill="none"
                        stroke="#10B981"
                        strokeWidth="2"
                      />

                      {/* Current Scrubber Point */}
                      {(() => {
                        const xPos = 40 + (timeMin / 30) * 340;
                        return (
                          <g>
                            <line x1={xPos} y1="15" x2={xPos} y2="175" stroke="#E6E8EC" strokeWidth="1" strokeDasharray="2,2" />
                            <circle cx={xPos} cy={170 - (caExtraction / 50) * 150} r="4" fill="#D97706" stroke="#0C0E12" strokeWidth="2" />
                            <circle cx={xPos} cy={30 + ((26.4 - shearForce) / 15) * 115} r="4" fill="#10B981" stroke="#0C0E12" strokeWidth="2" />
                          </g>
                        );
                      })()}

                      {/* Axis Labels */}
                      <text x="40" y="185" fill="#5E6573" fontSize="9" fontFamily="monospace">0m</text>
                      <text x="153" y="185" fill="#5E6573" fontSize="9" fontFamily="monospace">10m</text>
                      <text x="312" y="185" fill="#D97706" fontSize="9" fontWeight="bold" fontFamily="monospace">24m [Optimum]</text>
                      <text x="380" y="185" fill="#5E6573" fontSize="9" textAnchor="end" fontFamily="monospace">30m</text>
                    </svg>

                    <div className="flex justify-between items-center text-[11px] font-mono mt-2 pt-2 border-t border-[#1E232E]">
                      <div className="flex items-center space-x-2">
                        <span className="w-2.5 h-2.5 bg-[#D97706] inline-block rounded-xs"></span>
                        <span className="text-[#8E95A2]">Core Ca2+ Displaced (%): <strong className="text-[#D97706]">{caExtraction}%</strong></span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <span className="w-2.5 h-2.5 bg-[#10B981] inline-block rounded-xs"></span>
                        <span className="text-[#8E95A2]">WB Shear Force: <strong className="text-[#10B981]">{shearForce} N</strong></span>
                      </div>
                    </div>
                  </div>

                  {/* Interactive Time Slider */}
                  <div className="p-4 bg-[#111319] border border-[#1E232E] rounded-xs mb-4">
                    <div className="flex justify-between items-center mb-2 font-mono text-xs">
                      <span className="text-[#8E95A2]">Interactive Steeping Duration Scrubber:</span>
                      <span className="text-[#D97706] font-semibold text-sm tabular-nums">{timeMin} Minutes</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="30"
                      step="1"
                      value={timeMin}
                      onChange={(e) => setTimeMin(Number(e.target.value))}
                      className="w-full accent-[#D97706] cursor-pointer"
                    />
                    <div className="flex justify-between font-mono text-[10px] text-[#5E6573] mt-1">
                      <span>0m (Raw Dry)</span>
                      <span>12m (Superficial)</span>
                      <span className="text-[#D97706]">24m (Core Extraction)</span>
                      <span>30m (Over-leach)</span>
                    </div>
                  </div>

                  {/* Real-Time Live Readout Metrics */}
                  <div className="grid grid-cols-2 gap-2 font-mono text-xs">
                    <div className="p-3 bg-[#111319] border border-[#1E232E] rounded-xs">
                      <div className="text-[10px] text-[#5E6573]">BOUNDARY LAYER THICKNESS</div>
                      <div className="text-base font-semibold text-[#E6E8EC] my-0.5 tabular-nums">
                        {boundaryLayerUm} μm
                      </div>
                      <div className="text-[10px] text-[#10B981]">
                        {timeMin >= 2 ? 'Ultrasound microstreaming active' : 'Static liquid boundary'}
                      </div>
                    </div>

                    <div className="p-3 bg-[#111319] border border-[#1E232E] rounded-xs">
                      <div className="text-[10px] text-[#5E6573]">HAWKINS COOKER EQUIVALENT</div>
                      <div className="text-sm font-semibold text-[#D97706] my-0.5 tabular-nums truncate">
                        {whistleCount}
                      </div>
                      <div className="text-[10px] text-[#8E95A2]">
                        Benchmark Desi: 3 Whistles (9.8m)
                      </div>
                    </div>
                  </div>

                </div>

                <div className="font-mono text-[11px] text-[#5E6573] pt-4 border-t border-[#1E232E]">
                  Governing Equation: ∂c/∂t = ∇·(D_eff ∇c) - R_chelate // Hawkins 103.4 kPa Saturated Steam Model
                </div>
              </div>

              {/* Right 6 Columns: 5-Tab Technical Mechanism Selector */}
              <div className="lg:col-span-6 p-6 sm:p-8 bg-[#111319] flex flex-col justify-between">
                <div>
                  <div className="font-mono text-xs text-[#5E6573] uppercase tracking-wider mb-4">
                    BIOPHYSICAL MECHANISMS & EXPERIMENTAL PROOF
                  </div>

                  {/* 5 Tabs */}
                  <div className="flex flex-wrap gap-1 border-b border-[#1E232E] pb-2 mb-4 font-mono text-xs">
                    {[
                      { id: 'pathology', label: '1. Pathology' },
                      { id: 'stoichiometry', label: '2. S1-09 Buffer' },
                      { id: 'acoustics', label: '3. Hawkins Acoustics' },
                      { id: 'drying', label: '4. Two-Stage Drying' },
                      { id: 'flavor', label: '5. LOX Kinetics' }
                    ].map((tab) => (
                      <button
                        key={tab.id}
                        onClick={() => setActiveMechanism(tab.id)}
                        className={`px-3 py-1.5 rounded-xs transition-colors cursor-pointer ${
                          activeMechanism === tab.id
                            ? 'bg-[#151821] border border-[#D97706] text-[#D97706] font-semibold'
                            : 'bg-[#0C0E12] border border-[#1E232E] text-[#8E95A2] hover:text-[#E6E8EC]'
                        }`}
                      >
                        {tab.label}
                      </button>
                    ))}
                  </div>

                  {/* Tab Content Display */}
                  <div className="p-5 bg-[#0C0E12] border border-[#1E232E] rounded-xs min-h-[300px]">
                    
                    {activeMechanism === 'pathology' && (
                      <div>
                        <div className="font-mono text-xs text-[#D97706] font-semibold uppercase mb-2">
                          {BIOPHYSICAL_SOLUTION.pathology.title}
                        </div>
                        <p className="text-xs sm:text-sm text-[#8E95A2] leading-relaxed mb-4">
                          {BIOPHYSICAL_SOLUTION.pathology.description}
                        </p>
                        <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#1E232E]">
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">AGED AFRICAN DAL CA-PECTATE</div>
                            <div className="text-sm font-semibold text-[#EF4444] tabular-nums">33.5 mol / m³</div>
                            <div className="text-[10px] text-[#8E95A2]">Severe HTC Egg-Box Matrices</div>
                          </div>
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">DOMESTIC DESI BENCHMARK</div>
                            <div className="text-sm font-semibold text-[#10B981] tabular-nums">14.0 mol / m³</div>
                            <div className="text-[10px] text-[#8E95A2]">Natural Tender Cleaving</div>
                          </div>
                        </div>
                      </div>
                    )}

                    {activeMechanism === 'stoichiometry' && (
                      <div>
                        <div className="font-mono text-xs text-[#D97706] font-semibold uppercase mb-2">
                          {BIOPHYSICAL_SOLUTION.formulation.code}
                        </div>
                        <div className="space-y-2 mb-4 font-mono text-xs">
                          {BIOPHYSICAL_SOLUTION.formulation.components.map((comp, idx) => (
                            <div key={idx} className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                              <div className="flex justify-between items-center mb-1">
                                <span className="text-[#E6E8EC] font-semibold">{comp.name}</span>
                                <span className="text-[#D97706]">{comp.molarity} ({comp.concentration})</span>
                              </div>
                              <div className="text-[#8E95A2] text-[11px] font-sans">{comp.function}</div>
                            </div>
                          ))}
                        </div>
                        <div className="flex justify-between items-center font-mono text-xs p-2.5 bg-[#151821] border border-[#1E232E] rounded-xs">
                          <span className="text-[#8E95A2]">Equilibrium pH Envelope:</span>
                          <span className="text-[#10B981] font-semibold">{BIOPHYSICAL_SOLUTION.formulation.equilibriumPh}</span>
                        </div>
                      </div>
                    )}

                    {activeMechanism === 'acoustics' && (
                      <div>
                        <div className="font-mono text-xs text-[#D97706] font-semibold uppercase mb-2">
                          Hawkins Classic 3L Pressure Cooker Acoustics & Venting
                        </div>
                        <p className="text-xs sm:text-sm text-[#8E95A2] leading-relaxed mb-4">
                          {BIOPHYSICAL_SOLUTION.cookerThermodynamics.whistleDynamics}
                        </p>
                        <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#1E232E]">
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">OPERATING PRESSURE</div>
                            <div className="text-sm font-semibold text-[#E6E8EC] tabular-nums">15 psi (103.4 kPa g)</div>
                            <div className="text-[10px] text-[#8E95A2]">T_sat = 121.1°C (394.3 K)</div>
                          </div>
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">VENT VALVE SPEC</div>
                            <div className="text-sm font-semibold text-[#D97706] tabular-nums">48.5g Deadweight</div>
                            <div className="text-[10px] text-[#8E95A2]">Throat Dia: 2.1 mm (1.8g steam/chuff)</div>
                          </div>
                        </div>
                      </div>
                    )}

                    {activeMechanism === 'drying' && (
                      <div>
                        <div className="font-mono text-xs text-[#D97706] font-semibold uppercase mb-2">
                          Viscoelastic Two-Stage Tempered Fluid Bed Drying
                        </div>
                        <p className="text-xs sm:text-sm text-[#8E95A2] leading-relaxed mb-4">
                          {BIOPHYSICAL_SOLUTION.dryingMechanics.twoStageSchedule}
                        </p>
                        <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#1E232E]">
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">PEAK TENSILE HOOP STRESS</div>
                            <div className="text-sm font-semibold text-[#10B981] tabular-nums">0.40 MPa</div>
                            <div className="text-[10px] text-[#8E95A2]">0.431x Yield Strength (1.65 MPa)</div>
                          </div>
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">BROKEN COTYLEDON FINES</div>
                            <div className="text-sm font-semibold text-[#10B981] tabular-nums">&lt;0.35% Fines</div>
                            <div className="text-[10px] text-[#8E95A2]">Commercial Limit: 1.50%</div>
                          </div>
                        </div>
                      </div>
                    )}

                    {activeMechanism === 'flavor' && (
                      <div>
                        <div className="font-mono text-xs text-[#D97706] font-semibold uppercase mb-2">
                          Lipoxygenase Inactivation & Volatile Headspace Kinetics
                        </div>
                        <p className="text-xs sm:text-sm text-[#8E95A2] leading-relaxed mb-4">
                          Steeping at pH 5.20 acidic buffer holding denatures 86.4% of endogenous lipoxygenase (LOX), 
                          permanently arresting hexanal formation. High-pressure 12s counter-current deluge rinse strips 
                          98.7% of superficial salt film.
                        </p>
                        <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#1E232E]">
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">HEADSPACE HEXANAL</div>
                            <div className="text-sm font-semibold text-[#10B981] tabular-nums">0.025 ppm</div>
                            <div className="text-[10px] text-[#8E95A2]">OAV = 0.84 &lt; 1.0 (Untreated: 0.380 ppm)</div>
                          </div>
                          <div className="p-2.5 bg-[#111319] border border-[#1E232E] rounded-xs">
                            <div className="text-[10px] text-[#5E6573]">RETAINED PHOSPHATE</div>
                            <div className="text-sm font-semibold text-[#10B981] tabular-nums">142 mg / kg</div>
                            <div className="text-[10px] text-[#8E95A2]">35.2x Margin Below FSSAI 5,000 mg/kg</div>
                          </div>
                        </div>
                      </div>
                    )}

                  </div>
                </div>

                <div className="font-mono text-[11px] text-[#5E6573] pt-4 border-t border-[#1E232E]">
                  Validated via ISO 4120 3-AFC Triangular Sensory Panel (N=72, p = 0.420)
                </div>
              </div>

            </div>
          </div>
        )}

        {/* VIEW B: Forensic Industry Failure Analysis */}
        {activeView === 'viewB' && (
          <div className="p-6 sm:p-8 bg-[#0C0E12]">
            <div className="flex justify-between items-center mb-4">
              <span className="font-mono text-xs text-[#5E6573] uppercase tracking-wider">
                5-ROW FORENSIC FAILURE REGISTER & FIRST-PRINCIPLES COUNTERMEASURES
              </span>
              <span className="font-mono text-xs px-2 py-0.5 bg-[#151821] text-[#10B981] border border-[#232836] rounded-xs">
                5 / 5 DEFECTS ELIMINATED
              </span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#1E232E]">
                <thead>
                  <tr className="bg-[#111319] border-b border-[#1E232E] text-[#5E6573]">
                    <th className="p-3 w-1/5">Industry Failure Mode</th>
                    <th className="p-3 w-1/4">Chemical & Physical Mechanism</th>
                    <th className="p-3 w-1/4">Observed Commercial Defect</th>
                    <th className="p-3 w-1/4">FinnoaQ Engineered Solution</th>
                    <th className="p-3 text-right">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#1E232E]">
                  {FORENSIC_FAILURE_ANALYSIS.map((row, idx) => (
                    <tr key={idx} className="hover:bg-[#111319] transition-colors">
                      <td className="p-3 text-[#E6E8EC] font-semibold">{row.failureMode}</td>
                      <td className="p-3 text-[#8E95A2] font-sans text-xs">{row.chemicalMechanism}</td>
                      <td className="p-3 text-[#EF4444] font-sans text-xs">{row.observedDefect}</td>
                      <td className="p-3 text-[#10B981] font-sans text-xs">{row.finnoaqSolution}</td>
                      <td className="p-3 text-right">
                        <span className="px-2 py-0.5 bg-[#151821] text-[#10B981] border border-[#232836] rounded-xs text-[10px]">
                          {row.status}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="mt-4 p-4 bg-[#111319] border border-[#1E232E] rounded-xs flex flex-wrap justify-between items-center gap-2 font-mono text-xs text-[#5E6573]">
              <span>FAIL-0001 to FAIL-0025 Verified Closed in Governance Ledger</span>
              <span>Tested under ISO 11136:2014 & FSSAI Guidelines</span>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}
