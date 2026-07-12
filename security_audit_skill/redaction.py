from __future__ import annotations

import re

PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}"), "Bearer [REDACTED_TOKEN]"),
    (re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^\s'\",;]{8,}"), "[REDACTED_SECRET]"),
    (re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b"), "[REDACTED_JWT]"),
    (re.compile(r"(?i)\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s]+"), "[REDACTED_CONNECTION_STRING]"),
    (re.compile(r"(?i)\b(?:set-cookie|cookie):\s*[^\r\n]+"), "Cookie: [REDACTED_COOKIE]"),
    (re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE), "[REDACTED_EMAIL]"),
    (re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)"), "[REDACTED_PHONE]"),
    (re.compile(r"(?i)\b(?:sk|pk|rk|ghp|github_pat|xox[baprs])-[_A-Za-z0-9-]{12,}\b"), "[REDACTED_KEY]"),
]


def redact_text(text: str) -> str:
    output = text
    for pattern, replacement in PATTERNS:
        output = pattern.sub(replacement, output)
    return output
