# Model Context Protocol (MCP) Tích hợp với Azure AI Foundry

Hướng dẫn này trình bày cách tích hợp các máy chủ Model Context Protocol (MCP) với các agent của Azure AI Foundry, giúp điều phối công cụ mạnh mẽ và khả năng AI doanh nghiệp.

## Giới thiệu

Model Context Protocol (MCP) là một tiêu chuẩn mở cho phép các ứng dụng AI kết nối an toàn với các nguồn dữ liệu và công cụ bên ngoài. Khi tích hợp với Azure AI Foundry, MCP cho phép các agent truy cập và tương tác với nhiều dịch vụ, API và nguồn dữ liệu bên ngoài theo một cách chuẩn hóa.

Sự tích hợp này kết hợp sự linh hoạt của hệ sinh thái công cụ MCP với khung agent mạnh mẽ của Azure AI Foundry, cung cấp các giải pháp AI cấp doanh nghiệp với khả năng tùy chỉnh rộng rãi.

**Note:** Nếu bạn muốn sử dụng MCP trong Azure AI Foundry Agent Service, hiện tại chỉ hỗ trợ các khu vực sau: westus, westus2, uaenorth, southindia và switzerlandnorth

## Mục tiêu học tập

Sau khi hoàn thành hướng dẫn này, bạn sẽ có thể:

- Hiểu về Model Context Protocol và lợi ích của nó
- Thiết lập các máy chủ MCP để sử dụng với các agent Azure AI Foundry
- Tạo và cấu hình agent với tích hợp công cụ MCP
- Triển khai các ví dụ thực tế sử dụng các máy chủ MCP thật
- Xử lý phản hồi công cụ và trích dẫn trong các cuộc hội thoại của agent

## Yêu cầu trước

Trước khi bắt đầu, hãy đảm bảo bạn có:

- Một đăng ký Azure với quyền truy cập AI Foundry
- Python 3.10+ hoặc .NET 8.0+
- Azure CLI đã được cài đặt và cấu hình
- Quyền phù hợp để tạo tài nguyên AI

## Model Context Protocol (MCP) là gì?

Model Context Protocol là một phương thức chuẩn hóa để các ứng dụng AI kết nối với các nguồn dữ liệu và công cụ bên ngoài. Các lợi ích chính bao gồm:

- **Tích hợp chuẩn hóa**: Giao diện nhất quán giữa các công cụ và dịch vụ khác nhau
- **Bảo mật**: Cơ chế xác thực và ủy quyền an toàn
- **Linh hoạt**: Hỗ trợ nhiều nguồn dữ liệu, API và công cụ tùy chỉnh
- **Mở rộng**: Dễ dàng thêm các tính năng và tích hợp mới

## Thiết lập MCP với Azure AI Foundry

### Cấu hình môi trường

Chọn môi trường phát triển bạn ưa thích:

- [Triển khai Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Triển khai .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Triển khai Python

***Note*** Bạn có thể chạy [notebook này](mcp_support_python.ipynb)

### 1. Cài đặt các gói cần thiết

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Nhập các thư viện phụ thuộc

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Cấu hình các thiết lập MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Khởi tạo Project Client

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Tạo công cụ MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Ví dụ hoàn chỉnh bằng Python

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

## Triển khai .NET

***Note*** Bạn có thể chạy [notebook này](mcp_support_dotnet.ipynb)

### 1. Cài đặt các gói cần thiết

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Nhập các thư viện phụ thuộc

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Cấu hình các thiết lập

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Tạo định nghĩa công cụ MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Tạo agent với các công cụ MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Ví dụ hoàn chỉnh bằng .NET

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

## Tùy chọn cấu hình công cụ MCP

Khi cấu hình các công cụ MCP cho agent của bạn, bạn có thể chỉ định một số tham số quan trọng:

### Cấu hình Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Cấu hình .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Xác thực và Headers

Cả hai triển khai đều hỗ trợ headers tùy chỉnh cho xác thực:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Khắc phục sự cố phổ biến

### 1. Vấn đề kết nối
- Kiểm tra URL máy chủ MCP có thể truy cập được không
- Xác minh thông tin xác thực
- Đảm bảo kết nối mạng ổn định

### 2. Lỗi gọi công cụ
- Kiểm tra các tham số và định dạng của công cụ
- Xem xét các yêu cầu riêng của máy chủ
- Thực hiện xử lý lỗi phù hợp

### 3. Vấn đề hiệu năng
- Tối ưu tần suất gọi công cụ
- Áp dụng bộ nhớ đệm khi cần thiết
- Giám sát thời gian phản hồi của máy chủ

## Bước tiếp theo

Để nâng cao tích hợp MCP của bạn:

1. **Khám phá các máy chủ MCP tùy chỉnh**: Xây dựng máy chủ MCP riêng cho các nguồn dữ liệu độc quyền
2. **Triển khai bảo mật nâng cao**: Thêm OAuth2 hoặc các cơ chế xác thực tùy chỉnh
3. **Giám sát và phân tích**: Thực hiện ghi nhật ký và giám sát việc sử dụng công cụ
4. **Mở rộng giải pháp**: Xem xét cân bằng tải và kiến trúc máy chủ MCP phân tán

## Tài nguyên bổ sung

- [Tài liệu Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Mẫu Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Tổng quan về Azure AI Foundry Agents](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Đặc tả MCP](https://spec.modelcontextprotocol.io/)

## Hỗ trợ

Để được hỗ trợ thêm và giải đáp thắc mắc:
- Xem lại [tài liệu Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Kiểm tra [tài nguyên cộng đồng MCP](https://modelcontextprotocol.io/)

## Tiếp theo

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.