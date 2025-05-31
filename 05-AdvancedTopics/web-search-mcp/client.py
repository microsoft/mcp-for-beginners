#!/usr/bin/env python3
"""
Web Search MCP Client

This client demonstrates how to interact with the Web Search MCP Server
by calling its various tools for retrieving real-time web data.

The client connects to the MCP server via stdio communication and
shows how to call each of the four specialized search tools:
- general_search: For broad web search results
- news_search: For recent news articles
- product_search: For e-commerce product information
- qna: For direct question-answer snippets
"""

import asyncio
import argparse
import logging
import sys
from typing import Dict, Any
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent, TextResourceContents
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def call_tool(session: ClientSession, tool_name: str, params: Dict[str, Any]) -> None:
    """
    Call a tool on the MCP server and print the results.
    
    Args:
        session: MCP client session
        tool_name: Name of the tool to call
        params: Parameters to pass to the tool
    """
    logger.info(f"Calling {tool_name} with params: {params}")
    
    try:
        result = await session.call_tool(tool_name, arguments=params)
        
        if result and result.content:
            text_content = next((content for content in result.content 
                              if isinstance(content, TextContent)), None)
            
            if text_content:
                print(f"\n{'='*50}")
                print(f"{tool_name.upper()} RESULTS:")
                print(f"{'='*50}")
                print(text_content.text)
                print(f"{'='*50}\n")
                
                logger.info(f"Successfully called {tool_name}")
            else:
                logger.warning(f"No text content returned from {tool_name}")
                print(f"No text content returned from {tool_name}")
        else:
            logger.warning(f"No content returned from {tool_name}")
            print(f"No content returned from {tool_name}")
    except Exception as e:
        logger.error(f"Error calling {tool_name}: {e}")
        print(f"Error calling {tool_name}: {e}")

async def run_interactive_demo(session: ClientSession) -> None:
    """
    Run an interactive demo that lets the user try different search tools.
    
    Args:
        session: MCP client session
    """
    print("\n=== Web Search MCP Interactive Demo ===\n")
    try:
        # Get list of available tools
        logger.info("Getting list of tools")
        tools_response = await session.list_tools()
        tool_names = [tool.name for tool in tools_response.tools]
        
        print(f"Connected to server")
        print(f"Available tools: {', '.join(tool_names)}")
        
        while True:
            print("\nOptions:")
            print("1. General Web Search")
            print("2. News Search")
            print("3. Product Search")
            print("4. Question & Answer")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "5":
                print("Exiting demo. Goodbye!")
                break
                
            query = input("Enter your search query: ")
            
            if not query:
                print("Query cannot be empty. Please try again.")
                continue
                
            if choice == "1":
                await call_tool(session, "general_search", {"query": query})
            elif choice == "2":
                await call_tool(session, "news_search", {"query": query})
            elif choice == "3":                await call_tool(session, "product_search", {"query": query})
            elif choice == "4":
                await call_tool(session, "qna", {"question": query})
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    except Exception as e:
        logger.error(f"Error in interactive demo: {e}")
        print(f"Error: {e}")

async def run_all_tools_demo(session: ClientSession) -> None:
    """Run a demonstration of all available tools with preset queries."""
    print("\n=== Running All Tools Demo ===\n")
    
    try:
        # Get the README resource
        logger.info("Getting README resource")
        readme_response = await session.read_resource("readme://")
        if readme_response and readme_response.contents:
            text_resource = next((content for content in readme_response.contents 
                                if isinstance(content, TextResourceContents)), None)
            if text_resource:
                print(f"\n{'='*50}")
                print(f"README RESOURCE:")
                print(f"{'='*50}")
                print(text_resource.text)
                print(f"{'='*50}\n")
        
        # Test the general_search tool
        await call_tool(session, "general_search", {"query": "latest AI trends 2025", "num_results": 3})
        
        # Test the news_search tool
        await call_tool(session, "news_search", {"query": "AI policy updates", "num_results": 3})
        
        # Test the product_search tool
        await call_tool(session, "product_search", {"query": "best AI gadgets 2025", "num_results": 3})
        
        # Test the qna tool
        await call_tool(session, "qna", {"question": "what is artificial intelligence"})
        
    except Exception as e:
        logger.error(f"Error running tools demo: {e}")
        print(f"Error: {e}")

async def main() -> None:
    """Main entry point for the client."""
    # Load environment variables if dotenv module is available
    try:
        load_dotenv()
    except:
        pass
    
    parser = argparse.ArgumentParser(description="Web Search MCP Client")
    parser.add_argument(
        "--interactive", 
        action="store_true",
        help="Run in interactive mode"
    )
    
    args = parser.parse_args()
    
    logger.info("Starting Web Search MCP client")
    
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )
    
    try:
        logger.info("Connecting to server...")
        async with stdio_client(server_params) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                logger.info("Initializing session")
                await session.initialize()
                
                if args.interactive:
                    await run_interactive_demo(session)
                else:
                    await run_all_tools_demo(session)
    
    except KeyboardInterrupt:
        print("\nClient terminated by user.")
    except Exception as e:
        logger.error(f"Error during client execution: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())