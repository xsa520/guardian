"""Guardian: accept intent, call decision engine, record evidence, return decision."""
from guardian.decision_engine import DecisionEngine
from guardian.evidence_ledger import EvidenceLedger


class Guardian:
    """Single entry point: intent(actor, action, target) -> decision; records evidence."""

    def __init__(
        self,
        policy_path: str | None = None,
        ledger_path: str = "ledger/evidence_log.jsonl",
    ) -> None:
        self._decision_engine = DecisionEngine(policy_path)
        self._ledger = EvidenceLedger(ledger_path)

    def decide(self, actor: str, action: str, target: str) -> str:
        """Evaluate intent, record evidence, return ALLOW / DENY / ESCALATE."""
        decision = self._decision_engine.decide(actor, action, target)
        self._ledger.append(actor, action, target, decision)
        return decision

    def verify_replay(self) -> str:
        """Replay ledger: re-evaluate each record and compare. Return PASS or FAIL."""
        for rec in self._ledger.read():
            replayed = self._decision_engine.decide(
                rec["actor"], rec["action"], rec["target"]
            )
            if replayed != rec.get("decision"):
                return "FAIL"
        return "PASS"

    def validate_ledger(self) -> str:
        """Verify hash chain integrity. Return VALID or INVALID."""
        return "VALID" if self._ledger.validate_chain() else "INVALID"
