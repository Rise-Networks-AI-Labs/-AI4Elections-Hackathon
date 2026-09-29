# Technical Curriculum and Resource Library

Self-paced modules that feed the pre-technical bootcamps. Each module: **goal, what to learn, hands-on task, resources**. Verify links before publishing; the resources named are well-known public references, but URLs and versions change. **The modules are recommended learning resources, not mandatory technology requirements. Teams should select methods appropriate to their problem, data, prototype and available resources**

## What You Are Expected to Build

The #AI4Elections Hackathon is a Design + Develop competition. Participants are expected to develop a working prototype or technically credible proof of concept that addresses a defined electoral problem within one of the five challenge tracks.

Depending on the track, projects may include:

- Information verification, misinformation analysis, synthetic-media detection or provenance tools.
- Electoral data-analysis, data-quality, anomaly-detection, document-processing or logistics tools.
- Accessible and multilingual voter-information or civic-technology applications.
- Defensive cybersecurity, authorised security simulation, privacy or resilience tools.
- Election-observation, incident-reporting, civic-feedback or public-information tools.

Projects should demonstrate the core functionality of the proposed solution, explain the methodology used, document data sources and handling, identify limitations and risks, and show the safeguards required for further testing.

Idea-only proposals, presentations or mock-ups without a functioning technical component are not sufficient.

## Learning pathway
| Module | Title | Hours | Tracks |
|---|---|---|---|
| M0 | Electoral process 101 for technologists | 3 | All |
| M1 | Responsible AI and ethics in elections | 3 | All |
| M2 | Python and data foundations | 6 | All |
| M3 | ML fundamentals and honest evaluation | 6 | 1,2,3,5 |
| M4 | NLP and multilingual methods | 6 | 1,3,5 |
| M5 | Data quality, anomaly detection, document AI | 5 | 2 |
| M6 | Security, privacy and threat modelling | 5 | 4 (recommended for all) |
| M7 | Accessible and low-bandwidth product design | 4 | 3,5 |
| M8 | Shipping: repo hygiene, docs, demo | 3 | All |

## M0 Electoral process 101
Learn: Key stages of the electoral process, including registration, accreditation, voting, collation, result declaration and dispute resolution; key electoral stakeholders; and the distinction between legally authorised electoral functions and what technology should or should not do. Task: Draw a process map and identify where human or legally authorised institutional decisions are required. Resources: Nigeria's Electoral Act and INEC public guidelines; ACE Electoral Knowledge Network; International IDEA publications on technology in elections.

## M1 Responsible AI
Learn: fairness, transparency, accountability, privacy, safety; model cards and datasheets; human oversight; harm analysis. Task: complete a harm/benefit table for your idea. Resources: Model Cards (Mitchell et al.), Datasheets for Datasets (Gebru et al.), NIST AI Risk Management Framework, Nigeria Data Protection Act 2023, UNESCO Recommendation on the Ethics of AI.

## M2 Python and data foundations
Learn: Python, pandas, matplotlib, git/GitHub, virtual environments, reading CSV/JSONL. Task: Run at least one starter notebook and answer five data questions using the supplied synthetic data. Resources: Python docs tutorial, pandas "10 minutes" guide, Git handbook.

## M3 ML and honest evaluation
Learn: train/validation/test splits, leakage, baselines, precision/recall/F1, calibration, per-group metrics, confidence intervals. Task: improve `notebooks/01` baseline and try to *break* it. Resources: scikit-learn user guide, Google ML crash course, "Hands-On ML" (Geron).

## M4 NLP and multilingual
Learn: tokenisation, TF-IDF, embeddings, retrieval, RAG with citations, low-resource languages, code-switching, speech (ASR/TTS) limits. Task: extend `notebooks/03` with embeddings; measure per-language. Resources: Hugging Face course, sentence-transformers docs, Masakhane community, AfriBERTa/AfroXLMR-family models, Mozilla Common Voice and Google FLEURS (check licences), Lacuna/Masakhane datasets.

## M5 Data quality, anomaly detection, document AI
Learn: validation rules, outlier detection, Isolation Forest, base-rate reasoning, OCR and layout parsing, human review queues. Task: measure alerts per 1,000 records in `notebooks/02`. Resources: Great Expectations docs, scikit-learn outlier detection guide, Tesseract/PaddleOCR docs.

## M6 Security, privacy, threat modelling
Learn: STRIDE, LINDDUN, OWASP Top 10, secrets management, k-anonymity, differential privacy basics, tamper-evident logging, responsible disclosure. Task: write a 1-page threat model for your prototype. Resources: OWASP cheat sheets, Microsoft STRIDE guide, NIST privacy framework, NDPA 2023. **All security practice must use local, synthetic or explicitly authorised environments. Participants must not test live electoral systems or unauthorised institutional infrastructure.**

## M7 Accessibility and low-bandwidth design
Learn: WCAG 2.2 AA, screen readers (NVDA, TalkBack), colour contrast, plain language, offline-first/PWA, SMS/USSD constraints, testing on low-end Android. Task: audit a page with axe/Lighthouse and fix 3 issues. Resources: W3C WCAG quick reference, Inclusive Design Principles, Web.dev PWA guides.

## M8 Shipping
Learn: README, licence choice, reproducible environments, tests, demo scripting. Task: Set up your team's project and get a teammate to run it from scratch using your documentation. Resources: templates in `docs/05_templates/`.

## Tooling list (free tiers, verify availability)
Google Colab / Kaggle notebooks, GitHub Codespaces, Hugging Face Hub, Streamlit / Gradio (quick UIs), FastAPI, SQLite/DuckDB, Docker, Label Studio (annotation). Partner-provided compute credits will be announced separately (in-kind contributions are documented separately from cash).

## Recommended reading order by track
Track 1: M0,M1,M2,M3,M4,M8 | Track 2: M0,M1,M2,M3,M5,M8 | Track 3: M0,M1,M2,M4,M7,M8 | Track 4: M0,M1,M2,M6,M8 | Track 5: M0,M1,M2,M5,M7,M8
