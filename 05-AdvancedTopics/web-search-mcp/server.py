#!/usr/bin/env python3
"""
Web Search MCP Server

This advanced MCP server demonstrates integration with SerpAPI to provide
real-time web data to LLMs through four specialized tools:
- general_search: For broad web search results
- news_search: For recent news articles
- product_search: For e-commerce product information
- qna: For direct question-answer snippets

The server is built using FastMCP and showcases advanced concepts
like external API integration, structured data parsing, and
multi-tool orchestration.
"""

import os
import json
import httpx
import logging
from typing import Dict, Any
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP, Context

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
if not SERPAPI_KEY:
    logger.error("SERPAPI_KEY environment variable not found. Please set it in .env file.")
    raise EnvironmentError("SERPAPI_KEY environment variable is required")

# API configuration
SERPAPI_BASE_URL = "https://serpapi.com/search"
DEFAULT_TIMEOUT = 10.0  # seconds
DEFAULT_RESULTS_LIMIT = 5

# Initialize FastMCP server
mcp = FastMCP("WebSearchServer")

async def make_serpapi_request(ctx: Context, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make a request to SerpAPI with the given parameters.
    
    Args:
        ctx: MCP context object for logging
        params: Dictionary of parameters to send to SerpAPI
        
    Returns:
        Dict containing the API response
        
    Raises:
        Exception: If the API request fails
    """
    # Ensure API key is included
    request_params = {**params, "api_key": SERPAPI_KEY}
    
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            await ctx.info(f"Making SerpAPI request with engine: {params.get('engine', 'google')}")
            response = await client.get(SERPAPI_BASE_URL, params=request_params)
            response.raise_for_status()
            data = response.json()
            await ctx.info("SerpAPI request successful")
            return data
    except httpx.TimeoutException:
        await ctx.error("SerpAPI request timed out")
        raise Exception("Search request timed out. Please try again.")
    except httpx.RequestError as e:
        await ctx.error(f"SerpAPI request error: {e}")
        raise Exception(f"Failed to fetch data from search API: {e}")
    except httpx.HTTPStatusError as e:
        await ctx.error(f"SerpAPI HTTP error: {e.response.status_code} - {e.response.text}")
        raise Exception(f"Search API returned error status: {e.response.status_code}")
    except json.JSONDecodeError:
        await ctx.error("Failed to parse SerpAPI response as JSON")
        raise Exception("Failed to parse search results")

# Tool for general web search
@mcp.tool()
async def general_search(query: str, num_results: int = DEFAULT_RESULTS_LIMIT, ctx: Context = None) -> str:
    """
    Perform a general web search and return formatted results.
    
    Args:
        query: The search query
        num_results: Number of results to return (default: 5)
        ctx: MCP context object
        
    Returns:
        Formatted search results as a string
    """
    await ctx.info(f"Performing general search for: {query}")
    
    try:
        # Prepare parameters for SerpAPI
        params = {
            "q": query,
            "num": num_results,
            "engine": "google",
        }
        
        # Make the API request
        response_data = await make_serpapi_request(ctx, params)
        
        # Extract organic results
        organic_results = response_data.get("organic_results", [])
        if not organic_results:
            await ctx.info("No general search results found")
            return "No search results found."
        
        # Format results for return
        formatted_results = []
        for i, result in enumerate(organic_results[:num_results]):
            formatted_results.append(
                f"## {i+1}. {result.get('title', 'No title')}\n"
                f"**Link**: {result.get('link', 'No link')}\n"
                f"**Snippet**: {result.get('snippet', 'No description')}\n"
            )
        
        await ctx.info(f"Returning {len(formatted_results)} general search results")
        return "\n\n".join(formatted_results)
    except Exception as e:
        await ctx.error(f"General search failed: {str(e)}")
        return f"Error: Unable to fetch results. {str(e)}"

# Tool for news search
@mcp.tool()
async def news_search(query: str, num_results: int = DEFAULT_RESULTS_LIMIT, ctx: Context = None) -> str:
    """
    Search for recent news articles related to a query.
    
    Args:
        query: The search query
        num_results: Number of news articles to return (default: 5)
        ctx: MCP context object
        
    Returns:
        Formatted news search results as a string
    """
    await ctx.info(f"Performing news search for: {query}")
    
    try:
        # Prepare parameters for SerpAPI
        params = {
            "q": query,
            "num": num_results,
            "engine": "google_news",
        }
        
        # Make the API request
        response_data = await make_serpapi_request(ctx, params)
        
        # Extract news results
        news_results = response_data.get("news_results", [])
        if not news_results:
            await ctx.info("No news articles found")
            return "No news articles found."
        
        # Format results for return
        formatted_results = []
        for i, result in enumerate(news_results[:num_results]):
            formatted_results.append(
                f"## {i+1}. {result.get('title', 'No title')}\n"
                f"**Source**: {result.get('source', 'Unknown source')} | "
                f"**Date**: {result.get('date', 'Unknown date')}\n"
                f"**Link**: {result.get('link', 'No link')}\n"
                f"**Snippet**: {result.get('snippet', 'No description')}\n"
            )
        
        await ctx.info(f"Returning {len(formatted_results)} news results")
        return "\n\n".join(formatted_results)
    except Exception as e:
        await ctx.error(f"News search failed: {str(e)}")
        return f"Error: Unable to fetch news. {str(e)}"

# Tool for product search
@mcp.tool()
async def product_search(query: str, num_results: int = DEFAULT_RESULTS_LIMIT, ctx: Context = None) -> str:
    """
    Search for products matching a query.
    
    Args:
        query: The product search query
        num_results: Number of product results to return (default: 5)
        ctx: MCP context object
        
    Returns:
        Formatted product search results as a string
    """
    await ctx.info(f"Performing product search for: {query}")
    
    try:
        # Prepare parameters for SerpAPI
        params = {
            "q": query,
            "engine": "google_shopping",
            "shopping_intent": "high",
            "num": num_results
        }
        
        # Make the API request
        response_data = await make_serpapi_request(ctx, params)
        
        # Extract shopping results
        shopping_results = response_data.get("shopping_results", [])
        if not shopping_results:
            await ctx.info("No product results found")
            return "No product results found."
        
        # Format results for return
        formatted_results = []
        for i, result in enumerate(shopping_results[:num_results]):
            formatted_results.append(
                f"## {i+1}. {result.get('title', 'No title')}\n"
                f"**Price**: {result.get('price', 'Unknown price')}\n"
                f"**Rating**: {result.get('rating', 'No rating')} "
                f"({result.get('reviews', 'No')} reviews)\n"
                f"**Source**: {result.get('source', 'Unknown source')}\n"
                f"**Link**: {result.get('link', 'No link')}\n"
            )
        
        await ctx.info(f"Returning {len(formatted_results)} product results")
        return "\n\n".join(formatted_results)
    except Exception as e:
        await ctx.error(f"Product search failed: {str(e)}")
        return f"Error: Unable to fetch products. {str(e)}"

# Tool for Q&A search
@mcp.tool()
async def qna(question: str, ctx: Context = None) -> str:
    """
    Get direct answers to questions from search engines.
    
    Args:
        question: The question to find an answer for
        ctx: MCP context object
        
    Returns:
        Answer snippet as a string
    """
    await ctx.info(f"Searching for answer to: {question}")
    
    try:
        # Prepare parameters for SerpAPI
        params = {
            "q": question,
            "engine": "google",
        }
        
        # Make the API request
        response_data = await make_serpapi_request(ctx, params)
        
        # Try to extract answer box first (direct answer)
        answer_box = response_data.get("answer_box", {})
        if answer_box:
            await ctx.info("Found answer in answer box")
            if "answer" in answer_box:
                return f"**Answer**: {answer_box['answer']}"
            elif "snippet" in answer_box:
                return f"**Answer**: {answer_box['snippet']}"
            elif "snippet_highlighted_words" in answer_box:
                return f"**Answer**: {' '.join(answer_box['snippet_highlighted_words'])}"
        
        # Try knowledge graph if no answer box
        knowledge_graph = response_data.get("knowledge_graph", {})
        if knowledge_graph and "description" in knowledge_graph:
            await ctx.info("Found answer in knowledge graph")
            return f"**Answer**: {knowledge_graph['description']}"
        
        # Try featured snippet
        if "featured_snippet" in response_data:
            await ctx.info("Found answer in featured snippet")
            snippet = response_data["featured_snippet"]
            if "snippet" in snippet:
                return f"**Answer**: {snippet['snippet']}"
        
        # Try related questions
        related_questions = response_data.get("related_questions", [])
        if related_questions:
            await ctx.info("Found answer in related questions")
            formatted = []
            for i, question in enumerate(related_questions[:3]):
                formatted.append(
                    f"**Question**: {question.get('question', 'Unknown question')}\n"
                    f"**Answer**: {question.get('snippet', 'No answer available')}\n"
                    f"**Source**: {question.get('source', {}).get('link', 'No source')}"
                )
            return "\n\n".join(formatted)
        
        # Fallback to first organic result snippet
        organic_results = response_data.get("organic_results", [])
        if organic_results and "snippet" in organic_results[0]:
            await ctx.info("No direct answer found, using first organic result")
            return f"**Possible answer**: {organic_results[0]['snippet']}"
        
        await ctx.info("No answer found")
        return "No direct answer found for your question."
    except Exception as e:
        await ctx.error(f"Q&A search failed: {str(e)}")
        return f"Error: Unable to find an answer. {str(e)}"
        
@mcp.resource("readme://")
async def get_readme() -> str:
    """Get README information for the Web Search MCP Server"""
    return """
    # Web Search MCP Server
    
    This MCP server provides tools for integrating web search capabilities into LLMs using SerpAPI.
    
    ## Available Tools:
    
    1. `general_search(query, num_results=5)` - Perform a general web search
    2. `news_search(query, num_results=5)` - Search for recent news articles
    3. `product_search(query, num_results=5)` - Search for products
    4. `qna(question)` - Get direct answers to questions
    
    ## Usage:
    
    Call these tools from an MCP client to retrieve real-time web data.
    """

if __name__ == "__main__":
    mcp.run()