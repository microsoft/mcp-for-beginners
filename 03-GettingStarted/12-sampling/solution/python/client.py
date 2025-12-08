"""
cd to the `examples/snippets/clients` directory and run:
    uv run client
"""

import asyncio
import os

from pydantic import AnyUrl

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from mcp.shared.context import RequestContext

import os
from openai import OpenAI

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Using python to run the server
    args=["sample-server.py"]
)

async def call_llm(prompt: str, system_prompt: str) -> str:
    client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_TOKEN"],
)

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="openai/gpt-4o-mini",
        temperature=1,
        max_tokens=200,
        top_p=1
    )

    return response.choices[0].message.content


# Optional: create a sampling callback
async def handle_sampling_message(
    context: RequestContext[ClientSession, None], params: types.CreateMessageRequestParams
) -> types.CreateMessageResult:
    print(f"Sampling request: {params.messages}")

    message = params.messages[0].content.text

    # todo, call an actual llm and change below
    response = await call_llm(message, "You're a helpful assistant, keep to the topic, don't make things up too much but definitely create a compelling product description")

    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text=response,
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=handle_sampling_message) as session:
            # Initialize the connection
            await session.initialize()

            # List available prompts
            # prompts = await session.list_prompts()
            # print(f"Available prompts: {[p.name for p in prompts.prompts]}")

            # # Get a prompt (greet_user prompt from fastmcp_quickstart)
            # if prompts.prompts:
            #     prompt = await session.get_prompt("greet_user", arguments={"name": "Alice", "style": "friendly"})
            #     print(f"Prompt result: {prompt.messages[0].content}")

            # # List available resources
            # resources = await session.list_resources()
            # print(f"Available resources: {[r.uri for r in resources.resources]}")

            # List available tools
            # tools = await session.list_tools()
            # print(f"Available tools: {[t.name for t in tools.tools]}")

            # # Read a resource (greeting resource from fastmcp_quickstart)
            # resource_content = await session.read_resource(AnyUrl("greeting://World"))
            # content_block = resource_content.contents[0]
            # if isinstance(content_block, types.TextContent):
            #     print(f"Resource content: {content_block.text}")

            # Call a tool (create_product tool from fastmcp_quickstart)
            result = await session.call_tool("create_product", arguments={"product_name": "paprika", "keywords": "red, juicy, vegetable"})
            print("result:", result.content[0].text)

            result = await session.call_tool("get_products", arguments={})
            print("result:", result.content[0].text)

            # result_unstructured = result.content[0]
            # if isinstance(result_unstructured, types.TextContent):
            #     print(f"Tool result: {result_unstructured.text}")
            # result_structured = result.structuredContent
            # print(f"Structured tool result: {result_structured}")


def main():
    """Entry point for the client script."""
    asyncio.run(run())


if __name__ == "__main__":
    main()