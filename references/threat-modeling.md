# Threat Modeling Guide

## Minimum model

For each system record:

- Asset
- Business owner
- Data handled
- Users and roles
- Entry points
- Trust boundaries
- Dependencies
- Privileged operations
- Abuse cases
- Existing controls
- Detection controls
- Recovery controls

## Abuse-case prompts

- Can one user read or change another user's record?
- Can a lower role call an administrator endpoint directly?
- Can identifiers be enumerated?
- Can an expired, revoked, or copied token still be used?
- Can a workflow step be skipped or replayed?
- Can price, package, approval, or payment state be changed client-side?
- Can uploads become public or executable?
- Can the application fetch attacker-controlled URLs?
- Can a service account access more data than required?
- Can a compromised integration trigger bulk exports or messages?
- Can a backup be downloaded, deleted, or restored by too many identities?
- Can an attacker remain undetected after privilege or data-access changes?

## Output

Create a table:

| ID | Asset | Threat actor | Entry point | Abuse case | Existing controls | Likelihood | Impact | Test approach | Status |
|---|---|---|---|---|---|---|---|---|---|

Do not assign likelihood from intuition alone. Record the evidence or mark it `[Inference]`.
