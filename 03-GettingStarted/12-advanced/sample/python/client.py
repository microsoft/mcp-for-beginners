from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            mcp_tools = await session.list_tools()
            print("LISTING TOOLS")

            tools = []

            for tool in mcp_tools.tools:
                print("Tool: ", tool.name)
                tools.append({
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                })

            while True:
                command = input("Enter command (or 'quit' to exit): ")
                if command == "quit":
                    break
                # Process other commands as needed

                # if command in tools, then call the tool
                if command in [tool["name"] for tool in tools]:
                    # Find the tool
                    tool = next((t for t in tools if t["name"] == command), None)
                    if tool:
                        print(f"Using tool: {tool['name']}")

                        # Prepare the arguments for the tool
                        arguments = {}
                        print("Tool arguments:", tool["parameters"])
                        for param in tool["parameters"]["properties"]:
                            print(f"Parameter: {param}")
                            arguments[param] = input(f"Enter {param}: ")

                        result = await session.call_tool(tool["name"], arguments=arguments)

                        print("Result: ", result.content)




if __name__ == "__main__":
    import asyncio

    asyncio.run(run())