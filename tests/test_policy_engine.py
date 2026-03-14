"""Tests for policy engine: ALLOW, DENY, ESCALATE, and default DENY."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from core.decision_engine import DecisionEngine
from core.intent_schema import Intent


def test_send_email_is_allow() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="any_agent", action="send_email", target="user")
    assert engine.decide(intent) == "ALLOW"


def test_delete_database_is_deny() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="any_agent", action="delete_database", target="db")
    assert engine.decide(intent) == "DENY"


def test_transfer_funds_by_agent_finance_is_escalate() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="agent_finance", action="transfer_funds", target="*")
    assert engine.decide(intent) == "ESCALATE"


def test_unknown_action_defaults_to_deny() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="agent", action="unknown_dangerous_action", target="x")
    assert engine.decide(intent) == "DENY"
