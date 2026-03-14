"""Typed structures for policy rules (actor, action, target, effect)."""
from dataclasses import dataclass
from typing import Literal

Effect = Literal["ALLOW", "DENY", "ESCALATE"]


@dataclass
class PolicyRule:
    """A single policy rule with optional wildcard (*) for actor, action, target."""

    actor: str
    action: str
    target: str
    effect: Effect

    def matches(self, actor: str, action: str, target: str) -> bool:
        """Return True if (actor, action, target) matches this rule; * matches any."""
        if self.actor != "*" and self.actor != actor:
            return False
        if self.action != "*" and self.action != action:
            return False
        if self.target != "*" and self.target != target:
            return False
        return True
