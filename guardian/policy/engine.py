"""Deterministic policy engine: ALLOW / DENY / ESCALATE with wildcard matching; default DENY."""
from typing import List, Optional

from guardian.models import Intent, PolicyRule, Effect
from guardian.policy.loader import PolicyLoader


class PolicyEngine:
    """Evaluate intent against loaded rules. First match wins; no match => DENY."""

    def __init__(self, policy_path: str | None = None) -> None:
        loader = PolicyLoader(policy_path)
        self._rules: List[PolicyRule] = loader.load()

    def evaluate(self, intent: Intent) -> Effect:
        """Return ALLOW, DENY, or ESCALATE for the first matching rule; else DENY."""
        for rule in self._rules:
            if rule.matches(intent.actor, intent.action, intent.target):
                return rule.effect
        return "DENY"

    def evaluate_triple(self, actor: str, action: str, target: str) -> Effect:
        """Convenience: evaluate (actor, action, target) without an Intent."""
        for rule in self._rules:
            if rule.matches(actor, action, target):
                return rule.effect
        return "DENY"
