"""Evidence ledger: append decisions with timestamp and SHA256 hash chain."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def _compute_hash(payload: dict) -> str:
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


class EvidenceLedger:
    """Append-only ledger: each record has timestamp and hash chain (hash, previous_hash)."""

    GENESIS = "0"

    def __init__(self, log_path: str = "ledger/evidence_log.jsonl") -> None:
        self._path = Path(log_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def _last_hash(self) -> str:
        if not self._path.exists():
            return self.GENESIS
        last = self.GENESIS
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    last = rec.get("hash", self.GENESIS)
                except (json.JSONDecodeError, TypeError):
                    pass
        return last

    def append(self, actor: str, action: str, target: str, decision: str) -> dict:
        """Append one decision with timestamp and hash chain; return the record."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        previous_hash = self._last_hash()
        payload = {
            "timestamp": timestamp,
            "actor": actor,
            "action": action,
            "target": target,
            "decision": decision,
            "previous_hash": previous_hash,
        }
        record_hash = _compute_hash(payload)
        payload["hash"] = record_hash
        with open(self._path, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
        return payload

    def read(self):
        """Yield each record from the ledger."""
        if not self._path.exists():
            return
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except (json.JSONDecodeError, TypeError):
                    continue

    def validate_chain(self) -> bool:
        """Verify hash chain integrity; return True if valid."""
        expected_prev = self.GENESIS
        for rec in self.read():
            if rec.get("previous_hash") != expected_prev:
                return False
            payload = {k: rec[k] for k in ["timestamp", "actor", "action", "target", "decision", "previous_hash"] if k in rec}
            expected_hash = _compute_hash(payload)
            if rec.get("hash") != expected_hash:
                return False
            expected_prev = rec["hash"]
        return True
