"""Tests for decision/receipt correlation verifier."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from guardian import (
    Guardian,
    DecisionRecord,
    ExecutionReceipt,
    ReceiptCorrelationVerifier,
)


def test_correlation_pass() -> None:
    verifier = ReceiptCorrelationVerifier()
    dr = DecisionRecord(
        intent_actor="a",
        intent_action="send_email",
        intent_target="t",
        policy_result="ALLOW",
        decision="ALLOW",
        decision_hash="h1",
        timestamp="2026-03-17T12:00:00Z",
    )
    rec = ExecutionReceipt(decision_id="h1", actor="a", action="send_email", target="t", timestamp="2026-03-17T12:01:00Z")
    assert verifier.verify_single(dr, rec) is True
    assert verifier.verify([dr], [rec]) == "PASS"


def test_correlation_fail_wrong_intent() -> None:
    verifier = ReceiptCorrelationVerifier()
    dr = DecisionRecord(
        intent_actor="a",
        intent_action="send_email",
        intent_target="t",
        policy_result="ALLOW",
        decision="ALLOW",
        decision_hash="h1",
        timestamp="2026-03-17T12:00:00Z",
    )
    rec = ExecutionReceipt(decision_id="h1", actor="a", action="delete_database", target="t", timestamp="2026-03-17T12:01:00Z")
    assert verifier.verify_single(dr, rec) is False


def test_correlation_fail_unknown_decision_id() -> None:
    verifier = ReceiptCorrelationVerifier()
    dr = DecisionRecord(
        intent_actor="a",
        intent_action="send_email",
        intent_target="t",
        policy_result="ALLOW",
        decision="ALLOW",
        decision_hash="h1",
        timestamp="2026-03-17T12:00:00Z",
    )
    rec = ExecutionReceipt(decision_id="other", actor="a", action="send_email", target="t", timestamp="2026-03-17T12:01:00Z")
    assert verifier.verify([dr], [rec]) == "FAIL"
