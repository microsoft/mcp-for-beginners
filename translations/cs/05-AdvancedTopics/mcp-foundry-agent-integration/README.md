# Integrace Model Context Protocol (MCP) s Azure AI Foundry

Tento průvodce ukazuje, jak integrovat servery Model Context Protocol (MCP) s agenty Azure AI Foundry, což umožňuje pokročilou orchestraci nástrojů a podnikové AI funkce.

## Úvod

Model Context Protocol (MCP) je otevřený standard, který umožňuje AI aplikacím bezpečně se připojit k externím datovým zdrojům a nástrojům. Po integraci s Azure AI Foundry umožňuje MCP agentům přístup a interakci s různými externími službami, API a datovými zdroji jednotným způsobem.

Tato integrace kombinuje flexibilitu ekosystému nástrojů MCP s robustním rámcem agentů Azure AI Foundry, čímž poskytuje podniková AI řešení s rozsáhlými možnostmi přizpůsobení.

**Note:** Pokud chcete používat MCP v Azure AI Foundry Agent Service, aktuálně jsou podporovány pouze následující regiony: westus, westus2, uaenorth, southindia a switzerlandnorth

## Cíle učení

Na konci tohoto průvodce budete schopni:

- Pochopit Model Context Protocol a jeho výhody
- Nastavit MCP servery pro použití s agenty Azure AI Foundry
- Vytvořit a nakonfigurovat agenty s integrací MCP nástrojů
- Implementovat praktické příklady s reálnými MCP servery
- Zpracovávat odpovědi nástrojů a citace v konverzacích agentů

## Požadavky

Před začátkem se ujistěte, že máte:

- Azure předplatné s přístupem k AI Foundry
- Python 3.10+ nebo .NET 8.0+
- Nainstalovaný a nakonfigurovaný Azure CLI
- Odpovídající oprávnění pro vytváření AI zdrojů

## Co je Model Context Protocol (MCP)?

Model Context Protocol je standardizovaný způsob, jak mohou AI aplikace přistupovat k externím datovým zdrojům a nástrojům. Mezi hlavní výhody patří:

- **Standardizovaná integrace**: Konzistentní rozhraní napříč různými nástroji a službami
- **Bezpečnost**: Bezpečné mechanismy autentizace a autorizace
- **Flexibilita**: Podpora různých datových zdrojů, API a vlastních nástrojů
- **Rozšiřitelnost**: Snadné přidávání nových funkcí a integrací

## Nastavení MCP s Azure AI Foundry

### Konfigurace prostředí

Vyberte si preferované vývojové prostředí:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** Tento [notebook](mcp_support_python.ipynb) můžete spustit

### 1. Instalace požadovaných balíčků

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Import závislostí

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigurace nastavení MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicializace klienta projektu

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Vytvoření MCP nástroje

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Kompletní příklad v Pythonu

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

***Note*** Tento [notebook](mcp_support_dotnet.ipynb) můžete spustit

### 1. Instalace požadovaných balíčků

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Import závislostí

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurace nastavení

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Vytvoření definice MCP nástroje

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Vytvoření agenta s MCP nástroji

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Kompletní příklad v .NET

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

## Možnosti konfigurace MCP nástrojů

Při konfiguraci MCP nástrojů pro vaše agenty můžete specifikovat několik důležitých parametrů:

### Python konfigurace

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET konfigurace

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentizace a hlavičky

Obě implementace podporují vlastní hlavičky pro autentizaci:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Řešení běžných problémů

### 1. Problémy s připojením
- Ověřte, že je URL MCP serveru dostupná
- Zkontrolujte autentizační údaje
- Ujistěte se o síťové konektivitě

### 2. Selhání volání nástroje
- Zkontrolujte argumenty a formátování volání nástroje
- Ověřte specifické požadavky serveru
- Implementujte správné zpracování chyb

### 3. Výkonové problémy
- Optimalizujte frekvenci volání nástrojů
- Použijte cache tam, kde je to vhodné
- Sledujte dobu odezvy serveru

## Další kroky

Pro další vylepšení integrace MCP:

1. **Prozkoumejte vlastní MCP servery**: Vytvořte si vlastní MCP servery pro proprietární datové zdroje
2. **Implementujte pokročilou bezpečnost**: Přidejte OAuth2 nebo vlastní autentizační mechanismy
3. **Monitorování a analýzy**: Zavádějte logování a sledování využití nástrojů
4. **Škálování řešení**: Zvažte load balancing a distribuované architektury MCP serverů

## Další zdroje

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## Podpora

Pro další podporu a dotazy:
- Prohlédněte si [dokumentaci Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Navštivte [MCP komunitní zdroje](https://modelcontextprotocol.io/)

## Co dál

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.