from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp.server import FastMCP
from typing import Any, Literal

from token_verifier import IntrospectionTokenVerifier

settings = {
    "host": "localhost",
    "port": 8000,
    "auth_server_url": AnyHttpUrl("http://localhost:8001"),
    "mcp_scope": "mcp:read",
    "server_url": AnyHttpUrl("http://localhost:8000"),
}

token_verifier = IntrospectionTokenVerifier(
    introspection_endpoint=f"{settings['auth_server_url']}/introspect",
    server_url=settings["server_url"],
    validate_resource=True,
)

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True,
        # Auth configuration for RS mode
    token_verifier=token_verifier,
    auth=AuthSettings(
        issuer_url=settings["auth_server_url"],
        required_scopes=[settings["mcp_scope"]],
        resource_server_url=settings["server_url"],
    ),
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

def main():
    app.run(transport="streamable-http")

if __name__ == "__main__":
    main()