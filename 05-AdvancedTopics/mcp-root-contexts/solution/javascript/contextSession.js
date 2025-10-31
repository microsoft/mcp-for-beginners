// JavaScript Example: Context Session Manager
import { McpClient, RootContextManager } from '@mcp/client';

class ContextSession {
  constructor(serverUrl, apiKey = null) {
    // Initialize the MCP client
    this.client = new McpClient({ serverUrl, apiKey });
    // Initialize context manager
    this.contextManager = new RootContextManager(this.client);
  }

  /**
   * Create a new conversation context
   * @param {string} sessionName - Name of the conversation session
   * @param {Object} metadata - Additional metadata for the context
   * @returns {Promise<string>} - Context ID
   */
  async createConversationContext(sessionName, metadata = {}) {
    try {
      const contextResult = await this.contextManager.createRootContext({
        name: sessionName,
        metadata: {
          ...metadata,
          createdAt: new Date().toISOString(),
          status: 'active'
        }
      });
      
      console.log(`✅ Created '${sessionName}' with ID: ${contextResult.id}`);
      return contextResult.id;
    } catch (error) {
      console.error('❌ Error creating context:', error);
      throw error;
    }
  }

  /**
   * Send a message in an existing context
   * @param {string} contextId - The root context ID
   * @param {string} message - The user's message
   * @param {Object} options - Additional options
   */
  async sendMessage(contextId, message, options = {}) {
    try {
      const response = await this.client.sendPrompt(message, {
        rootContextId: contextId,
        temperature: options.temperature || 0.7,
        allowedTools: options.allowedTools || []
      });
      
      // Store insights if requested
      if (options.storeInsights) {
        await this.storeConversationInsights(contextId, message, response.generatedText);
      }
      
      return {
        message: response.generatedText,
        toolCalls: response.toolCalls || [],
        contextId
      };
    } catch (error) {
      console.error(`❌ Error in context ${contextId}:`, error);
      throw error;
    }
  }

  /**
   * Store important insights from a conversation
   * @param {string} contextId - The root context ID
   * @param {string} userMessage - User's message
   * @param {string} aiResponse - AI's response
   */
  async storeConversationInsights(contextId, userMessage, aiResponse) {
    try {
      const combinedText = userMessage + "\n" + aiResponse;
      const insightWords = ["important", "key point", "remember", "significant", "crucial"];
      
      const potentialInsights = combinedText
        .split(".")
        .filter(sentence => 
          insightWords.some(word => sentence.toLowerCase().includes(word))
        )
        .map(sentence => sentence.trim())
        .filter(sentence => sentence.length > 10);
      
      if (potentialInsights.length > 0) {
        const insights = {};
        potentialInsights.forEach((insight, index) => {
          insights[`insight_${Date.now()}_${index}`] = insight;
        });
        
        await this.contextManager.updateContextMetadata(contextId, insights);
        console.log(`💡 Stored ${potentialInsights.length} insights`);
      }
    } catch (error) {
      console.warn('⚠️  Could not store insights:', error);
    }
  }

  /**
   * Get comprehensive context information
   * @param {string} contextId - The root context ID
   * @returns {Promise<Object>} - Formatted context information
   */
  async getContextInfo(contextId) {
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
    } catch (error) {
      console.error(`❌ Error getting context info:`, error);
      throw error;
    }
  }

  /**
   * Generate an intelligent conversation summary
   * @param {string} contextId - The root context ID
   * @returns {Promise<string>} - Generated summary
   */
  async generateContextSummary(contextId) {
    try {
      const response = await this.client.sendPrompt(
        "Please summarize our conversation in 3-4 sentences, " +
        "highlighting key points and any decisions made.",
        { rootContextId: contextId, temperature: 0.3 }
      );
      
      // Store summary with timestamp
      await this.contextManager.updateContextMetadata(contextId, {
        conversationSummary: response.generatedText,
        summarizedAt: new Date().toISOString()
      });
      
      return response.generatedText;
    } catch (error) {
      console.error(`❌ Error generating summary:`, error);
      throw error;
    }
  }

  /**
   * Archive a context with final summary
   * @param {string} contextId - The root context ID
   * @returns {Promise<Object>} - Archive operation result
   */
  async archiveContext(contextId) {
    try {
      // Generate final summary before archiving
      const summary = await this.generateContextSummary(contextId);
      
      // Archive the context
      await this.contextManager.archiveContext(contextId);
      
      return {
        status: "archived",
        contextId,
        summary
      };
    } catch (error) {
      console.error(`❌ Error archiving context:`, error);
      throw error;
    }
  }
}

// Complete demonstration of context session management
export async function demonstrateContextSession() {
  console.log('🚀 Starting Context Session Demo\n');
  const session = new ContextSession('https://mcp-server-example.com');
  
  try {
    // 1. Create customer support context
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
    
    // 2. Initial support request
    const response1 = await session.sendMessage(
      contextId,
      "I'm experiencing slow query performance after the latest update.",
      { storeInsights: true }
    );
    console.log('🤖 AI:', response1.message.substring(0, 100) + '...');
    
    // 3. Follow-up with more context
    const response2 = await session.sendMessage(
      contextId,
      "We've checked indexes and they're properly configured.",
      { storeInsights: true }
    );
    console.log('🤖 AI:', response2.message.substring(0, 100) + '...');
    
    // 4. Review context information
    const contextInfo = await session.getContextInfo(contextId);
    console.log('\n📊 Context Summary:', {
      name: contextInfo.name,
      messages: contextInfo.messageCount,
      created: contextInfo.created
    });
    
    // 5. Generate final summary
    const summary = await session.generateContextSummary(contextId);
    console.log('\n📝 Final Summary:', summary);
    
    // 6. Archive completed session
    await session.archiveContext(contextId);
    console.log('\n✅ Support session completed and archived!');
    
  } catch (error) {
    console.error('❌ Demo failed:', error);
  }
}

// Run the demonstration
if (import.meta.main) {
  demonstrateContextSession();
}

export { ContextSession };