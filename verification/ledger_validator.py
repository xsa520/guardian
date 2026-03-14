"""Ledger validator: verifies hash chain integrity of the evidence ledger."""
import json
from pathlib import Path

from evidence.evidence_record import EvidenceRecord
from evidence.hash_chain import GENESIS_HASH, compute_hash


class LedgerValidator:
    """Verifies that each record's hash matches recomputed hash and previous_hash chain is intact."""

    def __init__(self, log_path: str = "ledger/evidence_log.jsonl") -> None:
        self._path = Path(log_path)

    def validate(self) -> str:
        """Return 'VALID' if hash chain is intact, else 'INVALID'."""
        if not self._path.exists():
            return "VALID"

        expected_prev = GENESIS_HASH
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    return "INVALID"
                rec = EvidenceRecord.from_dict(d)
                if rec.previous_hash != expected_prev:
                    return "INVALID"
                expected_hash = compute_hash(
                    rec.timestamp, rec.actor, rec.action, rec.target, rec.decision, rec.previous_hash
                )
                if rec.hash != expected_hash:
                    return "INVALID"
                expected_prev = rec.hash
        return "VALID"
