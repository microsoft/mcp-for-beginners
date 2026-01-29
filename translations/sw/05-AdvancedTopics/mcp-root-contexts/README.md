# MCP Root Contexts

Muktadha mzizi ni dhana muhimu katika Model Context Protocol inayotoa safu ya kudumu kwa kuhifadhi historia ya mazungumzo na hali iliyoshirikiwa kati ya maombi na vikao vingi.

## Utangulizi

Katika somo hili, tutaangalia jinsi ya kuunda, kusimamia, na kutumia muktadha mzizi katika MCP.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelewa madhumuni na muundo wa muktadha mzizi
- Kuunda na kusimamia muktadha mzizi kwa kutumia maktaba za mteja wa MCP
- Kutekeleza muktadha mzizi katika programu za .NET, Java, JavaScript, na Python
- Kutumia muktadha mzizi kwa mazungumzo ya mizunguko mingi na usimamizi wa hali
- Kutekeleza mbinu bora za usimamizi wa muktadha mzizi

## Kuelewa Muktadha Mzizi

Muktadha mzizi hutumika kama chombo kinachoshikilia historia na hali kwa mfululizo wa mwingiliano unaohusiana. Huwezesha:

- **Uendelevu wa Mazungumzo**: Kuhifadhi mazungumzo yenye mizunguko mingi yenye muktadha thabiti
- **Usimamizi wa Kumbukumbu**: Kuhifadhi na kupata taarifa kati ya mwingiliano
- **Usimamizi wa Hali**: Kufuatilia maendeleo katika michakato tata
- **Kushirikiana kwa Muktadha**: Kuruhusu wateja wengi kufikia hali ile ile ya mazungumzo

Katika MCP, muktadha mzizi una sifa hizi muhimu:

- Kila muktadha mzizi una kitambulisho cha kipekee.
- Unaweza kuwa na historia ya mazungumzo, mapendeleo ya mtumiaji, na metadata nyingine.
- Unaweza kuundwa, kufikiwa, na kuhifadhiwa kama inavyohitajika.
- Unaunga mkono udhibiti wa upatikanaji wa kina na ruhusa.

## Mzunguko wa Maisha wa Muktadha Mzizi

```mermaid
flowchart TD
    A[Create Root Context] --> B[Initialize with Metadata]
    B --> C[Send Requests with Context ID]
    C --> D[Update Context with Results]
    D --> C
    D --> E[Archive Context When Complete]
```

## Kufanya Kazi na Muktadha Mzizi

Hapa kuna mfano wa jinsi ya kuunda na kusimamia muktadha mzizi.

### Utekelezaji wa C#

```csharp
// .NET Example: Root Context Management
using Microsoft.Mcp.Client;
using System;
using System.Threading.Tasks;
using System.Collections.Generic;

public class RootContextExample
{
    private readonly IMcpClient _client;
    private readonly IRootContextManager _contextManager;
    
    public RootContextExample(IMcpClient client, IRootContextManager contextManager)
    {
        _client = client;
        _contextManager = contextManager;
    }
    
    public async Task DemonstrateRootContextAsync()
    {
        // 1. Create a new root context
        var contextResult = await _contextManager.CreateRootContextAsync(new RootContextCreateOptions
        {
            Name = "Customer Support Session",
            Metadata = new Dictionary<string, string>
            {
                ["CustomerName"] = "Acme Corporation",
                ["PriorityLevel"] = "High",
                ["Domain"] = "Cloud Services"
            }
        });
        
        string contextId = contextResult.ContextId;
        Console.WriteLine($"Created root context with ID: {contextId}");
        
        // 2. First interaction using the context
        var response1 = await _client.SendPromptAsync(
            "I'm having issues scaling my web service deployment in the cloud.", 
            new SendPromptOptions { RootContextId = contextId }
        );
        
        Console.WriteLine($"First response: {response1.GeneratedText}");
        
        // Second interaction - the model will have access to the previous conversation
        var response2 = await _client.SendPromptAsync(
            "Yes, we're using containerized deployments with Kubernetes.", 
            new SendPromptOptions { RootContextId = contextId }
        );
        
        Console.WriteLine($"Second response: {response2.GeneratedText}");
        
        // 3. Add metadata to the context based on conversation
        await _contextManager.UpdateContextMetadataAsync(contextId, new Dictionary<string, string>
        {
            ["TechnicalEnvironment"] = "Kubernetes",
            ["IssueType"] = "Scaling"
        });
        
        // 4. Get context information
        var contextInfo = await _contextManager.GetRootContextInfoAsync(contextId);
        
        Console.WriteLine("Context Information:");
        Console.WriteLine($"- Name: {contextInfo.Name}");
        Console.WriteLine($"- Created: {contextInfo.CreatedAt}");
        Console.WriteLine($"- Messages: {contextInfo.MessageCount}");
        
        // 5. When the conversation is complete, archive the context
        await _contextManager.ArchiveRootContextAsync(contextId);
        Console.WriteLine($"Archived context {contextId}");
    }
}
```

Katika msimbo uliotangulia tumefanya:

1. Kuunda muktadha mzizi kwa kikao cha msaada kwa wateja.
1. Kutuma ujumbe mwingi ndani ya muktadha huo, kuruhusu modeli kuhifadhi hali.
1. Kusasisha muktadha na metadata inayohusiana kulingana na mazungumzo.
1. Kupata taarifa za muktadha kuelewa historia ya mazungumzo.
1. Kuhifadhi muktadha baada ya mazungumzo kukamilika.

## Mfano: Utekelezaji wa Muktadha Mzizi kwa uchambuzi wa kifedha

Katika mfano huu, tutaunda muktadha mzizi kwa kikao cha uchambuzi wa kifedha, kuonyesha jinsi ya kuhifadhi hali kati ya mwingiliano mingi.

### Utekelezaji wa Java

```java
// Java Example: Root Context Implementation
package com.example.mcp.contexts;

import com.mcp.client.McpClient;
import com.mcp.client.ContextManager;
import com.mcp.models.RootContext;
import com.mcp.models.McpResponse;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class RootContextsDemo {
    private final McpClient client;
    private final ContextManager contextManager;
    
    public RootContextsDemo(String serverUrl) {
        this.client = new McpClient.Builder()
            .setServerUrl(serverUrl)
            .build();
            
        this.contextManager = new ContextManager(client);
    }
    
    public void demonstrateRootContext() throws Exception {
        // Create context metadata
        Map<String, String> metadata = new HashMap<>();
        metadata.put("projectName", "Financial Analysis");
        metadata.put("userRole", "Financial Analyst");
        metadata.put("dataSource", "Q1 2025 Financial Reports");
        
        // 1. Create a new root context
        RootContext context = contextManager.createRootContext("Financial Analysis Session", metadata);
        String contextId = context.getId();
        
        System.out.println("Created context: " + contextId);
        
        // 2. First interaction
        McpResponse response1 = client.sendPrompt(
            "Analyze the trends in Q1 financial data for our technology division",
            contextId
        );
        
        System.out.println("First response: " + response1.getGeneratedText());
        
        // 3. Update context with important information gained from response
        contextManager.addContextMetadata(contextId, 
            Map.of("identifiedTrend", "Increasing cloud infrastructure costs"));
        
        // Second interaction - using the same context
        McpResponse response2 = client.sendPrompt(
            "What's driving the increase in cloud infrastructure costs?",
            contextId
        );
        
        System.out.println("Second response: " + response2.getGeneratedText());
        
        // 4. Generate a summary of the analysis session
        McpResponse summaryResponse = client.sendPrompt(
            "Summarize our analysis of the technology division financials in 3-5 key points",
            contextId
        );
        
        // Store the summary in context metadata
        contextManager.addContextMetadata(contextId, 
            Map.of("analysisSummary", summaryResponse.getGeneratedText()));
            
        // Get updated context information
        RootContext updatedContext = contextManager.getRootContext(contextId);
        
        System.out.println("Context Information:");
        System.out.println("- Created: " + updatedContext.getCreatedAt());
        System.out.println("- Last Updated: " + updatedContext.getLastUpdatedAt());
        System.out.println("- Analysis Summary: " + 
            updatedContext.getMetadata().get("analysisSummary"));
            
        // 5. Archive context when done
        contextManager.archiveContext(contextId);
        System.out.println("Context archived");
    }
}
```

Katika msimbo uliotangulia tumefanya:

1. Kuunda muktadha mzizi kwa kikao cha uchambuzi wa kifedha.
2. Kutuma ujumbe mwingi ndani ya muktadha huo, kuruhusu modeli kuhifadhi hali.
3. Kusasisha muktadha na metadata inayohusiana kulingana na mazungumzo.
4. Kutengeneza muhtasari wa kikao cha uchambuzi na kuuhifadhi katika metadata ya muktadha.
5. Kuhifadhi muktadha baada ya mazungumzo kukamilika.

## Mfano: Usimamizi wa Muktadha Mzizi

Kusimamia muktadha mzizi kwa ufanisi ni muhimu kwa kuhifadhi historia ya mazungumzo na hali. Hapa chini ni mfano wa jinsi ya kutekeleza usimamizi wa muktadha mzizi.

### Utekelezaji wa JavaScript

```javascript
// JavaScript Example: Managing MCP Root Contexts
const { McpClient, RootContextManager } = require('@mcp/client');

class ContextSession {
  constructor(serverUrl, apiKey = null) {
    // Initialize the MCP client
    this.client = new McpClient({
      serverUrl,
      apiKey
    });
    
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
      
      console.log(`Created root context '${sessionName}' with ID: ${contextResult.id}`);
      return contextResult.id;
    } catch (error) {
      console.error('Error creating root context:', error);
      throw error;
    }
  }
  
  /**
   * Send a message in an existing context
   * @param {string} contextId - The root context ID
   * @param {string} message - The user's message
   * @param {Object} options - Additional options
   * @returns {Promise<Object>} - Response data
   */
  async sendMessage(contextId, message, options = {}) {
    try {
      // Send the message using the specified context
      const response = await this.client.sendPrompt(message, {
        rootContextId: contextId,
        temperature: options.temperature || 0.7,
        allowedTools: options.allowedTools || []
      });
      
      // Optionally store important insights from the conversation
      if (options.storeInsights) {
        await this.storeConversationInsights(contextId, message, response.generatedText);
      }
      
      return {
        message: response.generatedText,
        toolCalls: response.toolCalls || [],
        contextId
      };
    } catch (error) {
      console.error(`Error sending message in context ${contextId}:`, error);
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
      // Extract potential insights (in a real app, this would be more sophisticated)
      const combinedText = userMessage + "\n" + aiResponse;
      
      // Simple heuristic to identify potential insights
      const insightWords = ["important", "key point", "remember", "significant", "crucial"];
      
      const potentialInsights = combinedText
        .split(".")
        .filter(sentence => 
          insightWords.some(word => sentence.toLowerCase().includes(word))
        )
        .map(sentence => sentence.trim())
        .filter(sentence => sentence.length > 10);
      
      // Store insights in context metadata
      if (potentialInsights.length > 0) {
        const insights = {};
        potentialInsights.forEach((insight, index) => {
          insights[`insight_${Date.now()}_${index}`] = insight;
        });
        
        await this.contextManager.updateContextMetadata(contextId, insights);
        console.log(`Stored ${potentialInsights.length} insights in context ${contextId}`);
      }
    } catch (error) {
      console.warn('Error storing conversation insights:', error);
      // Non-critical error, so just log warning
    }
  }
  
  /**
   * Get summary information about a context
   * @param {string} contextId - The root context ID
   * @returns {Promise<Object>} - Context information
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
      console.error(`Error getting context info for ${contextId}:`, error);
      throw error;
    }
  }
  
  /**
   * Generate a summary of the conversation in a context
   * @param {string} contextId - The root context ID
   * @returns {Promise<string>} - Generated summary
   */
  async generateContextSummary(contextId) {
    try {
      // Ask the model to generate a summary of the conversation so far
      const response = await this.client.sendPrompt(
        "Please summarize our conversation so far in 3-4 sentences, highlighting the main points discussed.",
        { rootContextId: contextId, temperature: 0.3 }
      );
      
      // Store the summary in context metadata
      await this.contextManager.updateContextMetadata(contextId, {
        conversationSummary: response.generatedText,
        summarizedAt: new Date().toISOString()
      });
      
      return response.generatedText;
    } catch (error) {
      console.error(`Error generating context summary for ${contextId}:`, error);
      throw error;
    }
  }
  
  /**
   * Archive a context when it's no longer needed
   * @param {string} contextId - The root context ID
   * @returns {Promise<Object>} - Result of the archive operation
   */
  async archiveContext(contextId) {
    try {
      // Generate a final summary before archiving
      const summary = await this.generateContextSummary(contextId);
      
      // Archive the context
      await this.contextManager.archiveContext(contextId);
      
      return {
        status: "archived",
        contextId,
        summary
      };
    } catch (error) {
      console.error(`Error archiving context ${contextId}:`, error);
      throw error;
    }
  }
}

// Example usage
async function demonstrateContextSession() {
  const session = new ContextSession('https://mcp-server-example.com');
  
  try {
    // 1. Create a new context for a product support conversation
    const contextId = await session.createConversationContext(
      'Product Support - Database Performance',
      {
        customer: 'Globex Corporation',
        product: 'Enterprise Database',
        severity: 'Medium',
        supportAgent: 'AI Assistant'
      }
    );
    
    // 2. First message in the conversation
    const response1 = await session.sendMessage(
      contextId,
      "I'm experiencing slow query performance on our database cluster after the latest update.",
      { storeInsights: true }
    );
    console.log('Response 1:', response1.message);
    
    // Follow-up message in the same context
    const response2 = await session.sendMessage(
      contextId,
      "Yes, we've already checked the indexes and they seem to be properly configured.",
      { storeInsights: true }
    );
    console.log('Response 2:', response2.message);
    
    // 3. Get information about the context
    const contextInfo = await session.getContextInfo(contextId);
    console.log('Context Information:', contextInfo);
    
    // 4. Generate and display conversation summary
    const summary = await session.generateContextSummary(contextId);
    console.log('Conversation Summary:', summary);
    
    // 5. Archive the context when done
    const archiveResult = await session.archiveContext(contextId);
    console.log('Archive Result:', archiveResult);
    
    // 6. Handle any errors gracefully
  } catch (error) {
    console.error('Error in context session demonstration:', error);
  }
}

demonstrateContextSession();
```

Katika msimbo uliotangulia tumefanya:

1. Kuunda muktadha mzizi kwa mazungumzo ya msaada wa bidhaa kwa kutumia kazi `createConversationContext`. Katika kesi hii, muktadha ni kuhusu matatizo ya utendaji wa hifadhidata.

1. Kutuma ujumbe mwingi ndani ya muktadha huo, kuruhusu modeli kuhifadhi hali kwa kutumia kazi `sendMessage`. Ujumbe unaotumwa ni kuhusu utendaji wa upatikanaji wa data polepole na usanidi wa faharasa.

1. Kusasisha muktadha na metadata inayohusiana kulingana na mazungumzo.

1. Kutengeneza muhtasari wa mazungumzo na kuuhifadhi katika metadata ya muktadha kwa kutumia kazi `generateContextSummary`.

1. Kuhifadhi muktadha baada ya mazungumzo kukamilika kwa kutumia kazi `archiveContext`.

1. Kushughulikia makosa kwa ustadi ili kuhakikisha uimara.

## Muktadha Mzizi kwa Msaada wa Mizunguko Mingi

Katika mfano huu, tutaunda muktadha mzizi kwa kikao cha msaada wa mizunguko mingi, kuonyesha jinsi ya kuhifadhi hali kati ya mwingiliano mingi.

### Utekelezaji wa Python

```python
# Python Example: Root Context for Multi-Turn Assistance
import asyncio
from datetime import datetime
from mcp_client import McpClient, RootContextManager

class AssistantSession:
    def __init__(self, server_url, api_key=None):
        self.client = McpClient(server_url=server_url, api_key=api_key)
        self.context_manager = RootContextManager(self.client)
    
    async def create_session(self, name, user_info=None):
        """Create a new root context for an assistant session"""
        metadata = {
            "session_type": "assistant",
            "created_at": datetime.now().isoformat(),
        }
        
        # Add user information if provided
        if user_info:
            metadata.update({f"user_{k}": v for k, v in user_info.items()})
            
        # Create the root context
        context = await self.context_manager.create_root_context(name, metadata)
        return context.id
    
    async def send_message(self, context_id, message, tools=None):
        """Send a message within a root context"""
        # Create options with context ID
        options = {
            "root_context_id": context_id
        }
        
        # Add tools if specified
        if tools:
            options["allowed_tools"] = tools
        
        # Send the prompt within the context
        response = await self.client.send_prompt(message, options)
        
        # Update context metadata with conversation progress
        await self.context_manager.update_context_metadata(
            context_id,
            {
                f"message_{datetime.now().timestamp()}": message[:50] + "...",
                "last_interaction": datetime.now().isoformat()
            }
        )
        
        return response
    
    async def get_conversation_history(self, context_id):
        """Retrieve conversation history from a context"""
        context_info = await self.context_manager.get_context_info(context_id)
        messages = await self.client.get_context_messages(context_id)
        
        return {
            "context_info": context_info,
            "messages": messages
        }
    
    async def end_session(self, context_id):
        """End an assistant session by archiving the context"""
        # Generate a summary prompt first
        summary_response = await self.client.send_prompt(
            "Please summarize our conversation and any key points or decisions made.",
            {"root_context_id": context_id}
        )
        
        # Store summary in metadata
        await self.context_manager.update_context_metadata(
            context_id,
            {
                "summary": summary_response.generated_text,
                "ended_at": datetime.now().isoformat(),
                "status": "completed"
            }
        )
        
        # Archive the context
        await self.context_manager.archive_context(context_id)
        
        return {
            "status": "completed",
            "summary": summary_response.generated_text
        }

# Example usage
async def demo_assistant_session():
    assistant = AssistantSession("https://mcp-server-example.com")
    
    # 1. Create session
    context_id = await assistant.create_session(
        "Technical Support Session",
        {"name": "Alex", "technical_level": "advanced", "product": "Cloud Services"}
    )
    print(f"Created session with context ID: {context_id}")
    
    # 2. First interaction
    response1 = await assistant.send_message(
        context_id, 
        "I'm having trouble with the auto-scaling feature in your cloud platform.",
        ["documentation_search", "diagnostic_tool"]
    )
    print(f"Response 1: {response1.generated_text}")
    
    # Second interaction in the same context
    response2 = await assistant.send_message(
        context_id,
        "Yes, I've already checked the configuration settings you mentioned, but it's still not working."
    )
    print(f"Response 2: {response2.generated_text}")
    
    # 3. Get history
    history = await assistant.get_conversation_history(context_id)
    print(f"Session has {len(history['messages'])} messages")
    
    # 4. End session
    end_result = await assistant.end_session(context_id)
    print(f"Session ended with summary: {end_result['summary']}")

if __name__ == "__main__":
    asyncio.run(demo_assistant_session())
```

Katika msimbo uliotangulia tumefanya:

1. Kuunda muktadha mzizi kwa kikao cha msaada wa kiufundi kwa kutumia kazi `create_session`. Muktadha unajumuisha taarifa za mtumiaji kama jina na kiwango cha kiufundi.

1. Kutuma ujumbe mwingi ndani ya muktadha huo, kuruhusu modeli kuhifadhi hali kwa kutumia kazi `send_message`. Ujumbe unaotumwa ni kuhusu matatizo na kipengele cha auto-scaling.

1. Kupata historia ya mazungumzo kwa kutumia kazi `get_conversation_history`, inayotoa taarifa za muktadha na ujumbe.

1. Kumaliza kikao kwa kuhifadhi muktadha na kutengeneza muhtasari kwa kutumia kazi `end_session`. Muhtasari unakamata pointi muhimu kutoka mazungumzo.

## Mbinu Bora za Muktadha Mzizi

Hapa kuna mbinu bora za kusimamia muktadha mzizi kwa ufanisi:

- **Unda Muktadha Ulioelekezwa**: Unda muktadha mzizi tofauti kwa madhumuni au nyanja tofauti za mazungumzo ili kudumisha uwazi.

- **Weka Sera za Kumalizika**: Tekeleza sera za kuhifadhi au kufuta muktadha wa zamani ili kusimamia hifadhi na kufuata sera za uhifadhi wa data.

- **Hifadhi Metadata Muhimu**: Tumia metadata ya muktadha kuhifadhi taarifa muhimu kuhusu mazungumzo ambayo inaweza kuwa ya msaada baadaye.

- **Tumia Vitambulisho vya Muktadha kwa Ulinganifu**: Mara muktadha unapo undwa, tumia kitambulisho chake kwa ulinganifu kwa maombi yote yanayohusiana ili kudumisha mfuatano.

- **Tengeneza Muhtasari**: Wakati muktadha unapo kuwa mkubwa, fikiria kutengeneza muhtasari ili kukamata taarifa muhimu huku ukisimamia ukubwa wa muktadha.

- **Tekeleza Udhibiti wa Upatikanaji**: Kwa mifumo ya watumiaji wengi, tekeleza udhibiti sahihi wa upatikanaji ili kuhakikisha faragha na usalama wa muktadha wa mazungumzo.

- **Shughulikia Mipaka ya Muktadha**: Fahamu mipaka ya ukubwa wa muktadha na tekeleza mikakati ya kushughulikia mazungumzo marefu sana.

- **Hifadhi Muktadha Baada ya Kukamilika**: Hifadhi muktadha baada ya mazungumzo kukamilika ili kuachilia rasilimali huku ukihifadhi historia ya mazungumzo.

## Nini Kifuatacho

- [5.5 Routing](../mcp-routing/README.md)

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.