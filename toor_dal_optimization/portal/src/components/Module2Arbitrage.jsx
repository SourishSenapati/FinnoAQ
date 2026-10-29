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
    <section id="arbitrage" className="w-full bg-[#0C0E12] border-b border-[#1E232E] scroll-mt-20">
      <div className="max-w-[1440px] mx-auto border-x border-[#1E232E]">
        
        {/* Module Header */}
        <div className="p-5 sm:p-6 border-b border-[#1E232E] bg-[#111319] flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <span className="px-2.5 py-1 bg-[#151821] text-[#94A3B8] border border-[#232836] font-mono text-xs rounded-xs">
              [02 // UNIT ECONOMICS & ARBITRAGE]
            </span>
            <h2 className="text-base sm:text-lg font-semibold tracking-tight text-[#E6E8EC]">
              Mandi Arbitrage & Mill Financial Model
            </h2>
          </div>
          <span className="font-mono text-xs text-[#10B981]">
            RECONCILED ECONOMIC MODEL // V11
          </span>
        </div>

        {/* 2-Pane Workstation: Left Controls + Right Live Output */}
        <div className="grid grid-cols-1 lg:grid-cols-12 border-b border-[#1E232E]">
          
          {/* Left Pane: Interactive Sensitivity Controls (5 Cols) */}
          <div className="lg:col-span-5 p-6 sm:p-8 bg-[#0C0E12] border-b lg:border-b-0 lg:border-r border-[#1E232E] flex flex-col justify-between">
            <div>
              <div className="font-mono text-xs text-[#5E6573] uppercase tracking-wider mb-6">
                SENSITIVITY CONTROLS & PLANT SCALING
              </div>

              {/* Control 1: Daily Capacity */}
              <div className="mb-6">
                <div className="flex justify-between items-center mb-2">
                  <label className="font-mono text-xs text-[#8E95A2]">
                    Plant Daily Processing Capacity
                  </label>
                  <span className="font-mono text-sm font-semibold text-[#E6E8EC] tabular-nums">
                    {capacityTpd} TPD ({dailyKg.toLocaleString()} kg/day)
                  </span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[5, 15, 30].map((tpd) => (
                    <button
                      key={tpd}
                      onClick={() => setCapacityTpd(tpd)}
                      className={`py-2 px-3 font-mono text-xs rounded-xs border transition-colors cursor-pointer ${
                        capacityTpd === tpd 
                          ? 'bg-[#151821] border-[#D97706] text-[#D97706] font-medium' 
                          : 'bg-[#13151B] border-[#1E232E] text-[#8E95A2] hover:bg-[#171B24]'
                      }`}
                    >
                      {tpd} TPD {tpd === 15 ? '(Design)' : ''}
                    </button>
                  ))}
                </div>
              </div>

              {/* Control 2: Mandi Spread */}
              <div className="mb-5">
                <div className="flex justify-between items-center mb-2">
                  <label className="font-mono text-xs text-[#8E95A2]">
                    Mandi Arbitrage Spread (Gross)
                  </label>
                  <span className="font-mono text-sm font-semibold text-[#D97706] tabular-nums">
                    ₹{mandiSpread.toFixed(2)} / kg
                  </span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[14, 20, 28].map((spread) => (
                    <button
                      key={spread}
                      onClick={() => setMandiSpread(spread)}
                      className={`py-2 px-3 font-mono text-xs rounded-xs border transition-colors cursor-pointer ${
                        mandiSpread === spread 
                          ? 'bg-[#151821] border-[#D97706] text-[#D97706] font-medium' 
                          : 'bg-[#13151B] border-[#1E232E] text-[#8E95A2] hover:bg-[#171B24]'
                      }`}
                    >
                      ₹{spread}/kg {spread === 20 ? '(Baseline)' : ''}
                    </button>
                  ))}
                </div>
                <div className="mt-1 font-mono text-[11px] text-[#5E6573]">
                  Imported Raw: ₹85.00/kg → Desi Parity: ₹{desiParity.toFixed(2)}/kg
                </div>
              </div>

              {/* Control 3: Operating Days */}
              <div className="mb-5">
                <div className="flex justify-between items-center mb-2">
                  <label className="font-mono text-xs text-[#8E95A2]">
                    Annual Operating Days
                  </label>
                  <span className="font-mono text-sm font-semibold text-[#E6E8EC] tabular-nums">
                    {operatingDays} Days / Year
                  </span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[200, 300, 330].map((days) => (
                    <button
                      key={days}
                      onClick={() => setOperatingDays(days)}
                      className={`py-2 px-3 font-mono text-xs rounded-xs border transition-colors cursor-pointer ${
                        operatingDays === days 
                          ? 'bg-[#151821] border-[#D97706] text-[#D97706] font-medium' 
                          : 'bg-[#13151B] border-[#1E232E] text-[#8E95A2] hover:bg-[#171B24]'
                      }`}
                    >
                      {days} Days {days === 300 ? '(Standard)' : ''}
                    </button>
                  ))}
                </div>
              </div>
            </div>

            <div className="pt-4 border-t border-[#1E232E] font-mono text-[11px] text-[#5E6573]">
              Deterministic Cash-Flow Engine & Sensitivity Model (FNQ-MB-2026)
            </div>
          </div>

          {/* Right Pane: Live Waterfall & Output Cards (7 Cols) */}
          <div className="lg:col-span-7 p-6 sm:p-8 bg-[#111319] flex flex-col justify-between">
            <div>
              <div className="flex justify-between items-center mb-4">
                <span className="font-mono text-xs text-[#5E6573] uppercase tracking-wider">
                  UNIT ECONOMICS WATERFALL (PER KG BASIS)
                </span>
                <span className="font-mono text-xs text-[#10B981]">
                  AUDITED BALANCE CONSERVATION
                </span>
              </div>

              {/* Horizontal Waterfall Bar */}
              <div className="p-4 bg-[#0C0E12] border border-[#1E232E] rounded-xs mb-5">
                <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-2 font-mono text-xs">
                  
                  {/* Base Intake */}
                  <div className="p-2.5 bg-[#13151B] border border-[#1E232E] rounded-xs flex-1 text-center">
                    <div className="text-[10px] text-[#5E6573]">BASE RAW INTAKE</div>
                    <div className="text-sm font-semibold text-[#E6E8EC] tabular-nums">₹85.00</div>
                    <div className="text-[10px] text-[#8E95A2]">Imported Grain</div>
                  </div>

                  <span className="text-[#5E6573] text-center font-bold">+</span>

                  {/* OpEx with Hover Breakdown */}
                  <div 
                    onMouseEnter={() => setShowOpexPopover(true)}
                    onMouseLeave={() => setShowOpexPopover(false)}
                    className="p-2.5 bg-[#151821] border border-[#1E232E] hover:border-[#D97706] rounded-xs flex-1 text-center cursor-help relative transition-colors"
                  >
                    <div className="text-[10px] text-[#D97706]">DIRECT OPEX ℹ</div>
                    <div className="text-sm font-semibold text-[#E6E8EC] tabular-nums">₹6.34</div>
                    <div className="text-[10px] text-[#8E95A2]">85% Recycled</div>

                    {/* OpEx Popover Breakdown */}
                    {showOpexPopover && (
                      <div className="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-64 p-3 bg-[#13151B] border border-[#D97706] rounded-xs shadow-xl z-30 text-left">
                        <div className="font-mono text-[10px] text-[#D97706] uppercase font-semibold mb-2">
                          Itemized Direct OpEx Breakdown:
                        </div>
                        <div className="space-y-1 font-mono text-[11px] text-[#8E95A2]">
                          <div className="flex justify-between">
                            <span>S1-09 Reagents:</span>
                            <span className="text-[#E6E8EC]">₹3.63/kg (57%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Biomass Steam:</span>
                            <span className="text-[#E6E8EC]">₹1.12/kg (18%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Electrical Power:</span>
                            <span className="text-[#E6E8EC]">₹0.48/kg (8%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Direct Labor:</span>
                            <span className="text-[#E6E8EC]">₹0.62/kg (10%)</span>
                          </div>
                          <div className="flex justify-between">
                            <span>Water, ZLD & Maint:</span>
                            <span className="text-[#E6E8EC]">₹0.49/kg (7%)</span>
                          </div>
                        </div>
                      </div>
                    )}
                  </div>

                  <span className="text-[#5E6573] text-center font-bold">+</span>

                  {/* FinnoaQ Margin */}
                  <div className="p-2.5 bg-[#13151B] border border-[#1E232E] rounded-xs flex-1 text-center">
                    <div className="text-[10px] text-[#5E6573]">FINNOAQ MARGIN</div>
                    <div className="text-sm font-semibold text-[#E6E8EC] tabular-nums">₹{finnoaqMargin.toFixed(2)}</div>
                    <div className="text-[10px] text-[#8E95A2]">Tolling Fee ₹{tollingFee.toFixed(2)}</div>
                  </div>

                  <span className="text-[#5E6573] text-center font-bold">+</span>

                  {/* Partner Miller Lift (Amber Highlight) */}
                  <div className="p-2.5 bg-[#151821] border border-[#D97706] rounded-xs flex-1 text-center">
                    <div className="text-[10px] text-[#D97706] font-semibold">MILLER NET LIFT</div>
                    <div className="text-sm font-bold text-[#D97706] tabular-nums">+₹{millerLift.toFixed(2)}</div>
                    <div className="text-[10px] text-[#D97706]">Partner Profit</div>
                  </div>

                  <span className="text-[#5E6573] text-center font-bold">=</span>

                  {/* Desi Parity */}
                  <div className="p-2.5 bg-[#13151B] border border-[#1E232E] rounded-xs flex-1 text-center">
                    <div className="text-[10px] text-[#10B981]">DESI PARITY</div>
                    <div className="text-sm font-semibold text-[#10B981] tabular-nums">₹{desiParity.toFixed(2)}</div>
                    <div className="text-[10px] text-[#8E95A2]">Market Parity</div>
                  </div>

                </div>
              </div>

              {/* 4 Live Output Cards */}
              <div className="grid grid-cols-2 gap-3 mb-4">
                
                {/* Card 1: Total Arbitrage Pool */}
                <div className="p-4 bg-[#0C0E12] border border-[#1E232E] rounded-xs">
                  <div className="font-mono text-[11px] text-[#5E6573] uppercase tracking-wider">
                    TOTAL ARBITRAGE POOL
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#E6E8EC] my-1 tabular-nums">
                    ₹{annualArbitragePoolLakhs} Lakhs
                  </div>
                  <div className="font-mono text-xs text-[#8E95A2]">
                    ₹{dailyArbitragePoolLakhs} Lakhs / day ({capacityTpd} TPD @ ₹{mandiSpread}/kg)
                  </div>
                </div>

                {/* Card 2: Partner Miller Net Lift */}
                <div className="p-4 bg-[#151821] border border-[#D97706] rounded-xs">
                  <div className="font-mono text-[11px] text-[#D97706] uppercase font-semibold tracking-wider">
                    PARTNER MILLER NET PROFIT LIFT
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#D97706] my-1 tabular-nums">
                    ₹{annualMillerLiftLakhs} Lakhs
                  </div>
                  <div className="font-mono text-xs text-[#D97706]">
                    +₹{millerLift}/kg net margin (+₹{Math.round(millerLift * 1000).toLocaleString()}/MT)
                  </div>
                </div>

                {/* Card 3: FinnoaQ EBITDA */}
                <div className="p-4 bg-[#0C0E12] border border-[#1E232E] rounded-xs">
                  <div className="font-mono text-[11px] text-[#5E6573] uppercase tracking-wider">
                    FINNOAQ ANNUAL EBITDA
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#10B981] my-1 tabular-nums">
                    ₹{annualFinnoaqEbitdaLakhs} Lakhs
                  </div>
                  <div className="font-mono text-xs text-[#8E95A2]">
                    @ 90% utilization (Tolling ₹{tollingFee} - OpEx ₹6.34)
                  </div>
                </div>

                {/* Card 4: CapEx Payback */}
                <div className="p-4 bg-[#0C0E12] border border-[#1E232E] rounded-xs">
                  <div className="font-mono text-[11px] text-[#5E6573] uppercase tracking-wider">
                    CAPEX SIMPLE PAYBACK
                  </div>
                  <div className="font-mono text-xl sm:text-2xl font-bold text-[#E6E8EC] my-1 tabular-nums">
                    {paybackYears} Years
                  </div>
                  <div className="font-mono text-xs text-[#8E95A2]">
                    Turnkey CapEx: ₹{turnkeyCapex.toFixed(1)} Lakhs
                  </div>
                </div>

              </div>
            </div>

            <div className="font-mono text-[11px] text-[#5E6573]">
              All financial schedules trace directly to audited <span className="text-[#E6E8EC]">FINANCIAL_MODEL_15TPD.xlsx</span>
            </div>
          </div>

        </div>

        {/* 3-Tab Financial Drawer: OpEx Schedule / CapEx Schedule / 5-Year Cash Flow */}
        <div className="p-6 bg-[#0C0E12]">
          
          {/* Tab Navigation */}
          <div className="flex border-b border-[#1E232E] mb-6">
            <button
              onClick={() => setActiveTab('opex')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'opex'
                  ? 'border-[#D97706] text-[#D97706] font-semibold'
                  : 'border-transparent text-[#8E95A2] hover:text-[#E6E8EC]'
              }`}
            >
              [TAB 1 // ITEMIZED OPEX SCHEDULE (₹6.34/KG)]
            </button>
            <button
              onClick={() => setActiveTab('capex')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'capex'
                  ? 'border-[#D97706] text-[#D97706] font-semibold'
                  : 'border-transparent text-[#8E95A2] hover:text-[#E6E8EC]'
              }`}
            >
              [TAB 2 // TURNKEY CAPEX SCHEDULE (₹135.0 LAKHS)]
            </button>
            <button
              onClick={() => setActiveTab('cashflow')}
              className={`pb-3 px-4 font-mono text-xs cursor-pointer border-b-2 transition-colors ${
                activeTab === 'cashflow'
                  ? 'border-[#D97706] text-[#D97706] font-semibold'
                  : 'border-transparent text-[#8E95A2] hover:text-[#E6E8EC]'
              }`}
            >
              [TAB 3 // 5-YEAR CASH FLOW PRO-FORMA]
            </button>
          </div>

          {/* Tab 1: OpEx Schedule */}
          {activeTab === 'opex' && (
            <div className="overflow-x-auto">
              <table className="w-full text-left font-mono text-xs border border-[#1E232E]">
                <thead>
                  <tr className="bg-[#111319] border-b border-[#1E232E] text-[#5E6573]">
                    <th className="p-3">Cost Channel</th>
                    <th className="p-3 text-right">Cost (₹/kg)</th>
                    <th className="p-3 text-right">Share (%)</th>
                    <th className="p-3">Process Specification & Equipment Basis</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#1E232E]">
                  {OPEX_BREAKDOWN.map((item, idx) => (
                    <tr key={idx} className="hover:bg-[#111319] transition-colors">
                      <td className="p-3 text-[#E6E8EC] font-medium">{item.category}</td>
                      <td className="p-3 text-right text-[#D97706] font-semibold tabular-nums">₹{item.costPerKg.toFixed(2)}</td>
                      <td className="p-3 text-right text-[#8E95A2] tabular-nums">{item.percentage}%</td>
                      <td className="p-3 text-[#8E95A2]">{item.details}</td>
                    </tr>
                  ))}
                  <tr className="bg-[#151821] font-semibold text-[#E6E8EC]">
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
              <table className="w-full text-left font-mono text-xs border border-[#1E232E]">
                <thead>
                  <tr className="bg-[#111319] border-b border-[#1E232E] text-[#5E6573]">
                    <th className="p-3">Area Tag</th>
                    <th className="p-3">Subsystem & Package Scope</th>
                    <th className="p-3 text-right">CapEx (₹ Lakhs)</th>
                    <th className="p-3">Equipment Specifications & Standards</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#1E232E]">
                  {CAPEX_SCHEDULE.map((area, idx) => (
                    <tr key={idx} className="hover:bg-[#111319] transition-colors">
                      <td className="p-3 text-[#D97706] font-semibold">{area.area}</td>
                      <td className="p-3 text-[#E6E8EC]">{area.name}</td>
                      <td className="p-3 text-right text-[#E6E8EC] font-semibold tabular-nums">₹{area.costLakhs.toFixed(2)}L</td>
                      <td className="p-3 text-[#8E95A2]">{area.specs}</td>
                    </tr>
                  ))}
                  <tr className="bg-[#151821] font-semibold text-[#E6E8EC]">
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
              <table className="w-full text-left font-mono text-xs border border-[#1E232E]">
                <thead>
                  <tr className="bg-[#111319] border-b border-[#1E232E] text-[#5E6573]">
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
                <tbody className="divide-y divide-[#1E232E]">
                  {FIVE_YEAR_CASH_FLOW.map((row, idx) => (
                    <tr key={idx} className="hover:bg-[#111319] transition-colors">
                      <td className="p-3 text-[#E6E8EC] font-semibold">{row.year}</td>
                      <td className="p-3 text-right text-[#8E95A2] tabular-nums">{row.utilization}</td>
                      <td className="p-3 text-right text-[#8E95A2] tabular-nums">{row.volumeMT}</td>
                      <td className="p-3 text-right text-[#E6E8EC] tabular-nums">{row.revenue}</td>
                      <td className="p-3 text-right text-[#8E95A2] tabular-nums">{row.opex}</td>
                      <td className="p-3 text-right text-[#10B981] font-semibold tabular-nums">{row.ebitda}</td>
                      <td className="p-3 text-right text-[#10B981] tabular-nums">{row.ebitdaMargin}</td>
                      <td className="p-3 text-right text-[#E6E8EC] tabular-nums">{row.pat}</td>
                      <td className="p-3 text-right text-[#D97706] font-semibold tabular-nums">{row.cumFcf}</td>
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

