"""Blog post server that calls the LLM provider directly (recommended pattern).

This is the replacement for Sampling recommended by MCP 2026-07-28: the server
owns its LLM integration instead of asking the client's LLM through
`sampling/createMessage`. It works with every client and every protocol version,
because the server never sends a request back to the client.

Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY (optionally
AZURE_OPENAI_DEPLOYMENT), then run: python server_direct_llm.py
(listens on http://localhost:8000/mcp)
"""

import json
import os
from typing import List

from openai import AsyncOpenAI
from pydantic import BaseModel

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Blog post generator (direct LLM)")


class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    abstract: str


posts: List[BlogPost] = []


async def generate_abstract(title: str, content: str) -> str:
    """Ask the LLM provider for a short abstract of a blog post."""
    llm = AsyncOpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    response = await llm.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
        messages=[
            {"role": "system", "content": "You write short, accurate blog post abstracts."},
            {"role": "user", "content": f"Create an abstract of this blog post. Title: {title}. Draft: {content}"},
        ],
        max_completion_tokens=100,
    )
    return response.choices[0].message.content


@mcp.tool()
async def create_blog(title: str, content: str) -> str:
    """Create a blog post and generate a summary"""
    post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=await generate_abstract(title, content),
    )
    posts.append(post)

    return json.dumps({"id": post.id, "title": post.title, "abstract": post.abstract})


if __name__ == "__main__":
    print("Starting server on http://localhost:8000/mcp ...")
    mcp.run(transport="streamable-http")
