"""Configuration for the Guardian control plane."""
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class GuardianConfig:
    """Settings for policy path and ledger path."""

    policy_path: Optional[str | Path] = None
    ledger_path: str = "ledger/evidence_log.jsonl"

    def __post_init__(self) -> None:
        if self.policy_path is not None:
            self.policy_path = Path(self.policy_path)
