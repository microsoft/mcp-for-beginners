# ماڈل کانٹیکسٹ پروٹوکول (MCP) کو مائیکروسافٹ فاؤنڈری کے ساتھ انضمام

یہ رہنما دکھاتا ہے کہ ماڈل کانٹیکسٹ پروٹوکول (MCP) سرورز کو مائیکروسافٹ فاؤنڈری ایجنٹس کے ساتھ کیسے مربوط کیا جائے، جو طاقتور ٹول آرکیسٹریشن اور انٹرپرائز AI صلاحیتوں کو ممکن بناتا ہے۔

## تعارف

ماڈل کانٹیکسٹ پروٹوکول (MCP) ایک اوپن اسٹینڈرڈ ہے جو AI ایپلیکیشنز کو بیرونی ڈیٹا ذرائع اور ٹولز کے ساتھ محفوظ طریقے سے جڑنے کے قابل بناتا ہے۔ جب مائیکروسافٹ فاؤنڈری کے ساتھ مربوط کیا جاتا ہے، تو MCP ایجنٹس کو مختلف بیرونی خدمات، APIs، اور ڈیٹا ذرائع تک معیاری طریقے سے رسائی اور تعامل کی اجازت دیتا ہے۔

یہ انضمام MCP کے ٹول ایکو سسٹم کی لچک کو مائیکروسافٹ فاؤنڈری کے مضبوط ایجنٹ فریم ورک کے ساتھ ملاتا ہے، انٹرپرائز گریڈ AI حل فراہم کرتے ہوئے وسیع حد تک تخصیص کی صلاحیتوں کے ساتھ۔

**نوٹ:** اگر آپ MCP کو مائیکروسافٹ فاؤنڈری ایجنٹ سروس میں استعمال کرنا چاہتے ہیں، تو فی الحال صرف درج ذیل ریجنز کی حمایت کی جاتی ہے: westus, westus2, uaenorth, southindia اور switzerlandnorth

## سیکھنے کے مقاصد

اس رہنما کے آخر میں، آپ قابل ہوں گے کہ:

- ماڈل کانٹیکسٹ پروٹوکول اور اس کے فوائد کو سمجھیں
- MCP سرورز کو مائیکروسافٹ فاؤنڈری ایجنٹس کے ساتھ استعمال کے لیے سیٹ اپ کریں
- MCP ٹول انضمام کے ساتھ ایجنٹس تخلیق اور تشکیل دیں
- حقیقی MCP سرورز استعمال کرتے ہوئے عملی مثالیں نافذ کریں
- ایجنٹ کی بات چیت میں ٹول کے جوابات اور حوالہ جات کو ہینڈل کریں

## ضروریات

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس ہے:

- مائیکروسافٹ فاؤنڈری رسائی کے ساتھ Azure سبسکرپشن
- Python 3.10+ یا .NET 8.0+
- Azure CLI انسٹال اور ترتیب دیا ہوا
- AI وسائل بنانے کے لیے مناسب اجازتیں

## ماڈل کانٹیکسٹ پروٹوکول (MCP) کیا ہے؟

ماڈل کانٹیکسٹ پروٹوکول AI ایپلیکیشنز کے لیے ایک معیاری طریقہ ہے جس کے ذریعہ وہ بیرونی ڈیٹا ذرائع اور ٹولز سے جڑتی ہیں۔ اہم فوائد میں شامل ہیں:

- **معیاری انضمام**: مختلف ٹولز اور خدمات کے درمیان مستقل انٹرفیس
- **سیکیورٹی**: محفوظ تصدیق اور اجازت کے طریقے
- **لچک**: مختلف ڈیٹا ذرائع، APIs، اور کسٹم ٹولز کی حمایت
- **قابل توسیع**: نئی صلاحیتوں اور انضمام کو آسانی سے شامل کرنا

## مائیکروسافٹ فاؤنڈری کے ساتھ MCP سیٹ اپ کرنا

### ماحول کی ترتیب

اپنی ترجیحی ڈیولپمنٹ ماحول کا انتخاب کریں:

- [Python امپلیمنٹیشن](#python-امپلیمنٹیشن)
- [.NET امپلیمنٹیشن](#codeblock5)

---

## Python امپلیمنٹیشن

***نوٹ*** آپ یہ [نوٹ بک](./mcp_support_python.ipynb) چلا سکتے ہیں

### 1. مطلوبہ پیکجز انسٹال کریں

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. انحصارات درآمد کریں

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP ترتیبات کو تشکیل دیں

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. پروجیکٹ کلائنٹ کو شروع کریں

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP ٹول بنائیں

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # اختیاری: مجاز ٹولز کی وضاحت کریں
)
```

### 6. مکمل Python مثال

```python
with project_client:
    agents_client = project_client.agents

    # MCP ٹولز کے ساتھ نیا ایجنٹ بنائیں
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # مواصلات کے لیے تھریڈ بنائیں
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # تھریڈ کے لیے پیغام تیار کریں
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # ٹول کی منظوریوں کا انتظام کریں اور ایجنٹ چلائیں
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

    # گفتگو دکھائیں
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

## .NET امپلیمنٹیشن

***نوٹ*** آپ یہ [نوٹ بک](./mcp_support_dotnet.ipynb) چلا سکتے ہیں

### 1. مطلوبہ پیکجز انسٹال کریں

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. انحصارات درآمد کریں

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. ترتیبات تشکیل دیں

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP ٹول کی تعریف بنائیں

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP ٹولز کے ساتھ ایجنٹ بنائیں

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. مکمل .NET مثال

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

## MCP ٹول تشکیل کے اختیارات

اپنے ایجنٹ کے لیے MCP ٹولز کو تشکیل دیتے وقت، آپ کئی اہم پیرامیٹرز مخصوص کر سکتے ہیں:

### Python ترتیب

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP سرور کے لیے شناخت کنندہ
    server_url="https://api.example.com/mcp", # MCP سرور کا آخر نقطہ
    allowed_tools=[],                       # اختیاری: اجازت شدہ آلات کی وضاحت کریں
)
```

### .NET ترتیب

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## توثیق اور ہیڈرز

دونوں امپلیمنٹیشنز کسٹم ہیڈرز کو توثیق کے لیے سپورٹ کرتی ہیں:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## عام مسائل کا حل

### 1. کنکشن مسائل
- MCP سرور URL کی رسائی کی تصدیق کریں
- تصدیقی اسناد چیک کریں
- نیٹ ورک کنیکٹیویٹی کو یقینی بنائیں

### 2. ٹول کال میں ناکامیاں
- ٹول دلائل اور فارمیٹنگ کا جائزہ لیں
- سرور مخصوص تقاضے چیک کریں
- مناسب ایرر ہینڈلنگ نافذ کریں

### 3. کارکردگی کے مسائل
- ٹول کال کی فریکوئنسی کو بہتر بنائیں
- جہاں مناسب ہو کیشنگ نافذ کریں
- سرور کے ردعمل کے اوقات کی نگرانی کریں

## اگلے اقدامات

اپنی MCP انضمام کو مزید بہتر بنانے کے لیے:

1. **کسٹم MCP سرورز کا جائزہ لیں**: اپنے ذاتی ڈیٹا ذرائع کے لیے اپنے MCP سرورز بنائیں
2. **ترقی یافتہ سیکیورٹی نافذ کریں**: OAuth2 یا کسٹم تصدیقی طریقے شامل کریں
3. **مانیٹرنگ اور تجزیات**: ٹول استعمال کے لیے لاگنگ اور مانیٹرنگ نافذ کریں
4. **اپنے حل کو مقیاس دیں**: لوڈ بیلنسنگ اور تقسیم شدہ MCP سرور آرکیٹیکچرز پر غور کریں

## اضافی وسائل

- [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/)

## سپورٹ

اضافی سپورٹ اور سوالات کے لیے:
- [Microsoft Foundry دستاویزات](https://learn.microsoft.com/azure/ai-foundry/) کا جائزہ لیں
- [MCP کمیونٹی وسائل](https://modelcontextprotocol.io/) چیک کریں

## اگلا کیا ہے

- [5.14 MCP کانٹیکسٹ انجینئرنگ](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->