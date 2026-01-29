# Lesson: How to Build Web Search MCP Server

Dis chapter go show you how to build real-life AI agent wey fit connect with external APIs, handle different kain data, manage errors, and use plenty tools together—all for production-ready format. You go see:

- **How to connect with external APIs wey need authentication**
- **How to handle different kain data from multiple endpoints**
- **Strong error handling and logging methods**
- **How to use many tools for one server**

By di end, you go sabi di patterns and best practices wey dey important for advanced AI and LLM-powered apps.

## Introduction

For dis lesson, you go learn how to build advanced MCP server and client wey go extend LLM power with real-time web data using SerpAPI. Dis skill dey very important if you wan develop dynamic AI agents wey fit access up-to-date info from di web.

## Learning Objectives

By di end of dis lesson, you go fit:

- Connect external APIs (like SerpAPI) securely into MCP server
- Use multiple tools for web, news, product search, and Q&A
- Parse and format structured data wey LLM go fit use
- Handle errors and manage API rate limits well
- Build and test both automated and interactive MCP clients

## Web Search MCP Server

Dis section go show you di architecture and features of di Web Search MCP Server. You go see how FastMCP and SerpAPI dey work together to extend LLM power with real-time web data.

### Overview

Dis implementation get four tools wey dey show MCP power to handle different kain external API tasks securely and well:

- **general_search**: For general web results
- **news_search**: For recent news headlines
- **product_search**: For e-commerce data
- **qna**: For question-and-answer snippets

### Features
- **Code Examples**: E get language-specific code blocks for Python (and e fit extend to other languages) using code pivots for clarity

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

Before you run di client, e go make sense to understand wetin di server dey do. Di [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) file dey implement di MCP server, wey dey expose tools for web, news, product search, and Q&A by connecting with SerpAPI. E dey handle incoming requests, manage API calls, parse responses, and return structured results to di client.

You fit check di full implementation for [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Here be small example of how di server dey define and register tool:

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

- **External API Integration**: E dey show how to handle API keys and external requests securely
- **Structured Data Parsing**: E dey show how to turn API responses into LLM-friendly formats
- **Error Handling**: Strong error handling with correct logging
- **Interactive Client**: E get both automated tests and interactive mode for testing
- **Context Management**: E dey use MCP Context for logging and tracking requests

## Prerequisites

Before you start, make sure say your environment dey set up well by following dis steps. Dis go make sure say all dependencies dey installed and your API keys dey configured well for smooth development and testing.

- Python 3.8 or higher
- SerpAPI API Key (Sign up for [SerpAPI](https://serpapi.com/) - free tier dey available)

## Installation

To start, follow dis steps to set up your environment:

1. Install dependencies using uv (recommended) or pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Create `.env` file for di project root with your SerpAPI key:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Usage

Di Web Search MCP Server na di main component wey dey expose tools for web, news, product search, and Q&A by connecting with SerpAPI. E dey handle incoming requests, manage API calls, parse responses, and return structured results to di client.

You fit check di full implementation for [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Running the Server

To start di MCP server, use dis command:

```bash
python server.py
```

Di server go run as stdio-based MCP server wey di client fit connect to directly.

### Client Modes

Di client (`client.py`) get two modes to interact with di MCP server:

- **Normal mode**: E dey run automated tests wey dey test all di tools and confirm say their responses dey okay. Dis one dey useful to quickly check say di server and tools dey work as dem suppose.
- **Interactive mode**: E dey start menu-driven interface wey you fit use manually select and call tools, enter custom queries, and see results for real time. Dis one dey good to explore di server capabilities and try different inputs.

You fit check di full implementation for [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Running the Client

To run di automated tests (dis go automatically start di server):

```bash
python client.py
```

Or run am for interactive mode:

```bash
python client.py --interactive
```

### Testing with Different Methods

You get different ways to test and interact with di tools wey di server provide, depending on wetin you need and how you wan work.

#### Writing Custom Test Scripts with di MCP Python SDK
You fit also build your own test scripts using di MCP Python SDK:

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

For dis context, "test script" mean custom Python program wey you go write to act as client for di MCP server. Instead of formal unit test, dis script go let you programmatically connect to di server, call any of di tools with parameters wey you choose, and check di results. Dis method dey useful for:
- Prototyping and trying tool calls
- Confirming how di server dey respond to different inputs
- Automating repeated tool calls
- Building your own workflows or integrations on top di MCP server

You fit use test scripts to quickly try new queries, debug tool behavior, or even as starting point for more advanced automation. Below be example of how to use MCP Python SDK to create dis kain script:

## Tool Descriptions

You fit use di tools wey di server provide to do different kain searches and queries. Each tool dey described below with di parameters and example usage.

Dis section go give details about each available tool and their parameters.

### general_search

E dey do general web search and return formatted results.

**How to call dis tool:**

You fit call `general_search` from your own script using MCP Python SDK, or interactively using di Inspector or di interactive client mode. Here be code example using di SDK:

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

Or for interactive mode, select `general_search` from di menu and enter your query when dem ask.

**Parameters:**
- `query` (string): Di search query

**Example Request:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

E dey search for recent news articles wey relate to query.

**How to call dis tool:**

You fit call `news_search` from your own script using MCP Python SDK, or interactively using di Inspector or di interactive client mode. Here be code example using di SDK:

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

Or for interactive mode, select `news_search` from di menu and enter your query when dem ask.

**Parameters:**
- `query` (string): Di search query

**Example Request:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

E dey search for products wey match query.

**How to call dis tool:**

You fit call `product_search` from your own script using MCP Python SDK, or interactively using di Inspector or di interactive client mode. Here be code example using di SDK:

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

Or for interactive mode, select `product_search` from di menu and enter your query when dem ask.

**Parameters:**
- `query` (string): Di product search query

**Example Request:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

E dey get direct answers to questions from search engines.

**How to call dis tool:**

You fit call `qna` from your own script using MCP Python SDK, or interactively using di Inspector or di interactive client mode. Here be code example using di SDK:

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

Or for interactive mode, select `qna` from di menu and enter your question when dem ask.

**Parameters:**
- `question` (string): Di question to find answer for

**Example Request:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Code Details

Dis section go give code snippets and references for di server and client implementations.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Check [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) and [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) for full implementation details.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Advanced Concepts for Dis Lesson

Before you start to build, here be some important advanced concepts wey go show for dis chapter. If you understand dem, e go help you follow along, even if you no sabi dem before:

- **Multi-tool Orchestration**: Dis mean say you fit run plenty different tools (like web search, news search, product search, and Q&A) inside one MCP server. E go make your server fit handle plenty tasks, no be just one.
- **API Rate Limit Handling**: Many external APIs (like SerpAPI) dey limit how many requests you fit make for certain time. Good code go check for dis limits and handle dem well, so your app no go break if you reach di limit.
- **Structured Data Parsing**: API responses dey complex and nested sometimes. Dis concept na about turning di responses into clean, easy-to-use formats wey LLMs or other programs go fit use.
- **Error Recovery**: Sometimes things fit go wrong—maybe network fail, or API no return wetin you expect. Error recovery mean say your code fit handle dis problems and still give useful feedback, instead of crashing.
- **Parameter Validation**: Dis na about checking say all inputs to your tools dey correct and safe to use. E include setting default values and making sure say di types dey correct, wey go help prevent bugs and confusion.

Dis section go help you diagnose and solve common issues wey fit happen when you dey work with di Web Search MCP Server. If you see errors or unexpected behavior, dis troubleshooting section go provide solutions to di most common issues. Check dis tips first before you find extra help—dem fit solve your problem quick.

## Troubleshooting

When you dey work with di Web Search MCP Server, you fit see some issues—dis na normal when you dey develop with external APIs and new tools. Dis section go give practical solutions to di most common problems, so you fit continue your work quick. If you see error, start here: di tips below dey address di issues wey most users dey face and fit solve your problem without extra help.

### Common Issues

Below na some of di most common problems users dey face, with clear explanation and steps to solve dem:

1. **Missing SERPAPI_KEY for .env file**
   - If you see error `SERPAPI_KEY environment variable not found`, e mean say your app no fit find di API key wey e need to access SerpAPI. To fix am, create file wey dem call `.env` for your project root (if e no dey already) and add line like `SERPAPI_KEY=your_serpapi_key_here`. Make sure say you replace `your_serpapi_key_here` with your real key from SerpAPI website.

2. **Module not found errors**
   - Errors like `ModuleNotFoundError: No module named 'httpx'` dey show say one Python package wey you need no dey. Dis dey happen if you never install all di dependencies. To fix am, run `pip install -r requirements.txt` for your terminal to install everything wey your project need.

3. **Connection issues**
   - If you see error like `Error during client execution`, e mean say di client no fit connect to di server, or di server no dey run as e suppose. Check say di client and server dey compatible versions, and say `server.py` dey present and dey run for di correct directory. Restart di server and client fit also help.

4. **SerpAPI errors**
   - If you see `Search API returned error status: 401`, e mean say your SerpAPI key dey miss, no correct, or don expire. Go your SerpAPI dashboard, confirm your key, and update your `.env` file if e need am. If your key dey correct but you still see dis error, check if your free tier don finish.

### Debug Mode

Normally, di app dey log only important info. If you wan see more details about wetin dey happen (for example, to solve hard issues), you fit enable DEBUG mode. Dis one go show you plenty details about each step wey di app dey take.

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

Notice how DEBUG mode dey include extra lines about HTTP requests, responses, and other internal details. Dis one fit help you troubleshoot well.
To make DEBUG mode work, set the logging level to DEBUG for the top of your `client.py` or `server.py`:

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

## Wetin go happen next 

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->