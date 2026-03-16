"""Demo: test three intents with Guardian — send_email, delete_database, transfer_funds."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian


def main() -> None:
    g = Guardian()

    for action in ["send_email", "delete_database", "transfer_funds"]:
        actor = "agent_finance" if action == "transfer_funds" else "agent_1"
        target = "account_1" if action == "transfer_funds" else "customer"
        record = g.decide(actor=actor, action=action, target=target)
        print(f"{action} -> {record['decision']}")


if __name__ == "__main__":
    main()
