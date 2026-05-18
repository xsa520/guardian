# Guardian

## Constitutional Governance Layer for Cross-Sovereign AI Systems

Guardian defines the constitutional governance layer that preserves sovereign integrity when independently governed AI systems coordinate.

**Core structural gap Guardian addresses:**

Independently governed systems can each satisfy their own admissibility and authority requirements — yet still produce decisions that remain formally non-equivalent or unreconcilable across governance boundaries.

Guardian formalizes the conditions under which this gap can be resolved without collapsing sovereign governance structures into one another.

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

Defines cross-system acceptance, authority translation, and governance-valid interoperability. Formalizes sovereign discontinuity rights and constitutional anti-normalization boundaries.

> Persistent interoperability does not constitute implicit acceptance.

→ [specs/guardian-v0.3-acceptance.md](./specs/guardian-v0.3-acceptance.md)

---

## Core Model

**Intent → Policy → Decision → Evidence**

| Layer | Responsibility |
|-------|----------------|
| Decision Identity | What makes a decision canonically itself |
| Decision Equivalence | When two decisions are formally the same |
| Acceptance | Under what authority context a decision is valid |
| Constitutional Prohibitions | What equivalence is permanently prohibited from becoming |

---

## The Problem Guardian Solves

Current AI governance frameworks address:

- Identity (who is authorized)
- Execution receipts (what happened)
- Compliance (did the system follow its rules)

What remains undefined:

> When independently governed systems each produce a valid decision, what determines whether those decisions are equivalent — and which should be accepted when governance boundaries interact?

Without decision equivalence, cross-system governance remains in its adjectival phase: “interoperable,” “coordinated,” “aligned” — without the structural basis to verify what those adjectives mean when sovereign boundaries interact.

---

## Empirical Implementation

Guardian’s constitutional architecture has been operationalized in a live governance environment since 2026-02-11.

### Four-layer governance stack:

| Layer | Guardian Mapping |
|-------|------------------|
| Decision Layer | V0.2 Decision Equivalence |
| Acceptance Layer | V0.3 Acceptance |
| Execution Layer | Runtime governance bridge |
| Lifecycle Layer | V0.4+ Behavioral Governance |

**Evidence anchoring:** RFC3161 (DigiCert)  
**Audit chain:** Append-only, hash-verified

See: [guardian_layers/](./guardian_layers/)

---

## Repository Structure

```txt
guardian/
├── specs/               # Formal specifications
│   ├── guardian-v0.2-decision-equivalence.md
│   ├── guardian-v0.3-mini-acceptance.md
│   ├── guardian-v0.3-acceptance.md
│   └── guardian-v0.4-candidate.md
├── drafts/              # In-development specifications
├── guardian_layers/     # Empirical implementation mapping
├── docs/                # Architecture and conceptual documents
├── guardian/            # Reference implementation
├── schemas/             # JSON schemas
├── examples/            # Example scripts
└── tests/               # Validation and test suites

---

## Reference Implementation

→ [Decifact](https://decifact.com) — Decision verification for 
governed AI systems

---

## License

See [LICENSE](LICENSE).
