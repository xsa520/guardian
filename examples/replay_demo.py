"""Replay demo: run intents, write evidence, replay ledger, print verification result."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian


def main() -> None:
    g = Guardian(ledger_path="ledger/evidence_log.jsonl")

    g.decide("agent_1", "send_email", "customer")
    print("Decision recorded: ALLOW")

    g.decide("agent_1", "delete_database", "main_db")
    print("Decision recorded: DENY")

    print("Replaying ledger...")
    print(f"Replay verification: {g.verify_replay()}")
    print(f"Ledger integrity: {g.validate_ledger()}")


if __name__ == "__main__":
    main()
