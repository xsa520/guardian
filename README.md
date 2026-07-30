# Guardian

## Constitutional Governance Layer for Cross-Sovereign AI Systems

Guardian defines the constitutional governance layer that preserves sovereign integrity when independently governed AI systems coordinate.

**Core structural gap Guardian addresses:**

Independently governed systems can each satisfy their own admissibility and authority requirements — yet still produce decisions that remain formally non-equivalent or unreconcilable across governance boundaries.

Guardian formalizes the conditions under which this gap can be evaluated as equivalence, non-equivalence, or formal incomparability without collapsing sovereign governance structures into one another.

### Where Guardian Fits in the Governance Chain

Cross-system coordination involves several distinct governance questions:

1. **Referent continuity** — do the judgments still concern the same governed object?
2. **Governing-basis currency** — are the relevant definitions, authority conditions, evidence thresholds, and time states still current?
3. **Comparison determination** — do the judgments share a valid comparison basis, and if so, are they equivalent or non-equivalent?
4. **Reliance authority** — may a receiving party rely on the comparison result for a particular purpose?
5. **Execution admissibility** — may the resulting action proceed under current conditions?
6. **Runtime continuity** — do the governing conditions remain valid as execution continues?
7. **Evidence reconciliation** — were all required evaluations completed and preserved as reviewable evidence?

Guardian is a research constitution and specification framework primarily concerned with Layer 3 — comparison determination — and the constitutional prohibitions that govern it. It requires the relevant comparison inputs from Layers 1 and 2 to be represented. It does not itself establish ongoing authority, authorize reliance, determine execution admissibility, govern runtime continuation, or discharge downstream evidentiary obligations — those remain separate governance layers, each with its own responsible party.

A Guardian-governed equivalence determination describes a relationship between judgments. It does not authorize what any system should do with that determination.

---

## Constitutional Property

> Cross-governance comparability without cross-governance authority inheritance.

Equivalence determinations under Guardian carry explicit constitutional prohibitions:

- Equivalence does not transfer admissibility
- Equivalence does not transfer authority
- Equivalence does not create inheritance obligations
- Acceptance remains sovereign
- Equivalence cannot launder legitimacy

See: [specs/guardian-v0.2-decision-equivalence.md](./specs/guardian-v0.2-decision-equivalence.md) — Section 10

---

## Specification Layers

### V0.2 — Decision Equivalence

Defines decision identity and the invariant boundary that determines canonical equivalence across independently governed systems.

→ [specs/guardian-v0.2-decision-equivalence.md](./specs/guardian-v0.2-decision-equivalence.md)

### V0.3-mini — Acceptance Minimal Invariant

Defines the minimal deterministic conditions under which a decision is accepted within or across governance domains.

> Equivalence does not imply acceptance.

→ [specs/guardian-v0.3-mini-acceptance.md](./specs/guardian-v0.3-mini-acceptance.md)

### V0.3 — Acceptance

Examines the constitutional conditions and prohibitions surrounding cross-domain acceptance — sovereign discontinuity rights and anti-normalization boundaries.

> Persistent interoperability does not constitute implicit acceptance.

It does not itself grant reliance authority, authorize execution, or transfer authority between governance domains. Defining acceptance conditions is not the same as performing acceptance, which remains a decision for the receiving governance domain.

→ [specs/guardian-v0.3-acceptance.md](./specs/guardian-v0.3-acceptance.md)

---

## Core Model

**Intent → Policy → Decision → Evidence**

| Layer | Responsibility |
|-------|----------------|
| Decision Identity | What makes a decision canonically itself |
| Decision Equivalence | Whether judgments share a valid comparison basis and how equivalence, non-equivalence, or formal incomparability is represented |
| Acceptance | Under what authority context a decision is valid |
| Constitutional Prohibitions | What equivalence is permanently prohibited from becoming |

---

## The Problem Guardian Solves

Current AI governance frameworks address:

- Identity (who is authorized)
- Execution receipts (what happened)
- Compliance (did the system follow its rules)

What remains undefined:

> When independently governed systems produce judgments under different governing sources, what determines whether those judgments share a valid comparison basis — and how should equivalence, non-equivalence, or formal incomparability be represented without transferring authority between them?

Without decision equivalence, cross-system governance remains in its adjectival phase: “interoperable,” “coordinated,” “aligned” — without the structural basis to verify what those adjectives mean when sovereign boundaries interact.

---

## Empirical Foundation

Guardian concepts have been exercised since 2026-02-11
through controlled internal governance experiments and
reference implementations.

These experiments inform the specification. They do not constitute
external production certification, nor proof that all governance
layers described in the seven-layer chain above are operationalized.
Guardian's own specifications (V0.2, V0.3-mini, V0.3) concentrate on
Layer 3 and the constitutional prohibitions surrounding Layer 4;
Layers 1, 2, and 5–7 remain research relationships informed by, but
not established by, this work.

**Evidence anchoring:** RFC3161 (DigiCert)  
**Audit chain:** Append-only, hash-verified

---

## Repository Structure

```txt
guardian/
├── specs/               # Formal and candidate specifications
│   ├── guardian-v0.2-decision-equivalence.md
│   ├── guardian-v0.3-mini-acceptance.md
│   ├── guardian-v0.3-acceptance.md
│   └── guardian-v0.4-candidate.md
├── docs/                # Architecture and conceptual documents
├── guardian/            # Historical runtime-authorization prototype
├── policies/            # Prototype policy definitions
├── schemas/             # Prototype and evidence schemas
├── examples/            # Historical runtime examples
└── tests/               # Prototype validation tests
```

### Implementation-status note

The executable Python package currently preserved in `guardian/`
implements Guardian's earlier single-runtime authorization prototype:
intent and policy evaluation resulting in ALLOW, DENY, or ESCALATE.

It does not implement the current cross-system comparison semantics
defined by the Guardian specifications. The comparison-layer reference
implementation is Decifact.

The prototype remains in this repository as implementation history
pending a separate decision on archival, extraction, or long-term
repositioning.

---

## Reference Implementation

Decifact is the reference implementation of the comparison layer
(Layer 3): it determines whether independently governed judgments
share a valid comparison basis, and classifies them as equivalent,
non-equivalent, or formally incomparable.

It does not grant reliance authority, authorize execution, or
govern runtime continuation. Those remain separate governance
responsibilities (Layers 4–7 above).

→ [Decifact](https://decifact.com) — comparison-layer reference implementation

→ [xsa520/decifact](https://github.com/xsa520/decifact) — Source code

---

## License

See [LICENSE](LICENSE).
