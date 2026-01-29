# ಮಾದರಿ ಸಂದರ್ಭ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಅನ್ನು Azure AI Foundry ಜೊತೆಗೆ ಏಕೀಕರಣ

ಈ ಮಾರ್ಗದರ್ಶಿ ಮಾದರಿ ಸಂದರ್ಭ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಸರ್ವರ್‌ಗಳನ್ನು Azure AI Foundry ಏಜೆಂಟ್‌ಗಳೊಂದಿಗೆ ಏಕೀಕರಿಸುವ ವಿಧಾನವನ್ನು ತೋರಿಸುತ್ತದೆ, ಶಕ್ತಿಶಾಲಿ ಉಪಕರಣ ಸಂಯೋಜನೆ ಮತ್ತು ಎಂಟರ್‌ಪ್ರೈಸ್ AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಮಾದರಿ ಸಂದರ್ಭ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಒಂದು ತೆರೆಯಲಾದ ಮಾನದಂಡವಾಗಿದೆ, ಇದು AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಬಾಹ್ಯ ಡೇಟಾ ಮೂಲಗಳು ಮತ್ತು ಉಪಕರಣಗಳಿಗೆ ಸುರಕ್ಷಿತವಾಗಿ ಸಂಪರ್ಕಿಸಲು ಅನುಮತಿಸುತ್ತದೆ. Azure AI Foundry ಜೊತೆಗೆ ಏಕೀಕರಿಸಿದಾಗ, MCP ಏಜೆಂಟ್‌ಗಳಿಗೆ ವಿವಿಧ ಬಾಹ್ಯ ಸೇವೆಗಳು, APIಗಳು ಮತ್ತು ಡೇಟಾ ಮೂಲಗಳೊಂದಿಗೆ ಮಾನದಂಡಿತ ರೀತಿಯಲ್ಲಿ ಪ್ರವೇಶ ಮತ್ತು ಸಂವಹನ ಮಾಡಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.

ಈ ಏಕೀಕರಣವು MCP ಉಪಕರಣ ಪರಿಸರದ ಲವಚಿಕತೆಯನ್ನು Azure AI Foundry ನ ಬಲವಾದ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಜೊತೆಗೆ ಸಂಯೋಜಿಸಿ, ವ್ಯಾಪಕ ಕಸ್ಟಮೈಜೆಷನ್ ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಎಂಟರ್‌ಪ್ರೈಸ್-ಗ್ರೇಡ್ AI ಪರಿಹಾರಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

**ಗಮನಿಸಿ:** ನೀವು Azure AI Foundry ಏಜೆಂಟ್ ಸೇವೆಯಲ್ಲಿ MCP ಬಳಸಲು ಬಯಸಿದರೆ, ಪ್ರಸ್ತುತ ಕೆಳಗಿನ ಪ್ರದೇಶಗಳು ಮಾತ್ರ ಬೆಂಬಲಿತವಾಗಿವೆ: westus, westus2, uaenorth, southindia ಮತ್ತು switzerlandnorth

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಮಾರ್ಗದರ್ಶಿಯ ಕೊನೆಯಲ್ಲಿ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- ಮಾದರಿ ಸಂದರ್ಭ ಪ್ರೋಟೋಕಾಲ್ ಮತ್ತು ಅದರ ಲಾಭಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- Azure AI Foundry ಏಜೆಂಟ್‌ಗಳೊಂದಿಗೆ ಬಳಸಲು MCP ಸರ್ವರ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸುವುದು
- MCP ಉಪಕರಣ ಏಕೀಕರಣದೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದು ಮತ್ತು ಸಂರಚಿಸುವುದು
- ನೈಜ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಬಳಸಿ ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳನ್ನು ಜಾರಿಗೆ ತರುವುದು
- ಏಜೆಂಟ್ ಸಂಭಾಷಣೆಗಳಲ್ಲಿ ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಮತ್ತು ಉಲ್ಲೇಖಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ನೀವು ಹೊಂದಿರಬೇಕು:

- AI Foundry ಪ್ರವೇಶದೊಂದಿಗೆ Azure ಚಂದಾದಾರಿಕೆ
- Python 3.10+ ಅಥವಾ .NET 8.0+
- Azure CLI ಸ್ಥಾಪಿತ ಮತ್ತು ಸಂರಚಿತ
- AI ಸಂಪನ್ಮೂಲಗಳನ್ನು ರಚಿಸಲು ಸೂಕ್ತ ಅನುಮತಿಗಳು

## ಮಾದರಿ ಸಂದರ್ಭ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಎಂದರೆ ಏನು?

ಮಾದರಿ ಸಂದರ್ಭ ಪ್ರೋಟೋಕಾಲ್ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಬಾಹ್ಯ ಡೇಟಾ ಮೂಲಗಳು ಮತ್ತು ಉಪಕರಣಗಳಿಗೆ ಸಂಪರ್ಕಿಸಲು ಮಾನದಂಡಿತ ವಿಧಾನವಾಗಿದೆ. ಪ್ರಮುಖ ಲಾಭಗಳು:

- **ಮಾನದಂಡಿತ ಏಕೀಕರಣ**: ವಿಭಿನ್ನ ಉಪಕರಣಗಳು ಮತ್ತು ಸೇವೆಗಳ ನಡುವೆ ಸತತ ಇಂಟರ್ಫೇಸ್
- **ಸುರಕ್ಷತೆ**: ಸುರಕ್ಷಿತ ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು ಅನುಮತಿ ಯಂತ್ರಗಳು
- **ಲವಚಿಕತೆ**: ವಿವಿಧ ಡೇಟಾ ಮೂಲಗಳು, APIಗಳು ಮತ್ತು ಕಸ್ಟಮ್ ಉಪಕರಣಗಳಿಗೆ ಬೆಂಬಲ
- **ವಿಸ್ತರಣೀಯತೆ**: ಹೊಸ ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಏಕೀಕರಣಗಳನ್ನು ಸುಲಭವಾಗಿ ಸೇರಿಸುವುದು

## Azure AI Foundry ಜೊತೆಗೆ MCP ಸ್ಥಾಪನೆ

### ಪರಿಸರ ಸಂರಚನೆ

ನಿಮ್ಮ ಇಚ್ಛಿತ ಅಭಿವೃದ್ಧಿ ಪರಿಸರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:

- [Python ಅನುಷ್ಠಾನ](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET ಅನುಷ್ಠಾನ](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python ಅನುಷ್ಠಾನ

***ಗಮನಿಸಿ*** ನೀವು ಈ [ನೋಟ್ಬುಕ್](./mcp_support_python.ipynb) ಅನ್ನು ಚಾಲನೆ ಮಾಡಬಹುದು

### 1. ಅಗತ್ಯ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

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

### 3. MCP ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಸಂರಚಿಸಿ

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. ಪ್ರಾಜೆಕ್ಟ್ ಕ್ಲೈಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ

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
    allowed_tools=[],  # ಐಚ್ಛಿಕ: ಅನುಮತಿಸಲಾದ ಸಾಧನಗಳನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಿ
)
```

### 6. ಪೂರ್ಣ Python ಉದಾಹರಣೆ

```python
with project_client:
    agents_client = project_client.agents

    # MCP ಸಾಧನಗಳೊಂದಿಗೆ ಹೊಸ ಏಜೆಂಟ್ ರಚಿಸಿ
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # ಸಂವಹನಕ್ಕಾಗಿ ಥ್ರೆಡ್ ರಚಿಸಿ
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # ಥ್ರೆಡ್‌ಗೆ ಸಂದೇಶ ರಚಿಸಿ
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # ಸಾಧನ ಅನುಮೋದನೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ ಮತ್ತು ಏಜೆಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ
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

***ಗಮನಿಸಿ*** ನೀವು ಈ [ನೋಟ್ಬುಕ್](./mcp_support_dotnet.ipynb) ಅನ್ನು ಚಾಲನೆ ಮಾಡಬಹುದು

### 1. ಅಗತ್ಯ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. ಅವಲಂಬನೆಗಳನ್ನು ಆಮದುಮಾಡಿ

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಸಂರಚಿಸಿ

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

### 6. ಪೂರ್ಣ .NET ಉದಾಹರಣೆ

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

ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗಾಗಿ MCP ಉಪಕರಣಗಳನ್ನು ಸಂರಚಿಸುವಾಗ, ನೀವು ಹಲವಾರು ಪ್ರಮುಖ ಪರಿಮಾಣಗಳನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಬಹುದು:

### Python ಸಂರಚನೆ

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP ಸರ್ವರ್‌ಗಾಗಿ ಗುರುತು
    server_url="https://api.example.com/mcp", # MCP ಸರ್ವರ್ ಎಂಡ್‌ಪಾಯಿಂಟ್
    allowed_tools=[],                       # ಐಚ್ಛಿಕ: ಅನುಮತಿಸಲಾದ ಸಾಧನಗಳನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಿ
)
```

### .NET ಸಂರಚನೆ

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು ಹೆಡರ್‌ಗಳು

ಎರಡೂ ಅನುಷ್ಠಾನಗಳು ಪ್ರಮಾಣೀಕರಣಕ್ಕಾಗಿ ಕಸ್ಟಮ್ ಹೆಡರ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ:

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
- MCP ಸರ್ವರ್ URL ಲಭ್ಯವಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
- ಪ್ರಮಾಣೀಕರಣ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
- ನೆಟ್‌ವರ್ಕ್ ಸಂಪರ್ಕವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ

### 2. ಉಪಕರಣ ಕರೆ ವಿಫಲತೆಗಳು
- ಉಪಕರಣದ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು ಮತ್ತು ಸ್ವರೂಪಣೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
- ಸರ್ವರ್-ನಿರ್ದಿಷ್ಟ ಅಗತ್ಯಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
- ಸರಿಯಾದ ದೋಷ ನಿರ್ವಹಣೆಯನ್ನು ಜಾರಿಗೆ ತರುವಿರಿ

### 3. ಕಾರ್ಯಕ್ಷಮತೆ ಸಮಸ್ಯೆಗಳು
- ಉಪಕರಣ ಕರೆಗಳ ಆವರ್ತನೆಯನ್ನು ಸುಧಾರಿಸಿ
- ಸೂಕ್ತ ಸ್ಥಳಗಳಲ್ಲಿ ಕ್ಯಾಶಿಂಗ್ ಜಾರಿಗೆ ತರುವಿರಿ
- ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯಗಳನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ

## ಮುಂದಿನ ಹಂತಗಳು

ನಿಮ್ಮ MCP ಏಕೀಕರಣವನ್ನು ಇನ್ನಷ್ಟು ಸುಧಾರಿಸಲು:

1. **ಕಸ್ಟಮ್ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ**: ಸ್ವಂತ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ ನಿಮ್ಮ ಸ್ವಂತ ಡೇಟಾ ಮೂಲಗಳಿಗೆ
2. **ಅಧಿಕ ಸುರಕ್ಷತೆ ಜಾರಿಗೆ ತರುವಿರಿ**: OAuth2 ಅಥವಾ ಕಸ್ಟಮ್ ಪ್ರಮಾಣೀಕರಣ ಯಂತ್ರಗಳನ್ನು ಸೇರಿಸಿ
3. **ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ವಿಶ್ಲೇಷಣೆ**: ಉಪಕರಣ ಬಳಕೆಗೆ ಲಾಗಿಂಗ್ ಮತ್ತು ಮೇಲ್ವಿಚಾರಣೆಯನ್ನು ಜಾರಿಗೆ ತರುವಿರಿ
4. **ನಿಮ್ಮ ಪರಿಹಾರವನ್ನು ವಿಸ್ತರಿಸಿ**: ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸಿಂಗ್ ಮತ್ತು ವಿತರಿತ MCP ಸರ್ವರ್ ವಾಸ್ತುಶಿಲ್ಪಗಳನ್ನು ಪರಿಗಣಿಸಿ

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [Azure AI Foundry ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/azure/ai-foundry/)
- [ಮಾದರಿ ಸಂದರ್ಭ ಪ್ರೋಟೋಕಾಲ್ ಮಾದರಿಗಳು](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry ಏಜೆಂಟ್‌ಗಳ ಅವಲೋಕನ](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP ವಿಶೇಷಣ](https://spec.modelcontextprotocol.io/)

## ಬೆಂಬಲ

ಹೆಚ್ಚಿನ ಬೆಂಬಲ ಮತ್ತು ಪ್ರಶ್ನೆಗಳಿಗೆ:
- [Azure AI Foundry ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/azure/ai-foundry/) ಪರಿಶೀಲಿಸಿ
- [MCP ಸಮುದಾಯ ಸಂಪನ್ಮೂಲಗಳು](https://modelcontextprotocol.io/) ಪರಿಶೀಲಿಸಿ

## ಮುಂದೇನು

- [5.14 MCP ಸಂದರ್ಭ ಎಂಜಿನಿಯರಿಂಗ್](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->