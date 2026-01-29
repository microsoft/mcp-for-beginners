# Model Context Protocol (MCP) लाई Azure AI Foundry सँग एकीकृत गर्ने तरिका

यो मार्गदर्शनले Model Context Protocol (MCP) सर्भरहरूलाई Azure AI Foundry एजेन्टहरूसँग कसरी एकीकृत गर्ने देखाउँछ, जसले शक्तिशाली उपकरण समन्वय र उद्यम स्तरको AI क्षमताहरू सक्षम बनाउँछ।

## परिचय

Model Context Protocol (MCP) एउटा खुला मानक हो जसले AI अनुप्रयोगहरूलाई बाह्य डाटा स्रोत र उपकरणहरूसँग सुरक्षित रूपमा जडान गर्न सक्षम बनाउँछ। Azure AI Foundry सँग एकीकृत हुँदा, MCP ले एजेन्टहरूलाई विभिन्न बाह्य सेवा, API, र डाटा स्रोतहरूसँग मानकीकृत तरिकाले पहुँच र अन्तरक्रिया गर्न अनुमति दिन्छ।

यो एकीकरणले MCP को उपकरण पारिस्थितिकी तन्त्रको लचिलोपनलाई Azure AI Foundry को बलियो एजेन्ट फ्रेमवर्कसँग जोड्छ, जसले व्यापक अनुकूलन क्षमतासहित उद्यम-स्तरको AI समाधानहरू प्रदान गर्दछ।

**Note:** यदि तपाईं Azure AI Foundry Agent Service मा MCP प्रयोग गर्न चाहनुहुन्छ भने, हालका लागि निम्न क्षेत्रहरू मात्र समर्थित छन्: westus, westus2, uaenorth, southindia र switzerlandnorth

## सिकाइका उद्देश्यहरू

यस मार्गदर्शनको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- Model Context Protocol र यसको फाइदाहरू बुझ्न
- Azure AI Foundry एजेन्टहरूसँग प्रयोग गर्न MCP सर्भरहरू सेटअप गर्न
- MCP उपकरण एकीकरणसहित एजेन्टहरू सिर्जना र कन्फिगर गर्न
- वास्तविक MCP सर्भरहरू प्रयोग गरेर व्यावहारिक उदाहरणहरू कार्यान्वयन गर्न
- एजेन्ट संवादहरूमा उपकरण प्रतिक्रियाहरू र उद्धरणहरू व्यवस्थापन गर्न

## पूर्वआवश्यकताहरू

सुरु गर्नु अघि, सुनिश्चित गर्नुहोस् कि तपाईं सँग छ:

- AI Foundry पहुँच सहित Azure सदस्यता
- Python 3.10+ वा .NET 8.0+
- Azure CLI इन्स्टल र कन्फिगर गरिएको
- AI स्रोतहरू सिर्जना गर्न उपयुक्त अनुमति

## Model Context Protocol (MCP) के हो?

Model Context Protocol AI अनुप्रयोगहरूलाई बाह्य डाटा स्रोत र उपकरणहरूसँग जडान गर्ने मानकीकृत तरिका हो। मुख्य फाइदाहरूमा समावेश छन्:

- **मानकीकृत एकीकरण**: विभिन्न उपकरण र सेवाहरूमा समान इन्टरफेस
- **सुरक्षा**: सुरक्षित प्रमाणीकरण र प्राधिकरण संयन्त्रहरू
- **लचिलोपन**: विभिन्न डाटा स्रोत, API, र अनुकूलित उपकरणहरूको समर्थन
- **विस्तारयोग्यता**: नयाँ क्षमताहरू र एकीकरणहरू सजिलै थप्न सकिने

## Azure AI Foundry सँग MCP सेटअप गर्ने तरिका

### वातावरण कन्फिगरेसन

आफ्नो मनपर्ने विकास वातावरण छान्नुहोस्:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** तपाईं यो [notebook](mcp_support_python.ipynb) चलाउन सक्नुहुन्छ

### 1. आवश्यक प्याकेजहरू इन्स्टल गर्नुहोस्

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. निर्भरता आयात गर्नुहोस्

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP सेटिङहरू कन्फिगर गर्नुहोस्

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. प्रोजेक्ट क्लाइन्ट सुरु गर्नुहोस्

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP उपकरण सिर्जना गर्नुहोस्

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. पूर्ण Python उदाहरण

```python
with project_client:
    agents_client = project_client.agents

    # Create a new agent with MCP tools
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Create thread for communication
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Create message to thread
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Handle tool approvals and run agent
    mcp_tool.update_headers("SuperSecret", "123456")
    run = agents_client.runs.create(thread_id=thread.id, agent_id=agent.id, tool_resources=mcp_tool.resources)
    print(f"Created run, ID: {run.id}")

    while run.status in ["queued", "in_progress", "requires_action"]:
        time.sleep(1)
        run = agents_client.runs.get(thread_id=thread.id, run_id=run.id)

        if run.status == "requires_action" and isinstance(run.required_action, SubmitToolApprovalAction):
            tool_calls = run.required_action.submit_tool_approval.tool_calls
            if not tool_calls:
                print("No tool calls provided - cancelling run")
                agents_client.runs.cancel(thread_id=thread.id, run_id=run.id)
                break

            tool_approvals = []
            for tool_call in tool_calls:
                if isinstance(tool_call, RequiredMcpToolCall):
                    try:
                        print(f"Approving tool call: {tool_call}")
                        tool_approvals.append(
                            ToolApproval(
                                tool_call_id=tool_call.id,
                                approve=True,
                                headers=mcp_tool.headers,
                            )
                        )
                    except Exception as e:
                        print(f"Error approving tool_call {tool_call.id}: {e}")

            if tool_approvals:
                agents_client.runs.submit_tool_outputs(
                    thread_id=thread.id, run_id=run.id, tool_approvals=tool_approvals
                )

        print(f"Current run status: {run.status}")

    print(f"Run completed with status: {run.status}")

    # Display conversation
    messages = agents_client.messages.list(thread_id=thread.id)
    print("\nConversation:")
    print("-" * 50)
    for msg in messages:
        if msg.text_messages:
            last_text = msg.text_messages[-1]
            print(f"{msg.role.upper()}: {last_text.text.value}")
            print("-" * 50)
```

---

## .NET Implementation

***Note*** तपाईं यो [notebook](mcp_support_dotnet.ipynb) चलाउन सक्नुहुन्छ

### 1. आवश्यक प्याकेजहरू इन्स्टल गर्नुहोस्

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. निर्भरता आयात गर्नुहोस्

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. सेटिङहरू कन्फिगर गर्नुहोस्

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP उपकरण परिभाषा सिर्जना गर्नुहोस्

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP उपकरणहरूसँग एजेन्ट सिर्जना गर्नुहोस्

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. पूर्ण .NET उदाहरण

```csharp
// Create thread and message
PersistentAgentThread thread = await agentClient.Threads.CreateThreadAsync();

PersistentThreadMessage message = await agentClient.Messages.CreateMessageAsync(
    thread.Id,
    MessageRole.User,
    "What's difference between Azure OpenAI and OpenAI?");

// Configure tool resources with headers
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
ToolResources toolResources = mcpToolResource.ToToolResources();

// Create and handle run
ThreadRun run = await agentClient.Runs.CreateRunAsync(thread, agent, toolResources);

while (run.Status == RunStatus.Queued || run.Status == RunStatus.InProgress || run.Status == RunStatus.RequiresAction)
{
    await Task.Delay(TimeSpan.FromMilliseconds(1000));
    run = await agentClient.Runs.GetRunAsync(thread.Id, run.Id);

    if (run.Status == RunStatus.RequiresAction && run.RequiredAction is SubmitToolApprovalAction toolApprovalAction)
    {
        var toolApprovals = new List<ToolApproval>();
        foreach (var toolCall in toolApprovalAction.SubmitToolApproval.ToolCalls)
        {
            if (toolCall is RequiredMcpToolCall mcpToolCall)
            {
                Console.WriteLine($"Approving MCP tool call: {mcpToolCall.Name}");
                toolApprovals.Add(new ToolApproval(mcpToolCall.Id, approve: true)
                {
                    Headers = { ["SuperSecret"] = "123456" }
                });
            }
        }

        if (toolApprovals.Count > 0)
        {
            run = await agentClient.Runs.SubmitToolOutputsToRunAsync(thread.Id, run.Id, toolApprovals: toolApprovals);
        }
    }
}

// Display messages
using Azure;

AsyncPageable<PersistentThreadMessage> messages = agentClient.Messages.GetMessagesAsync(
    threadId: thread.Id,
    order: ListSortOrder.Ascending
);

await foreach (PersistentThreadMessage threadMessage in messages)
{
    Console.Write($"{threadMessage.CreatedAt:yyyy-MM-dd HH:mm:ss} - {threadMessage.Role,10}: ");
    foreach (MessageContent contentItem in threadMessage.ContentItems)
    {
        if (contentItem is MessageTextContent textItem)
        {
            Console.Write(textItem.Text);
        }
        else if (contentItem is MessageImageFileContent imageFileItem)
        {
            Console.Write($"<image from ID: {imageFileItem.FileId}>");
        }
        Console.WriteLine();
    }
}
```

---

## MCP उपकरण कन्फिगरेसन विकल्पहरू

एजेन्टका लागि MCP उपकरणहरू कन्फिगर गर्दा, तपाईंले केही महत्वपूर्ण प्यारामिटरहरू निर्दिष्ट गर्न सक्नुहुन्छ:

### Python कन्फिगरेसन

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET कन्फिगरेसन

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## प्रमाणीकरण र हेडरहरू

दुवै इम्प्लिमेन्टेसनहरूले प्रमाणीकरणका लागि अनुकूलित हेडरहरू समर्थन गर्छन्:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## सामान्य समस्याहरू समाधान गर्ने तरिका

### 1. जडान समस्या
- MCP सर्भर URL पहुँचयोग्य छ कि छैन जाँच गर्नुहोस्
- प्रमाणीकरण प्रमाणपत्रहरू जाँच गर्नुहोस्
- नेटवर्क कनेक्टिविटी सुनिश्चित गर्नुहोस्

### 2. उपकरण कल असफलता
- उपकरणका तर्कहरू र ढाँचाहरू समीक्षा गर्नुहोस्
- सर्भर-विशिष्ट आवश्यकताहरू जाँच गर्नुहोस्
- उचित त्रुटि ह्यान्डलिङ कार्यान्वयन गर्नुहोस्

### 3. प्रदर्शन समस्या
- उपकरण कलको आवृत्ति अनुकूलन गर्नुहोस्
- जहाँ उपयुक्त हो क्यासिङ लागू गर्नुहोस्
- सर्भर प्रतिक्रिया समयहरू अनुगमन गर्नुहोस्

## आगामी कदमहरू

तपाईंको MCP एकीकरण अझ सुधार गर्न:

1. **अनुकूलित MCP सर्भरहरू अन्वेषण गर्नुहोस्**: आफ्नै MCP सर्भरहरू निर्माण गर्नुहोस् निजी डाटा स्रोतहरूको लागि
2. **उन्नत सुरक्षा कार्यान्वयन गर्नुहोस्**: OAuth2 वा अनुकूलित प्रमाणीकरण संयन्त्रहरू थप्नुहोस्
3. **अनुगमन र विश्लेषण**: उपकरण प्रयोगको लागि लगिङ र अनुगमन कार्यान्वयन गर्नुहोस्
4. **आफ्नो समाधान विस्तार गर्नुहोस्**: लोड ब्यालेन्सिङ र वितरित MCP सर्भर संरचनाहरू विचार गर्नुहोस्

## थप स्रोतहरू

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## समर्थन

थप समर्थन र प्रश्नहरूको लागि:
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/) समीक्षा गर्नुहोस्
- [MCP community resources](https://modelcontextprotocol.io/) जाँच गर्नुहोस्

## के गर्ने अर्को

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।