#!/usr/bin/env python3
"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools
that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from typing import Any

from mcp.server.mcpserver import MCPServer
from mcp.server.stdio import stdio_server
from mcp.shared.message import SessionMessage
from mcp.types import DiscoverResult, JSONRPCError, JSONRPCRequest, RequestParams

PROTOCOL_VERSION = "2026-07-28"
LEGACY_PROTOCOL_VERSION = "2025-11-25"
PROTOCOL_VERSION_KEY = "io.modelcontextprotocol/protocolVersion"
CLIENT_CAPABILITIES_KEY = "io.modelcontextprotocol/clientCapabilities"
UNSUPPORTED_PROTOCOL_VERSION_ERROR = -32022


class _DefaultVersionStream:
    """Default version-less, non-handshake connections to the current protocol."""

    def __init__(self, source: Any):
        self.source = source
        self.modern: bool | None = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        message = await self.source.__anext__()
        if not isinstance(message, SessionMessage) or not isinstance(message.message, JSONRPCRequest):
            return message

        request = message.message
        if self.modern is None:
            self.modern = request.method != "initialize"

        params = dict(request.params or {})
        metadata = dict(params.get("_meta") or {})
        if self.modern and PROTOCOL_VERSION_KEY not in metadata:
            metadata[PROTOCOL_VERSION_KEY] = PROTOCOL_VERSION
            metadata.setdefault(CLIENT_CAPABILITIES_KEY, {})
            params["_meta"] = metadata
            request = request.model_copy(update={"params": params})
            return SessionMessage(request, message.metadata)
        return message

    async def aclose(self):
        await self.source.aclose()


class _SupportedVersionsStream:
    """Keep version errors consistent with dual-era discovery."""

    def __init__(self, destination: Any):
        self.destination = destination

    async def __aenter__(self):
        await self.destination.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        return await self.destination.__aexit__(exc_type, exc_value, traceback)

    async def send(self, message: SessionMessage):
        response = message.message
        if (
            isinstance(response, JSONRPCError)
            and response.error.code == UNSUPPORTED_PROTOCOL_VERSION_ERROR
        ):
            data = dict(response.error.data or {})
            data["supported"] = [PROTOCOL_VERSION, LEGACY_PROTOCOL_VERSION]
            error = response.error.model_copy(update={"data": data})
            message = SessionMessage(
                response.model_copy(update={"error": error}),
                message.metadata,
            )
        await self.destination.send(message)

    async def aclose(self):
        await self.destination.aclose()


class CalculatorMCPServer(MCPServer):
    def __init__(self, name: str):
        super().__init__(name)
        self._lowlevel_server.add_request_handler(
            "server/discover",
            RequestParams,
            self._discover,
        )

    async def _discover(self, context: Any, params: RequestParams | None) -> DiscoverResult:
        return DiscoverResult(
            supportedVersions=[PROTOCOL_VERSION, LEGACY_PROTOCOL_VERSION],
            capabilities=self._lowlevel_server.get_capabilities(
                protocol_version=context.protocol_version,
            ),
            instructions=self.instructions,
        )

    def run(self) -> None:
        import asyncio

        asyncio.run(self.run_stdio_async())

    async def run_stdio_async(self) -> None:
        async with stdio_server() as (read_stream, write_stream):
            await self._lowlevel_server.run(
                _DefaultVersionStream(read_stream),
                _SupportedVersionsStream(write_stream),
                self._lowlevel_server.create_initialization_options(),
            )
# Create an MCP server
mcp = CalculatorMCPServer("Calculator MCP Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    # Start the server
    mcp.run()
