# Integracija Model Context Protocol (MCP) s Microsoft Foundry

Ta vodič prikazuje, kako integrirati strežnike Model Context Protocol (MCP) z Microsoft Foundry agenti, kar omogoča zmogljivo orkestracijo orodij in zmogljivosti podjetniške umetne inteligence.

## Uvod

Model Context Protocol (MCP) je odprt standard, ki omogoča aplikacijam umetne inteligence varno povezavo z zunanjimi viri podatkov in orodji. Ko je integriran z Microsoft Foundry, MCP omogoča agentom dostop do različnih zunanjih storitev, API-jev in virov podatkov na standardiziran način.

Ta integracija združuje prilagodljivost MCP-ovega ekosistema orodij z robustnim ogrodjem Microsoft Foundry agentov, kar ponuja rešitve umetne inteligence ravni podjetij z obsežnimi možnostmi prilagajanja.

**Opomba:** Če želite uporabiti MCP v Microsoft Foundry Agent Service, so trenutno podprte le naslednje regije: westus, westus2, uaenorth, southindia in switzerlandnorth

## Cilji učenja

Do konca tega vodiča boste sposobni:

- Razumeti Model Context Protocol in njegove prednosti
- Nastaviti MCP strežnike za uporabo z Microsoft Foundry agenti
- Ustvariti in konfigurirati agente z integracijo MCP orodij
- Izvesti praktične primere z uporabo pravih MCP strežnikov
- Obvladovati odzive orodij in navedbe v pogovorih agentov

## Predpogoji

Pred začetkom zagotovite, da imate:

- Azure naročnino z dostopom do Microsoft Foundry
- Python 3.10+ ali .NET 8.0+
- Namestljen in konfiguriran Azure CLI
- Pravilne pravice za ustvarjanje AI virov

## Kaj je Model Context Protocol (MCP)?

Model Context Protocol je standardiziran način, kako se aplikacije umetne inteligence povezujejo z zunanjimi viri podatkov in orodji. Ključne prednosti vključujejo:

- **Standardizirana integracija**: Konsistenten vmesnik med različnimi orodji in storitvami
- **Varnost**: Varnostni mehanizmi za avtentikacijo in avtorizacijo
- **Prilagodljivost**: Podpora za različne vire podatkov, API-je in prilagojena orodja
- **Razširljivost**: Enostavno dodajanje novih zmogljivosti in integracij

## Nastavitev MCP z Microsoft Foundry

### Konfiguracija okolja

Izberite želeno razvojno okolje:

- [Implementacija v Pythonu](#implementacija-v-pythonu)
- [Implementacija v .NET-u](#codeblock5)

---

## Implementacija v Pythonu

***Opomba*** Ta [zvezek](./mcp_support_python.ipynb) lahko zaženete

### 1. Namestitev zahtevanih paketov

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Uvoz odvisnosti

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfiguracija nastavitev MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicializacija projektnega odjemalca

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Ustvarjanje MCP orodja

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Neobvezno: določite dovoljena orodja
)
```

### 6. Popoln primer v Pythonu

```python
with project_client:
    agents_client = project_client.agents

    # Ustvari novega agenta z MCP orodji
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Ustvari nit za komunikacijo
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Ustvari sporočilo za nit
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Obdelaj odobritve orodij in zaženi agenta
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

    # Prikaži pogovor
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

## Implementacija v .NET-u

***Opomba*** Ta [zvezek](./mcp_support_dotnet.ipynb) lahko zaženete

### 1. Namestitev zahtevanih paketov

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Uvoz odvisnosti

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfiguracija nastavitev

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Ustvarjanje definicije MCP orodja

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Ustvarjanje agenta z MCP orodji

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Popoln primer v .NET-u

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

## Možnosti konfiguracije MCP orodij

Pri konfiguraciji MCP orodij za vašega agenta lahko določite več pomembnih parametrov:

### Konfiguracija za Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifikator za MCP strežnik
    server_url="https://api.example.com/mcp", # Končna točka MCP strežnika
    allowed_tools=[],                       # Neobvezno: določite dovoljena orodja
)
```

### Konfiguracija za .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Avtentikacija in zaglavja

Obe implementaciji podpirata prilagojena zaglavja za avtentikacijo:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Odpravljanje pogostih težav

### 1. Težave s povezavo
- Preverite, ali je MCP strežnik dosegljiv preko URL
- Preverite podatke za avtentikacijo
- Zagotovite omrežno povezljivost

### 2. Napake pri klicu orodja
- Preverite argumente in oblikovanje orodja
- Upoštevajte zahteve, specifične za strežnik
- Implementirajte ustrezno obravnavo napak

### 3. Težave z zmogljivostjo
- Optimizirajte pogostost klicev orodja
- Uporabite predpomnjenje tam, kjer je primerno
- Spremljajte čase odziva strežnika

## Naslednji koraki

Za nadaljnjo izboljšavo integracije MCP:

1. **Raziščite prilagojene MCP strežnike**: Zgradite svoje MCP strežnike za lastne vire podatkov
2. **Izvedite napredno varnost**: Dodajte OAuth2 ali druge mehanizme prilagojene avtentikacije
3. **Nadzor in analitika**: Implementirajte beleženje in spremljanje uporabe orodij
4. **Razširite svojo rešitev**: Razmislite o uravnoteženju obremenitve in distribuiranih arhitekturah MCP strežnikov

## Dodatni viri

- [Dokumentacija Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Vzorec Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Pregled Microsoft Foundry agentov](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Specifikacija MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Podpora

Za dodatno podporo in vprašanja:
- Preberite [dokumentacijo Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Oglejte si [skupnostne vire MCP](https://modelcontextprotocol.io/)

## Kaj sledi

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->