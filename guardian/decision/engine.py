"""Decision engine: policy evaluation + DecisionRecord generation (before execution)."""
import hashlib
import json
from datetime import datetime, timezone
from typing import Optional

from guardian.models import Intent, DecisionRecord
from guardian.policy.engine import PolicyEngine


def _compute_decision_hash(payload: dict) -> str:
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


class DecisionEngine:
    """Evaluates intent via policy and emits a DecisionRecord artifact before execution."""

    def __init__(self, policy_path: Optional[str] = None) -> None:
        self._policy = PolicyEngine(policy_path)

    def decide(self, intent: Intent) -> DecisionRecord:
        """Evaluate intent and return a DecisionRecord (artifact); no execution."""
        policy_result = self._policy.evaluate(intent)
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        payload_for_hash = {
            "actor": intent.actor,
            "action": intent.action,
            "target": intent.target,
            "policy_result": policy_result,
            "timestamp": timestamp,
        }
        decision_hash = _compute_decision_hash(payload_for_hash)
        return DecisionRecord(
            intent_actor=intent.actor,
            intent_action=intent.action,
            intent_target=intent.target,
            policy_result=policy_result,
            decision=policy_result,
            decision_hash=decision_hash,
            timestamp=timestamp,
            intent_metadata=intent.metadata or None,
            policy_rule_id=None,
        )
