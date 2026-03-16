from guardian import Guardian

guardian = Guardian()


def guarded_tool(intent):
    """Example LangChain-style tool wrapper with governance check."""
    record = guardian.decide(intent)

    if record["decision"] != "ALLOW":
        raise Exception(f"Guardian blocked action: {record['decision']}")

    return "executed"

