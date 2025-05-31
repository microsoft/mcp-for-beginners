# Web Search MCP Server

This advanced sample demonstrates how to build a sophisticated MCP server and client using FastMCP to extend LLM capabilities with real-time web data via SerpAPI, a critical skill for developing dynamic AI agents.

## Overview

This implementation features four tools that showcase MCP's ability to handle diverse, external API-driven tasks securely and efficiently:

- **general_search**: For broad web results
- **news_search**: For recent headlines
- **product_search**: For e-commerce data
- **qna**: For question-and-answer snippets

## Features

- **External API Integration**: Demonstrates secure handling of API keys and external requests
- **Structured Data Parsing**: Shows how to transform API responses into LLM-friendly formats
- **Error Handling**: Robust error handling with appropriate logging
- **Interactive Client**: Includes both automated tests and an interactive mode for testing
- **Context Management**: Leverages MCP Context for logging and tracking requests

## Prerequisites

- Python 3.8 or higher
- SerpAPI API Key (Sign up at [SerpAPI](https://serpapi.com/) - free tier available)

## Installation

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

### Running the Server

Start the MCP server:

```bash
python server.py
```

The server will run as a stdio-based MCP server that the client can connect to directly.

### Running the Client

Run the automated tests (this will automatically start the server):

```bash
python client.py
```

Or run in interactive mode:

```bash
python client.py --interactive
```

### Testing with Different Methods

#### Using the Interactive Mode
The easiest way to test the tools is using the interactive mode:

```bash
python client.py --interactive
```

This provides a menu-driven interface to try each tool with custom queries.

#### Using the MCP Python SDK
You can also build your own test scripts using the MCP Python SDK:

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

## Tool Descriptions

### general_search

Performs a general web search and returns formatted results.

**Parameters:**
- `query` (string): The search query
- `num_results` (integer, optional): Number of results to return (default: 5)

**Example Request:**
```json
{
  "query": "latest AI trends"
}
```

### news_search

Searches for recent news articles related to a query.

**Parameters:**
- `query` (string): The search query
- `num_results` (integer, optional): Number of news articles to return (default: 5)

**Example Request:**
```json
{
  "query": "AI policy updates"
}
```

### product_search

Searches for products matching a query.

**Parameters:**
- `query` (string): The product search query
- `num_results` (integer, optional): Number of product results to return (default: 5)

**Example Request:**
```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Gets direct answers to questions from search engines.

**Parameters:**
- `question` (string): The question to find an answer for

**Example Request:**
```json
{
  "question": "what is artificial intelligence"
}
```

## Advanced Concepts Demonstrated

1. **Multi-tool Orchestration**: Managing multiple tools with distinct purposes within a single server
2. **API Rate Limit Handling**: Built-in timeout handling for external API calls
3. **Structured Data Parsing**: Converting complex API responses into formatted, LLM-friendly text
4. **Error Recovery**: Graceful degradation when API calls fail
5. **Parameter Validation**: Proper handling of optional parameters with defaults

## Troubleshooting

### Common Issues

1. **Missing SERPAPI_KEY in .env file**
   - Error: `SERPAPI_KEY environment variable not found`
   - Solution: Create or edit the `.env` file in the project root directory and add your SerpAPI key

2. **Module not found errors**
   - Error: `ModuleNotFoundError: No module named 'httpx'` (or similar)
   - Solution: Ensure you've installed all dependencies using `pip install -r requirements.txt`

3. **Connection issues**
   - Error: `Error during client execution`
   - Solution: Make sure the client and server are compatible versions and that server.py exists in the same directory

4. **SerpAPI errors**
   - Error: `Search API returned error status: 401`
   - Solution: Verify your SerpAPI key is correct and not expired

### Debug Mode

To enable more verbose logging, set the logging level to DEBUG:

```python
# At the top of your client.py or server.py
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

## Why in 05-AdvancedTopics?

This sample is placed in the 05-AdvancedTopics directory because it demonstrates complex integrations and advanced concepts:

- Integration with external APIs requiring authentication
- Handling diverse data types from multiple endpoints
- Robust error handling and logging strategies
- Multi-tool orchestration in a production-ready format

The implementation provides a sophisticated example that builds upon the fundamentals covered in earlier chapters while introducing patterns useful for real-world applications.
