# Database Security Review

## Required inputs

- Engine and version
- Architecture and network diagram
- Schema and migrations
- User and role list
- Grants and ownership
- Row-level security policies
- Stored procedures and functions
- Connection and pool configuration
- Backup policy and restore evidence
- Audit-log configuration
- Data classification and retention policy

Use read-only administrative access first.

## Review areas

### Connectivity

- Public reachability
- Private endpoints
- Firewall allowlists
- TLS enforcement
- Administrative console exposure
- Replica and analytics endpoint exposure

### Identity and privilege

- Shared accounts
- Dormant users
- Default accounts
- Excessive grants
- Role inheritance
- Schema ownership
- Function execution rights
- Developer production access
- Service-account privilege

### Tenant isolation

- RLS or equivalent controls
- Application-supplied tenant identifiers
- Background jobs and exports
- Administrative bypass paths
- Reporting replicas
- Search and cache isolation

### Secrets

- Connection strings in source, build artifacts, logs, or CI
- Rotation
- Environment separation
- Secret-manager use
- Development credentials accepted by production

### Data protection

- Encryption in transit and at rest
- Key access
- Masking and pseudonymization
- Sensitive columns
- Production data in staging
- Retention and deletion
- Bulk export authorization

### Database logic

- Dynamic SQL
- Security-definer functions
- Triggers
- Unsafe extensions
- Stored routine privilege escalation
- Error leakage

### Monitoring

- Failed authentication
- Privilege and schema changes
- Bulk reads or exports
- Administrator activity
- Table deletion
- Log integrity and retention

### Backup and recovery

- Frequency
- Encryption
- Access
- Immutability
- Off-site or cross-account copies
- Restore testing
- RPO and RTO
- Deletion protection
- Key recovery

## Required conclusion wording

Do not state that the database is safe. State:

```text
[Partially verified] The listed controls were reviewed for the named database environment on the stated date. Areas without access or restoration evidence remain unverified.
```
