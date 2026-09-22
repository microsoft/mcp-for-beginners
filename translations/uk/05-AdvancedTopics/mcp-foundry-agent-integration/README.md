# Інтеграція Model Context Protocol (MCP) з Microsoft Foundry

У цьому посібнику показано, як інтегрувати сервери Model Context Protocol (MCP) з агентами Microsoft Foundry, забезпечуючи потужну оркестрацію інструментів та корпоративні можливості ШІ.

## Вступ

Model Context Protocol (MCP) — це відкритий стандарт, який дозволяє ШІ-застосункам безпечно підключатися до зовнішніх джерел даних та інструментів. При інтеграції з Microsoft Foundry, MCP дає агентам можливість отримувати доступ та взаємодіяти з різними зовнішніми службами, API та джерелами даних у стандартизований спосіб.

Ця інтеграція поєднує гнучкість екосистеми інструментів MCP із надійною агентовою платформою Microsoft Foundry, забезпечуючи корпоративні рішення зі ШІ з широкими можливостями налаштування.

**Примітка:** Якщо ви хочете використовувати MCP в службі агентів Microsoft Foundry, наразі підтримуються лише такі регіони: westus, westus2, uaenorth, southindia та switzerlandnorth

## Цілі навчання

Після проходження цього посібника ви зможете:

- Розуміти Model Context Protocol та його переваги
- Налаштувати сервери MCP для роботи з агентами Microsoft Foundry
- Створювати та конфігурувати агентів із інтеграцією інструментів MCP
- Реалізувати практичні приклади з використанням реальних серверів MCP
- Обробляти відповіді інструментів і посилання під час розмов агентів

## Вимоги

Перед початком переконайтеся, що у вас є:

- Підписка Azure з доступом до Microsoft Foundry
- Python 3.10+ або .NET 8.0+
- Встановлений та налаштований Azure CLI
- Відповідні дозволи для створення ресурсів ШІ

## Що таке Model Context Protocol (MCP)?

Model Context Protocol – стандартизований спосіб для ШІ-застосунків підключатися до зовнішніх джерел даних та інструментів. Основні переваги включають:

- **Стандартизована інтеграція**: Послідовний інтерфейс для різних інструментів та служб
- **Безпека**: Захищені механізми автентифікації та авторизації
- **Гнучкість**: Підтримка різних джерел даних, API та кастомних інструментів
- **Розширюваність**: Легке додавання нових можливостей і інтеграцій

## Налаштування MCP з Microsoft Foundry

### Конфігурація середовища

Виберіть улюблене середовище розробки:

- [Імплементація на Python](#імплементація-на-python)
- [Імплементація на .NET](#codeblock5)

---

## Імплементація на Python

***Примітка*** Ви можете запустити цей [ноутбук](./mcp_support_python.ipynb)

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

### 3. Налаштування параметрів MCP

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

### 5. Створення інструменту MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Необов’язково: вкажіть дозволені інструменти
)
```

### 6. Повний приклад на Python

```python
with project_client:
    agents_client = project_client.agents

    # Створити нового агента з інструментами MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Створити потік для спілкування
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Створити повідомлення для потоку
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Обробити затвердження інструментів і запустити агента
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

    # Показати розмову
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

## Імплементація на .NET

***Примітка*** Ви можете запустити цей [ноутбук](./mcp_support_dotnet.ipynb)

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

### 3. Налаштування параметрів

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Створення визначення інструменту MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Створення агента з інструментами MCP

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

## Опції конфігурації інструментів MCP

Під час налаштування інструментів MCP для вашого агента ви можете вказати кілька важливих параметрів:

### Конфігурація на Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Ідентифікатор сервера MCP
    server_url="https://api.example.com/mcp", # Кінцева точка сервера MCP
    allowed_tools=[],                       # Необов’язково: вкажіть дозволені інструменти
)
```

### Конфігурація на .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Аутентифікація та заголовки

Обидві імплементації підтримують налаштування кастомних заголовків для аутентифікації:

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
- Перевірте доступність URL серверу MCP
- Переконайтесь в правильності облікових даних аутентифікації
- Забезпечте мережеве з'єднання

### 2. Помилки виклику інструмента
- Перевірте аргументи інструменту та їх форматування
- Врахуйте вимоги конкретного серверу
- Реалізуйте коректну обробку помилок

### 3. Проблеми з продуктивністю
- Оптимізуйте частоту викликів інструментів
- Використовуйте кешування за потреби
- Моніторьте час відгуку серверу

## Наступні кроки

Для подальшого вдосконалення інтеграції MCP:

1. **Дослідіть кастомні сервери MCP**: Створіть власні сервери MCP для пропрієтарних джерел даних
2. **Реалізуйте розширену безпеку**: Додайте OAuth2 або кастомні механізми аутентифікації
3. **Моніторинг та аналітика**: Запровадьте логування та моніторинг використання інструментів
4. **Масштабування рішення**: Розгляньте балансування навантаження та розподілені архітектури серверів MCP

## Додаткові ресурси

- [Документація Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Приклади Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Огляд агентів Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Специфікація MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Підтримка

Для додаткової підтримки та запитань:
- Ознайомтеся з [документацією Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Перевірте [спільнотні ресурси MCP](https://modelcontextprotocol.io/)

## Що далі

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->