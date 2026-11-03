import sys

import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server, ServerRequestContext

from tools import tools


def convert_to_json(model_cls: type) -> dict:
    schema = model_cls.model_json_schema()
    properties = {}
    required = schema.get("required", [])
    for prop, details in schema.get("properties", {}).items():
        properties[prop] = {"type": details.get("type", "string")}
    return {
        "type": "object",
        "properties": properties,
        "required": required
    }

# In mcp 2.x, the low-level Server takes its handlers as constructor arguments
# (on_list_tools=..., on_call_tool=...). Each handler receives a request context
# and the typed request params, and returns the full result object.
async def handle_list_tools(
    ctx: ServerRequestContext, params: types.PaginatedRequestParams | None
) -> types.ListToolsResult:
    """List available tools."""
    vm_tools = []
    for tool in tools.values():
        # stdio servers must keep stdout for MCP messages, so log to stderr
        print(f"Registered tool: {tool['name']}", file=sys.stderr)
        vm_tools.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                input_schema=convert_to_json(tool["input_schema"]),
            )
        )
    return types.ListToolsResult(tools=vm_tools)

async def handle_call_tool(
    ctx: ServerRequestContext, params: types.CallToolRequestParams
) -> types.CallToolResult:
    name = params.name
    arguments = params.arguments or {}

    # tools is a dictionary with tool names as keys
    if name not in tools:
        raise ValueError(f"Unknown tool: {name}")

    tool = tools[name]

    result = "default"
    try:
        result = await tool["handler"](arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return types.CallToolResult(
        content=[types.TextContent(type="text", text=str(result))]
    )

server = Server(
    "example-server",
    version="0.1.0",
    on_list_tools=handle_list_tools,
    on_call_tool=handle_call_tool,
)

async def run():
    """Run the server over stdio."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(
                notification_options=NotificationOptions(),
            ),
        )


if __name__ == "__main__":
    import asyncio

    print("Starting server...", file=sys.stderr)
    asyncio.run(run())
