import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import { z } from "zod";
import express from "express";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
},
{
  "capabilities": {
    "elicitation": {}
  }
});

function checkAvailability(date: string): Promise<boolean> {
    // Simulate checking availability
    return Promise.resolve(date === "2025-01-01");
}

 server.tool(
  "book-trip",
  { 
    date: z.string()
  },
  async ({ date }) => {
    // 1. Check availability
    const available = await checkAvailability(date);
    
    if (!available) {
      // 2. Ask user if they want to try alternative dates
      const result = await server.server.elicitInput({
        message: `No trip available at on ${date}. Would you like to check alternative dates?`,
        requestedSchema: {
          type: "object",
          properties: {
            checkAlternatives: {
              type: "boolean",
              title: "Alternate date",
              description: "Fill in other date"
            },
            newDate: {
              type: "string",
              title: "New Date",
              description: "Please provide a new date"
            }
          },
          required: ["checkAlternatives"]
        }
      });

      // 3. Check if user provided a new date
      if (result.action === "accept" && result.content?.checkAlternatives) {
        let ok = await checkAvailability(result.content?.newDate as string);
        if(ok) {
          return {
            content: [
              {
                type: "text",
                text: `Trip booked on alternate date: ${result.content?.newDate}`
              }
            ]
          };
        } else {
          // 3b. No trip available on new date
          return {
            content: [
              {
                type: "text",
                text: `No trip available on ${result.content?.newDate}.`
              }
            ]
          };
        }  
      }
      // 4. User didn't provide a new date
      return {
        content: [{
          type: "text",
          text: "No booking made. Original date not available."
        }]
      };
    } else {
    // 1b. available, confirm booking
      return {
        content: [{
          type: "text",
          text: `Booked trip on ${date}`
        }]
      };
  }
  }
);

const app = express();
app.use(express.json());

// Store transports for each session type
const transports = {
  sse: {} as Record<string, SSEServerTransport>
};

app.get('/sse', async (req, res) => {
  // Create SSE transport for legacy clients
  const transport = new SSEServerTransport('/messages', res);
  transports.sse[transport.sessionId] = transport;
  
  res.on("close", () => {
    delete transports.sse[transport.sessionId];
  });
  
  await server.connect(transport);
});

// Legacy message endpoint for older clients
app.post('/messages', async (req, res) => {
  const sessionId = req.query.sessionId as string;
  const transport = transports.sse[sessionId];
  if (transport) {
    await transport.handlePostMessage(req, res, req.body);
  } else {
    res.status(400).send('No transport found for sessionId');
  }
});

app.listen(3000);