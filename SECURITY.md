# Security

Guardian is security-sensitive infrastructure. It sits between AI agents and execution and influences whether actions are allowed, denied, or escalated. Compromise or misuse of Guardian can lead to unauthorized execution or bypass of governance controls.

## Reporting Vulnerabilities

We take security seriously. If you believe you have found a security vulnerability:

- **Do not** open a public GitHub issue for the vulnerability.
- Report it privately by emailing the maintainers or using a private reporting channel advertised in the repository (e.g. GitHub Security Advisories, or an email address listed in the repo).
- Include a clear description of the issue, steps to reproduce, and impact if possible.
- Allow a reasonable time for a fix before any public disclosure.

We will acknowledge receipt and work with you to understand and address the report.

## Scope

Security-sensitive areas include but are not limited to:

- Policy loading and rule evaluation (e.g. path traversal, injection via policy files).
- Evidence ledger integrity (e.g. hash chain bypass, log tampering).
- Decision Engine and Permission Model (e.g. logic errors that allow unintended ALLOW or bypass of ESCALATE).
- Any component that could allow an attacker to influence or bypass governance decisions.

Thank you for helping keep Guardian and its users safe.
