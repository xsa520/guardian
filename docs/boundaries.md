# Guardian Boundaries

> **Historical scope note**
>
> This document describes the boundaries of Guardian's early
> single-runtime authorization prototype. Its references to policy
> evaluation, permission decisions, and execution control should not
> be read as the current scope of the Guardian research constitution.
>
> The current Guardian scope is cross-system comparison determination:
> whether independently governed judgments share a valid comparison
> basis and how equivalence, non-equivalence, or formal
> incomparability is represented without transferring authority.
>
> This historical prototype remains relevant as an execution-governance
> example, but it is not itself a cross-system comparison engine.

Guardian is a **decision-governance control plane**, not an agent framework or execution runtime. This document states what Guardian is and is not responsible for.

## Guardian Is Responsible For

| Responsibility | Description |
|----------------|-------------|
| **Intent normalization** | Accept intent (actor, action, target, optional metadata) and normalize for policy evaluation. |
| **Deterministic policy evaluation** | Apply policy rules with ALLOW / DENY / ESCALATE and wildcard matching; default DENY. |
| **Decision artifact generation** | Produce a verifiable `DecisionRecord` *before* execution. |
| **Append-only evidence ledger** | Record decision artifacts in a hash-chained ledger. |
| **Replay verification** | Re-evaluate ledger entries and compare decisions. |
| **Decision/receipt correlation** | Compare decision records to execution receipts (by decision_id / decision_hash). |

## Guardian Is NOT Responsible For

| Out of scope | Description |
|--------------|-------------|
| **Agent planning** | Guardian does not plan, reason, or choose tools. |
| **Tool orchestration** | Guardian does not invoke or orchestrate tools. |
| **Runtime sandboxing** | Guardian does not sandbox or isolate execution. |
| **Actual execution** | Guardian does not execute actions; it only produces decisions. |
| **Cryptographic execution attestation** | Signed execution proofs are the responsibility of the execution layer (e.g. AutoGen governance proposal). |

## Pipeline Position

```
Intent → [Guardian: Policy → Decision Artifact → Ledger] → Execution (external) → Receipt (external)
```

Guardian owns the middle box. Execution and receipts are produced by other systems; Guardian can *correlate* receipts to decisions but does not produce receipts.

## Why This Matters

Keeping Guardian narrow ensures:

- **Single responsibility**: Decision governance only.
- **No runtime creep**: The repo stays minimal and publishable.
- **Clear distinction**: Decision artifact (what was allowed) vs execution receipt (what happened) remains explicit.
