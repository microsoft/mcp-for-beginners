# Modellkontekstprotokoll (MCP) integrasjon med Microsoft Foundry

Denne veiledningen viser hvordan du integrerer Model Context Protocol (MCP) servere med Microsoft Foundry-agenter, slik at man får kraftig verktøyorchestration og bedrifts-AI-funksjoner.

## Introduksjon

Model Context Protocol (MCP) er en åpen standard som gjør det mulig for AI-applikasjoner å koble seg sikkert til eksterne datakilder og verktøy. Når integrert med Microsoft Foundry, lar MCP agenter få tilgang til og samhandle med ulike eksterne tjenester, API-er og datakilder på en standardisert måte.

Denne integrasjonen kombinerer fleksibiliteten i MCPs verktøyøkosystem med Microsoft Foundrys robuste agent-rammeverk, og gir bedriftsnivå AI-løsninger med omfattende tilpasningsmuligheter.

**Merk:** Hvis du ønsker å bruke MCP i Microsoft Foundry Agent Service, støttes for øyeblikket bare følgende regioner: westus, westus2, uaenorth, southindia og switzerlandnorth

## Læringsmål

Ved slutten av denne veiledningen vil du kunne:

- Forstå Model Context Protocol og dens fordeler
- Sette opp MCP-servere for bruk med Microsoft Foundry-agenter
- Lage og konfigurere agenter med MCP verktøyintegrasjon
- Implementere praktiske eksempler med ekte MCP-servere
- Håndtere verktøysvar og referanser i agent-samtaler

## Forutsetninger

Før du starter, sørg for at du har:

- Et Azure-abonnement med tilgang til Microsoft Foundry
- Python 3.10+ eller .NET 8.0+
- Azure CLI installert og konfigurert
- Passende tillatelser for å opprette AI-ressurser

## Hva er Model Context Protocol (MCP)?

Model Context Protocol er en standardisert metode for AI-applikasjoner å koble seg til eksterne datakilder og verktøy. Viktige fordeler inkluderer:

- **Standardisert integrasjon**: Konsistent grensesnitt på tvers av forskjellige verktøy og tjenester
- **Sikkerhet**: Sikker autentisering og autorisasjonsmekanismer
- **Fleksibilitet**: Støtte for ulike datakilder, API-er og tilpassede verktøy
- **Utvidbarhet**: Lett å legge til nye funksjoner og integrasjoner

## Sette opp MCP med Microsoft Foundry

### Miljøkonfigurasjon

Velg ditt foretrukne utviklingsmiljø:

- [Python-implementering](#python-implementering)
- [.NET-implementering](#codeblock5)

---

## Python-implementering

***Merk*** Du kan kjøre denne [notebooken](./mcp_support_python.ipynb)

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

### 5. Lag MCP-verktøy

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Valgfritt: spesifiser tillatte verktøy
)
```

### 6. Komplett Python-eksempel

```python
with project_client:
    agents_client = project_client.agents

    # Opprett en ny agent med MCP-verktøy
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Opprett tråd for kommunikasjon
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Opprett melding til tråd
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Håndter verktøy-godkjenninger og kjør agent
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

    # Vis samtale
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

***Merk*** Du kan kjøre denne [notebooken](./mcp_support_dotnet.ipynb)

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

### 4. Lag MCP-verktøydefinisjon

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Lag agent med MCP-verktøy

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Komplett .NET-eksempel

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

## MCP verktøykonfigurasjonsvalg

Når du konfigurerer MCP-verktøy for agenten din, kan du spesifisere flere viktige parametere:

### Python-konfigurasjon

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifikator for MCP-serveren
    server_url="https://api.example.com/mcp", # MCP-serverendepunkt
    allowed_tools=[],                       # Valgfritt: spesifiser tillatte verktøy
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

Begge implementeringer støtter tilpassede headere for autentisering:

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
- Sjekk at MCP-server-URL er tilgjengelig
- Kontroller autentiseringsopplysninger
- Sørg for nettverkstilkobling

### 2. Feil ved verktøysamtaler
- Gå gjennom verktøyargumenter og format
- Sjekk server-spesifikke krav
- Implementer korrekt feilbehandling

### 3. Ytelsesproblemer
- Optimaliser verktøysamtale-frekvensen
- Implementer caching der det er hensiktsmessig
- Overvåk responstider fra serveren

## Neste steg

For å forbedre MCP-integrasjonen din ytterligere:

1. **Utforsk egendefinerte MCP-servere**: Bygg egne MCP-servere for proprietære datakilder
2. **Implementer avansert sikkerhet**: Legg til OAuth2 eller tilpassede autentiseringsmekanismer
3. **Overvåk og analyser**: Implementer logging og overvåking for verktøybruk
4. **Skaler løsningen**: Vurder lastbalansering og distribuerte MCP-server-arkitekturer

## Ekstra ressurser

- [Microsoft Foundry Dokumentasjon](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol-eksempler](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Oversikt over Microsoft Foundry-agenter](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Spesifikasjon](https://modelcontextprotocol.io/specification/2026-07-28/)

## Support

For ytterligere støtte og spørsmål:
- Se gjennom [Microsoft Foundry dokumentasjonen](https://learn.microsoft.com/azure/ai-foundry/)
- Sjekk [MCP fellesskapsressurser](https://modelcontextprotocol.io/)

## Hva nå

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->