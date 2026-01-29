# Интеграција Model Context Protocol (MCP) са Azure AI Foundry

Овај водич показује како да интегришете сервере Model Context Protocol (MCP) са Azure AI Foundry агентима, омогућавајући моћну оркестрацију алата и корпоративне AI могућности.

## Увод

Model Context Protocol (MCP) је отворени стандард који омогућава AI апликацијама безбедно повезивање са спољним изворима података и алатима. Када се интегрише са Azure AI Foundry, MCP омогућава агентима приступ и интеракцију са разним спољним сервисима, API-јима и изворима података на стандардизован начин.

Ова интеграција спаја флексибилност MCP екосистема алата са робусним оквиром Azure AI Foundry агената, пружајући корпоративна AI решења са широким могућностима прилагођавања.

**Note:** Ако желите да користите MCP у Azure AI Foundry Agent Service, тренутно су подржане само следеће регије: westus, westus2, uaenorth, southindia и switzerlandnorth

## Циљеви учења

На крају овог водича моћи ћете да:

- Разумете Model Context Protocol и његове предности
- Подесите MCP сервере за коришћење са Azure AI Foundry агентима
- Креирате и конфигуришете агенте са интеграцијом MCP алата
- Имплементирате практичне примере користећи праве MCP сервере
- Обрадите одговоре алата и цитате у разговорима агената

## Захтеви

Пре почетка, уверите се да имате:

- Azure претплату са приступом AI Foundry
- Python 3.10+ или .NET 8.0+
- Инсталиран и конфигурисан Azure CLI
- Одговарајуће дозволе за креирање AI ресурса

## Шта је Model Context Protocol (MCP)?

Model Context Protocol је стандардизован начин за AI апликације да се повежу са спољним изворима података и алатима. Кључне предности укључују:

- **Стандардизована интеграција**: Конзистентан интерфејс за различите алате и сервисе
- **Безбедност**: Безбедни механизми аутентификације и ауторизације
- **Флексибилност**: Подршка за разне изворе података, API-је и прилагођене алате
- **Проширивост**: Лако додавање нових могућности и интеграција

## Подешавање MCP са Azure AI Foundry

### Конфигурација окружења

Изаберите жељено развојно окружење:

- [Python имплементација](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET имплементација](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python имплементација

***Note*** Можете покренути овај [notebook](mcp_support_python.ipynb)

### 1. Инсталирање потребних пакета

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Увоз зависности

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Конфигурисање MCP подешавања

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Иницијализација Project Client-а

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Креирање MCP алата

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Комплетан Python пример

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

## .NET имплементација

***Note*** Можете покренути овај [notebook](mcp_support_dotnet.ipynb)

### 1. Инсталирање потребних пакета

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Увоз зависности

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Конфигурисање подешавања

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Креирање дефиниције MCP алата

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Креирање агента са MCP алатима

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Комплетан .NET пример

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

## Опције конфигурације MCP алата

При конфигурисању MCP алата за вашег агента, можете одредити неколико важних параметара:

### Python конфигурација

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET конфигурација

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Аутентификација и заглавља

Обе имплементације подржавају прилагођена заглавља за аутентификацију:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Решавање уобичајених проблема

### 1. Проблеми са везом
- Проверите да ли је MCP URL сервера доступан
- Проверите аутентификационе податке
- Уверите се у мрежну повезаност

### 2. Неуспех позива алата
- Прегледајте аргументе и формат позива алата
- Проверите захтеве специфичне за сервер
- Имплементирајте правилно руковање грешкама

### 3. Проблеми са перформансама
- Оптимизујте учесталост позива алата
- Користите кеширање где је прикладно
- Пратите време одговора сервера

## Следећи кораци

Да бисте додатно унапредили вашу MCP интеграцију:

1. **Истражите прилагођене MCP сервере**: Креирајте своје MCP сервере за власничке изворе података
2. **Имплементирајте напредну безбедност**: Додајте OAuth2 или прилагођене механизме аутентификације
3. **Мониторинг и аналитика**: Имплементирајте логовање и праћење коришћења алата
4. **Шкалирање решења**: Размотрите балансер оптерећења и дистрибуиране архитектуре MCP сервера

## Додатни ресурси

- [Azure AI Foundry документација](https://learn.microsoft.com/azure/ai-foundry/)
- [Примери Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Преглед Azure AI Foundry агената](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP спецификација](https://spec.modelcontextprotocol.io/)

## Подршка

За додатну подршку и питања:
- Прегледајте [Azure AI Foundry документацију](https://learn.microsoft.com/azure/ai-foundry/)
- Погледајте [MCP заједничке ресурсе](https://modelcontextprotocol.io/)

## Шта следи

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.