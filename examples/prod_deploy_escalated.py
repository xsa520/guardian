"""Scenario: deploy_service to production is escalated by Guardian."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian


def main() -> None:
    guardian = Guardian()

    intent = {
        "actor": "deploy_agent",
        "action": "deploy_service",
        "target": "prod_cluster",
        "metadata": {"service": "payments-api", "environment": "production"},
    }

    record = guardian.decide(intent)
    print("Intent:", intent)
    print("Decision record:", record)


if __name__ == "__main__":
    main()

