import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { ListToolsRequestSchema, CallToolRequestSchema } from "@modelcontextprotocol/sdk/types.js";

import { tools } from './tools/index.js';

// Create an MCP server
export const server = new Server({
  name: "Demo",
  version: "1.0.0"
}, {
    capabilities: {
        "tools": {}
    }
});

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: tools
  };
    // return {
    //     tools: [{
    //         name: "add",
    //         description: "Add two numbers",
    //         inputSchema: {
    //             "type": "object", 
    //             "properties": {
    //                 "a": {"type": "number"},
    //                 "b": {"type": "number" }
    //             }
    //         }
    //     }]
    // }

});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if (!tool) {
       return {
        error: {
            code: "tool_not_found",
            message: `Tool ${name} not found.`
        }
       };
    }
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);

       // @ts-ignore
       const result = await tool.callback(input);

       return {
          content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
      };
    } catch (error) {
       return {
          error: {
             code: "invalid_arguments",
             message: `Invalid arguments for tool ${name}: ${error instanceof Error ? error.message : String(error)}`
          }
    };
   }

});

const transport = new StdioServerTransport();

export async function start() {
    console.log("Starting server...");
    await server.connect(transport);
}