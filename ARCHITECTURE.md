# Architecture

This document describes Guardian's system design, governance pipeline, core components, and design principles.

## System Flow

Guardian sits between AI agents and execution. Request flow:

```
LLM
  │
  ▼
Agent (declares intent: actor, action, target)
  │
  ▼
Guardian
  │
  ├── Policy Engine   (loads rules, matches intent)
  ├── Decision Engine (returns ALLOW / DENY / ESCALATE)
  ├── Permission Model (evaluates actor, action, target)
  │
  ▼
Decision (ALLOW / DENY / ESCALATE)
  │
  ▼
Evidence Ledger (append-only, hash-chained)
  │
  ▼
Execution (only if permitted by policy and decision)
```

## Governance Pipeline

1. **Intent** — The agent submits an intent (actor, action, target). No execution occurs until Guardian evaluates it.

2. **Policy** — Rules are loaded from policy configuration (e.g. JSON). Rules support wildcards and define effect: ALLOW, DENY, or ESCALATE.

3. **Decision** — The Decision Engine returns a single outcome. No rule match defaults to DENY.

4. **Evidence** — Every decision is written to the evidence ledger with a timestamp and hash chain. The ledger is append-only and replayable.

5. **Execution** — Downstream systems use the decision to allow, block, or route to human review (ESCALATE).

## Core Components

| Component | Role |
|-----------|------|
| **Intent** | Schema for agent declarations (actor, action, target, optional metadata). |
| **Policy Engine** | Loads policy rules, matches intents (including `*` wildcards), returns effect. |
| **Decision Engine** | Orchestrates policy evaluation; returns ALLOW, DENY, or ESCALATE. |
| **Permission Model** | Applies rules to (actor, action, target); first match wins; default DENY. |
| **Evidence Logger** | Appends decision records to the ledger with SHA256 hash chaining. |
| **Replay Verifier** | Replays the ledger, re-evaluates with Decision Engine, verifies consistency. |
| **Ledger Validator** | Verifies hash chain integrity of the evidence log. |

## Design Principles

- **Deterministic decisions** — Same intent and policy always yield the same decision. No hidden state in the decision path.
- **Policy as code** — Behavior is controlled by declared rules (e.g. JSON), not hardcoded branches.
- **Evidence by default** — Every decision is recorded. The ledger is append-only and hash-chained for integrity.
- **Replayability** — Decisions can be replayed and validated against current policy to detect drift or tampering.
- **Explicit escalation** — ESCALATE supports workflows that require human or enterprise approval before execution.
