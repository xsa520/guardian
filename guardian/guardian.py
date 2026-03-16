"""Guardian: high-level façade for intent governance and evidence logging."""
from typing import Any, Dict, Optional, Union

from core.intent_schema import Intent
from core.decision_engine import DecisionEngine
from guardian.evidence_ledger import EvidenceLedger


class Guardian:
    """Single entry point into the governance layer.

    - Accepts an intent (actor, action, target, optional metadata)
    - Evaluates it via the DecisionEngine
    - Appends evidence to the ledger
    - Returns a structured, replayable decision record
    """

    def __init__(
        self,
        policy_path: str | None = None,
        ledger_path: str = "ledger/evidence_log.jsonl",
    ) -> None:
        self._decision_engine = DecisionEngine(policy_path)
        self._ledger = EvidenceLedger(ledger_path)

    def decide(
        self,
        intent: Optional[Union[Intent, Dict[str, Any]]] = None,
        *,
        actor: Optional[str] = None,
        action: Optional[str] = None,
        target: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Evaluate intent, record evidence, and return a structured decision record.

        Canonical intent fields:
        - actor
        - action
        - target
        - metadata (optional dict)

        Returns a dict with shape:
        {
            "decision": "ALLOW" | "DENY" | "ESCALATE",
            "reason": "...",
            "policy_id": None,
            "actor": "...",
            "action": "...",
            "target": "...",
            "timestamp": "...",
        }
        """
        intent_obj: Intent

        if intent is not None:
            if isinstance(intent, Intent):
                intent_obj = intent
            elif isinstance(intent, dict):
                actor = intent.get("actor")
                action = intent.get("action")
                target = intent.get("target")
                metadata = intent.get("metadata", metadata)
                if actor is None or action is None or target is None:
                    raise ValueError("intent must include 'actor', 'action', and 'target'")
                intent_obj = Intent(actor=actor, action=action, target=target, metadata=metadata)
            else:
                raise TypeError("intent must be an Intent or dict if provided")
        else:
            if actor is None or action is None or target is None:
                raise ValueError("actor, action, and target are required when no intent is provided")
            intent_obj = Intent(actor=actor, action=action, target=target, metadata=metadata)

        decision = self._decision_engine.decide(intent_obj)
        record = self._ledger.append(intent_obj.actor, intent_obj.action, intent_obj.target, decision)

        return {
            "decision": decision,
            "reason": "Decision produced by policy evaluation.",
            "policy_id": None,
            "actor": intent_obj.actor,
            "action": intent_obj.action,
            "target": intent_obj.target,
            "timestamp": record["timestamp"],
        }

    def verify_replay(self) -> str:
        """Replay ledger: re-evaluate each record and compare. Return PASS or FAIL."""
        for rec in self._ledger.read():
            # Ledger records from EvidenceLedger.append() include "decision"
            intent = Intent(
                actor=rec["actor"],
                action=rec["action"],
                target=rec["target"],
            )
            replayed = self._decision_engine.decide(intent)
            if replayed != rec["decision"]:
                return "FAIL"
        return "PASS"

    def validate_ledger(self) -> str:
        """Verify hash chain integrity. Return VALID or INVALID."""
        return "VALID" if self._ledger.validate_chain() else "INVALID"
