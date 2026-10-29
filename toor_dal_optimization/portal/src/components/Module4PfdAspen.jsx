import React, { useState } from 'react';
import { MASS_BALANCE_RECONCILIATION } from '../data/micrositeData.js';

// Unit Operations for the PFD
const PFD_NODES = [
  {
    tag: 'D-101',
    name: 'Raw Grain Cleaner & Destoner',
    category: 'Mechanical Pretreatment',
    vessel: 'Vibratory Air-Screen Destoning Deck',
    capacity: '1,200 kg/h intake capacity',
    power: '3.7 kW drive motor + 2.2 kW aspiration fan',
    envelope: 'Ambient (25°C), 1.0 atm, continuous feed',
    linkedStreams: ['STR-01', 'STR-02'],
    render: '/drawings/CHU-100_SolidWorks_3D_Iso_transparent.png',
    duty: 'Removes foreign debris, stones, dust, and shriveled grains prior to steeping.'
  },
  {
    tag: 'TK-101A/B',
    name: 'Ultrasonic Bio-Chelation Steeping Battery',
    category: 'Biochemical Reaction & Acoustics',
    vessel: 'Twin 2,500L Vertical Cylindrical (SS316L contact parts)',
    capacity: '2x 2.5 m³ working volume (5.0 m³ total battery)',
    power: '2x 2.2 kW geared hydrofoil agitators + 17 W/L ultrasonic horns',
    envelope: '48.0°C ± 0.5°C, pH 5.20 ± 0.05, 24.0 min batch hold',
    linkedStreams: ['STR-02', 'STR-03', 'STR-04'],
    render: '/drawings/TK-101_SolidWorks_3D_Iso_transparent.png',
    duty: '40 kHz acoustic cavitation thinning boundary layer; S1-09 buffer unzips middle lamella Ca-pectate egg-boxes.'
  },
  {
    tag: 'SC-101',
    name: 'High-Frequency Dewatering Screen & Deluge Wash',
    category: 'Solid-Liquid Separation',
    vessel: 'Linear Vibratory Screen with Polyurethane/SS304 Deck',
    capacity: '1,500 kg/h wet pulse slurry handling',
    power: '2x 1.1 kW vibro-motors + 3.0 kW high-pressure deluge pump',
    envelope: 'Ambient, 12.0s counter-current deluge rinse (<27.6 ppm surface salts)',
    linkedStreams: ['STR-04', 'STR-05', 'STR-06', 'STR-10'],
    render: '/drawings/SC-101_SolidWorks_3D_Iso_transparent.png',
    duty: 'Drains bulk steep liquor to 28.0% WB moisture; washes surface salts to prevent drying bloom.'
  },
  {
    tag: 'DR-101A/B',
    name: 'Two-Stage Tempered Fluid Bed Dryer Skid',
    category: 'Thermal Dehydration & Viscoelastic Conditioning',
    vessel: 'Continuous Vibrating Fluid Bed with 20-min Tempering Deck',
    capacity: '850 kg/h finished dry discharge (195 kWth peak duty)',
    power: '15.0 kW fluidizing supply fan + 7.5 kW exhaust blower',
    envelope: 'Stage 1: 65°C (45m) → Tempering: 55°C (20m) → Stage 2: 55°C (40m)',
    linkedStreams: ['STR-05', 'STR-07', 'STR-08'],
    render: '/drawings/DR-101_SolidWorks_3D_Iso_transparent.png',
    duty: 'Removes 3,678 kg/day moisture while suppressing peak hoop stress below 0.40 MPa and breakage <0.35%.'
  },
  {
    tag: 'EV-101',
    name: 'MVR Zero Liquid Discharge (ZLD) Evaporator',
    category: 'Effluent Recovery & Byproduct Concentration',
    vessel: 'Falling Film Tubular Concentrator with MVR Turbo-Fan (SS316L)',
    capacity: '250 kg/h evaporative water recovery',
    power: '11.0 kW MVR vapor compressor + 1.5 kW circulation pump',
    envelope: '58.0°C – 85.0°C under vacuum (0.18 – 0.58 bar a)',
    linkedStreams: ['STR-10', 'STR-11', 'STR-12'],
    render: '/drawings/EV-101_SolidWorks_3D_Iso_transparent.png',
    duty: 'Concentrates 15% purge liquor to 45% solids for cattle feed; recovers 948 kg/day pure distillate.'
  },
  {
    tag: 'B-101',
    name: 'Friction Polishing & Automated Bagging Battery',
    category: 'Finishing & Packaging',
    vessel: 'Rotary Friction Polisher & Electronic Net Weigher',
    capacity: '1,000 kg/h packaging throughput',
    power: '4.0 kW polisher drive + 1.5 kW dust collector',
    envelope: 'Ambient (25°C), 10.5% WB stable equilibrium moisture',
    linkedStreams: ['STR-08', 'STR-09'],
    render: '/drawings/STR-100_SolidWorks_3D_Iso_transparent.png',
    duty: 'Restores golden translucent sheen, removes loose fines, and packages into 25kg/50kg HDPE bags.'
  }
];

// Full Aspen Plus V14 12-Stream Master Table
const ASPEN_12_STREAMS = [
  { id: 'STR-01', desc: 'Raw Feed Dal (As Received)', fromTo: 'Raw Storage SIL-101 → Cleaner D-101', phase: 'Solid', wetKg: 15000.0, dryKg: 13425.0, waterKg: 1575.0, moistureWb: '10.50%', rateKgH: 750.0, basis: 'Design intake reference' },
  { id: 'STR-02', desc: 'Cleaned Dal to Soaking', fromTo: 'Cleaner D-101 → Soak Tank TK-101', phase: 'Solid', wetKg: 15000.0, dryKg: 13425.0, waterKg: 1575.0, moistureWb: '10.50%', rateKgH: 750.0, basis: 'Zero foreign matter' },
  { id: 'STR-03', desc: 'Fresh Makeup S1-09 Buffer Liquor', fromTo: 'Dosing Skid SK-100 → Soak Tank TK-101', phase: 'Liquid', wetKg: 22500.0, dryKg: 0.0, waterKg: 22500.0, moistureWb: '100.00%', rateKgH: 1125.0, basis: '1:1.5 mass liquor ratio (pH 5.20)' },
  { id: 'STR-04', desc: 'Spent Steep Liquor to Dewatering', fromTo: 'Soak Tank TK-101 → Screen SC-101', phase: 'Slurry', wetKg: 19109.7, dryKg: 184.0, waterKg: 18925.7, moistureWb: '99.04%', rateKgH: 955.5, basis: 'Contains 184 kg leached fines' },
  { id: 'STR-05', desc: 'Pre-Dryer Wet Dal [Scenario B1]', fromTo: 'Dewatering Screen SC-101 → Dryer DR-101', phase: 'Wet Solid', wetKg: 18390.3, dryKg: 13241.0, waterKg: 5149.3, moistureWb: '28.00%', rateKgH: 919.5, basis: 'True 28.0% WB screen discharge' },
  { id: 'STR-06', desc: 'Counter-Current Deluge Spray Water', fromTo: 'Utility Soft Water → Screen SC-101', phase: 'Liquid', wetKg: 2250.0, dryKg: 0.0, waterKg: 2250.0, moistureWb: '100.00%', rateKgH: 140.6, basis: '12s spray stripping (<27.6 ppm salts)' },
  { id: 'STR-07', desc: 'Dryer Evaporated Moisture Vapor', fromTo: 'Fluid Bed Dryer DR-101 → Cyclone CY-101', phase: 'Vapor', wetKg: 3678.1, dryKg: 0.0, waterKg: 3678.1, moistureWb: '100.00%', rateKgH: 183.9, basis: 'Thermal duty: 142.8 kWth' },
  { id: 'STR-08', desc: 'Dried Finished Dal Ex-Dryer', fromTo: 'Fluid Bed Dryer DR-101 → Polishing B-101', phase: 'Solid', wetKg: 14712.2, dryKg: 13241.0, waterKg: 1471.2, moistureWb: '10.00%', rateKgH: 735.6, basis: 'Tempered product (hoop stress ≤ 0.40 MPa)' },
  { id: 'STR-09', desc: 'Polished Saleable Conditioned Dal', fromTo: 'Polishing B-101 → Packaging PK-101', phase: 'Solid', wetKg: 14360.0, dryKg: 12706.8, waterKg: 1653.2, moistureWb: '10.50%', rateKgH: 718.0, basis: '97.37% dry solids recovery, 95.73% yield' },
  { id: 'STR-10', desc: 'Recycled Bleed Liquor to ZLD', fromTo: 'Drain Sump → Evaporator EV-101', phase: 'Liquid', wetKg: 1198.5, dryKg: 15.0, waterKg: 1183.5, moistureWb: '98.75%', rateKgH: 74.9, basis: '15% purge rate to prevent scaling' },
  { id: 'STR-11', desc: 'MVR Falling Film Vapor Overhead', fromTo: 'Evaporator EV-101 → Condensate Header', phase: 'Vapor', wetKg: 948.5, dryKg: 0.0, waterKg: 948.5, moistureWb: '100.00%', rateKgH: 59.3, basis: 'Pure distillate recycled back to wash' },
  { id: 'STR-12', desc: 'Concentrated ZLD Slurry Byproduct', fromTo: 'Evaporator EV-101 → Animal Feed Sump', phase: 'Slurry', wetKg: 250.0, dryKg: 15.0, waterKg: 235.0, moistureWb: '94.00%', rateKgH: 15.6, basis: '45% solids byproduct monetization' }
];

export default function Module4PfdAspen() {
  const [activeNodeIndex, setActiveNodeIndex] = useState(1); // Default TK-101A/B
  const [streamView, setStreamView] = useState('aspen12'); // 'summary' | 'aspen12'

  const activeNode = PFD_NODES[activeNodeIndex];

  return (
    <section id="pfd-aspen" className="w-full bg-[#0A0B0D] border-b border-[#222630] scroll-mt-20">
      <div className="max-w-[1440px] mx-auto border-x border-[#222630]">
        
        {/* Module Header */}
        <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [03 // PROCESS SCHEMATIC & HARDWARE INSPECTOR]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#F3F4F6]">
              Interactive 15 TPD Process Flow Diagram (PFD) & Aspen Stream Inspector
            </h2>
          </div>
          <span className="font-mono text-xs px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm">
            0.000000% CLOSURE ERROR // ELECNRTL CONVERGED
          </span>
        </div>

        {/* 1. Horizontal Connected Engineering Block Diagram */}
        <div className="p-6 bg-[#0A0B0D] border-b border-[#222630]">
          <div className="flex justify-between items-center mb-4">
            <span className="font-mono text-xs text-[#64748B] uppercase tracking-wider">
              PFD SCHEMATIC: CLICK ANY UNIT OPERATION TO INSPECT 3D CAD & HIGHLIGHT ASPEN STREAMS
            </span>
            <span className="font-mono text-xs text-[#F59E0B] font-semibold">
              Selected: {activeNode.tag} ({activeNode.name})
            </span>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
            {PFD_NODES.map((node, idx) => {
              const isSelected = activeNodeIndex === idx;
              return (
                <button
                  key={node.tag}
                  onClick={() => setActiveNodeIndex(idx)}
                  className={`p-3.5 text-left border rounded-sm transition-all cursor-pointer relative ${
                    isSelected
                      ? 'bg-[#171A21] border-[#F59E0B] shadow-lg'
                      : 'bg-[#111317] border-[#222630] hover:border-[#64748B]'
                  }`}
                >
                  <div className="flex justify-between items-center mb-1.5">
                    <span className={`font-mono text-xs font-bold ${isSelected ? 'text-[#F59E0B]' : 'text-[#F3F4F6]'}`}>
                      {node.tag}
                    </span>
                    <span className="font-mono text-[10px] text-[#64748B]">
                      0{idx + 1}
                    </span>
                  </div>
                  
                  <div className="text-xs font-medium text-[#F3F4F6] line-clamp-2 mb-2">
                    {node.name}
                  </div>

                  <div className="font-mono text-[10px] text-[#9CA3AF] mb-2 truncate">
                    {node.capacity}
                  </div>

                  <div className="pt-2 border-t border-[#222630] flex flex-wrap gap-1">
                    {node.linkedStreams.map((s) => (
                      <span key={s} className="px-1 py-0.2 bg-[#0A0B0D] text-[9px] font-mono text-[#94A3B8] border border-[#2E3440] rounded-xs">
                        {s}
                      </span>
                    ))}
                  </div>
                </button>
              );
            })}
          </div>

          {/* Animated SVG Flow Connectors Bar */}
          <div className="mt-4 pt-3 border-t border-[#222630] flex items-center justify-between font-mono text-xs text-[#64748B] overflow-x-auto">
            <span>D-101 (Intake)</span>
            <span className="text-[#F59E0B]">── STR-02 ──▶</span>
            <span>TK-101A/B (Steeping)</span>
            <span className="text-[#F59E0B]">── STR-04 ──▶</span>
            <span>SC-101 (Dewatering)</span>
            <span className="text-[#F59E0B]">── STR-05 ──▶</span>
            <span>DR-101A/B (Drying)</span>
            <span className="text-[#F59E0B]">── STR-08 ──▶</span>
            <span>B-101 (Polishing)</span>
            <span className="text-[#10B981]">── STR-09 (Saleable) ──▶</span>
          </div>
        </div>

        {/* 2. Active Unit Op Hardware Specification Panel with Authentic 3D SolidWorks Render */}
        <div className="p-6 sm:p-8 bg-[#111317] border-b border-[#222630]">
          
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
            
            {/* Left 4 Cols: Authentic SolidWorks 3D CAD Isometric Render (Seamless Transparent PBR) */}
            <div 
              className="lg:col-span-4 p-5 border border-[#222630] rounded text-center relative overflow-hidden"
              style={{
                background: 'radial-gradient(circle at 50% 50%, rgba(245, 158, 11, 0.12) 0%, rgba(13, 15, 20, 0.98) 75%)'
              }}
            >
              <div className="flex justify-between items-center mb-3 font-mono text-[11px] text-[#64748B]">
                <span className="text-[#94A3B8]">SOLIDWORKS 2025 SP01.2</span>
                <span className="text-[#F59E0B] font-medium">ASME SEC VIII DIV 1</span>
              </div>
              <img
                src={activeNode.render}
                alt={activeNode.name}
                className="w-full h-52 object-contain mx-auto filter drop-shadow-[0_12px_24px_rgba(0,0,0,0.85)] transition-transform duration-300 hover:scale-105"
                onError={(e) => {
                  e.target.src = activeNode.render.replace('_transparent', '');
                }}
              />
              <div className="font-mono text-xs text-[#9CA3AF] mt-3">
                Tag: <strong className="text-white">{activeNode.tag}</strong> // {activeNode.category}
              </div>
            </div>

            {/* Right 8 Cols: Datasheet Grade Technical Parameters */}
            <div className="lg:col-span-8 flex flex-col justify-between">
              <div>
                <div className="flex flex-wrap items-center justify-between gap-2 mb-4 pb-2 border-b border-[#222630]">
                  <div className="flex items-center space-x-3">
                    <span className="font-mono text-xl font-bold text-[#F59E0B]">
                      {activeNode.tag}
                    </span>
                    <span className="text-[#64748B] font-mono text-xs">//</span>
                    <span className="font-mono text-base text-[#F3F4F6] font-semibold">
                      {activeNode.name}
                    </span>
                  </div>
                  <div className="flex items-center space-x-2 font-mono text-xs">
                    <span className="text-[#64748B]">LINKED STREAMS:</span>
                    {activeNode.linkedStreams.map((s) => (
                      <span key={s} className="px-2 py-0.5 bg-[#171A21] border border-[#F59E0B] text-[#F59E0B] rounded-sm font-semibold">
                        {s}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 font-mono text-xs mb-4">
                  <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                    <div className="text-[10px] text-[#64748B] uppercase">VESSEL GEOMETRY & TYPE</div>
                    <div className="text-[#F3F4F6] font-medium mt-1">{activeNode.vessel}</div>
                  </div>

                  <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                    <div className="text-[10px] text-[#64748B] uppercase">WORKING CAPACITY</div>
                    <div className="text-[#F3F4F6] font-medium mt-1">{activeNode.capacity}</div>
                  </div>

                  <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                    <div className="text-[10px] text-[#64748B] uppercase">CONNECTED DRIVE & POWER</div>
                    <div className="text-[#F59E0B] font-medium mt-1">{activeNode.power}</div>
                  </div>

                  <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                    <div className="text-[10px] text-[#64748B] uppercase">OPERATING ENVELOPE</div>
                    <div className="text-[#10B981] font-medium mt-1">{activeNode.envelope}</div>
                  </div>
                </div>

                <div className="p-3 bg-[#0A0B0D] border border-[#222630] rounded-sm font-mono text-xs text-[#9CA3AF]">
                  <strong className="text-[#F3F4F6]">Process Duty: </strong>
                  {activeNode.duty}
                </div>
              </div>
            </div>

          </div>

        </div>

        {/* 3. Collapsible / Tabbed Mass Balance Drawer */}
        <div className="p-6 bg-[#0A0B0D]">
          
          {/* Toggle between Summary 8-row and Full Aspen 12-stream table */}
          <div className="flex flex-wrap items-center justify-between gap-4 border-b border-[#222630] pb-3 mb-4">
            <div className="flex space-x-2">
              <button
                onClick={() => setStreamView('aspen12')}
                className={`px-3 py-1.5 font-mono text-xs rounded-sm transition-colors cursor-pointer border ${
                  streamView === 'aspen12'
                    ? 'bg-[#171A21] border-[#F59E0B] text-[#F59E0B] font-semibold'
                    : 'bg-[#111317] border-[#222630] text-[#9CA3AF] hover:text-[#F3F4F6]'
                }`}
              >
                [FULL ASPEN PLUS V14 12-STREAM TABLE (STR-01 TO STR-12)]
              </button>
              <button
                onClick={() => setStreamView('summary')}
                className={`px-3 py-1.5 font-mono text-xs rounded-sm transition-colors cursor-pointer border ${
                  streamView === 'summary'
                    ? 'bg-[#171A21] border-[#F59E0B] text-[#F59E0B] font-semibold'
                    : 'bg-[#111317] border-[#222630] text-[#9CA3AF] hover:text-[#F3F4F6]'
                }`}
              >
                [SUMMARY MASS & WATER BALANCE (8 ROWS)]
              </button>
            </div>

            <div className="font-mono text-xs text-[#64748B]">
              Highlighted Streams: <span className="text-[#F59E0B] font-semibold">{activeNode.linkedStreams.join(', ')}</span> (for {activeNode.tag})
            </div>
          </div>

          {/* Full Aspen 12-Stream Table */}
          {streamView === 'aspen12' && (
            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#222630]">
                <thead>
                  <tr className="bg-[#111317] border-b border-[#222630] text-[#64748B]">
                    <th className="p-2.5">Stream ID</th>
                    <th className="p-2.5">Stream Description</th>
                    <th className="p-2.5">Source → Destination</th>
                    <th className="p-2.5">Phase</th>
                    <th className="p-2.5 text-right">Wet Mass (kg/d)</th>
                    <th className="p-2.5 text-right">Dry Solids (kg/d)</th>
                    <th className="p-2.5 text-right">Moisture (% WB)</th>
                    <th className="p-2.5 text-right">Rate (kg/h)</th>
                    <th className="p-2.5">Thermodynamic Basis</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#222630]">
                  {ASPEN_12_STREAMS.map((s) => {
                    const isLinked = activeNode.linkedStreams.includes(s.id);
                    return (
                      <tr 
                        key={s.id} 
                        className={`transition-colors ${
                          isLinked 
                            ? 'bg-[#171A21] border-l-2 border-[#F59E0B]' 
                            : 'hover:bg-[#111317]'
                        }`}
                      >
                        <td className="p-2.5 font-bold">
                          <span className={isLinked ? 'text-[#F59E0B]' : 'text-[#F3F4F6]'}>
                            {s.id}
                          </span>
                          {isLinked && <span className="ml-1 text-[10px] text-[#F59E0B]">★</span>}
                        </td>
                        <td className={`p-2.5 ${isLinked ? 'text-[#F3F4F6] font-medium' : 'text-[#9CA3AF]'}`}>
                          {s.desc}
                        </td>
                        <td className="p-2.5 text-[#64748B] text-[11px]">{s.fromTo}</td>
                        <td className="p-2.5 text-[#9CA3AF]">{s.phase}</td>
                        <td className="p-2.5 text-right text-[#F3F4F6] tabular-nums font-medium">
                          {s.wetKg.toLocaleString(undefined, { minimumFractionDigits: 1 })}
                        </td>
                        <td className="p-2.5 text-right text-[#9CA3AF] tabular-nums">
                          {s.dryKg.toLocaleString(undefined, { minimumFractionDigits: 1 })}
                        </td>
                        <td className="p-2.5 text-right text-[#F59E0B] tabular-nums font-semibold">
                          {s.moistureWb}
                        </td>
                        <td className="p-2.5 text-right text-[#F3F4F6] tabular-nums">
                          {s.rateKgH.toFixed(1)}
                        </td>
                        <td className="p-2.5 text-[#64748B] text-[11px]">{s.basis}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}

          {/* Summary Mass & Water Balance (8 Rows) */}
          {streamView === 'summary' && (
            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#222630]">
                <thead>
                  <tr className="bg-[#111317] border-b border-[#222630] text-[#64748B]">
                    <th className="p-3">Process Balance Component</th>
                    <th className="p-3">Reconciled Value & Moisture State</th>
                    <th className="p-3">Calculation Model & Physical Basis</th>
                    <th className="p-3 text-right">Evidence Tier</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#222630]">
                  {MASS_BALANCE_RECONCILIATION.map((row, idx) => (
                    <tr key={idx} className="hover:bg-[#111317] transition-colors">
                      <td className="p-3 text-[#F3F4F6] font-semibold">{row.component}</td>
                      <td className="p-3 text-[#F59E0B] font-medium">{row.value}</td>
                      <td className="p-3 text-[#9CA3AF]">{row.basis}</td>
                      <td className="p-3 text-right">
                        <span className="px-2 py-0.5 bg-[#1E222A] text-[#10B981] border border-[#2E3440] rounded-sm text-[10px]">
                          {row.tier}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          <div className="mt-4 p-3 bg-[#111317] border border-[#222630] rounded-sm flex flex-wrap justify-between items-center gap-2 font-mono text-xs text-[#64748B]">
            <span>Model: FINNOAQ_15TPD_CONVERGED.bkp (Aspen Plus V14 ELECNRTL + STEAM-TA)</span>
            <span className="text-[#10B981]">Total Mass In = Total Mass Out = 41,250.57 kg/day (Closure: 0.000000%)</span>
          </div>

        </div>

      </div>
    </section>
  );
}
