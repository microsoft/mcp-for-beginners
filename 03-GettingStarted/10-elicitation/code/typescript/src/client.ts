import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";
import { ElicitRequestSchema } from "@modelcontextprotocol/sdk/types.js"
import { mainModule } from "process";


const client = new Client(
    {
      name: "test client",
      version: "1.0",
    },
    {
      capabilities: {
        elicitation: {},
      },
    },
  );

let baseUrl = new URL("http://localhost:3000/sse");

const sseTransport = new SSEClientTransport(baseUrl);

client.setRequestHandler(ElicitRequestSchema, (params) => {
    console.log(`${params.params.message}`);
    console.log("\nProvide the following information:");
    let schema = params.params.requestedSchema.properties;
    for (let key in schema) {
        console.log(`[INPUT]: '${key}' of type ${schema[key].type}`);
    }

    // TODO, ask for this input instead of faking the response like below

    return {
      action: "accept",
      content: {
        checkAlternatives: true,
        newDate: "2025-01-01"
      },
    };
});

async function main() {
  await client.connect(sseTransport);
  const result = await client.callTool({
    name: "book-trip",
    arguments: {
        date: "2025-01-02"
    }
    });

    console.log("Tool result: ", result);
}

main();

