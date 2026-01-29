# ادغام پروتکل زمینه مدل (MCP) با Azure AI Foundry

این راهنما نحوه ادغام سرورهای پروتکل زمینه مدل (MCP) با عامل‌های Azure AI Foundry را نشان می‌دهد که امکان هماهنگی قدرتمند ابزارها و قابلیت‌های هوش مصنوعی سازمانی را فراهم می‌کند.

## مقدمه

پروتکل زمینه مدل (MCP) یک استاندارد باز است که به برنامه‌های هوش مصنوعی اجازه می‌دهد به‌صورت امن به منابع داده و ابزارهای خارجی متصل شوند. هنگامی که با Azure AI Foundry ادغام شود، MCP به عامل‌ها امکان می‌دهد به خدمات، APIها و منابع داده خارجی مختلف به‌صورت استاندارد دسترسی داشته و با آن‌ها تعامل کنند.

این ادغام، انعطاف‌پذیری اکوسیستم ابزارهای MCP را با چارچوب قدرتمند عامل‌های Azure AI Foundry ترکیب می‌کند و راه‌حل‌های هوش مصنوعی سازمانی با قابلیت‌های سفارشی‌سازی گسترده ارائه می‌دهد.

**توجه:** اگر می‌خواهید از MCP در سرویس عامل Azure AI Foundry استفاده کنید، در حال حاضر فقط مناطق زیر پشتیبانی می‌شوند: westus، westus2، uaenorth، southindia و switzerlandnorth

## اهداف یادگیری

در پایان این راهنما، قادر خواهید بود:

- پروتکل زمینه مدل و مزایای آن را درک کنید
- سرورهای MCP را برای استفاده با عامل‌های Azure AI Foundry راه‌اندازی کنید
- عامل‌ها را با ادغام ابزار MCP ایجاد و پیکربندی کنید
- مثال‌های عملی با استفاده از سرورهای واقعی MCP پیاده‌سازی کنید
- پاسخ‌ها و ارجاعات ابزارها را در مکالمات عامل مدیریت کنید

## پیش‌نیازها

قبل از شروع، اطمینان حاصل کنید که:

- اشتراک Azure با دسترسی به AI Foundry دارید
- Python 3.10+ یا .NET 8.0+ نصب شده است
- Azure CLI نصب و پیکربندی شده است
- مجوزهای لازم برای ایجاد منابع هوش مصنوعی را دارید

## پروتکل زمینه مدل (MCP) چیست؟

پروتکل زمینه مدل روشی استاندارد برای اتصال برنامه‌های هوش مصنوعی به منابع داده و ابزارهای خارجی است. مزایای کلیدی آن عبارتند از:

- **ادغام استاندارد**: رابطی یکنواخت در سراسر ابزارها و خدمات مختلف
- **امنیت**: مکانیزم‌های احراز هویت و مجوزدهی امن
- **انعطاف‌پذیری**: پشتیبانی از منابع داده، APIها و ابزارهای سفارشی متنوع
- **قابلیت توسعه**: افزودن آسان قابلیت‌ها و ادغام‌های جدید

## راه‌اندازی MCP با Azure AI Foundry

### پیکربندی محیط

محیط توسعه مورد نظر خود را انتخاب کنید:

- [پیاده‌سازی Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [پیاده‌سازی .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## پیاده‌سازی Python

***توجه*** می‌توانید این [دفترچه یادداشت](mcp_support_python.ipynb) را اجرا کنید

### ۱. نصب بسته‌های مورد نیاز

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### ۲. وارد کردن وابستگی‌ها

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### ۳. پیکربندی تنظیمات MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### ۴. مقداردهی اولیه کلاینت پروژه

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### ۵. ایجاد ابزار MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### ۶. مثال کامل Python

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

## پیاده‌سازی .NET

***توجه*** می‌توانید این [دفترچه یادداشت](mcp_support_dotnet.ipynb) را اجرا کنید

### ۱. نصب بسته‌های مورد نیاز

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### ۲. وارد کردن وابستگی‌ها

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### ۳. پیکربندی تنظیمات

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### ۴. ایجاد تعریف ابزار MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### ۵. ایجاد عامل با ابزارهای MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### ۶. مثال کامل .NET

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

## گزینه‌های پیکربندی ابزار MCP

هنگام پیکربندی ابزارهای MCP برای عامل خود، می‌توانید چندین پارامتر مهم را مشخص کنید:

### پیکربندی Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### پیکربندی .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## احراز هویت و هدرها

هر دو پیاده‌سازی از هدرهای سفارشی برای احراز هویت پشتیبانی می‌کنند:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## رفع مشکلات رایج

### ۱. مشکلات اتصال
- بررسی کنید که URL سرور MCP در دسترس باشد
- اعتبارنامه‌های احراز هویت را بررسی کنید
- اتصال شبکه را اطمینان حاصل کنید

### ۲. خطاهای فراخوانی ابزار
- آرگومان‌ها و قالب‌بندی ابزار را بازبینی کنید
- نیازمندی‌های خاص سرور را بررسی کنید
- مدیریت خطای مناسب را پیاده‌سازی کنید

### ۳. مشکلات عملکرد
- فرکانس فراخوانی ابزار را بهینه کنید
- در صورت لزوم کشینگ را پیاده‌سازی کنید
- زمان پاسخ سرور را نظارت کنید

## مراحل بعدی

برای بهبود بیشتر ادغام MCP خود:

1. **کاوش سرورهای سفارشی MCP**: سرورهای MCP خود را برای منابع داده اختصاصی بسازید
2. **پیاده‌سازی امنیت پیشرفته**: افزودن OAuth2 یا مکانیزم‌های احراز هویت سفارشی
3. **نظارت و تحلیل**: پیاده‌سازی لاگ‌گیری و نظارت بر استفاده از ابزارها
4. **مقیاس‌پذیری راه‌حل**: در نظر گرفتن تعادل بار و معماری‌های توزیع‌شده سرور MCP

## منابع اضافی

- [مستندات Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [نمونه‌های پروتکل زمینه مدل](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [مروری بر عامل‌های Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [مشخصات MCP](https://spec.modelcontextprotocol.io/)

## پشتیبانی

برای پشتیبانی و سوالات بیشتر:
- مستندات [Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/) را بررسی کنید
- منابع جامعه [MCP](https://modelcontextprotocol.io/) را مشاهده کنید

## گام بعدی

- [5.14 مهندسی زمینه MCP](../mcp-contextengineering/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.