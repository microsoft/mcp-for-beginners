# یکپارچه‌سازی پروتکل زمینه مدل (MCP) با Microsoft Foundry

این راهنما نحوه یکپارچه‌سازی سرورهای پروتکل زمینه مدل (MCP) با عوامل Microsoft Foundry را نشان می‌دهد، که امکان هماهنگی ابزارهای قدرتمند و قابلیت‌های هوش مصنوعی سازمانی را فراهم می‌کند.

## مقدمه

پروتکل زمینه مدل (MCP) یک استاندارد باز است که به برنامه‌های هوش مصنوعی اجازه می‌دهد به‌طور ایمن به منابع داده و ابزارهای خارجی متصل شوند. هنگامی که با Microsoft Foundry یکپارچه شود، MCP به عوامل امکان دسترسی و تعامل با خدمات، APIها و منابع داده مختلف خارجی را به شکلی استاندارد می‌دهد.

این یکپارچه‌سازی انعطاف‌پذیری اکوسیستم ابزار MCP را با چارچوب قوی عوامل Microsoft Foundry ترکیب می‌کند و راه‌حل‌های هوش مصنوعی سازمانی با قابلیت‌های سفارشی‌سازی گسترده ارائه می‌دهد.

**توجه:** اگر می‌خواهید از MCP در سرویس عامل Microsoft Foundry استفاده کنید، در حال حاضر تنها مناطق زیر پشتیبانی می‌شوند: westus, westus2, uaenorth, southindia و switzerlandnorth

## اهداف یادگیری

در پایان این راهنما قادر خواهید بود:

- درک پروتکل زمینه مدل و فواید آن
- راه‌اندازی سرورهای MCP برای استفاده با عوامل Microsoft Foundry
- ایجاد و پیکربندی عوامل با یکپارچه‌سازی ابزار MCP
- پیاده‌سازی مثال‌های عملی با استفاده از سرورهای واقعی MCP
- مدیریت پاسخ‌ها و ارجاعات ابزار در گفتگوهای عامل

## پیش‌نیازها

پیش از شروع، اطمینان حاصل کنید که دارید:

- اشتراک Azure با دسترسی به Microsoft Foundry
- Python 3.10+ یا .NET 8.0+
- نصب و پیکربندی Azure CLI
- مجوزهای مناسب برای ایجاد منابع هوش مصنوعی

## پروتکل زمینه مدل (MCP) چیست؟

پروتکل زمینه مدل یک روش استاندارد برای اتصال برنامه‌های هوش مصنوعی به منابع داده و ابزارهای خارجی است. مزایای کلیدی شامل:

- **یکپارچه‌سازی استانداردشده**: رابط یکسان در ابزارها و خدمات مختلف
- **امنیت**: مکانیزم‌های احراز هویت و اجازه دسترسی ایمن
- **انعطاف‌پذیری**: پشتیبانی از منابع داده، APIها و ابزارهای سفارشی مختلف
- **قابلیت گسترش**: افزودن آسان قابلیت‌ها و یکپارچه‌سازی‌های جدید

## راه‌اندازی MCP با Microsoft Foundry

### تنظیم محیط

محیط توسعه مورد نظر خود را انتخاب کنید:

- [پیاده‌سازی Python](#پیاده‌سازی-python)
- [پیاده‌سازی .NET](#codeblock5)

---

## پیاده‌سازی Python

***توجه*** می‌توانید این [دفترچه یادداشت](./mcp_support_python.ipynb) را اجرا کنید

### 1. نصب بسته‌های مورد نیاز

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. وارد کردن وابستگی‌ها

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. پیکربندی تنظیمات MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. راه‌اندازی کلاینت پروژه

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. ایجاد ابزار MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # اختیاری: ابزارهای مجاز را مشخص کنید
)
```

### 6. مثال کامل Python

```python
with project_client:
    agents_client = project_client.agents

    # ایجاد یک عامل جدید با ابزارهای MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # ایجاد نخ برای ارتباط
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # ایجاد پیام برای نخ
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # مدیریت تأیید ابزارها و اجرای عامل
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

    # نمایش گفتگو
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

***توجه*** می‌توانید این [دفترچه یادداشت](./mcp_support_dotnet.ipynb) را اجرا کنید

### 1. نصب بسته‌های مورد نیاز

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. وارد کردن وابستگی‌ها

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. پیکربندی تنظیمات

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. ایجاد تعریف ابزار MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. ایجاد عامل با ابزارهای MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. مثال کامل .NET

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
    server_label="unique_server_name",      # شناسه برای سرور MCP
    server_url="https://api.example.com/mcp", # نقطه پایان سرور MCP
    allowed_tools=[],                       # اختیاری: ابزارهای مجاز را مشخص کنید
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

## رفع اشکال مشکلات رایج

### 1. مشکلات اتصال
- بررسی کنید آدرس سرور MCP در دسترس باشد
- اعتبارنامه‌های احراز هویت را بررسی کنید
- اطمینان حاصل کنید که اتصال شبکه برقرار است

### 2. خطاهای فراخوانی ابزار
- آرگومان‌ها و قالب‌بندی ابزار را مرور کنید
- نیازمندی‌های خاص سرور را چک کنید
- مدیریت خطای مناسب را پیاده‌سازی کنید

### 3. مشکلات عملکرد
- فراوانی فراخوانی ابزار را بهینه کنید
- در صورت لزوم کشینگ را پیاده‌سازی کنید
- زمان پاسخ سرور را نظارت کنید

## مراحل بعدی

برای بهبود بیشتر یکپارچه‌سازی MCP خود:

1. **کاوش سرورهای MCP سفارشی**: ساخت سرورهای MCP خود برای منابع داده اختصاصی
2. **پیاده‌سازی امنیت پیشرفته**: افزودن OAuth2 یا مکانیزم‌های احراز هویت سفارشی
3. **نظارت و تحلیل**: پیاده‌سازی لاگ‌گیری و نظارت برای استفاده از ابزارها
4. **گسترش راه‌حل شما**: در نظر گرفتن تعادل بار و معماری‌های سرور MCP توزیع‌شده

## منابع بیشتر

- [مستندات Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [نمونه‌های پروتکل زمینه مدل](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [بررسی کلی عوامل Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [مشخصات MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## پشتیبانی

برای پشتیبانی و سوالات بیشتر:
- مرور مستندات [Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- بررسی منابع جامعه [MCP](https://modelcontextprotocol.io/)

## مراحل بعدی

- [5.14 مهندسی زمینه MCP](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->