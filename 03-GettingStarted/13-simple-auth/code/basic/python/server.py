from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp.server import FastMCP
from typing import Any, Literal
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette.applications import Starlette
from starlette.routing import Mount

import asyncio
import datetime

settings = {
    "host": "localhost",
    "port": 8000,
    "auth_server_url": AnyHttpUrl("http://localhost:8001"),
    "mcp_scope": "mcp:read",
    "server_url": AnyHttpUrl("http://localhost:8000"),
}

def valid_token(token: str) -> bool:
    # remove the "Bearer " prefix
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        has_header = request.headers.get("Authorization")
        if not has_header:
            print("-> Missing Authorization header!")
            return Response(status_code=401, content="Unauthorized")

        if not valid_token(has_header):
            print("-> Invalid token!")
            return Response(status_code=403, content="Forbidden")

        print("Valid token, proceeding...")
        print(f"-> Received {request.method} {request.url}")
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

@app.tool()
async def get_time() -> dict[str, Any]:
    """
    Get the current server time.

    This tool demonstrates that system information can be protected
    by OAuth authentication. User must be authenticated to access it.
    """

    now = datetime.datetime.now()

    return {
        "current_time": now.isoformat(),
        "timezone": "UTC",  # Simplified for demo
        "timestamp": now.timestamp(),
        "formatted": now.strftime("%Y-%m-%d %H:%M:%S"),
    }

async def setup(app) -> None:
    """Run the server using StreamableHTTP transport."""

    starlette_app = app.streamable_http_app()
    return starlette_app

async def run(starlette_app):
    import uvicorn
    config = uvicorn.Config(
            starlette_app,
            host=app.settings.host,
            port=app.settings.port,
            log_level=app.settings.log_level.lower(),
        )
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    print("Running MCP Resource Server...")
    starlette_app = await setup(app)
    print("Adding custom middleware...")
    starlette_app.add_middleware(CustomHeaderMiddleware)

    await run(starlette_app)

if __name__ == "__main__":
    asyncio.run(main())

