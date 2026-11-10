
// The secret is sent in the Authorization header of every request

import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport, StreamableHTTPClientTransportOptions } from "@modelcontextprotocol/sdk/client/streamableHttp.js";



let sessionId: string | undefined = undefined;

let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

const serverUrl = "http://localhost:8000/mcp";

async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );

   const client = new Client({
      name: "example-client",
      version: "1.0.0"
   });

   await client.connect(transport);
   sessionId = transport.sessionId;
   console.log("Connected to MCP server with session ID:", sessionId);

   let toolsResult = await client.listTools();
   console.log("Available tools:", toolsResult.tools.map(t => t.name));

   let result = await client.callTool({ name: "get-current-time", arguments: {} });
   console.log("Tool result:", JSON.stringify(result.content));

   await client.close();
   console.log("Client disconnected.");
}

main()
   .then(() => {
      console.log("Client is ready to use.");
   })
   .catch((error) => {
      console.error("Error initializing client:", error);
   })
