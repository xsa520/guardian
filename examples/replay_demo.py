"""Replay demo: run two intents, write evidence, replay ledger, print verification result."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.decision_engine import DecisionEngine
from core.intent_schema import Intent
from evidence.evidence_logger import EvidenceLogger
from verification.ledger_validator import LedgerValidator
from verification.replay_verifier import ReplayVerifier


def main() -> None:
    engine = DecisionEngine()
    logger = EvidenceLogger("ledger/evidence_log.jsonl")

    # 1. Run two intents
    intent_allow = Intent(actor="agent_1", action="send_email", target="customer")
    decision_allow = engine.decide(intent_allow)
    logger.log(intent_allow, decision_allow)
    print("Decision recorded: ALLOW")

    intent_deny = Intent(actor="agent_1", action="delete_database", target="main_db")
    decision_deny = engine.decide(intent_deny)
    logger.log(intent_deny, decision_deny)
    print("Decision recorded: DENY")

    # 2. Replay the ledger
    print("Replaying ledger...")
    verifier = ReplayVerifier("ledger/evidence_log.jsonl")
    replay_result = verifier.verify()
    print(f"Replay verification: {replay_result}")

    # 3. Verify hash chain
    validator = LedgerValidator("ledger/evidence_log.jsonl")
    integrity = validator.validate()
    print(f"Ledger integrity: {integrity}")


if __name__ == "__main__":
    main()
