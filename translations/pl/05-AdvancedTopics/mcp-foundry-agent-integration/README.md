# Integracja Model Context Protocol (MCP) z Azure AI Foundry

Ten przewodnik pokazuje, jak zintegrować serwery Model Context Protocol (MCP) z agentami Azure AI Foundry, umożliwiając zaawansowaną orkiestrację narzędzi i możliwości AI na poziomie przedsiębiorstwa.

## Wprowadzenie

Model Context Protocol (MCP) to otwarty standard, który pozwala aplikacjom AI na bezpieczne łączenie się z zewnętrznymi źródłami danych i narzędziami. Po integracji z Azure AI Foundry, MCP umożliwia agentom dostęp i interakcję z różnymi zewnętrznymi usługami, API i źródłami danych w ustandaryzowany sposób.

Ta integracja łączy elastyczność ekosystemu narzędzi MCP z solidnym frameworkiem agentów Azure AI Foundry, oferując rozwiązania AI klasy korporacyjnej z szerokimi możliwościami dostosowania.

**Note:** Jeśli chcesz używać MCP w Azure AI Foundry Agent Service, obecnie obsługiwane są tylko następujące regiony: westus, westus2, uaenorth, southindia oraz switzerlandnorth

## Cele nauki

Po ukończeniu tego przewodnika będziesz potrafił:

- Zrozumieć Model Context Protocol i jego zalety
- Skonfigurować serwery MCP do współpracy z agentami Azure AI Foundry
- Tworzyć i konfigurować agentów z integracją narzędzi MCP
- Wdrażać praktyczne przykłady z użyciem rzeczywistych serwerów MCP
- Obsługiwać odpowiedzi narzędzi i cytowania w rozmowach agentów

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że posiadasz:

- Subskrypcję Azure z dostępem do AI Foundry
- Python 3.10+ lub .NET 8.0+
- Zainstalowane i skonfigurowane Azure CLI
- Odpowiednie uprawnienia do tworzenia zasobów AI

## Czym jest Model Context Protocol (MCP)?

Model Context Protocol to ustandaryzowany sposób, w jaki aplikacje AI łączą się z zewnętrznymi źródłami danych i narzędziami. Kluczowe zalety to:

- **Ustandaryzowana integracja**: Spójny interfejs dla różnych narzędzi i usług
- **Bezpieczeństwo**: Bezpieczne mechanizmy uwierzytelniania i autoryzacji
- **Elastyczność**: Wsparcie dla różnych źródeł danych, API i narzędzi niestandardowych
- **Rozszerzalność**: Łatwe dodawanie nowych funkcji i integracji

## Konfiguracja MCP z Azure AI Foundry

### Konfiguracja środowiska

Wybierz preferowane środowisko programistyczne:

- [Implementacja w Pythonie](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Implementacja w .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Implementacja w Pythonie

***Note*** Możesz uruchomić ten [notebook](mcp_support_python.ipynb)

### 1. Instalacja wymaganych pakietów

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Import zależności

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfiguracja ustawień MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicjalizacja klienta projektu

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Utworzenie narzędzia MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Kompletny przykład w Pythonie

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

## Implementacja w .NET

***Note*** Możesz uruchomić ten [notebook](mcp_support_dotnet.ipynb)

### 1. Instalacja wymaganych pakietów

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Import zależności

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfiguracja ustawień

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Utworzenie definicji narzędzia MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Utworzenie agenta z narzędziami MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Kompletny przykład w .NET

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

## Opcje konfiguracji narzędzi MCP

Podczas konfigurowania narzędzi MCP dla agenta możesz określić kilka ważnych parametrów:

### Konfiguracja w Pythonie

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Konfiguracja w .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Uwierzytelnianie i nagłówki

Obie implementacje obsługują niestandardowe nagłówki do uwierzytelniania:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Rozwiązywanie typowych problemów

### 1. Problemy z połączeniem
- Sprawdź, czy URL serwera MCP jest dostępny
- Zweryfikuj dane uwierzytelniające
- Upewnij się, że sieć działa poprawnie

### 2. Błędy wywołań narzędzi
- Sprawdź argumenty i formatowanie wywołań narzędzi
- Zweryfikuj wymagania specyficzne dla serwera
- Zaimplementuj odpowiednią obsługę błędów

### 3. Problemy z wydajnością
- Optymalizuj częstotliwość wywołań narzędzi
- Wprowadź cache tam, gdzie to możliwe
- Monitoruj czasy odpowiedzi serwera

## Kolejne kroki

Aby jeszcze bardziej rozwinąć integrację MCP:

1. **Poznaj niestandardowe serwery MCP**: Buduj własne serwery MCP dla własnych źródeł danych
2. **Wdroż zaawansowane zabezpieczenia**: Dodaj OAuth2 lub niestandardowe mechanizmy uwierzytelniania
3. **Monitorowanie i analityka**: Wprowadź logowanie i monitorowanie użycia narzędzi
4. **Skaluj rozwiązanie**: Rozważ load balancing i rozproszone architektury serwerów MCP

## Dodatkowe zasoby

- [Dokumentacja Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Przykłady Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Przegląd agentów Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Specyfikacja MCP](https://spec.modelcontextprotocol.io/)

## Wsparcie

W przypadku dodatkowego wsparcia i pytań:
- Zapoznaj się z [dokumentacją Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Sprawdź [zasoby społeczności MCP](https://modelcontextprotocol.io/)

## Co dalej

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.