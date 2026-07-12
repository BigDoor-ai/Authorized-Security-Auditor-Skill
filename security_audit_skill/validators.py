from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from .branding import ATTRIBUTION, EMAIL, LOGO_REFERENCE, WEBSITE

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("PyYAML is required. Install the package with: pip install -e .") from exc


ALLOWED_MODES = {
    "PLAN_ONLY",
    "REPOSITORY_REVIEW",
    "PASSIVE_EXTERNAL_REVIEW",
    "STAGING_ACTIVE_TEST",
    "LIMITED_PRODUCTION_VERIFICATION",
    "REMEDIATION",
    "RETEST",
}

ACTIVE_MODES = {
    "PASSIVE_EXTERNAL_REVIEW",
    "STAGING_ACTIVE_TEST",
    "LIMITED_PRODUCTION_VERIFICATION",
    "RETEST",
}

REQUIRED_PROHIBITIONS = {
    "denial_of_service",
    "persistence",
    "destructive_database_operations",
    "credential_theft",
    "bulk_data_extraction",
    "testing_third_party_assets",
}


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)


def _mapping(value: Any, name: str, result: ValidationResult) -> dict[str, Any]:
    if not isinstance(value, dict):
        result.add_error(f"{name} must be a mapping")
        return {}
    return value


def _nonempty(mapping: dict[str, Any], key: str, path: str, result: ValidationResult) -> Any:
    value = mapping.get(key)
    if value is None or value == "" or value == []:
        result.add_error(f"{path}.{key} is required")
    return value


def _parse_date(value: Any, path: str, result: ValidationResult) -> date | None:
    if not isinstance(value, str):
        result.add_error(f"{path} must be an ISO date string")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        result.add_error(f"{path} must use YYYY-MM-DD")
        return None


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("The YAML document must contain a mapping at the top level")
    return data


def validate_scope_data(data: dict[str, Any]) -> ValidationResult:
    result = ValidationResult()

    engagement = _mapping(data.get("engagement"), "engagement", result)
    authorization = _mapping(data.get("authorization"), "authorization", result)
    assets = _mapping(data.get("assets"), "assets", result)
    techniques = _mapping(data.get("techniques"), "techniques", result)
    operations = _mapping(data.get("operations"), "operations", result)
    handling = _mapping(data.get("data_handling"), "data_handling", result)
    high_risk = _mapping(data.get("high_risk_modules"), "high_risk_modules", result)
    branding = _mapping(data.get("branding"), "branding", result)

    for key in ("id", "title", "client_legal_name", "auditor_legal_name", "timezone", "start_date", "end_date", "mode"):
        _nonempty(engagement, key, "engagement", result)

    if branding.get("attribution") != ATTRIBUTION:
        result.add_error(f"branding.attribution must exactly equal: {ATTRIBUTION}")
    if branding.get("website") != WEBSITE:
        result.add_error(f"branding.website must exactly equal: {WEBSITE}")
    if branding.get("email") != EMAIL:
        result.add_error(f"branding.email must exactly equal: {EMAIL}")
    if branding.get("logo_path") != LOGO_REFERENCE:
        result.add_error(f"branding.logo_path must exactly equal: {LOGO_REFERENCE}")
    if branding.get("mandatory") is not True:
        result.add_error("branding.mandatory must be true")

    mode = engagement.get("mode")
    if mode and mode not in ALLOWED_MODES:
        result.add_error(f"engagement.mode must be one of: {', '.join(sorted(ALLOWED_MODES))}")

    start = (
        _parse_date(engagement.get("start_date"), "engagement.start_date", result)
        if engagement.get("start_date")
        else None
    )
    end = (
        _parse_date(engagement.get("end_date"), "engagement.end_date", result)
        if engagement.get("end_date")
        else None
    )
    if start and end and end < start:
        result.add_error("engagement.end_date cannot be before engagement.start_date")

    auth_status = _nonempty(authorization, "status", "authorization", result)
    if auth_status not in {"draft", "approved", "expired", "revoked"}:
        result.add_error("authorization.status must be draft, approved, expired, or revoked")

    if mode in ACTIVE_MODES:
        if auth_status != "approved":
            result.add_error(f"authorization.status must be approved for mode {mode}")
        for key in ("authorizer_name", "authorizer_title", "authorizer_email", "approval_reference", "approval_date"):
            _nonempty(authorization, key, "authorization", result)

    in_scope = assets.get("in_scope")
    if not isinstance(in_scope, list) or not in_scope:
        result.add_error("assets.in_scope must contain at least one asset")
        in_scope = []

    seen_ids: set[str] = set()
    for index, asset in enumerate(in_scope):
        path = f"assets.in_scope[{index}]"
        asset = _mapping(asset, path, result)
        for key in ("id", "type", "value", "environment"):
            _nonempty(asset, key, path, result)
        asset_id = asset.get("id")
        if asset_id in seen_ids:
            result.add_error(f"Duplicate asset id: {asset_id}")
        if asset_id:
            seen_ids.add(asset_id)
        if mode in ACTIVE_MODES:
            if asset.get("owner_confirmed") is not True:
                result.add_error(f"{path}.owner_confirmed must be true for active modes")
            active_test_modes = {
                "STAGING_ACTIVE_TEST",
                "LIMITED_PRODUCTION_VERIFICATION",
                "RETEST",
            }
            if mode in active_test_modes and asset.get("active_testing_allowed") is not True:
                result.add_error(f"{path}.active_testing_allowed must be true for mode {mode}")

    excluded = assets.get("excluded")
    if not isinstance(excluded, list) or not excluded:
        result.add_warning("assets.excluded is empty; explicitly list third-party and out-of-scope systems")

    allowed = techniques.get("allowed")
    prohibited = techniques.get("prohibited")
    if not isinstance(allowed, list) or not allowed:
        result.add_error("techniques.allowed must contain at least one technique")
    if not isinstance(prohibited, list):
        result.add_error("techniques.prohibited must be a list")
        prohibited_set: set[str] = set()
    else:
        prohibited_set = set(str(item) for item in prohibited)
        missing = REQUIRED_PROHIBITIONS - prohibited_set
        if missing:
            result.add_warning("Recommended prohibitions missing: " + ", ".join(sorted(missing)))

    contacts = operations.get("emergency_contacts")
    if mode in ACTIVE_MODES:
        if not isinstance(contacts, list) or not contacts:
            result.add_error("operations.emergency_contacts is required for active modes")
        else:
            for index, contact in enumerate(contacts):
                path = f"operations.emergency_contacts[{index}]"
                contact = _mapping(contact, path, result)
                _nonempty(contact, "name", path, result)
                _nonempty(contact, "role", path, result)
                if not contact.get("email") and not contact.get("phone"):
                    result.add_error(f"{path} requires email or phone")
        _nonempty(operations, "stop_phrase", "operations", result)

    rate = operations.get("max_requests_per_second")
    if rate is not None:
        if not isinstance(rate, (int, float)) or rate <= 0:
            result.add_error("operations.max_requests_per_second must be a positive number")
        elif rate > 10:
            result.add_warning("operations.max_requests_per_second is above 10; document why this rate is safe")

    if mode == "LIMITED_PRODUCTION_VERIFICATION" and operations.get("production_verification_allowed") is not True:
        result.add_error("operations.production_verification_allowed must be true for LIMITED_PRODUCTION_VERIFICATION")

    handling_fields = (
        "minimum_evidence_only",
        "encryption_required",
        "retention_days",
        "storage_location",
        "deletion_method",
    )
    for key in handling_fields:
        _nonempty(handling, key, "data_handling", result)
    retention = handling.get("retention_days")
    if retention is not None and (not isinstance(retention, int) or retention < 0):
        result.add_error("data_handling.retention_days must be a non-negative integer")

    for key, enabled in high_risk.items():
        if enabled is True:
            result.add_warning(
                f"High-risk module enabled: {key}. "
                "Confirm separate written authorization and safeguards."
            )

    return result


def validate_scope_file(path: str | Path) -> ValidationResult:
    try:
        data = load_yaml(path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return ValidationResult(errors=[f"Unable to read scope: {exc}"])
    return validate_scope_data(data)


FINDING_REQUIRED_HEADINGS = [
    "Description",
    "Business impact",
    "Technical impact",
    "Preconditions",
    "Minimal reproduction",
    "Sanitized evidence",
    "Data accessed",
    "Root cause",
    "Immediate containment",
    "Recommended remediation",
    "Standards mapping",
    "Retest procedure",
    "Limitations",
]


def validate_finding_text(text: str) -> ValidationResult:
    result = ValidationResult()
    if ATTRIBUTION not in text:
        result.add_error(f"Missing exact mandatory attribution: {ATTRIBUTION}")
    if not re.search(r"^#\s+[A-Z0-9_-]+:\s+.+", text, re.MULTILINE):
        result.add_error("Finding title must use '# FINDING-ID: Title'")
    for field_name in ("Verification status", "Severity", "Confidence", "Affected assets"):
        if not re.search(rf"^-\s+{re.escape(field_name)}:\s*\S+", text, re.MULTILINE | re.IGNORECASE):
            result.add_error(f"Missing metadata field: {field_name}")
    for heading in FINDING_REQUIRED_HEADINGS:
        if not re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE | re.IGNORECASE):
            result.add_error(f"Missing section: {heading}")
    verification_labels = (
        "[Verified]",
        "[Partially verified]",
        "[Unverified]",
        "[Inference]",
        "[Blocked]",
    )
    if not any(label in text for label in verification_labels):
        result.add_error("Finding must contain a verification label")
    if re.search(r"Bearer\s+[A-Za-z0-9._-]{20,}", text, re.IGNORECASE):
        result.add_warning("Finding may contain an unredacted bearer token")
    if re.search(r"(?:postgres|mysql|mongodb(?:\+srv)?)://[^\s]+", text, re.IGNORECASE):
        result.add_warning("Finding may contain an unredacted database connection string")
    return result


def validate_finding_file(path: str | Path) -> ValidationResult:
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        return ValidationResult(errors=[f"Unable to read finding: {exc}"])
    return validate_finding_text(text)
