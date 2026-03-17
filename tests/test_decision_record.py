"""Tests for decision record generation."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from guardian import Intent, DecisionEngine


def test_decision_record_has_required_fields() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="a", action="send_email", target="t")
    record = engine.decide(intent)
    assert record.intent_actor == "a"
    assert record.intent_action == "send_email"
    assert record.intent_target == "t"
    assert record.policy_result == "ALLOW"
    assert record.decision == "ALLOW"
    assert record.decision_hash
    assert record.timestamp


def test_decision_hash_is_deterministic() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="a", action="send_email", target="t")
    r1 = engine.decide(intent)
    r2 = engine.decide(intent)
    assert r1.decision_hash == r2.decision_hash
