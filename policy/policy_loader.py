"""Load policy rules from JSON (e.g. policy/default_policy.json)."""
import json
from pathlib import Path
from typing import List

from policy.policy_types import Effect, PolicyRule


class PolicyLoader:
    """Reads JSON policy file and returns list of PolicyRule objects."""

    def __init__(self, policy_path: str | Path | None = None) -> None:
        if policy_path is None:
            policy_path = Path(__file__).resolve().parent / "default_policy.json"
        self._path = Path(policy_path)

    def load(self) -> List[PolicyRule]:
        """Load rules from JSON; each object must have actor, action, target, effect."""
        if not self._path.exists():
            return []
        with open(self._path, "r", encoding="utf-8") as f:
            data = json.load(f)
        rules: List[PolicyRule] = []
        for item in data:
            rules.append(
                PolicyRule(
                    actor=item["actor"],
                    action=item["action"],
                    target=item["target"],
                    effect=item["effect"],
                )
            )
        return rules
