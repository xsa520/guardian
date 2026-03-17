"""Smoke tests: run example flows without errors."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from guardian import Guardian


def test_email_send_allowed_smoke() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        g = Guardian(ledger_path=str(Path(tmp) / "log.jsonl"))
        record = g.decide(actor="notification_agent", action="send_email", target="internal_list")
    assert record["decision"] == "ALLOW"


def test_file_delete_denied_smoke() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        g = Guardian(ledger_path=str(Path(tmp) / "log.jsonl"))
        record = g.decide(actor="maintenance_agent", action="delete_database", target="prod_db")
    assert record["decision"] == "DENY"


def test_prod_deploy_escalated_smoke() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        g = Guardian(ledger_path=str(Path(tmp) / "log.jsonl"))
        record = g.decide(actor="deploy_agent", action="deploy_service", target="prod_cluster")
    assert record["decision"] == "ESCALATE"


def test_replay_demo_smoke() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "log.jsonl"
        g = Guardian(ledger_path=str(path))
        g.decide(actor="agent_1", action="send_email", target="customer")
        g.decide(actor="agent_1", action="delete_database", target="main_db")
        assert g.verify_replay() == "PASS"
        assert g.validate_ledger() == "VALID"
