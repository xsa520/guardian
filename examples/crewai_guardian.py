from guardian import Guardian

guardian = Guardian()

intent = {
    "actor": "crewai_agent",
    "action": "delete_database",
    "target": "prod_db",
}

decision = guardian.decide(intent)

if decision != "ALLOW":
    print("Blocked by Guardian:", decision)

