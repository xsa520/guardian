"""Replay verifier: re-evaluate ledger entries and compare decisions."""
from pathlib import Path
from typing import Iterator

from guardian.models import Intent
from guardian.decision.engine import DecisionEngine


class ReplayVerifier:
    """Read ledger, reconstruct intents, re-run DecisionEngine, verify decisions match."""

    def __init__(self, ledger_path: str = "ledger/evidence_log.jsonl", policy_path: str | None = None) -> None:
        self._path = Path(ledger_path)
        self._engine = DecisionEngine(policy_path)

    def read_entries(self) -> Iterator[dict]:
        """Yield each ledger entry (dict with actor, action, target, decision, etc.)."""
        if not self._path.exists():
            return
        import json
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except (json.JSONDecodeError, TypeError):
                    continue

    def verify(self) -> str:
        """Replay all entries: reconstruct Intent, run DecisionEngine, compare. Return PASS or FAIL."""
        for entry in self.read_entries():
            intent = Intent(
                actor=entry["actor"],
                action=entry["action"],
                target=entry["target"],
                metadata=entry.get("metadata"),
            )
            record = self._engine.decide(intent)
            if record.decision != entry.get("decision"):
                return "FAIL"
        return "PASS"
