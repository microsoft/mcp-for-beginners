from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from reliability_sidecar import (
    OperationInProgress,
    OperationKeyConflict,
    ReliabilitySidecar,
    ResponseLost,
    TicketService,
    naive_create_support_ticket,
)


class ReliabilitySidecarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.database_path = Path(self.temporary_directory.name) / "exercise.sqlite3"
        self.ticket_service = TicketService(self.database_path)
        self.sidecar = ReliabilitySidecar(
            self.database_path,
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
                principal="customer-42",
                operation_key=operation_key,
                title="Cannot sign in",
                inject_response_loss=True,
            )

        # A new object represents a restarted worker with no process-local
        # memory of the first attempt.
        restarted_sidecar = ReliabilitySidecar(
            self.database_path,
            self.ticket_service,
        )
        result = restarted_sidecar.create_support_ticket(
            principal="customer-42",
            operation_key=operation_key,
            title="Cannot sign in",
        )

        self.assertEqual("T-0001", result["ticket_id"])
        self.assertEqual("verified", result["status"])
        self.assertEqual(1, self.ticket_service.ticket_count())
        self.assertEqual(
            "verified",
            restarted_sidecar.operation_state(
                principal="customer-42",
                operation_key=operation_key,
            ),
        )

    def test_verified_retry_returns_cached_result(self) -> None:
        arguments = {
            "principal": "customer-42",
            "operation_key": "op-billing-ticket-0001",
            "title": "Invoice is missing",
        }

        first = self.sidecar.create_support_ticket(**arguments)
        second = self.sidecar.create_support_ticket(**arguments)

        self.assertEqual(first, second)
        self.assertEqual(1, self.ticket_service.ticket_count())

    def test_same_key_with_different_input_is_rejected(self) -> None:
        operation_key = "op-profile-ticket-0001"
        self.sidecar.create_support_ticket(
            principal="customer-42",
            operation_key=operation_key,
            title="Profile is unavailable",
        )

        with self.assertRaises(OperationKeyConflict):
            self.sidecar.create_support_ticket(
                principal="customer-42",
                operation_key=operation_key,
                title="Delete my profile",
            )

        self.assertEqual(1, self.ticket_service.ticket_count())

    def test_existing_claim_without_evidence_does_not_repeat_effect(self) -> None:
        operation_key = "op-active-claim-0001"
        payload_digest = self.sidecar._payload_digest({"title": "Still processing"})
        _, claim_created = self.sidecar._claim(
            principal="customer-42",
            operation_key=operation_key,
            payload_digest=payload_digest,
        )
        self.assertTrue(claim_created)

        with self.assertRaises(OperationInProgress):
            self.sidecar.create_support_ticket(
                principal="customer-42",
                operation_key=operation_key,
                title="Still processing",
            )

        self.assertEqual(0, self.ticket_service.ticket_count())


if __name__ == "__main__":
    unittest.main()
