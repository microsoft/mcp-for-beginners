"""
Complete Python MCP Client Example

This client demonstrates how to:
1. Connect to an MCP server using stdio transport
2. List available tools and resources
3. Call calculator tools
4. Handle responses from the server
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client


class MCPCalculatorClient:
    def __init__(self):
        # Create server parameters for stdio connection
        self.server_params = StdioServerParameters(
            command="python",  # Executable
            args=["../01-first-server/solution/python/server.py"],  # Server script
            env=None,  # Optional environment variables
        )

    async def run(self):
        """Main client execution function"""
        print("🚀 Starting MCP Python Client...")

        try:
            async with stdio_client(self.server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    print("📡 Connecting to MCP server...")
                    
                    # Initialize the connection
                    await session.initialize()
                    print("✅ Connected to MCP server successfully!")

                    # List available tools
                    await self.list_tools(session)
                    
                    # Test calculator operations
                    await self.test_calculator_operations(session)
                    
                    # List and test resources
                    await self.list_and_test_resources(session)
                    
                    print("\n✨ Client operations completed successfully!")

        except Exception as e:
            print(f"❌ Error running MCP client: {e}")
            raise

    async def list_tools(self, session: ClientSession):
        """List all available tools on the server"""
        print("\n📋 Listing available tools:")
        try:
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
        except Exception as e:
            print(f"  Error listing tools: {e}")

    async def test_calculator_operations(self, session: ClientSession):
        """Test various calculator operations"""
        print("\n🧮 Testing Calculator Operations:")

        # These are the tools of the server in 01-first-server/solution/python
        operations = [
            ("add", {"a": 5, "b": 3}, "Add 5 + 3"),
            ("subtract", {"a": 10, "b": 4}, "Subtract 10 - 4"),
        ]

        for tool_name, arguments, description in operations:
            try:
                result = await session.call_tool(tool_name, arguments=arguments)
                result_text = self.extract_text_result(result)
                print(f"{description} = {result_text}")
            except Exception as e:
                print(f"  Error calling {tool_name}: {e}")

    async def list_and_test_resources(self, session: ClientSession):
        """List resource templates and read a resource from one"""
        print("\n📄 Listing available resource templates:")
        try:
            templates = await session.list_resource_templates()
            for template in templates.resource_templates:
                print(f"  - {template.name}: {template.uri_template}")

            # The server exposes greeting://{name}; fill in a name to read it
            print("\n📖 Reading resource: greeting://World")
            result = await session.read_resource("greeting://World")
            for content in result.contents:
                if isinstance(content, types.TextResourceContents):
                    print(f"Resource content: {content.text}")
        except Exception as e:
            print(f"  Error reading resources: {e}")

    def extract_text_result(self, result) -> str:
        """
        Extract text content from a tool result object.

        This method attempts to extract the text content from the `content` attribute
        of the result object. If no text content is found, it falls back to converting
        the result to a string. If an error occurs during extraction, it returns "No result".

        Args:
            result: The result object returned by a tool, which may contain a `content` attribute
                    with text or other types of data.

        Returns:
            A string representing the extracted text content, or a fallback string if no text is found.
        """
        try:
            if hasattr(result, 'content') and result.content:
                for content_item in result.content:
                    if hasattr(content_item, 'text') and content_item.text:
                        return content_item.text
                    elif hasattr(content_item, 'type') and content_item.type == "text":
                        return getattr(content_item, 'text', str(content_item))
            
            # Fallback: try to convert to string
            return str(result)
        except Exception:
            return "No result"


async def main():
    """Entry point for the client"""
    client = MCPCalculatorClient()
    await client.run()


if __name__ == "__main__":
    asyncio.run(main())
