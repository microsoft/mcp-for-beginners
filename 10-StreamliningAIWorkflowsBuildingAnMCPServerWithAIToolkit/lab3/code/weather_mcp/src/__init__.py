import os
import sys
from server import server

if __name__ == "__main__":
    """Main entry point"""
    transport_type = sys.argv[1] if len(sys.argv) > 1 else None
    server.settings.log_level = os.environ.get("LOG_LEVEL", "DEBUG")
    if transport_type in ("http", "streamable-http"):
        port = int(os.environ.get("PORT", 3001))
        # Streamable HTTP is the current MCP HTTP transport; the endpoint is
        # http://127.0.0.1:<port>/mcp. In mcp 2.x, host and port are passed to run().
        server.run(transport="streamable-http", host="127.0.0.1", port=port)
    elif transport_type == "stdio":
        server.run(transport="stdio")
    else:
        print("Invalid transport type. Use 'http' or 'stdio'.")
        sys.exit(1)
