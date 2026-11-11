import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js";

const port = 8000;

const app = express();
app.use(express.json());

// IMPORTANT: never hard-code secrets like this in real code; look the value
// up in a secret store or let an identity provider validate the credential
function isValid(secret: string) {
    return secret === "secret123";
}

// Middleware: every request must carry a valid Authorization header
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url);
    if (!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }

    let token = req.headers["authorization"];

    if (!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }

    console.log('Middleware executed');
    next();
});

// Map to store transports by session ID
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Handle POST requests for client-to-server communication
app.post('/mcp', async (req, res) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Reuse existing transport
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // New initialization request
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        transports[sessionId] = transport;
      }
    });

    // Clean up transport when closed
    transport.onclose = () => {
      if (transport.sessionId) {
        delete transports[transport.sessionId];
      }
    };

    const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    server.tool(
      "get-current-time",
      "Get the current server time in UTC",
      async () => ({
        content: [{ type: "text", text: new Date().toISOString() }]
      })
    );

    await server.connect(transport);
  } else {
    res.status(400).json({
      jsonrpc: '2.0',
      error: {
        code: -32000,
        message: 'Bad Request: No valid session ID provided',
      },
      id: null,
    });
    return;
  }

  // Handle the request
  await transport.handleRequest(req, res, req.body);
});

// Reusable handler for GET and DELETE requests
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }

  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Handle GET requests for server-to-client notifications via SSE
app.get('/mcp', handleSessionRequest);

// Handle DELETE requests for session termination
app.delete('/mcp', handleSessionRequest);

app.listen(port, () => {
    console.log(`MCP server listening on http://localhost:${port}/mcp`);
});
