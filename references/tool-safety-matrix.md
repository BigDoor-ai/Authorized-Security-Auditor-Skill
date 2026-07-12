# Tool Safety Matrix

## General rule

Tool availability is not authorization. Every command must be justified by the current mode and scope.

| Category | Examples | Default mode | Approval notes |
|---|---|---|---|
| File inspection | `find`, `grep`, `rg`, language parsers | Repository review | Local only |
| Build and tests | npm, pytest, go test, cargo test | Repository review | Avoid external integration tests unless approved |
| SAST | Semgrep, CodeQL, Bandit | Repository review | Record ruleset and version |
| SCA | OSV-Scanner, npm audit, pip-audit | Repository review | May contact advisory services; confirm network policy |
| Secret scanning | Gitleaks, TruffleHog in local filesystem mode | Repository review | Never validate discovered credentials against services |
| Container/IaC | Trivy, Checkov, tfsec | Repository review | Prefer local artifacts |
| Browser inspection | Browser devtools, low-volume fetch | Passive or staging | Approved hosts only |
| Port discovery | Nmap and equivalents | Active staging or approved infrastructure | Exact IPs, timing, and rate required |
| Web scanners | ZAP, Burp Scanner, Nuclei | Active staging | Templates and request limits must be reviewed |
| API fuzzing | Schemathesis and equivalents | Active staging | Synthetic data and rate limits required |
| Password testing | Password auditing tools | Separate high-risk approval | Never use leaked or reused real credentials |
| Load testing | k6, JMeter, Locust | Separate high-risk approval | Dedicated environment preferred |

## Scanner rules

1. Review targets and templates before launch.
2. Exclude destructive, intrusive, and denial-of-service checks.
3. Set conservative concurrency and rate limits.
4. Use staging unless production is separately approved.
5. Use identifiable user agents or headers where agreed.
6. Save raw logs securely.
7. Treat output as unverified until manually validated.
8. Stop on errors, latency spikes, or abnormal responses.

## Command recording

For every security command record:

```text
Timestamp:
Operator or agent:
Mode:
Authorization reference:
Target:
Tool and version:
Exact command:
Expected impact:
Observed result:
Evidence path:
Stop condition triggered: yes/no
```
