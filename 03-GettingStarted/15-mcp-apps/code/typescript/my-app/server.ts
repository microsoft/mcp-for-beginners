import {
  registerAppResource,
  registerAppTool,
  RESOURCE_MIME_TYPE,
} from "@modelcontextprotocol/ext-apps/server";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import fs from "node:fs/promises";
import path from "node:path";
import zod from "zod";

const DIST_DIR = path.join(import.meta.dirname, "dist");



/**
 * Creates a new MCP server instance with tools and resources registered.
 */
export function createServer(): McpServer {
  const server = new McpServer({
    name: "Quickstart MCP App Server",
    version: "1.0.0",
  });

  // Two-part registration: tool + resource, tied together by the resource URI.
  const resourceUri = "ui://get-time/mcp-app.html";

  const faq: { [key: string]: string } = {
    "shipping": "Our standard shipping time is 3-5 business days.",
    "return policy": "You can return any item within 30 days of purchase.",
    "warranty": "All products come with a 1-year warranty covering manufacturing defects.",
  }

  registerAppTool(
    server,
    "faq-search",
    {
      title: "Search FAQ",
      description: "Searches the FAQ for relevant answers.",
      inputSchema: zod.object({
        query: zod.string().default("shipping"),
      }),
      _meta: { ui: { resourceUri } }, // Links this tool to its UI resource
    },
    async ({ query }) => {
      const answer: string = faq[query.toLowerCase()] || "Sorry, I don't have an answer for that.";
      return { content: [{ type: "text", text: answer }] };
    },
  );


  // Register a tool with UI metadata. When the host calls this tool, it reads
  // `_meta.ui.resourceUri` to know which resource to fetch and render as an
  // interactive UI.
  registerAppTool(
    server,
    "get-time",
    {
      title: "Get Time",
      description: "Returns the current server time.",
      inputSchema: zod.object({}),
      _meta: { ui: { resourceUri } }, // Links this tool to its UI resource
    },
    async () => {
      const time: string = new Date().toISOString();
      return { content: [{ type: "text", text: time }] };
    },
  );

  // Register the resource, which returns the bundled HTML/JavaScript for the UI.
  registerAppResource(
    server,
    resourceUri,
    resourceUri,
    { mimeType: RESOURCE_MIME_TYPE },
    async () => {
      const html = await fs.readFile(path.join(DIST_DIR, "mcp-app.html"), "utf-8");

      return {
        contents: [
          {
            uri: resourceUri,
            mimeType: RESOURCE_MIME_TYPE,
            text: html,
            _meta: {
              ui: {},
            },
          },
        ],
      };
    },
  );

  return server;
}