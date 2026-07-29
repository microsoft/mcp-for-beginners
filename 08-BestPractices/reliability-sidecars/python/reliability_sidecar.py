"""Deterministic reliability-sidecar example using only Python and SQLite."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple


class ResponseLost(RuntimeError):
    """Simulates a transport failure after an external effect committed."""


class OperationKeyConflict(ValueError):
    """The same scoped key was reused for different effect-defining input."""


class OperationInProgress(RuntimeError):
    """Another worker owns the claim and no terminal evidence exists yet."""


class ReconciliationConflict(RuntimeError):
    """Authoritative state contains contradictory duplicate effects."""


@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    title: str
    principal: Optional[str]
    operation_key: Optional[str]


class TicketService:
    """Small stand-in for an external service with searchable references."""

    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        with closing(self._connect()) as connection, connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS tickets (
                    ticket_number INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    principal TEXT,
                    operation_key TEXT
                )
                """
            )

    def create_ticket(
        self,
        *,
        title: str,
        principal: Optional[str],
        operation_key: Optional[str],
    ) -> Ticket:
        """Commit a ticket. This service does not deduplicate requests."""

        with closing(self._connect()) as connection, connection:
            cursor = connection.execute(
                """
                INSERT INTO tickets (title, principal, operation_key)
                VALUES (?, ?, ?)
                """,
                (title, principal, operation_key),
            )
            ticket_number = int(cursor.lastrowid)
        return Ticket(
            ticket_id=f"T-{ticket_number:04d}",
            title=title,
            principal=principal,
            operation_key=operation_key,
        )

    def find_by_operation_key(
        self,
        *,
        principal: str,
        operation_key: str,
    ) -> Optional[Ticket]:
        """Reconcile one operation reference against authoritative state."""

        with closing(self._connect()) as connection, connection:
            rows = connection.execute(
                """
                SELECT ticket_number, title, principal, operation_key
                FROM tickets
                WHERE principal = ?
                  AND operation_key = ?
                ORDER BY ticket_number
                LIMIT 2
                """,
                (principal, operation_key),
            ).fetchall()
        if len(rows) > 1:
            raise ReconciliationConflict(
                "more than one ticket exists for the operation key"
            )
        if not rows:
            return None
        row = rows[0]
        return Ticket(
            ticket_id=f"T-{int(row['ticket_number']):04d}",
            title=str(row["title"]),
            principal=str(row["principal"]),
            operation_key=str(row["operation_key"]),
        )

    def ticket_count(self) -> int:
        with closing(self._connect()) as connection, connection:
            row = connection.execute("SELECT COUNT(*) AS count FROM tickets").fetchone()
        return int(row["count"])

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection


class ReliabilitySidecar:
    """Guards one effectful tool with durable claims and reconciliation."""

    TOOL_NAME = "create_support_ticket"

    def __init__(
        self,
        database_path: Path,
        ticket_service: TicketService,
    ) -> None:
        self.database_path = database_path
        self.ticket_service = ticket_service
        with closing(self._connect()) as connection, connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS operations (
                    principal TEXT NOT NULL,
                    tool_name TEXT NOT NULL,
                    operation_key TEXT NOT NULL,
                    payload_digest TEXT NOT NULL,
                    state TEXT NOT NULL,
                    result_json TEXT,
                    PRIMARY KEY (principal, tool_name, operation_key)
                )
                """
            )

    def create_support_ticket(
        self,
        *,
        principal: str,
        operation_key: str,
        title: str,
        inject_response_loss: bool = False,
    ) -> Dict[str, str]:
        """Create or recover exactly one intended support-ticket operation."""

        payload_digest = self._payload_digest({"title": title})
        record, claim_created = self._claim(
            principal=principal,
            operation_key=operation_key,
            payload_digest=payload_digest,
        )

        if record["payload_digest"] != payload_digest:
            raise OperationKeyConflict(
                "operation key is already bound to different input"
            )

        if record["state"] == "verified":
            return self._decode_result(record)

        # A claimed record may represent a crashed worker. A completed record
        # may represent a crash between checkpointing and verification.
        existing_ticket = self.ticket_service.find_by_operation_key(
            principal=principal,
            operation_key=operation_key,
        )
        if existing_ticket is not None:
            result = self._result(existing_ticket)
            self._mark_verified(
                principal=principal,
                operation_key=operation_key,
                result=result,
            )
            return result
        if not claim_created:
            raise OperationInProgress(
                "an existing claim has no terminal external evidence"
            )

        ticket = self.ticket_service.create_ticket(
            title=title,
            principal=principal,
            operation_key=operation_key,
        )

        # The effect is durable, but the caller never sees the response and the
        # operation record is still "claimed".
        if inject_response_loss:
            raise ResponseLost("ticket committed, but the response was lost")

        result = self._result(ticket)
        self._mark_completed(
            principal=principal,
            operation_key=operation_key,
            result=result,
        )

        verified_ticket = self.ticket_service.find_by_operation_key(
            principal=principal,
            operation_key=operation_key,
        )
        if verified_ticket is None:
            raise ReconciliationConflict(
                "ticket response was returned but authoritative state is empty"
            )
        verified_result = self._result(verified_ticket)
        self._mark_verified(
            principal=principal,
            operation_key=operation_key,
            result=verified_result,
        )
        return verified_result

    def operation_state(
        self,
        *,
        principal: str,
        operation_key: str,
    ) -> Optional[str]:
        with closing(self._connect()) as connection, connection:
            row = connection.execute(
                """
                SELECT state
                FROM operations
                WHERE principal = ?
                  AND tool_name = ?
                  AND operation_key = ?
                """,
                (principal, self.TOOL_NAME, operation_key),
            ).fetchone()
        return None if row is None else str(row["state"])

    def _claim(
        self,
        *,
        principal: str,
        operation_key: str,
        payload_digest: str,
    ) -> Tuple[sqlite3.Row, bool]:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            cursor = connection.execute(
                """
                INSERT OR IGNORE INTO operations (
                    principal,
                    tool_name,
                    operation_key,
                    payload_digest,
                    state,
                    result_json
                )
                VALUES (?, ?, ?, ?, 'claimed', NULL)
                """,
                (
                    principal,
                    self.TOOL_NAME,
                    operation_key,
                    payload_digest,
                ),
            )
            claim_created = cursor.rowcount == 1
            row = connection.execute(
                """
                SELECT payload_digest, state, result_json
                FROM operations
                WHERE principal = ?
                  AND tool_name = ?
                  AND operation_key = ?
                """,
                (principal, self.TOOL_NAME, operation_key),
            ).fetchone()
            connection.commit()
        finally:
            connection.close()
        if row is None:
            raise RuntimeError("operation claim disappeared")
        return row, claim_created

    def _mark_completed(
        self,
        *,
        principal: str,
        operation_key: str,
        result: Dict[str, str],
    ) -> None:
        self._update_state(
            principal=principal,
            operation_key=operation_key,
            state="completed",
            result=result,
        )

    def _mark_verified(
        self,
        *,
        principal: str,
        operation_key: str,
        result: Dict[str, str],
    ) -> None:
        self._update_state(
            principal=principal,
            operation_key=operation_key,
            state="verified",
            result=result,
        )

    def _update_state(
        self,
        *,
        principal: str,
        operation_key: str,
        state: str,
        result: Dict[str, str],
    ) -> None:
        encoded = json.dumps(result, sort_keys=True, separators=(",", ":"))
        with closing(self._connect()) as connection, connection:
            cursor = connection.execute(
                """
                UPDATE operations
                SET state = ?, result_json = ?
                WHERE principal = ?
                  AND tool_name = ?
                  AND operation_key = ?
                """,
                (
                    state,
                    encoded,
                    principal,
                    self.TOOL_NAME,
                    operation_key,
                ),
            )
        if cursor.rowcount != 1:
            raise RuntimeError("operation state update failed")

    @staticmethod
    def _payload_digest(payload: Dict[str, str]) -> str:
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    @staticmethod
    def _result(ticket: Ticket) -> Dict[str, str]:
        if ticket.operation_key is None:
            raise ReconciliationConflict(
                "guarded ticket is missing its operation reference"
            )
        return {
            "ticket_id": ticket.ticket_id,
            "operation_key": ticket.operation_key,
            "status": "verified",
        }

    @staticmethod
    def _decode_result(record: sqlite3.Row) -> Dict[str, str]:
        raw = record["result_json"]
        if not isinstance(raw, str):
            raise RuntimeError("verified operation is missing its result")
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise RuntimeError("verified operation result is invalid")
        return {str(key): str(item) for key, item in value.items()}

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection


def naive_create_support_ticket(
    ticket_service: TicketService,
    *,
    title: str,
    inject_response_loss: bool = False,
) -> Ticket:
    """Demonstrate a retryable-looking call with no duplicate guard."""

    ticket = ticket_service.create_ticket(
        title=title,
        principal=None,
        operation_key=None,
    )
    if inject_response_loss:
        raise ResponseLost("ticket committed, but the response was lost")
    return ticket
