"""Replay verifier: replays the ledger and re-evaluates decisions with DecisionEngine."""
import json
from pathlib import Path
from typing import Any, Iterator

from core.decision_engine import DecisionEngine
from core.intent_schema import Intent
from evidence.evidence_record import EvidenceRecord


class ReplayVerifier:
    """Reads ledger, reconstructs intents, re-runs DecisionEngine, verifies decisions match."""

    def __init__(self, log_path: str = "ledger/evidence_log.jsonl") -> None:
        self._path = Path(log_path)
        self._engine = DecisionEngine()

    def read(self) -> Iterator[EvidenceRecord]:
        """Yield each record from the evidence ledger."""
        if not self._path.exists():
            return
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                yield EvidenceRecord.from_dict(json.loads(line))

    def verify(self) -> str:
        """Replay all records: reconstruct Intent, run DecisionEngine, compare decision. Return 'PASS' or 'FAIL'."""
        for record in self.read():
            intent = Intent(actor=record.actor, action=record.action, target=record.target, metadata=record.metadata)
            replayed = self._engine.decide(intent)
            if replayed != record.decision:
                return "FAIL"
        return "PASS"
