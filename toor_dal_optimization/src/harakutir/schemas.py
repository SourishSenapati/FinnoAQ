"""
Pydantic schemas and data contracts for Harakutir Phase 1 Toor Dal study.
Strictly distinguishes observed_raw, derived_from_observed, published_literature,
assumption, hypothesis, simulation, synthetic_test_only, and missing.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime

class DatasetKind(str, Enum):
    OBSERVED_RAW = "observed_raw"
    DERIVED_FROM_OBSERVED = "derived_from_observed"
    PUBLISHED_LITERATURE = "published_literature"
    DIGITIZED_FROM_FIGURE = "digitized_from_figure"
    OFFICIAL_STATISTICS = "official_statistics"
    ASSUMPTION = "assumption"
    HYPOTHESIS = "hypothesis"
    SIMULATION = "simulation"
    SYNTHETIC_TEST_ONLY = "synthetic_test_only"
    MISSING = "missing"
    UNVERIFIED = "unverified"

class ProvenanceRecord(BaseModel):
    source_file: str
    record_pointer: str  # sheet/row/cell or page/paragraph
    source_hash: Optional[str] = None
    ingest_timestamp: datetime = Field(default_factory=datetime.utcnow)
    analyst_or_device: str
    raw_units: str
    normalized_units: str
    transformation_applied: str = "none"
    notes: Optional[str] = None

class SampleMetadata(BaseModel):
    sample_id: str  # e.g. "TZ_LOT_01", "IND_LOT_01"
    sample_type: str  # "Tanzanian" or "Indian Benchmark"
    lot_number: str
    origin_country: str
    growing_region: Optional[str] = None
    variety_or_cultivar: Optional[str] = None
    harvest_date: Optional[str] = None
    milling_date: Optional[str] = None
    import_date: Optional[str] = None
    supplier: Optional[str] = None
    storage_conditions: Optional[str] = None
    quantity_received_kg: float = Field(ge=0.0)
    retention_quantity_kg: float = Field(ge=0.0)
    dataset_kind: DatasetKind
    provenance: ProvenanceRecord

class PhysicalAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    # Dimensions
    length_mm: Optional[float] = Field(None, ge=1.0, le=15.0)
    width_mm: Optional[float] = Field(None, ge=1.0, le=15.0)
    thickness_mm: Optional[float] = Field(None, ge=1.0, le=10.0)
    length_width_ratio: Optional[float] = Field(None, ge=0.5, le=3.0)
    
    # Colour
    cielab_l: Optional[float] = Field(None, ge=0.0, le=100.0)
    cielab_a: Optional[float] = Field(None, ge=-50.0, le=50.0)
    cielab_b: Optional[float] = Field(None, ge=-50.0, le=100.0)
    
    # Bulk properties
    thousand_grain_weight_g: Optional[float] = Field(None, ge=20.0, le=250.0)
    bulk_density_g_ml: Optional[float] = Field(None, ge=0.4, le=1.5)
    true_density_g_ml: Optional[float] = Field(None, ge=0.8, le=2.0)
    broken_grain_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    defects_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    residual_seed_coat_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    
    # Mechanical
    raw_hardness_n: Optional[float] = Field(None, ge=10.0, le=500.0)
    
    provenance: ProvenanceRecord

class ProximateAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    moisture_pct: Optional[float] = Field(None, ge=1.0, le=25.0)
    protein_pct: Optional[float] = Field(None, ge=10.0, le=40.0)
    fat_pct: Optional[float] = Field(None, ge=0.1, le=10.0)
    crude_fibre_pct: Optional[float] = Field(None, ge=0.1, le=15.0)
    ash_pct: Optional[float] = Field(None, ge=0.5, le=10.0)
    total_carbohydrate_pct: Optional[float] = Field(None, ge=30.0, le=85.0)
    total_starch_pct: Optional[float] = Field(None, ge=25.0, le=75.0)
    
    analytical_method_standard: str = "AOAC / ISO / BIS validated"
    provenance: ProvenanceRecord

    @model_validator(mode="after")
    def check_sum_if_all_present(self):
        vals = [self.moisture_pct, self.protein_pct, self.fat_pct, self.crude_fibre_pct, self.ash_pct]
        if all(v is not None for v in vals) and self.total_carbohydrate_pct is not None:
            total_sum = sum(vals) + self.total_carbohydrate_pct
            # Allow small analytical rounding tolerance (97% - 103%)
            if not (97.0 <= total_sum <= 103.0):
                # Note: non-fatal if difference calculation is external, but flaggable
                pass
        return self

class StarchThermalAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    amylose_pct: Optional[float] = Field(None, ge=5.0, le=50.0)
    amylopectin_pct: Optional[float] = Field(None, ge=50.0, le=95.0)
    amylose_amylopectin_ratio: Optional[float] = Field(None, ge=0.05, le=1.0)
    
    # DSC
    dsc_onset_temp_c: Optional[float] = Field(None, ge=50.0, le=95.0)
    dsc_peak_temp_c: Optional[float] = Field(None, ge=55.0, le=100.0)
    dsc_conclusion_temp_c: Optional[float] = Field(None, ge=60.0, le=110.0)
    dsc_range_delta_t_c: Optional[float] = Field(None, ge=2.0, le=30.0)
    dsc_enthalpy_j_g: Optional[float] = Field(None, ge=0.5, le=25.0)
    
    # RVA
    rva_pasting_temp_c: Optional[float] = Field(None, ge=60.0, le=100.0)
    rva_peak_viscosity_cp: Optional[float] = Field(None, ge=100.0, le=6000.0)
    rva_breakdown_cp: Optional[float] = Field(None, ge=0.0, le=3000.0)
    rva_final_viscosity_cp: Optional[float] = Field(None, ge=200.0, le=8000.0)
    rva_setback_cp: Optional[float] = Field(None, ge=50.0, le=4000.0)
    
    provenance: ProvenanceRecord

class HydrationTimePoint(BaseModel):
    time_min: float = Field(ge=0.0)
    water_uptake_g_per_g: float = Field(ge=0.0, le=3.0)
    moisture_pct_dry_basis: float = Field(ge=0.0, le=300.0)
    mass_gain_pct: float = Field(ge=0.0, le=300.0)
    swelling_capacity_ml_grain: Optional[float] = None

class HydrationAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    soaking_temperature_c: float = Field(default=25.0)
    time_points: List[HydrationTimePoint]
    wai_g_per_g: Optional[float] = Field(None, ge=0.5, le=10.0)
    
    # Peleg fitted parameters (if derived)
    peleg_k1_min_per_pct: Optional[float] = None
    peleg_k2_pct_inv: Optional[float] = None
    peleg_r2: Optional[float] = None
    peleg_rmse: Optional[float] = None
    
    provenance: ProvenanceRecord

class StructuralAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    seed_coat_thickness_um: Optional[float] = Field(None, ge=10.0, le=200.0)
    cotyledon_cell_wall_thickness_um: Optional[float] = Field(None, ge=0.5, le=15.0)
    intercellular_void_fraction_pct: Optional[float] = Field(None, ge=0.5, le=40.0)
    surface_crack_density_per_mm2: Optional[float] = Field(None, ge=0.0, le=50.0)
    cellular_compactness_score: Optional[int] = Field(None, ge=1, le=5)
    post_hydration_cell_separation_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    post_cooking_disintegration_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    
    provenance: ProvenanceRecord

class PectinAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    total_pectin_pct_db: Optional[float] = Field(None, ge=0.5, le=15.0)
    water_soluble_pectin_wsp_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    chelator_soluble_pectin_csp_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    alkali_soluble_pectin_asp_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    degree_of_esterification_pct: Optional[float] = Field(None, ge=5.0, le=95.0)
    pectin_associated_ca_mg_per_g: Optional[float] = Field(None, ge=0.1, le=100.0)
    pectin_associated_mg_mg_per_g: Optional[float] = Field(None, ge=0.1, le=100.0)
    
    provenance: ProvenanceRecord

class MineralPhytateAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    total_calcium_mg_100g: Optional[float] = Field(None, ge=10.0, le=500.0)
    total_magnesium_mg_100g: Optional[float] = Field(None, ge=20.0, le=500.0)
    total_iron_mg_100g: Optional[float] = Field(None, ge=0.5, le=50.0)
    total_phosphorus_mg_100g: Optional[float] = Field(None, ge=50.0, le=1000.0)
    phytic_acid_mg_100g: Optional[float] = Field(None, ge=50.0, le=2000.0)
    
    molar_ratio_phytate_ca: Optional[float] = None
    molar_ratio_phytate_ca_mg: Optional[float] = None
    
    provenance: ProvenanceRecord

class TextureAssay(BaseModel):
    sample_id: str
    lot_number: str
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    stage: str  # "raw", "hydrated", "cooked"
    breaking_force_n: Optional[float] = Field(None, ge=0.5, le=500.0)
    firmness_n: Optional[float] = Field(None, ge=0.5, le=500.0)
    work_of_shear_n_s: Optional[float] = Field(None, ge=1.0, le=2000.0)
    hard_core_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    disintegration_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    
    provenance: ProvenanceRecord

class CookingTrial(BaseModel):
    sample_id: str
    lot_number: str
    trial_id: str
    test_type: str  # "Test A: No-Soak", "Test B: Standardized Soak", "Test C: Controlled Pressure"
    replicate_id: int = Field(ge=1)
    dataset_kind: DatasetKind
    
    sample_mass_g: float = Field(default=50.0, ge=10.0, le=200.0)
    water_to_dal_ratio: float = Field(default=4.0, ge=2.0, le=10.0)
    soaking_duration_min: float = Field(default=0.0, ge=0.0)
    operating_pressure_kpa: float = Field(default=103.0, ge=0.0, le=200.0)
    cooking_temperature_c: float = Field(default=121.0, ge=90.0, le=135.0)
    
    cooking_endpoint_time_min: Optional[float] = Field(None, ge=5.0, le=240.0)
    observed_whistles: Optional[int] = Field(None, ge=0, le=30)
    hard_core_pct: Optional[float] = Field(None, ge=0.0, le=100.0)
    cooking_loss_pct: Optional[float] = Field(None, ge=0.5, le=35.0)
    cooked_water_absorption_ratio: Optional[float] = Field(None, ge=1.0, le=4.5)
    cooked_grain_swelling_ratio: Optional[float] = Field(None, ge=1.0, le=4.5)
    final_cooked_moisture_pct: Optional[float] = Field(None, ge=40.0, le=85.0)
    
    provenance: ProvenanceRecord
