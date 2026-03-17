"""Intent: normalized representation of an action requested by an actor or agent."""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Intent:
    """An action requested by an actor or agent. Input to policy evaluation."""

    actor: str
    action: str
    target: str
    metadata: Optional[dict[str, Any]] = None

    def __post_init__(self) -> None:
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> dict[str, Any]:
        """Serialize for logging or schema validation."""
        d: dict[str, Any] = {"actor": self.actor, "action": self.action, "target": self.target}
        if self.metadata:
            d["metadata"] = self.metadata
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Intent":
        """Build Intent from dict (e.g. from API or agent framework)."""
        return cls(
            actor=d["actor"],
            action=d["action"],
            target=d["target"],
            metadata=d.get("metadata"),
        )
