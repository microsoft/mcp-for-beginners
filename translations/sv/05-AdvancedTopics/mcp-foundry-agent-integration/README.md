# Model Context Protocol (MCP) Integration med Azure AI Foundry

Denna guide visar hur du integrerar Model Context Protocol (MCP) servrar med Azure AI Foundry-agenter, vilket möjliggör kraftfull verktygsorkestrering och företagsinriktade AI-funktioner.

## Introduktion

Model Context Protocol (MCP) är en öppen standard som gör det möjligt för AI-applikationer att säkert ansluta till externa datakällor och verktyg. När MCP integreras med Azure AI Foundry kan agenter få tillgång till och interagera med olika externa tjänster, API:er och datakällor på ett standardiserat sätt.

Denna integration kombinerar flexibiliteten i MCP:s verktygsekosystem med Azure AI Foundrys robusta agentramverk, vilket ger företagsklassade AI-lösningar med omfattande anpassningsmöjligheter.

**Note:** Om du vill använda MCP i Azure AI Foundry Agent Service stöds för närvarande endast följande regioner: westus, westus2, uaenorth, southindia och switzerlandnorth

## Lärandemål

Efter att ha gått igenom denna guide kommer du att kunna:

- Förstå Model Context Protocol och dess fördelar
- Sätta upp MCP-servrar för användning med Azure AI Foundry-agenter
- Skapa och konfigurera agenter med MCP-verktygsintegration
- Implementera praktiska exempel med riktiga MCP-servrar
- Hantera verktygsrespons och källhänvisningar i agentkonversationer

## Förutsättningar

Innan du börjar, se till att du har:

- Ett Azure-abonnemang med tillgång till AI Foundry
- Python 3.10+ eller .NET 8.0+
- Azure CLI installerat och konfigurerat
- Lämpliga behörigheter för att skapa AI-resurser

## Vad är Model Context Protocol (MCP)?

Model Context Protocol är ett standardiserat sätt för AI-applikationer att ansluta till externa datakällor och verktyg. Viktiga fördelar inkluderar:

- **Standardiserad integration**: Enhetligt gränssnitt över olika verktyg och tjänster
- **Säkerhet**: Säker autentisering och auktorisering
- **Flexibilitet**: Stöd för olika datakällor, API:er och anpassade verktyg
- **Utbyggbarhet**: Lätt att lägga till nya funktioner och integrationer

## Sätta upp MCP med Azure AI Foundry

### Miljökonfiguration

Välj din föredragna utvecklingsmiljö:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** Du kan köra denna [notebook](mcp_support_python.ipynb)

### 1. Installera nödvändiga paket

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importera beroenden

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigurera MCP-inställningar

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Initiera projektklient

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Skapa MCP-verktyg

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Komplett Python-exempel

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

***Note*** Du kan köra denna [notebook](mcp_support_dotnet.ipynb)

### 1. Installera nödvändiga paket

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importera beroenden

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurera inställningar

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Skapa MCP-verktygsdefinition

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Skapa agent med MCP-verktyg

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Komplett .NET-exempel

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

## MCP-verktygskonfigurationsalternativ

När du konfigurerar MCP-verktyg för din agent kan du ange flera viktiga parametrar:

### Python-konfiguration

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET-konfiguration

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentisering och headers

Båda implementationerna stödjer anpassade headers för autentisering:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Felsökning av vanliga problem

### 1. Anslutningsproblem
- Kontrollera att MCP-serverns URL är åtkomlig
- Verifiera autentiseringsuppgifter
- Säkerställ nätverksanslutning

### 2. Fel vid verktygsanrop
- Granska verktygsargument och formatering
- Kontrollera serverns specifika krav
- Implementera korrekt felhantering

### 3. Prestandaproblem
- Optimera anropsfrekvens för verktyg
- Använd caching där det är lämpligt
- Övervaka serverns svarstider

## Nästa steg

För att ytterligare förbättra din MCP-integration:

1. **Utforska egna MCP-servrar**: Bygg egna MCP-servrar för proprietära datakällor
2. **Implementera avancerad säkerhet**: Lägg till OAuth2 eller anpassade autentiseringsmekanismer
3. **Övervakning och analys**: Implementera loggning och övervakning av verktygsanvändning
4. **Skalning av lösningen**: Överväg lastbalansering och distribuerade MCP-serverarkitekturer

## Ytterligare resurser

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## Support

För ytterligare support och frågor:
- Granska [Azure AI Foundry-dokumentationen](https://learn.microsoft.com/azure/ai-foundry/)
- Kolla in [MCP community-resurser](https://modelcontextprotocol.io/)

## Vad händer härnäst

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.