"""Tests for DecisionEngine."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from core.intent_schema import Intent
from core.decision_engine import DecisionEngine


def test_delete_database_is_denied() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="agent", action="delete_database", target="main_db")
    assert engine.decide(intent) == "DENY"


def test_allowed_action_returns_allow() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="agent", action="send_email", target="data.txt")
    assert engine.decide(intent) == "ALLOW"
