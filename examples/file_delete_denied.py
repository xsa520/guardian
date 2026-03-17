"""Scenario: delete_file on production database is denied by Guardian."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian  # noqa: E402


def main() -> None:
    guardian = Guardian()

    intent = {
        "actor": "maintenance_agent",
        "action": "delete_database",
        "target": "prod_db",
        "metadata": {"reason": "cleanup", "environment": "production"},
    }

    record = guardian.decide(intent)
    print("Intent:", intent)
    print("Decision record:", record)


if __name__ == "__main__":
    main()

