# Integracja Model Context Protocol (MCP) z Microsoft Foundry

Ten przewodnik pokazuje, jak zintegrować serwery Model Context Protocol (MCP) z agentami Microsoft Foundry, umożliwiając zaawansowaną orkiestrację narzędzi oraz możliwości AI dla przedsiębiorstw.

## Wprowadzenie

Model Context Protocol (MCP) to otwarty standard umożliwiający aplikacjom AI bezpieczne łączenie się z zewnętrznymi źródłami danych i narzędziami. Po integracji z Microsoft Foundry, MCP pozwala agentom na dostęp do różnych usług, API i źródeł danych w ustandaryzowany sposób.

Ta integracja łączy elastyczność ekosystemu narzędzi MCP z solidnym frameworkiem agentów Microsoft Foundry, zapewniając rozwiązania AI klasy przedsiębiorstw z szerokimi możliwościami dostosowywania.

**Uwagi:** Jeśli chcesz korzystać z MCP w Microsoft Foundry Agent Service, obecnie obsługiwane są tylko następujące regiony: westus, westus2, uaenorth, southindia oraz switzerlandnorth

## Cele nauki

Po zakończeniu tego przewodnika będziesz umiał:

- Zrozumieć Model Context Protocol i jego zalety
- Skonfigurować serwery MCP do użycia z agentami Microsoft Foundry
- Tworzyć i konfigurować agentów z integracją narzędzi MCP
- Wdrażać praktyczne przykłady z użyciem rzeczywistych serwerów MCP
- Obsługiwać odpowiedzi narzędzi i cytowania w rozmowach agentów

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że posiadasz:

- Subskrypcję Azure z dostępem do Microsoft Foundry
- Python 3.10+ lub .NET 8.0+
- Zainstalowane i skonfigurowane Azure CLI
- Odpowiednie uprawnienia do tworzenia zasobów AI

## Czym jest Model Context Protocol (MCP)?

Model Context Protocol to ustandaryzowany sposób łączenia aplikacji AI z zewnętrznymi źródłami danych i narzędziami. Kluczowe korzyści to:

- **Ustandaryzowana integracja**: Spójny interfejs między różnymi narzędziami i usługami
- **Bezpieczeństwo**: Bezpieczne mechanizmy uwierzytelniania i autoryzacji
- **Elastyczność**: Obsługa różnych źródeł danych, API i narzędzi niestandardowych
- **Rozszerzalność**: Łatwe dodawanie nowych funkcji i integracji

## Konfiguracja MCP z Microsoft Foundry

### Konfiguracja środowiska

Wybierz preferowane środowisko programistyczne:

- [Implementacja w Pythonie](#implementacja-w-pythonie)
- [Implementacja w .NET](#codeblock5)

---

## Implementacja w Pythonie

***Uwaga*** Możesz uruchomić ten [notatnik](./mcp_support_python.ipynb)

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
    allowed_tools=[],  # Opcjonalnie: określ dozwolone narzędzia
)
```

### 6. Kompletny przykład w Pythonie

```python
with project_client:
    agents_client = project_client.agents

    # Utwórz nowego agenta z narzędziami MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Utwórz wątek do komunikacji
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Utwórz wiadomość do wątku
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Obsłuż zatwierdzenia narzędzi i uruchom agenta
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

    # Wyświetl rozmowę
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

***Uwaga*** Możesz uruchomić ten [notatnik](./mcp_support_dotnet.ipynb)

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

Podczas konfiguracji narzędzi MCP dla agenta możesz określić kilka ważnych parametrów:

### Konfiguracja w Pythonie

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identyfikator serwera MCP
    server_url="https://api.example.com/mcp", # Punkt końcowy serwera MCP
    allowed_tools=[],                       # Opcjonalnie: określ dozwolone narzędzia
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

## Rozwiązywanie najczęstszych problemów

### 1. Problemy z połączeniem
- Sprawdź dostępność adresu URL serwera MCP
- Zweryfikuj dane uwierzytelniające
- Upewnij się, że sieć działa prawidłowo

### 2. Niepowodzenia wywołań narzędzi
- Sprawdź argumenty narzędzi i ich formatowanie
- Zweryfikuj wymagania specyficzne dla serwera
- Zaimplementuj właściwą obsługę błędów

### 3. Problemy z wydajnością
- Optymalizuj częstotliwość wywołań narzędzi
- Wprowadź buforowanie tam, gdzie jest to zasadne
- Monitoruj czasy odpowiedzi serwera

## Kolejne kroki

Aby dalej usprawnić integrację MCP:

1. **Poznaj własne serwery MCP**: Buduj własne serwery MCP do zastrzeżonych źródeł danych
2. **Wdroż zaawansowane zabezpieczenia**: Dodaj OAuth2 lub niestandardowe mechanizmy uwierzytelniania
3. **Monitorowanie i analityka**: Wprowadź logowanie i monitorowanie użycia narzędzi
4. **Skaluj swoje rozwiązanie**: Rozważ równoważenie obciążenia i rozproszone architektury serwerów MCP

## Dodatkowe zasoby

- [Dokumentacja Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Przykłady Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Przegląd agentów Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Specyfikacja MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Wsparcie

W celu dodatkowego wsparcia i pytań:
- Przejrzyj [dokumentację Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Sprawdź [zasoby społeczności MCP](https://modelcontextprotocol.io/)

## Co dalej

- [5.14 Inżynieria kontekstu MCP](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->