from guardian import Guardian

guardian = Guardian()

intent = {
    "actor": "autogen_agent",
    "action": "deploy_infrastructure",
    "target": "prod_cluster",
}

decision = guardian.decide(intent)

print("Guardian decision:", decision)

