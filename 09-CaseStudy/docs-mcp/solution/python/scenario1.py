# Scenario 1: Simple query to Docs MCP
# This script demonstrates how to connect to the Microsoft Learn Docs MCP server,
# send a query, and print the result.

import asyncio
import logging
import sys
from mcp.client.streamable_http import streamable_http_client
from mcp import ClientSession

import json

# Microsoft Docs MCP Server Endpoint
MCP_SERVER_URL = "https://learn.microsoft.com/api/mcp"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('mcp_client')

def prompt_user():
    """Prompt user for a search query."""
    print("Type your Microsoft Docs search query (or 'exit' to quit):")
    try:
        return input("> ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nDetected exit signal.")
        return "exit"

async def main():
    logger.info("Connecting to Microsoft Docs MCP Server at: %s", MCP_SERVER_URL)
    try:
        async with streamable_http_client(MCP_SERVER_URL) as (read_stream, write_stream, _):
            logger.info("Connection established. Initializing MCP session.")
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                logger.info("Session initialized successfully.")
                print("\n=== Microsoft Docs MCP Client ===")
                print("Tool: microsoft_docs_search")
                print("Enter documentation queries to search Microsoft Learn docs.")
                print("Type 'exit' or 'quit' to end the session.\n")
                
                while True:
                    user_query = prompt_user()
                    if not user_query:
                        print("Query cannot be empty. Please try again.")
                        continue
                    if user_query.lower() in ("exit", "quit"):
                        print("Exiting client. Goodbye!")
                        break
                    
                    try:
                        logger.info("Executing query: %s", user_query)
                        result = await session.call_tool("microsoft_docs_search", {"query": user_query})
                        # print("RESULT:", result)
                        print("\n--- Search Result ---")
                        if hasattr(result, 'content'):
                            # print(result.content)
                            for item in result.content:
                                data = json.loads(item.text)
                                # The Docs MCP server returns {"results": [...]}
                                my_list = data.get("results", []) if isinstance(data, dict) else data
                                for doc in my_list:
                                    print(f"[Title]: {doc.get('title', 'No title')}")
                                    print(f"[Content]: {doc.get('content', 'No content')}")
                                    print("---")
                                    
                        else:
                            print("No content returned from the search.")
                        print("---------------------\n")
                    except Exception as e:
                        logger.error("Query failed: %s", e)
                        print(f"Error: {e}. Please try a different query or check your connection.\n")
                        
    except Exception as e:
        logger.error("Connection error: %s", e)
        print(f"Failed to connect to Microsoft Docs MCP Server: {e}")
        print("Please check your internet connection and try again.")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting Microsoft Docs MCP Client...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
        sys.exit(0)