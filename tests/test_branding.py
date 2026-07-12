from security_audit_skill.branding import ATTRIBUTION, banner_text, text_has_attribution, text_has_logo_reference


def test_banner_contains_mandatory_attribution():
    assert ATTRIBUTION in banner_text()


def test_branding_detectors():
    text = "Powered by Bigdoor AI Labs Pte. Ltd.\n![Logo](branding/BigDoor-logo-900x225.jpg)"
    assert text_has_attribution(text)
    assert text_has_logo_reference(text)
