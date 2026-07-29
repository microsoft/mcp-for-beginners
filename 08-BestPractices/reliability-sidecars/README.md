# Reliability Sidecars: Idempotency and Safe Retries

## Overview

A tool can finish its real-world action and still appear to fail. For example,
a server may create a support ticket, but the connection can close before the
client receives the result. A blind retry may then create a second ticket.

This lesson introduces a vendor-neutral **reliability sidecar** pattern for
effectful MCP tools. Here, "sidecar" means a small reliability boundary around
a tool operation. It can be a library, middleware component, database-backed
service, or part of the tool implementation. It is not an MCP protocol feature
and does not have to be a separate process.

The pattern combines:

- a stable operation key created before the first effectful call;
- an immutable binding between that key, the caller, the tool, and its input;
- durable claim and progress records;
- reconciliation when the result is unknown; and
- separately recorded evidence that the effect really happened.

## Specification Status

This lesson is aligned with the `2026-07-28` MCP specification release
candidate. That revision is still a draft. The current production-ready
protocol revision remains `2025-11-25`.

The reliability pattern works with both revisions. Two details are especially
important when targeting the release candidate:

1. MCP is stateless at the protocol layer. Cross-call state must use explicit
   handles or ordinary tool arguments rather than connection-local session
   state.
2. Tasks moved from an experimental core feature to a negotiated extension.
   A task ID can help resume a long-running request, but it is not an
   idempotency key for the external action performed by that request.

## Learning Objectives

By the end of this lesson, you will be able to:

- explain why a timeout does not prove that a tool failed;
- distinguish request correlation from effect deduplication;
- design a stable operation-key contract for an effectful tool;
- choose between retry, reconciliation, and fail-closed behavior;
- preserve evidence independently from an agent's success message; and
- test the "effect committed, response lost" failure mode.

## The Ambiguous-Success Problem

Consider a tool named `create_support_ticket`:

```text
Client          MCP server          Ticket system
  | tools/call       |                    |
  |----------------->|                    |
  |                  | create ticket      |
  |                  |------------------->|
  |                  | ticket T-1007      |
  |                  |<-------------------|
  |       connection closes               |
  |<--------------- X |                    |
```

The client sees a transport failure. The ticket system already contains
`T-1007`. Retrying with no duplicate guard can create `T-1008`.

This is an **ambiguous outcome**:

- retrying may repeat a real-world effect;
- not retrying may leave the workflow unfinished; and
- the transport error alone cannot tell the client which case occurred.

## What MCP Mechanisms Do—and Do Not—Prove

- **JSON-RPC request ID:** matches a response to an in-flight request. It does
  not prove that a later retry is the same business operation.
- **Progress notification:** reports progress for an active request. It does
  not prove that an external effect committed.
- **Cancellation:** says a result is no longer needed or asks work to stop. It
  does not prove that work stopped before an external effect.
- **Trace context:** correlates telemetry across services. It does not prevent
  duplicate effects.
- **MCP Tasks extension:** provides a durable handle for long-running work. It
  does not make the downstream action idempotent.
- **Tool execution error:** gives actionable failure information. It does not
  prove that no side effect happened before the error.

These mechanisms are useful, but they solve different problems. Do not use a
JSON-RPC request ID, progress token, trace ID, or task ID as an accidental
substitute for an explicit operation contract.

## Step 1: Add an Explicit Operation Key

For an effectful tool, include an application-level operation key in the input
schema:

```json
{
  "name": "create_support_ticket",
  "description": "Creates one support ticket for a stable operation key.",
  "inputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
      "operation_key": {
        "type": "string",
        "minLength": 16,
        "maxLength": 128,
        "description": "Stable key reused for retries."
      },
      "title": {
        "type": "string",
        "minLength": 1,
        "maxLength": 200
      }
    },
    "required": ["operation_key", "title"],
    "additionalProperties": false
  },
  "outputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
      "ticket_id": {
        "type": "string"
      },
      "operation_key": {
        "type": "string"
      },
      "status": {
        "type": "string",
        "enum": ["verified"]
      }
    },
    "required": ["ticket_id", "operation_key", "status"],
    "additionalProperties": false
  }
}
```

The client or workflow coordinator creates the key before the first attempt and
stores it durably. Every retry of the same intended action uses the same key.
A new intended action uses a new key.

### Bind the Key to the Full Operation

An operation key is not globally meaningful by itself. Scope it to:

- the authenticated principal or tenant;
- the tool name and version;
- a canonical digest of effect-defining inputs; and
- the authorization or policy context when relevant.

If the same scoped key arrives with different effect-defining inputs, reject
the request. Silently accepting the new inputs could return an old result for a
different intended action.

Do not put secrets or personal data directly in the key. Use an opaque random
value and store sensitive scope information on the server.

## Step 2: Record a Durable Lifecycle

A useful lifecycle is:

```text
planned -> claimed -> completed -> verified
               \-> outcome_unknown
               \-> failed
```

- `planned`: the workflow has created the operation identity.
- `claimed`: one worker owns admission for the operation.
- `completed`: the tool or downstream service returned a result.
- `verified`: authoritative state confirms the intended effect.
- `outcome_unknown`: the effect may have happened, but evidence is incomplete.
- `failed`: authoritative evidence says the effect did not complete.

Terminal records should be immutable. If correction is necessary, append a
new evidence record rather than rewriting history.

### Admission Must Be Atomic

Two workers can receive the same retry concurrently. Use a database uniqueness
constraint, compare-and-set operation, or another atomic primitive so only one
claim is admitted.

The unique identity should cover the scoped operation key. A process-local
dictionary or lock is not sufficient when another server instance can receive
the next request.

## Step 3: Reconcile Before Retrying

When a claim exists but no terminal result is recorded:

1. Query an authoritative system using the stable operation reference.
2. If the intended effect exists exactly once, record verification and return
   the existing result.
3. If the effect definitely does not exist, retry with the same key only when
   the downstream contract makes that safe.
4. If reconciliation is unavailable or contradictory, fail closed and require
   investigation.

The strongest design forwards the operation key to a downstream API that
supports idempotency. When that is unavailable, store the key as a searchable
external reference or use another authoritative business identifier.

If the downstream system supports neither deduplication nor reconciliation,
the sidecar cannot manufacture exactly-once behavior. Human review may be the
only safe response to an ambiguous outcome.

## Safe Retry Decisions

- **Input validation failed before admission:** this is a definite failure.
  Correct the input; do not retry it unchanged.
- **Rate limit or service unavailable before any effect:** this is a known-safe
  transient failure. Retry with backoff and the same operation key.
- **Connection closed after sending:** the outcome is ambiguous. Reconcile
  first; never invent a new key.
- **Existing key has a verified result:** this is a duplicate. Return the
  recorded result.
- **Existing claim and the effect exists:** the action previously completed.
  Verify and return the external result.
- **Existing claim and the effect is authoritatively absent:** the action did
  not complete. Retry with the same key only when downstream execution is
  safe.
- **Same key has a different payload digest:** this is a contract conflict.
  Reject it and investigate.
- **Reconciliation is unavailable:** the outcome remains unknown. Fail closed
  rather than guessing.

Use bounded retries, exponential backoff, and jitter for retryable failures.
Those controls reduce load; they do not prevent duplicate effects by
themselves.

## Step 4: Separate Responses from Evidence

Treat evidence as a ladder:

1. **Agent statement**: the model says the action succeeded.
2. **Tool response**: the MCP tool returned a success result.
3. **Durable checkpoint**: the operation store recorded a result.
4. **External verification**: the authoritative system contains exactly the
   intended effect.

Higher levels are stronger. Promotion to `verified` should depend on the
evidence required by the operation's risk.

For a low-risk notification, a downstream message ID may be sufficient. For a
payment, deployment, or destructive action, verification may also require
ledger, provider, or reconciliation evidence.

## MCP Tasks Complement the Pattern

The `2026-07-28` Tasks extension is useful for long-running operations:

- the server can return a durable task handle;
- the client can poll `tasks/get`;
- the client persists the task ID across restarts;
- terminal task states do not change; and
- cancellation is cooperative.

Use a task ID to resume observation of a request. Use an operation key to
deduplicate the business effect. A robust implementation may bind both:

```text
operation key -> task ID -> external effect ID -> verification evidence
```

The task must be durably created before its handle is returned. Even so, a
connection can fail before the client receives that handle. The stable
operation key still gives the server a way to recognize the retried intent.

Do not describe cancellation as rollback. The external action may finish even
after cancellation is acknowledged, so reconciliation can still be necessary.

## Failure-Injection Exercise

The accompanying Python sample uses only the standard library and SQLite. It
simulates a support-ticket service and deliberately raises an exception after
the ticket commits but before the sidecar records completion.

Run the tests:

```bash
python -m unittest discover \
  -s 08-BestPractices/reliability-sidecars/python \
  -p "test_*.py" \
  -v
```

The exercise demonstrates:

1. a naive retry creates two tickets;
2. a guarded retry with the same key finds the first ticket;
3. a new sidecar instance resumes from the durable claim;
4. the verified result is reused without another effect; and
5. reusing a key for different inputs is rejected; and
6. a duplicate active claim with no external evidence fails closed.

For clarity, the sample does not implement stale-claim leases. A production
system that permits claim takeover needs an explicit lease-expiry policy,
atomic ownership transfer, and another reconciliation check before execution.

Open the sample:

- [Python implementation](./python/reliability_sidecar.py)
- [Deterministic tests](./python/test_reliability_sidecar.py)

## Production Checklist

- [ ] Generate the operation key before the first attempt.
- [ ] Persist the key before calling the effectful tool.
- [ ] Scope the key to principal, tool, and canonical input digest.
- [ ] Reject the same key with different effect-defining inputs.
- [ ] Use atomic duplicate admission across server instances.
- [ ] Keep records longer than the maximum retry and reconciliation window.
- [ ] Forward the key to the downstream service when supported.
- [ ] Reconcile ambiguous outcomes before executing again.
- [ ] Treat progress, traces, and model statements as observations, not commit
      evidence.
- [ ] Treat cancellation as cooperative, not transactional rollback.
- [ ] Record failures and conflicting evidence without overwriting history.
- [ ] Test concurrent duplicates and the response-lost-after-commit boundary.
- [ ] Require human review when authoritative reconciliation is impossible.

## Key Takeaways

1. A transport failure after an effectful call means **unknown**, not
   necessarily **failed**.
2. Retry safety is an application property; MCP does not promise exactly-once
   side effects.
3. The same intended action must keep the same scoped operation key.
4. Reconciliation should use authoritative state, not an agent's description
   of what happened.
5. Tasks improve durable observation, while operation keys and reconciliation
   prevent repeated business effects.

## References

- [MCP `2026-07-28` release candidate overview](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [Curriculum: What's Changing in MCP `2026-07-28`](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)
- [MCP draft specification](https://modelcontextprotocol.io/specification/draft/)
- [MCP draft tool guidance](https://modelcontextprotocol.io/specification/draft/server/tools)
- [MCP Tasks extension](https://modelcontextprotocol.io/extensions/tasks/overview)
- [MCP versioning and compatibility](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning)
- [JSON-RPC 2.0 specification](https://www.jsonrpc.org/specification)
