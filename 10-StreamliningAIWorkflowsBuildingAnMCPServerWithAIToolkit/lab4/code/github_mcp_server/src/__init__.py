import os
import sys
from server import server

if __name__ == "__main__":
    """Main entry point"""
    transport_type = sys.argv[1] if len(sys.argv) > 1 else None
    server.settings.log_level = os.environ.get("LOG_LEVEL", "DEBUG")
    if transport_type == "sse":
        port = int(os.environ.get("PORT", 3001))
        # In mcp 2.x, host and port are passed to run() instead of settings
        server.run(transport="sse", host="127.0.0.1", port=port)
    elif transport_type == "stdio":
        server.run(transport="stdio")
    else:
        print("Invalid transport type. Use 'sse' or 'stdio'.")
        sys.exit(1)