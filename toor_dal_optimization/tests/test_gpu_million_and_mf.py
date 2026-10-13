"""
Test suite validating the 7 Structured Memory Files (MF System),
Million-Scale GPU Simulation Artifacts, and 5-Sigma Statistical Process Capability.
"""

import os
import json
import pytest

REQUIRED_MF_FILES = [
    "PROJECT_VISION.md",
    "ARCHITECTURE.md",
    "SECURITY.md",
    "PERFORMANCE.md",
    "UX.md",
    "TESTING.md",
    "IMPROVEMENT_LOG.md"
]

def test_structured_memory_files_exist_and_populated():
    """Verify all 7 Structured Memory Files exist in workspace root and meet depth standards."""
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    for filename in REQUIRED_MF_FILES:
        filepath = os.path.join(root_dir, filename)
        assert os.path.isfile(filepath), f"Missing required Structured Memory File: {filename}"
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Must be substantive (> 1,000 characters)
        assert len(content) > 1000, f"Structured Memory File {filename} is too short ({len(content)} chars)"
        assert content.startswith("# "), f"Structured Memory File {filename} must begin with top-level heading"


def test_million_scale_gpu_convergence_artifact():
    """Verify that the 1,000,000 experiment GPU simulation artifact exists and contains valid convergence history."""
    artifact_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artifacts", "gpu_million_experiment_convergence.json"))
    assert os.path.isfile(artifact_path), f"Missing GPU convergence artifact: {artifact_path}"
    
    with open(artifact_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert data["total_experiments_evaluated"] == 1_000_000, "Must evaluate exactly 1,000,000 experiments"
    assert data["total_generations"] == 10, "Must evaluate 10 generations"
    assert len(data["generational_convergence_history"]) == 10, "Must contain 10 generation records"
    assert data["throughput_experiments_per_sec"] > 100_000, "GPU throughput must exceed 100,000 experiments/sec"
    assert data["final_5_sigma_validation"]["target_5_sigma_achieved"] is True, "5-Sigma target must be achieved"


def test_five_sigma_quality_metrics():
    """Verify that the 5-Sigma validation report demonstrates Cpk >= 1.62 and DPMO <= 3.4."""
    report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artifacts", "five_sigma_validation_report.json"))
    assert os.path.isfile(report_path), f"Missing 5-Sigma validation report: {report_path}"
    
    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    metrics = data["five_sigma_metrics"]
    cpk = metrics["process_capability_cpk"]
    sigma_level = metrics["achieved_sigma_level"]
    dpmo = metrics["defects_per_million_opportunities_dpmo"]
    
    assert cpk >= 1.62, f"Process capability Cpk {cpk} must be >= 1.62 for 5-Sigma standard"
    assert sigma_level >= 5.0, f"Sigma level {sigma_level} must be >= 5.0"
    assert dpmo <= 3.4, f"DPMO {dpmo} must be <= 3.4 for 5-Sigma manufacturing"
    assert metrics["target_5_sigma_achieved"] is True
