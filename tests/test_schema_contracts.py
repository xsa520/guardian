"""Tests that runtime objects conform to schema expectations (contract tests)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from guardian import Intent, DecisionEngine, Ledger, DecisionRecord


def test_intent_to_dict_has_required_fields() -> None:
    intent = Intent(actor="a", action="act", target="t")
    d = intent.to_dict()
    assert d["actor"] == "a"
    assert d["action"] == "act"
    assert d["target"] == "t"


def test_decision_record_to_dict_has_required_fields() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="a", action="send_email", target="t")
    record = engine.decide(intent)
    d = record.to_dict()
    assert "actor" in d and d["actor"] == "a"
    assert "action" in d and "target" in d
    assert "decision" in d and "decision_hash" in d and "timestamp" in d
    assert "policy_result" in d


def test_ledger_entry_has_chain_and_decision_fields() -> None:
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "log.jsonl"
        ledger = Ledger(str(path))
        engine = DecisionEngine()
        record = engine.decide(Intent(actor="a", action="send_email", target="t"))
        entry = ledger.append(record)
        assert "hash" in entry and "previous_hash" in entry
        assert "decision_hash" in entry and "decision" in entry
        assert entry["actor"] == "a"
