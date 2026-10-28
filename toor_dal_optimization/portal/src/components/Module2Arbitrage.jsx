import React, { useState } from 'react';
import { 
  COMMERCIAL_UNIT_ECONOMICS, 
  OPEX_BREAKDOWN, 
  CAPEX_SCHEDULE, 
  FIVE_YEAR_CASH_FLOW 
} from '../data/micrositeData.js';

export default function Module2Arbitrage() {
  // Sensitivity Controls
  const [capacityTpd, setCapacityTpd] = useState(15); // 5, 15, 30
  const [mandiSpread, setMandiSpread] = useState(20); // 14, 20, 28
  const [operatingDays, setOperatingDays] = useState(300); // 200, 300, 330
  
  // Financial Drawer Tab
  const [activeTab, setActiveTab] = useState('opex'); // 'opex', 'capex', 'cashflow'
  const [showOpexPopover, setShowOpexPopover] = useState(false);

  // Dynamic Financial Calculations
  const dailyKg = capacityTpd * 1000;
  const tollingFee = mandiSpread === 20 ? 12.00 : +(mandiSpread * 0.6).toFixed(2);
  const millerLift = +(mandiSpread - tollingFee).toFixed(2);
  const opexPerKg = 6.34;
  const finnoaqMargin = +(tollingFee - opexPerKg).toFixed(2);
  const desiParity = +(85.00 + mandiSpread).toFixed(2);

  // Totals
  const dailyArbitragePoolLakhs = +((dailyKg * mandiSpread) / 100000).toFixed(2);
  const annualArbitragePoolLakhs = +((dailyKg * mandiSpread * operatingDays) / 100000).toFixed(1);

  const dailyMillerLiftLakhs = +((dailyKg * millerLift) / 100000).toFixed(2);
  const annualMillerLiftLakhs = +((dailyKg * millerLift * operatingDays) / 100000).toFixed(1);

  // EBITDA with 90% utilization factor
  const annualFinnoaqEbitdaLakhs = +((dailyKg * finnoaqMargin * operatingDays * 0.90) / 100000).toFixed(2);
  
  // Scaled CapEx based on capacity (15 TPD is ₹135.0L)
  const turnkeyCapex = capacityTpd === 5 ? 75.0 : capacityTpd === 15 ? 135.0 : 225.0;
  const paybackYears = +(turnkeyCapex / (annualFinnoaqEbitdaLakhs || 1)).toFixed(2);

  return (
    <section id="arbitrage" className="w-full bg-[#0A0B0D] border-b border-[#222630]">
      <div className="max-w-[1440px] mx-auto border-x border-[#222630]">
        
        {/* Module Header */}
        <div className="p-6 border-b border-[#222630] bg-[#111317] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-0.5 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm">
              [01 // UNIT ECONOMICS & ARBITRAGE]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#F3F4F6]">
              Unified Mandi Arbitrage & Live Mill ROI Workstation
            </h2>
          </div>
          <span className="font-mono text-xs text-[#10B981]">
            DEDUPLICATED AUTHORITATIVE MODEL // V11
          </span>
        </div>

        {/* 2-Pane Workstation: Left Controls + Right Live Output */}
        <div className="grid grid-cols-1 lg:grid-cols-12 border-b border-[#222630]">
          
          {/* Left Pane: Interactive Sensitivity Controls (5 Cols) */}
          <div className="lg:col-span-5 p-6 sm:p-8 bg-[#0A0B0D] border-b lg:border-b-0 lg:border-r border-[#222630] flex flex-col justify-between">
            <div>
              <div className="font-mono text-xs text-[#64748B] uppercase tracking-wider mb-6">
                SENSITIVITY CONTROLS & PLANT SCALING
              </div>

              {/* Control 1: Daily Capacity */}
              <div className="mb-6">
                <div className="flex justify-between items-center mb-2">
                  <label className="font-mono text-xs text-[#9CA3AF]">
                    Plant Daily Processing Capacity
                  </label>
                  <span className="font-mono text-sm font-semibold text-[#F3F4F6] tabular-nums">
                    {capacityTpd} TPD ({dailyKg.toLocaleString()} kg/day)
                  </span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[5, 15, 30].map((tpd) => (
                    <button
                      key={tpd}
                      onClick={() => setCapacityTpd(tpd)}
                      className={`py-2 px-3 font-mono text-xs rounded-sm border transition-colors cursor-pointer ${
                        capacityTpd === tpd 
                          ? 'bg-[#171A21] border-[#F59E0B] text-[#F59E0B] font-semibold' 
                          : 'bg-[#111317] border-[#222630] text-[#9CA3AF] hover:bg-[#171A21]'
                      }`}
                    >
                      {tpd} TPD {tpd === 15 ? '(Design)' : ''}
                    </button>
                  ))}
                </div>
              </div>

              {/* Control 2: Mandi Spread */}
              <div className="mb-6">
                <div className="flex justify-between items-center mb-2">
                  <label className="font-mono text-xs text-[#9CA3AF]">
                    Mandi Arbitrage Spread (Gross)
                  </label>
                  <span className="font-mono text-sm font-semibold text-[#F59E0B] tabular-nums">
                    ₹{mandiSpread.toFixed(2)} / kg
                  </span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[14, 20, 28].map((spread) => (
                    <button
                      key={spread}
                      onClick={() => setMandiSpread(spread)}
                      className={`py-2 px-3 font-mono text-xs rounded-sm border transition-colors cursor-pointer ${
                        mandiSpread === spread 
                          ? 'bg-[#171A21] border-[#F59E0B] text-[#F59E0B] font-semibold' 
                          : 'bg-[#111317] border-[#222630] text-[#9CA3AF] hover:bg-[#171A21]'
                      }`}
                    >
                      ₹{spread}/kg {spread === 20 ? '(Baseline)' : ''}
                    </button>
                  ))}
                </div>
                <div className="mt-1 font-mono text-[11px] text-[#64748B]">
                  Imported Raw: ₹85.00/kg → Desi Parity: ₹{desiParity.toFixed(2)}/kg
                </div>
              </div>

              {/* Control 3: Operating Days */}
              <div className="mb-6">
                <div className="flex justify-between items-center mb-2">
                  <label className="font-mono text-xs text-[#9CA3AF]">
                    Annual Operating Days
                  </label>
                  <span className="font-mono text-sm font-semibold text-[#F3F4F6] tabular-nums">
                    {operatingDays} Days / Year
                  </span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[200, 300, 330].map((days) => (
                    <button
                      key={days}
                      onClick={() => setOperatingDays(days)}
                      className={`py-2 px-3 font-mono text-xs rounded-sm border transition-colors cursor-pointer ${
                        operatingDays === days 
                          ? 'bg-[#171A21] border-[#F59E0B] text-[#F59E0B] font-semibold' 
                          : 'bg-[#111317] border-[#222630] text-[#9CA3AF] hover:bg-[#171A21]'
                      }`}
                    >
                      {days} Days {days === 300 ? '(Standard)' : ''}
                    </button>
                  ))}
                </div>
              </div>
            </div>

            <div className="pt-4 border-t border-[#222630] font-mono text-[11px] text-[#64748B]">
              Deterministic Cash-Flow Engine & Sensitivity Model (FNQ-MB-2026)
            </div>
          </div>

          {/* Right Pane: Live Waterfall & Output Cards (7 Cols) */}
          <div className="lg:col-span-7 p-6 sm:p-8 bg-[#111317] flex flex-col justify-between">
            <div>
              <div className="flex justify-between items-center mb-4">
                <span className="font-mono text-xs text-[#64748B] uppercase tracking-wider">
                  LIVE UNIT ECONOMICS WATERFALL (PER KG BASIS)
                </span>
                <span className="font-mono text-xs text-[#10B981]">
                  100% AUDITED VALUE CONSERVATION
                </span>
              </div>

              {/* Horizontal Waterfall Bar */}
              <div className="p-4 bg-[#0A0B0D] border border-[#222630] rounded-sm mb-6">
                <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-2 font-mono text-xs">
                  
                  {/* Base Intake */}
                  <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm flex-1 text-center">
                    <div className="text-[10px] text-[#64748B]">BASE RAW INTAKE</div>
                    <div className="text-sm font-semibold text-[#F3F4F6] tabular-nums">₹85.00</div>
                    <div className="text-[10px] text-[#9CA3AF]">Imported Grain</div>
                  </div>

                  <span className="text-[#64748B] text-center font-bold">+</span>

                  {/* OpEx with Hover Breakdown */}
                  <div 
                    onMouseEnter={() => setShowOpexPopover(true)}
                    onMouseLeave={() => setShowOpexPopover(false)}
                    className="p-2.5 bg-[#171A21] border border-[#222630] hover:border-[#F59E0B] rounded-sm flex-1 text-center cursor-help relative transition-colors"
                  >
                    <div className="text-[10px] text-[#F59E0B]">DIRECT OPEX ℹ</div>
                    <div className="text-sm font-semibold text-[#F3F4F6] tabular-nums">₹6.34</div>
                    <div className="text-[10px] text-[#9CA3AF]">85% Recycled</div>

                    {/* OpEx Popover Breakdown */}
                    {showOpexPopover && (
                      <div className="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-64 p-3 bg-[#0A0B0D] border border-[#F59E0B] rounded-sm shadow-xl z-30 text-left">
                        <div className="font-mono text-[10px] text-[#F59E0B] uppercase font-semibold mb-2">
                          Itemized Direct OpEx Breakdown:
                        </div>
                        <div className="space-y-1 font-mono text-[11px] text-[#9CA3AF]">
                          <div className="flex justify-between">
                            <span>S1-09 Reagents:</span>
                            <span className="text-[#F3F4F6]">₹3.63/kg (57%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Biomass Steam:</span>
                            <span className="text-[#F3F4F6]">₹1.12/kg (18%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Electrical Power:</span>
                            <span className="text-[#F3F4F6]">₹0.48/kg (8%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Direct Labor:</span>
                            <span className="text-[#F3F4F6]">₹0.62/kg (10%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Water, ZLD & Maint:</span>
                            <span className="text-[#F3F4F6]">₹0.49/kg (7%)</span>
                          </div>
                        </div>
                      </div>
                    )}
                  </div>

                  <span className="text-[#64748B] text-center font-bold">+</span>

                  {/* FinnoaQ Margin */}
                  <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm flex-1 text-center">
                    <div className="text-[10px] text-[#64748B]">FINNOAQ MARGIN</div>
                    <div className="text-sm font-semibold text-[#F3F4F6] tabular-nums">₹{finnoaqMargin.toFixed(2)}</div>
                    <div className="text-[10px] text-[#9CA3AF]">Tolling Fee ₹{tollingFee.toFixed(2)}</div>
                  </div>

                  <span className="text-[#64748B] text-center font-bold">+</span>

                  {/* Partner Miller Lift (Amber Highlight) */}
                  <div className="p-2.5 bg-[#171A21] border border-[#F59E0B] rounded-sm flex-1 text-center">
                    <div className="text-[10px] text-[#F59E0B] font-semibold">MILLER NET LIFT</div>
                    <div className="text-sm font-bold text-[#F59E0B] tabular-nums">+₹{millerLift.toFixed(2)}</div>
                    <div className="text-[10px] text-[#F59E0B]">Partner Profit</div>
                  </div>

                  <span className="text-[#64748B] text-center font-bold">=</span>

                  {/* Desi Parity */}
                  <div className="p-2.5 bg-[#111317] border border-[#222630] rounded-sm flex-1 text-center">
                    <div className="text-[10px] text-[#10B981]">DESI PARITY</div>
                    <div className="text-sm font-semibold text-[#10B981] tabular-nums">₹{desiParity.toFixed(2)}</div>
                    <div className="text-[10px] text-[#9CA3AF]">Market Parity</div>
                  </div>

                </div>
              </div>

              {/* 4 Live Output Cards */}
              <div className="grid grid-cols-2 gap-3 mb-4">
                
                {/* Card 1: Total Arbitrage Pool */}
                <div className="p-4 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                  <div className="font-mono text-[11px] text-[#64748B] uppercase">
                    TOTAL ARBITRAGE POOL
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#F3F4F6] my-1 tabular-nums">
                    ₹{annualArbitragePoolLakhs} Lakhs
                  </div>
                  <div className="font-mono text-xs text-[#9CA3AF]">
                    ₹{dailyArbitragePoolLakhs} Lakhs / day ({capacityTpd} TPD @ ₹{mandiSpread}/kg)
                  </div>
                </div>

                {/* Card 2: Partner Miller Net Lift */}
                <div className="p-4 bg-[#0A0B0D] border border-[#F59E0B] rounded-sm">
                  <div className="font-mono text-[11px] text-[#F59E0B] uppercase font-semibold">
                    PARTNER MILLER NET PROFIT LIFT
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#F59E0B] my-1 tabular-nums">
                    ₹{annualMillerLiftLakhs} Lakhs
                  </div>
                  <div className="font-mono text-xs text-[#F59E0B]">
                    +₹{millerLift}/kg net margin (+₹{Math.round(millerLift * 1000).toLocaleString()}/MT)
                  </div>
                </div>

                {/* Card 3: FinnoaQ EBITDA */}
                <div className="p-4 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                  <div className="font-mono text-[11px] text-[#64748B] uppercase">
                    FINNOAQ ANNUAL EBITDA
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#10B981] my-1 tabular-nums">
                    ₹{annualFinnoaqEbitdaLakhs} Lakhs
                  </div>
                  <div className="font-mono text-xs text-[#9CA3AF]">
                    @ 90% utilization (Tolling ₹{tollingFee} - OpEx ₹6.34)
                  </div>
                </div>

                {/* Card 4: CapEx Payback */}
                <div className="p-4 bg-[#0A0B0D] border border-[#222630] rounded-sm">
                  <div className="font-mono text-[11px] text-[#64748B] uppercase">
                    CAPEX SIMPLE PAYBACK
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#F3F4F6] my-1 tabular-nums">
                    {paybackYears} Years
                  </div>
                  <div className="font-mono text-xs text-[#9CA3AF]">
                    Turnkey CapEx: ₹{turnkeyCapex.toFixed(1)} Lakhs
                  </div>
                </div>

              </div>
            </div>

            <div className="font-mono text-[11px] text-[#64748B]">
              All financial schedules trace directly to audited <span className="text-[#F3F4F6]">FINANCIAL_MODEL_15TPD.xlsx</span>
            </div>
          </div>

        </div>

        {/* 3-Tab Financial Drawer: OpEx Schedule / CapEx Schedule / 5-Year Cash Flow */}
        <div className="p-6 bg-[#0A0B0D]">
          
          {/* Tab Navigation */}
          <div className="flex border-b border-[#222630] mb-6">
            <button
              onClick={() => setActiveTab('opex')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'opex'
                  ? 'border-[#F59E0B] text-[#F59E0B] font-semibold'
                  : 'border-transparent text-[#9CA3AF] hover:text-[#F3F4F6]'
              }`}
            >
              [TAB 1 // ITEMIZED OPEX SCHEDULE (₹6.34/KG)]
            </button>
            <button
              onClick={() => setActiveTab('capex')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'capex'
                  ? 'border-[#F59E0B] text-[#F59E0B] font-semibold'
                  : 'border-transparent text-[#9CA3AF] hover:text-[#F3F4F6]'
              }`}
            >
              [TAB 2 // TURNKEY CAPEX SCHEDULE (₹135.0 LAKHS)]
            </button>
            <button
              onClick={() => setActiveTab('cashflow')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'cashflow'
                  ? 'border-[#F59E0B] text-[#F59E0B] font-semibold'
                  : 'border-transparent text-[#9CA3AF] hover:text-[#F3F4F6]'
              }`}
            >
              [TAB 3 // 5-YEAR CASH FLOW PRO-FORMA]
            </button>
          </div>

          {/* Tab 1: OpEx Schedule */}
          {activeTab === 'opex' && (
            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#222630]">
                <thead>
                  <tr className="bg-[#111317] border-b border-[#222630] text-[#64748B]">
                    <th className="p-3">Cost Channel</th>
                    <th className="p-3 text-right">Cost (₹/kg)</th>
                    <th className="p-3 text-right">Share (%)</th>
                    <th className="p-3">Process Specification & Equipment Basis</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#222630]">
                  {OPEX_BREAKDOWN.map((item, idx) => (
                    <tr key={idx} className="hover:bg-[#111317] transition-colors">
                      <td className="p-3 text-[#F3F4F6] font-medium">{item.category}</td>
                      <td className="p-3 text-right text-[#F59E0B] font-semibold tabular-nums">₹{item.costPerKg.toFixed(2)}</td>
                      <td className="p-3 text-right text-[#9CA3AF] tabular-nums">{item.percentage}%</td>
                      <td className="p-3 text-[#9CA3AF]">{item.details}</td>
                    </tr>
                  ))}
                  <tr className="bg-[#171A21] font-semibold text-[#F3F4F6]">
                    <td className="p-3">Total Reconciled Direct OpEx</td>
                    <td className="p-3 text-right text-[#10B981] tabular-nums text-sm">₹6.34</td>
                    <td className="p-3 text-right tabular-nums">100.0%</td>
                    <td className="p-3 text-[#10B981]">Audited with 85% closed-loop bleed-and-feed recycle</td>
                  </tr>
                </tbody>
              </table>
            </div>
          )}

          {/* Tab 2: CapEx Schedule */}
          {activeTab === 'capex' && (
            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#222630]">
                <thead>
                  <tr className="bg-[#111317] border-b border-[#222630] text-[#64748B]">
                    <th className="p-3">Area Tag</th>
                    <th className="p-3">Subsystem & Package Scope</th>
                    <th className="p-3 text-right">CapEx (₹ Lakhs)</th>
                    <th className="p-3">Equipment Specifications & Standards</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#222630]">
                  {CAPEX_SCHEDULE.map((area, idx) => (
                    <tr key={idx} className="hover:bg-[#111317] transition-colors">
                      <td className="p-3 text-[#F59E0B] font-semibold">{area.area}</td>
                      <td className="p-3 text-[#F3F4F6]">{area.name}</td>
                      <td className="p-3 text-right text-[#F3F4F6] font-semibold tabular-nums">₹{area.costLakhs.toFixed(2)}L</td>
                      <td className="p-3 text-[#9CA3AF]">{area.specs}</td>
                    </tr>
                  ))}
                  <tr className="bg-[#171A21] font-semibold text-[#F3F4F6]">
                    <td className="p-3 text-[#10B981]">Total Turnkey</td>
                    <td className="p-3 text-[#10B981]">Areas 100 to 900 Complete Turnkey Battery Limits</td>
                    <td className="p-3 text-right text-[#10B981] tabular-nums text-sm">₹135.00L</td>
                    <td className="p-3 text-[#10B981]">EPC Turnkey Scope (~$160,000 USD)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          )}

          {/* Tab 3: 5-Year Cash Flow Pro-Forma */}
          {activeTab === 'cashflow' && (
            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#222630]">
                <thead>
                  <tr className="bg-[#111317] border-b border-[#222630] text-[#64748B]">
                    <th className="p-3">Year</th>
                    <th className="p-3 text-right">Utilization</th>
                    <th className="p-3 text-right">Volume (MT)</th>
                    <th className="p-3 text-right">Revenue</th>
                    <th className="p-3 text-right">OpEx</th>
                    <th className="p-3 text-right">EBITDA</th>
                    <th className="p-3 text-right">EBITDA Margin</th>
                    <th className="p-3 text-right">PAT</th>
                    <th className="p-3 text-right">Cumulative FCF</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#222630]">
                  {FIVE_YEAR_CASH_FLOW.map((row, idx) => (
                    <tr key={idx} className="hover:bg-[#111317] transition-colors">
                      <td className="p-3 text-[#F3F4F6] font-semibold">{row.year}</td>
                      <td className="p-3 text-right text-[#9CA3AF] tabular-nums">{row.utilization}</td>
                      <td className="p-3 text-right text-[#9CA3AF] tabular-nums">{row.volumeMT}</td>
                      <td className="p-3 text-right text-[#F3F4F6] tabular-nums">{row.revenue}</td>
                      <td className="p-3 text-right text-[#9CA3AF] tabular-nums">{row.opex}</td>
                      <td className="p-3 text-right text-[#10B981] font-semibold tabular-nums">{row.ebitda}</td>
                      <td className="p-3 text-right text-[#10B981] tabular-nums">{row.ebitdaMargin}</td>
                      <td className="p-3 text-right text-[#F3F4F6] tabular-nums">{row.pat}</td>
                      <td className="p-3 text-right text-[#F59E0B] font-semibold tabular-nums">{row.cumFcf}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

        </div>

      </div>
    </section>
  );
}

