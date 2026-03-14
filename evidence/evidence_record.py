"""Evidence record: single ledger entry with hash chain fields."""
from dataclasses import dataclass
from typing import Any


@dataclass
class EvidenceRecord:
    """One append-only ledger entry with timestamp, intent fields, decision, and chain hashes."""

    timestamp: str
    actor: str
    action: str
    target: str
    decision: str
    hash: str
    previous_hash: str
    metadata: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize for JSONL (hash chain payload only; metadata optional)."""
        d: dict[str, Any] = {
            "timestamp": self.timestamp,
            "actor": self.actor,
            "action": self.action,
            "target": self.target,
            "decision": self.decision,
            "hash": self.hash,
            "previous_hash": self.previous_hash,
        }
        if self.metadata:
            d["metadata"] = self.metadata
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "EvidenceRecord":
        """Deserialize from JSONL line."""
        return cls(
            timestamp=d["timestamp"],
            actor=d["actor"],
            action=d["action"],
            target=d["target"],
            decision=d["decision"],
            hash=d["hash"],
            previous_hash=d["previous_hash"],
            metadata=d.get("metadata"),
        )
