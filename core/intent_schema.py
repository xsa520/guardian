"""Intent schema for agent actions evaluated by Guardian."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Intent:
    """Represents an agent's intent to perform an action."""

    actor: str
    action: str
    target: str
    metadata: Optional[dict] = None

    def __post_init__(self) -> None:
        if self.metadata is None:
            self.metadata = {}
