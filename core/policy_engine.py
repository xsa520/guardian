"""Policy engine: evaluates intents against loaded policy rules (no hardcoded logic)."""
from pathlib import Path
from typing import Optional

from core.intent_schema import Intent
from core.permission_model import PermissionModel
from policy.policy_loader import PolicyLoader
from policy.policy_types import PolicyRule


class PolicyEngine:
    """Evaluates intent against loaded policy rules; supports * wildcard; no match => DENY."""

    def __init__(self, policy_path: Optional[str | Path] = None) -> None:
        loader = PolicyLoader(policy_path)
        self._rules: list[PolicyRule] = loader.load()
        self._model = PermissionModel(self._rules)

    def evaluate(self, intent: Intent) -> str:
        """Return ALLOW, DENY, or ESCALATE for the given intent."""
        return self._model.decide(intent.actor, intent.action, intent.target)
