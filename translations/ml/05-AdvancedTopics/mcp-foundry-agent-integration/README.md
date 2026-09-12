# മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോകോൾ (MCP) മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയുമായി ഇന്റഗ്രേഷൻ

മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോകോൾ (MCP) സെർവറുകളെ മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറി ഏജന്റുകളുമായി എങ്ങനെ സംയോജിപ്പിക്കാമെന്ന് ഈ ഗൈഡ് കാണിച്ച് നല്‍കുന്നു, ശക്തമായ ടൂൾ ഓർക്കസ്‌ട്രേഷൻ மற்றும் എന്റർപ്രൈസ് AI ശേഷികകൾ സാധ്യമാക്കുന്നു.

## പരിചയം

മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോകോൾ (MCP) ഒരു ഓപ്പൺ സ്റ്റാൻഡേർഡാണ്, ഇത് AI അപ്ലിക്കേഷനുകൾക്ക് വിദേശ ഡാറ്റാ ഉറവിടങ്ങളുമായും ടൂളുകളുമായും സുരക്ഷിതമായി ബന്ധപ്പെടാൻ അനുവദിക്കുന്നു. മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയുമായി സംയോജിപ്പിക്കുമ്പോൾ, MCP ഏജന്റുകൾക്ക് വ്യത്യസ്ത വിദേശ സേവനങ്ങൾ, API-കൾ, ഡാറ്റാ ഉറവിടങ്ങൾ എന്നിവ സ്റ്റാൻഡേർഡായ രീതിയിൽ ആക്സസ് ചെയ്ത് ഇടപഴകാൻ കഴിയുന്നു.

MCP ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ ശക്തമായ ഘടന കൂടിച്ചേർത്ത MCP-യുടെ ടൂൾ പരിസ്ഥിതിയുടെ സൗകര്യത്തോടെ ഈ സംയോജനം സംയോജിപ്പിച്ച് എന്റർപ്രൈസ് ഗ്രേഡ് AI പരിഹാരങ്ങൾ വ്യാപകം ചെയ്ത് ഇഷ്ടാനുസൃതമാക്കാനുള്ള ശേഷികൾ നൽകുന്നു.

**കുറിപ്പ്:** Microsoft Foundry Agent Service-ൽ MCP ഉപയോഗിക്കാൻ താത്കാലികമായി ഈ താഴെ പറയുന്ന മേഖലകൾ മാത്രം പിന്തുണയ്ക്കുന്നു: westus, westus2, uaenorth, southindia, switzerlandnorth

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ഗൈഡിന്റെ അവസാനം, നിങ്ങൾക്ക് കഴിയും:

- മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോകോൾ മനസ്സിലാക്കുക അതിന്റെ നേട്ടങ്ങൾ അറിയുക
- മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറി ഏജന്റുകളുമായി MCP സെർവറുകൾ സജ്ജമാക്കുക
- MCP ടൂൾ ഇന്റഗ്രേഷനുള്ള ഏജന്റുകൾ സൃഷ്‌ടിക്കുകയും കോൺഫിഗർ ചെയ്യുകയും ചെയ്യുക
- യഥാർത്ഥ MCP സെർവറുകൾ ഉപയോഗിച്ച് പ്രായോഗിക ഉദാഹരണങ്ങൾ നടപ്പിലാക്കുക
- ഏജന്റ് സംഭാഷണങ്ങളിൽ ടൂൾ പ്രതികരണങ്ങളും ഉദ്ധരണികളും കൈകാര്യം ചെയ്യുക

## ആവശ്യമായ മുന്‍രണ്ടുകള്‍

ആരംഭിക്കുന്നതിന് മുമ്പ്, നിങ്ങൾക്ക് ഉണ്ടായിരിക്കണം:

- Microsoft Foundry ആക്സസ് ഉള്ള ഒരു Azure സബ്സ്ക്രിപ്ഷൻ
- Python 3.10+ അല്ലെങ്കിൽ .NET 8.0+
- Azure CLI ഇൻസ്റ്റാൾ ചെയ്ത് കോൺഫിഗർ ചെയ്തിരിക്കണം
- AI വിഭവങ്ങൾ സൃഷ്ടിക്കാൻ അനുവദിക്കുന്ന അനുയോജ്യമായ അനുമതികൾ

## മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോകോൾ (MCP) എന്താണ്?

മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോകോൾ AI അപ്ലിക്കേഷനുകൾക്ക് വിദേശ ഡാറ്റാ ഉറവിടങ്ങളും ടൂളുകളും സമാന രീതിയിൽ ബന്ധിപ്പിക്കാൻ ഉപകരിക്കുന്ന സ്റ്റാൻഡേർഡായ മാർഗമാണ്. പ്രധാന നേട്ടങ്ങൾ:

- **സ്റ്റാൻഡർഡൈസ്ഡ് ഇന്റഗ്രേഷൻ**: വ്യത്യസ്ത ടൂളുകളും സേവനങ്ങളും തമ്മിൽ ഏകീകൃത ഇന്റർഫേസ്
- **സുരക്ഷ**: സുരക്ഷിത അംഗീകാരംും അധികാര സ്ഥിരീകരണവും
- **സ്വുപരിഗണന**: വിവിധ ഡാറ്റാ ഉറവിടങ്ങളും API-കളും കസ്റ്റം ടൂളുകളും പിന്തുണവ്
- **വിപുലീകരണശേഷി**: പുതിയ കഴിവുകളും ഇന്റഗ്രേഷനുകളും എളുപ്പത്തിൽ ചേർക്കാനും

## മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയുമായി MCP ഇന്റഗ്രേഷൻ സജ്ജീകരിക്കൽ

### എൻവയോൺമെന്റ് കോൺഫിഗറേഷൻ

നിങ്ങളുടെ ഇഷ്ടാനുസൃത ഡെവലപ്മെന്റ് എൻവയോൺമെന്റ് തിരഞ്ഞെടുക്കൂ:

- [Python നടപ്പാക്കൽ](#python-നടപ്പാക്കൽ)
- [.NET നടപ്പാക്കൽ](#codeblock5)

---

## Python നടപ്പാക്കൽ

***കുറിപ്പ്*** നിങ്ങൾക്ക് ഈ [നോട്ട്ബുക്ക്](./mcp_support_python.ipynb) ഓടിക്കാം

### 1. ആവശ്യമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. ഡിപ്പൻഡൻസികൾ ഇറക്കുമതി ചെയ്യുക

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP ക്രമീകരണങ്ങൾ കോൺഫിഗർ ചെയ്യുക

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. പ്രോജക്റ്റ് ക്ലയന്റ് ഇൻലൈൻ ചെയ്യുക

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP ടൂൾ സൃഷ്‌ടിക്കുക

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # ഐക്ഷണികം: അനുവദിച്ചിരിക്കുന്ന ഉപകരണങ്ങൾ സൂചിപ്പിക്കുക
)
```

### 6. പൂർണ്ണമായ Python ഉദാഹരണം

```python
with project_client:
    agents_client = project_client.agents

    # MCP ഉപകരണങ്ങളോടുകൂടി പുതിയ ഒരു ഏജന്റ് സൃഷ്ടിക്കുക
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # ആശയവിനിമയ്ക്കായി ഒരു ത്രെഡ് സൃഷ്ടിക്കുക
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # ത്രെഡിലേക്ക് സന്ദേശം സൃഷ്ടിക്കുക
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # ഉപകരണാനുമതികൾ കൈകാര്യം ചെയ്ത് ഏജന്റ് പ്രവർത്തിപ്പിക്കുക
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

    # സംഭാഷണം പ്രദർശിപ്പിക്കുക
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

## .NET നടപ്പാക്കൽ

***കുറിപ്പ്*** നിങ്ങൾക്ക് ഈ [നോട്ട്ബുക്ക്](./mcp_support_dotnet.ipynb) ഓടിക്കാം

### 1. ആവശ്യമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. ഡിപ്പൻഡൻസികൾ ഇറക്കുമതി ചെയ്യുക

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. ക്രമീകരണങ്ങൾ കോൺഫിഗർ ചെയ്യുക

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP ടൂൾ നിർവ്വചനം സൃഷ്‌ടിക്കുക

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP ടൂളുകൾക്കൊപ്പം ഏജന്റ് സൃഷ്‌ടിക്കുക

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. പൂർണ്ണമായ .NET ഉദാഹരണം

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

## MCP ടൂൾ കോൺഫിഗറേഷൻ ഓപ്ഷനുകൾ

നിങ്ങളുടെ ഏജന്റിനായി MCP ടൂളുകൾ കോൺഫിഗർ ചെയ്യുമ്പോൾ, നിങ്ങൾക്ക് ചില പ്രധാന പാരാമീറ്ററുകൾ നിശ്ചയിക്കാം:

### Python കോൺഫിഗറേഷൻ

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP സെർവറിനുള്ള ഐഡന്റിഫയർ
    server_url="https://api.example.com/mcp", # MCP സെർവർ എൻഡ്‌പോയിന്റ്
    allowed_tools=[],                       # തിരഞ്ഞെടുക്കാം: അനുവദിച്ചിട്ടുള്ള ടൂളുകൾ വ്യക്തമാക്കുക
)
```

### .NET കോൺഫിഗറേഷൻ

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## അംഗീകാരം மற்றும் ഹെഡറുകൾ

ഇരുവിധ നടപ്പാക്കലുകളും അംഗീകാരംക്കായി കസ്റ്റം ഹെഡറുകൾ പിന്തുണയ്ക്കുന്നു:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## സാധാരണ പ്രശ്നങ്ങൾ പരിഹരിക്കൽ

### 1. കണക്ഷൻ പ്രശ്നങ്ങൾ
- MCP സെർവർ URL ലഭ്യമാണെന്ന് പരിശോധിക്കുക
- അംഗീകാരം ക്രെഡൻഷ്യലുകൾ പരിശോധിക്കുക
- നെറ്റ്‌വർക്ക് ബന്ധം ഉറപ്പാക്കുക

### 2. ടൂൾ കോൾ പരാജയങ്ങൾ
- ടൂൾ പാരാമീറ്ററുകളും ഫോർമാറ്റും വിശകലനം ചെയ്യുക
- സെർവർ-സ്പെസിഫിക് ആവശ്യകതകൾ പരിശോധിക്കുക
- ശരിയായ തെറ്റ് കൈകാര്യം പ്രയോഗിക്കുക

### 3. പ്രകടന പ്രശ്നങ്ങൾ
- ടൂൾ കോൾ ആവർത്തനം കുറയ്ക്കുക
- യോജിച്ച സ്ഥലങ്ങളിൽ കാഷിംഗ് പ്രയോഗിക്കുക
- സെർവർ പ്രതികരണ സമയം നിരീക്ഷിക്കുക

## അടുത്ത അറിയേണ്ട കാര്യങ്ങൾ

നിങ്ങളുടെ MCP ഇന്റഗ്രേഷൻ കൂടുതൽ മെച്ചപ്പെടുത്താൻ:

1. **കസ്റ്റം MCP സെർവറുകൾ പരിശോധന ചെയ്യുക**: ന്റെ സ്വന്തം MCP സെർവറുകൾ നിർമ്മിക്കുക പ്രൈവറ്റ് ഡാറ്റാ ഉറവിടങ്ങൾക്കായി
2. **അഗ്‌രഗണSecurityനിർവഹണം**: OAuth2 അല്ലെങ്കിൽ കസ്റ്റം അംഗീകാര സാങ്കേതിക വിദ്യകൾ ചേർക്കുക
3. **നിരീക്ഷണം, വിശകലനം**: ടൂൾ ഉപയോഗത്തിന് ലോഗിംഗ്, നിരീക്ഷണം നടപ്പിലാക്കുക
4. **ഉപമാനം**: ലോഡ് ബാലൻസിംഗ്, വിതരണം ചെയ്ത MCP സെർവർ ആർക്കിടെക്ചറുകൾ പരിഗണിക്കുക

## അധിക സഹായക വൃത്താന്തങ്ങൾ

- [Microsoft Foundry ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol സാമ്പിളുകൾ](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry ഏജന്റുകൾ അവലോകനം](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP സ്പെസിഫിക്കേഷൻ](https://modelcontextprotocol.io/specification/2026-07-28/)

## സഹായം

അധിക സഹായത്തിനും ചോദ്യങ്ങൾക്കുമായി:
- [Microsoft Foundry ഡോക്യുമെന്റേഷൻ പരിശോധിക്കുക](https://learn.microsoft.com/azure/ai-foundry/)
- [MCP കമ്മ്യൂണിറ്റി വിഭവങ്ങൾ പരിശോധിക്കുക](https://modelcontextprotocol.io/)

## അടുത്തത്

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->