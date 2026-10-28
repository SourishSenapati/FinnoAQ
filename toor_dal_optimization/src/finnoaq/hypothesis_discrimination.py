"""
FinnoaQ Engineering Workspace — Scientific Hypothesis Discrimination & Optimal Experimental Design (OED).
Project Reference: FNQ-PR-2026-001 | Toor Dal Cooking-Time Optimization
Lead Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

This module implements:
1. Formal representation of 10 competing hypotheses (H1 to H10) for slow cooking.
2. Linkage to the funded laboratory budget in Final_Proposal.docx (Option 1: INR 1,73,000).
3. Information-theoretic Expected Information Gain (EIG) and diagnostic cost-efficiency metrics.
4. Prioritized data-acquisition plan for client decision support.
"""

from typing import Dict, Any, List
import math

class HypothesisDiscriminationEngine:
    """
    Evaluates 10 competing hypotheses and ranks laboratory tests by Expected Information Gain (EIG).
    """
    def __init__(self):
        self.hypotheses = {
            'H1': {
                'title': 'Hydration Diffusion Barrier',
                'mechanism': 'Impaired water uptake kinetics across cotyledon surface (high k1, low Deff).',
                'predicted_observation': 'Significantly lower Peleg rate constant k1, reduced initial absorption rate R0.',
                'falsification_criterion': 'Target dal hydration curve matches Indian benchmark (p > 0.05 on k1).'
            },
            'H2': {
                'title': 'Cotyledon Geometry & Residual Seed Coat',
                'mechanism': 'Residual hydrophobic testa or abnormal surface area-to-volume ratio.',
                'predicted_observation': 'Residual seed coat > 0.5% w/w, altered sphericity.',
                'falsification_criterion': 'Residual testa < 0.1% w/w and geometry statistically identical to benchmark.'
            },
            'H3': {
                'title': 'Parenchyma Cell Compactness & Wall Thickness',
                'mechanism': 'Dense cellular packing impeding steam/water micro-channels during cooking.',
                'predicted_observation': 'Thicker primary cell walls on microscopy, higher bulk shear resistance.',
                'falsification_criterion': 'Cell wall thickness and density within benchmark normal range.'
            },
            'H4': {
                'title': 'Pectin De-esterification & Calcium Cross-Linking',
                'mechanism': 'Pectin methylesterase activity creating carboxylates crosslinked by Ca2+/Mg2+ (Hard-to-Cook).',
                'predicted_observation': 'Low water-soluble pectin fraction, high chelate-soluble pectin, chelation reversal.',
                'falsification_criterion': 'EDTA/citrate chelation produces no significant reduction in T90 vs water control.'
            },
            'H5': {
                'title': 'Phytate Depletion & Mineral Redistribution',
                'mechanism': 'Phytase breakdown of phytate releasing divalent cations to crosslink middle lamella.',
                'predicted_observation': 'Low phytate content, phytate-to-(Ca+Mg) molar ratio < 0.20.',
                'falsification_criterion': 'Phytate-to-(Ca+Mg) molar ratio > 0.40 (ample chelation capacity).'
            },
            'H6': {
                'title': 'Starch Gelatinization Enthalpy Shifts',
                'mechanism': 'Elevated gelatinization onset (To) or peak (Tp) temperature requiring higher cooking energy.',
                'predicted_observation': 'DSC peak gelatinization temperature Tp > 82 C (benchmark ~74-76 C).',
                'falsification_criterion': 'DSC Tp and Delta H_gel within 1.5 C / 1.0 J/g of Indian benchmark.'
            },
            'H7': {
                'title': 'Protein Denaturation & Insoluble Matrix Formation',
                'mechanism': 'Storage-induced protein aggregation restricting starch granule swelling during boiling.',
                'predicted_observation': 'Reduced protein dispersibility index (PDI), insoluble protein matrix.',
                'falsification_criterion': 'Protein solubility profile identical between imported and domestic dal.'
            },
            'H8': {
                'title': 'Cultivar Genetic Endosperm Traits',
                'mechanism': 'Tanzanian landrace (e.g., ICEAP lineage) inherent genetic seed hardness.',
                'predicted_observation': 'Trait persists across multiple harvest years and milling conditions.',
                'falsification_criterion': 'Cooking time normalizes under mild moisture conditioning.'
            },
            'H9': {
                'title': 'High-Temperature, High-Humidity Transit Aging',
                'mechanism': 'Shipping container microclimate aging inducing hard-to-cook defect in transit.',
                'predicted_observation': 'Fresh harvest cooks normally; aged/shipped consignment exhibits slow cooking.',
                'falsification_criterion': 'Controlled storage aging does not replicate defect.'
            },
            'H10': {
                'title': 'Cooking Measurement & Water Hardness Artifacts',
                'mechanism': 'Preliminary client observation was an artifact of domestic water hardness or pressure.',
                'predicted_observation': 'Discrepancy disappears when tested in demineralized water in calibrated autoclave.',
                'falsification_criterion': 'Target dal still exhibits >= 30% slower cooking in demineralized water.'
            }
        }

        # Funded Work Packages from Final_Proposal.docx (SOW Table 40, Total INR 1,73,000)
        self.work_packages = {
            'WP-01': {
                'title': 'Sample Intake, Grading & Physical Inspection',
                'cost_inr': 5000.0,
                'target_hypotheses': ['H2', 'H8'],
                'discriminating_power': 0.40  # bits of expected entropy reduction
            },
            'WP-02': {
                'title': 'Moisture & Proximate Composition (AOAC)',
                'cost_inr': 7000.0,
                'target_hypotheses': ['H1', 'H7'],
                'discriminating_power': 0.50
            },
            'WP-03': {
                'title': 'Starch Gelatinization & DSC Thermal Analysis',
                'cost_inr': 20000.0,
                'target_hypotheses': ['H6'],
                'discriminating_power': 0.85
            },
            'WP-04': {
                'title': 'Water Absorption Kinetics & Peleg Modeling',
                'cost_inr': 10000.0,
                'target_hypotheses': ['H1', 'H8'],
                'discriminating_power': 0.80
            },
            'WP-05': {
                'title': 'Cell-Wall Structural & Pectin Fractionation',
                'cost_inr': 28000.0,
                'target_hypotheses': ['H3', 'H4'],
                'discriminating_power': 0.95
            },
            'WP-06': {
                'title': 'Mineral Profiling (ICP-OES) & Phytate Determination',
                'cost_inr': 16000.0,
                'target_hypotheses': ['H4', 'H5'],
                'discriminating_power': 0.90
            },
            'WP-07': {
                'title': 'Texture Profile Analysis (TPA) & Shear Resistance',
                'cost_inr': 17000.0,
                'target_hypotheses': ['H3', 'H4', 'H7'],
                'discriminating_power': 0.75
            },
            'WP-08': {
                'title': 'Standardized Baseline Cooking Performance (Autoclave)',
                'cost_inr': 20000.0,
                'target_hypotheses': ['H10', 'H1', 'H4'],
                'discriminating_power': 0.98
            },
            'WP-09': {
                'title': 'Multi-Factor Statistical Analysis & Hypothesis Ranking',
                'cost_inr': 15000.0,
                'target_hypotheses': ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'],
                'discriminating_power': 0.65
            },
            'WP-10': {
                'title': 'Candidate Treatment Formulation Screening',
                'cost_inr': 20000.0,
                'target_hypotheses': ['H4', 'H6'],
                'discriminating_power': 0.92
            },
            'WP-11': {
                'title': 'Phase 1 Consolidated Technical Report & Client Review',
                'cost_inr': 15000.0,
                'target_hypotheses': ['ALL'],
                'discriminating_power': 0.30
            }
        }

    def evaluate_diagnostic_priorities(self) -> List[Dict[str, Any]]:
        """
        Ranks all funded work packages by diagnostic cost-efficiency:
        Cost Efficiency = Discriminating Power (bits) / Cost (kINR)
        """
        results = []
        total_budget = sum(wp['cost_inr'] for wp in self.work_packages.values())

        for wp_id, wp in self.work_packages.items():
            cost_kinr = wp['cost_inr'] / 1000.0
            eig_bits = wp['discriminating_power']
            efficiency = eig_bits / cost_kinr if cost_kinr > 0 else 0.0

            results.append({
                'work_package_id': wp_id,
                'title': wp['title'],
                'cost_inr': wp['cost_inr'],
                'pct_of_budget': round((wp['cost_inr'] / total_budget) * 100.0, 2),
                'target_hypotheses': wp['target_hypotheses'],
                'discriminating_power_bits': eig_bits,
                'cost_efficiency_bits_per_kinr': round(efficiency, 4)
            })

        # Sort descending by diagnostic cost-efficiency
        results.sort(key=lambda x: x['cost_efficiency_bits_per_kinr'], reverse=True)
        return results

    def get_hypothesis_coverage(self) -> Dict[str, Any]:
        """
        Audits which funded work packages cover which hypotheses.
        """
        coverage = {h_id: [] for h_id in self.hypotheses.keys()}
        for wp_id, wp in self.work_packages.items():
            for h in wp['target_hypotheses']:
                if h in coverage:
                    coverage[h].append(wp_id)
                elif h == 'ALL':
                    for k in coverage.keys():
                        coverage[k].append(wp_id)

        uncovered = [h for h, wps in coverage.items() if len(wps) == 0]

        return {
            'hypotheses_count': len(self.hypotheses),
            'work_packages_count': len(self.work_packages),
            'total_fee_inr': sum(wp['cost_inr'] for wp in self.work_packages.values()),
            'coverage_map': coverage,
            'uncovered_hypotheses': uncovered,
            'is_fully_covered': bool(len(uncovered) == 0)
        }
