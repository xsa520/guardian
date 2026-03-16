from guardian import Guardian

guardian = Guardian()

intent = {
    "actor": "autogen_agent",
    "action": "deploy_infrastructure",
    "target": "prod_cluster",
}

if __name__ == "__main__":
    record = guardian.decide(intent)
    print("Guardian decision:", record["decision"])

