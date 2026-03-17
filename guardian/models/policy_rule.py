"""PolicyRule: a single policy rule with optional wildcard (*) for actor, action, target."""
from dataclasses import dataclass
from typing import Literal

Effect = Literal["ALLOW", "DENY", "ESCALATE"]


@dataclass
class PolicyRule:
    """One rule: (actor, action, target) pattern and effect when matched."""

    actor: str
    action: str
    target: str
    effect: Effect

    def matches(self, actor: str, action: str, target: str) -> bool:
        """True if (actor, action, target) matches this rule; * matches any."""
        if self.actor != "*" and self.actor != actor:
            return False
        if self.action != "*" and self.action != action:
            return False
        if self.target != "*" and self.target != target:
            return False
        return True
