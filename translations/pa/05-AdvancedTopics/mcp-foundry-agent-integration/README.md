# ਮਾਡਲ ਸੰਦੇਸ਼ ਪ੍ਰੋਟੋਕਾਲ (MCP) ਦਾ Microsoft Foundry ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਇਹ ਗਾਈਡ ਦਰਸਾਉਂਦੀ ਹੈ ਕਿ ਕਿਵੇਂ ਮਾਡਲ ਸੰਦੇਸ਼ ਪ੍ਰੋਟੋਕਾਲ (MCP) ਸਰਵਰਾਂ ਨੂੰ Microsoft Foundry ਏਜੰਟਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ ਹੈ, ਜੋ ਸ਼ਕਤੀਸ਼ਾਲੀ ਟੂਲ ਆਰਕੇਸਟਰੈਸ਼ਨ ਅਤੇ ਉਦਯੋਗਿਕ AI ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ।

## ਪਰਿਚਯ

ਮਾਡਲ ਸੰਦੇਸ਼ ਪ੍ਰੋਟੋਕਾਲ (MCP) ਇੱਕ ਖੁੱਲ੍ਹਾ ਮਾਪਦੰਡ ਹੈ ਜੋ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬਾਹਰੀ ਡਾਟਾ ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਜੁੜਨ ਦੇਣ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਜਦੋਂ Microsoft Foundry ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਤਾਂ MCP ਏਜੰਟਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਬਾਹਰੀ ਸੇਵਾਵਾਂ, API ਅਤੇ ਡਾਟਾ ਸਰੋਤਾਂ ਤੱਕ ਪਹੁੰਚ ਅਤੇ ਪਰਸਪਰਕਿਰਿਆ ਕਰਨ ਦੀ ਸਹੂਲਤ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

ਇਹ ਇੰਟੀਗ੍ਰੇਸ਼ਨ MCP ਦੇ ਟੂਲ ਇੱਕੋਸਿਸਟਮ ਦੀ ਲਚਕੀਲਾਪਣ ਨੂੰ Microsoft Foundry ਦੇ ਮਜ਼ਬੂਤ ਏਜੰਟ ਫਰੇਮਵਰਕ ਨਾਲ ਜੋੜਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਉਦਯੋਗ-ਗਰੇਡ AI ਹੱਲ ਅਤੇ ਵਿਸ਼ਤ੍ਰਿਤ ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ ਸਮਰੱਥਾਵਾਂ ਮਿਲਦੀਆਂ ਹਨ।

**ਨੋਟ:** ਜੇ ਤੁਸੀਂ Microsoft Foundry ਏਜੰਟ ਸਰਵਿਸ ਵਿੱਚ MCP ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਹਾਲੇ ਸਿਰਫ਼ ਇਹਨਾਂ ਖੇਤਰਾਂ ਨੂੰ ਸਮਰਥਨ ਮਿਲਦਾ ਹੈ: westus, westus2, uaenorth, southindia ਅਤੇ switzerlandnorth

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਗਾਈਡ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਮਾਡਲ ਸੰਦੇਸ਼ ਪ੍ਰੋਟੋਕਾਲ ਅਤੇ ਇਸਦੇ ਫਾਇਦਿਆਂ ਨੂੰ ਸਮਝਣਾ
- Microsoft Foundry ਏਜੰਟਾਂ ਲਈ MCP ਸਰਵਰ ਸੈਟ ਅੱਪ ਕਰਨਾ
- MCP ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨਾਲ ਏਜੰਟ ਬਣਾਉਣਾ ਅਤੇ ਸੰਰਚਨਾ ਕਰਨਾ
- ਅਸਲੀ MCP ਸਰਵਰਾਂ ਦਾ ਉਪਯੋਗ ਕਰਕੇ ਵਿਆਵਹਾਰਿਕ ਉਦਾਹਰਨਾਂ ਲਾਗੂ ਕਰਨਾ
- ਏਜੰਟ ਗੱਲਬਾਤਾਂ ਵਿੱਚ ਟੂਲ ਜਵਾਬ ਅਤੇ ਸਰੋਤ ਹਵਾਲਿਆਂ ਨਾਲ ਨਿਪਟਣਾ

## ਲੋੜੀਂਦੇ ਪੂਰਵ-ਸ਼ਰਤਾਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੈ:

- ਇੱਕ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਜਿਸ ਵਿੱਚ Microsoft Foundry ਦੀ ਪਹੁੰਚ ਹੈ
- Python 3.10+ ਜਾਂ .NET 8.0+
- Azure CLI ਇੰਸਟਾਲ ਅਤੇ ਕੰਫਿਗਰ ਕੀਤੀ ਹੋਈ ਹੈ
- AI ਸਰੋਤ ਬਣਾਉਣ ਲਈ ਉਚਿਤ ਅਧਿਕਾਰ

## ਮਾਡਲ ਸੰਦੇਸ਼ ਪ੍ਰੋਟੋਕਾਲ (MCP) ਕੀ ਹੈ?

ਮਾਡਲ ਸੰਦੇਸ਼ ਪ੍ਰੋਟੋਕਾਲ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਬਾਹਰੀ ਡਾਟਾ ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਜੁੜਨ ਦਾ ਇੱਕ ਮਾਪਦੰਡ ਤਰੀਕਾ ਹੈ। ਮੁੱਖ ਫਾਇਦੇ ਇਹ ਹਨ:

- **ਮਿਆਰੀਕ੍ਰਿਤ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਲਈ ਸਥਿਰ ਇੰਟਰਫੇਸ
- **ਸੁਰੱਖਿਆ**: ਸੁਰੱਖਿਅਤ ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਅਧਿਕਾਰਣ ਪ੍ਰਣਾਲੀਆਂ
- **ਲਚਕੀਲਾਪਣ**: ਵੱਖ-ਵੱਖ ਡਾਟਾ ਸਰੋਤਾਂ, API ਅਤੇ ਕਸਟਮ ਟੂਲਾਂ ਲਈ ਸਹਿਯੋਗ
- **ਵਧਾਉਣਯੋਗਤਾ**: ਨਵੀਆਂ ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਜੋੜਨਾ

## Microsoft Foundry ਨਾਲ MCP ਸੈਟਅੱਪ ਕਰਨਾ

### ਮਹੌਲ ਸੰਰਚਨਾ

ਆਪਣੀ ਮਨਪਸੰਦ ਵਿਕਾਸ ਮਹੌਲ ਦੀ ਚੋਣ ਕਰੋ:

- [Python Implementation](#python-implementation)
- [.NET Implementation](#codeblock5)

---

## Python Implementation

***ਨੋਟ*** ਤੁਸੀਂ ਇਹ [ਨੋਟਬੁੱਕ](./mcp_support_python.ipynb) ਚਲਾ ਸਕਦੇ ਹੋ

### 1. ਜ਼ਰੂਰੀ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. ਡਿਪੈਂਡੰਸੀਆਂ ਆਮਦਨ ਕਰੋ

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP ਸੈਟਿੰਗਜ਼ ਕੰਫਿਗਰ ਕਰੋ

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. ਪ੍ਰੋਜੈਕਟ ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕਰੋ

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP ਟੂਲ ਬਣਾਓ

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # ਵਿਕਲਪੀ: ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਤਕਨੀਕਾਂ ਦਰਜ ਕਰੋ
)
```

### 6. ਪੂਰਾ Python ਉਦਾਹਰਨ

```python
with project_client:
    agents_client = project_client.agents

    # MCP ਟੂਲਾਂ ਨਾਲ ਨਵਾਂ ਏਜੰਟ ਬਣਾਓ
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # ਸੰਚਾਰ ਲਈ ਤਾਰ ਬਣਾਓ
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # ਤਾਰ ਲਈ ਸੁਨੇਹਾ ਬਣਾਓ
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # ਟੂਲ ਮਨਜ਼ੂਰੀਆਂ ਨੂੰ ਸੰਭਾਲੋ ਅਤੇ ਏਜੰਟ ਚਲਾਓ
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

    # ਗੱਲਬਾਤ ਦਿਖਾਓ
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

***ਨੋਟ*** ਤੁਸੀਂ ਇਹ [ਨੋਟਬੁੱਕ](./mcp_support_dotnet.ipynb) ਚਲਾ ਸਕਦੇ ਹੋ

### 1. ਜ਼ਰੂਰੀ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. ਡਿਪੈਂਡੰਸੀਆਂ ਆਮਦਨ ਕਰੋ

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. ਸੈਟਿੰਗਜ਼ ਕੰਫਿਗਰ ਕਰੋ

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP ਟੂਲ ਪਰਿਭਾਸ਼ਾ ਬਣਾਓ

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP ਟੂਲਾਂ ਨਾਲ ਏਜੰਟ ਬਣਾਓ

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. ਪੂਰਾ .NET ਉਦਾਹਰਨ

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

## MCP ਟੂਲ ਸੰਰਚਨਾ ਵਿਕਲਪ

ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ ਏਜੰਟ ਲਈ MCP ਟੂਲਾਂ ਨੂੰ ਸੰਰਚਿਤ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਕਈ ਮਹੱਤਵਪੂਰਨ ਪੈਰਾਮੀਟਰ ਨਿਰਧਾਰਤ ਕਰ ਸਕਦੇ ਹੋ:

### Python ਸੰਰਚਨਾ

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP ਸਰਵਰ ਲਈ ਪਹਚਾਣਿਕਤਾ
    server_url="https://api.example.com/mcp", # MCP ਸਰਵਰ ਐਂਡਪਾਇੰਟ
    allowed_tools=[],                       # ਵਿਕਲਪਕ: ਇਜਾਜ਼ਤ ਦੱਤੇ ਗਏ ਟੂਲ ਹਦਾਇਤ ਕਰੋ
)
```

### .NET ਸੰਰਚਨਾ

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਹੈਡਰਜ਼

ਦੋਹਾਂ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਵਿੱਚ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ ਕਸਟਮ ਹੈਡਰਜ਼ ਦਾ ਸਮਰਥਨ ਹੈ:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## ਆਮ ਸਮੱਸਿਆਵਾਂ ਲਈ ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ

### 1. ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ
- MCP ਸਰਵਰ URL ਦੀ ਪਹੁੰਚਯੋਗਤਾ ਦੀ ਜਾਂਚ ਕਰੋ
- ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਮਾਣਪੱਤਰ ਚੈੱਕ ਕਰੋ
- ਨੈੱਟਵਰਕ ਕੁਨੈਕਟਿਵਿਟੀ ਯਕੀਨੀ ਬਣਾਓ

### 2. ਟੂਲ ਕਾਲ ਫੇਲਯੁਰਜ਼
- ਟੂਲ ਆਰਗੁਮੈਂਟ ਅਤੇ ਫਾਰਮੈਟਿੰਗ ਦੀ ਸਮੀਖਿਆ ਕਰੋ
- ਸਰਵਰ-ਖ਼ਾਸ ਲੋੜਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
- ਢੰਗ ਨਾਲ ਗਲਤੀ ਸੰਭਾਲ ਲਾਗੂ ਕਰੋ

### 3. ਕਾਰਗੁਜ਼ਾਰੀ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ
- ਟੂਲ ਕਾਲ ਦੀ ਆਵ੍ਰਿਤੀ ਨੂੰ ਅਨੁਕੂਲ ਕਰੋ
- ਜਿੱਥੇ ਠੀਕ ਹੋਵੇ ਕੈਸ਼ਿੰਗ ਲਾਗੂ ਕਰੋ
- ਸਰਵਰ ਜਵਾਬ ਸਮਿਆਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ

## ਅੱਗੇ ਦੇ ਕਦਮ

ਆਪਣੀ MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਹੋਰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ:

1. **ਕਸਟਮ MCP ਸਰਵਰ ਖੋਜੋ**: ਆਪਣੀ ਖਾਸ ਡਾਟਾ ਸਰੋਤਾਂ ਲਈ MCP ਸਰਵਰ ਬਣਾਓ
2. **ਉੱਚ ਸੁਰੱਖਿਆ ਲਾਗੂ ਕਰੋ**: OAuth2 ਜਾਂ ਕਸਟਮ ਪ੍ਰਮਾਣੀਕਰਨ ਮਕੈਨਿਜ਼ਮ ਸ਼ਾਮਲ ਕਰੋ
3. **ਮਾਨੀਟਰਿੰਗ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ**: ਟੂਲ ਵਰਤੋਂ ਲਈ ਲੋਗਿੰਗ ਅਤੇ ਮਾਨੀਟਰਿੰਗ ਲਾਗੂ ਕਰੋ
4. **ਆਪਣੇ ਹੱਲ ਨੂੰ ਵੱਡਾ ਕਰੋ**: ਲੋਡ ਬੈਲੈਂਸਿੰਗ ਅਤੇ ਵੰਡੇ MCP ਸਰਵਰ ਆਰਕੀਟੈਕਚਰਾਂ ਬਾਰੇ ਸੋਚੋ

## ਵਾਧੂ ਸਰੋਤ

- [Microsoft Foundry ਦਸਤਾਵੇਜ਼ੀकरण](https://learn.microsoft.com/azure/ai-foundry/)
- [ਮਾਡਲ ਸੰਦੇਸ਼ ਪ੍ਰੋਟੋਕਾਲ ਨਮੂਨੇ](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry ਏਜੰਟ ਪੂਰਵ-ਦ੍ਰਿਸ਼ਟੀ](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP ਸਪੈਸੀਫਿਕੇਸ਼ਨ](https://modelcontextprotocol.io/specification/2026-07-28/)

## ਸਹਾਇਤਾ

ਵਾਧੂ ਸਹਾਇਤਾ ਅਤੇ ਸਵਾਲਾਂ ਲਈ:
- [Microsoft Foundry ਦਸਤਾਵੇਜ਼ੀ』ਖੋ](https://learn.microsoft.com/azure/ai-foundry/)
- [MCP ਸਮੁਦਾਇ ਸਰੋਤਾਂ ਦਾ ਜਾਇਜ਼ਾ ਲਓ](https://modelcontextprotocol.io/)

## ਅਗਲਾ ਕੀ ਹੈ

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->