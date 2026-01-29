# دمج بروتوكول سياق النموذج (MCP) مع Azure AI Foundry

يوضح هذا الدليل كيفية دمج خوادم بروتوكول سياق النموذج (MCP) مع وكلاء Azure AI Foundry، مما يتيح تنسيق أدوات قوي وقدرات ذكاء اصطناعي على مستوى المؤسسات.

## المقدمة

بروتوكول سياق النموذج (MCP) هو معيار مفتوح يتيح لتطبيقات الذكاء الاصطناعي الاتصال بأمان بمصادر البيانات والأدوات الخارجية. عند دمجه مع Azure AI Foundry، يسمح MCP للوكلاء بالوصول إلى خدمات خارجية مختلفة وواجهات برمجة التطبيقات ومصادر البيانات والتفاعل معها بطريقة موحدة.

يجمع هذا التكامل بين مرونة نظام أدوات MCP مع إطار عمل الوكلاء القوي في Azure AI Foundry، مما يوفر حلول ذكاء اصطناعي على مستوى المؤسسات مع إمكانيات تخصيص واسعة.

**ملاحظة:** إذا كنت ترغب في استخدام MCP في خدمة وكلاء Azure AI Foundry، فإن المناطق المدعومة حالياً هي: westus، westus2، uaenorth، southindia و switzerlandnorth

## أهداف التعلم

بنهاية هذا الدليل، ستكون قادراً على:

- فهم بروتوكول سياق النموذج وفوائده
- إعداد خوادم MCP لاستخدامها مع وكلاء Azure AI Foundry
- إنشاء وتكوين وكلاء مع دمج أدوات MCP
- تنفيذ أمثلة عملية باستخدام خوادم MCP حقيقية
- التعامل مع استجابات الأدوات والاستشهادات في محادثات الوكلاء

## المتطلبات الأساسية

قبل البدء، تأكد من توفر:

- اشتراك Azure مع وصول إلى AI Foundry
- Python 3.10+ أو .NET 8.0+
- تثبيت وتكوين Azure CLI
- الأذونات المناسبة لإنشاء موارد الذكاء الاصطناعي

## ما هو بروتوكول سياق النموذج (MCP)؟

بروتوكول سياق النموذج هو طريقة موحدة لتطبيقات الذكاء الاصطناعي للاتصال بمصادر البيانات والأدوات الخارجية. تشمل الفوائد الرئيسية:

- **تكامل موحد**: واجهة متسقة عبر أدوات وخدمات مختلفة
- **الأمان**: آليات مصادقة وتفويض آمنة
- **المرونة**: دعم لمصادر بيانات مختلفة، وواجهات برمجة التطبيقات، والأدوات المخصصة
- **قابلية التوسع**: سهولة إضافة قدرات وتكاملات جديدة

## إعداد MCP مع Azure AI Foundry

### تكوين البيئة

اختر بيئة التطوير المفضلة لديك:

- [تنفيذ Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [تنفيذ .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## تنفيذ Python

***ملاحظة*** يمكنك تشغيل هذا [الدفتر](mcp_support_python.ipynb)

### 1. تثبيت الحزم المطلوبة

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. استيراد التبعيات

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. تكوين إعدادات MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. تهيئة عميل المشروع

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. إنشاء أداة MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. مثال Python كامل

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

## تنفيذ .NET

***ملاحظة*** يمكنك تشغيل هذا [الدفتر](mcp_support_dotnet.ipynb)

### 1. تثبيت الحزم المطلوبة

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. استيراد التبعيات

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. تكوين الإعدادات

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. إنشاء تعريف أداة MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. إنشاء وكيل مع أدوات MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. مثال .NET كامل

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

## خيارات تكوين أداة MCP

عند تكوين أدوات MCP لوكيلك، يمكنك تحديد عدة معلمات مهمة:

### تكوين Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### تكوين .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## المصادقة والرؤوس

كلا التنفيذين يدعمان رؤوس مخصصة للمصادقة:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## استكشاف المشكلات الشائعة وإصلاحها

### 1. مشاكل الاتصال
- تحقق من إمكانية الوصول إلى عنوان URL لخادم MCP
- راجع بيانات اعتماد المصادقة
- تأكد من اتصال الشبكة

### 2. فشل استدعاء الأداة
- راجع وسيطات الأداة وتنسيقها
- تحقق من متطلبات الخادم الخاصة
- نفذ معالجة أخطاء مناسبة

### 3. مشاكل الأداء
- حسّن تكرار استدعاء الأداة
- نفذ التخزين المؤقت عند الحاجة
- راقب أوقات استجابة الخادم

## الخطوات التالية

لتعزيز تكامل MCP الخاص بك:

1. **استكشاف خوادم MCP المخصصة**: أنشئ خوادم MCP خاصة بمصادر بياناتك
2. **تنفيذ أمان متقدم**: أضف OAuth2 أو آليات مصادقة مخصصة
3. **المراقبة والتحليلات**: نفذ تسجيل ومراقبة لاستخدام الأدوات
4. **توسيع الحل الخاص بك**: فكر في موازنة التحميل وهندسة خوادم MCP الموزعة

## موارد إضافية

- [توثيق Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [نماذج بروتوكول سياق النموذج](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [نظرة عامة على وكلاء Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [مواصفات MCP](https://spec.modelcontextprotocol.io/)

## الدعم

للحصول على دعم إضافي وأسئلة:
- راجع [توثيق Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- تحقق من [موارد مجتمع MCP](https://modelcontextprotocol.io/)

## ما التالي

- [5.14 هندسة سياق MCP](../mcp-contextengineering/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.