# Guardian

Guardian is an **architectural exploration** of treating governance decisions as first-class verifiable artifacts. This repository explores a model where the decision itself is recorded as an independent artifact before execution, improving auditability and enabling verification independent of runtime behavior.

---

## 1. Project Overview

Guardian explores the idea that **governance decisions can be treated as verifiable artifacts**, independent from runtime execution. Many governance systems rely primarily on execution receipts as evidence. This repository explores a different model: the **decision artifact exists before execution** and can therefore be verified independently from runtime behavior.

---

## 2. Architecture Model

The governance pipeline is:

**Intent → Policy Evaluation → Decision Artifact → Execution → Execution Receipt**

| Stage | Role |
|-------|------|
| **Intent** | An action requested by an actor or agent. |
| **Policy Evaluation** | Governance rules evaluate whether the action should be allowed. |
| **Decision Artifact** | The evaluated decision is recorded as a verifiable artifact *before* execution. |
| **Execution** | The runtime system performs the action. |
| **Execution Receipt** | Runtime evidence that execution occurred. |

---

## 3. Decision Provenance

Recording decisions separately from execution can improve **auditability** and **replayability**. The decision artifact captures *what was decided* at policy-evaluation time; the execution receipt captures *what actually happened* at runtime. By keeping both, systems can detect divergence between policy outcomes and runtime behavior, and can replay or verify decisions without depending solely on execution logs.

---

## 4. Governance Model Comparison

| Layer | Execution-Receipt Governance | Decision-Artifact Model |
|-------|-----------------------------|--------------------------|
| Intent | yes | yes |
| Policy Evaluation | yes | yes |
| Decision Artifact | embedded | **explicit artifact** |
| Execution | yes | yes |
| Receipt | **primary evidence** | secondary evidence |

In execution-receipt-centric models, the receipt is the main evidence. In the decision-artifact model, the explicit decision record is the primary governance artifact; the receipt serves as secondary evidence of what was executed.

---

## 5. Interoperability Discussion

If multiple governance frameworks emit **compatible decision artifacts**, interoperability between systems may become possible. Shared schema and semantics for decision records could allow different runtimes and policy engines to exchange, verify, or replay each other’s decisions. This repository only explores the idea; it does not define a standard.

---

## Repository Contents

- **docs/** — Architecture and concept documentation.
- **schemas/** — JSON schema for a decision artifact (`decision_record.schema.json`).

See [docs/architecture.md](docs/architecture.md) for the full pipeline and [schemas/decision_record.schema.json](schemas/decision_record.schema.json) for the schema.
