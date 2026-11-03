"""Client for the product description server (MCP Sampling).

DEPRECATED FEATURE: Sampling is deprecated in MCP 2026-07-28. This client keeps
the legacy flow working: it connects with the 2025-11-25 `initialize` handshake
and answers the server's `sampling/createMessage` requests by calling Azure OpenAI.

1. Start the server in another terminal: python server.py
2. Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY (optionally AZURE_OPENAI_DEPLOYMENT)
3. Run: python client.py
"""

import asyncio
import os

from mcp import ClientSession, types
from mcp.client.context import ClientRequestContext
from mcp.client.streamable_http import streamable_http_client

from openai import OpenAI

SERVER_URL = "http://localhost:8000/mcp"


async def call_llm(prompt: str, system_prompt: str) -> str:
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
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
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
        max_completion_tokens=200,
    )

    return response.choices[0].message.content


# The sampling callback runs whenever the server sends `sampling/createMessage`
async def handle_sampling_message(
    context: ClientRequestContext, params: types.CreateMessageRequestParams
) -> types.CreateMessageResult:
    print(f"Sampling request: {params.messages}")

    message = params.messages[0].content.text

    response = await call_llm(message, "You're a helpful assistant, keep to the topic, don't make things up too much but definitely create a compelling product description")

    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text=response,
        ),
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
        stopReason="endTurn",
    )


async def run():
    async with streamable_http_client(SERVER_URL) as (read, write):
        async with ClientSession(read, write, sampling_callback=handle_sampling_message) as session:
            # The 2025-11-25 initialize handshake. Sampling needs it: on a
            # 2026-07-28 connection the server cannot send sampling requests.
            await session.initialize()

            # Call the tool; the server will send us a sampling request while it runs
            result = await session.call_tool("create_product", arguments={"product_name": "paprika", "keywords": "red, juicy, vegetable"})
            print("result:", result.content[0].text)

            result = await session.call_tool("get_products", arguments={})
            print("result:", result.content[0].text)


def main():
    """Entry point for the client script."""
    asyncio.run(run())


if __name__ == "__main__":
    main()
