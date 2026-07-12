# Comprehensive Audit Methodology

## 1. Engagement intake

- Confirm business objectives and critical services.
- Identify legal owner and authorization chain.
- Validate scope and exclusions.
- Agree communications, critical escalation, evidence handling, and stop conditions.
- Record limitations before testing begins.

## 2. Architecture and data flow

Document:

- Users, roles, tenants, and administrators
- Public and private trust boundaries
- Web, mobile, API, database, queue, storage, and third-party flows
- Personal, financial, identity, and commercially sensitive data
- Authentication and session boundaries
- Administrative control planes

## 3. Threat modeling

Use assets, actors, entry points, trust boundaries, and abuse cases. Prioritize:

- Account takeover
- Cross-tenant access
- Administrative takeover
- Bulk export
- Payment or approval manipulation
- Uploaded-file abuse
- Database exposure
- Cloud credential compromise
- Supply-chain compromise
- Event-period or peak-traffic disruption

## 4. Repository and supply chain

Review:

- Secrets and environment handling
- Dependency versions and lockfiles
- Authentication and authorization middleware
- Input validation and output encoding
- Database query construction
- File upload and object storage
- Webhook verification
- Payment state transitions
- Logging and error handling
- CI/CD permissions
- Branch protections and deployment approvals
- Containers and infrastructure as code

## 5. External attack surface

Inventory approved:

- Domains and subdomains
- DNS records and certificates
- Public IPs and services
- Alternate origins
- Admin and debug interfaces
- Public object storage
- Public documents, source maps, backups, and configuration files
- Deprecated or forgotten systems

## 6. Web application

Review:

- Security headers and browser controls
- Authentication and account recovery
- Sessions and token lifecycle
- Horizontal and vertical authorization
- Multi-tenant isolation
- Injection classes
- XSS, CSRF, SSRF, redirects, traversal, and parser risks
- File upload and download authorization
- Business logic and race conditions
- Rate limits and anti-automation controls
- Cache and sensitive response handling

## 7. APIs

Review:

- Endpoint inventory and versioning
- Object-level authorization
- Function-level authorization
- Authentication and token validation
- Mass assignment
- Excessive data exposure
- Resource consumption
- CORS
- Webhook signatures and replay resistance
- GraphQL depth, complexity, and introspection controls where applicable
- Error handling and inventory management

## 8. Database and data protection

Review:

- Public exposure and network boundaries
- TLS and connection security
- Users, roles, grants, ownership, and dormant accounts
- Row-level security and tenant isolation
- Stored procedures, functions, triggers, and dynamic SQL
- Encryption and key management
- Sensitive-data classification, masking, and minimization
- Production data in non-production environments
- Audit logging
- Backups, immutability, restoration, RPO, and RTO

## 9. Cloud and infrastructure

Review:

- IAM users, roles, service accounts, and MFA
- Public resources and security groups
- Secret management
- Network segmentation
- WAF, CDN, and origin exposure
- Serverless and container permissions
- Audit logs and retention
- Backup and regional recovery
- Infrastructure-as-code drift

## 10. Mobile

Review:

- Local data and token storage
- Transport security
- Certificate validation
- Permissions and exported components
- Deep links and WebViews
- Logging, screenshots, notifications, and clipboard
- Third-party SDKs
- Build and signing configuration
- API authorization
- Rooted or jailbroken device assumptions

## 11. Privacy and governance

Review:

- Data inventory and purpose
- Consent and notices
- Third-party sharing
- Retention and deletion
- Data-subject request process
- Cross-border transfer documentation
- Logs and analytics containing personal data
- Post-engagement evidence retention

## 12. Monitoring and incident response

Review detection for:

- Failed logins and OTP abuse
- Account takeover
- Privilege changes
- Bulk exports
- Cross-tenant access
- Database administration
- Suspicious API activity
- Public resource changes
- Malware uploads
- Credential exposure

Review incident classification, containment, evidence preservation, communications, recovery, and post-incident learning.

## 13. Resilience and recovery

Review:

- Single points of failure
- Database and application restoration
- DNS and cloud-account recovery
- Administrator lockout recovery
- Third-party outage procedures
- Queue and notification failures
- Ransomware and credential-compromise scenarios

## 14. Reporting and retesting

- Validate findings manually.
- Separate confirmed findings from scanner leads.
- Assign business-aware severity.
- Escalate critical findings immediately.
- Produce executive and technical outputs.
- Track remediation owners and dates.
- Retest exact fixes and bypass variants.
- Record residual risk and accepted risk.
