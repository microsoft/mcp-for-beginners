# Model Context Protocol (MCP) ကို Azure AI Foundry နှင့် ပေါင်းစပ်ခြင်း

ဤလမ်းညွှန်သည် Model Context Protocol (MCP) ဆာဗာများကို Azure AI Foundry အေးဂျင့်များနှင့် ပေါင်းစပ်၍ အင်အားကြီးသော ကိရိယာများ စီမံခန့်ခွဲမှုနှင့် စီးပွားရေးအဆင့် AI စွမ်းဆောင်ရည်များကို အသုံးပြုနိုင်ရန် ပြသထားသည်။

## နိဒါန်း

Model Context Protocol (MCP) သည် AI အက်ပလီကေးရှင်းများကို ပြင်ပဒေတာရင်းမြစ်များနှင့် ကိရိယာများနှင့် လုံခြုံစိတ်ချစွာ ချိတ်ဆက်နိုင်စေရန် ဖွင့်လှစ်ထားသော စံသတ်မှတ်ချက်တစ်ခုဖြစ်သည်။ Azure AI Foundry နှင့် ပေါင်းစပ်သည့်အခါ MCP သည် အေးဂျင့်များအား အမျိုးမျိုးသော ပြင်ပဝန်ဆောင်မှုများ၊ API များနှင့် ဒေတာရင်းမြစ်များကို စံပြုထားသည့် နည်းလမ်းဖြင့် ဝင်ရောက်အသုံးပြုနိုင်စေသည်။

ဤပေါင်းစပ်မှုသည် MCP ၏ ကိရိယာပတ်ဝန်းကျင်၏ လွတ်လပ်မှုနှင့် Azure AI Foundry ၏ ခိုင်မာသော အေးဂျင့် ဖရိမ်ဝတ်ကို ပေါင်းစပ်ကာ စီးပွားရေးအဆင့် AI ဖြေရှင်းချက်များကို ကျယ်ပြန့်စွာ စိတ်ကြိုက်ပြင်ဆင်နိုင်စေသည်။

**[!NOTE]** Azure AI Foundry Agent Service တွင် MCP ကို အသုံးပြုလိုပါက လက်ရှိတွင် အောက်ပါဒေသများသာ ထောက်ပံ့ထားပါသည်။ westus, westus2, uaenorth, southindia နှင့် switzerlandnorth

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤလမ်းညွှန်ပြီးဆုံးသည်နှင့်အတူ သင်သည် -

- Model Context Protocol ၏ အဓိပ္ပါယ်နှင့် အကျိုးကျေးဇူးများကို နားလည်နိုင်မည်
- Azure AI Foundry အေးဂျင့်များနှင့် အသုံးပြုရန် MCP ဆာဗာများကို တပ်ဆင်နိုင်မည်
- MCP ကိရိယာ ပေါင်းစပ်ထားသော အေးဂျင့်များကို ဖန်တီးပြီး ပြင်ဆင်နိုင်မည်
- အမှန်တကယ် MCP ဆာဗာများကို အသုံးပြု၍ လက်တွေ့ ဥပမာများကို အကောင်အထည်ဖော်နိုင်မည်
- အေးဂျင့် စကားပြောများတွင် ကိရိယာတုံ့ပြန်မှုများနှင့် ကိုးကားချက်များကို ကိုင်တွယ်နိုင်မည်

## မတိုင်မီ လိုအပ်ချက်များ

စတင်မတိုင်မီ အောက်ပါအချက်များရှိရန် သေချာပါစေ -

- AI Foundry ဝင်ရောက်ခွင့်ပါသော Azure စာရင်းသွင်းမှု
- Python 3.10+ သို့မဟုတ် .NET 8.0+
- Azure CLI တပ်ဆင်ပြီး ပြင်ဆင်ထားခြင်း
- AI အရင်းအမြစ်များ ဖန်တီးခွင့်ရှိခြင်း

## Model Context Protocol (MCP) ဆိုတာဘာလဲ?

Model Context Protocol သည် AI အက်ပလီကေးရှင်းများကို ပြင်ပဒေတာရင်းမြစ်များနှင့် ကိရိယာများနှင့် ချိတ်ဆက်ရန် စံပြုထားသည့် နည်းလမ်းတစ်ခုဖြစ်သည်။ အဓိက အကျိုးကျေးဇူးများမှာ -

- **စံပြုထားသော ပေါင်းစပ်မှု**: ကိရိယာနှင့် ဝန်ဆောင်မှုအမျိုးမျိုးအတွက် တူညီသော အင်တာဖေ့စ်
- **လုံခြုံမှု**: လုံခြုံသော အတည်ပြုခြင်းနှင့် ခွင့်ပြုခြင်းစနစ်များ
- **လွတ်လပ်မှု**: အမျိုးမျိုးသော ဒေတာရင်းမြစ်များ၊ API များနှင့် စိတ်ကြိုက်ကိရိယာများကို ထောက်ပံ့မှု
- **တိုးချဲ့နိုင်မှု**: စွမ်းဆောင်ရည်အသစ်များနှင့် ပေါင်းစပ်မှုများကို လွယ်ကူစွာ ထည့်သွင်းနိုင်ခြင်း

## Azure AI Foundry နှင့် MCP တပ်ဆင်ခြင်း

### ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း

သင်နှစ်သက်ရာ ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်ကို ရွေးချယ်ပါ -

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***[!NOTE]*** သင်သည် ဤ [notebook](mcp_support_python.ipynb) ကို ပြေးနိုင်သည်

### ၁။ လိုအပ်သော ပက်ကေ့ဂျ်များ တပ်ဆင်ခြင်း

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### ၂။ လိုအပ်သော အရာများကို သွင်းယူခြင်း

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### ၃။ MCP ဆက်တင်များ ပြင်ဆင်ခြင်း

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### ၄။ Project Client ကို စတင်ဖန်တီးခြင်း

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### ၅။ MCP ကိရိယာ ဖန်တီးခြင်း

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### ၆။ Python ဥပမာ ပြည့်စုံ

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

***[!NOTE]*** သင်သည် ဤ [notebook](mcp_support_dotnet.ipynb) ကို ပြေးနိုင်သည်

### ၁။ လိုအပ်သော ပက်ကေ့ဂျ်များ တပ်ဆင်ခြင်း

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### ၂။ လိုအပ်သော အရာများကို သွင်းယူခြင်း

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### ၃။ ဆက်တင်များ ပြင်ဆင်ခြင်း

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### ၄။ MCP ကိရိယာ သတ်မှတ်ချက် ဖန်တီးခြင်း

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### ၅။ MCP ကိရိယာများပါရှိသော အေးဂျင့် ဖန်တီးခြင်း

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### ၆။ .NET ဥပမာ ပြည့်စုံ

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

## MCP ကိရိယာ ပြင်ဆင်မှု ရွေးချယ်စရာများ

အေးဂျင့်အတွက် MCP ကိရိယာများကို ပြင်ဆင်ရာတွင် အရေးကြီးသော ပါရာမီတာများကို သတ်မှတ်နိုင်သည် -

### Python ပြင်ဆင်မှု

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET ပြင်ဆင်မှု

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## အတည်ပြုခြင်းနှင့် Header များ

နှစ်မျိုးစလုံးတွင် အတည်ပြုခြင်းအတွက် စိတ်ကြိုက် header များ ထောက်ပံ့သည် -

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## ဖြစ်ပေါ်နိုင်သော ပြဿနာများ ဖြေရှင်းနည်း

### ၁။ ချိတ်ဆက်မှု ပြဿနာများ
- MCP ဆာဗာ URL သည် ဝင်ရောက်နိုင်မှုရှိကြောင်း စစ်ဆေးပါ
- အတည်ပြုချက် အချက်အလက်များကို စစ်ဆေးပါ
- ကွန်ယက် ချိတ်ဆက်မှု ရှိကြောင်း သေချာစေပါ

### ၂။ ကိရိယာ ခေါ်ဆိုမှု မအောင်မြင်ခြင်း
- ကိရိယာ အချက်အလက်များနှင့် ဖော်မတ်ကို ပြန်လည်စစ်ဆေးပါ
- ဆာဗာအထူးလိုအပ်ချက်များကို စစ်ဆေးပါ
- မှားယွင်းမှု ကိုင်တွယ်မှုကို မှန်ကန်စွာ အကောင်အထည်ဖော်ပါ

### ၃။ စွမ်းဆောင်ရည် ပြဿနာများ
- ကိရိယာ ခေါ်ဆိုမှု အကြိမ်ရေကို တိုးတက်အောင် ပြင်ဆင်ပါ
- လိုအပ်သလို cache ကို အသုံးပြုပါ
- ဆာဗာ တုံ့ပြန်ချိန်များကို စောင့်ကြည့်ပါ

## နောက်တစ်ဆင့်များ

MCP ပေါင်းစပ်မှုကို ပိုမိုတိုးတက်စေရန် -

1. **စိတ်ကြိုက် MCP ဆာဗာများ ရှာဖွေပါ**: ကိုယ်ပိုင် ဒေတာရင်းမြစ်များအတွက် MCP ဆာဗာများ တည်ဆောက်ပါ
2. **လုံခြုံရေး မြှင့်တင်ပါ**: OAuth2 သို့မဟုတ် စိတ်ကြိုက် အတည်ပြုစနစ်များ ထည့်သွင်းပါ
3. **စောင့်ကြည့်မှုနှင့် သုံးသပ်မှု**: ကိရိယာ အသုံးပြုမှုအတွက် မှတ်တမ်းတင်ခြင်းနှင့် စောင့်ကြည့်မှု ထည့်သွင်းပါ
4. **ဖြေရှင်းချက်ကို တိုးချဲ့ပါ**: လုပ်ငန်းခွဲခြားခြင်းနှင့် ဖြန့်ဝေထားသော MCP ဆာဗာ ဖွဲ့စည်းမှုများကို စဉ်းစားပါ

## အပိုဆောင်း အရင်းအမြစ်များ

- [Azure AI Foundry စာတမ်းများ](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol နမူနာများ](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry အေးဂျင့်များ အကျဉ်းချုပ်](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP သတ်မှတ်ချက်](https://spec.modelcontextprotocol.io/)

## အထောက်အပံ့

ထပ်မံအထောက်အပံ့နှင့် မေးခွန်းများအတွက် -
- [Azure AI Foundry စာတမ်းများ](https://learn.microsoft.com/azure/ai-foundry/) ကို ပြန်လည်ကြည့်ရှုပါ
- [MCP အသိုင်းအဝိုင်း အရင်းအမြစ်များ](https://modelcontextprotocol.io/) ကို စစ်ဆေးပါ

## နောက်တစ်ဆင့်

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းသည် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။