# Architecture

This document describes the governance pipeline and the responsibilities of each stage.

## Pipeline

**Intent → Policy → Decision → Execution → Receipt**

---

## Stage Responsibilities

### Intent

The **intent** is the action requested by an actor or agent. It describes *what* the requester wants to do (e.g. send an email, transfer funds, deploy a service). Intent is the input to governance: it is evaluated against policy before any execution occurs.

### Policy Evaluation

**Policy** defines the rules that govern whether an action is allowed, denied, or must be escalated. The policy evaluation stage takes the intent and produces a result (e.g. allow, deny, escalate). This stage is responsible for applying governance rules consistently and deterministically.

### Decision

The **decision** is the outcome of policy evaluation. In this model, the decision is recorded as an **explicit artifact** before execution. This artifact includes the intent, the policy result, and metadata (e.g. timestamp, decision identifier, optional hash). The decision artifact is the primary governance record.

### Execution

**Execution** is the runtime step where the system actually performs the action. Execution happens only after a decision artifact has been produced. The runtime may use the decision record to authorize or constrain what is executed.

### Receipt

The **receipt** is runtime evidence that execution occurred. It answers “did this action actually run?” and may include outcome, timestamps, or identifiers. In a decision-artifact-centric model, the receipt is secondary evidence; the decision artifact remains the primary record of *what was decided*.

---

## Summary

| Stage | Responsibility |
|-------|----------------|
| Intent | Capture the requested action. |
| Policy | Evaluate the intent against governance rules. |
| Decision | Record the evaluated decision as a verifiable artifact. |
| Execution | Perform the action in the runtime. |
| Receipt | Record evidence that execution occurred. |

This pipeline ensures that every governed action has a clear path from request to decision to execution to evidence, with the decision artifact existing as an independent, verifiable record.
