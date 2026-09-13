# ಮಾದರಿ ಪ್ರ سيا ಪ್ರೋಟೋಕಾಲ್ (MCP) ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಜೊತೆಗೆ ಏಕೀಕರಣ

ಈ ಮಾರ್ಗದರ್ಶಕೆ ಮಾದರಿ ಪ್ರ ಸ್ಯ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಸರ್ವರ್‌ಗಳನ್ನು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್‌ಗಳೊಂದಿಗೆ ಏಕೀಕರಿಸುವ ವಿಧಾನವನ್ನು ತೋರಿಸುತ್ತದೆ, ಶಕ್ತಿಶಾಲಿ ಉಪಕರಣ ಸಂಯೋಜನೆ ಮತ್ತು ಸಂಸ್ಥೆಗಳ AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸಾಧ್ಯಮಾಡುವಂತೆ.

## ಪರಿಚಯ

ಮಾದರಿ ಪ್ರ ಸ್ಯ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಒಂದು ತೆರೆಯಾದ ಮಾನಕವಾಗಿದೆ, ಅದು AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಬಾಹ್ಯ ಡೇಟಾ ಮೂಲಗಳು ಮತ್ತು ಉಪಕರಣಗಳಿಗೆ ಸುರಕ್ಷಿತವಾಗಿ ಸಂಪರ್ಕ ಸಾಧಿಸಲು ನೆರವಾಗುತ್ತದೆ. ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಜೊತೆಗೆ ಏಕೀಕರಿಸಿದಾಗ, MCP ಏಜೆಂಟ್‌ಗಳಿಗೆ ವಿವಿಧ ಬಾಹ್ಯ ಸೇವೆಗಳು, APIಗಳು ಮತ್ತು ಡೇಟಾ ಮೂಲಗಳೊಂದಿಗೆ ಮಾನಕೀಕೃತ ರೀತಿಯಲ್ಲಿ ಪ್ರವೇಶಿಸುವ ಮತ್ತು ಸಂವಹನ ಮಾಡುವ ಅವಕಾಶ ಕಲ್ಪಿಸುತ್ತದೆ.

ಈ ಏಕೀಕರಣ MCP ಯ ಉಪಕರಣ ಪರಿಸರದ ಲವಚಿಕತೆಯನ್ನು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಯ ದೃಢವಾದ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಗೆ ಸಂಯೋಜಿಸಿ, ವ್ಯಾಪಾರ ಮಟ್ಟದ AI ಪರಿಹಾರಗಳನ್ನು ವಿಸ್ತೃತ ವೈಯಕ್ತಿಕೀಕರಣ ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಒದಗಿಸುತ್ತದೆ.

**ಗಮನಿಸಿ:** ನೀವು Microsoft Foundry ಏಜೆಂಟ್ ಸೇವೆಯಲ್ಲಿ MCP ಅನ್ನು ಬಳಸಲು ಬಯಸಿದರೆ, ಪ್ರಸ್ತುತ ಕೆಳಗಿನ ಪ್ರದೇಶಗಳು ಮಾತ್ರ ಬೆಂಬಲವಿದೆ: westus, westus2, uaenorth, southindia ಮತ್ತು switzerlandnorth

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಮಾರ್ಗದರ್ಶಕದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- ಮಾದರಿ ಪ್ರ ಸ್ಯ ಪ್ರೋಟೋಕಾಲ್ ಮತ್ತು ಅದರ ಲಾಭಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್‌ಗಳಿಗಾಗಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸುವುದು
- MCP ಉಪಕರಣ ಏಕೀಕರಣದೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದು ಮತ್ತು ಸಂರಚಿಸುವುದು
- ನಿಜವಾದ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳನ್ನು ಜಾರಿಗೊಳಿಸುವುದು
- ಏಜೆಂಟ್ ಸಂಭಾಷಣೆಯಲ್ಲಿ ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಮತ್ತು ಉಲ್ಲೇಖಗಳನ್ನು ವರಹಿಸುವುದು

## ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

ಶುರುಮಾಡುವ ಮೊದಲು, ನೀವು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಪ್ರವೇಶ ಹೊಂದಿರುವ ಅಜೂರ್ ಚಂದಾದಾರಿಕೆ
- Python 3.10+ ಅಥವಾ .NET 8.0+
- ಅಜೂರ್ CLI ಅನ್ನು ಸ್ಥಾಪಿಸಿದ್ದು ಮತ್ತು ಸಂರಚಿಸಲಾಗಿದೆ
- AI ಸಂಪನ್ಮೂಲಗಳನ್ನು ರಚಿಸಲು ಸೂಕ್ತ ಅನುಮತಿಗಳು

## ಮಾದರಿ ಪ್ರ ಸ್ಯ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಅಂದ್ರೇನು?

ಮಾದರಿ ಪ್ರ ಸ್ಯ ಪ್ರೋಟೋಕಾಲ್ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಬಾಹ್ಯ ಡೇಟಾ ಮೂಲಗಳು ಮತ್ತು ಉಪಕರಣಗಳಿಗೆ ಸಂಪರ್ಕಿಸಲು ಮಾನಕೀಕೃತ ವಿಧಾನವಾಗಿದೆ. ಮುಖ್ಯ ಲಾಭಗಳು:

- **ಮಾನಕೀಕೃತ ಏಕೀಕರಣ**: ವಿಭಿನ್ನ ಉಪಕರಣಗಳು ಮತ್ತು ಸೇವೆಗಳ ನಡುವೆಯೂ ಸಮನಿಷ್ಠ ಇಂಟರ್ಫೇಸ್
- **ಸುರಕ್ಷತೆ**: ಸುರಕ್ಷಿತ ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು ಅನುಮತಿಯ ಕ್ರಮಗಳು
- **ಲವಚಿಕತೆ**: ವಿವಿಧ ಡೇಟಾ ಮೂಲಗಳು, APIಗಳು, ಮತ್ತು ಕಸ್ಟಮ್ ಉಪಕರಣಗಳಿಗೆ ಬೆಂಬಲ
- **ವಿಸ್ತರಣೀಯತೆ**: ಹೊಸ ಸಾಮರ್ಥ್ಯ ಮತ್ತು ಏಕೀಕರಣಗಳು ಸೇರಿಸಲು ಸುಲಭ

## ಮಾದರಿ ಪ್ರ ಸ್ಯ ಪ್ರೋಟೋಕಾಲ್ ಅನ್ನು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಜೊತೆಗೆ ಸ್ಥಾಪಿಸುವುದು

### ಪರಿಸರ ಸಂರಚನೆ

ನಿಮ್ಮ ಅನುಕೂಲದ ಅಭಿವೃದ್ಧಿ ಪರಿಸರವನ್ನು ಆರಿಸಿ:

- [Python ಅನುಷ್ಠಾನ](#python-ಅನುಷ್ಠಾನ)
- [.NET ಅನುಷ್ಠಾನ](#codeblock5)

---

## Python ಅನುಷ್ಠಾನ

***ಗಮನಿಸಿ*** ನೀವು ಈ [ನೋಟ್ಬುಕ್](./mcp_support_python.ipynb) ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಬಹುದು

### 1. ಅಗತ್ಯ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಸ್ಥಾಪಿಸು

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. ಅವಲಂಬನೆಗಳನ್ನು ಆಮದುಮಾಡಿ

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP ಸಂರಚನೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. ಪ್ರಾಜೆಕ್ಟ್ ಕ್ಲೈಂಟ್ ಆರಂಭಿಸಿ

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP ಉಪಕರಣವನ್ನು ರಚಿಸಿ

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # ಐಚ್ಛಿಕ: ಪರವಾನಗಿಯುಳ್ಳ ಟೂಲ್‌ಗಳನ್ನು ಸೂಚಿಸಿ
)
```

### 6. ಸಂಪೂರ್ಣ Python ಉದಾಹರಣೆ

```python
with project_client:
    agents_client = project_client.agents

    # MCP সরঞ্জামಗಳೊಂದಿಗೆ ಹೊಸ ಏಜೆಂಟ್ ರಚಿಸಿ
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # ಸಂವಹನಕ್ಕಾಗಿ ತುಣುಕು ರಚಿಸಿ
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # ತುಣುಕುಗೆ ಸಂದೇಶ ರಚಿಸಿ
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # ಟೂಲ್ ಅನುಮೋದನೆಗಳನ್ನು ನಿಭಾಯಿಸಿ ಮತ್ತು ಏಜೆಂಟ್ ಅನ್ನು ನಡೆಸಿ
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

    # ಸಂಭಾಷಣೆಯನ್ನು ಪ್ರದರ್ಶಿಸಿ
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

## .NET ಅನುಷ್ಠಾನ

***ಗಮನಿಸಿ*** ನೀವು ಈ [ನೋಟ್ಬುಕ್](./mcp_support_dotnet.ipynb) ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಬಹುದು

### 1. ಅಗತ್ಯ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಸ್ಥಾಪಿಸು

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. ಅವಲಂಬನೆಗಳನ್ನು ಆಮದುಮಾಡಿ

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. ಸಂರಚನೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನವನ್ನು ರಚಿಸಿ

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP ಉಪಕರಣಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ ರಚಿಸಿ

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. ಸಂಪೂರ್ಣ .NET ಉದಾಹರಣೆ

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

## MCP ಉಪಕರಣ ಸಂರಚನಾ ಆಯ್ಕೆಗಳು

ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗಾಗಿ MCP ಉಪಕರಣಗಳನ್ನು ಸಂರಚಿಸುವಾಗ, ನೀವು ಹಲವು ಮಹತ್ವದ ಪರಿಮಾಣಗಳನ್ನು ಸೂಚಿಸಬಹುದು:

### Python ಸಂರಚನೆ

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP ಸರ್ವರ್‌ಗಾಗಿ ಗುರುತಿಸು
    server_url="https://api.example.com/mcp", # MCP ಸರ್ವರ್ ಎಂಡ್ಪಾಯಿಂಟ್
    allowed_tools=[],                       # ಐಚ್ಛಿಕ: ಅನುಮತಿಸಲಾದ ಸಾಧನಗಳನ್ನು ಸೂಚಿಸಿ
)
```

### .NET ಸಂರಚನೆ

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು ಹೆಡರ್ಸ್

ಇಬ್ಬರೂ ಅನುಷ್ಠಾನಗಳು ಪ್ರಮಾಣೀಕರಣಕ್ಕಾಗಿ ಕಸ್ಟಮ್ ಹೆಡರ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳ ಪರಿಹಾರ

### 1. ಸಂಪರ್ಕ ಸಮಸ್ಯೆಗಳು
- MCP ಸರ್ವರ್ URL ಯನ್ನು ಪ್ರವೇಶಿಸಬಹುದಾದ್ದು ಎಂದು ಪರಿಶೀಲಿಸಿ
- ಪ್ರಮಾಣೀಕರಣ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
- ಜಾಲ ಸಂಪರ್ಕ ದಾಖಲಿಸುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ

### 2. ಉಪಕರಣ ಕರೆ ವಿಫಲತೆಗಳು
- ಉಪಕರಣದ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು ಮತ್ತು ಸ್ವರೂಪ ಪರಿಶೀಲಿಸಿ
- ಸರ್ವರ್-ವಿಶಿಷ್ಟ ಅಗತ್ಯಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
- ಸರಿ ಪ್ರಮಾಣದ ದೋಷ ನಿರ್ವಹಣೆಯನ್ನು ಜಾರಿಗೊಳಿಸಿ

### 3. ಕಾರ್ಯಕ್ಷಮತೆ ಸಮಸ್ಯೆಗಳು
- ಉಪಕರಣ ಕರೆ ಆವರ್ತನೆಯನ್ನು ತಕ್ಕಮಾರಿಗೆ ಮಾಡಸು
- ಬೇಕಾದಲ್ಲಿ ಕ್ಯಾಶಿಂಗ್ ಜಾರಿಗೆ
- ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯಾ ಸಮಯಗಳನ್ನು ಗಮನಿಸಿ

## ಮುಂದಿನ ಹೆಜ್ಜೆಗಳು

ನಿಮ್ಮ MCP ಏಕೀಕರಣವನ್ನು ಇನ್ನಷ್ಟು ಶಕ್ತಿಶಾಲಿಗೊಳಿಸಲು:

1. **ಕಸ್ಟಮ್ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ**: ನಿಮ್ಮದೇ ಮಾಲೀಕತ್ವದ ಡೇಟಾ ಮೂಲಗಳಿಗಾಗಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ
2. **ಹೆಚ್ಚಿದ ಸುರಕ್ಷತೆ ಜಾರಿಗೆ**: OAuth2 ಅಥವಾ ಕಸ್ಟಮ್ ಪ್ರಮಾಣೀಕರಣ ವಿಧಾನಗಳನ್ನು ಸೇರಿಸಿ
3. **ನಿರೀಕ್ಷಣೆ ಮತ್ತು ವಿಶ್ಲೇಷಣೆ**: ಉಪಕರಣ ಬಳಕೆಗೆ ಲಾಗ್ ಮತ್ತು ಮಾನಿಟರಿಂಗ್ ಜಾರಿಗೆ ತರಿಸಿ
4. **ನಿಮ್ಮ ಪರಿಹಾರವನ್ನು ವಿಸ್ತರಿಸಿ**: ಲೋಡ್ ಬ್ಯಾಲನ್ಸ್ ಮತ್ತು ವಿತರಿತ MCP ಸರ್ವರ್ ವಾಸ್ತುಶಿಲ್ಪಗಳನ್ನು ಪರಿಗಣಿಸಿ

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [Microsoft Foundry ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/azure/ai-foundry/)
- [ಮಾದರಿ ಪ್ರ ಸ್ಯ ಪ್ರೋಟೋಕಾಲ್ ಮಾದರிகள்](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry ಏಜೆಂಟ್‌ಗಳ ಅವಲೋಕನ](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP ನಿರ್ದಿಷ್ಟತೆ](https://modelcontextprotocol.io/specification/2026-07-28/)

## ಬೆಂಬಲ

ಹೆಚ್ಚುವರಿ ಬೆಂಬಲ ಮತ್ತು ಪ್ರಶ್ನೆಗಳಿಗಾಗಿ:
- [Microsoft Foundry ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/azure/ai-foundry/) ಪರಿಶೀಲಿಸಿ
- [MCP ಸಮುದಾಯ ಸಂಪನ್ಮೂಲಗಳು](https://modelcontextprotocol.io/) ಪರಿಶೀಲಿಸಿ

## ಮುಂದೇನು

- [5.14 MCP ಕಾಂಟೆಕ್ಸ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->