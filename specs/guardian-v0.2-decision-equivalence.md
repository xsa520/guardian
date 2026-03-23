# Guardian v0.2 — Decision Equivalence Specification

## 0. Status

Draft v0.2 (Pre-Standard)

This specification defines decision identity, invariant boundary, and equivalence conditions.
It is intended to be minimal, deterministic, and non-interpretive.

---

## 1. Scope

This specification defines:

- What constitutes a decision
- How decision identity is determined
- When two decisions are equivalent
- Why execution, identity, and outcomes are insufficient for equivalence

This specification does NOT define:

- Execution protocols
- Transport layers
- Identity systems (DID, keys, etc.)
- Policy evaluation logic

---

## 2. Definitions

### 2.1 Decision

A **Decision** is a first-class artifact representing an intended action under a defined semantic context.

A decision exists **prior to execution** and is independent of:

- transport representation
- execution result
- system-specific encoding

---

### 2.2 Identity Context

The **Identity Context** defines the origin of a decision.

It includes:

- agent identity (DID, key, or equivalent)
- authority scope (if applicable)

Identity context answers:

> **who is making the decision**

---

### 2.3 Invariant Boundary

The **Invariant Boundary** is the minimal set of semantic elements that define a decision.

It includes:

- intent (what is being decided)
- target (what the decision applies to)
- parameters (material inputs affecting outcome)
- policy-relevant fields (fields that affect evaluation)

It explicitly excludes:

- transport format
- encoding differences
- signature envelopes
- execution receipts

---

## 3. Decision Identity

A decision is uniquely identified by:


DecisionIdentity = hash(canonical(IdentityContext) + canonical(InvariantBoundary))


Two decisions may share the same identity context but differ in identity if their invariant boundaries differ.

---

## 4. Decision Equivalence

### 4.1 Definition

Two decisions A and B are **equivalent if and only if**:


InvariantBoundary(A) == InvariantBoundary(B)
AND
IdentityContext(A) == IdentityContext(B)


---

### 4.2 Non-Equivalence Conditions

Decisions are NOT equivalent if any of the following differ:

- semantic intent
- target
- material parameters
- policy-relevant structure

---

## 5. Invalid Equivalence Heuristics

The following MUST NOT be used to determine equivalence:

### 5.1 Execution Outcome


Outcome(A) == Outcome(B) -> INVALID


Same result does not imply same decision.

---

### 5.2 Identity-Only Matching


Identity(A) == Identity(B) -> INVALID


Same actor does not imply same decision.

---

### 5.3 Structural / Hash Matching


hash(serialized(A)) == hash(serialized(B)) -> INVALID


Structural equality does not imply semantic equality.

---

### 5.4 Transport-Level Equality

Envelope, signature, or relay-level equivalence is irrelevant to decision identity.

---

## 6. Economic Implications

Any system performing:

- attribution
- compensation
- settlement

MUST base equivalence on decision identity.

Equivalence misclassification results in invalid economic attribution.

---

### 6.1 Constraint

> **Economic settlement without decision equivalence is undefined.**

---

### 6.2 Rationale

If two non-equivalent decisions are treated as equivalent:

- attribution becomes invalid
- compensation becomes inconsistent
- settlement loses correctness guarantees

---

## 7. Verification

A valid equivalence check MUST:

1. Extract invariant boundary from both decisions
2. Normalize semantic fields (not structure)
3. Compare invariant sets deterministically

Normalization MUST preserve semantic meaning and MUST NOT alter invariant boundary.


verify_equivalence(A, B):
return invariant(A) == invariant(B)


---

## 8. Separation of Concerns

| Layer        | Responsibility                  |
|-------------|--------------------------------|
| Identity     | Who acts                       |
| Execution    | What happened                  |
| Receipt      | Evidence of execution          |
| Decision     | What is being decided          |

Decision equivalence is orthogonal to all other layers.

---

## 9. Design Principle

> **Execution equivalence is not decision equivalence.**

---

## 10. Consequence

Any system lacking explicit decision equivalence:

- cannot guarantee audit consistency
- cannot resolve cross-engine disagreement
- cannot ensure economic correctness

---

## 11. Summary

This specification establishes:

- Decision as a first-class artifact
- Invariant boundary as the core identity of decision
- Equivalence as a deterministic, semantic condition

All higher-level systems MUST rely on this layer for:

- consistency
- auditability
- economic correctness
