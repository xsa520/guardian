"""Agent integration demo: three intents → send_email ALLOW, delete_database DENY, transfer_funds ESCALATE."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.decision_engine import DecisionEngine
from core.intent_schema import Intent


def main() -> None:
    engine = DecisionEngine()

    intents = [
        Intent(actor="agent_1", action="send_email", target="customer"),
        Intent(actor="agent_1", action="delete_database", target="main_db"),
        Intent(actor="agent_finance", action="transfer_funds", target="account_1"),
    ]
    for intent in intents:
        decision = engine.decide(intent)
        print(f"Intent: {intent.action} -> {decision}")


if __name__ == "__main__":
    main()
