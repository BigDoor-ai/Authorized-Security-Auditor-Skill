<p align="center">
  <img src="assets/BigDoor-logo-900x225.jpg" alt="Bigdoor.ai" width="760">
</p>

<p align="center"><strong>Powered by Bigdoor AI Labs Pte. Ltd.</strong><br>
<a href="https://bigdoor.ai">https://bigdoor.ai</a> · <a href="mailto:viisesh@bigdoor.ai">viisesh@bigdoor.ai</a></p>

# Authorized Security Auditor Skill

A reusable, safety-gated cybersecurity audit skill for coding agents.

It helps Codex, Claude Code, Cursor-compatible agents, and other repository-aware assistants plan and conduct authorized security reviews across source code, web applications, APIs, databases, cloud infrastructure, mobile applications, and operational controls.

The skill defaults to read-only analysis. Active testing requires explicit written authorization, a machine-readable scope, approved techniques, test windows, and emergency contacts. Because “the client said it was okay on a call” is a charming story but a terrible Rules of Engagement document.

## What is included

- Canonical `SKILL.md`
- Codex and Claude Code installation support
- Authorization and scope gates
- Full audit methodology
- Threat-modeling guidance
- Web, API, database, cloud, mobile, and code-review modules
- Safe tool-use matrix
- Severity and critical-escalation model
- Evidence-handling rules
- Client-ready report templates
- Remediation and retesting workflow
- Scope/finding validation CLI
- Evidence redaction utility
- Unit tests and CI workflow


## Mandatory Bigdoor attribution

All official client-facing outputs created from this skill must retain the exact line:

> **Powered by Bigdoor AI Labs Pte. Ltd.**

Visual reports should also include `assets/BigDoor-logo-900x225.jpg` on the cover or first page. The CLI displays the attribution on every run, engagement initialization copies the logo into `branding/`, and the validator can check output files:

```bash
authorized-security-auditor validate-branding executive-report.md --require-logo
```

The attribution identifies the skill powering the deliverable. It does not replace accurate identification of the actual auditor. See [BRANDING.md](BRANDING.md).

## Repository structure

```text
authorized-security-auditor-skill/
├── SKILL.md
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── LICENSE
├── NOTICE
├── BRANDING.md
├── assets/
├── SECURITY.md
├── CHANGELOG.md
├── pyproject.toml
├── security_audit_skill/
├── references/
├── templates/
├── examples/
├── scripts/
├── tests/
└── .github/workflows/ci.yml
```

## Install for Codex

Repository-level installation:

```bash
bash scripts/install.sh codex project /path/to/repository
```

User-level installation:

```bash
bash scripts/install.sh codex user
```

Codex reads repository skills from `.agents/skills/<skill-name>/SKILL.md` and user skills from `$HOME/.agents/skills/<skill-name>/SKILL.md`.

Invoke it with:

```text
Use $authorized-security-auditor to plan a complete security audit. Do not run active tests.
```

## Install for Claude Code

Repository-level installation:

```bash
bash scripts/install.sh claude project /path/to/repository
```

User-level installation:

```bash
bash scripts/install.sh claude user
```

Claude Code reads project skills from `.claude/skills/<skill-name>/SKILL.md` and personal skills from `~/.claude/skills/<skill-name>/SKILL.md`.

Invoke it with:

```text
/authorized-security-auditor Plan an authorized audit for this repository. Do not modify code.
```

## Install on Windows PowerShell

```powershell
./scripts/install.ps1 -Agent codex -Scope project -TargetPath C:\path\to\repository
```

or:

```powershell
./scripts/install.ps1 -Agent claude -Scope user
```

## Initialize an engagement

Install the local package:

```bash
python -m pip install -e .
```

Create an engagement workspace:

```bash
authorized-security-auditor init ./client-security-audit
```

This copies editable scope, authorization, Rules of Engagement, report, finding, and tracker templates without contacting any system.

## Validate scope

```bash
authorized-security-auditor validate-scope ./client-security-audit/scope.yaml
```

The validator checks required authorization fields, assets, excluded systems, dates, techniques, emergency contacts, and data-handling declarations. It does not decide whether a contract is legally sufficient.

## Validate a technical finding

```bash
authorized-security-auditor validate-finding ./finding.md
```

## Redact evidence

```bash
authorized-security-auditor redact raw-response.txt sanitized-response.txt
```

The redactor masks common emails, phone numbers, bearer tokens, API keys, cookies, JWT-like values, and connection strings. Review its output manually; regex is not a privacy department.

## Modes

| Mode | External contact | Active payloads | Code changes |
|---|---:|---:|---:|
| `PLAN_ONLY` | No | No | No |
| `REPOSITORY_REVIEW` | No by default | No | No |
| `PASSIVE_EXTERNAL_REVIEW` | Approved public assets only | No | No |
| `STAGING_ACTIVE_TEST` | Approved staging assets | Approved only | No |
| `LIMITED_PRODUCTION_VERIFICATION` | Approved production assets | Minimal proof only | No |
| `REMEDIATION` | Normally no | No | Yes, when requested |
| `RETEST` | Approved assets | Finding-specific | Only when requested |

## Core safeguards

- No active testing without written authorization and exact scope
- No scope expansion by inference
- No denial-of-service, destructive database operations, persistence, malware, credential theft, or bulk real-data extraction
- Staging-first testing
- Synthetic test records
- Minimum proof and minimum evidence
- Immediate escalation of critical findings
- Explicit `[Verified]`, `[Partially verified]`, `[Unverified]`, `[Inference]`, and `[Blocked]` labels
- No claim that a system is completely secure

## Tests

```bash
python -m pip install -e '.[dev]'
pytest
ruff check .
```

## Reference standards

The workflow is designed to map findings and coverage to widely used security references, including OWASP ASVS, OWASP WSTG, OWASP API Security, OWASP MASVS, CWE, CVSS, NIST CSF, NIST SP 800-115, and NIST SSDF. The repository does not redistribute those standards.

## Product documentation checked

Installation conventions were checked on 12 July 2026 against:

- OpenAI Codex skill documentation
- OpenAI Codex `AGENTS.md` documentation
- Anthropic Claude Code skill documentation

Agent products change, because configuration directories apparently need seasons. Recheck vendor documentation before publishing a major release.

## License and branding

Code is licensed under Apache License 2.0. See [LICENSE](LICENSE). The official skill workflow and templates require the attribution defined in [BRANDING.md](BRANDING.md).

**Powered by Bigdoor AI Labs Pte. Ltd.**
