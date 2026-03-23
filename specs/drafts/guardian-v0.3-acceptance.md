# Guardian v0.3 — Acceptance
## Status: Draft (Non-normative, exploratory)

## Purpose
Defines when a decision should be accepted under an authority context.

Builds on v0.2 Decision Equivalence.

## Core Principle
Equivalence does not imply acceptance.

## 1. Acceptance Context

Defines authority conditions under which a decision is evaluated.

Includes:
- DID
- credentials
- entity binding
- policy context
- trust domain
## 2. Authority Source

Authority may come from:
- identity
- credentials
- legal entity
- policy authority
## 3. Acceptance Rule

A decision is accepted iff:
- identity is valid
- authority source is valid
- credentials are valid
- policy allows action
## 4. Relationship to Equivalence

Equivalence:
- same decision

Acceptance:
- valid decision
## 5. Minimal Reference Implementation
```python
def verify_acceptance(decision, context):
    if not verify_identity(decision):
        return False
    if not verify_authority(decision):
        return False
    if not verify_policy(decision, context):
        return False
    return True
```
