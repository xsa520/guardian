# Guardian

Guardian is a **decision-governance control plane** for autonomous systems: it treats governance decisions as **first-class verifiable artifacts** that exist *before* execution and can be audited and replayed independently of runtime behavior.

---

## 1. Why Guardian

Modern AI agent systems need a **governance layer** between agent reasoning and real-world execution. Many systems rely mainly on **execution receipts** as evidence. Guardian explores a different model: the **decision artifact** is recorded *before* execution, so you can verify *what was allowed* independently of *what actually ran*. That improves auditability, replayability, and the ability to detect divergence between policy and runtime.

---

## 2. Core Model

**Intent → Policy → Decision Artifact → Execution → Receipt**

| Stage | Role |
|-------|------|
| **Intent** | Action requested by an actor or agent. |
| **Policy** | Governance rules evaluate whether the action is allowed (ALLOW / DENY / ESCALATE). |
| **Decision Artifact** | The evaluated decision is recorded as a verifiable artifact *before* execution. |
| **Execution** | The runtime performs the action (outside Guardian). |
| **Receipt** | Runtime evidence that execution occurred (outside Guardian). |

Guardian is responsible for **intent normalization**, **deterministic policy evaluation**, **decision artifact generation**, **append-only evidence ledger**, **replay verification**, and **decision/receipt correlation**. Guardian is **not** responsible for agent planning, tool orchestration, runtime sandboxing, actual execution, or cryptographic execution attestation.

---

## 3. Where Guardian Sits

**Agent Governance Architecture Map**

```
             ┌──────────────────────────────┐
             │         Application           │
             │  user workflows / automation  │
             └──────────────────────────────┘
                            │
                            ▼
             ┌──────────────────────────────┐
             │       Agent Framework         │
             │  LangChain / AutoGen / etc.   │
             │ planning, reasoning, tools    │
             └──────────────────────────────┘
                            │
                            ▼
    ┌────────────────────────────────────────────┐
    │     Governance Control Plane (Guardian)     │
    │                                              │
    │  Intent → Policy → Decision → Evidence       │
    │  deterministic policy evaluation             │
    │  decision artifacts                          │
    │  tamper-evident decision ledger              │
    │  replay verification                         │
    └────────────────────────────────────────────┘
                            │
                            ▼
       ┌────────────────────────────────────┐
       │       Runtime Enforcement Layer     │
       │  policy enforcement, gating, audit │
       └────────────────────────────────────┘
                            │
                            ▼
    ┌────────────────────────────────────────────┐
    │       Execution Environment / Tools         │
    └────────────────────────────────────────────┘
                            │
                            ▼
       ┌────────────────────────────────────┐
       │  Cryptographic Execution Receipts  │
       └────────────────────────────────────┘
```

**Governance models**

| Layer | Question |
|-------|----------|
| Agent Framework | What does the agent want to do? |
| Governance Control Plane | Why was a decision allowed? |
| Runtime Enforcement | Can this action execute right now? |
| Execution Receipts | What actually happened during execution? |

Guardian focuses on the **decision governance layer**.

---

## 4. Why Decision Provenance Matters

Recording decisions separately from execution improves **auditability** and **replayability**. The decision artifact captures *what was decided* at policy-evaluation time; the execution receipt captures *what actually happened* at runtime. By keeping both, systems can detect divergence between policy and runtime and can replay or verify decisions without depending solely on execution logs. See [docs/decision_provenance.md](docs/decision_provenance.md).

---

## 5. Example Flow

1. Caller submits **intent** (actor, action, target).
2. Guardian evaluates **policy** (ALLOW / DENY / ESCALATE; default DENY; wildcards).
3. Guardian produces a **DecisionRecord** (with `decision_hash`, timestamp) and appends it to the **ledger**.
4. Caller (or runtime enforcement) decides whether to execute; execution and **receipt** are outside Guardian.
5. Optional: **Replay** verifier re-evaluates ledger entries; **receipt correlation** verifier compares receipts to decision records.

See [docs/example_decision_flow.md](docs/example_decision_flow.md).

---

## 6. Repository Structure

```
guardian/
  guardian/           # Single canonical package
    models/           # Intent, PolicyRule, DecisionRecord, ExecutionReceipt
    policy/           # Policy loader and deterministic engine
    decision/         # Decision engine (artifact before execution)
    ledger/           # Append-only hash-chained evidence ledger
    verification/     # Replay verifier, receipt correlation verifier
    integrations/     # Integration points (stubs)
    api.py            # Guardian facade
    config.py         # Configuration
  docs/               # Architecture and concepts
  schemas/            # JSON schemas
  examples/           # Example scripts
  tests/              # Tests
```

---

## 7. Schema

| Schema | Description |
|--------|-------------|
| [intent.schema.json](schemas/intent.schema.json) | Intent (actor, action, target, optional metadata). |
| [policy.schema.json](schemas/policy.schema.json) | Policy rules (actor, action, target, effect). |
| [decision_record.schema.json](schemas/decision_record.schema.json) | Decision artifact. |
| [execution_receipt.schema.json](schemas/execution_receipt.schema.json) | Execution receipt (secondary evidence). |
| [evidence_log_entry.schema.json](schemas/evidence_log_entry.schema.json) | Single ledger entry with hash chain. |

---

## 8. Interoperability

If multiple governance frameworks emit **compatible decision artifacts**, interoperability may become possible: shared schema and semantics allow exchange, verification, and replay across systems. **Guardian does not attempt to define a governance standard.** This repository explores the idea only. See [docs/interoperability.md](docs/interoperability.md).

---

## 9. Boundaries

Guardian is a **decision-governance control plane only**. It does not do agent planning, tool orchestration, runtime sandboxing, actual execution, or cryptographic execution attestation. See [docs/boundaries.md](docs/boundaries.md).

---

## Quick Start

```bash
# From repo root (install in dev mode or set PYTHONPATH)
pip install -e .
# Or: set PYTHONPATH to repo root

python examples/email_send_allowed.py
python examples/replay_demo.py
pytest tests/
```

## License

See [LICENSE](LICENSE).
