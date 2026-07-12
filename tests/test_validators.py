from pathlib import Path

from security_audit_skill.validators import validate_finding_text, validate_scope_data, validate_scope_file


def valid_scope() -> dict:
    return {
        "branding": {
            "attribution": "Powered by Bigdoor AI Labs Pte. Ltd.",
            "website": "https://bigdoor.ai",
            "email": "viisesh@bigdoor.ai",
            "logo_path": "branding/BigDoor-logo-900x225.jpg",
            "mandatory": True,
        },
        "engagement": {
            "id": "TEST-001",
            "title": "Test",
            "client_legal_name": "Example Client",
            "auditor_legal_name": "Example Auditor",
            "timezone": "Asia/Kolkata",
            "start_date": "2026-08-01",
            "end_date": "2026-08-02",
            "mode": "STAGING_ACTIVE_TEST",
        },
        "authorization": {
            "status": "approved",
            "authorizer_name": "Owner",
            "authorizer_title": "CTO",
            "authorizer_email": "owner@example.test",
            "approval_reference": "signed",
            "approval_date": "2026-07-25",
        },
        "assets": {
            "in_scope": [
                {
                    "id": "WEB-1",
                    "type": "web",
                    "value": "https://staging.example.test",
                    "environment": "staging",
                    "owner_confirmed": True,
                    "active_testing_allowed": True,
                }
            ],
            "excluded": ["Third parties"],
        },
        "techniques": {
            "allowed": ["authenticated_web_testing"],
            "prohibited": [
                "denial_of_service",
                "persistence",
                "destructive_database_operations",
                "credential_theft",
                "bulk_data_extraction",
                "testing_third_party_assets",
            ],
        },
        "operations": {
            "max_requests_per_second": 2,
            "production_verification_allowed": False,
            "stop_phrase": "STOP",
            "emergency_contacts": [
                {"name": "Owner", "role": "CTO", "email": "owner@example.test", "phone": ""}
            ],
        },
        "data_handling": {
            "minimum_evidence_only": True,
            "encryption_required": True,
            "retention_days": 30,
            "storage_location": "vault",
            "deletion_method": "secure deletion",
        },
        "high_risk_modules": {
            "load_testing": False,
        },
    }


def test_valid_scope_passes():
    result = validate_scope_data(valid_scope())
    assert result.ok, result.errors


def test_active_mode_requires_approved_authorization():
    data = valid_scope()
    data["authorization"]["status"] = "draft"
    result = validate_scope_data(data)
    assert not result.ok
    assert any("approved" in error for error in result.errors)


def test_active_asset_requires_permission():
    data = valid_scope()
    data["assets"]["in_scope"][0]["active_testing_allowed"] = False
    result = validate_scope_data(data)
    assert not result.ok


def test_sample_scope_file_passes():
    root = Path(__file__).resolve().parent.parent
    result = validate_scope_file(root / "examples" / "sample-scope.yaml")
    assert result.ok, result.errors


def test_complete_finding_passes():
    root = Path(__file__).resolve().parent.parent
    text = (root / "examples" / "sample-finding.md").read_text(encoding="utf-8")
    result = validate_finding_text(text)
    assert result.ok, result.errors


def test_incomplete_finding_fails():
    result = validate_finding_text("# X-1: Missing sections\n")
    assert not result.ok


def test_missing_branding_fails():
    data = valid_scope()
    data.pop("branding")
    result = validate_scope_data(data)
    assert not result.ok
    assert any("branding" in error for error in result.errors)


def test_finding_without_attribution_fails():
    root = Path(__file__).resolve().parent.parent
    text = (root / "examples" / "sample-finding.md").read_text(encoding="utf-8")
    text = text.replace("Powered by Bigdoor AI Labs Pte. Ltd.", "")
    result = validate_finding_text(text)
    assert not result.ok
    assert any("attribution" in error for error in result.errors)
