# TODO add python client

import asyncio

from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.types import ElicitRequestParams, ElicitResult, TextContent
from mcp.shared.context import RequestContext

async def elicitation_callback_handler(context: RequestContext[ClientSession, None], params: ElicitRequestParams):
    print(f"[CLIENT] Received elicitation data: {params.message}")
 
    # 1. refuses no select other date
    # return ElicitResult(action="accept", content={
    #     "checkAlternative": False
    # }) # should say no booking made, WORKS

    # 2. cancels booking
    # return ElicitResult(action="decline"), WORKS

    print("[CLIENT]: Selecting alternative date: 2025-01-01")

    # 3. opts to select another date, 2025-01-01 which leads to a booking
    return ElicitResult(action="accept", content={
         "checkAlternative": True,
         "alternativeDate": "2025-01-01"
    }) # should book 1 jan instead of initial 2nd Jan


    

async def main():
    # Connect to a Server-Sent Events (SSE) server
    async with sse_client(url="http://localhost:8000/sse") as (
        read_stream,
        write_stream
    ):
        # Create a session using the client streams
        async with ClientSession(
            read_stream, 
            write_stream,
            elicitation_callback=elicitation_callback_handler) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")

            # call tool
            result = await session.call_tool("book_trip", {
                "date": "2025-01-02"
            })
            print("Result: ", result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())