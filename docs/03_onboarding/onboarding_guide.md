# Participant Onboarding Guide

Welcome to the **#AI4Elections Hackathon**: build working, responsible AI for electoral integrity, transparency and inclusion in Nigeria.

## 1. Timeline at a glance
| Date (2026) | Milestone |
|---|---|
| 8 Oct | Applications open |
| 29 Oct, 11:59pm WAT | Applications close |
| 30 Oct - 6 Nov | Eligibility checks and screening |
| 9-10 Nov | Shortlist notification |
| 11-13 Nov | Team formation and track allocation |
| **14 Nov** | **Onboarding and kickoff** |
| 16-20 Nov | Problem validation, design, technical bootcamps, mentor matching |
| 21-30 Nov | Prototype sprint, mentor check-ins and clinics |
| **30 Nov** | **Prototype submission** |
| Dec | Judging, national finale and awards |
| Jan-Feb 2027 | Testing, mentorship, pilot discussions for selected teams |

## 2. Before kickoff (checklist)
- [ ] Confirmation email received; accept your place within the stated window
- [ ] Government ID and any organisation/institution documents ready (see eligibility)
- [ ] Team of 1-4 finalised (each member registered individually; **team membership cannot change after the hackathon begins**)
- [ ] GitHub account; join the hackathon organisation and community channel
- [ ] Read: General Rules, your Track Brief, Code of Conduct summary below
- [ ] Set up environment (Section 4) and run `notebooks/02`
- [ ] Nominate a team contact and a prize recipient (agree distribution in writing)

## 3. Eligibility reminders
Nigerian participants aged 18+ (supervised youth pathway for younger participants). Academic teams need a faculty lead, a student/postgraduate researcher and an HOD approval letter. Organisations need CAC registration, at least 60% of team resident in Nigeria, and IDs for all members. Individuals need a valid government ID and ID of any affiliated organisation. All submissions in English. Idea-only proposals, mock-ups and projects that already won grants/awards elsewhere are ineligible.

## 4. Environment setup
```bash
git clone https://github.com/Rise-Networks-AI-Labs/-AI4Elections-Hackathon && cd ai4elections
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python tools/generate_synthetic_data.py             # regenerates the data pack
jupyter-notebook notebooks/
```
No laptop? Use Google Colab or GitHub Codespaces; ask mentors about partner compute credits.

## 5. Code of Conduct (summary; full version to be signed by every participant)
1. Be respectful, inclusive and nonpartisan; no harassment or discrimination.
2. No unauthorised access or testing of any live electoral system or institutional infrastructure.
3. Use only synthetic, public or authorised data; protect personal information.
4. No deceptive content, political persuasion or microtargeting.
5. Credit others' work and follow open-source licences; disclose AI-tool assistance in your docs.
6. Report concerns to the organisers (channel and contact to be inserted).
Breaches can lead to disqualification.

## 6. How you will be supported
Mentors (technical, electoral, accessibility, legal/data-protection) hold clinics 21-30 Nov. Book via the mentor sign-up sheet. Judges do not score teams they mentored.

## 7. Submission checklist (30 Nov)
See `docs/01_technical_briefs/00_general_challenge_rules.md`. Final deadline time to be confirmed by organisers.

## 8. Communication
Announcements channel (read-only), team-help channel, and track channels. Response SLA for organisers: to be confirmed.

## 9. Intellectual property and openness
IP terms will be published before the competition. Teams are encouraged to use open licences for components. Confirm terms in the participant agreement before you start.

## 10. Wellbeing and access
Tell us about accessibility needs at registration so we can arrange support.
