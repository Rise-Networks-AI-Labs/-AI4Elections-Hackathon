# Technical Brief: Track 2 - Electoral Data Intelligence

## Challenge
Apply responsible AI to *authorised, public or synthetic* electoral data: improve data quality, process public documents, support logistics analysis, and surface anomalies **for human review**.

## Hard rule
Solutions must **not** independently declare results or replace legally authorised processes. Every output is a flag, forecast of workload or a summary that a human can check.

## Example problem statements
- **2A. Data-quality checker:** validate result-sheet style records for arithmetic and consistency errors (start with `notebooks/02`).
- **2B. Document intelligence:** extract structured fields from public, scanned or PDF electoral documents (OCR + layout + validation).
- **2C. Logistics modelling:** predict delivery delays and propose staffing/route plans on simulated data.
- **2D. Anomaly explainer:** for each flagged record, explain *why* in plain language and list benign explanations.

## Approaches
Rule engines + statistical outlier detection, Benford-style digit tests (treat cautiously, as they produce false alarms), OCR pipelines, forecasting/optimisation for logistics, dashboards with audit trails.

## Data
Starter: `polling_units_synthetic.csv`, `results_synthetic.csv`, `logistics_deliveries_synthetic.csv`, `anomaly_labels_HELD_OUT.csv` (practice only; real data has no answer key). Only public/authorised real datasets.

## Success criteria
Precision/recall against injected anomalies, reviewer workload (alerts per 1,000 records), explanation quality, reproducibility, audit logging, clear statement of statistical limits.

## Red lines
No fraud accusations; no predicting winners for persuasion; no re-identifying individuals; no use of unauthorised results data.

## Pitfalls
Base-rate fallacy (rare anomalies + imperfect detector = many false alarms), natural variation flagged as fraud, overfitting to synthetic patterns.
