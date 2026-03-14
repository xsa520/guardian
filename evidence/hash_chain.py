"""Hash chain: SHA256 chaining for append-only ledger integrity."""
import hashlib
import json
from typing import Any


GENESIS_HASH = "0"


def payload_for_hash(timestamp: str, actor: str, action: str, target: str, decision: str, previous_hash: str) -> dict[str, Any]:
    """Canonical payload used to compute record hash (key order fixed)."""
    return {
        "timestamp": timestamp,
        "actor": actor,
        "action": action,
        "target": target,
        "decision": decision,
        "previous_hash": previous_hash,
    }


def compute_hash(timestamp: str, actor: str, action: str, target: str, decision: str, previous_hash: str) -> str:
    """Compute SHA256 hash of the canonical payload (no 'hash' field in payload)."""
    payload = payload_for_hash(timestamp, actor, action, target, decision, previous_hash)
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def get_previous_hash_from_last_line(ledger_path: str) -> str:
    """Read last non-empty line from ledger and return its 'hash'; else return GENESIS_HASH."""
    from pathlib import Path
    path = Path(ledger_path)
    if not path.exists():
        return GENESIS_HASH
    last_hash = GENESIS_HASH
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                last_hash = record.get("hash", GENESIS_HASH)
            except (json.JSONDecodeError, TypeError):
                continue
    return last_hash
