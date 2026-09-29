# Contributing and Code Style (team template)

- Branching: `main` stable, feature branches `feat/<name>`, pull requests with one reviewer.
- Commits: imperative, small, reference issue IDs.
- Python: PEP 8, type hints on public functions, docstrings, `ruff`/`black` optional. Tests with `pytest` for core logic.
- Notebooks: clear outputs before commit unless demonstrating results; no secrets, no personal data.
- Secrets: environment variables or `.env` (gitignored). Never commit keys.
- Dependencies: pin versions in `requirements.txt`; prefer maintained, permissively licensed libraries.
- Docs: update README and API docs with every behavioural change.
- Licence: choose one (MIT/Apache-2.0 for code, CC BY 4.0 for docs/data) and add `LICENSE`.
- AI assistance: note in README which parts were AI-assisted and how you verified them.
