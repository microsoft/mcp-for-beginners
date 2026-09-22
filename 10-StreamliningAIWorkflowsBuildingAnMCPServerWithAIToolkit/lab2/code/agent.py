"""Connect model with mcp tools in Python
# Run this python script
> pip install mcp openai
> python <this-script-path>.py
"""
import asyncio
import json
import os
from typing import Any, Dict
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client

from openai import OpenAI

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self._servers = {}
        self._tool_to_server_map = {}
        self.exit_stack = AsyncExitStack()
        self.azureai = OpenAI(
            base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )
        self.model = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1")

    async def connect_stdio_server(self, server_id: str, command: str, args: list[str], env: Dict[str, str]):
        """Connect to an MCP server using STDIO transport
        
        Args:
            server_id: Unique identifier for this server connection
            command: Command to run the MCP server
            args: Arguments for the command
            env: Optional environment variables
        """
        server_params = StdioServerParameters(
            command=command,
            args=args,
            env=env
        )
        
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        stdio, write = stdio_transport
        session = await self.exit_stack.enter_async_context(ClientSession(stdio, write))
        await session.initialize()
        
        # Register the server
        await self._register_server(server_id, session)
    
    async def connect_sse_server(self, server_id: str, url: str, headers: Dict[str, str]):
        """Connect to an MCP server using SSE transport
        
        Args:
            server_id: Unique identifier for this server connection
            url: URL of the SSE server
            headers: Optional HTTP headers
        """
        sse_context = await self.exit_stack.enter_async_context(sse_client(url=url, headers=headers))
        read, write = sse_context
        session = await self.exit_stack.enter_async_context(ClientSession(read, write))
        await session.initialize()
        
        # Register the server
        await self._register_server(server_id, session)
    
    async def _register_server(self, server_id: str, session: ClientSession):
        """Register a server and its tools in the client
        
        Args:
            server_id: Unique identifier for this server
            session: Connected ClientSession
        """
        # List available tools
        response = await session.list_tools()
        tools = response.tools
        
        # Store server connection info
        self._servers[server_id] = {
            "session": session,
            "tools": tools
        }
        
        # Update tool-to-server mapping
        for tool in tools:
            self._tool_to_server_map[tool.name] = server_id
            
        print(f"\nConnected to server '{server_id}' with tools:", [tool.name for tool in tools])

    async def chatWithTools(self, messages: list[Any]) -> None:
        """Chat with model and using tools
        Args:
            messages: Messages to send to the model
        """
        if not self._servers:
            raise ValueError("No MCP servers connected. Connect to at least one server first.")

        # Collect tools from all connected servers
        available_tools = []
        for server_id, server_info in self._servers.items():
            for tool in server_info["tools"]:
                available_tools.append({ 
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema
                    },
                })

        while True:

            # Call model
            response = self.azureai.chat.completions.create(
                messages = messages,
                model = self.model,
                tools=available_tools,
            )
            hasToolCall = False

            if response.choices[0].message.tool_calls:
                messages.append(response.choices[0].message.model_dump(exclude_none=True))
                for tool in response.choices[0].message.tool_calls:
                    hasToolCall = True
                    tool_name = tool.function.name
                    tool_args = json.loads(tool.function.arguments)
                
                
                    # Find the appropriate server for this tool
                    if tool_name in self._tool_to_server_map:
                        server_id = self._tool_to_server_map[tool_name]
                        server_session = self._servers[server_id]["session"]
                        
                        # Execute tool call on the appropriate server
                        result = await server_session.call_tool(tool_name, tool_args)
                        print(f"[Server '{server_id}' call tool '{tool_name}' with args {tool_args}]: {result.content}")

                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool.id,
                            "content": str(result.content),
                        })
            else:
                messages.append({
                    "role": "assistant",
                    "content": response.choices[0].message.content,
                })
                print(f"[Model Response]: {response.choices[0].message.content}")
        
            if not hasToolCall:
                break
    
    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()
        await asyncio.sleep(1)

async def main():
    client = MCPClient()
    messages = [
        {"role": "system", "content": "You are my browser automation assistant, helping me operate the browser"},
        {"role": "user", "content": "Navigate to github.com/kinfey"},
    ]
    try:
        await client.connect_stdio_server(
            "mcp-mbnn4zlx", 
            "npx", 
            [
                "-y",
                "@playwright/mcp@latest",
            ],
            {
            }
        )
        await client.chatWithTools(messages)
    except Exception as e:
        print(f"\nError: {str(e)}")
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())