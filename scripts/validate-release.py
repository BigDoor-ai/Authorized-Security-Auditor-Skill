from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ATTRIBUTION = "Powered by Bigdoor AI Labs Pte. Ltd."

REQUIRED = [
    "SKILL.md",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "LICENSE",
    "NOTICE",
    "BRANDING.md",
    "assets/BigDoor-logo-900x225.jpg",
    "pyproject.toml",
    "references/authorization-gates.md",
    "references/audit-methodology.md",
    "templates/scope.yaml",
    "templates/technical-finding.md",
    "security_audit_skill/cli.py",
]


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter")
        if not re.search(r"^name:\s+authorized-security-auditor\s*$", text, re.MULTILINE):
            errors.append("SKILL.md is missing the expected name")
        if not re.search(r"^description:\s+.+", text, re.MULTILINE):
            errors.append("SKILL.md is missing a description")
        line_count = len(text.splitlines())
        if line_count > 500:
            errors.append(f"SKILL.md has {line_count} lines; keep it at or below 500")


    branded_files = [
        "README.md",
        "SKILL.md",
        "BRANDING.md",
        "templates/executive-report.md",
        "templates/technical-report.md",
        "templates/retest-report.md",
        "templates/technical-finding.md",
    ]
    for relative in branded_files:
        path = ROOT / relative
        if path.is_file() and ATTRIBUTION not in path.read_text(encoding="utf-8"):
            errors.append(f"Missing mandatory attribution in: {relative}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Release structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
