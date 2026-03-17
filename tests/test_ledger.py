"""Tests for append-only ledger and hash chain."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from guardian import Guardian, Intent, DecisionEngine, Ledger


def test_ledger_append_and_read() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "evidence_log.jsonl"
        ledger = Ledger(str(path))
        engine = DecisionEngine()
        intent = Intent(actor="a", action="send_email", target="t")
        record = engine.decide(intent)
        ledger.append(record)
        entries = list(ledger.read())
        assert len(entries) == 1
        assert entries[0]["actor"] == "a"
        assert entries[0]["decision"] == "ALLOW"
        assert "hash" in entries[0]
        assert entries[0]["previous_hash"] == "0"


def test_ledger_hash_chain_valid() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "evidence_log.jsonl"
        g = Guardian(ledger_path=str(path))
        g.decide(actor="a", action="send_email", target="t")
        g.decide(actor="a", action="delete_database", target="db")
        assert g.validate_ledger() == "VALID"


def test_ledger_detects_tampering() -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False, encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": "2026-03-17T12:00:00Z",
            "actor": "a", "action": "read", "target": "f",
            "decision": "ALLOW",
            "decision_hash": "fake",
            "hash": "wrong_hash",
            "previous_hash": "0",
        }) + "\n")
        path = f.name
    try:
        g = Guardian(ledger_path=path)
        assert g.validate_ledger() == "INVALID"
    finally:
        Path(path).unlink(missing_ok=True)
