import { z } from "zod";
import { ToolCallback } from "@modelcontextprotocol/sdk/server/mcp.js";

import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

let schema = { a: z.number(), b: z.number() };

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// server.tool("multiply",
//   schema,
//   async ({ a, b }) => ({
//     content: [{ type: "text", text: String(a * b) }]
//   })
// );

// server.tool(
//     addTool.name, 
//     addTool.inputSchema, 
//     addTool.callback as ToolCallback
// );

// server.tool(
//     subtractTool.name, 
//     subtractTool.inputSchema, 
//     subtractTool.callback as ToolCallback
// );
