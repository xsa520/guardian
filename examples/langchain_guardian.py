import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guardian import Guardian  # noqa: E402

guardian = Guardian()


def guarded_tool(intent):
    """Example LangChain-style tool wrapper with governance check."""
    record = guardian.decide(intent)

    if record["decision"] != "ALLOW":
        raise Exception(f"Guardian blocked action: {record['decision']}")

    return "executed"

