# Stack-Specific Checklists

## Next.js and React

- Server versus client trust boundaries
- `NEXT_PUBLIC_` exposure
- Route handlers and Server Actions authorization
- Middleware assumptions
- Cache and revalidation of sensitive data
- Client-side role checks without server enforcement
- Source maps and build artifacts
- Image or URL fetch SSRF exposure
- Cookie flags and token storage

## Node.js APIs

- Schema validation
- Prototype pollution
- Unsafe object merging
- SQL/NoSQL query construction
- JWT validation and key rotation
- Express or framework trust-proxy settings
- CORS and rate limits
- Error and log leakage
- Dependency lifecycle

## Python and Django/FastAPI/Flask

- Debug mode
- Secret keys
- CSRF and session configuration
- ORM raw queries
- Serializer or schema authorization
- Admin exposure
- File handling
- Dependency and package integrity
- Deserialization and template safety

## PHP and Laravel/WordPress

- Debug configuration
- CSRF and middleware
- Policies, gates, and route protection
- Blade escaping and raw output
- Storage exposure
- Plugin and theme provenance
- Administrative users
- XML-RPC or legacy endpoints
- File permissions and backups

## Supabase

- RLS enabled on exposed tables
- Policies tested by role and tenant
- Service-role key kept server-side
- Storage bucket policies
- Auth redirect allowlist
- Edge Function secrets and authorization
- Realtime subscriptions and row access
- Database functions and security-definer behavior

## Firebase

- Firestore and Storage rules
- Rules tested with emulator
- Admin SDK isolation
- Custom claims and token refresh
- App Check assumptions
- Callable function authorization
- Public configuration versus secrets

## PostgreSQL/MySQL

- Public exposure
- TLS
- Users, grants, ownership, and default roles
- Row-level security where applicable
- Dynamic SQL and stored routines
- Audit logging
- Backup access and restoration
- Production data in non-production

## AWS/Azure/GCP

- Root or owner account protections
- MFA and break-glass access
- Service-account privilege
- Public storage and databases
- Network security groups
- Audit-log coverage and retention
- Secret and key management
- Cross-account roles
- Backup and regional recovery

## Docker and Kubernetes

- Root containers
- Privileged mode and capabilities
- Host mounts
- Image provenance and vulnerabilities
- Secrets in images and manifests
- Network policies
- RBAC
- Public dashboards
- Admission controls
- Resource limits

## Mobile

- Sensitive local storage
- Tokens in logs or preferences
- Certificate validation
- Exported Android components
- iOS URL schemes and universal links
- WebView bridges
- Clipboard and screenshots
- Third-party SDK data collection
- API object authorization
