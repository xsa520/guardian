"""Policy engine: load JSON rules, support wildcard *, return rule effect."""
import json
from pathlib import Path
from typing import Any, List

Effect = str  # "ALLOW" | "DENY" | "ESCALATE"


def _matches(rule: dict, actor: str, action: str, target: str) -> bool:
    if rule.get("actor") != "*" and rule.get("actor") != actor:
        return False
    if rule.get("action") != "*" and rule.get("action") != action:
        return False
    if rule.get("target") != "*" and rule.get("target") != target:
        return False
    return True


class PolicyEngine:
    """Loads JSON policy rules and returns effect for (actor, action, target)."""

    def __init__(self, policy_path: str | Path | None = None) -> None:
        if policy_path is None:
            policy_path = Path(__file__).resolve().parent.parent / "policies" / "example_policy.json"
        self._path = Path(policy_path)
        self._rules: List[dict] = []
        self._load()

    def _load(self) -> None:
        if not self._path.exists():
            return
        with open(self._path, "r", encoding="utf-8") as f:
            self._rules = json.load(f)

    def evaluate(self, actor: str, action: str, target: str) -> Effect | None:
        """Return effect of first matching rule, or None if no match (caller uses DENY)."""
        for rule in self._rules:
            if _matches(rule, actor, action, target):
                return rule.get("effect")
        return None
