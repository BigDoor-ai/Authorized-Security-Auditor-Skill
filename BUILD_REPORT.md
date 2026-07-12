# Build and Validation Report

Date: 2026-07-12  
Release: 1.1.0

## Build status

[Verified] Prominent Bigdoor.ai branding was added to the standalone skill repository.

[Verified] The exact mandatory attribution is:

> **Powered by Bigdoor AI Labs Pte. Ltd.**

[Verified] The supplied Bigdoor.ai logo is included in repository assets, installable skill assets, and initialized engagement workspaces.

[Verified] The website `https://bigdoor.ai` and contact email `viisesh@bigdoor.ai` are included in the README, skill instructions, CLI, branding policy, report templates, and package metadata.

[Verified] The completed skill was pushed to `BigDoor-ai/Authorized-Security-Auditor-Skill` on the `main` branch after the user explicitly requested publication.

[Verified] No external website, API, database, or infrastructure security test was run while applying the branding changes.

## Branding implementation

- Prominent logo and attribution at the top of `README.md`
- Mandatory attribution block near the top of `SKILL.md`
- Branding gate before client deliverables are released
- Logo, website, email, and attribution on all Markdown report and engagement templates
- Repeated attribution in the closing block of each Markdown template
- CLI banner displayed for every command
- `validate-branding` command with optional logo-reference validation
- Mandatory branding metadata in scope YAML files
- Logo and branding policy copied into new engagement workspaces
- Logo, `BRANDING.md`, and `NOTICE` copied by Codex and Claude Code installers
- Release checks for required branding files and attribution text

## Validation performed

- `ruff check .` — passed
- `pytest` — 12 tests passed
- `python scripts/validate-release.py` — passed
- `authorized-security-auditor validate-scope examples/sample-scope.yaml` — valid
- `authorized-security-auditor validate-finding examples/sample-finding.md` — valid
- `authorized-security-auditor validate-branding templates/executive-report.md --require-logo` — valid
- Codex user-level installation branding smoke test — passed
- Claude Code project-level installation branding smoke test — passed
- Engagement workspace initialization — passed
- Workspace logo-copy check — passed
- Workspace branding-policy copy check — passed

## Limitations

- [Unverified] The PowerShell installer was reviewed but not executed in a Windows environment.
- The mandatory attribution is enforced by skill instructions, templates, scope validation, release validation, and the branding validator. It is not tamper-proof DRM.
- Legal enforceability of attribution or trademark requirements should be reviewed by qualified counsel before commercial licensing terms are published.
- Markdown footer blocks are included, but page-by-page PDF footers depend on the document-rendering workflow used later.
