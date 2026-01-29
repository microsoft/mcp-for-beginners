# Model Context Protocol (MCP) चे Azure AI Foundry सोबत एकत्रीकरण

हा मार्गदर्शक Model Context Protocol (MCP) सर्व्हर्सना Azure AI Foundry एजंट्ससोबत कसे एकत्र करायचे हे दाखवतो, ज्यामुळे शक्तिशाली टूल ऑर्केस्ट्रेशन आणि एंटरप्राइझ AI क्षमता शक्य होतात.

## परिचय

Model Context Protocol (MCP) हा एक खुला मानक आहे जो AI अनुप्रयोगांना सुरक्षितपणे बाह्य डेटा स्रोत आणि टूल्सशी जोडण्याची परवानगी देतो. Azure AI Foundry सोबत एकत्र केल्यावर, MCP एजंट्सना विविध बाह्य सेवा, API आणि डेटा स्रोतांशी प्रमाणित पद्धतीने प्रवेश आणि संवाद साधण्याची सुविधा देते.

हे एकत्रीकरण MCP च्या टूल इकोसिस्टमची लवचिकता आणि Azure AI Foundry च्या मजबूत एजंट फ्रेमवर्कला एकत्र करून एंटरप्राइझ-ग्रेड AI सोल्यूशन्ससाठी विस्तृत सानुकूलन क्षमता प्रदान करते.

**Note:** जर तुम्हाला Azure AI Foundry Agent Service मध्ये MCP वापरायचा असेल, तर सध्या फक्त खालील प्रदेश समर्थित आहेत: westus, westus2, uaenorth, southindia आणि switzerlandnorth

## शिकण्याचे उद्दिष्टे

या मार्गदर्शकाच्या शेवटी, तुम्ही सक्षम असाल:

- Model Context Protocol आणि त्याचे फायदे समजून घेणे
- Azure AI Foundry एजंट्ससाठी MCP सर्व्हर्स सेटअप करणे
- MCP टूल एकत्रीकरणासह एजंट तयार करणे आणि कॉन्फिगर करणे
- प्रत्यक्ष MCP सर्व्हर्स वापरून व्यावहारिक उदाहरणे अंमलात आणणे
- एजंट संवादांमध्ये टूल प्रतिसाद आणि संदर्भ हाताळणे

## पूर्वअट

सुरू करण्यापूर्वी, खात्री करा की तुमच्याकडे आहे:

- AI Foundry प्रवेशासह Azure सदस्यता
- Python 3.10+ किंवा .NET 8.0+
- Azure CLI स्थापित आणि कॉन्फिगर केलेले
- AI संसाधने तयार करण्यासाठी योग्य परवानग्या

## Model Context Protocol (MCP) म्हणजे काय?

Model Context Protocol हा AI अनुप्रयोगांना बाह्य डेटा स्रोत आणि टूल्सशी जोडण्यासाठी एक प्रमाणित मार्ग आहे. मुख्य फायदे:

- **प्रमाणित एकत्रीकरण**: विविध टूल्स आणि सेवांमध्ये सुसंगत इंटरफेस
- **सुरक्षा**: सुरक्षित प्रमाणीकरण आणि अधिकृतता यंत्रणा
- **लवचिकता**: विविध डेटा स्रोत, API आणि सानुकूल टूल्ससाठी समर्थन
- **विस्तारयोग्यता**: नवीन क्षमता आणि एकत्रीकरण सहजपणे जोडता येतात

## Azure AI Foundry सोबत MCP सेटअप करणे

### पर्यावरण कॉन्फिगरेशन

तुमच्या पसंतीनुसार विकास पर्यावरण निवडा:

- [Python अंमलबजावणी](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET अंमलबजावणी](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python अंमलबजावणी

***Note*** तुम्ही हा [notebook](mcp_support_python.ipynb) चालवू शकता

### 1. आवश्यक पॅकेजेस इन्स्टॉल करा

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. अवलंबित्व आयात करा

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP सेटिंग्ज कॉन्फिगर करा

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. प्रोजेक्ट क्लायंट प्रारंभ करा

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP टूल तयार करा

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

## .NET अंमलबजावणी

***Note*** तुम्ही हा [notebook](mcp_support_dotnet.ipynb) चालवू शकता

### 1. आवश्यक पॅकेजेस इन्स्टॉल करा

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. अवलंबित्व आयात करा

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. सेटिंग्ज कॉन्फिगर करा

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP टूल डिफिनिशन तयार करा

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP टूल्ससह एजंट तयार करा

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

## MCP टूल कॉन्फिगरेशन पर्याय

तुमच्या एजंटसाठी MCP टूल्स कॉन्फिगर करताना, तुम्ही काही महत्त्वाचे पॅरामीटर्स निर्दिष्ट करू शकता:

### Python कॉन्फिगरेशन

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET कॉन्फिगरेशन

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## प्रमाणीकरण आणि हेडर्स

दोन्ही अंमलबजावण्या प्रमाणीकरणासाठी सानुकूल हेडर्सना समर्थन देतात:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## सामान्य समस्या निवारण

### 1. कनेक्शन समस्या
- MCP सर्व्हर URL उपलब्ध आहे का तपासा
- प्रमाणीकरण क्रेडेन्शियल्स तपासा
- नेटवर्क कनेक्टिव्हिटी सुनिश्चित करा

### 2. टूल कॉल अयशस्वी होणे
- टूल आर्ग्युमेंट्स आणि फॉरमॅटिंग तपासा
- सर्व्हर-विशिष्ट गरजा तपासा
- योग्य त्रुटी हाताळणी अंमलात आणा

### 3. कार्यक्षमता समस्या
- टूल कॉलची वारंवारिता ऑप्टिमाइझ करा
- जिथे योग्य असेल तिथे कॅशिंग वापरा
- सर्व्हर प्रतिसाद वेळा मॉनिटर करा

## पुढील पावले

तुमच्या MCP एकत्रीकरणाला अधिक सुधारण्यासाठी:

1. **सानुकूल MCP सर्व्हर्स एक्सप्लोर करा**: तुमच्या खासगी डेटा स्रोतांसाठी स्वतःचे MCP सर्व्हर्स तयार करा
2. **प्रगत सुरक्षा अंमलात आणा**: OAuth2 किंवा सानुकूल प्रमाणीकरण यंत्रणा जोडा
3. **मॉनिटरिंग आणि विश्लेषण**: टूल वापरासाठी लॉगिंग आणि मॉनिटरिंग अंमलात आणा
4. **तुमचे सोल्यूशन स्केल करा**: लोड बॅलन्सिंग आणि वितरित MCP सर्व्हर आर्किटेक्चरचा विचार करा

## अतिरिक्त संसाधने

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## समर्थन

अधिक मदतीसाठी आणि प्रश्नांसाठी:
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/) पहा
- [MCP community resources](https://modelcontextprotocol.io/) तपासा

## पुढे काय

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.