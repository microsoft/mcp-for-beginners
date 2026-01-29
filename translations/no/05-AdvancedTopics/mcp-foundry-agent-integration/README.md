# Model Context Protocol (MCP) Integrasjon med Azure AI Foundry

Denne veiledningen viser hvordan du integrerer Model Context Protocol (MCP) servere med Azure AI Foundry-agenter, noe som muliggjør kraftig verktøyorchestrering og AI-løsninger for bedrifter.

## Introduksjon

Model Context Protocol (MCP) er en åpen standard som gjør det mulig for AI-applikasjoner å koble seg sikkert til eksterne datakilder og verktøy. Når MCP integreres med Azure AI Foundry, kan agenter få tilgang til og samhandle med ulike eksterne tjenester, API-er og datakilder på en standardisert måte.

Denne integrasjonen kombinerer fleksibiliteten i MCPs verktøyøkosystem med Azure AI Foundrys robuste agentrammeverk, og tilbyr AI-løsninger på bedriftsnivå med omfattende tilpasningsmuligheter.

**Note:** Hvis du ønsker å bruke MCP i Azure AI Foundry Agent Service, støttes for øyeblikket kun følgende regioner: westus, westus2, uaenorth, southindia og switzerlandnorth

## Læringsmål

Etter å ha fullført denne veiledningen vil du kunne:

- Forstå Model Context Protocol og fordelene med det
- Sette opp MCP-servere for bruk med Azure AI Foundry-agenter
- Opprette og konfigurere agenter med MCP-verktøyintegrasjon
- Implementere praktiske eksempler med ekte MCP-servere
- Håndtere verktøysvar og referanser i agentdialoger

## Forutsetninger

Før du begynner, sørg for at du har:

- Et Azure-abonnement med tilgang til AI Foundry
- Python 3.10+ eller .NET 8.0+
- Azure CLI installert og konfigurert
- Nødvendige tillatelser for å opprette AI-ressurser

## Hva er Model Context Protocol (MCP)?

Model Context Protocol er en standardisert måte for AI-applikasjoner å koble til eksterne datakilder og verktøy. Viktige fordeler inkluderer:

- **Standardisert integrasjon**: Konsistent grensesnitt på tvers av ulike verktøy og tjenester
- **Sikkerhet**: Sikker autentisering og autorisasjon
- **Fleksibilitet**: Støtte for ulike datakilder, API-er og tilpassede verktøy
- **Utvidbarhet**: Enkel å legge til nye funksjoner og integrasjoner

## Sette opp MCP med Azure AI Foundry

### Miljøkonfigurasjon

Velg ditt foretrukne utviklingsmiljø:

- [Python-implementasjon](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET-implementasjon](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python-implementasjon

***Note*** Du kan kjøre denne [notebooken](mcp_support_python.ipynb)

### 1. Installer nødvendige pakker

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importer avhengigheter

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigurer MCP-innstillinger

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Initialiser prosjektklient

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Opprett MCP-verktøy

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Fullstendig Python-eksempel

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

## .NET-implementasjon

***Note*** Du kan kjøre denne [notebooken](mcp_support_dotnet.ipynb)

### 1. Installer nødvendige pakker

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importer avhengigheter

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurer innstillinger

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Opprett MCP-verktøydefinisjon

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Opprett agent med MCP-verktøy

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Fullstendig .NET-eksempel

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

## MCP-verktøykonfigurasjonsalternativer

Når du konfigurerer MCP-verktøy for agenten din, kan du spesifisere flere viktige parametere:

### Python-konfigurasjon

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET-konfigurasjon

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentisering og headere

Begge implementasjonene støtter tilpassede headere for autentisering:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Feilsøking av vanlige problemer

### 1. Tilkoblingsproblemer
- Sjekk at MCP-serverens URL er tilgjengelig
- Kontroller autentiseringsopplysninger
- Sørg for nettverkstilkobling

### 2. Feil ved verktøysamtaler
- Gå gjennom verktøyargumenter og formatering
- Sjekk serverspesifikke krav
- Implementer riktig feilhåndtering

### 3. Ytelsesproblemer
- Optimaliser hyppigheten av verktøysamtaler
- Bruk caching der det er hensiktsmessig
- Overvåk responstider fra serveren

## Neste steg

For å forbedre MCP-integrasjonen ytterligere:

1. **Utforsk tilpassede MCP-servere**: Bygg dine egne MCP-servere for proprietære datakilder
2. **Implementer avansert sikkerhet**: Legg til OAuth2 eller tilpassede autentiseringsmekanismer
3. **Overvåking og analyse**: Implementer logging og overvåking av verktøybruk
4. **Skaler løsningen din**: Vurder lastbalansering og distribuerte MCP-serverarkitekturer

## Ytterligere ressurser

- [Azure AI Foundry Dokumentasjon](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Eksempler](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agenter Oversikt](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Spesifikasjon](https://spec.modelcontextprotocol.io/)

## Support

For ytterligere støtte og spørsmål:
- Se gjennom [Azure AI Foundry dokumentasjonen](https://learn.microsoft.com/azure/ai-foundry/)
- Sjekk [MCP fellesskapsressurser](https://modelcontextprotocol.io/)

## Hva nå

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.