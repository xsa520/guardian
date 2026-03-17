"""Receipt correlation verifier: compare decision records to execution receipts."""
from typing import Iterable

from guardian.models import DecisionRecord, ExecutionReceipt


class ReceiptCorrelationVerifier:
    """Verify that execution receipts correspond to decision records (same intent, decision_id)."""

    def verify(
        self,
        decision_records: Iterable[DecisionRecord],
        receipts: Iterable[ExecutionReceipt],
    ) -> str:
        """Check that each receipt has a matching decision (by decision_id = decision_hash) and intent match.
        Returns PASS if all receipts correlate; FAIL otherwise.
        """
        decisions_by_id: dict[str, DecisionRecord] = {}
        for dr in decision_records:
            decisions_by_id[dr.decision_hash] = dr
        for rec in receipts:
            dec = decisions_by_id.get(rec.decision_id)
            if dec is None:
                return "FAIL"
            if dec.intent_actor != rec.actor or dec.intent_action != rec.action or dec.intent_target != rec.target:
                return "FAIL"
        return "PASS"

    def verify_single(self, decision_record: DecisionRecord, receipt: ExecutionReceipt) -> bool:
        """True if receipt correlates to this decision (same intent, decision_id links to record)."""
        if receipt.decision_id != decision_record.decision_hash:
            return False
        return (
            decision_record.intent_actor == receipt.actor
            and decision_record.intent_action == receipt.action
            and decision_record.intent_target == receipt.target
        )
