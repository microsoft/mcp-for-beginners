# Integracija protokola konteksta modela (MCP) s Microsoft Foundry

Ovaj vodič pokazuje kako integrirati poslužitelje protokola konteksta modela (MCP) s agentima Microsoft Foundry, omogućujući snažnu orkestraciju alata i mogućnosti AI za poduzeća.

## Uvod

Protokol konteksta modela (MCP) otvoreni je standard koji omogućuje AI aplikacijama sigurnu vezu s vanjskim izvorima podataka i alatima. Kada je integriran s Microsoft Foundry, MCP omogućuje agentima pristup i interakciju s raznim vanjskim uslugama, API-jima i izvorima podataka na standardizirani način.

Ova integracija kombinira fleksibilnost MCP-ovog ekosustava alata s robusnim okvirom Microsoft Foundry agenata, pružajući AI rješenja razine poduzeća s opsežnim mogućnostima prilagodbe.

> **Napomena:** Ako želite koristiti MCP u Microsoft Foundry Agent Service, trenutno su podržane samo sljedeće regije: westus, westus2, uaenorth, southindia i switzerlandnorth

## Ciljevi učenja

Do kraja ovog vodiča moći ćete:

- Razumjeti protokol konteksta modela i njegove prednosti
- Postaviti MCP poslužitelje za korištenje s Microsoft Foundry agentima
- Kreirati i konfigurirati agente s MCP integracijom alata
- Implementirati praktične primjere koristeći stvarne MCP poslužitelje
- Rukovati odgovorima alata i citatima u razgovorima agenata

## Preduvjeti

Prije početka, osigurajte da imate:

- Pretplatu na Azure s pristupom Microsoft Foundry
- Python 3.10+ ili .NET 8.0+
- Instaliran i konfiguriran Azure CLI
- Odgovarajuće dozvole za kreaciju AI resursa

## Što je protokol konteksta modela (MCP)?

Protokol konteksta modela je standardizirani način za AI aplikacije za povezivanje s vanjskim izvorima podataka i alatima. Ključne prednosti uključuju:

- **Standardizirana integracija**: Konzistentno sučelje preko različitih alata i usluga
- **Sigurnost**: Sigurni mehanizmi autentikacije i autorizacije
- **Fleksibilnost**: Podrška za razne izvore podataka, API-je i prilagođene alate
- **Proširivost**: Lako dodavanje novih mogućnosti i integracija

## Postavljanje MCP-a s Microsoft Foundry

### Konfiguracija okoline

Odaberite svoj preferirani razvojni okoliš:

- [Python implementacija](#python-implementation)
- [.NET implementacija](#net-implementation)

---

## Python implementacija

***Napomena*** Možete pokrenuti ovaj [notebook](./mcp_support_python.ipynb)

### 1. Instalirajte potrebne pakete

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Uvezite ovisnosti

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigurirajte postavke MCP-a

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicijalizirajte projektni klijent

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Kreirajte MCP alat

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Cjelovit Python primjer

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

## .NET implementacija

***Napomena*** Možete pokrenuti ovaj [notebook](./mcp_support_dotnet.ipynb)

### 1. Instalirajte potrebne pakete

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Uvezite ovisnosti

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurirajte postavke

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Kreirajte definiciju MCP alata

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Kreirajte agenta s MCP alatima

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Cjelovit .NET primjer

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

## Opcije konfiguracije MCP alata

Prilikom konfiguriranja MCP alata za svog agenta možete specificirati nekoliko važnih parametara:

### Python konfiguracija

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET konfiguracija

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentikacija i zaglavlja

Obje implementacije podržavaju prilagođena zaglavlja za autentikaciju:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Rješavanje uobičajenih problema

### 1. Problemi s povezivanjem
- Provjerite je li URL MCP poslužitelja dostupan
- Provjerite vjerodajnice za autentikaciju
- Osigurajte mrežnu povezanost

### 2. Neuspjesi poziva alata
- Pregledajte argumente alata i formatiranje
- Provjerite zahtjeve specifične za poslužitelj
- Implementirajte pravilno rukovanje pogreškama

### 3. Problemi s izvedbom
- Optimizirajte učestalost poziva alata
- Implementirajte predmemoriranje gdje je prikladno
- Nadgledajte vrijeme odgovora poslužitelja

## Sljedeći koraci

Kako biste dodatno unaprijedili svoju MCP integraciju:

1. **Istražite prilagođene MCP poslužitelje**: Izgradite vlastite MCP poslužitelje za vlasničke izvore podataka
2. **Implementirajte naprednu sigurnost**: Dodajte OAuth2 ili prilagođene mehanizme autentikacije
3. **Nadzor i analitika**: Implementirajte zapisivanje i nadzor korištenja alata
4. **Škalu vaše rješenje**: Razmotrite balansiranje opterećenja i distribuirane arhitekture MCP poslužitelja

## Dodatni resursi

- [Microsoft Foundry dokumentacija](https://learn.microsoft.com/azure/ai-foundry/)
- [Primjeri protokola konteksta modela](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Pregled agenata Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP specifikacija](https://modelcontextprotocol.io/specification/2026-07-28/)

## Podrška

Za dodatnu podršku i pitanja:
- Pregledajte [Microsoft Foundry dokumentaciju](https://learn.microsoft.com/azure/ai-foundry/)
- Provjerite [MCP zajedničke resurse](https://modelcontextprotocol.io/)

## Što dalje

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->