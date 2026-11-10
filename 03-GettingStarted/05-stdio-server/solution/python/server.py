#!/usr/bin/env python3
"""
MCP stdio server example - Updated for MCP Specification 2025-06-18

This server demonstrates the recommended stdio transport instead of the 
deprecated SSE transport. The stdio transport is simpler, more secure,
and provides better performance.
"""

import asyncio
import logging

import jsonschema  # installed together with the mcp package
from mcp.server import Server, ServerRequestContext
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequestParams,
    CallToolResult,
    ListToolsResult,
    PaginatedRequestParams,
    TextContent,
    Tool,
)

# Configure logging to stderr (never use stdout for logging in stdio servers)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Define tools using list_tools and call_tool handlers.
# In mcp 2.x, the low-level Server receives its handlers as constructor
# arguments (on_list_tools=..., on_call_tool=...) instead of decorators.
TOOLS = [
    Tool(
        name="add",
        description="Add two numbers together",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    ),
    Tool(
        name="multiply",
        description="Multiply two numbers together",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    ),
    Tool(
        name="get_greeting",
        description="Generate a personalized greeting",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Name to greet"}
            },
            "required": ["name"]
        }
    ),
    Tool(
        name="get_server_info",
        description="Get information about this MCP server",
        inputSchema={"type": "object", "properties": {}}
    )
]
TOOLS_BY_NAME = {tool.name: tool for tool in TOOLS}


async def list_tools(ctx: ServerRequestContext, params: PaginatedRequestParams | None) -> ListToolsResult:
    """List available tools"""
    return ListToolsResult(tools=TOOLS)


def error_result(message: str) -> CallToolResult:
    """A failed tool call is a normal result with is_error set."""
    return CallToolResult(content=[TextContent(type="text", text=message)], is_error=True)

async def call_tool(ctx: ServerRequestContext, params: CallToolRequestParams) -> CallToolResult:
    """Handle tool calls"""
    name = params.name
    arguments = params.arguments or {}

    # The low-level Server does not validate arguments for us, so check them
    # against the tool's input schema before using them
    tool = TOOLS_BY_NAME.get(name)
    if tool is None:
        return error_result(f"Unknown tool: {name}")
    try:
        jsonschema.validate(arguments, tool.input_schema)
    except jsonschema.ValidationError as e:
        return error_result(f"Invalid arguments for {name}: {e.message}")

    if name == "add":
        result = arguments["a"] + arguments["b"]
        logger.info(f"Adding {arguments['a']} + {arguments['b']} = {result}")
        return CallToolResult(content=[TextContent(type="text", text=str(result))])
    
    elif name == "multiply":
        result = arguments["a"] * arguments["b"]
        logger.info(f"Multiplying {arguments['a']} * {arguments['b']} = {result}")
        return CallToolResult(content=[TextContent(type="text", text=str(result))])
    
    elif name == "get_greeting":
        greeting = f"Hello, {arguments['name']}! Welcome to the MCP stdio server."
        logger.info(f"Generated greeting for {arguments['name']}")
        return CallToolResult(content=[TextContent(type="text", text=greeting)])
    
    elif name == "get_server_info":
        info = {
            "server_name": "example-stdio-server",
            "version": "1.0.0",
            "transport": "stdio",
            "capabilities": ["tools"],
            "description": "Example MCP server using stdio transport (MCP 2025-06-18 specification)"
        }
        return CallToolResult(content=[TextContent(type="text", text=str(info))])
    
    else:
        return error_result(f"Unknown tool: {name}")

# Create the server
server = Server(
    "example-stdio-server",
    version="1.0.0",
    on_list_tools=list_tools,
    on_call_tool=call_tool,
)

async def main():
    """Main server function using stdio transport"""
    logger.info("Starting MCP stdio server...")
    
    try:
        # Use stdio transport - this is the recommended approach
        async with stdio_server() as (read_stream, write_stream):
            logger.info("Server connected via stdio transport")
            await server.run(
                read_stream,
                write_stream,
                server.create_initialization_options()
            )
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
