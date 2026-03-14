"""Permission model: decides ALLOW / DENY / ESCALATE from actor, action, target."""
from typing import List

from policy.policy_types import Effect, PolicyRule


class PermissionModel:
    """Simple permission decision based on actor, action, target using policy rules."""

    def __init__(self, rules: List[PolicyRule] | None = None) -> None:
        self._rules = rules or []

    def decide(self, actor: str, action: str, target: str) -> Effect:
        """Return ALLOW, DENY, or ESCALATE for the first matching rule; else DENY."""
        for rule in self._rules:
            if rule.matches(actor, action, target):
                return rule.effect
        return "DENY"
