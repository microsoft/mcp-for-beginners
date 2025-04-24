// mcp_sample.ts - MCP TypeScript Sample Implementation
import { EventEmitter } from 'events';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {  ResourceTemplate } from '@modelcontextprotocol/sdk/server/mcp.js';
import { z } from 'zod';


/**
 * Extended MCP Server implementation in TypeScript
 */
export class ExtendedMcpServer {
  private serverName: string;
  private version: string;
  private models: string[];
  private events: EventEmitter;
  private mcpServer: McpServer;

  constructor(options: {
    serverName?: string;
    version?: string;
    models?: string[];
  } = {}) {
    this.serverName = options.serverName || 'TypeScript MCP Server';
    this.version = options.version || '1.0.0';
    this.models = options.models || ['gpt-4', 'llama-3-70b', 'claude-3-sonnet'];
    this.events = new EventEmitter();

    // Create the core MCP server
    this.mcpServer = new McpServer({
      name: this.serverName,
      version: this.version
    });

    // Register the completion tool
    this.registerCompletionTool();
    
    // Register the search resource
    this.registerSearchResource();
  }

  get name(): string {
    return this.serverName;
  }

  /**
   * Register the completion tool with the MCP server
   */
  private registerCompletionTool(): void {
    this.mcpServer.tool(
      'completion',
      {
        model: z.string(),
        prompt: z.string(),
        options: z.object({
          temperature: z.number().optional(),
          max_tokens: z.number().optional(),
          stream: z.boolean().optional()
        }).optional()
      },
      async ({ model, prompt, options }) => {
        console.log(`Processing completion request for model: ${model}`);
        
        // Validate model
        if (!this.models.includes(model)) {
          throw new Error(`Model ${model} not supported`);
        }
        
        // Emit event for monitoring/metrics
        this.events.emit('request', { 
          type: 'completion', 
          model, 
          timestamp: new Date() 
        });
        
        // In a real implementation, this would call an AI model
        // Here we just echo back parts of the request with a mock response
        const response = {
          id: `mcp-resp-${Date.now()}`,
          model,
          text: `This is a response to: ${prompt.substring(0, 30)}...`,
          usage: {
            promptTokens: prompt.split(' ').length,
            completionTokens: 20,
            totalTokens: prompt.split(' ').length + 20
          }
        };
        
        // Simulate network delay
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Emit completion event
        this.events.emit('completion', {
          model,
          timestamp: new Date()
        });
        
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(response)
            }
          ]
        };
      }
    );
  }
  
  /**
   * Register search resource with the MCP server
   */
  private registerSearchResource(): void {
    this.mcpServer.resource(
      'search',
      new ResourceTemplate("test://{query}", { list: undefined }),
      async (uri, { query }) => {
        
        console.log(`Processing search request for: ${uri}`);
        
        console.log(`Processing search request for: ${query}`);
        
        
        // Simulate search processing
        await new Promise(resolve => setTimeout(resolve, 300));
        
        // Mock search results
        const results = [
          { title: 'Result 1', snippet: `Related to ${query}...` },
          { title: 'Result 2', snippet: `Information about ${query}...` },
          { title: 'Result 3', snippet: `More details on ${query}...` }
        ];
        
        return {
          contents: [
            {
              uri: uri.href,
              text: JSON.stringify(results)
            }
          ]
        };
      }
    );
  }

  /**
   * Connect the server to a transport
   * @returns Promise that resolves when connected
   */
  public async connect(): Promise<void> {
    const transport = new StdioServerTransport();
    await this.mcpServer.connect(transport);
    console.log(`Server connected via stdio transport`);
  }

  /**
   * Register an event listener
   * @param event - The event name
   * @param listener - The event handler function
   */
  public on(event: string, listener: (...args: any[]) => void): void {
    this.events.on(event, listener);
  }
  
  /**
   * Get the MCP server instance
   * @returns The MCP server instance
   */
  public getMcpServer(): McpServer {
    return this.mcpServer;
  }

  /**
   * Get the list of supported models
   * @returns Array of supported model names
   */
  public getSupportedModels(): string[] {
    return [...this.models];
  }
}

// Demo usage

const server = new ExtendedMcpServer({
  serverName: 'TypeScript MCP Demo Server',
  version: '1.0.0'
});

// Register event handlers
server.on('request', (data) => {
  console.log(`Request received: ${JSON.stringify(data)}`);
});

server.on('completion', (data) => {
  console.log(`Completion finished: ${JSON.stringify(data)}`);
});

console.log(`MCP Server "${server.name}" initialized`);
console.log(`Supported models: ${server.getSupportedModels().join(', ')}`);

// Connect the server
server.connect().catch(error => {
  console.error('Failed to connect server:', error);
  process.exit(1);
});

