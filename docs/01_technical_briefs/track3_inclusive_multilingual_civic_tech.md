# Technical Brief: Track 3 - Inclusive and Multilingual Electoral/Civic Technology

## Challenge
Remove barriers to participation: language, disability, digital literacy, distance, low connectivity.

## Example problem statements
- **3A. Voter-information assistant:** answers only from approved, cited sources in English, Pidgin, Hausa, Yoruba, Igbo (+ others), text and voice.
- **3B. Low-bandwidth channels:** SMS/USSD/IVR or offline-first PWA versions of key information.
- **3C. Assistive interfaces:** screen-reader-first, high-contrast, large-print, sign-language-friendly or easy-read content.
- **3D. Digital literacy coach:** short guided lessons on registration, checking a polling unit, and spotting fake messages.
- **3E. Accessibility mapper:** crowdsourced (consent-based) reporting of venue barriers.

## Approaches
Retrieval-augmented generation restricted to an approved corpus (or pure retrieval), multilingual embeddings, speech-to-text/text-to-speech evaluation, WCAG 2.2 AA, plain-language rewriting with human review, progressive web apps.

## Data
Starter: `voter_info_faq_multilingual.csv` (Hausa/Yoruba/Igbo empty: recruit native-speaker reviewers), `accessibility_barriers_survey_synthetic.csv`, `polling_units_synthetic.csv`.

## Success criteria
Answer accuracy vs approved sources; hallucination rate (target: zero unsupported answers); per-language quality with native reviewer sign-off; WCAG audit results; usability test with real users from target groups (with consent); works on low-end phones and 2G.

## Red lines
No invented electoral rules or dates; no generating advice that could disenfranchise; no collecting disability data without consent and need.
