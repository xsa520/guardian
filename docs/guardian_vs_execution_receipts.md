# Guardian vs Execution Receipts

This document compares **execution-receipt-centric** governance models with **decision-artifact-centric** models (as explored in Guardian), and discusses advantages and trade-offs.

## Two Governance Perspectives

### 1. Execution-Receipt-Centric Governance

In this model, the **primary evidence** of governance is the **execution receipt**. The system records that an action was executed, often with timestamps, actor, outcome, and sometimes a link to policy or intent. Governance and audit rely heavily on “what ran” and infer or attach “what was allowed” from the receipt or from logs.

**Characteristics:**

- Evidence is generated *after* execution.
- The receipt is the main artifact for audit and compliance.
- Decision (allow/deny) may be embedded in logs or receipt metadata rather than as a first-class artifact.
- Replay or verification typically starts from execution history.

### 2. Decision-Artifact-Centric Governance

In this model, the **decision** is recorded as an **explicit, first-class artifact** *before* execution. The receipt remains important as evidence that execution occurred, but the decision artifact is the primary record of *what governance allowed or denied*.

**Characteristics:**

- The decision exists as a verifiable record before any execution.
- Audit can rely on decision artifacts independent of runtime.
- Receipts serve as secondary evidence (did execution match the decision?).
- Replay can verify that re-evaluation reproduces the same decision.

## Comparison

| Aspect | Execution-Receipt-Centric | Decision-Artifact-Centric |
|--------|---------------------------|---------------------------|
| Primary evidence | Execution receipt | Decision artifact |
| When evidence is created | After execution | Before execution (for the decision) |
| Decision record | Often embedded or inferred | Explicit, standalone artifact |
| Verifying “what was allowed” | From receipt/logs | From decision record |
| Detecting runtime vs policy divergence | Harder | Easier (compare decision to receipt) |
| Replay of policy outcome | Depends on execution trail | Re-evaluate and compare to stored decision |

## Advantages of Decision-Artifact-Centric Model

- **Clear provenance** — What was decided is recorded at evaluation time, not inferred later.
- **Independent verification** — Decision can be checked (e.g. replayed) without relying on execution logs.
- **Divergence detection** — Comparing decision to receipt can reveal runtime violations or bugs.
- **Audit clarity** — Auditors see a direct record of governance outcomes, not only “what ran.”

## Trade-offs

- **Extra artifact** — Systems must produce, store, and optionally sign or hash decision records.
- **Consistency** — Execution must be tied to the correct decision (e.g. by reference or id) so that receipt and decision can be correlated.
- **Adoption** — Existing systems built around receipts would need to add a decision-recording step and possibly schema alignment for interoperability.

## Conclusion

Execution receipts are essential for knowing *what happened*. Decision artifacts are about knowing *what was decided* before it happened. The Guardian repository explores a design where both exist: the decision artifact as the primary governance record, and the execution receipt as secondary evidence. This is an architectural exploration, not a standard; the trade-offs above can inform how different systems might adopt or adapt the idea.
