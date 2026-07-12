# Authorization and Scope Gates

## Gate A: Planning

Required evidence: none.

Permitted:

- Draft scope
- Draft Rules of Engagement
- Threat-model planning
- Audit methodology
- Report templates

## Gate B: Repository review

Required:

- Permission to access the repository
- Confirmed repository or local directory
- Agreement on whether local scanners may run

Permitted:

- Read-only source and configuration review
- Local builds and tests
- Local SAST, SCA, secret, container, and IaC scanning

Not permitted by this gate:

- Requests to external hosts
- Use of production credentials
- Active application testing

## Gate C: Passive external review

Required:

- Written authorization
- Exact hostnames or IPs
- Approved dates
- Emergency contact
- Confirmation of third-party exclusions

Permitted:

- Low-volume public-page inspection
- DNS and certificate review
- Header and TLS observations
- Public artifact inventory

## Gate D: Active staging testing

Required:

- All Gate C requirements
- Staging URL or IP
- Test accounts for every relevant role
- Approved techniques
- Approved source IPs, when applicable
- Rate limits
- Synthetic data plan
- Backup or rollback confirmation
- Stop procedure

## Gate E: Limited production verification

Required:

- Separate, explicit production approval
- Exact finding or control to verify
- Lowest-impact proof plan
- Approved time window
- Live emergency contact
- Monitoring awareness

## Gate F: High-risk modules

Separate authorization is required for:

- Load or stress testing
- Social engineering
- Wireless testing
- Physical testing
- Password spraying
- Destructive recovery exercises
- Real payment flows
- Tests likely to trigger bulk notifications

## Required authorization fields

- Client legal name
- Authorizer name, title, and contact
- Auditor legal name
- Engagement identifier
- In-scope assets
- Explicit exclusions
- Environment classification
- Start and end dates
- Time zone
- Permitted methods
- Prohibited methods
- Rate limits
- Source IPs
- Data-handling rules
- Emergency contacts
- Stop phrase or stop process
- Signature or equivalent approval evidence

## Decision rule

When evidence is ambiguous, do not perform the active step. Record:

```text
[Blocked] The requested test requires authorization evidence that is not available in the engagement files.
```
