# Decifact Product Roadmap

## Purpose

Decifact is the reference implementation of Guardian.
This document outlines the commercial deployment roadmap
aligned with Guardian spec maturity.

Status: Internal planning document
Date: 2026-05-17

---

## Phase 1 — Decision Verifier (V0.2)

Target: Guardian V0.2 decision equivalence attestation

Function:
- Verify whether two independently governed decisions
  are formally equivalent
- Produce cryptographically signed equivalence receipt
- RFC3161 timestamp anchoring

Trigger: Mohamed spec review closure
Status: Architecture defined, not yet deployed

---

## Phase 2 — Acceptance Verifier (V0.3)

Target: Guardian V0.3 acceptance condition validation

Function:
- Verify whether a decision produced in one governed
  system is acceptance-compatible in another
- Cross-domain authority translation
- Governance boundary attestation

Trigger: First enterprise cross-system coordination inquiry
Status: Spec candidate, not yet deployed

---

## Phase 3 — Governance Memory Verifier (V0.4)

Target: Guardian V0.4 governance memory integrity

Function:
- Verify whether admissible state at t₀ is replayable
- Cross-system governance memory comparability
- State lineage integrity attestation

Trigger: Production reconciliation conflict case
Status: Emerging — V0.4 candidate in research

---

## Phase 4 — Certification Framework

Target: Guardian as cross-system governance standard

Function:
- Certify governed systems as Guardian-compatible
- Standards body partnership
- Regulatory compliance mapping (EU AI Act, etc.)

Trigger: External citation + standards body engagement
Status: Not yet defined

---

## Commercial Model (Preliminary)

| Phase | Model | Entry Point |
|-------|-------|-------------|
| Phase 1 | Verifier SaaS | Decifact Early Access |
| Phase 2 | Enterprise API | Cross-domain coordination |
| Phase 3 | Infrastructure | Production governance |
| Phase 4 | Certification | Standards partnerships |

---

## Current Status

Early Access open at decifact.com
Guardian V0.2 + V0.3-mini public
V0.4 in research

Next milestone: Mohamed spec review → Phase 1 deployment
