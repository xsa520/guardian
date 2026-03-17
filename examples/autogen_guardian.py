import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian  # noqa: E402

guardian = Guardian()

intent = {
    "actor": "autogen_agent",
    "action": "deploy_infrastructure",
    "target": "prod_cluster",
}

if __name__ == "__main__":
    record = guardian.decide(intent)
    print("Guardian decision:", record["decision"])

