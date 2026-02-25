import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
/**
 * Starts an MCP server with Streamable HTTP transport in stateless mode.
 *
 * @param createServer - Factory function that creates a new McpServer instance per request.
 */
export declare function startStreamableHTTPServer(createServer: () => McpServer): Promise<void>;
/**
 * Starts an MCP server with stdio transport.
 *
 * @param createServer - Factory function that creates a new McpServer instance.
 */
export declare function startStdioServer(createServer: () => McpServer): Promise<void>;
