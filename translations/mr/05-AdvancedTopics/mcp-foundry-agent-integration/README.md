# मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) ची मायक्रोसॉफ्ट फाउंड्रीसह समाकलन

हा मार्गदर्शक मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) सर्व्हर मायक्रोसॉफ्ट फाउंड्री एजंट्ससह कसे एकत्र करायचे हे दर्शवितो, ज्यामुळे पॉवरफुल टूल ऑर्केस्ट्रेशन आणि एंटरप्राइज AI क्षमता सक्षम होतात.

## परिचय

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) हा एक खुला मानक आहे जो AI अनुप्रयोगांना सुरक्षितपणे बाह्य डेटास्थाने आणि साधनांशी कनेक्ट होण्यास सक्षम करतो. मायक्रोसॉफ्ट फाउंड्रीसोबत समाकलित केल्यावर, MCP एजंट्सना विविध बाह्य सेवा, API आणि डेटास्त्रोत यांच्या मानकीकृत पद्धतीने प्रवेश आणि संवाद साधता येतो.

हे समाकलन MCP च्या टूल इकोसिस्टमच्या लवचिकतेला मायक्रोसॉफ्ट फाउंड्रीच्या मजबूत एजंट फ्रेमवर्कशी जोडते, ज्यामुळे व्यापक सानुकूलन क्षमतांसह एंटरप्राइज-ग्रेड AI उपाय उपलब्ध होतात.

**टीप:** जर आपण मायक्रोसॉफ्ट फाउंड्री एजंट सर्व्हिसमध्ये MCP वापरू इच्छित असाल, तर सध्या फक्त खालील प्रदेश समर्थित आहेत: westus, westus2, uaenorth, southindia आणि switzerlandnorth

## शिकण्याचे उद्दिष्ट

या मार्गदर्शकाच्या शेवटी, आपण सक्षम असाल:

- मॉडेल कॉन्टेक्स्ट प्रोटोकॉल आणि त्याचे फायदे समजून घेणे
- मायक्रोसॉफ्ट फाउंड्री एजंटसाठी MCP सर्व्हर सेटअप करणे
- MCP टूल समाकलनासह एजंट तयार आणि संरचीत करणे
- वास्तविक MCP सर्व्हर वापरून व्यावहारिक उदाहरणे राबविणे
- एजंट संभाषणांमध्ये टूल प्रतिसाद आणि संदर्भ व्यवस्थापित करणे

## पूर्वतयारी

सुरुवात करण्यापूर्वी, खालील बाबी तपासा:

- मायक्रोसॉफ्ट फाउंड्री प्रवेश असलेली Azure सदस्यता
- Python 3.10+ किंवा .NET 8.0+
- Azure CLI इन्स्टॉल आणि कॉन्फिगर केलेले असणे
- AI संसाधने तयार करण्याची योग्य परवानगी

## मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) म्हणजे काय?

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल हा AI अनुप्रयोगांना बाह्य डेटास्त्रोत आणि साधनांशी कनेक्ट होण्यासाठी एक मानकीकृत मार्ग आहे. मुख्य फायदे यामध्ये आहेत:

- **मानकीकृत समाकलन**: वेगवेगळ्या साधने आणि सेवांमध्ये सुसंगत इंटरफेस
- **सुरक्षा**: सुरक्षित प्रमाणीकरण आणि अधिकृतता प्रणाली
- **लवचिकता**: विविध डेटास्त्रोत, API आणि सानुकूल साधनांसाठी समर्थन
- **विस्तृतता**: नवीन क्षमता आणि समाकलन सहजपणे जोडणे

## मायक्रोसॉफ्ट फाउंड्रीसह MCP सेटअप करणे

### पर्यावरण कॉन्फिगरेशन

आपले प्राधान्यसिद्ध विकास पर्यावरण निवडा:

- [Python अमलात आणणी](#python-अमलात-आणणी)
- [.NET अमलात आणणी](#codeblock5)

---

## Python अमलात आणणी

***टिप*** आपण हा [नोटबुक](./mcp_support_python.ipynb) चालवू शकता

### 1. आवश्यक पॅकेजेस इन्स्टॉल करा

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. अवलंबित्वे आयात करा

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
    allowed_tools=[],  # ऐच्छिक: परवानगी असलेली साधने निर्दिष्ट करा
)
```

### 6. पूर्ण Python उदाहरण

```python
with project_client:
    agents_client = project_client.agents

    # MCP साधनांसह नवीन एजंट तयार करा
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # संवादासाठी थ्रेड तयार करा
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # थ्रेडसाठी संदेश तयार करा
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # साधन मंजुरी हाताळा आणि एजंट चालवा
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

    # संभाषण प्रदर्शित करा
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

## .NET अमलात आणणी

***टिप*** आपण हा [नोटबुक](./mcp_support_dotnet.ipynb) चालवू शकता

### 1. आवश्यक पॅकेजेस इन्स्टॉल करा

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. अवलंबित्वे आयात करा

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

### 5. MCP टूलसह एजंट तयार करा

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

जेव्हा आपण आपल्या एजंटसाठी MCP टूल कॉन्फिगर करता, तेव्हा आपण अनेक महत्त्वाचे घटक निर्दिष्ट करू शकता:

### Python कॉन्फिगरेशन

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP सर्व्हरसाठी ओळखकर्ता
    server_url="https://api.example.com/mcp", # MCP सर्व्हर एंडपॉईंट
    allowed_tools=[],                       # ऐच्छिक: परवानगी दिलेले साधने निर्दिष्ट करा
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

दोन्ही अमलात आणण्या कस्टम हेडर्ससाठी समर्थन करतात ज्यांचा वापर प्रमाणीकरणासाठी होतो:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## सामान्य समस्या सोडविण्याचे उपाय

### 1. कनेक्शन समस्या
- MCP सर्व्हर URL उपलब्ध असल्याची खात्री करा
- प्रमाणीकरण क्रेडेन्शियल तपासा
- नेटवर्क कनेक्टिव्हिटी सुनिश्चित करा

### 2. टूल कॉल अयशस्वी
- टूल आर्ग्यूमेंट्स आणि फॉरमॅटिंगची समीक्षा करा
- सर्व्हर-विशिष्ट गरजा तपासा
- योग्य त्रुटी हाताळणी अमलात आणा

### 3. कार्यक्षमता समस्या
- टूल कॉलची वारंवारता ऑप्टिमाइज़ करा
- योग्य ठिकाणी कॅशिंग लागू करा
- सर्व्हर प्रतिसाद वेळा निरीक्षण करा

## पुढील टप्पे

आपल्या MCP समाकलनात पुढील सुधारणा करण्यासाठी:

1. **सानुकूल MCP सर्व्हर एक्सप्लोर करा**: आपल्या स्वतःच्या MCP सर्व्हर तयार करा खासगी डेटास्रोतसाठी
2. **उन्नत सुरक्षा अमलात आणा**: OAuth2 किंवा सानुकूल प्रमाणीकरण मेकॅनिझम जोडा
3. **मॉनिटरिंग आणि विश्लेषण**: टूल वापरासाठी लॉगिंग आणि मॉनिटरिंग अमलात आणा
4. **आपले समाधान स्केल करा**: लोड बॅलेंसिंग आणि वितरित MCP सर्व्हर आर्किटेक्चर विचारात घ्या

## अतिरिक्त स्रोत

- [Microsoft Foundry दस्तऐवज](https://learn.microsoft.com/azure/ai-foundry/)
- [मॉडेल कॉन्टेक्स्ट प्रोटोकॉल नमुने](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry एजंट्स आढावा](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP तपशीलवार विशिष्टता](https://modelcontextprotocol.io/specification/2026-07-28/)

## समर्थन

अतिरिक्त समर्थन आणि प्रश्नांसाठी:
- [Microsoft Foundry दस्तऐवज पहा](https://learn.microsoft.com/azure/ai-foundry/)
- [MCP समुदाय स्रोत तपासा](https://modelcontextprotocol.io/)

## पुढे काय आहे

- [5.14 MCP कॉन्टेक्स्ट इंजिनिअरिंग](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->