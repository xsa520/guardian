# Guardian Decision Artifact — v0 (Semantic Invariant)

## Status

Draft — Semantic Proposal (Non-binding)

---

## 1. Problem

In agent systems, execution receipts are often treated as primary evidence.

However, receipts alone do not establish whether an action was **authorized** — only that it occurred.

This creates ambiguity for:

* audit
* replay
* cross-engine verification

---

## 2. Core Invariant

A **Decision Artifact** is a first-class, independently verifiable object that represents the outcome of a policy evaluation.

It MUST NOT be:

* reconstructed from execution receipts
* reduced to metadata attached to execution logs

---

## 3. Separation of Concerns

| Layer     | Responsibility              |
| --------- | --------------------------- |
| Decision  | why an action is allowed    |
| Execution | what actually happened      |
| Receipt   | record of execution outcome |

**Invariant:**
Decision ≠ Receipt

---

## 4. Verifier Semantics

A verifier SHOULD:

1. Validate the integrity and signature of the decision artifact
2. Evaluate the policy reference and evaluation method
3. Determine replayability based on evaluation type

---

## 5. Deterministic Boundary

Replayability is only guaranteed when:

* the evaluation method is deterministic
* inputs are fully specified

This corresponds to **Proof of Computation (PoC)**.

Probabilistic outputs MAY be signed, but:

* are not replay-equivalent evidence
* require additional interpretation

---

## 6. Minimal Fields (Abstract)

A decision artifact SHOULD minimally include:

* intent_id
* policy_reference
* evaluation_method
* decision_outcome
* decision_hash

This set is intentionally minimal and engine-agnostic.

---

## 7. Cross-Engine Implication

In cross-engine scenarios:

* execution traces may not be available
* only signed artifacts can be exchanged

Therefore:

Verification MUST rely on decision artifacts, not execution receipts or execution trace reconstruction.

---

## 8. Non-Goals

This document does NOT define:

* execution formats
* transport protocols
* runtime enforcement mechanisms

It is purely a **semantic invariant layer**.

---

## 9. Summary

A system is verifiable across engines only if:

* decisions are independently representable
* verification does not depend on execution reconstruction

This document defines that boundary.
