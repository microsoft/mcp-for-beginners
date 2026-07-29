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
    caller_id: Optional[str]
    operation_key: Optional[str]


class TicketService:
    """Small stand-in for an external service with searchable references."""

    def __init__(self, ticket_database_path: Path) -> None:
        self.ticket_database_path = ticket_database_path
        with closing(self._connect()) as connection, connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS tickets (
                    ticket_number INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    caller_id TEXT,
                    operation_key TEXT
                )
                """
            )

    def create_ticket(
        self,
        *,
        title: str,
        caller_id: Optional[str],
        operation_key: Optional[str],
    ) -> Ticket:
        """Commit a ticket. This service does not deduplicate requests."""

        with closing(self._connect()) as connection, connection:
            cursor = connection.execute(
                """
                INSERT INTO tickets (title, caller_id, operation_key)
                VALUES (?, ?, ?)
                """,
                (title, caller_id, operation_key),
            )
            ticket_number = int(cursor.lastrowid)
        return Ticket(
            ticket_id=f"T-{ticket_number:04d}",
            title=title,
            caller_id=caller_id,
            operation_key=operation_key,
        )

    def find_by_operation_key(
        self,
        *,
        caller_id: str,
        operation_key: str,
    ) -> Optional[Ticket]:
        """Reconcile one operation reference against authoritative state."""

        with closing(self._connect()) as connection, connection:
            rows = connection.execute(
                """
                SELECT ticket_number, title, caller_id, operation_key
                FROM tickets
                WHERE caller_id = ?
                  AND operation_key = ?
                ORDER BY ticket_number
                LIMIT 2
                """,
                (caller_id, operation_key),
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
            caller_id=str(row["caller_id"]),
            operation_key=str(row["operation_key"]),
        )

    def ticket_count(self) -> int:
        with closing(self._connect()) as connection, connection:
            row = connection.execute("SELECT COUNT(*) AS count FROM tickets").fetchone()
        return int(row["count"])

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.ticket_database_path)
        connection.row_factory = sqlite3.Row
        return connection


class ReliabilitySidecar:
    """Guards a ticket-creating tool with durable claims and reconciliation."""

    TOOL_ID = "create_support_ticket:v1"

    def __init__(
        self,
        operation_database_path: Path,
        ticket_service: TicketService,
    ) -> None:
        self.operation_database_path = operation_database_path
        self.ticket_service = ticket_service
        with closing(self._connect()) as connection, connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS operations (
                    caller_id TEXT NOT NULL,
                    tool_id TEXT NOT NULL,
                    operation_key TEXT NOT NULL,
                    input_hash TEXT NOT NULL,
                    state TEXT NOT NULL,
                    result_json TEXT,
                    PRIMARY KEY (caller_id, tool_id, operation_key)
                )
                """
            )

    def create_support_ticket(
        self,
        *,
        caller_id: str,
        operation_key: str,
        title: str,
        inject_response_loss: bool = False,
    ) -> Dict[str, str]:
        """Create or recover one intended support-ticket operation."""

        input_hash = self._input_hash({"title": title})
        record, claim_created = self._claim(
            caller_id=caller_id,
            operation_key=operation_key,
            input_hash=input_hash,
        )

        if record["input_hash"] != input_hash:
            raise OperationKeyConflict(
                "operation key is already bound to different input"
            )

        if record["state"] == "verified":
            return self._decode_result(record)

        # A claimed record may represent a crashed worker. A completed record
        # may represent a crash between checkpointing and verification.
        existing_ticket = self.ticket_service.find_by_operation_key(
            caller_id=caller_id,
            operation_key=operation_key,
        )
        if existing_ticket is not None:
            self._require_matching_ticket(existing_ticket, expected_title=title)
            result = self._result(existing_ticket, status="verified")
            self._mark_verified(
                caller_id=caller_id,
                operation_key=operation_key,
                result=result,
            )
            return result
        if not claim_created:
            if record["state"] == "completed":
                raise ReconciliationConflict(
                    "completed operation has no matching external ticket"
                )
            raise OperationInProgress(
                "an existing claim has no terminal external evidence"
            )

        ticket = self.ticket_service.create_ticket(
            title=title,
            caller_id=caller_id,
            operation_key=operation_key,
        )

        # The effect is durable, but the caller never sees the response and the
        # operation record is still "claimed".
        if inject_response_loss:
            raise ResponseLost("ticket committed, but the response was lost")

        result = self._result(ticket, status="completed")
        self._mark_completed(
            caller_id=caller_id,
            operation_key=operation_key,
            result=result,
        )

        verified_ticket = self.ticket_service.find_by_operation_key(
            caller_id=caller_id,
            operation_key=operation_key,
        )
        if verified_ticket is None:
            raise ReconciliationConflict(
                "ticket response was returned but authoritative state is empty"
            )
        self._require_matching_ticket(verified_ticket, expected_title=title)
        verified_result = self._result(verified_ticket, status="verified")
        self._mark_verified(
            caller_id=caller_id,
            operation_key=operation_key,
            result=verified_result,
        )
        return verified_result

    def operation_state(
        self,
        *,
        caller_id: str,
        operation_key: str,
    ) -> Optional[str]:
        record = self._operation_record(
            caller_id=caller_id,
            operation_key=operation_key,
        )
        return None if record is None else str(record["state"])

    def _operation_record(
        self,
        *,
        caller_id: str,
        operation_key: str,
    ) -> Optional[sqlite3.Row]:
        with closing(self._connect()) as connection, connection:
            row = connection.execute(
                """
                SELECT input_hash, state, result_json
                FROM operations
                WHERE caller_id = ?
                  AND tool_id = ?
                  AND operation_key = ?
                """,
                (caller_id, self.TOOL_ID, operation_key),
            ).fetchone()
        return row

    def _claim(
        self,
        *,
        caller_id: str,
        operation_key: str,
        input_hash: str,
    ) -> Tuple[sqlite3.Row, bool]:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            cursor = connection.execute(
                """
                INSERT OR IGNORE INTO operations (
                    caller_id,
                    tool_id,
                    operation_key,
                    input_hash,
                    state,
                    result_json
                )
                VALUES (?, ?, ?, ?, 'claimed', NULL)
                """,
                (
                    caller_id,
                    self.TOOL_ID,
                    operation_key,
                    input_hash,
                ),
            )
            claim_created = cursor.rowcount == 1
            row = connection.execute(
                """
                SELECT input_hash, state, result_json
                FROM operations
                WHERE caller_id = ?
                  AND tool_id = ?
                  AND operation_key = ?
                """,
                (caller_id, self.TOOL_ID, operation_key),
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
        caller_id: str,
        operation_key: str,
        result: Dict[str, str],
    ) -> None:
        updated = self._update_state(
            caller_id=caller_id,
            operation_key=operation_key,
            state="completed",
            result=result,
            allowed_states=("claimed", "completed"),
        )
        if updated:
            return
        record = self._operation_record(
            caller_id=caller_id,
            operation_key=operation_key,
        )
        if record is None or record["state"] != "verified":
            raise RuntimeError("operation completion update failed")

    def _mark_verified(
        self,
        *,
        caller_id: str,
        operation_key: str,
        result: Dict[str, str],
    ) -> None:
        updated = self._update_state(
            caller_id=caller_id,
            operation_key=operation_key,
            state="verified",
            result=result,
            allowed_states=("claimed", "completed"),
        )
        if updated:
            return
        record = self._operation_record(
            caller_id=caller_id,
            operation_key=operation_key,
        )
        if record is None or record["state"] != "verified":
            raise RuntimeError("operation verification update failed")
        if self._decode_result(record) != result:
            raise ReconciliationConflict(
                "verified operation result conflicts with external evidence"
            )

    def _update_state(
        self,
        *,
        caller_id: str,
        operation_key: str,
        state: str,
        result: Dict[str, str],
        allowed_states: Tuple[str, str],
    ) -> bool:
        encoded = json.dumps(result, sort_keys=True, separators=(",", ":"))
        with closing(self._connect()) as connection, connection:
            cursor = connection.execute(
                """
                UPDATE operations
                SET state = ?, result_json = ?
                WHERE caller_id = ?
                  AND tool_id = ?
                  AND operation_key = ?
                  AND state IN (?, ?)
                """,
                (
                    state,
                    encoded,
                    caller_id,
                    self.TOOL_ID,
                    operation_key,
                    *allowed_states,
                ),
            )
        return cursor.rowcount == 1

    @staticmethod
    def _input_hash(payload: Dict[str, str]) -> str:
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    @staticmethod
    def _require_matching_ticket(
        ticket: Ticket,
        *,
        expected_title: str,
    ) -> None:
        if ticket.title != expected_title:
            raise ReconciliationConflict(
                "ticket found for the operation key has different input"
            )

    @staticmethod
    def _result(ticket: Ticket, *, status: str) -> Dict[str, str]:
        if ticket.operation_key is None:
            raise ReconciliationConflict(
                "guarded ticket is missing its operation reference"
            )
        if status not in {"completed", "verified"}:
            raise ValueError(f"unsupported operation status: {status}")
        return {
            "ticket_id": ticket.ticket_id,
            "operation_key": ticket.operation_key,
            "status": status,
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
        connection = sqlite3.connect(self.operation_database_path)
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
        caller_id=None,
        operation_key=None,
    )
    if inject_response_loss:
        raise ResponseLost("ticket committed, but the response was lost")
    return ticket
