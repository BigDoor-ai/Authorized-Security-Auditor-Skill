<p align="center">
  <a href="https://bigdoor.ai">
    <img src="https://raw.githubusercontent.com/BigDoor-ai/Authorized-Security-Auditor-Skill/main/assets/BigDoor-logo-900x225.jpg" alt="Bigdoor AI Labs Pte. Ltd." width="620">
  </a>
</p>

<p align="center"><strong>Powered by Bigdoor AI Labs Pte. Ltd.</strong><br>
<a href="https://bigdoor.ai">https://bigdoor.ai</a> · <a href="mailto:viisesh@bigdoor.ai">viisesh@bigdoor.ai</a></p>

# Copy-Paste Prompts

Replace values inside `<ANGLE BRACKETS>` before using a prompt. Coding agents remain tragically unable to infer a signed Rules of Engagement from enthusiasm.

## 1. Install for the current project

```text
Install the Authorized Security Auditor Skill from:
https://github.com/BigDoor-ai/Authorized-Security-Auditor-Skill

Install it for this project only. Read README.md and SKILL.md before changing anything. Use the repository's official installer where supported. Verify that the skill is available to the coding agent and report:
1. the exact installation path,
2. files installed,
3. verification performed,
4. anything that remains unverified.

Do not run a security audit, contact any external system, modify application code, deploy, or push changes during installation.
```

## 2. Install for the user account

```text
Install the Authorized Security Auditor Skill from:
https://github.com/BigDoor-ai/Authorized-Security-Auditor-Skill

Install it for my user account so it is available across projects. Read README.md and SKILL.md first, use the supported user-level installer, verify the installation, and report the exact path. Do not run any audit or contact external systems.
```

## 3. Plan a website audit without testing

```text
Use the Authorized Security Auditor Skill to prepare a complete security-audit plan for:
<WEBSITE_URL>

Client: <CLIENT_LEGAL_NAME>
Known assets: <DOMAINS_SUBDOMAINS_APIS_MOBILE_APPS>
Known technology stack: <STACK_OR_UNKNOWN>

Mode: PLAN_ONLY.
Do not contact the website, run scanners, submit payloads, or test any system. Produce:
1. proposed scope,
2. authorization checklist,
3. Rules of Engagement,
4. asset and user-role inventory,
5. web, API, database, cloud, mobile, code, privacy, backup, and incident-response test plan,
6. required client access,
7. deliverables,
8. remediation and retest plan.

Clearly label assumptions and unverified areas.
```

## 4. Passive external website review

```text
Use the Authorized Security Auditor Skill to perform a low-impact passive external review of:
<WEBSITE_URL>

Authorization reference: <SIGNED_APPROVAL_OR_TICKET_REFERENCE>
Authorized owner: <CLIENT_LEGAL_NAME>
In-scope assets: <EXACT_DOMAINS_AND_SUBDOMAINS>
Excluded assets: <THIRD_PARTIES_AND_OTHER_EXCLUSIONS>
Approved dates: <START_DATE> to <END_DATE>
Emergency contact: <NAME_EMAIL_PHONE>

Mode: PASSIVE_EXTERNAL_REVIEW.
Only perform low-volume public inspection, DNS and certificate review, response-header review, public technology and asset inventory, and public-document exposure review. Do not submit attack payloads, brute-force, fuzz, exploit, upload files, enumerate users, test third-party systems, or run denial-of-service activity.

Produce an executive summary, technical observations, evidence, limitations, and a recommended active-testing plan. Treat scanner or fingerprinting output as unverified until manually confirmed.
```

## 5. Complete authorized staging website audit

```text
Use the Authorized Security Auditor Skill to conduct a complete authorized security assessment of the staging environment below.

Client legal name: <CLIENT_LEGAL_NAME>
Written authorization reference: <SIGNED_APPROVAL_REFERENCE>
Staging website: <STAGING_URL>
In-scope subdomains and APIs: <EXACT_SCOPE>
Excluded systems and third parties: <EXCLUSIONS>
Approved dates and timezone: <DATES_AND_TIMEZONE>
Approved source IPs: <SOURCE_IPS>
Maximum request rate: <REQUESTS_PER_SECOND>
Emergency stop contact and phrase: <CONTACT_AND_STOP_PHRASE>
Test accounts and roles: <ROLE_ACCOUNTS>
Permitted techniques: <APPROVED_TECHNIQUES>
Prohibited techniques: denial-of-service, persistence, destructive database operations, credential theft, bulk production-data extraction, monitoring evasion, and any test outside scope.

Mode: STAGING_ACTIVE_TEST.

Before testing:
1. validate the authorization and scope files,
2. identify missing prerequisites,
3. stop and remain in PLAN_ONLY mode if required evidence is missing.

Then assess applicable areas including attack surface, authentication, sessions, authorization and tenant isolation, OWASP web risks, APIs, file handling, business logic, rate limits, source code, dependencies, database configuration, cloud IAM, storage, secrets, mobile APIs, privacy, logging, backup, recovery, and incident response.

Use synthetic records only. Stop at minimum proof. Do not access unnecessary data. Escalate critical findings immediately. Produce branded executive, technical, remediation, and retest deliverables using the repository templates.
```

## 6. Repository and source-code security review

```text
Use the Authorized Security Auditor Skill to perform a read-only security review of this repository.

Mode: REPOSITORY_REVIEW.
Do not contact external systems, use production credentials, modify files, deploy, or push changes.

Review architecture, authentication, authorization, tenant isolation, input validation, database queries, file uploads, webhooks, payments, secrets, dependencies, CI/CD, containers, infrastructure as code, logging, backups, and tests. Run only appropriate local read-only checks. Record every command and tool version.

For each issue, provide verification status, severity, confidence, affected files and lines, business impact, root cause, remediation, and retest instructions. Separate confirmed findings from scanner leads and unverified concerns.
```

## 7. Database-focused review

```text
Use the Authorized Security Auditor Skill to assess database security for:
<APPLICATION_OR_PROJECT>

Environment: <STAGING_OR_PRODUCTION>
Authorization reference: <APPROVAL_REFERENCE>
Database engine and version: <ENGINE_VERSION>
Access provided: <READ_ONLY_ACCESS_OR_CONFIG_FILES>
Exact database assets in scope: <DATABASES_HOSTS_PROJECTS>

Review network exposure, TLS, users, roles, grants, row-level security, tenant isolation, service accounts, secrets, stored procedures, backups, restoration evidence, encryption, audit logging, data retention, production data in non-production, and bulk export controls.

Do not run destructive queries, alter permissions, extract full records, or claim the database is safe. Clearly state what was verified, partially verified, unverified, or blocked.
```

## 8. Fix confirmed findings

```text
Use the Authorized Security Auditor Skill in REMEDIATION mode to fix only the confirmed findings listed in:
<FINDINGS_FILE_OR_REPORT>

Work on branch: <BRANCH_NAME>
Do not perform unrelated refactoring. Add regression tests where practical, apply the smallest secure correction, run relevant lint, typecheck, tests, build, and local security checks, and document every changed file and command.

Do not deploy or push unless I explicitly request it. Do not mark a finding fixed unless the relevant test passes and the result is supported by evidence.
```

## 9. Retest remediation

```text
Use the Authorized Security Auditor Skill in RETEST mode to retest findings:
<FINDING_IDS>

Authorization reference: <APPROVAL_REFERENCE>
Approved environment and assets: <EXACT_SCOPE>
Version or commit: <VERSION_OR_COMMIT>

Reproduce the original issue, test reasonable bypass variants, verify related roles and tenants, review regression tests and relevant logs, and classify each finding as Fixed, Partially fixed, Not fixed, Risk accepted, Unable to verify, or Superseded.

Stop at minimum proof and produce the branded retest report.
```

---

**Powered by Bigdoor AI Labs Pte. Ltd.**  
https://bigdoor.ai · viisesh@bigdoor.ai
