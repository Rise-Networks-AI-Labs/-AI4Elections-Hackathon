# Technical Brief: Track 1 - AI and Electoral Information Integrity

## Challenge
Help people and fact-checkers detect, assess and respond to AI-generated or manipulated electoral information: synthetic media, impersonation and misleading content, especially in Nigerian languages and on WhatsApp-like channels.

## Who it serves
Fact-checkers, newsrooms, election observers, CSOs, and ordinary voters.

## Example problem statements (final ones to be validated with subject-matter experts)
- **1A. Claim triage:** rank incoming claims by likely harm and check-worthiness so limited fact-checkers see the riskiest first.
- **1B. Claim matching:** find whether a new viral message matches an already fact-checked claim (multilingual, paraphrase-robust).
- **1C. Provenance:** help publishers attach and verify content-provenance information (e.g. C2PA-style manifests) for official communications.
- **1D. Synthetic media screening assistant:** guide users through verification steps (reverse image search prompts, metadata inspection) rather than issuing a fake/real verdict.

## Suggested technical approaches
Text classification and retrieval (TF-IDF baseline -> multilingual embeddings), semantic similarity search over fact-check archives, metadata/provenance inspection, human-in-the-loop review queues, confidence-based abstention, explainable evidence display.

## Data
Starter: `misinformation_claims_synthetic.jsonl`. Real published fact-checks may be used if licence permits and personal data is excluded. Do not generate or distribute realistic election deepfakes; use clearly labelled, harmless samples.

## Success criteria
| Metric | Why |
|---|---|
| Precision/recall per language (en, pcm, +others) | Avoid English-only bias |
| Calibration and abstention rate | Knowing when to defer to humans |
| Time-to-triage saved for a reviewer (simulated) | Practical value |
| Robustness to paraphrase / typos / code-switching | Real-world messiness |

## Red lines
No tool that auto-removes or publicly labels individuals' speech as false without human review. No political-opinion profiling. No creation of deceptive content.

## Risks to address in your Safety doc
False positives silencing legitimate speech; bias against dialects; adversarial evasion; misuse of your detector to attack opponents.
