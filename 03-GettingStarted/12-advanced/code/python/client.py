import asyncio
import os

from pydantic import AnyUrl

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from mcp.shared.context import RequestContext

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Using uv to run the server
    args=["server.py"] # We're already in snippets dir
    
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")

            result = await session.call_tool("add", { "a": 5, "b": 3 })
            print(f"Result of add tool: {result}")

def main():
    """Entry point for the client script."""
    asyncio.run(run())


if __name__ == "__main__":
    main()