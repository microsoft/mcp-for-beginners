"""Blog post server that uses MCP Sampling.

DEPRECATED FEATURE: Sampling (`sampling/createMessage`) is deprecated in MCP
2026-07-28. This sample is kept for legacy (2025-11-25) clients. New servers
should call an LLM provider API directly; see server_direct_llm.py.

With mcp 2.3.0, `ctx.session.create_message` only works when the client connected
with the 2025-11-25 `initialize` handshake. On a 2026-07-28 connection it raises
`NoBackChannelError`.

Run with: python server.py   (listens on http://localhost:8000/mcp)
"""

import json
from typing import List

from pydantic import BaseModel

from mcp.server.mcpserver import Context, MCPServer
from mcp.types import SamplingMessage, TextContent

mcp = MCPServer("Blog post generator")


class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    abstract: str


posts: List[BlogPost] = []


@mcp.tool()
async def create_blog(title: str, content: str, ctx: Context) -> str:
    """Create a blog post and generate a summary"""

    post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=""
    )

    prompt = f"Create an abstract of the following blog post: title: {title} and draft: {content} "

    # Deprecated: ask the client's LLM to write the abstract (Sampling).
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
    )

    post.abstract = result.content.text

    posts.append(post)

    # return the complete blog post
    return json.dumps({
        "id": post.title,
        "abstract": post.abstract
    })


if __name__ == "__main__":
    print("Starting server on http://localhost:8000/mcp ...")
    mcp.run(transport="streamable-http")
