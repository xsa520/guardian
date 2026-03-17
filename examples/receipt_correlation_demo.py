"""Receipt correlation demo: produce decisions, simulate execution receipts, verify correlation."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian, ExecutionReceipt


def main() -> None:
    g = Guardian(ledger_path="ledger/evidence_log_correlation_demo.jsonl")

    # Produce two decision artifacts (only ALLOW would be "executed" in a real system)
    r1 = g.decide_artifact(actor="agent_a", action="send_email", target="user")
    r2 = g.decide_artifact(actor="agent_a", action="delete_database", target="db")

    decisions = [r1, r2]
    # Simulate execution receipts only for the ALLOW decision (send_email)
    receipts = [
        ExecutionReceipt(
            decision_id=r1.decision_hash,
            actor=r1.intent_actor,
            action=r1.intent_action,
            target=r1.intent_target,
            timestamp=r1.timestamp,
            outcome="success",
        ),
    ]

    result = g.verify_receipt_correlation(decisions, receipts)
    print("Decision records:", len(decisions))
    print("Receipts (simulated):", len(receipts))
    print("Receipt correlation:", result)


if __name__ == "__main__":
    main()
