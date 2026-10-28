"""
Root-Cause Claim Ledger and Evidence Hierarchy Manager.
Strictly classifies claims into Categories A, B, C, D and ensures zero causal overreach.
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

@dataclass
class ClaimRecord:
    claim_id: str
    wording: str
    evidence_category: str  # "A" (Confirmed Diff), "B" (Strongly Associated), "C" (Potential Mechanism), "D" (Unlikely Factor)
    evidence_status: str    # "DATA_READINESS_ONLY", "EMPIRICAL_SUPPORTED", "REJECTED"
    supporting_assays: List[str]
    supporting_source_pointer: str
    code_version: str
    uncertainty_level: str  # "HIGH", "MEDIUM", "LOW"
    alternative_explanations: List[str]
    contradictory_evidence: Optional[str] = None
    limitations: List[str] = field(default_factory=list)
    phase2_validation_required: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class RootCauseClaimLedger:
    def __init__(self):
        self.claims: Dict[str, ClaimRecord] = {}

    def add_claim(self, claim: ClaimRecord):
        self.claims[claim.claim_id] = claim

    def get_claim(self, claim_id: str) -> Optional[ClaimRecord]:
        return self.claims.get(claim_id)

    def list_claims_by_category(self, category: str) -> List[ClaimRecord]:
        return [c for c in self.claims.values() if c.evidence_category == category]

    def export_ledger_dict(self) -> List[Dict[str, Any]]:
        return [asdict(c) for c in self.claims.values()]

def get_baseline_phase1_claims() -> RootCauseClaimLedger:
    """
    Construct the baseline diagnostic claims matrix for Phase 1.
    All claims are data-gated; until empirical lab data arrive,
    they are recorded as DATA_READINESS_ONLY / Hypotheses for Phase 2 validation.
    """
    ledger = RootCauseClaimLedger()
    
    # Claim 1: Household observation of whistle differential
    ledger.add_claim(ClaimRecord(
        claim_id="CLAIM_01_WHISTLE_DIFF",
        wording="Tanzanian Toor Dal exhibits an initial household cooking requirement of approximately 6 whistles compared with 3 whistles for Indian benchmark under domestic conditions.",
        evidence_category="B",  # Strongly associated practical observation
        evidence_status="DATA_READINESS_ONLY",
        supporting_assays=["COOK_04 (N_whistles)", "Household observation log"],
        supporting_source_pointer="Phase1_Scope_of_Work_Toor_Dal.docx §1, Table 2",
        code_version="1.0.0",
        uncertainty_level="HIGH",
        alternative_explanations=[
            "Domestic cooker stove heat output variations",
            "Water hardness differences between domestic locations",
            "Steam release valve calibration differences"
        ],
        contradictory_evidence=None,
        limitations=[
            "Pressure-cooker whistle count is a practical operational reference, not a calibrated scientific endpoint.",
            "Must be validated under instrumented laboratory autoclave at 103 kPa / 121°C."
        ],
        phase2_validation_required="Controlled instrumented pressure cooking (Test C) with logged temperature and pressure profiles."
    ))

    # Claim 2: Water mass transfer / hydration limitation
    ledger.add_claim(ClaimRecord(
        claim_id="CLAIM_02_HYDRATION_LIMITATION",
        wording="Slower cold water uptake (elevated Peleg k1) may act as a rate-limiting initial resistance to cotyledon swelling.",
        evidence_category="C",  # Potential mechanism requiring validation
        evidence_status="DATA_READINESS_ONLY",
        supporting_assays=["HYD_01 to HYD_07", "HYD_12 (Peleg k1)", "HYD_15 (r0)"],
        supporting_source_pointer="Phase1_Scope_of_Work_Toor_Dal.docx §8, Table 10",
        code_version="1.0.0",
        uncertainty_level="HIGH",
        alternative_explanations=[
            "Residual seed-coat waxiness rather than cotyledon permeability",
            "Milling damage and micro-cracking variations between lots"
        ],
        contradictory_evidence=None,
        limitations=[
            "Hydration rate at 25°C does not necessarily predict thermal softening rate at 121°C."
        ],
        phase2_validation_required="Test B standardized soaking comparative trials vs Test A no-soak trials."
    ))

    # Claim 3: Pectin-Divalent Cation Crosslinking (3P Cascade Hypothesis)
    ledger.add_claim(ClaimRecord(
        claim_id="CLAIM_03_PECTIN_CATION_CROSSLINKING",
        wording="Endogenous phytase dephosphorylation of phytic acid during warm transit may liberate Ca2+/Mg2+ that crosslinks low-DE pectin in the middle lamella, preventing thermal cell separation.",
        evidence_category="C",  # Potential mechanism requiring validation
        evidence_status="DATA_READINESS_ONLY",
        supporting_assays=["PEC_01 to PEC_07", "MIN_01 (Ca)", "MIN_05 (Phytate)", "MIN_06 (Phytate:Ca ratio)"],
        supporting_source_pointer="Phase1_Scope_of_Work_Toor_Dal.docx §10, §11, Table 18, Table 20",
        code_version="1.0.0",
        uncertainty_level="HIGH",
        alternative_explanations=[
            "Genetic differences in cotyledon cellular wall thickness (cellulose/lignin)",
            "Starch gelatinization retrogradation or protein denaturation during post-harvest drying"
        ],
        contradictory_evidence=None,
        limitations=[
            "Correlation between low phytate and high hard-core percentage does not prove causality without chemical chelator reversal trials."
        ],
        phase2_validation_required="Phase 2 food-grade chelating/tempering trials (EDTA/citrate/hexametaphosphate) to test reversibility."
    ))

    # Claim 4: Starch Thermal Barrier
    ledger.add_claim(ClaimRecord(
        claim_id="CLAIM_04_STARCH_GELATINIZATION",
        wording="Starch gelatinization onset/peak temperature and enthalpy may differ measurably between Tanzanian and Indian toor dal.",
        evidence_category="C",  # Potential mechanism
        evidence_status="DATA_READINESS_ONLY",
        supporting_assays=["STR_04 to STR_08 (DSC)", "STR_09 to STR_13 (RVA)"],
        supporting_source_pointer="Phase1_Scope_of_Work_Toor_Dal.docx §7, Table 13",
        code_version="1.0.0",
        uncertainty_level="HIGH",
        alternative_explanations=[
            "Starch gelatinization in excess water occurs at 65-75°C, well below autoclave temperature (121°C), suggesting starch is not the primary thermal bottleneck."
        ],
        contradictory_evidence="Literature shows legume starch fully gelatinizes within 10-15 min at 100°C if water is present.",
        limitations=["Requires DSC and RVA confirmation on isolated starch granules."],
        phase2_validation_required="Comparative DSC thermograms in isolated starch vs whole cotyledon flour."
    ))

    return ledger
