# Ecosystem Positioning

Guardian occupies one layer in a broader agent governance stack. This document clarifies where Guardian sits relative to other concerns.

## Stack Layers

| Layer | Question | Example projects / ideas |
|-------|----------|---------------------------|
| **Application** | User workflows, automation | Custom apps |
| **Agent Framework** | What does the agent want to do? | LangChain, AutoGen, CrewAI |
| **Governance Control Plane** | Why was a decision allowed? | **Guardian** |
| **Runtime Enforcement** | Can this action execute right now? | e.g. agent-governance-toolkit |
| **Execution Environment** | APIs, DBs, infrastructure | Various |
| **Execution Receipts** | What actually happened? | e.g. AutoGen governance proposal (signed attestation) |

## Guardian’s Niche

Guardian focuses on the **decision governance layer**:

- **Input**: Intent (actor, action, target).
- **Output**: A **decision artifact** (ALLOW / DENY / ESCALATE) recorded before execution, plus an append-only ledger and replay/receipt-correlation verification.

Guardian does **not**:

- Replace the agent framework (planning, tools, reasoning).
- Replace the runtime enforcement layer (gating, sandboxing, audit at execution time).
- Replace cryptographic execution attestation (signed receipts).

## Interoperability

If other governance or execution frameworks emit:

- **Decision artifacts** compatible with Guardian’s schema (e.g. `decision_record.schema.json`), or  
- **Execution receipts** that reference a decision (e.g. `decision_id` = `decision_hash`),

then Guardian’s replay and receipt-correlation tools can work with them. This repository explores that idea and does not define a standard.

## Summary

Guardian is a **minimal, coherent** decision-governance control plane: intent in, decision artifact and ledger entry out, with replay and receipt correlation. The rest of the stack (agents, runtime enforcement, execution, receipts) is out of scope.
