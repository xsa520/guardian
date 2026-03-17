# Interoperability

This document explains how **decision artifacts** might allow different governance systems to interoperate when they emit compatible records. This repository only explores the idea; it does not define or mandate a standard.

## The Idea

Today, governance is often implemented per system or per vendor. Each runtime or policy engine may use its own format for “what was allowed” and “what was executed.” That makes it hard to:

- Pass decisions between systems (e.g. from one policy engine to another runtime).
- Verify or replay decisions produced by another framework.
- Aggregate or audit decisions across multiple governance systems.

If multiple governance frameworks emit **compatible decision artifacts** — for example, records that share the same or a similar schema and semantics — then:

- **Exchange** — One system could consume another’s decision record to authorize or constrain execution.
- **Verification** — A verifier could validate a decision from system A using the same schema and replay logic, even if it was produced by a different policy engine.
- **Audit** — Auditors could treat decision records from different systems as a common evidence type, as long as they conform to the same contract.

Interoperability would depend on agreement (or standardization) around:

- The **structure** of the decision record (e.g. intent, actor, policy result, decision id, timestamp, optional hash).
- The **semantics** of fields (e.g. what “allow” and “deny” mean, how intent is represented).
- Optionally, **signing or hashing** so that records can be verified as unchanged and attributed to a particular evaluator.

## What This Repository Does Not Do

This repository **explores** the idea of decision artifacts and interoperability. It does not:

- Define an official or industry standard.
- Require other systems to adopt any specific schema.
- Implement or certify interoperability between real systems.

The schema in `schemas/decision_record.schema.json` is an example structure for a decision artifact. If multiple systems chose to emit records that conform to that (or a compatible) schema, interoperability could become possible; that would be a choice of those systems, not something this project mandates.
