"""Demo: create an Intent, run DecisionEngine, print Guardian Decision."""
import sys
from pathlib import Path

# Ensure project root is on path when running: python examples/demo.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.intent_schema import Intent
from core.decision_engine import DecisionEngine


def main() -> None:
    intent = Intent(actor="demo_agent", action="send_email", target="config.yaml")
    engine = DecisionEngine()
    decision = engine.decide(intent)
    print(f"Guardian Decision: {decision}")


if __name__ == "__main__":
    main()
