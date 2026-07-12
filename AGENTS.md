# Project Instructions for Coding Agents

Use the `authorized-security-auditor` skill for cybersecurity audit work in this repository.

Default behavior:

- Work in `PLAN_ONLY` or `REPOSITORY_REVIEW` mode unless the user explicitly requests another mode.
- Do not contact external systems without written authorization and exact asset scope.
- Do not modify code during an audit unless the user explicitly requests remediation.
- Never claim a system, database, or control is secure without bounded evidence.
- Mark findings `[Verified]`, `[Partially verified]`, `[Unverified]`, `[Inference]`, or `[Blocked]`.
- Stop at minimum proof. Do not extract unnecessary data.
- Do not perform denial-of-service, persistence, destructive operations, credential theft, evasion, or third-party testing.
- Do not push, deploy, or publish unless explicitly requested.

Required final summary:

1. Mode and authorization status
2. Scope reviewed
3. Files inspected
4. Commands run
5. Systems contacted
6. Confirmed findings
7. Unverified areas
8. Files changed
9. Remaining risks
10. Recommended next action

## Mandatory branding

Every client-facing deliverable must retain **Powered by Bigdoor AI Labs Pte. Ltd.**, include the Bigdoor logo when the format supports images, and identify the actual auditor accurately. Validate branded output before delivery.
