"""DecisionRecord: verifiable decision artifact produced before execution."""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class DecisionRecord:
    """Governance decision artifact. Exists before execution; primary evidence."""

    intent_actor: str
    intent_action: str
    intent_target: str
    policy_result: str  # ALLOW | DENY | ESCALATE
    decision: str  # same or opaque id
    decision_hash: str
    timestamp: str  # ISO 8601
    intent_metadata: Optional[dict[str, Any]] = None
    policy_rule_id: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize for ledger and schema validation."""
        d: dict[str, Any] = {
            "actor": self.intent_actor,
            "action": self.intent_action,
            "target": self.intent_target,
            "policy_result": self.policy_result,
            "decision": self.decision,
            "decision_hash": self.decision_hash,
            "timestamp": self.timestamp,
        }
        if self.intent_metadata:
            d["metadata"] = self.intent_metadata
        if self.policy_rule_id is not None:
            d["policy_rule_id"] = self.policy_rule_id
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "DecisionRecord":
        """Deserialize from ledger or API."""
        return cls(
            intent_actor=d["actor"],
            intent_action=d["action"],
            intent_target=d["target"],
            policy_result=d["policy_result"],
            decision=d["decision"],
            decision_hash=d["decision_hash"],
            timestamp=d["timestamp"],
            intent_metadata=d.get("metadata"),
            policy_rule_id=d.get("policy_rule_id"),
        )
