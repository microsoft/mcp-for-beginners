# Model Context Protocol (MCP) Integration with Microsoft Foundry

This guide demonstrates how to integrate Model Context Protocol (MCP) servers with Microsoft Foundry agents, enabling powerful tool orchestration and enterprise AI capabilities.

## Introduction

Model Context Protocol (MCP) is an open standard that enables AI applications to securely connect to external data sources and tools. When integrated with Microsoft Foundry, MCP allows agents to access and interact with various external services, APIs, and data sources in a standardized way.

This integration combines the flexibility of MCP's tool ecosystem with Microsoft Foundry's robust agent framework, providing enterprise-grade AI solutions with extensive customization capabilities.

> **Note:** If you want to use MCP in Microsoft Foundry Agent Service, currently only the following regions are supported: westus, westus2, uaenorth, southindia and switzerlandnorth

## Learning Objectives

By the end of this guide, you will be able to:

- Understand the Model Context Protocol and its benefits
- Set up MCP servers for use with Microsoft Foundry agents
- Create and configure agents with MCP tool integration
- Implement practical examples using real MCP servers
- Handle tool responses and citations in agent conversations

## Prerequisites

Before starting, ensure you have:

- An Azure subscription with Microsoft Foundry access
- Python 3.10+ or .NET 8.0+
- Azure CLI installed and configured
- Appropriate permissions to create AI resources

## What is Model Context Protocol (MCP)?

Model Context Protocol is a standardized way for AI applications to connect to external data sources and tools. Key benefits include:

- **Standardized Integration**: Consistent interface across different tools and services
- **Security**: Secure authentication and authorization mechanisms
- **Flexibility**: Support for various data sources, APIs, and custom tools
- **Extensibility**: Easy to add new capabilities and integrations

## Setting Up MCP with Microsoft Foundry

### Environment Configuration

Choose your preferred development environment:

- [Python Implementation](#python-implementation)
- [.NET Implementation](#net-implementation)

---

## Python Implementation

***Note*** You can run this [notebook](./mcp_support_python.ipynb)

The Python code uses `azure-ai-projects` 2.x. In this version, you create an agent with `project_client.agents.create_version(...)` and talk to it through the OpenAI-compatible Responses API (`project_client.get_openai_client()`). The 1.x `azure-ai-agents` API with `McpTool`, threads, runs, and `ToolApproval` is no longer used.

### 1. Install Required Packages

```bash
pip install "azure-ai-projects>=2.10.0,<3" "azure-identity>=1.27.0,<2" "openai>=3.44.0,<4"
```

The MCP server runs remotely and Foundry calls it for you, so you don't need the `mcp` package for this example.

### 2. Import Dependencies

```python
import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MCPTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from openai.types.responses.response_input_param import McpApprovalResponse, ResponseInputParam
```

### 3. Configure Project and MCP Settings

```python
project_endpoint = os.environ.get(
    "FOUNDRY_PROJECT_ENDPOINT",
    "https://your-resource.services.ai.azure.com/api/projects/your-project",
)
model_deployment_name = os.environ.get("FOUNDRY_MODEL_NAME", "Your model deployment name")
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Initialize Project Client

```python
credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint=project_endpoint, credential=credential)
```

### 5. Create MCP Tool

```python
mcp_tool = MCPTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    require_approval="always",  # Every MCP tool call waits for your approval
    # allowed_tools=["microsoft_docs_search"],  # Optional: restrict which MCP tools the agent may call
)
```

### 6. Complete Python Example

With `require_approval="always"`, the agent returns an `mcp_approval_request` item instead of calling the MCP server directly. You approve the request by sending an `mcp_approval_response` back in the same conversation:

```python
with project_client, project_client.get_openai_client() as openai_client:
    # Create (a new version of) the agent with the MCP tool
    agent = project_client.agents.create_version(
        agent_name="my-mcp-agent",
        definition=PromptAgentDefinition(
            model=model_deployment_name,
            instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
            tools=[mcp_tool],
        ),
    )
    print(f"Created agent {agent.name}, version {agent.version}")
    agent_reference = {"agent_reference": {"name": agent.name, "type": "agent_reference"}}

    try:
        # A conversation keeps the context across several responses
        conversation = openai_client.conversations.create()
        print(f"Created conversation, ID: {conversation.id}")

        response = openai_client.responses.create(
            conversation=conversation.id,
            input="What's the difference between Azure OpenAI and OpenAI?",
            extra_body=agent_reference,
        )

        # Approve MCP tool calls until the agent stops asking for approval
        while True:
            approvals: ResponseInputParam = []
            for item in response.output:
                if item.type == "mcp_approval_request" and item.server_label == mcp_server_label:
                    print(f"Approving MCP tool call: {item.name}({item.arguments})")
                    approvals.append(
                        McpApprovalResponse(
                            type="mcp_approval_response",
                            approve=True,
                            approval_request_id=item.id,
                        )
                    )
            if not approvals:
                break
            response = openai_client.responses.create(
                conversation=conversation.id,
                input=approvals,
                extra_body=agent_reference,
            )

        # Show which MCP tools the agent called
        for item in response.output:
            if item.type == "mcp_call":
                print(f"MCP call: {item.server_label}.{item.name} -> {'error' if item.error else 'ok'}")

        print("\nAgent response:")
        print("-" * 50)
        print(response.output_text)
    finally:
        # Clean up the agent version created by this notebook
        project_client.agents.delete_version(agent_name=agent.name, agent_version=agent.version)
        print("Deleted agent version")
```

---

## .NET Implementation

***Note*** You can run this [notebook](./mcp_support_dotnet.ipynb)

### 1. Install Required Packages

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Import Dependencies

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Configure Settings

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Create MCP Tool Definition

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Create Agent with MCP Tools

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Complete .NET Example

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

## MCP Tool Configuration Options

When configuring MCP tools for your agent, you can specify several important parameters:

### Python Configuration

```python
mcp_tool = MCPTool(
    server_label="unique_server_name",         # Identifier for the MCP server
    server_url="https://api.example.com/mcp",  # MCP server endpoint
    require_approval="always",                 # "always" or "never"
    allowed_tools=["tool_a", "tool_b"],        # Optional: restrict which tools can be used
)
```

### .NET Configuration

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Authentication and Headers

Both implementations support custom headers for authentication:

### Python

Pass static headers with `headers`. For secrets, prefer a project connection (`project_connection_id`), which stores the credentials in your Foundry project instead of in code:

```python
mcp_tool = MCPTool(
    server_label="unique_server_name",
    server_url="https://api.example.com/mcp",
    headers={"SuperSecret": "123456"},
    # project_connection_id="<your-connection-id>",
)
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Troubleshooting Common Issues

### 1. Connection Issues
- Verify MCP server URL is accessible
- Check authentication credentials
- Ensure network connectivity

### 2. Tool Call Failures
- Review tool arguments and formatting
- Check server-specific requirements
- Implement proper error handling

### 3. Performance Issues
- Optimize tool call frequency
- Implement caching where appropriate
- Monitor server response times

## Next Steps

To further enhance your MCP integration:

1. **Explore Custom MCP Servers**: Build your own MCP servers for proprietary data sources
2. **Implement Advanced Security**: Add OAuth2 or custom authentication mechanisms
3. **Monitor and Analytics**: Implement logging and monitoring for tool usage
4. **Scale Your Solution**: Consider load balancing and distributed MCP server architectures

## Additional Resources

- [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/)

## Support

For additional support and questions:
- Review the [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- Check the [MCP community resources](https://modelcontextprotocol.io/)

## What's next 

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)
