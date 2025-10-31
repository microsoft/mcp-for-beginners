// TypeScript type definitions for MCP Client (mock types for demonstration)
declare module '@mcp/client' {
  export interface McpClientOptions {
    serverUrl: string;
    apiKey?: string;
  }

  export interface RootContextCreateOptions {
    name: string;
    metadata?: Record<string, unknown>;
  }

  export interface RootContextResult {
    id: string;
    name: string;
    createdAt: string;
    lastUpdatedAt: string;
    messageCount: number;
    metadata: Record<string, unknown>;
    status: string;
  }

  export interface SendPromptOptions {
    rootContextId?: string;
    temperature?: number;
    allowedTools?: string[];
  }

  export interface PromptResponse {
    generatedText: string;
    toolCalls?: Array<{ name: string; arguments: Record<string, unknown> }>;
  }

  export class McpClient {
    constructor(options: McpClientOptions);
    sendPrompt(message: string, options?: SendPromptOptions): Promise<PromptResponse>;
  }

  export class RootContextManager {
    constructor(client: McpClient);
    createRootContext(options: RootContextCreateOptions): Promise<RootContextResult>;
    getContextInfo(contextId: string): Promise<RootContextResult>;
    updateContextMetadata(contextId: string, metadata: Record<string, unknown>): Promise<void>;
    archiveContext(contextId: string): Promise<void>;
  }
}