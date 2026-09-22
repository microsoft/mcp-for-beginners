# MCP Roots (Legacy Feature)

> [!WARNING]
> Roots are deprecated as of MCP `2026-07-28`. They remain in this revision for
> compatibility and are eligible for removal in the first specification
> revision released on or after July 28, 2027. New implementations should pass
> directories or files through tool parameters, resource URIs, or server
> configuration.

## Overview

Roots let an MCP client tell a server which filesystem locations are relevant
to the current request. A root contains a required `file://` URI and an optional
human-readable name.

Roots are informational hints. They are not conversation-history containers,
protocol sessions, or an access-control mechanism. The protocol does not
enforce that a server stays within the listed roots.

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain what MCP Roots represent and what they do not represent.
- Recognize the current `roots/list` multi-round-trip flow.
- Apply security controls independently of Roots.
- Migrate new implementations to supported alternatives.

## Root Data

A client returns each root as a `file://` URI with an optional display name:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Clients should expose only locations approved by the user. Servers should treat
the result as guidance about relevant files, not as proof of authorization.

## MCP 2026-07-28 Flow

A client that supports Roots declares the capability in every request:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

While processing a client request, a server can return an
`InputRequiredResult` containing a `roots/list` input request:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

The client gathers the approved roots and retries the original request with the
matching `inputResponses` and unchanged `requestState`. This multi-round-trip
pattern keeps the protocol stateless; there is no `initialize` handshake or
protocol-level session.

## Legacy 2025-11-25 Behavior

In MCP `2025-11-25`, clients advertised Roots during initialization. A server
could issue a direct `roots/list` request, and a client could send
`notifications/roots/list_changed` when its roots changed.

That lifecycle is legacy behavior. Do not combine its initialization or
notification examples with a `2026-07-28` implementation.

## Recommended Replacements

### Tool Parameters

Make the required directory or file explicit in the tool schema:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### Resource URIs

Use MCP Resources when the server can expose the relevant files through stable
URIs. This keeps discovery and retrieval explicit.

### Server Configuration

For fixed deployments, configure allowed directories when the server starts.
This is often clearer than discovering them during a tool call.

## Security Requirements

Whichever replacement you choose:

- Obtain user consent before exposing filesystem locations.
- Canonicalize and validate paths to prevent traversal.
- Enforce authorization and sandboxing independently of root values.
- Recheck permissions when a file is accessed, not only when it is listed.
- Avoid returning sensitive paths in logs or error messages.

## Key Takeaways

- Roots describe relevant filesystem locations; they do not store conversation
  state.
- Roots are guidance, not an access-control boundary.
- MCP `2026-07-28` carries the capability per request and uses
  `InputRequiredResult` for `roots/list`.
- New implementations should use tool parameters, resource URIs, or server
  configuration instead.

## Additional Resources

- [Roots in MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Deprecated features registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->