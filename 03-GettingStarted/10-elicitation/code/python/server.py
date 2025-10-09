from pydantic import BaseModel, Field

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

from starlette.applications import Starlette
from starlette.routing import Mount, Host

mcp = FastMCP(name="Elicitation Example")

# todo: elicitation example, turn it into sse

class BookingPreferences(BaseModel):
    """Schema for collecting user preferences."""

    checkAlternative: bool = Field(description="Would you like to check another date?")
    alternativeDate: str = Field(
        default="2024-12-26",
        description="Alternative date (YYYY-MM-DD)",
    )

def not_available_date(date: str) -> bool:
    # Simulate date availability check
    return date != "2024-12-25"


@mcp.tool()
async def book_trip(date: str, ctx: Context[ServerSession, None]) -> str:
    """Book a trip with date availability check."""
    # Check if date is available
    if not_available_date(date):
        # Date unavailable - ask user for alternative
        result = await ctx.elicit(
            message=(f"No trips available on {date}. Would you like to try another date?"),
            schema=BookingPreferences,
        )

        if result.action == "accept" and result.data:
            if result.data.checkAlternative:
                return f"[SUCCESS] Booked for {result.data.alternativeDate}"
            return "[CANCELLED] No booking made"
        return "[CANCELLED] Booking cancelled"

    # Date available
    return f"[SUCCESS] Booked for {date}"

app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

if __name__ == "__main__":
    print("Starting Elicitation Example MCP Server...")
    mcp.run()