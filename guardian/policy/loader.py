"""Load policy rules from JSON."""
import json
from pathlib import Path
from typing import List

from guardian.models import PolicyRule


def _default_policy_path() -> Path:
    return Path(__file__).resolve().parent / "default_policy.json"


class PolicyLoader:
    """Load rules from JSON; each object must have actor, action, target, effect."""

    def __init__(self, policy_path: str | Path | None = None) -> None:
        self._path = Path(policy_path) if policy_path is not None else _default_policy_path()

    def load(self) -> List[PolicyRule]:
        if not self._path.exists():
            return []
        with open(self._path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [
            PolicyRule(
                actor=item["actor"],
                action=item["action"],
                target=item["target"],
                effect=item["effect"],
            )
            for item in data
        ]
