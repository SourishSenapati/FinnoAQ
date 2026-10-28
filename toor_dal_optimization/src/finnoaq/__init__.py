"""
FinnoaQ Autonomous R&D and Computational Discovery Package.
Phase 1 Diagnostic Comparison of Tanzanian Toor Dal vs. Indian Benchmark Toor Dal,
coupled with Closed-Loop AI-Native Product Development Lifecycle (Stages 01-12, Gates G0-G9).
Integrated with Learn Harness Engineering and Foodoscope Computational Gastronomy.
"""

from src.finnoaq.foodoscope import FoodoscopeInformaticsEngine
from src.finnoaq.virtual_screening import VirtualScreeningPipeline, CandidateTreatment, ScreeningResult
from src.finnoaq.digital_twin import ClosedLoopDigitalTwin
from src.finnoaq.harness import HarnessEngineeringManager

__version__ = "2.1.0"
__author__ = "FinnoaQ R&D Team"

__all__ = [
    "FoodoscopeInformaticsEngine",
    "VirtualScreeningPipeline",
    "CandidateTreatment",
    "ScreeningResult",
    "ClosedLoopDigitalTwin",
    "HarnessEngineeringManager",
]
