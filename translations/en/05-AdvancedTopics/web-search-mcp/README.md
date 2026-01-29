# Lesson: Building a Web Search MCP Server

This chapter shows you how to build a real-world AI agent that integrates with external APIs, handles various data types, manages errors, and coordinates multiple tools—all in a production-ready setup. You'll learn about:

- **Integrating external APIs that require authentication**
- **Handling diverse data from multiple endpoints**
- **Robust error handling and logging techniques**
- **Orchestrating multiple tools within a single server**

By the end, you'll gain hands-on experience with patterns and best practices essential for advanced AI and LLM-powered applications.

## Introduction

In this lesson, you'll learn how to build an advanced MCP server and client that enhance LLM capabilities with real-time web data using SerpAPI. This skill is crucial for creating dynamic AI agents that can access up-to-date information from the web.

## Learning Objectives

By the end of this lesson, you will be able to:

- Securely integrate external APIs (like SerpAPI) into an MCP server
- Implement multiple tools for web, news, product search, and Q&A
- Parse and format structured data for LLM consumption
- Effectively handle errors and manage API rate limits
- Build and test both automated and interactive MCP clients

## Web Search MCP Server

This section introduces the architecture and features of the Web Search MCP Server. You'll see how FastMCP and SerpAPI work together to extend LLM capabilities with real-time web data.

### Overview

This implementation includes four tools that demonstrate MCP's ability to securely and efficiently handle diverse, external API-driven tasks:

- **general_search**: For broad web results
- **news_search**: For recent headlines
- **product_search**: For e-commerce data
- **qna**: For question-and-answer snippets

### Features
- **Code Examples**: Language-specific code blocks for Python (and easily extendable to other languages) using code pivots for clarity

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Before running the client, it’s useful to understand what the server does. The [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) file implements the MCP server, exposing tools for web, news, product search, and Q&A by integrating with SerpAPI. It handles incoming requests, manages API calls, parses responses, and returns structured results to the client.

You can review the full implementation in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Here is a brief example of how the server defines and registers a tool:

### Python Server

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **External API Integration**: Shows secure handling of API keys and external requests
- **Structured Data Parsing**: Demonstrates how to convert API responses into LLM-friendly formats
- **Error Handling**: Robust error handling with proper logging
- **Interactive Client**: Includes both automated tests and an interactive mode for testing
- **Context Management**: Uses MCP Context for logging and tracking requests

## Prerequisites

Before you start, make sure your environment is set up correctly by following these steps. This ensures all dependencies are installed and your API keys are configured properly for smooth development and testing.

- Python 3.8 or higher
- SerpAPI API Key (Sign up at [SerpAPI](https://serpapi.com/) - free tier available)

## Installation

To get started, follow these steps to set up your environment:

1. Install dependencies using uv (recommended) or pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with your SerpAPI key:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Usage

The Web Search MCP Server is the core component that exposes tools for web, news, product search, and Q&A by integrating with SerpAPI. It handles incoming requests, manages API calls, parses responses, and returns structured results to the client.

You can review the full implementation in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Running the Server

To start the MCP server, use the following command:

```bash
python server.py
```

The server will run as a stdio-based MCP server that the client can connect to directly.

### Client Modes

The client (`client.py`) supports two modes for interacting with the MCP server:

- **Normal mode**: Runs automated tests that exercise all the tools and verify their responses. This is useful for quickly checking that the server and tools are working as expected.
- **Interactive mode**: Starts a menu-driven interface where you can manually select and call tools, enter custom queries, and see results in real time. This is ideal for exploring the server's capabilities and experimenting with different inputs.

You can review the full implementation in [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Running the Client

To run the automated tests (this will automatically start the server):

```bash
python client.py
```

Or run in interactive mode:

```bash
python client.py --interactive
```

### Testing with Different Methods

There are several ways to test and interact with the tools provided by the server, depending on your needs and workflow.

#### Writing Custom Test Scripts with the MCP Python SDK
You can also build your own test scripts using the MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

In this context, a "test script" means a custom Python program you write to act as a client for the MCP server. Instead of a formal unit test, this script lets you programmatically connect to the server, call any of its tools with parameters you choose, and inspect the results. This approach is useful for:
- Prototyping and experimenting with tool calls
- Validating how the server responds to different inputs
- Automating repeated tool invocations
- Building your own workflows or integrations on top of the MCP server

You can use test scripts to quickly try out new queries, debug tool behavior, or even as a starting point for more advanced automation. Below is an example of how to use the MCP Python SDK to create such a script:

## Tool Descriptions

You can use the following tools provided by the server to perform different types of searches and queries. Each tool is described below with its parameters and example usage.

This section provides details about each available tool and their parameters.

### general_search

Performs a general web search and returns formatted results.

**How to call this tool:**

You can call `general_search` from your own script using the MCP Python SDK, or interactively using the Inspector or the interactive client mode. Here is a code example using the SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Alternatively, in interactive mode, select `general_search` from the menu and enter your query when prompted.

**Parameters:**
- `query` (string): The search query

**Example Request:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Searches for recent news articles related to a query.

**How to call this tool:**

You can call `news_search` from your own script using the MCP Python SDK, or interactively using the Inspector or the interactive client mode. Here is a code example using the SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Alternatively, in interactive mode, select `news_search` from the menu and enter your query when prompted.

**Parameters:**
- `query` (string): The search query

**Example Request:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Searches for products matching a query.

**How to call this tool:**

You can call `product_search` from your own script using the MCP Python SDK, or interactively using the Inspector or the interactive client mode. Here is a code example using the SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Alternatively, in interactive mode, select `product_search` from the menu and enter your query when prompted.

**Parameters:**
- `query` (string): The product search query

**Example Request:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Gets direct answers to questions from search engines.

**How to call this tool:**

You can call `qna` from your own script using the MCP Python SDK, or interactively using the Inspector or the interactive client mode. Here is a code example using the SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Alternatively, in interactive mode, select `qna` from the menu and enter your question when prompted.

**Parameters:**
- `question` (string): The question to find an answer for

**Example Request:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Code Details

This section provides code snippets and references for the server and client implementations.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

See [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) and [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) for full implementation details.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Advanced Concepts in This Lesson

Before you start building, here are some important advanced concepts that will appear throughout this chapter. Understanding these will help you follow along, even if you're new to them:

- **Multi-tool Orchestration**: Running several different tools (like web search, news search, product search, and Q&A) within a single MCP server. This lets your server handle a variety of tasks, not just one.
- **API Rate Limit Handling**: Many external APIs (like SerpAPI) limit how many requests you can make in a certain time. Good code checks for these limits and handles them gracefully, so your app doesn’t break if you hit a limit.
- **Structured Data Parsing**: API responses are often complex and nested. This means converting those responses into clean, easy-to-use formats that are friendly for LLMs or other programs.
- **Error Recovery**: Sometimes things go wrong—maybe the network fails, or the API doesn’t return what you expect. Error recovery means your code can handle these problems and still provide useful feedback instead of crashing.
- **Parameter Validation**: Checking that all inputs to your tools are correct and safe to use. This includes setting default values and ensuring the types are right, which helps prevent bugs and confusion.

This section will help you diagnose and fix common issues you might encounter while working with the Web Search MCP Server. If you run into errors or unexpected behavior, this troubleshooting section offers solutions to the most frequent problems. Review these tips before seeking further help—they often resolve issues quickly.

## Troubleshooting

When working with the Web Search MCP Server, you may occasionally run into issues—this is normal when developing with external APIs and new tools. This section provides practical solutions to the most common problems, so you can get back on track quickly. If you encounter an error, start here: the tips below address the issues most users face and can often fix your problem without extra help.

### Common Issues

Below are some of the most frequent problems users encounter, along with clear explanations and steps to resolve them:

1. **Missing SERPAPI_KEY in .env file**
   - If you see the error `SERPAPI_KEY environment variable not found`, it means your application can’t find the API key needed to access SerpAPI. To fix this, create a file named `.env` in your project root (if it doesn’t already exist) and add a line like `SERPAPI_KEY=your_serpapi_key_here`. Be sure to replace `your_serpapi_key_here` with your actual key from the SerpAPI website.

2. **Module not found errors**
   - Errors such as `ModuleNotFoundError: No module named 'httpx'` indicate that a required Python package is missing. This usually happens if you haven’t installed all dependencies. To fix this, run `pip install -r requirements.txt` in your terminal to install everything your project needs.

3. **Connection issues**
   - If you get an error like `Error during client execution`, it often means the client can’t connect to the server, or the server isn’t running as expected. Double-check that both the client and server are compatible versions, and that `server.py` is present and running in the correct directory. Restarting both the server and client can also help.

4. **SerpAPI errors**
   - Seeing `Search API returned error status: 401` means your SerpAPI key is missing, incorrect, or expired. Go to your SerpAPI dashboard, verify your key, and update your `.env` file if needed. If your key is correct but you still see this error, check if your free tier quota has been used up.

### Debug Mode

By default, the app logs only important information. If you want to see more details about what’s happening (for example, to diagnose tricky issues), you can enable DEBUG mode. This will show you much more about each step the app takes.

**Example: Normal Output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Example: DEBUG Output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Notice how DEBUG mode includes extra lines about HTTP requests, responses, and other internal details. This can be very helpful for troubleshooting.
To enable DEBUG mode, set the logging level to DEBUG at the top of your `client.py` or `server.py`:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## What's next 

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.