# 模型上下文协议（MCP）与 Microsoft Foundry 集成

本指南演示如何将模型上下文协议（MCP）服务器与 Microsoft Foundry 代理集成，实现强大的工具编排和企业级 AI 功能。

## 介绍

模型上下文协议（MCP）是一种开放标准，使 AI 应用能够安全地连接到外部数据源和工具。与 Microsoft Foundry 集成时，MCP 允许代理以标准化方式访问和交互各种外部服务、API 和数据源。

此集成将 MCP 灵活的工具生态系统与 Microsoft Foundry 强大的代理框架结合，提供具备广泛定制能力的企业级 AI 解决方案。

**注意：** 如果您想在 Microsoft Foundry 代理服务中使用 MCP，目前仅支持以下区域：westus、westus2、uaenorth、southindia 和 switzerlandnorth

## 学习目标

完成本指南后，您将能够：

- 了解模型上下文协议及其优势
- 设置 MCP 服务器以供 Microsoft Foundry 代理使用
- 创建并配置集成 MCP 工具的代理
- 使用真实 MCP 服务器实现实际示例
- 处理代理对话中的工具响应和引用

## 前提条件

开始之前，请确保您：

- 拥有包含 Microsoft Foundry 访问权限的 Azure 订阅
- 安装 Python 3.10+ 或 .NET 8.0+
- 安装并配置 Azure CLI
- 具备创建 AI 资源的适当权限

## 什么是模型上下文协议（MCP）？

模型上下文协议是一种标准化方式，使 AI 应用程序能够连接外部数据源和工具。主要优势包括：

- <strong>标准化集成</strong>：跨不同工具和服务提供一致接口
- <strong>安全性</strong>：安全的身份验证和授权机制
- <strong>灵活性</strong>：支持各种数据源、API 和自定义工具
- <strong>可扩展性</strong>：易于添加新功能和集成

## 与 Microsoft Foundry 配置 MCP 

### 环境配置

请选择您偏好的开发环境：

- [Python 实现](#python-实现)
- [.NET 实现](#codeblock5)

---

## Python 实现

<strong><em>注意</em></strong> 您可以运行此[笔记本](./mcp_support_python.ipynb)

### 1. 安装所需包

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. 导入依赖

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. 配置 MCP 设置

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. 初始化项目客户端

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. 创建 MCP 工具

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # 可选：指定允许的工具
)
```

### 6. 完整 Python 示例

```python
with project_client:
    agents_client = project_client.agents

    # 使用MCP工具创建一个新代理
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # 创建用于通信的线程
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # 创建发送给线程的消息
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # 处理工具批准并运行代理
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

    # 显示对话
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

## .NET 实现

<strong><em>注意</em></strong> 您可以运行此[笔记本](./mcp_support_dotnet.ipynb)

### 1. 安装所需包

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. 导入依赖

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. 配置设置

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. 创建 MCP 工具定义

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. 使用 MCP 工具创建代理

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. 完整 .NET 示例

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

## MCP 工具配置选项

配置代理的 MCP 工具时，您可以指定若干重要参数：

### Python 配置

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP 服务器的标识符
    server_url="https://api.example.com/mcp", # MCP 服务器端点
    allowed_tools=[],                       # 可选：指定允许的工具
)
```

### .NET 配置

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## 认证与请求头

两种实现均支持自定义请求头用于认证：

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## 常见问题排查

### 1. 连接问题
- 验证 MCP 服务器 URL 可访问
- 检查认证凭据
- 确保网络连接正常

### 2. 工具调用失败
- 检查工具参数和格式
- 确认服务器特定要求
- 实施恰当的错误处理

### 3. 性能问题
- 优化工具调用频率
- 适当实现缓存
- 监控服务器响应时间

## 后续步骤

进一步增强您的 MCP 集成：

1. **探索自定义 MCP 服务器**：为专有数据源构建自己的 MCP 服务器
2. <strong>实现高级安全</strong>：添加 OAuth2 或自定义认证机制
3. <strong>监控与分析</strong>：实现工具使用的日志记录和监测
4. <strong>扩展您的解决方案</strong>：考虑负载均衡和分布式 MCP 服务器架构

## 额外资源

- [Microsoft Foundry 文档](https://learn.microsoft.com/azure/ai-foundry/)
- [模型上下文协议示例](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry 代理概述](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP 规范](https://modelcontextprotocol.io/specification/2026-07-28/)

## 支持

如需更多支持和问题解答：
- 查阅 [Microsoft Foundry 文档](https://learn.microsoft.com/azure/ai-foundry/)
- 访问 [MCP 社区资源](https://modelcontextprotocol.io/)

## 下一步

- [5.14 MCP 上下文工程](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->