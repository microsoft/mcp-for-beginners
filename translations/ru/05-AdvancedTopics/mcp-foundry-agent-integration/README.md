# Интеграция Model Context Protocol (MCP) с Azure AI Foundry

В этом руководстве показано, как интегрировать серверы Model Context Protocol (MCP) с агентами Azure AI Foundry, что позволяет реализовать мощную оркестрацию инструментов и корпоративные возможности ИИ.

## Введение

Model Context Protocol (MCP) — это открытый стандарт, который позволяет ИИ-приложениям безопасно подключаться к внешним источникам данных и инструментам. При интеграции с Azure AI Foundry MCP даёт агентам возможность получать доступ и взаимодействовать с различными внешними сервисами, API и источниками данных по единому стандарту.

Эта интеграция сочетает гибкость экосистемы инструментов MCP с надёжной архитектурой агентов Azure AI Foundry, обеспечивая корпоративные решения ИИ с широкими возможностями настройки.

**Note:** Если вы хотите использовать MCP в Azure AI Foundry Agent Service, на данный момент поддерживаются только следующие регионы: westus, westus2, uaenorth, southindia и switzerlandnorth

## Цели обучения

К концу этого руководства вы сможете:

- Понять, что такое Model Context Protocol и его преимущества
- Настроить серверы MCP для работы с агентами Azure AI Foundry
- Создавать и настраивать агентов с интеграцией инструментов MCP
- Реализовывать практические примеры с использованием реальных серверов MCP
- Обрабатывать ответы инструментов и ссылки в диалогах агентов

## Требования

Перед началом убедитесь, что у вас есть:

- Подписка Azure с доступом к AI Foundry
- Python 3.10+ или .NET 8.0+
- Установленный и настроенный Azure CLI
- Необходимые права для создания ресурсов AI

## Что такое Model Context Protocol (MCP)?

Model Context Protocol — это стандартизированный способ подключения ИИ-приложений к внешним источникам данных и инструментам. Основные преимущества:

- **Стандартизированная интеграция**: единый интерфейс для разных инструментов и сервисов
- **Безопасность**: надёжные механизмы аутентификации и авторизации
- **Гибкость**: поддержка различных источников данных, API и кастомных инструментов
- **Расширяемость**: лёгкое добавление новых возможностей и интеграций

## Настройка MCP с Azure AI Foundry

### Конфигурация окружения

Выберите предпочитаемую среду разработки:

- [Реализация на Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Реализация на .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Реализация на Python

***Note*** Вы можете запустить этот [notebook](mcp_support_python.ipynb)

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
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Полный пример на Python

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

## Реализация на .NET

***Note*** Вы можете запустить этот [notebook](mcp_support_dotnet.ipynb)

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

## Параметры конфигурации инструментов MCP

При настройке инструментов MCP для вашего агента можно указать несколько важных параметров:

### Конфигурация для Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Конфигурация для .NET

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

## Устранение распространённых проблем

### 1. Проблемы с подключением
- Проверьте доступность URL сервера MCP
- Проверьте правильность учётных данных для аутентификации
- Убедитесь в наличии сетевого соединения

### 2. Ошибки вызова инструментов
- Проверьте аргументы и форматирование вызовов инструментов
- Учитывайте требования конкретного сервера
- Реализуйте корректную обработку ошибок

### 3. Проблемы с производительностью
- Оптимизируйте частоту вызовов инструментов
- Используйте кэширование там, где это уместно
- Отслеживайте время отклика сервера

## Следующие шаги

Для дальнейшего улучшения интеграции MCP:

1. **Изучите создание собственных серверов MCP**: создавайте свои MCP-серверы для проприетарных источников данных
2. **Реализуйте расширенную безопасность**: добавьте OAuth2 или кастомные механизмы аутентификации
3. **Мониторинг и аналитика**: внедрите логирование и мониторинг использования инструментов
4. **Масштабирование решения**: рассмотрите балансировку нагрузки и распределённую архитектуру MCP-серверов

## Дополнительные ресурсы

- [Документация Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Примеры Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Обзор агентов Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Спецификация MCP](https://spec.modelcontextprotocol.io/)

## Поддержка

Для дополнительной поддержки и вопросов:
- Ознакомьтесь с [документацией Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Посетите [сообщество MCP](https://modelcontextprotocol.io/)

## Что дальше

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.