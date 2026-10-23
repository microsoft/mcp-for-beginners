# Model Context Protocol (MCP) Integratie met Microsoft Foundry

Deze gids laat zien hoe Model Context Protocol (MCP)-servers geïntegreerd kunnen worden met Microsoft Foundry-agenten, waardoor krachtige toolorkestratie en enterprise AI-mogelijkheden mogelijk worden.

## Inleiding

Model Context Protocol (MCP) is een open standaard die AI-toepassingen in staat stelt om veilig verbinding te maken met externe databronnen en tools. Wanneer geïntegreerd met Microsoft Foundry, stelt MCP agenten in staat om op een gestandaardiseerde manier toegang te krijgen tot en te communiceren met diverse externe services, API's en databronnen.

Deze integratie combineert de flexibiliteit van MCP's tool-ecosysteem met het robuuste agentframework van Microsoft Foundry, en biedt AI-oplossingen van ondernemingsniveau met uitgebreide aanpassingsmogelijkheden.

> **Opmerking:** Als u MCP wilt gebruiken in Microsoft Foundry Agent Service, worden momenteel alleen de volgende regio's ondersteund: westus, westus2, uaenorth, southindia en switzerlandnorth

## Leerdoelen

Aan het einde van deze gids zult u in staat zijn om:

- Het Model Context Protocol en de voordelen ervan begrijpen
- MCP-servers opzetten voor gebruik met Microsoft Foundry-agenten
- Agenten maken en configureren met MCP-toolintegratie
- Praktische voorbeelden uitvoeren met echte MCP-servers
- Omgaan met toolantwoorden en citaties in agentgesprekken

## Vereisten

Zorg voordat u begint dat u:

- Een Azure-abonnement met toegang tot Microsoft Foundry
- Python 3.10+ of .NET 8.0+
- Azure CLI geïnstalleerd en geconfigureerd
- Passende machtigingen voor het aanmaken van AI-resources

## Wat is Model Context Protocol (MCP)?

Model Context Protocol is een gestandaardiseerde manier voor AI-toepassingen om verbinding te maken met externe databronnen en tools. Belangrijke voordelen zijn:

- **Gestandaardiseerde Integratie**: Consistente interface voor verschillende tools en services
- **Beveiliging**: Veilige authenticatie- en autorisatiemechanismen
- **Flexibiliteit**: Ondersteuning voor diverse databronnen, API's en aangepaste tools
- **Uitbreidbaarheid**: Gemakkelijk nieuwe mogelijkheden en integraties toevoegen

## MCP instellen met Microsoft Foundry

### Omgevingsconfiguratie

Kies uw voorkeursontwikkelomgeving:

- [Python-implementatie](#python-implementation)
- [.NET-implementatie](#net-implementation)

---

## Python-implementatie

***Opmerking*** U kunt deze [notebook](./mcp_support_python.ipynb) uitvoeren

### 1. Vereiste pakketten installeren

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Afhankelijkheden importeren

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP-configuratie instellen

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Projectclient initialiseren

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP-tool maken

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Volledig Python-voorbeeld

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

## .NET-implementatie

***Opmerking*** U kunt deze [notebook](./mcp_support_dotnet.ipynb) uitvoeren

### 1. Vereiste pakketten installeren

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Afhankelijkheden importeren

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Instellingen configureren

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP-tooldefinitie maken

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Agent maken met MCP-tools

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Volledig .NET-voorbeeld

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

## MCP-toolconfiguratieopties

Bij het configureren van MCP-tools voor uw agent kunt u verschillende belangrijke parameters opgeven:

### Python-configuratie

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET-configuratie

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Authenticatie en headers

Beide implementaties ondersteunen aangepaste headers voor authenticatie:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Problemen oplossen bij veelvoorkomende problemen

### 1. Verbindingsproblemen
- Controleer of de MCP-server-URL toegankelijk is
- Controleer authenticatiegegevens
- Zorg voor netwerkconnectiviteit

### 2. Fouten bij tool-aanroepen
- Bekijk toolargumenten en opmaak
- Controleer serverspecifieke vereisten
- Implementeer correcte foutafhandeling

### 3. Prestatieproblemen
- Optimaliseer de frequentie van tool-aanroepen
- Implementeer caching waar van toepassing
- Monitor responstijden van de server

## Volgende stappen

Om uw MCP-integratie verder te verbeteren:

1. **Verken aangepaste MCP-servers**: Bouw uw eigen MCP-servers voor proprietaire databronnen
2. **Implementeer geavanceerde beveiliging**: Voeg OAuth2 of aangepaste authenticatiemechanismen toe
3. **Monitoren en analyses**: Implementeer logging en monitoring voor toolgebruik
4. **Schaal uw oplossing**: Overweeg load balancing en gedistribueerde MCP-serverarchitecturen

## Aanvullende bronnen

- [Microsoft Foundry-documentatie](https://learn.microsoft.com/azure/ai-foundry/)
- [Voorbeelden van Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Overzicht Microsoft Foundry Agents](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP-specificatie](https://modelcontextprotocol.io/specification/2026-07-28/)

## Ondersteuning

Voor extra ondersteuning en vragen:
- Bekijk de [Microsoft Foundry-documentatie](https://learn.microsoft.com/azure/ai-foundry/)
- Controleer de [MCP-communitybronnen](https://modelcontextprotocol.io/)

## Wat nu?

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->