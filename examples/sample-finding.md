<p align="center">
  <img src="branding/BigDoor-logo-900x225.jpg" alt="Bigdoor.ai" width="720">
</p>

<p align="center"><strong>Powered by Bigdoor AI Labs Pte. Ltd.</strong><br>
<a href="https://bigdoor.ai">https://bigdoor.ai</a> · <a href="mailto:viisesh@bigdoor.ai">viisesh@bigdoor.ai</a></p>

# AS-001: Cross-tenant invoice access

- Verification status: `[Verified]`
- Severity: High
- Confidence: High
- Affected assets: Staging customer portal
- Affected versions or commit: `example-commit`
- Affected roles or tenants: Authenticated customer
- Discovery date: 2026-08-02
- Notification date: 2026-08-02

## Description

An authenticated test user could request a synthetic invoice belonging to another test tenant by changing the invoice identifier. The server verified authentication but did not verify invoice ownership.

## Business impact

A real attacker could access other customers' invoice data if the same control exists in production.

## Technical impact

Broken object-level authorization on the invoice-download endpoint.

## Preconditions

A valid authenticated customer account and knowledge of another invoice identifier.

## Minimal reproduction

1. Sign in using the approved tenant A test account.
2. Request tenant A's synthetic invoice.
3. Replace the invoice identifier with the approved tenant B synthetic fixture identifier.
4. Observe that the server returns tenant B's synthetic invoice.

## Sanitized evidence

Only synthetic tenant and invoice records were used. Raw session values were redacted.

## Data accessed

One synthetic invoice fixture. No production or personal data was accessed.

## Root cause

The route checked that a session existed but did not constrain the invoice query by the authenticated tenant identifier.

## Immediate containment

Disable invoice downloads or require an administrative allowlist until server-side ownership checks are deployed.

## Recommended remediation

Query invoices using both the invoice identifier and the authenticated tenant identifier. Add a centralized authorization policy and regression tests covering cross-tenant identifiers.

## Standards mapping

- CWE: CWE-639
- OWASP ASVS: Access control requirements
- OWASP API Security: Broken Object Level Authorization

## Retest procedure

Repeat the original cross-tenant request and test identifiers across the first, middle, and last synthetic records for each role.

## Limitations

Production was excluded from the assessment.

---

**Powered by Bigdoor AI Labs Pte. Ltd.**  
https://bigdoor.ai · viisesh@bigdoor.ai
