"""Guardian: decision-governance control plane API. Intent → Policy → Decision Artifact → (external) Execution → Receipt."""
from typing import Any, Dict, Optional, Union

from guardian.models import Intent, DecisionRecord
from guardian.decision.engine import DecisionEngine
from guardian.ledger.ledger import Ledger
from guardian.verification.replay import ReplayVerifier
from guardian.verification.receipt_correlation import ReceiptCorrelationVerifier
from guardian.config import GuardianConfig


class Guardian:
    """Single entry point: intent normalization, policy evaluation, decision artifact, ledger append, replay and receipt correlation."""

    def __init__(
        self,
        policy_path: Optional[str] = None,
        ledger_path: str = "ledger/evidence_log.jsonl",
        config: Optional[GuardianConfig] = None,
    ) -> None:
        if config is not None:
            policy_path = str(config.policy_path) if config.policy_path else None
            ledger_path = config.ledger_path
        self._decision_engine = DecisionEngine(policy_path)
        self._ledger = Ledger(ledger_path)
        self._replay_verifier = ReplayVerifier(ledger_path, policy_path)
        self._receipt_correlation = ReceiptCorrelationVerifier()

    def decide(
        self,
        intent: Optional[Union[Intent, Dict[str, Any]]] = None,
        *,
        actor: Optional[str] = None,
        action: Optional[str] = None,
        target: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Normalize intent, evaluate policy, produce DecisionRecord, append to ledger. Returns a dict for backward compatibility."""
        intent_obj = self._normalize_intent(intent, actor=actor, action=action, target=target, metadata=metadata)
        record = self._decision_engine.decide(intent_obj)
        self._ledger.append(record)
        return {
            "decision": record.decision,
            "reason": "Decision produced by policy evaluation.",
            "policy_id": record.policy_rule_id,
            "actor": record.intent_actor,
            "action": record.intent_action,
            "target": record.intent_target,
            "timestamp": record.timestamp,
            "decision_hash": record.decision_hash,
        }

    def decide_artifact(
        self,
        intent: Optional[Union[Intent, Dict[str, Any]]] = None,
        *,
        actor: Optional[str] = None,
        action: Optional[str] = None,
        target: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DecisionRecord:
        """Produce and record a decision artifact; return the DecisionRecord (and append to ledger)."""
        intent_obj = self._normalize_intent(intent, actor=actor, action=action, target=target, metadata=metadata)
        record = self._decision_engine.decide(intent_obj)
        self._ledger.append(record)
        return record

    def _normalize_intent(
        self,
        intent: Optional[Union[Intent, Dict[str, Any]]],
        *,
        actor: Optional[str] = None,
        action: Optional[str] = None,
        target: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Intent:
        if intent is not None:
            if isinstance(intent, Intent):
                return intent
            if isinstance(intent, dict):
                a = intent.get("actor", actor)
                b = intent.get("action", action)
                c = intent.get("target", target)
                m = intent.get("metadata", metadata)
                if a is None or b is None or c is None:
                    raise ValueError("intent must include 'actor', 'action', and 'target'")
                return Intent(actor=a, action=b, target=c, metadata=m)
            raise TypeError("intent must be an Intent or dict")
        if actor is None or action is None or target is None:
            raise ValueError("actor, action, and target are required when no intent is provided")
        return Intent(actor=actor, action=action, target=target, metadata=metadata)

    def verify_replay(self) -> str:
        """Replay ledger: re-evaluate each entry and compare. Return PASS or FAIL."""
        return self._replay_verifier.verify()

    def validate_ledger(self) -> str:
        """Verify hash chain integrity. Return VALID or INVALID."""
        return "VALID" if self._ledger.validate_chain() else "INVALID"

    def verify_receipt_correlation(
        self,
        decision_records: list[DecisionRecord],
        receipts: list[Any],
    ) -> str:
        """Verify execution receipts correlate to decision records. receipts can be ExecutionReceipt or dict."""
        from guardian.models import ExecutionReceipt
        recs = [r if isinstance(r, ExecutionReceipt) else ExecutionReceipt.from_dict(r) for r in receipts]
        return self._receipt_correlation.verify(decision_records, recs)
