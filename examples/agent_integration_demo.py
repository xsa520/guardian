"""Agent integration demo: three intents — send_email ALLOW, delete_database DENY, transfer_funds ESCALATE."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian


def main() -> None:
    g = Guardian()

    intents = [
        ("agent_1", "send_email", "customer"),
        ("agent_1", "delete_database", "main_db"),
        ("agent_finance", "transfer_funds", "account_1"),
    ]
    for actor, action, target in intents:
        record = g.decide(actor=actor, action=action, target=target)
        print(f"Intent: {action} -> {record['decision']}")


if __name__ == "__main__":
    main()
