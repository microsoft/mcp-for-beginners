# Model Context Protocol (MCP) Integration med Microsoft Foundry

Denna guide visar hur du integrerar Model Context Protocol (MCP) servrar med Microsoft Foundry-agent, vilket möjliggör kraftfull verktygsorkestrering och AI-funktioner för företag.

## Introduktion

Model Context Protocol (MCP) är en öppen standard som gör det möjligt för AI-applikationer att säkert ansluta till externa datakällor och verktyg. När det integreras med Microsoft Foundry tillåter MCP agenter att komma åt och interagera med olika externa tjänster, API:er och datakällor på ett standardiserat sätt.

Denna integration kombinerar flexibiliteten i MCP:s verktygsekosystem med Microsoft Foundrys robusta agentramverk och erbjuder AI-lösningar för företag med omfattande anpassningsmöjligheter.

**Obs:** Om du vill använda MCP i Microsoft Foundry Agent Service stöds för närvarande endast följande regioner: westus, westus2, uaenorth, southindia och switzerlandnorth

## Lärandemål

I slutet av denna guide kommer du att kunna:

- Förstå Model Context Protocol och dess fördelar
- Ställa in MCP-servrar för användning med Microsoft Foundry-agenter
- Skapa och konfigurera agenter med MCP-verktygsintegration
- Implementera praktiska exempel med verkliga MCP-servrar
- Hantera verktygssvar och källhänvisningar i agentkonversationer

## Förutsättningar

Innan du börjar, se till att du har:

- Ett Azure-abonnemang med tillgång till Microsoft Foundry
- Python 3.10+ eller .NET 8.0+
- Azure CLI installerat och konfigurerat
- Lämpliga behörigheter för att skapa AI-resurser

## Vad är Model Context Protocol (MCP)?

Model Context Protocol är ett standardiserat sätt för AI-applikationer att ansluta till externa datakällor och verktyg. Viktiga fördelar inkluderar:

- **Standardiserad integration**: Enhetligt gränssnitt över olika verktyg och tjänster
- **Säkerhet**: Säkra autentiserings- och auktoriseringsmekanismer
- **Flexibilitet**: Stöd för olika datakällor, API:er och egna verktyg
- **Utbyggbarhet**: Lätt att lägga till nya funktioner och integrationer

## Installera och konfigurera MCP med Microsoft Foundry

### Miljökonfiguration

Välj din föredragna utvecklingsmiljö:

- [Python-implementering](#python-implementering)
- [.NET-implementering](#codeblock5)

---

## Python-implementering

***Obs*** Du kan köra denna [notebook](./mcp_support_python.ipynb)

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
    allowed_tools=[],  # Valfritt: specificera tillåtna verktyg
)
```

### 6. Komplett Python-exempel

```python
with project_client:
    agents_client = project_client.agents

    # Skapa en ny agent med MCP-verktyg
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Skapa tråd för kommunikation
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Skapa meddelande till tråd
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Hantera godkännanden för verktyg och kör agent
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

    # Visa konversation
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

## .NET-implementering

***Obs*** Du kan köra denna [notebook](./mcp_support_dotnet.ipynb)

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

## Konfigurationsalternativ för MCP-verktyg

När du konfigurerar MCP-verktyg för din agent kan du specificera flera viktiga parametrar:

### Python-konfiguration

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier för MCP-servern
    server_url="https://api.example.com/mcp", # MCP-serverns slutpunkt
    allowed_tools=[],                       # Valfritt: specificera tillåtna verktyg
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
- Verifiera att MCP-serverns URL är åtkomlig
- Kontrollera autentiseringsuppgifter
- Säkerställ nätverksanslutning

### 2. Verktygsanropsfel
- Granska verktygsargument och formatering
- Kontrollera serverspecifika krav
- Implementera korrekt felhantering

### 3. Prestandaproblem
- Optimera anropsfrekvens för verktyg
- Implementera cachelagring där det är lämpligt
- Övervaka serverresponstider

## Nästa steg

För att ytterligare förbättra din MCP-integration:

1. **Utforska anpassade MCP-servrar**: Bygg dina egna MCP-servrar för proprietära datakällor
2. **Implementera avancerad säkerhet**: Lägg till OAuth2 eller egna autentiseringsmekanismer
3. **Övervakning och analys**: Implementera loggning och övervakning för verktygsanvändning
4. **Skala din lösning**: Överväg lastbalansering och distribuerade MCP-serverarkitekturer

## Ytterligare resurser

- [Microsoft Foundry Dokumentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Exempel](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Översikt av Microsoft Foundry-agenter](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP-specifikation](https://modelcontextprotocol.io/specification/2026-07-28/)

## Support

För ytterligare support och frågor:
- Granska [Microsoft Foundrys dokumentation](https://learn.microsoft.com/azure/ai-foundry/)
- Kontrollera [MCP-communityresurser](https://modelcontextprotocol.io/)

## Vad händer härnäst  

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->