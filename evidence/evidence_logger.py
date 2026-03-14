"""Evidence logger: appends decisions to ledger/evidence_log.jsonl with hash chain."""
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from evidence.evidence_record import EvidenceRecord
from evidence.hash_chain import compute_hash, get_previous_hash_from_last_line


class EvidenceLogger:
    """Appends decision records to ledger/evidence_log.jsonl; each entry includes hash + previous_hash."""

    def __init__(self, log_path: str = "ledger/evidence_log.jsonl") -> None:
        self._path = Path(log_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, intent: Any, decision: str) -> EvidenceRecord:
        """Append one decision record with timestamp, hash, and previous_hash. Returns the record."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        actor = getattr(intent, "actor", "")
        action = getattr(intent, "action", "")
        target = getattr(intent, "target", "")
        metadata = getattr(intent, "metadata", None) or {}

        previous_hash = get_previous_hash_from_last_line(str(self._path))
        record_hash = compute_hash(timestamp, actor, action, target, decision, previous_hash)

        record = EvidenceRecord(
            timestamp=timestamp,
            actor=actor,
            action=action,
            target=target,
            decision=decision,
            hash=record_hash,
            previous_hash=previous_hash,
            metadata=metadata if metadata else None,
        )
        with open(self._path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record.to_dict(), ensure_ascii=False) + "\n")
        return record
