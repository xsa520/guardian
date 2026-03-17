"""ExecutionReceipt: runtime evidence that execution occurred (secondary to decision artifact)."""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ExecutionReceipt:
    """Evidence that execution occurred. Used for decision/receipt correlation."""

    decision_id: str  # or decision_hash to correlate with DecisionRecord
    actor: str
    action: str
    target: str
    timestamp: str  # ISO 8601
    outcome: Optional[str] = None  # e.g. success, failure
    receipt_id: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "decision_id": self.decision_id,
            "actor": self.actor,
            "action": self.action,
            "target": self.target,
            "timestamp": self.timestamp,
        }
        if self.outcome is not None:
            d["outcome"] = self.outcome
        if self.receipt_id is not None:
            d["receipt_id"] = self.receipt_id
        if self.metadata:
            d["metadata"] = self.metadata
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "ExecutionReceipt":
        return cls(
            decision_id=d["decision_id"],
            actor=d["actor"],
            action=d["action"],
            target=d["target"],
            timestamp=d["timestamp"],
            outcome=d.get("outcome"),
            receipt_id=d.get("receipt_id"),
            metadata=d.get("metadata"),
        )
