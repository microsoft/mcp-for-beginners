# Интеграция Model Context Protocol (MCP) с Microsoft Foundry

В этом руководстве показано, как интегрировать серверы Model Context Protocol (MCP) с агентами Microsoft Foundry, что обеспечивает мощную оркестрацию инструментов и возможности корпоративного ИИ.

## Введение

Model Context Protocol (MCP) — это открытый стандарт, который позволяет приложениям ИИ безопасно подключаться к внешним источникам данных и инструментам. При интеграции с Microsoft Foundry MCP позволяет агентам получать доступ и взаимодействовать с различными внешними сервисами, API и источниками данных в стандартизированной форме.

Эта интеграция сочетает гибкость экосистемы инструментов MCP с надежной системой агентов Microsoft Foundry, предоставляя решения корпоративного класса ИИ с широкими возможностями настройки.

**Примечание:** Если вы хотите использовать MCP в Microsoft Foundry Agent Service, на данный момент поддерживаются только следующие регионы: westus, westus2, uaenorth, southindia и switzerlandnorth

## Цели обучения

К концу этого руководства вы сможете:

- Понять протокол Model Context Protocol и его преимущества
- Настроить серверы MCP для использования с агентами Microsoft Foundry
- Создавать и настраивать агентов с интеграцией инструментов MCP
- Реализовать практические примеры с реальными серверами MCP
- Обрабатывать ответы инструментов и ссылки в разговорах агентов

## Требования

Перед началом убедитесь, что у вас есть:

- Подписка Azure с доступом к Microsoft Foundry
- Python 3.10+ или .NET 8.0+
- Установленная и настроенная Azure CLI
- Необходимые разрешения для создания ресурсов ИИ

## Что такое Model Context Protocol (MCP)?

Model Context Protocol — это стандартизированный способ для приложений ИИ подключаться к внешним источникам данных и инструментам. Ключевые преимущества включают:

- **Стандартизированная интеграция**: Единый интерфейс для различных инструментов и сервисов
- **Безопасность**: Безопасные механизмы аутентификации и авторизации
- **Гибкость**: Поддержка различных источников данных, API и пользовательских инструментов
- **Расширяемость**: Легкость добавления новых возможностей и интеграций

## Настройка MCP с Microsoft Foundry

### Конфигурация окружения

Выберите предпочитаемую среду разработки:

- [Реализация на Python](#реализация-на-python)
- [Реализация на .NET](#codeblock5)

---

## Реализация на Python

***Примечание*** Вы можете запустить этот [блокнот](./mcp_support_python.ipynb)

### 1. Установка необходимых пакетов

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Импорт зависимостей

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Настройка параметров MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Инициализация клиента проекта

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Создание инструмента MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Необязательно: укажите разрешённые инструменты
)
```

### 6. Полный пример на Python

```python
with project_client:
    agents_client = project_client.agents

    # Создать нового агента с инструментами MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Создать поток для общения
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Создать сообщение для потока
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Обработать утверждения инструментов и запустить агента
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

    # Отобразить разговор
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

## Реализация на .NET

***Примечание*** Вы можете запустить этот [блокнот](./mcp_support_dotnet.ipynb)

### 1. Установка необходимых пакетов

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Импорт зависимостей

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Настройка параметров

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Создание определения инструмента MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Создание агента с инструментами MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Полный пример на .NET

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

## Опции конфигурации инструмента MCP

При настройке инструментов MCP для вашего агента вы можете указать несколько важных параметров:

### Конфигурация Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Идентификатор сервера MCP
    server_url="https://api.example.com/mcp", # Конечная точка сервера MCP
    allowed_tools=[],                       # Необязательно: укажите допустимые инструменты
)
```

### Конфигурация .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Аутентификация и заголовки

Обе реализации поддерживают пользовательские заголовки для аутентификации:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Устранение распространенных проблем

### 1. Проблемы с подключением
- Проверьте доступность URL сервера MCP
- Проверьте учетные данные для аутентификации
- Убедитесь в наличии сетевого подключения

### 2. Сбои вызовов инструментов
- Проверьте аргументы и форматирование инструментов
- Проверьте требования, специфичные для сервера
- Реализуйте правильную обработку ошибок

### 3. Проблемы с производительностью
- Оптимизируйте частоту вызовов инструментов
- Используйте кеширование, где это возможно
- Следите за временем отклика сервера

## Следующие шаги

Для дальнейшего улучшения интеграции MCP:

1. **Изучите собственные серверы MCP**: Создавайте свои серверы MCP для проприетарных источников данных
2. **Реализуйте расширенную безопасность**: Добавьте OAuth2 или пользовательские механизмы аутентификации
3. **Мониторинг и аналитика**: Внедрите логирование и мониторинг использования инструментов
4. **Масштабируйте решение**: Рассмотрите балансировку нагрузки и распределённую архитектуру серверов MCP

## Дополнительные ресурсы

- [Документация Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Примеры Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Обзор агентов Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Спецификация MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Поддержка

Для дополнительной поддержки и вопросов:
- Ознакомьтесь с [документацией Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Посетите [ресурсы сообщества MCP](https://modelcontextprotocol.io/)

## Что дальше

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->