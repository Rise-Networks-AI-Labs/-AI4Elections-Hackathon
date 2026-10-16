# #AI4Elections Hackathon: Public Repository

**Artificial Intelligence for Electoral Innovation, Integrity and Inclusion**

The **#AI4Elections Hackathon** is a nonpartisan, design-and-develop competition organised by **Rise Networks** from October 2026 to February 2027. Participants will develop working, responsible AI prototypes that address challenges related to Nigeria's electoral and civic processes.

> Institutional partners are named only with written permission. Participation by any institution does not imply endorsement. Winning does not constitute approval for operational deployment.

## Start Here

Participants should begin with the following resources:

1. **Participant Onboarding Guide** - `docs/03_onboarding/onboarding_guide.md`
   Timeline, preparation checklist, code of conduct and participant guidance.

2. **Technical Challenge Briefs** - `docs/01_technical_briefs/`
   General challenge rules and detailed briefs for each track.

3. **Technical Curriculum and Resources** - `docs/02_curriculum/`
   Learning modules, technical resources and recommended materials.

4. **Pre-Technical Bootcamps** - `docs/04_bootcamps/`
   Technical bootcamp plans and learning activities.

5. **Synthetic Starter Data Pack** - `data/synthetic/`
   Fictional datasets for experimentation, testing and prototype development, together with the data dictionary.

6. **Starter Notebooks** - `notebooks/`
   Practical examples and baseline workflows to help participants get started.

7. **Developer Documentation Templates** - `docs/05_templates/`
   Templates for project documentation, architecture, model cards, datasheets, safety, APIs and evaluation.

## Challenge Tracks

| Track | Challenge Area                                  | Starter Notebook |
| ----- | ----------------------------------------------- | ---------------- |
| 1     | AI and Electoral Information Integrity          | 01               |
| 2     | Electoral Data Intelligence                     | 02               |
| 3     | Inclusive and Multilingual Civic Tech           | 03               |
| 4     | Electoral Cybersecurity and Resilience          | 05               |
| 5     | Election Observation and Citizen Accountability | 04               |

## Getting Started

Participants can set up the starter environment using the following commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tools/generate_synthetic_data.py
jupyter notebook notebooks/
```

Windows users may activate the virtual environment with:

```bash
.venv\Scripts\activate
```

Participants who do not have access to a suitable local development environment may use platforms such as Google Colab or GitHub Codespaces, subject to availability.

## Repository Structure

The repository contains the following main sections:

* **data/** - Synthetic starter datasets and supporting documentation.
* **docs/** - Challenge briefs, curriculum, onboarding materials, bootcamp resources and documentation templates.
* **notebooks/** - Starter notebooks and technical examples.
* **src/** - Helper code and data-loading utilities.
* **tools/** - Scripts for generating and working with the starter materials.
* **requirements.txt** - Python dependencies for the starter environment.
* **LICENSE** - Repository licensing information.

## Key Principles

All participants are expected to:

* Build nonpartisan solutions.
* Use synthetic, public or properly authorised data.
* Never access, test or interfere with live electoral systems or institutional infrastructure.
* Keep humans involved in decisions where automated systems may affect people.
* Develop working prototypes rather than idea-only proposals.
* Clearly document the limitations, assumptions and risks of their solutions.
* Respect applicable data protection, security, accessibility and open-source requirements.

## Team Submissions

Teams should follow the official submission instructions provided by the organisers.

Participants should use the documentation templates and technical resources provided in this repository when developing and documenting their prototypes.

The prototype submission deadline is **22 December 2026**.

## Licences

Unless otherwise stated:

* **Code:** MIT License
* **Documentation and synthetic data:** CC BY 4.0

The organisers reserve the right to update licensing information where necessary.

## Contact

**Rise Networks**

Website: ai4elections.risenetworks.org

Official programme email and community channel details will be provided by the organisers.
