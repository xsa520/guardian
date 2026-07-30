# Repository Reconciliation Items

Bounded, deferred architecture decisions. Recorded for future
decision-making — none are resolved in the same pass as the
historical-scope notices added on 2026-07-30.

---

## Item 1 — Legacy runtime prototype vs current comparison constitution

**Status:** OPEN — architecture decision required.

**Observed:**

The repository contains two historically distinct Guardian models,
built at different times, never reconciled with each other:

```
1. Early runtime-authorization prototype (2026-03-14 to 03-17)
   intent → policy → ALLOW / DENY / ESCALATE → execution
   Files: ARCHITECTURE.md, docs/boundaries.md,
   docs/ecosystem_positioning.md, guardian/ (executable package),
   examples/, tests/

2. Current cross-system comparison constitution (2026-03-23 onward)
   equivalence / non-equivalence / formal incomparability
   Files: README.md, specs/guardian-v0.2-decision-equivalence.md,
   specs/guardian-v0.3-mini-acceptance.md,
   specs/guardian-v0.3-acceptance.md,
   specs/guardian-v0.4-candidate.md
```

The README was rewritten on 2026-05-14 to reflect the comparison
constitution positioning. `ARCHITECTURE.md`, `docs/boundaries.md`,
`docs/ecosystem_positioning.md`, and the entire `guardian/` executable
package were never updated to match — they still describe and
implement the earlier single-runtime authorization model.

**Immediate action (completed 2026-07-30):**

Explicit historical-scope notices added to `ARCHITECTURE.md`,
`docs/boundaries.md`, `docs/ecosystem_positioning.md`, and an
Implementation-status note added to `README.md`. No implementation
code was removed or rewritten.

**Decision required (not yet made):**

- retain the prototype in place, clearly labeled as historical;
- move it under `legacy/` or `prototypes/`;
- extract it to a separate repository;
- retire it after preserving release history.

**Non-goal:**

Do not rewrite the old runtime engine (`guardian/decision/engine.py`
and related modules) into a comparison engine as an incidental
documentation cleanup. Do not retroactively describe the prototype as
having been designed against the seven-layer responsibility map — no
evidence supports that it was; the map postdates the prototype by
months.

**Relation to Guardian V0.4 candidate:** None. The V0.4 candidate
(`specs/guardian-v0.4-candidate.md`, Governance Memory Integrity) is
an unrelated, separate direction and is not affected by this item.
