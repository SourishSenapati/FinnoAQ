import React from 'react';

export default function Navbar() {
  const scrollTo = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className="sticky top-0 z-50 w-full bg-[#0A0B0D] border-b border-[#222630]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
        
        {/* Left: Monochrome Identifier */}
        <div className="flex items-center space-x-3">
          <div className="px-2.5 py-1 bg-[#1E222A] text-[#94A3B8] border border-[#2E3440] font-mono text-xs rounded-sm tracking-wide">
            [FNQ-PR-2026-COMM-001 // REV V11]
          </div>
          <span className="hidden md:inline font-mono text-xs text-[#64748B]">
            15 TPD TURNKEY COMMERCIAL PLATFORM
          </span>
        </div>

        {/* Center: Clean Anchor Links */}
        <nav className="hidden lg:flex items-center space-x-6 font-mono text-xs text-[#9CA3AF]">
          <button 
            onClick={() => scrollTo('hero')} 
            className="hover:text-[#F3F4F6] transition-colors cursor-pointer"
          >
            [00 // OVERVIEW]
          </button>
          <button 
            onClick={() => scrollTo('arbitrage')} 
            className="hover:text-[#F3F4F6] transition-colors cursor-pointer"
          >
            [01 // ROI WORKSTATION]
          </button>
          <button 
            onClick={() => scrollTo('biophysics')} 
            className="hover:text-[#F3F4F6] transition-colors cursor-pointer"
          >
            [02 // BIOPHYSICS]
          </button>
          <button 
            onClick={() => scrollTo('pfd-aspen')} 
            className="hover:text-[#F3F4F6] transition-colors cursor-pointer"
          >
            [03 // PFD & ASPEN]
          </button>
          <button 
            onClick={() => scrollTo('roadmap')} 
            className="hover:text-[#F3F4F6] transition-colors cursor-pointer"
          >
            [04 // ROADMAP]
          </button>
          <button 
            onClick={() => scrollTo('scoping')} 
            className="hover:text-[#F3F4F6] transition-colors cursor-pointer"
          >
            [05 // 48-HR TRIAL]
          </button>
          <button 
            onClick={() => scrollTo('data-room')} 
            className="hover:text-[#F3F4F6] transition-colors cursor-pointer"
          >
            [06 // DATA ROOM]
          </button>
        </nav>

        {/* Right: Solid Amber CTA */}
        <div className="flex items-center space-x-3">
          <button
            onClick={() => scrollTo('scoping')}
            className="bg-[#F59E0B] text-black font-semibold text-xs px-3.5 py-1.5 rounded-sm hover:bg-[#D97706] transition-colors cursor-pointer font-mono tracking-tight"
          >
            Request 48-Hr Grain Trial
          </button>
        </div>

      </div>
    </header>
  );
}
