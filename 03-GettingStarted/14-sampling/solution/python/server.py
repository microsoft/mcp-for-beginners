"""Product description server that uses MCP Sampling.

DEPRECATED FEATURE: Sampling (`sampling/createMessage`) is deprecated in MCP
2026-07-28. This sample is kept for legacy (2025-11-25) clients. New servers
should call an LLM provider API directly; see ../../code/python/server_direct_llm.py.

With mcp 2.3.0, `ctx.session.create_message` only works when the client connected
with the 2025-11-25 `initialize` handshake (as client.py does). On a 2026-07-28
connection it raises `NoBackChannelError`.

Run with: python server.py   (listens on http://localhost:8000/mcp)
"""

import json
from typing import List

from pydantic import BaseModel

from mcp.server.mcpserver import Context, MCPServer
from mcp.types import SamplingMessage, TextContent

mcp = MCPServer("Product description generator")


class Product(BaseModel):
    id: int
    name: str
    description: str

    def __init__(self, name: str, description: str):
        super().__init__(
            id=len(products) + 1,
            name=name,
            description=description
        )


products: List[Product] = []


@mcp.tool()
async def create_product(product_name: str, keywords: str, ctx: Context) -> str:
    """Create a product and generate a product description using LLM sampling."""

    product = Product(name=product_name, description="")

    prompt = f"Create a product description about {product_name} described by as {keywords}"

    # Deprecated: ask the client's LLM to write the description (Sampling).
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
    )

    product.description = result.content.text

    products.append(product)

    # return the complete product
    return json.dumps({
        "id": product.id,
        "name": product.name,
        "description": product.description
    })


@mcp.tool()
def get_products() -> str:
    """List all products created so far."""
    return json.dumps([product.model_dump() for product in products])


if __name__ == "__main__":
    print("Starting server on http://localhost:8000/mcp ...")
    mcp.run(transport="streamable-http")
