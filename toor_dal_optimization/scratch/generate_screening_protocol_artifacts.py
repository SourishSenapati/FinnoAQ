"""
Generate pre-registered 4-condition randomized experimental template and protocol documents.
Strictly adheres to Phase 3 of the Master Directive.
"""
import random
import csv
import os

def generate_screening_artifacts():
    random.seed(20261015)
    
    # Blind coding mapping
    blind_codes = [
        "BLD-74A", "BLD-19B", "BLD-83C", "BLD-42D",
        "BLD-91E", "BLD-26F", "BLD-65G", "BLD-38H",
        "BLD-57J", "BLD-14K", "BLD-89L", "BLD-63M",
        "BLD-29N", "BLD-72P", "BLD-45Q", "BLD-98R"
    ]
    random.shuffle(blind_codes)

    conditions = [
        ('C1-CTRL', 'Untreated Control', 'None', 0.0, 0, 0.0, 'None'),
        ('C2-H2O', 'Water-Only Soaked', 'Potable Soft Water', 0.0, 30, 30.0, '30.0g Potable Soft Water Mist Spray'),
        ('C3-BIC025', '0.25% w/w NaHCO3 in Liquor', 'Food-Grade NaHCO3', 0.25, 30, 30.0, '30.0g Potable Soft Water Mist Spray'),
        ('C4-BIC050', '0.50% w/w NaHCO3 in Liquor', 'Food-Grade NaHCO3', 0.50, 30, 30.0, '30.0g Potable Soft Water Mist Spray'),
    ]

    batches = []
    for cond_id, desc, chem, conc, soak_t, rinse_g, rinse_m in conditions:
        for rep in range(1, 5):
            batches.append({
                'condition_id': cond_id,
                'condition_desc': desc,
                'reagent_name': chem,
                'solution_conc_w_w_pct': conc,
                'soak_time_min': soak_t,
                'rinse_water_mass_g': rinse_g,
                'rinse_method': rinse_m,
                'replicate_num': rep,
                'batch_id': f'{cond_id}-{rep:02d}',
            })

    # Pre-registered randomization
    random.shuffle(batches)
    for idx, b in enumerate(batches, 1):
        b['randomized_run_order'] = idx
        b['blind_sample_code'] = blind_codes[idx - 1]

    batches.sort(key=lambda x: x['randomized_run_order'])

    fieldnames = [
        'randomized_run_order',
        'blind_sample_code',
        'batch_id',
        'condition_id',
        'condition_desc',
        'replicate_num',
        'raw_dal_lot_id',
        'raw_dal_initial_moisture_wb_pct',
        'raw_dal_mass_g',
        'reagent_name',
        'reagent_fcc_grade_verified',
        'solution_conc_w_w_pct',
        'soak_liquor_ratio',
        'soak_liquor_mass_g',
        'soak_water_temp_c',
        'soak_water_ph',
        'soak_water_tds_ppm',
        'soak_duration_min',
        'drained_wet_mass_g',
        'rinse_water_mass_g',
        'rinse_method',
        'post_rinse_drained_wet_mass_g',
        'absorbed_water_g',
        'drained_liquor_effluent_mass_g',
        'dryer_temp_c',
        'dryer_time_min',
        'dried_dal_mass_g',
        'dry_solids_recovery_pct',
        'post_condition_moisture_wb_pct',
        'water_activity_aw',
        'cook_dal_mass_g',
        'cook_water_mass_g',
        'induction_power_watts',
        't0_heat_on_timestamp',
        't_vent_steady_steam_s',
        'whistle_1_time_s',
        'whistle_2_time_s',
        'whistle_3_time_s',
        'whistle_4_time_s',
        'whistle_5_time_s',
        'whistle_6_time_s',
        'exact_cooking_time_min',
        'whistles_at_endpoint',
        'assessor_1_score_0_to_2',
        'assessor_2_score_0_to_2',
        'assessor_disagreement_flag',
        'consensus_tactile_score_0_to_2',
        'chalky_core_pct',
        'cooked_expansion_ratio',
        'sensory_appearance_1_to_9',
        'sensory_texture_1_to_9',
        'sensory_flavor_1_to_9',
        'sensory_overall_1_to_9',
        'retained_na_mg_per_100g',
        'operator_name',
        'test_date',
        'notes'
    ]

    out_csv = 'data/kitchen_screening_4conditions_template.csv'
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for b in batches:
            row = {
                'randomized_run_order': b['randomized_run_order'],
                'blind_sample_code': b['blind_sample_code'],
                'batch_id': b['batch_id'],
                'condition_id': b['condition_id'],
                'condition_desc': b['condition_desc'],
                'replicate_num': b['replicate_num'],
                'raw_dal_lot_id': 'TZ-2026-IMP-001',
                'raw_dal_initial_moisture_wb_pct': '',
                'raw_dal_mass_g': 200.0,
                'reagent_name': b['reagent_name'],
                'reagent_fcc_grade_verified': 'YES (FCC / Food Grade INS 500(ii))' if 'NaHCO3' in b['reagent_name'] else 'N/A',
                'solution_conc_w_w_pct': b['solution_conc_w_w_pct'],
                'soak_liquor_ratio': 1.50 if b['soak_time_min'] > 0 else 0.0,
                'soak_liquor_mass_g': 300.0 if b['soak_time_min'] > 0 else 0.0,
                'soak_water_temp_c': '',
                'soak_water_ph': '',
                'soak_water_tds_ppm': '',
                'soak_duration_min': b['soak_time_min'],
                'drained_wet_mass_g': '',
                'rinse_water_mass_g': b['rinse_water_mass_g'],
                'rinse_method': b['rinse_method'],
                'post_rinse_drained_wet_mass_g': '',
                'absorbed_water_g': '',
                'drained_liquor_effluent_mass_g': '',
                'dryer_temp_c': 55.0 if b['soak_time_min'] > 0 else '',
                'dryer_time_min': '',
                'dried_dal_mass_g': '',
                'dry_solids_recovery_pct': '',
                'post_condition_moisture_wb_pct': '',
                'water_activity_aw': '',
                'cook_dal_mass_g': 100.0,
                'cook_water_mass_g': 350.0,
                'induction_power_watts': 1000,
                't0_heat_on_timestamp': '',
                't_vent_steady_steam_s': '',
                'whistle_1_time_s': '',
                'whistle_2_time_s': '',
                'whistle_3_time_s': '',
                'whistle_4_time_s': '',
                'whistle_5_time_s': '',
                'whistle_6_time_s': '',
                'exact_cooking_time_min': '',
                'whistles_at_endpoint': '',
                'assessor_1_score_0_to_2': '',
                'assessor_2_score_0_to_2': '',
                'assessor_disagreement_flag': '',
                'consensus_tactile_score_0_to_2': '',
                'chalky_core_pct': '',
                'cooked_expansion_ratio': '',
                'sensory_appearance_1_to_9': '',
                'sensory_texture_1_to_9': '',
                'sensory_flavor_1_to_9': '',
                'sensory_overall_1_to_9': '',
                'retained_na_mg_per_100g': '',
                'operator_name': '',
                'test_date': '2026-10-16',
                'notes': ''
            }
            writer.writerow(row)

    print(f"Generated {out_csv} with 16 randomized batches and full blinding codes.")

if __name__ == '__main__':
    generate_screening_artifacts()
