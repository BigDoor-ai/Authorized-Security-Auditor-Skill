# Severity and Triage

Use CVSS where useful, but do not let a calculator erase business context.

## Critical

Examples:

- Unrestricted production database access
- Remote code execution on a critical service
- Administrative authentication bypass
- Cross-tenant bulk personal-data access
- Public production credentials with material privilege
- Compromise path capable of disabling critical event or commercial operations

Action:

- Validate minimally
- Stop further exploitation
- Notify the approved critical contact immediately
- Recommend containment
- Record notification and response

## High

Examples:

- Account takeover
- Privilege escalation
- Sensitive record access across accounts
- Injection with meaningful data or system impact
- Dangerous file upload
- Major cloud or storage exposure

Target: urgent remediation according to the client SLA.

## Medium

A meaningful weakness requiring conditions, limited privileges, user interaction, or restricted impact.

## Low

A defense-in-depth weakness with limited direct impact.

## Informational

An observation, inventory fact, or improvement without demonstrated vulnerability.

## Confidence

- High: directly reproduced with stable evidence
- Medium: strong evidence but incomplete reproduction or environmental limits
- Low: scanner lead, code smell, or architecture concern requiring validation

## Required triage fields

- Technical severity
- Business criticality
- Exploit prerequisites
- Affected user population
- Data classification
- Detection likelihood
- Compensating controls
- Remediation complexity
- Exposure duration

## Risk acceptance

Risk acceptance must identify:

- Finding
- Business owner
- Rationale
- Compensating controls
- Expiration date
- Review date
- Sign-off

Use `templates/risk-acceptance.md`.
