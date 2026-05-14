# Guardian v0.3-mini — Acceptance Minimal Invariant

## Status

Draft v0.3-mini (Trigger Deployment Reference)

Defines the minimal deterministic conditions under which a decision is accepted within or across governance domains.

---

## Core Principle

> **Equivalence does not imply acceptance.**

Equivalent decisions may still differ in validity depending on authority, policy, and verifier context.

---

## Acceptance Definition

A decision is accepted if and only if:

1. Decision equivalence is valid
2. Verifier context is explicitly defined
3. Authority is valid
4. Authority conflicts are deterministically resolved
5. Policy permits the decision

---

## Verifier Context

Acceptance MUST be evaluated relative to:

- verifier identity
- trust domain
- policy
- authority resolution order

Without verifier context:

> Acceptance is INVALID.

---

## Authority Resolution

When multiple authority sources conflict:

> Deterministic precedence MUST resolve authority.

Example:

policy > legal authority > credential > identity

Unresolved authority conflict:

> Acceptance is INVALID.

---

## Cross-Domain Acceptance

Acceptance across governance domains requires:

- explicit trust-domain mapping
- authority translation
- verifier agreement

Without these:

> Cross-domain acceptance is INVALID.

---

## Non-Acceptance Conditions

A decision MUST NOT be accepted if:

- authority is ambiguous
- policy denies
- verifier context is undefined
- trust-domain mapping is absent
- authority conflict is unresolved

---

## Consequence

> Without explicit acceptance rules, independently governed systems remain governance-valid but non-comparable.

---

## Summary

Guardian v0.3-mini establishes:

- acceptance as context-bound
- authority as deterministic
- verifier context as mandatory
- cross-domain acceptance as explicit
- governance validity as distinct from decision equivalence
