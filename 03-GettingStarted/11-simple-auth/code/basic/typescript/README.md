# Run sample

This sample starts an MCP server (Streamable HTTP on `http://localhost:8000/mcp`) behind an Express middleware that checks for a valid `Authorization` header.

## Install dependencies

```bash
npm install
```

## Build

```bash
npm run build
```

## Start server

```bash
npm start
```

this should start the server.

### Start client

In a separate terminal, run:

```bash
npm run client
```

You should see a result similar to:

```text
Connected to MCP server with session ID: 4bb7dbba-9095-412b-ab62-f2c430927a80
Available tools: [ 'get-current-time' ]
Tool result: [{"type":"text","text":"2026-11-10T20:52:30.428Z"}]
Client disconnected.
Client is ready to use.
```

this means the credential being sent through is being allowed, and in the server terminal you see `Middleware executed` for each request.

Try changing the credential in `src/client.ts` to "secret1234", run `npm run build` and `npm run client` again, then you should see:

```text
Error initializing client: StreamableHTTPError: Streamable HTTP error: Error POSTing to endpoint: Forbidden
```

this means you were authenticated (you had a credential), but it was invalid. A request without an `Authorization` header at all gets `401 Unauthorized`.
