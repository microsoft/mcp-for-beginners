# Интеграция на Model Context Protocol (MCP) с Azure AI Foundry

Това ръководство показва как да интегрирате сървъри на Model Context Protocol (MCP) с агенти на Azure AI Foundry, което позволява мощна оркестрация на инструменти и корпоративни AI възможности.

## Въведение

Model Context Protocol (MCP) е отворен стандарт, който позволява на AI приложенията да се свързват сигурно с външни източници на данни и инструменти. Когато е интегриран с Azure AI Foundry, MCP дава възможност на агентите да имат достъп и да взаимодействат с различни външни услуги, API-та и източници на данни по стандартизиран начин.

Тази интеграция съчетава гъвкавостта на екосистемата от инструменти на MCP с надеждната рамка за агенти на Azure AI Foundry, предоставяйки корпоративни AI решения с широки възможности за персонализация.

**Note:** Ако искате да използвате MCP в Azure AI Foundry Agent Service, в момента се поддържат само следните региони: westus, westus2, uaenorth, southindia и switzerlandnorth

## Цели на обучението

След приключване на това ръководство ще можете да:

- Разберете какво е Model Context Protocol и какви са ползите от него
- Настроите MCP сървъри за използване с агенти на Azure AI Foundry
- Създавате и конфигурирате агенти с интеграция на MCP инструменти
- Прилагате практически примери с реални MCP сървъри
- Обработвате отговори от инструменти и цитати в разговорите на агентите

## Предварителни изисквания

Преди да започнете, уверете се, че разполагате с:

- Абонамент за Azure с достъп до AI Foundry
- Python 3.10+ или .NET 8.0+
- Инсталиран и конфигуриран Azure CLI
- Подходящи разрешения за създаване на AI ресурси

## Какво е Model Context Protocol (MCP)?

Model Context Protocol е стандартизиран начин за AI приложенията да се свързват с външни източници на данни и инструменти. Основните предимства включват:

- **Стандартизирана интеграция**: Последователен интерфейс за различни инструменти и услуги
- **Сигурност**: Сигурни механизми за удостоверяване и упълномощаване
- **Гъвкавост**: Поддръжка на различни източници на данни, API-та и персонализирани инструменти
- **Разширяемост**: Лесно добавяне на нови възможности и интеграции

## Настройка на MCP с Azure AI Foundry

### Конфигурация на средата

Изберете предпочитаната от вас среда за разработка:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** Можете да стартирате този [notebook](mcp_support_python.ipynb)

### 1. Инсталиране на необходимите пакети

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Импортиране на зависимости

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Конфигуриране на MCP настройки

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Инициализиране на клиент за проекта

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Създаване на MCP инструмент

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Пълен Python пример

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

***Note*** Можете да стартирате този [notebook](mcp_support_dotnet.ipynb)

### 1. Инсталиране на необходимите пакети

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Импортиране на зависимости

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Конфигуриране на настройки

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Създаване на дефиниция за MCP инструмент

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Създаване на агент с MCP инструменти

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Пълен .NET пример

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

## Опции за конфигуриране на MCP инструменти

При конфигуриране на MCP инструменти за вашия агент, можете да зададете няколко важни параметъра:

### Python конфигурация

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET конфигурация

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Удостоверяване и заглавки

И двете реализации поддържат персонализирани заглавки за удостоверяване:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Отстраняване на често срещани проблеми

### 1. Проблеми с връзката
- Проверете дали URL адресът на MCP сървъра е достъпен
- Проверете удостоверителните данни
- Уверете се в наличието на мрежова свързаност

### 2. Грешки при извикване на инструменти
- Прегледайте аргументите и форматирането на инструмента
- Проверете специфичните изисквания на сървъра
- Прилагайте подходяща обработка на грешки

### 3. Проблеми с производителността
- Оптимизирайте честотата на извикване на инструменти
- Използвайте кеширане, където е подходящо
- Следете времето за отговор на сървъра

## Следващи стъпки

За да подобрите още интеграцията с MCP:

1. **Изследвайте персонализирани MCP сървъри**: Създайте свои MCP сървъри за собствени източници на данни
2. **Прилагайте разширена сигурност**: Добавете OAuth2 или персонализирани механизми за удостоверяване
3. **Мониторинг и анализи**: Внедрете логване и мониторинг на използването на инструментите
4. **Мащабиране на решението**: Обмислете балансиране на натоварването и разпределени архитектури на MCP сървъри

## Допълнителни ресурси

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## Поддръжка

За допълнителна помощ и въпроси:
- Прегледайте [документацията на Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Проверете [общностните ресурси за MCP](https://modelcontextprotocol.io/)

## Какво следва

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.