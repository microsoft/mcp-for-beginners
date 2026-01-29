# Model Context Protocol (MCP) Integration mit Azure AI Foundry

Dieser Leitfaden zeigt, wie Model Context Protocol (MCP)-Server mit Azure AI Foundry-Agenten integriert werden, um leistungsstarke Tool-Orchestrierung und Enterprise-KI-Funktionen zu ermöglichen.

## Einführung

Model Context Protocol (MCP) ist ein offener Standard, der es KI-Anwendungen ermöglicht, sicher auf externe Datenquellen und Tools zuzugreifen. In Kombination mit Azure AI Foundry erlaubt MCP Agenten, auf verschiedene externe Dienste, APIs und Datenquellen auf standardisierte Weise zuzugreifen und mit ihnen zu interagieren.

Diese Integration verbindet die Flexibilität des MCP-Tool-Ökosystems mit dem robusten Agenten-Framework von Azure AI Foundry und bietet so Enterprise-KI-Lösungen mit umfangreichen Anpassungsmöglichkeiten.

**Note:** Wenn Sie MCP im Azure AI Foundry Agent Service verwenden möchten, werden derzeit nur die folgenden Regionen unterstützt: westus, westus2, uaenorth, southindia und switzerlandnorth

## Lernziele

Am Ende dieses Leitfadens werden Sie in der Lage sein:

- Das Model Context Protocol und seine Vorteile zu verstehen
- MCP-Server für die Nutzung mit Azure AI Foundry-Agenten einzurichten
- Agenten mit MCP-Tool-Integration zu erstellen und zu konfigurieren
- Praktische Beispiele mit echten MCP-Servern umzusetzen
- Tool-Antworten und Quellenangaben in Agentengesprächen zu verarbeiten

## Voraussetzungen

Stellen Sie vor Beginn sicher, dass Sie Folgendes haben:

- Ein Azure-Abonnement mit Zugriff auf AI Foundry
- Python 3.10+ oder .NET 8.0+
- Azure CLI installiert und konfiguriert
- Die erforderlichen Berechtigungen zum Erstellen von AI-Ressourcen

## Was ist Model Context Protocol (MCP)?

Model Context Protocol ist eine standardisierte Methode, mit der KI-Anwendungen eine Verbindung zu externen Datenquellen und Tools herstellen können. Wichtige Vorteile sind:

- **Standardisierte Integration**: Einheitliche Schnittstelle für verschiedene Tools und Dienste
- **Sicherheit**: Sichere Authentifizierungs- und Autorisierungsmechanismen
- **Flexibilität**: Unterstützung verschiedener Datenquellen, APIs und benutzerdefinierter Tools
- **Erweiterbarkeit**: Einfache Erweiterung um neue Funktionen und Integrationen

## Einrichtung von MCP mit Azure AI Foundry

### Umgebungskonfiguration

Wählen Sie Ihre bevorzugte Entwicklungsumgebung:

- [Python-Implementierung](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET-Implementierung](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python-Implementierung

***Note*** Sie können dieses [Notebook](mcp_support_python.ipynb) ausführen

### 1. Installation der benötigten Pakete

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Import der Abhängigkeiten

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfiguration der MCP-Einstellungen

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Initialisierung des Projekt-Clients

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Erstellung des MCP-Tools

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Komplettes Python-Beispiel

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

## .NET-Implementierung

***Note*** Sie können dieses [Notebook](mcp_support_dotnet.ipynb) ausführen

### 1. Installation der benötigten Pakete

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Import der Abhängigkeiten

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfiguration der Einstellungen

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Erstellung der MCP-Tool-Definition

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Erstellung eines Agenten mit MCP-Tools

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Komplettes .NET-Beispiel

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

## MCP Tool-Konfigurationsoptionen

Bei der Konfiguration von MCP-Tools für Ihren Agenten können Sie mehrere wichtige Parameter festlegen:

### Python-Konfiguration

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET-Konfiguration

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Authentifizierung und Header

Beide Implementierungen unterstützen benutzerdefinierte Header für die Authentifizierung:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Fehlerbehebung bei häufigen Problemen

### 1. Verbindungsprobleme
- Überprüfen Sie, ob die MCP-Server-URL erreichbar ist
- Prüfen Sie die Authentifizierungsdaten
- Stellen Sie die Netzwerkverbindung sicher

### 2. Fehler bei Tool-Aufrufen
- Überprüfen Sie die Argumente und das Format der Tool-Aufrufe
- Beachten Sie server-spezifische Anforderungen
- Implementieren Sie eine geeignete Fehlerbehandlung

### 3. Leistungsprobleme
- Optimieren Sie die Häufigkeit der Tool-Aufrufe
- Nutzen Sie Caching, wo sinnvoll
- Überwachen Sie die Antwortzeiten des Servers

## Nächste Schritte

Um Ihre MCP-Integration weiter zu verbessern:

1. **Eigene MCP-Server entwickeln**: Erstellen Sie eigene MCP-Server für proprietäre Datenquellen
2. **Erweiterte Sicherheit implementieren**: Fügen Sie OAuth2 oder benutzerdefinierte Authentifizierungsmechanismen hinzu
3. **Überwachung und Analyse**: Implementieren Sie Logging und Monitoring für die Tool-Nutzung
4. **Skalierung Ihrer Lösung**: Berücksichtigen Sie Lastverteilung und verteilte MCP-Server-Architekturen

## Zusätzliche Ressourcen

- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Beispiele](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Übersicht](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Spezifikation](https://spec.modelcontextprotocol.io/)

## Support

Für weitere Unterstützung und Fragen:
- Lesen Sie die [Azure AI Foundry Dokumentation](https://learn.microsoft.com/azure/ai-foundry/)
- Besuchen Sie die [MCP Community-Ressourcen](https://modelcontextprotocol.io/)

## Was kommt als Nächstes

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.