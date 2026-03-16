# Guardian

A verifiable governance layer for autonomous AI agents.

AI agents can now execute real-world actions —  
writing code, running infrastructure, accessing databases,
triggering workflows, and moving financial assets.

But most agent systems still look like this:

Agent → Tool → Execution

This architecture is powerful — but dangerously incomplete.

When something goes wrong, most systems cannot answer:

• Who approved the action?  
• What policy allowed it?  
• Can the decision be replayed?  
• Is there verifiable evidence?  

Guardian introduces a deterministic governance layer between AI agents and execution environments.

---

# Quick Example

```python
from guardian import Guardian

guardian = Guardian()

intent = {
    "actor": "agent_finance",
    "action": "transfer_funds",
    "target": "bank_api"
}

decision = guardian.decide(intent)

print(decision)

# Possible outputs:
# ALLOW
# DENY
# ESCALATE
```

Guardian evaluates the intent against policy rules before execution.

Every decision is recorded as verifiable evidence and can be replayed for audit.

## The Missing Layer

Modern autonomous systems need more than capability.

They need governance.

Guardian inserts a control plane between agents and execution:

LLM  
 ↓  
Agent Framework  
(LangChain / CrewAI / AutoGen / Custom Agents)  
 ↓  
Guardian Governance Layer  
 ↓  
Execution Environment  
 ↓  
Evidence Ledger  
 ↓  
Replay / Audit

Every action becomes:

Intent → Policy → Decision → Evidence → Execution

This makes agent behavior:

• controllable  
• auditable  
• replayable  
• safe for production systems  

## Architecture

Guardian acts as a governance control plane.

Before any action executes:

1. The agent declares intent  
2. Guardian evaluates policy  
3. A deterministic decision is produced  
4. Evidence is written to a ledger  
5. Only then does execution happen  

## Core Principles

Guardian is built around five ideas.

**Intent** — Agents must explicitly declare the action they intend to perform.  

**Policy as Code** — Behavior is controlled by declarative policies rather than hidden logic.  

**Deterministic Decisions** — Guardian returns one of three outcomes: `ALLOW`, `DENY`, `ESCALATE`.  

**Evidence Ledger** — Every decision is recorded as verifiable evidence.  

**Replay Verification** — Decisions can be replayed and validated against policy.  

## Policy Example

Guardian policies are simple rule declarations.

```json
[
  {
    "actor": "*",
    "action": "send_email",
    "target": "*",
    "effect": "ALLOW"
  },
  {
    "actor": "*",
    "action": "delete_database",
    "target": "*",
    "effect": "DENY"
  },
  {
    "actor": "agent_finance",
    "action": "transfer_funds",
    "target": "*",
    "effect": "ESCALATE"
  }
]
```

## Why Governance Instead of Guardrails?

Most AI safety tooling focuses on guardrails.

Guardrails filter model outputs.

Guardian governs agent actions.

Guardian introduces:

• Policy-based decision control  
• Verifiable evidence logs  
• Deterministic replay verification  

This allows autonomous systems to operate with auditability and accountability.

## Example Use Cases

**AI Coding Agents**  
Prevent destructive repository changes or unsafe deployments.

**Infrastructure Automation**  
Control cloud and database operations before execution.

**Financial Agents**  
Require escalation for sensitive actions like fund transfers.

**Enterprise AI Workflows**  
Provide evidence and replayability for AI actions.

## Framework Integration

Guardian is framework-agnostic.

It can sit between any AI agent system and its execution layer, including:

• LangChain  
• CrewAI  
• AutoGen  
• Custom agent runtimes  

This allows governance to be enforced independently of the agent framework.

## Quickstart

Run the examples:

```bash
python examples/demo.py
python examples/replay_demo.py
python examples/agent_integration_demo.py
```

Expected behavior:

`send_email` → ALLOW  
`delete_database` → DENY  
`transfer_funds` → ESCALATE  

## Status

Experimental infrastructure project focused on deterministic governance for autonomous systems.

## Roadmap

Stage 1 — Core governance engine  
Stage 2 — Evidence ledger and replay verification  
Stage 3 — Policy DSL and permission model  
Stage 4 — Developer integrations  
Stage 5 — Hosted governance workflows  

## License

Apache-2.0  
See LICENSE for details.
