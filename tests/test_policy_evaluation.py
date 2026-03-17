"""Tests for policy evaluation: ALLOW, DENY, ESCALATE, wildcards, default DENY."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from guardian import Intent, DecisionEngine


def test_send_email_is_allow() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="any_agent", action="send_email", target="user")
    record = engine.decide(intent)
    assert record.decision == "ALLOW"


def test_delete_database_is_deny() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="any_agent", action="delete_database", target="db")
    record = engine.decide(intent)
    assert record.decision == "DENY"


def test_transfer_funds_by_agent_finance_is_escalate() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="agent_finance", action="transfer_funds", target="*")
    record = engine.decide(intent)
    assert record.decision == "ESCALATE"


def test_deploy_service_prod_cluster_is_escalate() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="deploy_agent", action="deploy_service", target="prod_cluster")
    record = engine.decide(intent)
    assert record.decision == "ESCALATE"


def test_unknown_action_defaults_to_deny() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="agent", action="unknown_dangerous_action", target="x")
    record = engine.decide(intent)
    assert record.decision == "DENY"
