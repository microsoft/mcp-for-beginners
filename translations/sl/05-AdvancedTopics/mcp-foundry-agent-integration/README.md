# Integracija Model Context Protocol (MCP) z Azure AI Foundry

Ta vodič prikazuje, kako integrirati strežnike Model Context Protocol (MCP) z agenti Azure AI Foundry, kar omogoča zmogljivo orkestracijo orodij in podjetniške AI zmogljivosti.

## Uvod

Model Context Protocol (MCP) je odprt standard, ki omogoča AI aplikacijam varno povezavo z zunanjimi podatkovnimi viri in orodji. Ko je integriran z Azure AI Foundry, MCP agentom omogoča dostop do različnih zunanjih storitev, API-jev in podatkovnih virov na standardiziran način.

Ta integracija združuje prilagodljivost MCP-ovega ekosistema orodij z robustnim agentnim ogrodjem Azure AI Foundry, kar zagotavlja podjetniške AI rešitve z obsežnimi možnostmi prilagajanja.

**Note:** Če želite uporabljati MCP v Azure AI Foundry Agent Service, so trenutno podprte le naslednje regije: westus, westus2, uaenorth, southindia in switzerlandnorth

## Cilji učenja

Ob koncu tega vodiča boste znali:

- Razumeti Model Context Protocol in njegove prednosti
- Nastaviti MCP strežnike za uporabo z agenti Azure AI Foundry
- Ustvariti in konfigurirati agente z integracijo MCP orodij
- Izvesti praktične primere z uporabo pravih MCP strežnikov
- Obvladovati odzive orodij in navajanja v pogovorih agentov

## Predpogoji

Pred začetkom poskrbite, da imate:

- Azure naročnino z dostopom do AI Foundry
- Python 3.10+ ali .NET 8.0+
- Nameščen in konfiguriran Azure CLI
- Ustrezna dovoljenja za ustvarjanje AI virov

## Kaj je Model Context Protocol (MCP)?

Model Context Protocol je standardiziran način, da se AI aplikacije povežejo z zunanjimi podatkovnimi viri in orodji. Ključne prednosti vključujejo:

- **Standardizirana integracija**: Enoten vmesnik za različna orodja in storitve
- **Varnost**: Varni mehanizmi za avtentikacijo in avtorizacijo
- **Prilagodljivost**: Podpora za različne podatkovne vire, API-je in prilagojena orodja
- **Razširljivost**: Enostavno dodajanje novih zmogljivosti in integracij

## Nastavitev MCP z Azure AI Foundry

### Konfiguracija okolja

Izberite želeno razvojno okolje:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** Lahko zaženete ta [notebook](mcp_support_python.ipynb)

### 1. Namestite potrebne pakete

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

### 3. Konfigurirajte nastavitve MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicializirajte projektni odjemalec

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Ustvarite MCP orodje

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Celovit Python primer

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

***Note*** Lahko zaženete ta [notebook](mcp_support_dotnet.ipynb)

### 1. Namestite potrebne pakete

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Uvoz odvisnosti

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurirajte nastavitve

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Ustvarite definicijo MCP orodja

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Ustvarite agenta z MCP orodji

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Celovit .NET primer

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

## Avtentikacija in glave

Obe implementaciji podpirata prilagojene glave za avtentikacijo:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Reševanje pogostih težav

### 1. Težave s povezavo
- Preverite, ali je URL MCP strežnika dostopen
- Preverite avtentikacijske podatke
- Zagotovite omrežno povezljivost

### 2. Napake pri klicu orodij
- Preglejte argumente in oblikovanje klicev orodij
- Preverite zahteve specifične za strežnik
- Uvedite ustrezno obravnavo napak

### 3. Težave z zmogljivostjo
- Optimizirajte pogostost klicev orodij
- Uporabite predpomnjenje, kjer je primerno
- Spremljajte odzivne čase strežnika

## Naslednji koraki

Za nadaljnje izboljšanje vaše MCP integracije:

1. **Raziskujte prilagojene MCP strežnike**: Zgradite svoje MCP strežnike za lastne podatkovne vire
2. **Izvedite napredno varnost**: Dodajte OAuth2 ali prilagojene mehanizme avtentikacije
3. **Spremljanje in analitika**: Uvedite beleženje in spremljanje uporabe orodij
4. **Razširite svojo rešitev**: Razmislite o uravnoteženju obremenitev in distribuiranih arhitekturah MCP strežnikov

## Dodatni viri

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## Podpora

Za dodatno podporo in vprašanja:
- Preglejte [dokumentacijo Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Oglejte si [MCP skupnostne vire](https://modelcontextprotocol.io/)

## Kaj sledi

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.