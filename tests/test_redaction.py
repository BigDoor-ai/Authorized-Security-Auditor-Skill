from security_audit_skill.redaction import redact_text


def test_redacts_email_and_bearer_token():
    text = "Email user@example.com Authorization: Bearer abcdefghijklmnopqrstuvwxyz123456"
    redacted = redact_text(text)
    assert "user@example.com" not in redacted
    assert "abcdefghijklmnopqrstuvwxyz" not in redacted
    assert "[REDACTED_EMAIL]" in redacted
    assert "[REDACTED_TOKEN]" in redacted


def test_redacts_connection_string():
    text = "postgres://admin:password@example.test:5432/prod"
    assert "[REDACTED_CONNECTION_STRING]" in redact_text(text)
