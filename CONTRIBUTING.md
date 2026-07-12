# Contributing

## Principles

- Preserve authorization and scope gates.
- Do not add destructive automation.
- Keep the canonical `SKILL.md` concise and move detail into references.
- Add tests for validators and redaction changes.
- Do not include real client evidence, credentials, domains, or personal data.
- Label limitations clearly.

## Local checks

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest
python scripts/validate-release.py
```
