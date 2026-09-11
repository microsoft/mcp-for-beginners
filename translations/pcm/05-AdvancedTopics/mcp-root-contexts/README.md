# MCP Roots (Old Feature)

> [!WARNING]
> Roots don stop dey use for MCP since `2026-07-28`. Dey still dey for dis version for
> to make am still fit work and dem fit comot am for first specification
> version wey dem go release after July 28, 2027. New tins wey you wan do suppose
> use tool parameters, resource URIs, or server configuration to carry files or folder.


## Overview

Roots make MCP client fit tell server which filesystem place dem matter for
the current request. One root get required `file://` URI and one human-readable name wey no be must.


protocol session, or access-control way. The protocol no dey force server
to only operate inside the roots wey dem list.


## Learning Objectives

By the time you finish dis lesson, you go fit:

- Talk wetin MCP Roots mean and wetin dem no mean.
- Know how the current `roots/list` multiple round-trip dey waka.
- Fit apply security controls anyhow, no need Roots.
- Fit move new tins go supported alternatives.

## Root Data

One client go return each root as `file://` URI with optional display name:

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

Clients suppose only show locations wey user don approve. Servers suppose hold
the result as guide about files wey matter, no be proof say dem get permission.

## MCP 2026-07-28 Flow

One client wey dey support Roots, e go talk this ability for every request:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

When server dey process client request, e fit return
`InputRequiredResult` wey get `roots/list` input request:

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

Client go collect the approved roots and try the original request again with
the matching `inputResponses` and the same `requestState`. This multiple round-trip
style keep the protocol stateless; no `initialize` handshake or
protocol session dey.

## Old 2025-11-25 Behavior

For MCP `2025-11-25`, clients go talk Roots during initialization. Server fit
send direct `roots/list` request, and client fit send
`notifications/roots/list_changed` when root dem change.

That kind life cycle na old behavior. No put initialization or
notification example for `2026-07-28` implementation.

## Recommended Replacements

### Tool Parameters

Make the required folder or file clear for tool schema:

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

Use MCP Resources if server fit show relevant files through stable
URIs. This one dey make discovery and picking files clear.

### Server Configuration

For fixed deployments, set allowed directories when server begin work.
This one dey more clear than to find dem during tool call.

## Security Requirements

No matter which replacement you choose:

- Make sure user agree before you show filesystem place dem.
- Check say path correct well make no be attacker fit pass through.
- Make sure authorization and sandboxing dey happen separate from root values.
- Always check permissions when dem dey access file, no be only when dem list am.
- No put sensitive paths for logs or error messages.

## Key Takeaways

- Roots na to talk which filesystem places matter; dem no store conversation
  state.
- Roots na guide, no be boundary for access.
- MCP `2026-07-28` carry the ability for every request and use
  `InputRequiredResult` for `roots/list`.
- New development suppose use tool parameters, resource URIs, or server
  configuration.

## Additional Resources

- [Roots in MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Deprecated features registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Wetin Don Change for MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->