#!/usr/bin/env python3
"""
FinnoaQ Industrial Pulse Engineering & Technology Evaluation CLI Wrapper.
Project Ref: FNQ-PR-2026-001 | Lead Engineer: Sourish Senapati
"""

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(base_dir, "src")
for p in [base_dir, src_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

from finnoaq.pulse_tech_cli import main

if __name__ == "__main__":
    main()
