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
  const faqResourceUri = "ui://get-faq/mcp-faq.html";
  const infoUri = "ui://app-info";

  registerAppTool(
    server,
    "play-rps",
    {
      title: "Play Rock-Paper-Scissors",
      description: "Play a game of rock-paper-scissors with the server.",
      inputSchema: zod.object({
        choice: zod.enum(["rock", "paper", "scissors"]),
      }),
      _meta: { ui: { resourceUri } }, // Links this tool to its UI resource
    },
    async ({ choice }) => {
      const options = ["rock", "paper", "scissors"] as const;
      const serverChoice = options[Math.floor(Math.random() * options.length)];

      let result: string;
      if (choice === serverChoice) {
        result = `It's a tie! We both chose ${choice}.`;
      } else if (
        (choice === "rock" && serverChoice === "scissors") ||
        (choice === "paper" && serverChoice === "rock") ||
        (choice === "scissors" && serverChoice === "paper")
      ) {
        result = `You win! You chose ${choice} and I chose ${serverChoice}.`;
      } else {
        result = `I win! You chose ${choice} and I chose ${serverChoice}.`;
      }

      return {
        content: [
          { type: "text", text: result },
        ],
      };
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