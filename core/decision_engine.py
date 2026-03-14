"""Decision engine: orchestrates policy evaluation and returns ALLOW / DENY / ESCALATE."""
from pathlib import Path
from typing import Optional

from core.intent_schema import Intent
from core.policy_engine import PolicyEngine


class DecisionEngine:
    """Evaluates intents via PolicyEngine and returns ALLOW, DENY, or ESCALATE."""

    def __init__(self, policy_path: Optional[str | Path] = None) -> None:
        self._policy = PolicyEngine(policy_path)

    def decide(self, intent: Intent) -> str:
        """Return 'ALLOW', 'DENY', or 'ESCALATE' for the given intent."""
        return self._policy.evaluate(intent)
