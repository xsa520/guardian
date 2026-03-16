from guardian import Guardian

guardian = Guardian()


def guarded_tool(intent):
    decision = guardian.decide(intent)

    if decision != "ALLOW":
        raise Exception(f"Guardian blocked action: {decision}")

    return "executed"

