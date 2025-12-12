<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "036e01c8c6ecc8610809d52e4a738641",
  "translation_date": "2025-12-11T15:29:55+00:00",
  "source_file": "05-AdvancedTopics/mcp-foundry-agent-integration/README.md",
  "language_code": "ml"
}
-->
# മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ (MCP) ആസ്യൂർ AI ഫൗണ്ടറിയുമായി ഇന്റഗ്രേഷൻ

മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ (MCP) സർവറുകളെ ആസ്യൂർ AI ഫൗണ്ടറി ഏജന്റുകളുമായി എങ്ങനെ ഇന്റഗ്രേറ്റ് ചെയ്യാമെന്ന് ഈ ഗൈഡ് കാണിക്കുന്നു, ശക്തമായ ടൂൾ ഓർക്കസ്ട്രേഷൻയും എന്റർപ്രൈസ് AI കഴിവുകളും സജ്ജമാക്കുന്നു.

## പരിചയം

മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ (MCP) ഒരു ഓപ്പൺ സ്റ്റാൻഡേർഡാണ്, ഇത് AI ആപ്ലിക്കേഷനുകൾക്ക് ബാഹ്യ ഡാറ്റാ സ്രോതസ്സുകളുമായി ടൂളുകളുമായി സുരക്ഷിതമായി കണക്ട് ചെയ്യാൻ അനുവദിക്കുന്നു. ആസ്യൂർ AI ഫൗണ്ടറിയുമായി ഇന്റഗ്രേറ്റ് ചെയ്തപ്പോൾ, MCP ഏജന്റുകൾക്ക് വിവിധ ബാഹ്യ സേവനങ്ങൾ, APIകൾ, ഡാറ്റാ സ്രോതസ്സുകൾ എന്നിവ സ്റ്റാൻഡേർഡൈസ്ഡ് രീതിയിൽ ആക്‌സസ് ചെയ്ത് ഇടപഴകാൻ സാധിക്കും.

ഈ ഇന്റഗ്രേഷൻ MCPയുടെ ടൂൾ ഇക്കോസിസ്റ്റത്തിന്റെ ഫ്ലെക്സിബിലിറ്റിയും ആസ്യൂർ AI ഫൗണ്ടറിയുടെ ശക്തമായ ഏജന്റ് ഫ്രെയിംവർക്കും സംയോജിപ്പിച്ച് വ്യാപകമായ കസ്റ്റമൈസേഷൻ കഴിവുകളുള്ള എന്റർപ്രൈസ് ഗ്രേഡ് AI പരിഹാരങ്ങൾ നൽകുന്നു.

**കുറിപ്പ്:** MCP ആസ്യൂർ AI ഫൗണ്ടറി ഏജന്റ് സർവീസിൽ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, നിലവിൽ താഴെപ്പറയുന്ന മേഖലകൾ മാത്രമാണ് പിന്തുണയ്ക്കുന്നത്: westus, westus2, uaenorth, southindia, switzerlandnorth

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ഗൈഡ് അവസാനിക്കുന്നതോടെ, നിങ്ങൾക്ക് സാധിക്കും:

- മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ മനസിലാക്കുക, അതിന്റെ ഗുണങ്ങൾ അറിയുക
- MCP സർവറുകൾ ആസ്യൂർ AI ഫൗണ്ടറി ഏജന്റുകളുമായി ഉപയോഗിക്കാൻ സജ്ജമാക്കുക
- MCP ടൂൾ ഇന്റഗ്രേഷനോടുകൂടിയ ഏജന്റുകൾ സൃഷ്ടിക്കുകയും കോൺഫിഗർ ചെയ്യുകയും ചെയ്യുക
- യഥാർത്ഥ MCP സർവറുകൾ ഉപയോഗിച്ച് പ്രായോഗിക ഉദാഹരണങ്ങൾ നടപ്പിലാക്കുക
- ഏജന്റ് സംഭാഷണങ്ങളിൽ ടൂൾ പ്രതികരണങ്ങളും ഉദ്ധരണികളും കൈകാര്യം ചെയ്യുക

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

തുടങ്ങുന്നതിന് മുമ്പ്, ഉറപ്പാക്കുക:

- AI ഫൗണ്ടറി ആക്‌സസ് ഉള്ള ആസ്യൂർ സബ്സ്ക്രിപ്ഷൻ
- Python 3.10+ അല്ലെങ്കിൽ .NET 8.0+
- ആസ്യൂർ CLI ഇൻസ്റ്റാൾ ചെയ്ത് കോൺഫിഗർ ചെയ്തിട്ടുള്ളത്
- AI റിസോഴ്‌സുകൾ സൃഷ്ടിക്കാൻ അനുയോജ്യമായ അനുമതികൾ

## മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ (MCP) എന്താണ്?

മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ AI ആപ്ലിക്കേഷനുകൾക്ക് ബാഹ്യ ഡാറ്റാ സ്രോതസ്സുകളുമായി ടൂളുകളുമായി കണക്ട് ചെയ്യാനുള്ള സ്റ്റാൻഡേർഡൈസ്ഡ് മാർഗമാണ്. പ്രധാന ഗുണങ്ങൾ:

- **സ്റ്റാൻഡേർഡൈസ്ഡ് ഇന്റഗ്രേഷൻ**: വ്യത്യസ്ത ടൂളുകളുടെയും സേവനങ്ങളുടെയും ഇടയിൽ ഏകസമതല ഇന്റർഫേസ്
- **സുരക്ഷ**: സുരക്ഷിതമായ ഓതന്റിക്കേഷൻ, ഓതറൈസേഷൻ മെക്കാനിസങ്ങൾ
- **ഫ്ലെക്സിബിലിറ്റി**: വിവിധ ഡാറ്റാ സ്രോതസ്സുകൾ, APIകൾ, കസ്റ്റം ടൂളുകൾ പിന്തുണയ്ക്കൽ
- **വ്യാപ്തി വർദ്ധിപ്പിക്കൽ**: പുതിയ കഴിവുകളും ഇന്റഗ്രേഷനുകളും എളുപ്പത്തിൽ ചേർക്കാൻ സാധിക്കുക

## ആസ്യൂർ AI ഫൗണ്ടറിയുമായി MCP സജ്ജമാക്കൽ

### പരിസ്ഥിതി കോൺഫിഗറേഷൻ

നിങ്ങളുടെ ഇഷ്ടപ്പെട്ട ഡെവലപ്പ്മെന്റ് പരിസ്ഥിതി തിരഞ്ഞെടുക്കുക:

- [Python ഇംപ്ലിമെന്റേഷൻ](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET ഇംപ്ലിമെന്റേഷൻ](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python ഇംപ്ലിമെന്റേഷൻ

***കുറിപ്പ്*** നിങ്ങൾക്ക് ഈ [നോട്ട്ബുക്ക്](./mcp_support_python.ipynb) ഓടിക്കാം

### 1. ആവശ്യമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. ഡിപ്പെൻഡൻസികൾ ഇമ്പോർട്ട് ചെയ്യുക

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP സെറ്റിംഗുകൾ കോൺഫിഗർ ചെയ്യുക

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. പ്രോജക്ട് ക്ലയന്റ് ഇൻഷിയലൈസ് ചെയ്യുക

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP ടൂൾ സൃഷ്ടിക്കുക

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # ഐച്ഛികം: അനുവദിച്ചിരിക്കുന്ന ഉപകരണങ്ങൾ വ്യക്തമാക്കുക
)
```

### 6. പൂർണ്ണ Python ഉദാഹരണം

```python
with project_client:
    agents_client = project_client.agents

    # MCP ഉപകരണങ്ങളോടുകൂടിയ പുതിയ ഏജന്റ് സൃഷ്ടിക്കുക
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # ആശയവിനിമയത്തിനായി ത്രെഡ് സൃഷ്ടിക്കുക
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # ത്രെഡിന് സന്ദേശം സൃഷ്ടിക്കുക
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # ഉപകരണ അംഗീകാരങ്ങൾ കൈകാര്യം ചെയ്ത് ഏജന്റ് പ്രവർത്തിപ്പിക്കുക
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

## .NET ഇംപ്ലിമെന്റേഷൻ

***കുറിപ്പ്*** നിങ്ങൾക്ക് ഈ [നോട്ട്ബുക്ക്](./mcp_support_dotnet.ipynb) ഓടിക്കാം

### 1. ആവശ്യമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. ഡിപ്പെൻഡൻസികൾ ഇമ്പോർട്ട് ചെയ്യുക

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. സെറ്റിംഗുകൾ കോൺഫിഗർ ചെയ്യുക

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP ടൂൾ ഡിഫിനിഷൻ സൃഷ്ടിക്കുക

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP ടൂളുകളോടുകൂടിയ ഏജന്റ് സൃഷ്ടിക്കുക

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. പൂർണ്ണ .NET ഉദാഹരണം

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

നിങ്ങളുടെ ഏജന്റിനായി MCP ടൂളുകൾ കോൺഫിഗർ ചെയ്യുമ്പോൾ, നിങ്ങൾക്ക് ചില പ്രധാന പാരാമീറ്ററുകൾ വ്യക്തമാക്കാം:

### Python കോൺഫിഗറേഷൻ

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP സെർവറിന്റെ ഐഡന്റിഫയർ
    server_url="https://api.example.com/mcp", # MCP സെർവർ എൻഡ്‌പോയിന്റ്
    allowed_tools=[],                       # ഐച്ഛികം: അനുവദിച്ചിരിക്കുന്ന ഉപകരണങ്ങൾ വ്യക്തമാക്കുക
)
```

### .NET കോൺഫിഗറേഷൻ

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## ഓതന്റിക്കേഷൻ, ഹെഡറുകൾ

രണ്ടു ഇംപ്ലിമെന്റേഷനുകളും ഓതന്റിക്കേഷനായി കസ്റ്റം ഹെഡറുകൾ പിന്തുണയ്ക്കുന്നു:

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
- MCP സർവർ URL ആക്‌സസിബിൾ ആണെന്ന് ഉറപ്പാക്കുക
- ഓതന്റിക്കേഷൻ ക്രെഡൻഷ്യലുകൾ പരിശോധിക്കുക
- നെറ്റ്‌വർക്ക് കണക്ടിവിറ്റി ഉറപ്പാക്കുക

### 2. ടൂൾ കോൾ പരാജയങ്ങൾ
- ടൂൾ ആർഗ്യുമെന്റുകളും ഫോർമാറ്റിംഗും പരിശോധിക്കുക
- സർവർ-സ്പെസിഫിക് ആവശ്യകതകൾ പരിശോധിക്കുക
- ശരിയായ എറർ ഹാൻഡ്ലിംഗ് നടപ്പിലാക്കുക

### 3. പ്രകടന പ്രശ്നങ്ങൾ
- ടൂൾ കോൾ ആവൃത്തി ഒപ്റ്റിമൈസ് ചെയ്യുക
- ആവശ്യമായിടത്ത് കാഷിംഗ് നടപ്പിലാക്കുക
- സർവർ പ്രതികരണ സമയം നിരീക്ഷിക്കുക

## അടുത്ത ഘട്ടങ്ങൾ

നിങ്ങളുടെ MCP ഇന്റഗ്രേഷൻ കൂടുതൽ മെച്ചപ്പെടുത്താൻ:

1. **കസ്റ്റം MCP സർവറുകൾ എക്സ്പ്ലോർ ചെയ്യുക**: സ്വന്തം MCP സർവറുകൾ നിർമ്മിച്ച് പ്രോപ്രൈറ്ററി ഡാറ്റാ സ്രോതസ്സുകൾക്കായി
2. **അഡ്വാൻസ്ഡ് സെക്യൂരിറ്റി നടപ്പിലാക്കുക**: OAuth2 അല്ലെങ്കിൽ കസ്റ്റം ഓതന്റിക്കേഷൻ മെക്കാനിസങ്ങൾ ചേർക്കുക
3. **മോണിറ്ററിംഗ്, അനലിറ്റിക്സ്**: ടൂൾ ഉപയോഗത്തിനായി ലോഗിംഗ്, മോണിറ്ററിംഗ് നടപ്പിലാക്കുക
4. **സ്കെയിൽ ചെയ്യുക**: ലോഡ് ബാലൻസിംഗ്, ഡിസ്‌ട്രിബ്യൂട്ടഡ് MCP സർവർ ആർക്കിടെക്ചറുകൾ പരിഗണിക്കുക

## അധിക സ്രോതസ്സുകൾ

- [Azure AI Foundry ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol സാമ്പിളുകൾ](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry ഏജന്റുകൾ അവലോകനം](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP സ്പെസിഫിക്കേഷൻ](https://spec.modelcontextprotocol.io/)

## പിന്തുണ

കൂടുതൽ പിന്തുണക്കും ചോദ്യങ്ങൾക്കും:
- [Azure AI Foundry ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-foundry/) പരിശോധിക്കുക
- [MCP കമ്മ്യൂണിറ്റി സ്രോതസ്സുകൾ](https://modelcontextprotocol.io/) പരിശോധിക്കുക

## അടുത്തത്

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->