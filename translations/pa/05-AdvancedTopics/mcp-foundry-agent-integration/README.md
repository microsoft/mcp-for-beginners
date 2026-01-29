# Model Context Protocol (MCP) ਦਾ Azure AI Foundry ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਇਹ ਗਾਈਡ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ ਕਿਵੇਂ Model Context Protocol (MCP) ਸਰਵਰਾਂ ਨੂੰ Azure AI Foundry ਏਜੰਟਾਂ ਨਾਲ ਜੋੜਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਸ਼ਕਤੀਸ਼ਾਲੀ ਟੂਲ ਆਰਕੀਸਟ੍ਰੇਸ਼ਨ ਅਤੇ ਉਦਯੋਗਿਕ AI ਸਮਰੱਥਾਵਾਂ ਮਿਲਦੀਆਂ ਹਨ।

## ਜਾਣ ਪਹਿਚਾਣ

Model Context Protocol (MCP) ਇੱਕ ਖੁੱਲ੍ਹਾ ਮਿਆਰੀਕ੍ਰਿਤ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬਾਹਰੀ ਡਾਟਾ ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਜੁੜਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਜਦੋਂ ਇਸਨੂੰ Azure AI Foundry ਨਾਲ ਜੋੜਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ MCP ਏਜੰਟਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਬਾਹਰੀ ਸੇਵਾਵਾਂ, APIs ਅਤੇ ਡਾਟਾ ਸਰੋਤਾਂ ਤੱਕ ਪਹੁੰਚ ਅਤੇ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

ਇਹ ਇੰਟੀਗ੍ਰੇਸ਼ਨ MCP ਦੇ ਟੂਲ ਇਕੋਸਿਸਟਮ ਦੀ ਲਚਕੀਲਾਪਣ ਨੂੰ Azure AI Foundry ਦੇ ਮਜ਼ਬੂਤ ਏਜੰਟ ਫਰੇਮਵਰਕ ਨਾਲ ਮਿਲਾ ਕੇ ਉਦਯੋਗਿਕ ਪੱਧਰ ਦੇ AI ਹੱਲ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਵਿਆਪਕ ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ ਸਮਰੱਥਾਵਾਂ ਹਨ।

**Note:** ਜੇ ਤੁਸੀਂ MCP ਨੂੰ Azure AI Foundry Agent Service ਵਿੱਚ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਇਸ ਸਮੇਂ ਸਿਰਫ ਹੇਠਾਂ ਦਿੱਤੇ ਖੇਤਰਾਂ ਨੂੰ ਸਹਿਯੋਗ ਮਿਲਦਾ ਹੈ: westus, westus2, uaenorth, southindia ਅਤੇ switzerlandnorth

## ਸਿੱਖਣ ਦੇ ਲਕੜੀ

ਇਸ ਗਾਈਡ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- Model Context Protocol ਅਤੇ ਇਸਦੇ ਫਾਇਦੇ ਸਮਝਣਾ
- Azure AI Foundry ਏਜੰਟਾਂ ਲਈ MCP ਸਰਵਰ ਸੈੱਟਅਪ ਕਰਨਾ
- MCP ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨਾਲ ਏਜੰਟ ਬਣਾਉਣਾ ਅਤੇ ਸੰਰਚਿਤ ਕਰਨਾ
- ਅਸਲੀ MCP ਸਰਵਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਯੋਗਿਕ ਉਦਾਹਰਣ ਲਾਗੂ ਕਰਨਾ
- ਏਜੰਟ ਗੱਲਬਾਤਾਂ ਵਿੱਚ ਟੂਲ ਜਵਾਬਾਂ ਅਤੇ ਹਵਾਲਿਆਂ ਨੂੰ ਸੰਭਾਲਣਾ

## ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੈ:

- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਜਿਸ ਵਿੱਚ AI Foundry ਦੀ ਪਹੁੰਚ ਹੈ
- Python 3.10+ ਜਾਂ .NET 8.0+
- Azure CLI ਇੰਸਟਾਲ ਅਤੇ ਸੰਰਚਿਤ
- AI ਸਰੋਤ ਬਣਾਉਣ ਲਈ ਉਚਿਤ ਅਧਿਕਾਰ

## Model Context Protocol (MCP) ਕੀ ਹੈ?

Model Context Protocol AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਬਾਹਰੀ ਡਾਟਾ ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਜੁੜਨ ਦਾ ਇੱਕ ਮਿਆਰੀਕ੍ਰਿਤ ਤਰੀਕਾ ਹੈ। ਮੁੱਖ ਫਾਇਦੇ ਹਨ:

- **ਮਿਆਰੀਕ੍ਰਿਤ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਲਈ ਇੱਕਸਾਰ ਇੰਟਰਫੇਸ
- **ਸੁਰੱਖਿਆ**: ਸੁਰੱਖਿਅਤ ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਅਧਿਕਾਰ ਪ੍ਰਣਾਲੀਆਂ
- **ਲਚਕੀਲਾਪਣ**: ਵੱਖ-ਵੱਖ ਡਾਟਾ ਸਰੋਤਾਂ, APIs ਅਤੇ ਕਸਟਮ ਟੂਲਾਂ ਲਈ ਸਹਿਯੋਗ
- **ਵਿਸਤਾਰਯੋਗਤਾ**: ਨਵੀਆਂ ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਸਮਰੱਥਾ

## Azure AI Foundry ਨਾਲ MCP ਸੈੱਟਅਪ ਕਰਨਾ

### ਵਾਤਾਵਰਣ ਸੰਰਚਨਾ

ਆਪਣੇ ਮਨਪਸੰਦ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਦੀ ਚੋਣ ਕਰੋ:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** ਤੁਸੀਂ ਇਹ [notebook](mcp_support_python.ipynb) ਚਲਾ ਸਕਦੇ ਹੋ

### 1. ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Dependencies ਇੰਪੋਰਟ ਕਰੋ

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP ਸੈਟਿੰਗਜ਼ ਸੰਰਚਿਤ ਕਰੋ

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
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. ਪੂਰਾ Python ਉਦਾਹਰਣ

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

***Note*** ਤੁਸੀਂ ਇਹ [notebook](mcp_support_dotnet.ipynb) ਚਲਾ ਸਕਦੇ ਹੋ

### 1. ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Dependencies ਇੰਪੋਰਟ ਕਰੋ

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. ਸੈਟਿੰਗਜ਼ ਸੰਰਚਿਤ ਕਰੋ

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP ਟੂਲ ਡਿਫਿਨੀਸ਼ਨ ਬਣਾਓ

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

### 6. ਪੂਰਾ .NET ਉਦਾਹਰਣ

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

ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ ਏਜੰਟ ਲਈ MCP ਟੂਲ ਸੰਰਚਿਤ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਕਈ ਮਹੱਤਵਪੂਰਨ ਪੈਰਾਮੀਟਰ ਨਿਰਧਾਰਤ ਕਰ ਸਕਦੇ ਹੋ:

### Python ਸੰਰਚਨਾ

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET ਸੰਰਚਨਾ

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਹੈਡਰ

ਦੋਹਾਂ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਕਸਟਮ ਹੈਡਰਾਂ ਦਾ ਸਹਿਯੋਗ ਹੈ:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## ਆਮ ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ

### 1. ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ
- MCP ਸਰਵਰ URL ਦੀ ਪਹੁੰਚ ਯਕੀਨੀ ਬਣਾਓ
- ਪ੍ਰਮਾਣਿਕਤਾ ਦੇ ਕ੍ਰੈਡੈਂਸ਼ਲ ਚੈੱਕ ਕਰੋ
- ਨੈੱਟਵਰਕ ਕਨੈਕਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ

### 2. ਟੂਲ ਕਾਲ ਫੇਲ੍ਹ ਹੋਣਾ
- ਟੂਲ ਦੇ ਆਰਗੁਮੈਂਟ ਅਤੇ ਫਾਰਮੈਟਿੰਗ ਦੀ ਸਮੀਖਿਆ ਕਰੋ
- ਸਰਵਰ-ਵਿਸ਼ੇਸ਼ ਲੋੜਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
- ਠੀਕ ਤਰੀਕੇ ਨਾਲ ਐਰਰ ਹੈਂਡਲਿੰਗ ਲਾਗੂ ਕਰੋ

### 3. ਪ੍ਰਦਰਸ਼ਨ ਸਮੱਸਿਆਵਾਂ
- ਟੂਲ ਕਾਲ ਦੀ ਫ੍ਰਿਕਵੈਂਸੀ ਨੂੰ ਅਪਟੀਮਾਈਜ਼ ਕਰੋ
- ਜਿੱਥੇ ਲੋੜ ਹੋਵੇ ਕੈਸ਼ਿੰਗ ਲਾਗੂ ਕਰੋ
- ਸਰਵਰ ਜਵਾਬ ਸਮੇਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ

## ਅਗਲੇ ਕਦਮ

ਆਪਣੇ MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਹੋਰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ:

1. **ਕਸਟਮ MCP ਸਰਵਰ ਬਣਾਓ**: ਆਪਣੇ ਖਾਸ ਡਾਟਾ ਸਰੋਤਾਂ ਲਈ MCP ਸਰਵਰ ਤਿਆਰ ਕਰੋ
2. **ਉੱਚ ਸੁਰੱਖਿਆ ਲਾਗੂ ਕਰੋ**: OAuth2 ਜਾਂ ਕਸਟਮ ਪ੍ਰਮਾਣਿਕਤਾ ਪ੍ਰਣਾਲੀਆਂ ਸ਼ਾਮਲ ਕਰੋ
3. **ਮਾਨੀਟਰਿੰਗ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ**: ਟੂਲ ਦੀ ਵਰਤੋਂ ਲਈ ਲੌਗਿੰਗ ਅਤੇ ਮਾਨੀਟਰਿੰਗ ਲਾਗੂ ਕਰੋ
4. **ਆਪਣੇ ਹੱਲ ਨੂੰ ਸਕੇਲ ਕਰੋ**: ਲੋਡ ਬੈਲੈਂਸਿੰਗ ਅਤੇ ਵੰਡੇ MCP ਸਰਵਰ ਆਰਕੀਟੈਕਚਰਾਂ ਬਾਰੇ ਸੋਚੋ

## ਵਾਧੂ ਸਰੋਤ

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## ਸਹਾਇਤਾ

ਵਾਧੂ ਸਹਾਇਤਾ ਅਤੇ ਸਵਾਲਾਂ ਲਈ:
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/) ਨੂੰ ਵੇਖੋ
- [MCP community resources](https://modelcontextprotocol.io/) ਦੀ ਜਾਂਚ ਕਰੋ

## ਅਗਲਾ ਕੀ ਹੈ

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।