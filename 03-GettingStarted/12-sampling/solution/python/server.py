from starlette.applications import Starlette
from starlette.routing import Mount, Host

from mcp.server.fastmcp import Context, FastMCP

from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

import json


from uuid import uuid4
from typing import List
from pydantic import BaseModel


mcp = FastMCP("My App")

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
async def create_product(product_name: str, keywords: str, ctx: Context[ServerSession, None]) -> str:
    """Create a product and generate a product description using LLM sampling."""

    product = Product(name=product_name, description="")

    prompt = f"Create a product description about {product_name} described by as {keywords}"

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

if __name__ == "__main__":
    print("Starting server...")
    mcp.run()


# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

# run app with: uvicorn 03-GettingStarted/12-sampling/solution/python/server:app --port 8000