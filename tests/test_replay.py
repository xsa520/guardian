"""Tests for replay verification."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from guardian import Guardian


def test_replay_passes_after_same_policy() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "evidence_log.jsonl"
        g = Guardian(ledger_path=str(path))
        g.decide(actor="a", action="send_email", target="t")
        g.decide(actor="a", action="delete_database", target="db")
        assert g.verify_replay() == "PASS"


def test_replay_and_ledger_valid() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "evidence_log.jsonl"
        g = Guardian(ledger_path=str(path))
        g.decide(actor="agent_1", action="send_email", target="customer")
        g.decide(actor="agent_1", action="delete_database", target="main_db")
        assert g.verify_replay() == "PASS"
        assert g.validate_ledger() == "VALID"
