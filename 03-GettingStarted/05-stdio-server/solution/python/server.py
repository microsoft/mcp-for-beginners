#!/usr/bin/env python3
"""
MCP stdio server example - Updated for MCP Specification 2025-06-18

This server demonstrates the recommended stdio transport instead of the 
deprecated SSE transport. The stdio transport is simpler, more secure,
and provides better performance.
"""

import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configure logging to stderr (never use stdout for logging in stdio servers)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

# Define tools using list_tools and call_tool handlers
@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools"""
    return [
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

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    if name == "add":
        result = arguments["a"] + arguments["b"]
        logger.info(f"Adding {arguments['a']} + {arguments['b']} = {result}")
        return [TextContent(type="text", text=str(result))]
    
    elif name == "multiply":
        result = arguments["a"] * arguments["b"]
        logger.info(f"Multiplying {arguments['a']} * {arguments['b']} = {result}")
        return [TextContent(type="text", text=str(result))]
    
    elif name == "get_greeting":
        greeting = f"Hello, {arguments['name']}! Welcome to the MCP stdio server."
        logger.info(f"Generated greeting for {arguments['name']}")
        return [TextContent(type="text", text=greeting)]
    
    elif name == "get_server_info":
        info = {
            "server_name": "example-stdio-server",
            "version": "1.0.0",
            "transport": "stdio",
            "capabilities": ["tools"],
            "description": "Example MCP server using stdio transport (MCP 2025-06-18 specification)"
        }
        return [TextContent(type="text", text=str(info))]
    
    else:
        raise ValueError(f"Unknown tool: {name}")

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
