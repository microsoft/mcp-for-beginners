from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from openai import OpenAI

# llm
import os
import json

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

def call_llm(prompt, functions):
    token = os.environ["GITHUB_TOKEN"]
    endpoint = "https://models.github.ai/inference"

    model_name = "gpt-4o"

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    print("CALLING LLM")
    response = client.chat.completions.create(
        messages=[
            {
            "role": "system",
            "content": "You are a helpful assistant.",
            },
            {
            "role": "user",
            "content": prompt,
            },
        ],
        model=model_name,
        tools = functions,
        # Optional parameters
        temperature=1.,
        max_tokens=1000,
        top_p=1.    
    )

    # .content if we want just see the text response 
    response_message = response.choices[0].message
    
    functions_to_call = []

    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            # print("TOOL: ", tool_call)
            name = tool_call.function.name
            print("TOOL NAME: ", name)
            args = json.loads(tool_call.function.arguments)
            functions_to_call.append({ "name": name, "args": args })

    return functions_to_call

def convert_to_llm_tool(tool):
    tool_schema = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "type": "function",
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"]
            }
        }
    }

    return tool_schema

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

        
          

            # List available tools
            tools = await session.list_tools()
            print("LISTING TOOLS")

            functions = []

            for tool in tools.tools:
                print("Tool: ", tool.name)
                # print("Tool", tool.inputSchema["properties"])
                functions.append(convert_to_llm_tool(tool))
            
            while True:
                print("Waiting for input... (type 'quit' to exit)")
                prompt = input("Enter prompt: ")
                if prompt == "quit":
                    break
            
                # ask LLM what tools to all, if any
                functions_to_call = call_llm(prompt, functions)

                # call suggested functions
                for f in functions_to_call:
                    result = await session.call_tool(f["name"], arguments=f["args"])
                    print("TOOLS result: ", result.content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())