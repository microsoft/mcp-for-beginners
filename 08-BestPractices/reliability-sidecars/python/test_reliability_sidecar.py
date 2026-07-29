from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import tempfile
from threading import Barrier
import unittest
from pathlib import Path

from reliability_sidecar import (
    OperationInProgress,
    OperationKeyConflict,
    ReconciliationConflict,
    ReliabilitySidecar,
    ResponseLost,
    TicketService,
    naive_create_support_ticket,
)


class ReliabilitySidecarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.temporary_path = Path(self.temporary_directory.name)
        self.ticket_database_path = self.temporary_path / "tickets.sqlite3"
        self.operation_database_path = self.temporary_path / "operations.sqlite3"
        self.ticket_service = TicketService(self.ticket_database_path)
        self.sidecar = ReliabilitySidecar(
            self.operation_database_path,
            self.ticket_service,
        )

    def test_naive_retry_repeats_a_committed_effect(self) -> None:
        with self.assertRaises(ResponseLost):
            naive_create_support_ticket(
                self.ticket_service,
                title="Cannot sign in",
                inject_response_loss=True,
            )

        second_ticket = naive_create_support_ticket(
            self.ticket_service,
            title="Cannot sign in",
        )

        self.assertEqual("T-0002", second_ticket.ticket_id)
        self.assertEqual(2, self.ticket_service.ticket_count())

    def test_guarded_retry_reconciles_after_response_loss(self) -> None:
        operation_key = "op-login-ticket-0001"
        with self.assertRaises(ResponseLost):
            self.sidecar.create_support_ticket(
                caller_id="customer-42",
                operation_key=operation_key,
                title="Cannot sign in",
                inject_response_loss=True,
            )

        self.assertEqual(
            "claimed",
            self.sidecar.operation_state(
                caller_id="customer-42",
                operation_key=operation_key,
            ),
        )

        # A new object represents a restarted worker with no process-local
        # memory of the first attempt.
        restarted_sidecar = ReliabilitySidecar(
            self.operation_database_path,
            self.ticket_service,
        )
        result = restarted_sidecar.create_support_ticket(
            caller_id="customer-42",
            operation_key=operation_key,
            title="Cannot sign in",
        )

        self.assertEqual("T-0001", result["ticket_id"])
        self.assertEqual("verified", result["status"])
        self.assertEqual(1, self.ticket_service.ticket_count())
        self.assertEqual(
            "verified",
            restarted_sidecar.operation_state(
                caller_id="customer-42",
                operation_key=operation_key,
            ),
        )

    def test_verified_retry_returns_cached_result(self) -> None:
        arguments = {
            "caller_id": "customer-42",
            "operation_key": "op-login-ticket-0001",
            "title": "Cannot sign in",
        }

        first = self.sidecar.create_support_ticket(**arguments)
        second = self.sidecar.create_support_ticket(**arguments)

        self.assertEqual(first, second)
        self.assertEqual(1, self.ticket_service.ticket_count())

    def test_same_key_with_different_input_is_rejected(self) -> None:
        operation_key = "op-login-ticket-0001"
        self.sidecar.create_support_ticket(
            caller_id="customer-42",
            operation_key=operation_key,
            title="Cannot sign in",
        )

        with self.assertRaises(OperationKeyConflict):
            self.sidecar.create_support_ticket(
                caller_id="customer-42",
                operation_key=operation_key,
                title="Cannot reset password",
            )

        self.assertEqual(1, self.ticket_service.ticket_count())

        conflicting_ticket_service = TicketService(
            self.temporary_path / "conflicting-tickets.sqlite3"
        )
        conflicting_ticket_service.create_ticket(
            caller_id="customer-42",
            operation_key=operation_key,
            title="Cannot reset password",
        )
        conflicting_sidecar = ReliabilitySidecar(
            self.temporary_path / "conflicting-operations.sqlite3",
            conflicting_ticket_service,
        )

        with self.assertRaises(ReconciliationConflict):
            conflicting_sidecar.create_support_ticket(
                caller_id="customer-42",
                operation_key=operation_key,
                title="Cannot sign in",
            )

    def test_existing_claim_without_evidence_does_not_repeat_effect(self) -> None:
        operation_key = "op-login-ticket-0001"
        input_hash = self.sidecar._input_hash({"title": "Cannot sign in"})
        _, claim_created = self.sidecar._claim(
            caller_id="customer-42",
            operation_key=operation_key,
            input_hash=input_hash,
        )
        self.assertTrue(claim_created)

        with self.assertRaises(OperationInProgress):
            self.sidecar.create_support_ticket(
                caller_id="customer-42",
                operation_key=operation_key,
                title="Cannot sign in",
            )

        self.sidecar._mark_completed(
            caller_id="customer-42",
            operation_key=operation_key,
            result={
                "ticket_id": "T-0001",
                "operation_key": operation_key,
                "status": "completed",
            },
        )
        with self.assertRaises(ReconciliationConflict):
            self.sidecar.create_support_ticket(
                caller_id="customer-42",
                operation_key=operation_key,
                title="Cannot sign in",
            )

        self.assertEqual(0, self.ticket_service.ticket_count())

    def test_concurrent_claims_admit_one_owner_without_state_regression(
        self,
    ) -> None:
        operation_key = "op-login-ticket-0001"
        input_hash = self.sidecar._input_hash({"title": "Cannot sign in"})
        contenders = [
            ReliabilitySidecar(
                self.operation_database_path,
                self.ticket_service,
            )
            for _ in range(2)
        ]
        start_together = Barrier(2)

        def attempt_claim(sidecar: ReliabilitySidecar) -> bool:
            start_together.wait(timeout=2)
            _, claim_created = sidecar._claim(
                caller_id="customer-42",
                operation_key=operation_key,
                input_hash=input_hash,
            )
            return claim_created

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(attempt_claim, contender) for contender in contenders
            ]
            claim_results = [future.result(timeout=5) for future in futures]

        self.assertCountEqual([True, False], claim_results)

        ticket = self.ticket_service.create_ticket(
            caller_id="customer-42",
            operation_key=operation_key,
            title="Cannot sign in",
        )
        verified_result = contenders[0]._result(ticket, status="verified")
        contenders[0]._mark_verified(
            caller_id="customer-42",
            operation_key=operation_key,
            result=verified_result,
        )

        # The original owner finishes late. Its older "completed" update must
        # not replace the "verified" state written by the retrying worker.
        completed_result = contenders[1]._result(ticket, status="completed")
        contenders[1]._mark_completed(
            caller_id="customer-42",
            operation_key=operation_key,
            result=completed_result,
        )

        self.assertEqual(
            "verified",
            self.sidecar.operation_state(
                caller_id="customer-42",
                operation_key=operation_key,
            ),
        )


if __name__ == "__main__":
    unittest.main()
