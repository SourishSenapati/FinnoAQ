import React, { useState } from 'react';
import { BIOPHYSICAL_SOLUTION, FORENSIC_FAILURE_ANALYSIS } from '../data/micrositeData.js';

export default function Module3Biophysics() {
  const [activeView, setActiveView] = useState('viewA'); // 'viewA' | 'viewB'
  
  // View A: Mechanism Selector
  const [activeMechanism, setActiveMechanism] = useState('pathology');
  
  // Interactive Time Scrubber for Kinetics Curve (0 to 30 min)
  const [timeMin, setTimeMin] = useState(24);

  // Kinetic Calculations based on time:
  // Ca2+ extraction = 41.8% * (1 - exp(-time / 10.5)) / (1 - exp(-24 / 10.5))
  // Shear force drops from 26.4 N to 15.2 N
  const caExtraction = +(41.8 * (1 - Math.exp(-timeMin / 10.5)) / (1 - Math.exp(-24 / 10.5))).toFixed(1);
  const shearForce = +(26.4 - ((26.4 - 15.2) * (timeMin / 24))).toFixed(1);
  const boundaryLayerUm = timeMin >= 2 ? 8 : 42;
  const whistleCount = shearForce <= 18.0 ? '2 Whistles (7.0 min)' : shearForce <= 22.0 ? '4 Whistles (14.0 min)' : '8+ Whistles (HTC Failure)';

  return (
    <section id="biophysics" className="w-full bg-[#0A0B0D] border-b border-[#222630]">
      <div className="max-w-[1440px] mx-auto border-x border-[#222630]">
        
        {/* Module Header with 2-View Toggle */}
        <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [02 // BIOPHYSICS & FAILURE FORENSICS]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#F3F4F6]">
              Interactive Biophysics & Failure Forensics Workbench
            </h2>
          </div>

          {/* 2-View Interactive Segmented Toggle */}
          <div className="flex items-center bg-[#0A0B0D] p-1 border border-[#222630] rounded-sm">
            <button
              onClick={() => setActiveView('viewA')}
              className={`px-3 py-1.5 font-mono text-xs rounded-sm transition-colors cursor-pointer ${
                activeView === 'viewA'
                  ? 'bg-[#171A21] text-[#F59E0B] border border-[#F59E0B] font-semibold'
                  : 'text-[#9CA3AF] hover:text-[#F3F4F6] border border-transparent'
              }`}
            >
              [View A: S1-09 Chelation Kinetics & Physics]
            </button>
            <button
              onClick={() => setActiveView('viewB')}
              className={`px-3 py-1.5 font-mono text-xs rounded-sm transition-colors cursor-pointer ${
                activeView === 'viewB'
                  ? 'bg-[#171A21] text-[#F59E0B] border border-[#F59E0B] font-semibold'
                  : 'text-[#9CA3AF] hover:text-[#F3F4F6] border border-transparent'
              }`}
            >
              [View B: Forensic Industry Failure Analysis]
            </button>
          </div>
        </div>

        {/* VIEW A: S1-09 Chelation Kinetics & Physics */}
        {activeView === 'viewA' && (
          <div className="grid grid-cols-1 lg:grid-cols-12 border-b border-[#222630]">
            
            {/* Left 6 Columns: Interactive 24-Minute Kinetic Curve & Scrubber */}
            <div className="lg:col-span-6 p-6 sm:p-8 bg-[#0A0B0D] border-b lg:border-b-0 lg:border-r border-[#222630] flex flex-col justify-between">
              <div>
                <div className="flex justify-between items-center mb-3">
                  <span className="font-mono text-xs text-[#64748B] uppercase tracking-wider">
                    24-MIN CALCIUM EXTRACTION & TEXTURE KINETICS
                  </span>
                  <span className="font-mono text-xs text-[#10B981]">
                    T = 48.0°C // 17 W/L UAE
                  </span>
                </div>

                {/* SVG Kinetics Chart */}
                <div className="p-4 bg-[#111317] border border-[#222630] rounded-sm mb-4">
                  <svg viewBox="0 0 400 200" className="w-full h-48 overflow-visible">
                    {/* Grid Lines */}
                    <line x1="40" y1="20" x2="380" y2="20" stroke="#222630" strokeDasharray="2,2" />
                    <line x1="40" y1="60" x2="380" y2="60" stroke="#222630" strokeDasharray="2,2" />
                    <line x1="40" y1="100" x2="380" y2="100" stroke="#222630" strokeDasharray="2,2" />
                    <line x1="40" y1="140" x2="380" y2="140" stroke="#222630" strokeDasharray="2,2" />
                    <line x1="40" y1="170" x2="380" y2="170" stroke="#222630" />

                    {/* 18.0 N Threshold Line */}
                    <line x1="40" y1="120" x2="380" y2="120" stroke="#F59E0B" strokeDasharray="4,4" strokeWidth="1.5" />
                    <text x="375" y="115" fill="#F59E0B" fontSize="9" textAnchor="end" fontFamily="monospace">
                      18.0 N (2-Whistle Tenderness Limit)
                    </text>

                    {/* Curve 1: Calcium Extraction % (Amber) */}
                    <path
                      d="M 40 170 Q 120 70 380 40"
                      fill="none"
                      stroke="#F59E0B"
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
                          <line x1={xPos} y1="15" x2={xPos} y2="175" stroke="#F3F4F6" strokeWidth="1" strokeDasharray="2,2" />
                          <circle cx={xPos} cy={170 - (caExtraction / 50) * 150} r="4" fill="#F59E0B" stroke="#0A0B0D" strokeWidth="2" />
                          <circle cx={xPos} cy={30 + ((26.4 - shearForce) / 15) * 115} r="4" fill="#10B981" stroke="#0A0B0D" strokeWidth="2" />
                        </g>
                      );
                    })()}

                    {/* Axis Labels */}
                    <text x="40" y="185" fill="#64748B" fontSize="9" fontFamily="monospace">0m</text>
                    <text x="153" y="185" fill="#64748B" fontSize="9" fontFamily="monospace">10m</text>
                    <text x="312" y="185" fill="#F59E0B" fontSize="9" fontWeight="bold" fontFamily="monospace">24m [Optimum]</text>
                    <text x="380" y="185" fill="#64748B" fontSize="9" textAnchor="end" fontFamily="monospace">30m</text>
                  </svg>

                  <div className="flex justify-between items-center text-[11px] font-mono mt-2 pt-2 border-t border-[#222630]">
                    <div className="flex items-center space-x-2">
                      <span className="w-2.5 h-2.5 bg-[#F59E0B] inline-block rounded-xs"></span>
                      <span className="text-[#9CA3AF]">Core Ca2+ Displaced (%): <strong className="text-[#F59E0B]">{caExtraction}%</strong></span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <span className="w-2.5 h-2.5 bg-[#10B981] inline-block rounded-xs"></span>
                      <span className="text-[#9CA3AF]">WB Shear Force: <strong className="text-[#10B981]">{shearForce} N</strong></span>
                    </div>
                  </div>
                </div>

                {/* Interactive Time Slider */}
                <div className="p-4 bg-[#111317] border border-[#222630] rounded-sm mb-4">
                  <div className="flex justify-between items-center mb-2 font-mono text-xs">
                    <span className="text-[#9CA3AF]">Interactive Steeping Duration Scrubber:</span>
                    <span className="text-[#F59E0B] font-semibold text-sm tabular-nums">{timeMin} Minutes</span>
                  </div>
                  <input
                    type="range"
                    min="0"
                    max="30"
                    step="1"
                    value={timeMin}
                    onChange={(e) => setTimeMin(Number(e.target.value))}
                    className="w-full accent-[#F59E0B] cursor-pointer"
                  />
                  <div className="flex justify-between font-mono text-[10px] text-[#64748B] mt-1">
                    <span>0m (Raw Dry)</span>
                    <span>12m (Superficial)</span>
                    <span className="text-[#F59E0B]">24m (Core Extraction)</span>
                    <span>30m (Over-leach)</span>
                  </div>
                </div>

                {/* Real-Time Live Readout Metrics */}
                <div className="grid grid-cols-2 gap-2 font-mono text-xs">
                  <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm">
                    <div className="text-[10px] text-[#64748B]">BOUNDARY LAYER THICKNESS</div>
                    <div className="text-base font-semibold text-[#F3F4F6] my-0.5 tabular-nums">
                      {boundaryLayerUm} μm
                    </div>
                    <div className="text-[10px] text-[#10B981]">
                      {timeMin >= 2 ? 'Ultrasound microstreaming active' : 'Static liquid boundary'}
                    </div>
                  </div>

                  <div className="p-3 bg-[#111317] border border-[#222630] rounded-sm">
                    <div className="text-[10px] text-[#64748B]">HAWKINS COOKER EQUIVALENT</div>
                    <div className="text-sm font-semibold text-[#F59E0B] my-0.5 tabular-nums truncate">
                      {whistleCount}
                    </div>
                    <div className="text-[10px] text-[#9CA3AF]">
                      Benchmark Desi: 3 Whistles (9.8m)
                    </div>
                  </div>
                </div>

              </div>

              <div className="font-mono text-[11px] text-[#64748B] pt-4 border-t border-[#222630]">
                Governing Equation: ∂c/∂t = ∇·(D_eff ∇c) - R_chelate // Hawkins 103.4 kPa Saturated Steam Model
              </div>
            </div>

            {/* Right 6 Columns: 5-Tab Technical Mechanism Selector */}
            <div className="lg:col-span-6 p-6 sm:p-8 bg-[#111317] flex flex-col justify-between">
              <div>
                <div className="font-mono text-xs text-[#64748B] uppercase tracking-wider mb-4">
                  BIOPHYSICAL MECHANISMS & EXPERIMENTAL PROOF
                </div>

                {/* 5 Tabs */}
                <div className="flex flex-wrap gap-1 border-b border-[#222630] pb-2 mb-4 font-mono text-xs">
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
                      className={`px-3 py-1.5 rounded-sm transition-colors cursor-pointer ${
                        activeMechanism === tab.id
                          ? 'bg-[#171A21] border border-[#F59E0B] text-[#F59E0B] font-semibold'
                          : 'bg-[#0A0B0D] border border-[#222630] text-[#9CA3AF] hover:text-[#F3F4F6]'
                      }`}
                    >
                      {tab.label}
                    </button>
                  ))}
                </div>

                {/* Tab Content Display */}
                <div className="p-5 bg-[#0A0B0D] border border-[#222630] rounded-sm min-h-[300px]">
                  
                  {activeMechanism === 'pathology' && (
                    <div>
                      <div className="font-mono text-xs text-[#F59E0B] font-semibold uppercase mb-2">
                        {BIOPHYSICAL_SOLUTION.pathology.title}
                      </div>
                      <p className="text-xs sm:text-sm text-[#9CA3AF] leading-relaxed mb-4">
                        {BIOPHYSICAL_SOLUTION.pathology.description}
                      </p>
                      <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#222630]">
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">AGED AFRICAN DAL CA-PECTATE</div>
                          <div className="text-sm font-semibold text-[#EF4444] tabular-nums">33.5 mol / m³</div>
                          <div className="text-[10px] text-[#9CA3AF]">Severe HTC Egg-Box Matrices</div>
                        </div>
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">DOMESTIC DESI BENCHMARK</div>
                          <div className="text-sm font-semibold text-[#10B981] tabular-nums">14.0 mol / m³</div>
                          <div className="text-[10px] text-[#9CA3AF]">Natural Tender Cleaving</div>
                        </div>
                      </div>
                    </div>
                  )}

                  {activeMechanism === 'stoichiometry' && (
                    <div>
                      <div className="font-mono text-xs text-[#F59E0B] font-semibold uppercase mb-2">
                        {BIOPHYSICAL_SOLUTION.formulation.code}
                      </div>
                      <div className="space-y-2 mb-4 font-mono text-xs">
                        {BIOPHYSICAL_SOLUTION.formulation.components.map((comp, idx) => (
                          <div key={idx} className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                            <div className="flex justify-between items-center mb-1">
                              <span className="text-[#F3F4F6] font-semibold">{comp.name}</span>
                              <span className="text-[#F59E0B]">{comp.molarity} ({comp.concentration})</span>
                            </div>
                            <div className="text-[#9CA3AF] text-[11px] font-sans">{comp.function}</div>
                          </div>
                        ))}
                      </div>
                      <div className="flex justify-between items-center font-mono text-xs p-2.5 bg-[#171A21] border border-[#222630] rounded-sm">
                        <span className="text-[#9CA3AF]">Equilibrium pH Envelope:</span>
                        <span className="text-[#10B981] font-semibold">{BIOPHYSICAL_SOLUTION.formulation.equilibriumPh}</span>
                      </div>
                    </div>
                  )}

                  {activeMechanism === 'acoustics' && (
                    <div>
                      <div className="font-mono text-xs text-[#F59E0B] font-semibold uppercase mb-2">
                        Hawkins Classic 3L Pressure Cooker Acoustics & Venting
                      </div>
                      <p className="text-xs sm:text-sm text-[#9CA3AF] leading-relaxed mb-4">
                        {BIOPHYSICAL_SOLUTION.cookerThermodynamics.whistleDynamics}
                      </p>
                      <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#222630]">
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">OPERATING PRESSURE</div>
                          <div className="text-sm font-semibold text-[#F3F4F6] tabular-nums">15 psi (103.4 kPa g)</div>
                          <div className="text-[10px] text-[#9CA3AF]">T_sat = 121.1°C (394.3 K)</div>
                        </div>
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">VENT VALVE SPEC</div>
                          <div className="text-sm font-semibold text-[#F59E0B] tabular-nums">48.5g Deadweight</div>
                          <div className="text-[10px] text-[#9CA3AF]">Throat Dia: 2.1 mm (1.8g steam/chuff)</div>
                        </div>
                      </div>
                    </div>
                  )}

                  {activeMechanism === 'drying' && (
                    <div>
                      <div className="font-mono text-xs text-[#F59E0B] font-semibold uppercase mb-2">
                        Viscoelastic Two-Stage Tempered Fluid Bed Drying
                      </div>
                      <p className="text-xs sm:text-sm text-[#9CA3AF] leading-relaxed mb-4">
                        {BIOPHYSICAL_SOLUTION.dryingMechanics.twoStageSchedule}
                      </p>
                      <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#222630]">
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">PEAK TENSILE HOOP STRESS</div>
                          <div className="text-sm font-semibold text-[#10B981] tabular-nums">0.40 MPa</div>
                          <div className="text-[10px] text-[#9CA3AF]">0.431x Yield Strength (1.65 MPa)</div>
                        </div>
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">BROKEN COTYLEDON FINES</div>
                          <div className="text-sm font-semibold text-[#10B981] tabular-nums">&lt;0.35% Fines</div>
                          <div className="text-[10px] text-[#9CA3AF]">Commercial Limit: 1.50%</div>
                        </div>
                      </div>
                    </div>
                  )}

                  {activeMechanism === 'flavor' && (
                    <div>
                      <div className="font-mono text-xs text-[#F59E0B] font-semibold uppercase mb-2">
                        Lipoxygenase Inactivation & Volatile Headspace Kinetics
                      </div>
                      <p className="text-xs sm:text-sm text-[#9CA3AF] leading-relaxed mb-4">
                        Steeping at pH 5.20 acidic buffer holding denatures 86.4% of endogenous lipoxygenase (LOX), 
                        permanently arresting hexanal formation. High-pressure 12s counter-current deluge rinse strips 
                        98.7% of superficial salt film.
                      </p>
                      <div className="grid grid-cols-2 gap-2 font-mono text-xs pt-3 border-t border-[#222630]">
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">HEADSPACE HEXANAL</div>
                          <div className="text-sm font-semibold text-[#10B981] tabular-nums">0.025 ppm</div>
                          <div className="text-[10px] text-[#9CA3AF]">OAV = 0.84 &lt; 1.0 (Untreated: 0.380 ppm)</div>
                        </div>
                        <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm">
                          <div className="text-[10px] text-[#64748B]">RETAINED PHOSPHATE</div>
                          <div className="text-sm font-semibold text-[#10B981] tabular-nums">142 mg / kg</div>
                          <div className="text-[10px] text-[#9CA3AF]">35.2x Margin Below FSSAI 5,000 mg/kg</div>
                        </div>
                      </div>
                    </div>
                  )}

                </div>
              </div>

              <div className="font-mono text-[11px] text-[#64748B] pt-4 border-t border-[#222630]">
                Validated via ISO 4120 3-AFC Triangular Sensory Panel (N=72, p = 0.420)
              </div>
            </div>

          </div>
        )}

        {/* VIEW B: Forensic Industry Failure Analysis */}
        {activeView === 'viewB' && (
          <div className="p-6 sm:p-8 bg-[#0A0B0D]">
            <div className="flex justify-between items-center mb-4">
              <span className="font-mono text-xs text-[#64748B] uppercase tracking-wider">
                5-ROW FORENSIC FAILURE REGISTER & FIRST-PRINCIPLES COUNTERMEASURES
              </span>
              <span className="font-mono text-xs px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm">
                5 / 5 DEFECTS ELIMINATED
              </span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#222630]">
                <thead>
                  <tr className="bg-[#111317] border-b border-[#222630] text-[#64748B]">
                    <th className="p-3 w-1/5">Industry Failure Mode</th>
                    <th className="p-3 w-1/4">Chemical & Physical Mechanism</th>
                    <th className="p-3 w-1/4">Observed Commercial Defect</th>
                    <th className="p-3 w-1/4">FinnoaQ Engineered Solution</th>
                    <th className="p-3 text-right">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#222630]">
                  {FORENSIC_FAILURE_ANALYSIS.map((row, idx) => (
                    <tr key={idx} className="hover:bg-[#111317] transition-colors">
                      <td className="p-3 text-[#F3F4F6] font-semibold">{row.failureMode}</td>
                      <td className="p-3 text-[#9CA3AF] font-sans text-xs">{row.chemicalMechanism}</td>
                      <td className="p-3 text-[#EF4444] font-sans text-xs">{row.observedDefect}</td>
                      <td className="p-3 text-[#10B981] font-sans text-xs">{row.finnoaqSolution}</td>
                      <td className="p-3 text-right">
                        <span className="px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm text-[10px]">
                          {row.status}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="mt-4 p-4 bg-[#111317] border border-[#222630] rounded-sm flex flex-wrap justify-between items-center gap-2 font-mono text-xs text-[#64748B]">
              <span>FAIL-0001 to FAIL-0025 Verified Closed in Governance Ledger</span>
              <span>Tested under ISO 11136:2014 & FSSAI Guidelines</span>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}
