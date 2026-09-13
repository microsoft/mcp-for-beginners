# Integrace Model Context Protocol (MCP) s Microsoft Foundry

Tento průvodce ukazuje, jak integrovat servery Model Context Protocol (MCP) s agenty Microsoft Foundry, což umožňuje výkonnou orchestraci nástrojů a podnikové AI schopnosti.

## Úvod

Model Context Protocol (MCP) je otevřený standard, který umožňuje AI aplikacím bezpečně se připojit k externím datovým zdrojům a nástrojům. Když je integrován s Microsoft Foundry, MCP umožňuje agentům přístup k různým externím službám, API a datovým zdrojům a komunikaci s nimi standardizovaným způsobem.

Tato integrace kombinuje flexibilitu ekosystému nástrojů MCP s robustním rámcem agentů Microsoft Foundry, což poskytuje podnikové AI řešení s rozsáhlými možnostmi přizpůsobení.

**Poznámka:** Pokud chcete používat MCP v Microsoft Foundry Agent Service, aktuálně jsou podporovány pouze následující regiony: westus, westus2, uaenorth, southindia a switzerlandnorth

## Cíle učení

Na konci tohoto průvodce budete schopni:

- Porozumět Model Context Protocol a jeho přínosům
- Nastavit servery MCP pro použití s agenty Microsoft Foundry
- Vytvořit a nakonfigurovat agenty s integrací nástrojů MCP
- Implementovat praktické příklady využívající skutečné servery MCP
- Zpracovávat odpovědi nástrojů a citace v konverzacích agentů

## Předpoklady

Před zahájením se ujistěte, že máte:

- Předplatné Azure s přístupem k Microsoft Foundry
- Python 3.10+ nebo .NET 8.0+
- Nainstalovaný a nakonfigurovaný Azure CLI
- Odpovídající oprávnění pro vytváření AI zdrojů

## Co je Model Context Protocol (MCP)?

Model Context Protocol je standardizovaný způsob, jak může AI aplikace přistupovat k externím datovým zdrojům a nástrojům. Klíčové výhody zahrnují:

- **Standardizovaná integrace**: Konzistentní rozhraní napříč různými nástroji a službami
- **Bezpečnost**: Bezpečné mechanismy ověřování a autorizace
- **Flexibilita**: Podpora různých datových zdrojů, API a vlastních nástrojů
- **Rozšiřitelnost**: Jednoduché přidávání nových schopností a integrací

## Nastavení MCP s Microsoft Foundry

### Konfigurace prostředí

Vyberte preferované vývojové prostředí:

- [Python implementace](#python-implementace)
- [.NET implementace](#codeblock5)

---

## Python implementace

***Poznámka*** Tento [notebook](./mcp_support_python.ipynb) můžete spustit

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
    allowed_tools=[],  # Volitelné: specifikujte povolené nástroje
)
```

### 6. Kompletní příklad v Pythonu

```python
with project_client:
    agents_client = project_client.agents

    # Vytvořit nového agenta s nástroji MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Vytvořit vlákno pro komunikaci
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Vytvořit zprávu pro vlákno
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Zpracovat schválení nástrojů a spustit agenta
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

    # Zobrazit konverzaci
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

## .NET implementace

***Poznámka*** Tento [notebook](./mcp_support_dotnet.ipynb) můžete spustit

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

Při konfiguraci MCP nástrojů pro vaše agenty můžete určit několik důležitých parametrů:

### Konfigurace v Pythonu

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifikátor serveru MCP
    server_url="https://api.example.com/mcp", # Konec bodu serveru MCP
    allowed_tools=[],                       # Volitelné: specifikujte povolené nástroje
)
```

### Konfigurace v .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Ověřování a hlavičky

Obě implementace podporují vlastní hlavičky pro ověřování:

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
- Ověřte, že je URL serveru MCP přístupné
- Zkontrolujte přihlašovací údaje
- Ujistěte se o síťové konektivitě

### 2. Selhání zavolání nástrojů
- Zkontrolujte argumenty a formátování nástroje
- Dodržujte specifické požadavky serveru
- Implementujte správné zacházení s chybami

### 3. Výkonnostní problémy
- Optimalizujte frekvenci volání nástrojů
- Použijte cachování tam, kde je vhodné
- Sledujte časy odezvy serveru

## Další kroky

Pro další vylepšení vaší integrace MCP:

1. **Prozkoumejte vlastní MCP servery**: Vytvořte své vlastní MCP servery pro proprietární datové zdroje
2. **Implementujte pokročilou bezpečnost**: Přidejte OAuth2 nebo vlastní autentizační mechanismy
3. **Monitorování a analytika**: Implementujte logování a sledování využití nástrojů
4. **Škálování řešení**: Zvažte vyvažování zátěže a distribuované architektury MCP serverů

## Další zdroje

- [Dokumentace Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Ukázky Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Přehled agentů Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Specifikace MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Podpora

Pro další podporu a dotazy:
- Prohlédněte si [dokumentaci Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Zkontrolujte [komunitní zdroje MCP](https://modelcontextprotocol.io/)

## Co dál

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->