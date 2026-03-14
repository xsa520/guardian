"""Decision engine: evaluate policy, return ALLOW / DENY / ESCALATE; default DENY."""
from guardian.policy_engine import PolicyEngine


class DecisionEngine:
    """Returns ALLOW, DENY, or ESCALATE; default DENY when no rule matches."""

    def __init__(self, policy_path: str | None = None) -> None:
        self._policy = PolicyEngine(policy_path)

    def decide(self, actor: str, action: str, target: str) -> str:
        """Return ALLOW, DENY, or ESCALATE."""
        effect = self._policy.evaluate(actor, action, target)
        if effect is None:
            return "DENY"
        return effect
