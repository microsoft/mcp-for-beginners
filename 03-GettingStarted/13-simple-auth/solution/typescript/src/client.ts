
// TODO add secret to header

import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport, StreamableHTTPClientTransportOptions } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { config } from "dotenv";

config();


let sessionId: string | undefined = undefined;

let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": process.env.token || "secret123"
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

   console.log("Available tools:", toolsResult);
   console.log("Client disconnected.");
   transport.close();
}


main()
   .then(() => {
      console.log("Exiting...");
   })
   .catch((error) => {
      console.error("Error initializing client:", error);
   })
