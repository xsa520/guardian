# Example Decision Flow

This document walks through a single decision from intent to ledger entry.

## 1. Intent

An agent (or application) wants to perform an action. It submits an intent to Guardian:

```json
{
  "actor": "notification_agent",
  "action": "send_email",
  "target": "internal_list",
  "metadata": { "subject": "Status update" }
}
```

Guardian **normalizes** this (e.g. into an `Intent` model) and passes it to the policy engine.

## 2. Policy Evaluation

Guardian loads policy rules (e.g. from `guardian/policy/default_policy.json`) and evaluates the intent. Rules are matched in order; `*` is a wildcard.

Example rule:

```json
{ "actor": "*", "action": "send_email", "target": "*", "effect": "ALLOW" }
```

The first matching rule yields **ALLOW**. If no rule matches, the result is **DENY**.

## 3. Decision Artifact

Before any execution, Guardian produces a **DecisionRecord**:

- `actor`, `action`, `target` (from intent)
- `policy_result` / `decision`: ALLOW | DENY | ESCALATE
- `decision_hash`: hash of the decision payload for integrity
- `timestamp`: ISO 8601

This artifact is the **primary governance record**.

## 4. Ledger Append

The decision is appended to the **evidence ledger** (append-only, hash-chained). Each entry includes:

- The decision artifact fields
- `previous_hash` and `hash` for chain integrity

## 5. Return to Caller

Guardian returns the decision (and optionally the full record) to the caller. The **caller** (or a separate runtime enforcement layer) is responsible for:

- Allowing or blocking execution based on the decision
- Performing the actual execution
- Producing an execution receipt if needed

## 6. Replay and Receipt Correlation (Optional)

- **Replay**: Read the ledger, re-run policy for each entry, and verify that the re-evaluated decision matches the stored decision.
- **Receipt correlation**: Given a list of decision records and a list of execution receipts (each receipt has a `decision_id` linking to a decision), verify that receipts match the decisions (same intent, correct link).

## Code Sketch

```python
from guardian import Guardian

g = Guardian()
record = g.decide(actor="notification_agent", action="send_email", target="internal_list")
# record["decision"] == "ALLOW"
# record["decision_hash"] links this to the ledger entry

# Later: replay
assert g.verify_replay() == "PASS"
assert g.validate_ledger() == "VALID"
```

Execution and receipt production happen **outside** Guardian.
