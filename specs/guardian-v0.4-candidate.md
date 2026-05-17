# Guardian V0.4 Candidate — Governance Memory Integrity Layer

## Status

Candidate — not yet in spec
Derived from external corridor convergence
Date: 2026-05-17

---

## Core Problem

Guardian V0.2 establishes decision equivalence.
Guardian V0.3 establishes acceptance conditions.

A further structural question is emerging:

Whether the governance memory underlying independently
produced decisions — the admissible state that existed
when each decision formed — remains formally comparable,
replayable, and integrity-verified across governance
boundaries.

---

## Driving Observations

Ricky Jones (2026-05-17):
"The harder problem is reconstructing admissible state
at t₀ — what the system knew, what authorities were
active, what constraints applied, what dependencies
were still valid."

"State lineage rather than event sequence."

Robert Schneider (2026-05-17):
"What did your AI know at t₀?"
Traversable temporal graph → admissible state replay.

Elena Bobkova (2026-05-17):
Sanitized governance records distort what systems
learn from governance history.

Demarius Lawson (2026-05-16):
"A system can remain stable while semantic equivalence
drifts underneath it."

---

## Candidate Layer Definition

Governance Memory Integrity:

The structural condition under which the admissible
state that governed a decision at the moment of
formation can be:

1. Reconstructed — replayed from preserved state
   lineage, not approximated from event logs

2. Compared — formally evaluated against the admissible
   state of an independently governed system's decision

3. Verified — shown to be integrity-preserving across
   governance boundaries without relying on each
   system's own narrative

---

## Relationship to Existing Layers

V0.2 — Decision Equivalence:
Are the decisions the same?

V0.3 — Acceptance:
Is this decision valid here?

V0.4 candidate — Governance Memory Integrity:
Was the admissible state that produced each decision
formally comparable and integrity-verified across
governance boundaries?

---

## Commercial Implications

Verifier can attest:
- Decision equivalence (V0.2)
- Acceptance validity (V0.3)
- Governance memory comparability (V0.4)

This shifts Guardian from:
spec → verifiable governance infrastructure stack

---

## Remaining Questions

- What constitutes a minimal replayable state object?
- How is governance memory bounded for comparison?
- What makes two admissible states formally comparable?
- How does sanitized governance history affect
  cross-system memory integrity?

Status: open — not yet resolved in spec
