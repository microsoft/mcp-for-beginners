// TypeScript Example: Context Session Manager with Strong Types
import { McpClient, RootContextManager } from '@mcp/client';

interface ContextMetadata {
  [key: string]: string | number | boolean;
  createdAt?: string;
  status?: 'active' | 'archived' | 'suspended';
}

interface MessageOptions {
  temperature?: number;
  allowedTools?: string[];
  storeInsights?: boolean;
}

interface MessageResponse {
  message: string;
  toolCalls: Array<{ name: string; arguments: Record<string, unknown> }>;
  contextId: string;
}

interface ContextInfo {
  id: string;
  name: string;
  created: string;
  lastUpdated: string;
  messageCount: number;
  metadata: ContextMetadata;
  status: string;
}

interface ArchiveResult {
  status: 'archived';
  contextId: string;
  summary: string;
}

export class ContextSession {
  private readonly client: McpClient;
  private readonly contextManager: RootContextManager;

  constructor(serverUrl: string, apiKey?: string) {
    // Initialize the MCP client with TypeScript strict types
    this.client = new McpClient({ serverUrl, apiKey });
    // Initialize context manager
    this.contextManager = new RootContextManager(this.client);
  }

  /**
   * Create a new conversation context with type safety
   * @param sessionName - Name of the conversation session
   * @param metadata - Additional metadata for the context
   * @returns Promise resolving to context ID
   */
  async createConversationContext(
    sessionName: string, 
    metadata: ContextMetadata = {}
  ): Promise<string> {
    try {
      const contextResult = await this.contextManager.createRootContext({
        name: sessionName,
        metadata: {
          ...metadata,
          createdAt: new Date().toISOString(),
          status: 'active' as const
        }
      });
      
      console.log(`✅ Created '${sessionName}' with ID: ${contextResult.id}`);
      return contextResult.id;
    } catch (error: unknown) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      console.error('❌ Error creating context:', errorMessage);
      throw error;
    }
  }

  /**
   * Send a message in an existing context with full type safety
   * @param contextId - The root context ID
   * @param message - The user's message
   * @param options - Additional options with defaults
   */
  async sendMessage(
    contextId: string, 
    message: string, 
    options: MessageOptions = {}
  ): Promise<MessageResponse> {
    try {
      const response = await this.client.sendPrompt(message, {
        rootContextId: contextId,
        temperature: options.temperature ?? 0.7,
        allowedTools: options.allowedTools ?? []
      });
      
      // Store insights if requested
      if (options.storeInsights === true) {
        await this.storeConversationInsights(contextId, message, response.generatedText);
      }
      
      return {
        message: response.generatedText,
        toolCalls: response.toolCalls ?? [],
        contextId
      };
    } catch (error: unknown) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      console.error(`❌ Error in context ${contextId}:`, errorMessage);
      throw error;
    }
  }

  /**
   * Store important insights from a conversation with intelligent parsing
   * @param contextId - The root context ID
   * @param userMessage - User's message
   * @param aiResponse - AI's response
   */
  private async storeConversationInsights(
    contextId: string, 
    userMessage: string, 
    aiResponse: string
  ): Promise<void> {
    try {
      const combinedText = `${userMessage}\n${aiResponse}`;
      const insightKeywords = ['important', 'key point', 'remember', 'significant', 'crucial'];
      
      const potentialInsights = combinedText
        .split('.')
        .filter((sentence: string) => 
          insightKeywords.some((keyword: string) => 
            sentence.toLowerCase().includes(keyword)
          )
        )
        .map((sentence: string) => sentence.trim())
        .filter((sentence: string) => sentence.length > 10);
      
      if (potentialInsights.length > 0) {
        const insights: ContextMetadata = {};
        potentialInsights.forEach((insight: string, index: number) => {
          insights[`insight_${Date.now()}_${index}`] = insight;
        });
        
        await this.contextManager.updateContextMetadata(contextId, insights);
        console.log(`💡 Stored ${potentialInsights.length} insights`);
      }
    } catch (error: unknown) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      console.warn('⚠️  Could not store insights:', errorMessage);
    }
  }

  /**
   * Get comprehensive context information with strong typing
   * @param contextId - The root context ID
   * @returns Promise resolving to formatted context information
   */
  async getContextInfo(contextId: string): Promise<ContextInfo> {
    try {
      const contextInfo = await this.contextManager.getContextInfo(contextId);
      
      return {
        id: contextInfo.id,
        name: contextInfo.name,
        created: new Date(contextInfo.createdAt).toLocaleString(),
        lastUpdated: new Date(contextInfo.lastUpdatedAt).toLocaleString(),
        messageCount: contextInfo.messageCount,
        metadata: contextInfo.metadata,
        status: contextInfo.status
      };
    } catch (error: unknown) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      console.error('❌ Error getting context info:', errorMessage);
      throw error;
    }
  }

  /**
   * Generate an intelligent conversation summary
   * @param contextId - The root context ID
   * @returns Promise resolving to generated summary
   */
  async generateContextSummary(contextId: string): Promise<string> {
    try {
      const response = await this.client.sendPrompt(
        'Please summarize our conversation in 3-4 sentences, ' +
        'highlighting key points and any decisions made.',
        { rootContextId: contextId, temperature: 0.3 }
      );
      
      // Store summary with timestamp
      await this.contextManager.updateContextMetadata(contextId, {
        conversationSummary: response.generatedText,
        summarizedAt: new Date().toISOString()
      });
      
      return response.generatedText;
    } catch (error: unknown) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      console.error('❌ Error generating summary:', errorMessage);
      throw error;
    }
  }

  /**
   * Archive a context with final summary
   * @param contextId - The root context ID
   * @returns Promise resolving to archive operation result
   */
  async archiveContext(contextId: string): Promise<ArchiveResult> {
    try {
      // Generate final summary before archiving
      const summary = await this.generateContextSummary(contextId);
      
      // Archive the context
      await this.contextManager.archiveContext(contextId);
      
      return {
        status: 'archived' as const,
        contextId,
        summary
      };
    } catch (error: unknown) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      console.error('❌ Error archiving context:', errorMessage);
      throw error;
    }
  }
}

// Complete demonstration of context session management with types
export async function demonstrateContextSession(): Promise<void> {
  console.log('🚀 Starting TypeScript Context Session Demo\n');
  const session = new ContextSession('https://mcp-server-example.com');
  
  try {
    // 1. Create customer support context with typed metadata
    const contextId = await session.createConversationContext(
      'Product Support - Database Performance',
      {
        customer: 'Globex Corporation',
        product: 'Enterprise Database',
        severity: 'Medium',
        supportAgent: 'AI Assistant'
      }
    );
    
    console.log('\n📞 Starting customer support conversation...');
    
    // 2. Initial support request with options
    const response1 = await session.sendMessage(
      contextId,
      "I'm experiencing slow query performance after the latest update.",
      { storeInsights: true, temperature: 0.8 }
    );
    console.log('🤖 AI:', response1.message.substring(0, 100) + '...');
    
    // 3. Follow-up with more context
    const response2 = await session.sendMessage(
      contextId,
      "We've checked indexes and they're properly configured.",
      { storeInsights: true, allowedTools: ['database-analyzer'] }
    );
    console.log('🤖 AI:', response2.message.substring(0, 100) + '...');
    
    // 4. Review context information with full typing
    const contextInfo: ContextInfo = await session.getContextInfo(contextId);
    console.log('\n📊 Context Summary:', {
      name: contextInfo.name,
      messages: contextInfo.messageCount,
      created: contextInfo.created
    });
    
    // 5. Generate final summary
    const summary: string = await session.generateContextSummary(contextId);
    console.log('\n📝 Final Summary:', summary);
    
    // 6. Archive completed session
    const archiveResult: ArchiveResult = await session.archiveContext(contextId);
    console.log('\n✅ Support session completed and archived!');
    console.log(`📦 Archive Status: ${archiveResult.status}`);
    
  } catch (error: unknown) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown error occurred';
    console.error('❌ Demo failed:', errorMessage);
  }
}