import { McpServer, type AuthInfo } from "@modelcontextprotocol/server";
import * as z from "zod/v4";

import { classifyRegistration } from "./registration.js";

export function buildServer(
  authInfo: AuthInfo | undefined,
  dcrClientIdPrefix?: string
): McpServer {
  const server = new McpServer({ name: "cimd-dcr-auth-sample", version: "1.0.0" });

  server.registerTool(
    "registration-info",
    {
      title: "Registration information",
      description: "Explain whether the verified OAuth client used CIMD or a configured DCR identifier.",
      annotations: { readOnlyHint: true, openWorldHint: false }
    },
    async () => {
      if (!authInfo) {
        return { content: [{ type: "text", text: "No authenticated caller" }], isError: true };
      }
      const details = classifyRegistration(authInfo.clientId, dcrClientIdPrefix);
      return {
        content: [{ type: "text", text: JSON.stringify(details, null, 2) }],
        structuredContent: details
      };
    }
  );

  server.registerTool(
    "greet",
    {
      title: "Greet caller",
      description: "Greet a name when the caller has the tool:greet scope.",
      inputSchema: z.object({ name: z.string().min(1) }),
      annotations: { readOnlyHint: true, openWorldHint: false }
    },
    async ({ name }) => {
      if (!authInfo?.scopes.includes("tool:greet")) {
        return {
          content: [{ type: "text", text: "insufficient_scope: greet requires tool:greet" }],
          isError: true
        };
      }
      return { content: [{ type: "text", text: `Hello, ${name}.` }] };
    }
  );

  return server;
}