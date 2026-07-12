# Remediation and Retesting

## Remediation order

1. Active compromise and exposed credentials
2. Critical authorization and data-access failures
3. Remote execution and injection
4. Account takeover and administrative access
5. Public cloud, storage, and database exposure
6. File upload and server-side request risks
7. High-impact business logic
8. Logging and detection gaps
9. Medium and low weaknesses
10. Long-term secure-development improvements

## Fix standard

A remediation should address the root cause, not merely the demonstrated input.

Examples:

- Add centralized ownership checks rather than blocking one object ID.
- Parameterize queries rather than filtering one payload string.
- Enforce authorization server-side rather than hiding a button.
- Revoke and rotate exposed secrets rather than deleting one commit.
- Make storage private by default rather than obscuring URLs.

## Retest steps

1. Review the original evidence.
2. Confirm the target version and environment.
3. Reproduce the original path.
4. Test reasonable bypass variants.
5. Confirm related roles and tenants.
6. Check regression tests.
7. Verify logs or alerts where relevant.
8. Record residual exposure.

## Status definitions

- Fixed
- Partially fixed
- Not fixed
- Risk accepted
- Unable to verify
- Superseded

## Retest evidence

Include:

- Original finding ID
- Version or commit
- Date and tester
- Commands or requests
- Sanitized evidence
- Result
- Remaining limitations
