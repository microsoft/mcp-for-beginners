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


  const faq: { [key: string]: string } = {
    "shipping": "Our standard shipping time is 3-5 business days.",
    "return policy": "You can return any item within 30 days of purchase.",
    "warranty": "All products come with a 1-year warranty covering manufacturing defects.",
  }

  server.registerTool("ping", {}, async () => {
    return {
      content: [
        { type: "text", text: "pong" },
      ],
    };
  });

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

  registerAppTool(
    server,
    "get-app-info",
    {
      title: "Get App Info",
      description: "Returns basic information about the app.",
      inputSchema: zod.object({}),
      _meta: { ui: { resourceUri: infoUri } }, // Links this tool to its UI resource  
    },
    async () => {
      return {
        content: [
          { type: "text", text: "This is a sample MCP app demonstrating tools and resources." },
        ],
      };
    },
  );

  registerAppTool(
    server,
    "get-faq",
    {
      title: "Search FAQ",
      description: "Searches the FAQ for relevant answers.",
      inputSchema: zod.object({
        query: zod.string().default("shipping"),
      }),
      _meta: { ui: { resourceUri: faqResourceUri } }, // Links this tool to its UI resource
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

  registerAppResource(
    server,
    faqResourceUri,
    faqResourceUri,
    { mimeType: RESOURCE_MIME_TYPE },
    async () => {
      const html = await fs.readFile(path.join(DIST_DIR, "mcp-app.html"), "utf-8");

      return {
        contents: [
          {
            uri: faqResourceUri,
            mimeType: RESOURCE_MIME_TYPE,
            text: html,
            _meta: {
              ui: {},
            },
          },
        ],
      };
    }
  );

  const simpleClickUri = "ui://simple-click";
  registerAppTool(
    server,
    "simple-click",
    {
      title: "Simple Click Tool",
      description: "A simple tool that demonstrates UI interaction.",
      inputSchema: zod.object({}),
      _meta: { ui: { resourceUri: simpleClickUri } },
    },
    async () => {
      return {
        content: [
          { type: "text", text: "You clicked the button!" },
        ],
      };
    },
  );

  registerAppResource(
    server,
    simpleClickUri,
    simpleClickUri,
    { mimeType: RESOURCE_MIME_TYPE },
    async () => {
      return {
        contents: [
          {
            uri: simpleClickUri,
            mimeType: RESOURCE_MIME_TYPE,
            text: `
              <html>
                <body>
                  <div id="result">Click the button to test UI interaction.</div>
                 
                  <button id="click-btn">Click me!</button>
                  <script type="module">
                    const btn = document.getElementById("click-btn");
                    const elResult = document.getElementById("result");

                    window.addEventListener("message", (event) => {
                      debugger;
                      const { method } = event.data || {};
                      if (method === "ping") {
                        elResult.textContent = "Received ping from host!";
                      }
                    }); 

                    btn.addEventListener("click", async () => {
                      elResult.textContent = "You CLICKED the button!";
                      window.parent.postMessage({
                        id: Math.random().toString(16).slice(2),
                        jsonrpc: "2.0",
                        method: "ping",
                        params: {},
                      }, "*");
                      });
                  </script>
                </body>
              </html>
            `,
            _meta: {
              ui: {},
            },
          },
        ],
      };
    }
  );


  registerAppResource(
    server,
    infoUri,
    infoUri,
    { mimeType: RESOURCE_MIME_TYPE },
    async () => {
      return {
        contents: [
          {
            uri: infoUri,
            mimeType: RESOURCE_MIME_TYPE,
            text: "This is a sample MCP app demonstrating tools and resources.",
            _meta: {
              ui: {},
            },
          },
        ],
      };
    }
  );

  return server;
}