from __future__ import annotations

from pathlib import Path

ATTRIBUTION = "Powered by Bigdoor AI Labs Pte. Ltd."
WEBSITE = "https://bigdoor.ai"
EMAIL = "viisesh@bigdoor.ai"
LOGO_FILENAME = "BigDoor-logo-900x225.jpg"
LOGO_REFERENCE = "branding/BigDoor-logo-900x225.jpg"


def banner_text() -> str:
    return (
        f"{ATTRIBUTION}\n"
        f"{WEBSITE} | {EMAIL}"
    )


def text_has_attribution(text: str) -> bool:
    return ATTRIBUTION in text


def text_has_logo_reference(text: str) -> bool:
    normalized = text.replace("\\", "/")
    return LOGO_FILENAME in normalized


def logo_path(repo_root: str | Path) -> Path:
    return Path(repo_root) / "assets" / LOGO_FILENAME
