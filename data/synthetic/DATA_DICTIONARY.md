# Synthetic Starter Data Pack: Data Dictionary
**All data is fictional.** Party labels A-E, polling unit IDs (`SIM-#####`), incidents, claims and survey respondents do not refer to real parties, places' actual polling units, people or events. States and zones are real geography used only for realism; LGAs/wards are invented labels. Not for inference about real elections.

| File | Rows | Description | Tracks |
|---|---|---|---|
| polling_units_synthetic.csv | 900 | Unit attributes: zone, state, LGA, ward, settlement, registered_voters, accessible_venue, has_grid_power, network_coverage, distance_to_lga_hq_km | 2,3,5 |
| results_synthetic.csv | 900 | pu_id, registered_voters, accredited_voters, votes_A..E, rejected_votes. ~5% have injected inconsistencies | 2,4 |
| anomaly_labels_HELD_OUT.csv | 900 | Answer key for injected anomalies (practice only; use for evaluation, not training your final claims) | 2 |
| voter_info_faq_multilingual.csv | 20 | FAQ questions in English + draft Pidgin; ha/yo/ig empty for community translation; answers are placeholders | 3 |
| misinformation_claims_synthetic.jsonl | 300 | claim_id, text, label (true/false/misleading/unverifiable), language, channel, synthetic_media_attached, spread_score | 1 |
| incident_reports_synthetic.csv | 400 | incident_id, timestamp (fictional date), location ids, category, description, severity_0_4, reporter_type, verified, has_photo_evidence | 5,4 |
| logistics_deliveries_synthetic.csv | 300 | pu_id, distance_km, settlement, vehicle, dispatch_hour, transit_hours, materials_complete | 2,5 |
| accessibility_barriers_survey_synthetic.csv | 500 | Simulated respondents: state, settlement, age_band, gender, disability_type, preferred_language, main_barrier, confidence_finding_info_1_5 | 3,4 |

## Anomaly types in results
`accredited_exceeds_registered`, `sum_mismatch` (votes+rejected != accredited), `digit_transposition`, `suspicious_round_numbers`, `duplicated_from_previous_unit`.

## Notes
- Distributions are simplistic; do not draw conclusions about real geography or behaviour.
