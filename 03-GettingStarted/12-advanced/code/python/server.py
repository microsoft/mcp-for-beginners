from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

from tools import tools

server = Server("example-server")

def convert_to_json(model_cls: type) -> dict:
    schema = model_cls.schema()
    properties = {}
    required = schema.get("required", [])
    for prop, details in schema.get("properties", {}).items():
        properties[prop] = {"type": details.get("type", "string")}
    return {
        "type": "object",
        "properties": properties,
        "required": required
    }

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    vm_tools = []
    for tool in tools.values():
        print(f"Registered tool: {tool['name']}")
        vm_tools.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=convert_to_json(tool["input_schema"]),
            )
        )
    return vm_tools

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools[name]

    result = "default"
    try:
        result = await tool["handler"](arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 

async def run():
    """Run the server with lifespan management."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    import asyncio

    print("Starting server...")
    asyncio.run(run())
