import assert from "node:assert/strict";
import { test } from "node:test";

import { Client, StreamableHTTPClientTransport } from "@modelcontextprotocol/client";
import { createMcpHandler, type AuthInfo } from "@modelcontextprotocol/server";

import { mcpRoutePath, parsePort } from "../src/config.js";
import { buildServer } from "../src/mcp.js";

test("parses only a complete integer port", () => {
  assert.equal(parsePort("3001"), 3001);
  assert.throws(() => parsePort("3001abc"), /PORT must be an integer/);
  assert.throws(() => parsePort("3001.5"), /PORT must be an integer/);
});

test("uses the configured MCP server pathname", () => {
  assert.equal(mcpRoutePath(new URL("https://server.example.com/api/mcp")), "/api/mcp");
});

test("serves registration information over MCP 2026-07-28", async () => {
  const authInfo: AuthInfo = {
    token: "verified-in-test",
    clientId: "https://client.example.com/oauth/metadata.json",
    scopes: ["tool:greet"],
    expiresAt: Math.floor(Date.now() / 1000) + 300
  };
  const handler = createMcpHandler(({ authInfo: requestAuth }) =>
    buildServer(requestAuth)
  );
  const transport = new StreamableHTTPClientTransport(new URL("http://test.local/mcp"), {
    fetch: (url, init) => handler.fetch(new Request(url, init), { authInfo })
  });
  const client = new Client(
    { name: "course-test-client", version: "1.0.0" },
    { versionNegotiation: { mode: "auto" } }
  );

  try {
    await client.connect(transport);
    const result = await client.callTool({ name: "registration-info", arguments: {} });
    assert.deepEqual(result.structuredContent, {
      mechanism: "cimd",
      clientId: authInfo.clientId,
      explanation: "The client_id is an HTTPS URL with a path, matching the CIMD identifier shape."
    });
  } finally {
    await client.close();
    await handler.close();
  }
});