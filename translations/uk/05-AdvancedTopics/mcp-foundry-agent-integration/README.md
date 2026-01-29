# Інтеграція Model Context Protocol (MCP) з Azure AI Foundry

Цей посібник демонструє, як інтегрувати сервери Model Context Protocol (MCP) з агентами Azure AI Foundry, що дозволяє ефективно організовувати інструменти та реалізовувати корпоративні AI-рішення.

## Вступ

Model Context Protocol (MCP) — це відкритий стандарт, який дає змогу AI-додаткам безпечно підключатися до зовнішніх джерел даних та інструментів. При інтеграції з Azure AI Foundry MCP дозволяє агентам отримувати доступ і взаємодіяти з різними зовнішніми сервісами, API та джерелами даних у стандартизований спосіб.

Ця інтеграція поєднує гнучкість екосистеми інструментів MCP з надійною архітектурою агентів Azure AI Foundry, забезпечуючи корпоративні AI-рішення з широкими можливостями налаштування.

**Note:** Якщо ви хочете використовувати MCP у службі Azure AI Foundry Agent, наразі підтримуються лише такі регіони: westus, westus2, uaenorth, southindia та switzerlandnorth

## Цілі навчання

Після проходження цього посібника ви зможете:

- Розуміти Model Context Protocol та його переваги
- Налаштувати сервери MCP для роботи з агентами Azure AI Foundry
- Створювати та конфігурувати агентів з інтеграцією MCP інструментів
- Реалізовувати практичні приклади з використанням реальних серверів MCP
- Обробляти відповіді інструментів та посилання в розмовах агентів

## Вимоги

Перед початком переконайтеся, що у вас є:

- Підписка Azure з доступом до AI Foundry
- Python 3.10+ або .NET 8.0+
- Встановлений та налаштований Azure CLI
- Відповідні права для створення AI-ресурсів

## Що таке Model Context Protocol (MCP)?

Model Context Protocol — це стандартизований спосіб підключення AI-додатків до зовнішніх джерел даних та інструментів. Основні переваги:

- **Стандартизована інтеграція**: уніфікований інтерфейс для різних інструментів і сервісів
- **Безпека**: надійні механізми автентифікації та авторизації
- **Гнучкість**: підтримка різних джерел даних, API та кастомних інструментів
- **Розширюваність**: легке додавання нових можливостей та інтеграцій

## Налаштування MCP з Azure AI Foundry

### Конфігурація середовища

Обирайте зручне для вас середовище розробки:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** Ви можете запустити цей [ноутбук](mcp_support_python.ipynb)

### 1. Встановлення необхідних пакетів

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Імпорт залежностей

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Налаштування MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Ініціалізація клієнта проекту

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Створення MCP інструменту

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Повний приклад на Python

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

***Note*** Ви можете запустити цей [ноутбук](mcp_support_dotnet.ipynb)

### 1. Встановлення необхідних пакетів

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Імпорт залежностей

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Налаштування

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Створення визначення MCP інструменту

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Створення агента з MCP інструментами

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Повний приклад на .NET

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

## Параметри конфігурації MCP інструментів

Під час налаштування MCP інструментів для вашого агента можна вказати кілька важливих параметрів:

### Конфігурація для Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Конфігурація для .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Аутентифікація та заголовки

Обидві реалізації підтримують кастомні заголовки для аутентифікації:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Вирішення поширених проблем

### 1. Проблеми з підключенням
- Перевірте доступність URL сервера MCP
- Переконайтеся у правильності облікових даних для аутентифікації
- Перевірте мережеве з’єднання

### 2. Помилки виклику інструментів
- Перевірте аргументи та форматування виклику інструменту
- Врахуйте специфічні вимоги сервера
- Реалізуйте коректну обробку помилок

### 3. Проблеми з продуктивністю
- Оптимізуйте частоту викликів інструментів
- Використовуйте кешування там, де це доречно
- Моніторьте час відповіді сервера

## Наступні кроки

Щоб покращити інтеграцію MCP:

1. **Досліджуйте кастомні сервери MCP**: створюйте власні сервери MCP для приватних джерел даних
2. **Реалізуйте розширену безпеку**: додайте OAuth2 або інші механізми аутентифікації
3. **Моніторинг та аналітика**: впровадьте логування та моніторинг використання інструментів
4. **Масштабування рішення**: розгляньте балансування навантаження та розподілену архітектуру MCP серверів

## Додаткові ресурси

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## Підтримка

Для додаткової підтримки та запитань:
- Ознайомтеся з [документацією Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Перевірте [ресурси спільноти MCP](https://modelcontextprotocol.io/)

## Що далі

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.