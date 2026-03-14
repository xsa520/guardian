"""Tests for replay verification and evidence ledger."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from core.decision_engine import DecisionEngine
from core.intent_schema import Intent
from evidence.evidence_logger import EvidenceLogger
from evidence.hash_chain import GENESIS_HASH, compute_hash
from verification.ledger_validator import LedgerValidator
from verification.replay_verifier import ReplayVerifier


def test_delete_database_intent_produces_deny() -> None:
    engine = DecisionEngine()
    intent = Intent(actor="agent", action="delete_database", target="main_db")
    assert engine.decide(intent) == "DENY"


def test_replay_validation_passes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        ledger = Path(tmp) / "evidence_log.jsonl"
        logger = EvidenceLogger(str(ledger))
        engine = DecisionEngine()

        intent_allow = Intent(actor="a", action="read", target="f")
        logger.log(intent_allow, engine.decide(intent_allow))
        intent_deny = Intent(actor="a", action="delete_database", target="db")
        logger.log(intent_deny, engine.decide(intent_deny))

        verifier = ReplayVerifier(str(ledger))
        assert verifier.verify() == "PASS"

        validator = LedgerValidator(str(ledger))
        assert validator.validate() == "VALID"


def test_ledger_validator_detects_tampering() -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False, encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": "2026-03-15T12:00:00Z",
            "actor": "a", "action": "read", "target": "f",
            "decision": "ALLOW",
            "hash": "wrong_hash",
            "previous_hash": GENESIS_HASH,
        }) + "\n")
        path = f.name
    try:
        validator = LedgerValidator(path)
        assert validator.validate() == "INVALID"
    finally:
        Path(path).unlink(missing_ok=True)
