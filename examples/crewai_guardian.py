import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian  # noqa: E402

guardian = Guardian()

intent = {
    "actor": "crewai_agent",
    "action": "delete_database",
    "target": "prod_db",
}


def run_example() -> None:
    record = guardian.decide(intent)
    if record["decision"] != "ALLOW":
        print("Blocked by Guardian:", record["decision"])


if __name__ == "__main__":
    run_example()

