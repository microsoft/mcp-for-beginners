# Integrácia Model Context Protocol (MCP) s Azure AI Foundry

Tento návod ukazuje, ako integrovať servery Model Context Protocol (MCP) s agentmi Azure AI Foundry, čím umožníte pokročilú orchestráciu nástrojov a podnikové AI funkcie.

## Úvod

Model Context Protocol (MCP) je otvorený štandard, ktorý umožňuje AI aplikáciám bezpečne sa pripájať k externým dátovým zdrojom a nástrojom. Po integrácii s Azure AI Foundry umožňuje MCP agentom pristupovať a interagovať s rôznymi externými službami, API a dátovými zdrojmi štandardizovaným spôsobom.

Táto integrácia spája flexibilitu ekosystému nástrojov MCP s robustným rámcom agentov Azure AI Foundry, čím poskytuje podnikové AI riešenia s rozsiahlymi možnosťami prispôsobenia.

**Note:** Ak chcete používať MCP v Azure AI Foundry Agent Service, momentálne sú podporované iba tieto regióny: westus, westus2, uaenorth, southindia a switzerlandnorth

## Ciele učenia

Na konci tohto návodu budete schopní:

- Pochopiť Model Context Protocol a jeho výhody
- Nastaviť MCP servery pre použitie s agentmi Azure AI Foundry
- Vytvoriť a nakonfigurovať agentov s integráciou MCP nástrojov
- Implementovať praktické príklady s reálnymi MCP servermi
- Spracovávať odpovede nástrojov a citácie v konverzáciách agentov

## Predpoklady

Pred začatím sa uistite, že máte:

- Predplatné Azure s prístupom k AI Foundry
- Python 3.10+ alebo .NET 8.0+
- Nainštalovaný a nakonfigurovaný Azure CLI
- Príslušné oprávnenia na vytváranie AI zdrojov

## Čo je Model Context Protocol (MCP)?

Model Context Protocol je štandardizovaný spôsob, ako sa AI aplikácie pripájajú k externým dátovým zdrojom a nástrojom. Hlavné výhody zahŕňajú:

- **Štandardizovaná integrácia**: Konzistentné rozhranie naprieč rôznymi nástrojmi a službami
- **Bezpečnosť**: Bezpečné mechanizmy autentifikácie a autorizácie
- **Flexibilita**: Podpora rôznych dátových zdrojov, API a vlastných nástrojov
- **Rozšíriteľnosť**: Jednoduché pridávanie nových funkcií a integrácií

## Nastavenie MCP s Azure AI Foundry

### Konfigurácia prostredia

Vyberte si preferované vývojové prostredie:

- [Python implementácia](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET implementácia](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python implementácia

***Note*** Tento [notebook](mcp_support_python.ipynb) môžete spustiť priamo

### 1. Inštalácia potrebných balíčkov

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

### 3. Konfigurácia nastavení MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicializácia klienta projektu

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Vytvorenie MCP nástroja

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Kompletný príklad v Pythone

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

## .NET implementácia

***Note*** Tento [notebook](mcp_support_dotnet.ipynb) môžete spustiť priamo

### 1. Inštalácia potrebných balíčkov

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Import závislostí

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigurácia nastavení

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Vytvorenie definície MCP nástroja

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Vytvorenie agenta s MCP nástrojmi

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Kompletný príklad v .NET

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

## Možnosti konfigurácie MCP nástrojov

Pri konfigurácii MCP nástrojov pre vášho agenta môžete špecifikovať niekoľko dôležitých parametrov:

### Python konfigurácia

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET konfigurácia

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentifikácia a hlavičky

Obe implementácie podporujú vlastné hlavičky pre autentifikáciu:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Riešenie bežných problémov

### 1. Problémy s pripojením
- Overte, či je URL MCP servera dostupná
- Skontrolujte autentifikačné údaje
- Uistite sa o funkčnosti siete

### 2. Zlyhania volania nástrojov
- Skontrolujte argumenty a formátovanie volaní nástrojov
- Overte špecifické požiadavky servera
- Implementujte správne spracovanie chýb

### 3. Problémy s výkonom
- Optimalizujte frekvenciu volaní nástrojov
- Používajte cache tam, kde je to vhodné
- Monitorujte časy odozvy servera

## Ďalšie kroky

Pre ďalšie vylepšenie integrácie MCP:

1. **Preskúmajte vlastné MCP servery**: Vytvorte si vlastné MCP servery pre proprietárne dátové zdroje
2. **Implementujte pokročilú bezpečnosť**: Pridajte OAuth2 alebo vlastné autentifikačné mechanizmy
3. **Monitorovanie a analytika**: Zaveste logovanie a monitorovanie používania nástrojov
4. **Škálovanie riešenia**: Zvážte load balancing a distribuované architektúry MCP serverov

## Dodatočné zdroje

- [Dokumentácia Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Príklady Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Prehľad agentov Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Špecifikácia MCP](https://spec.modelcontextprotocol.io/)

## Podpora

Pre ďalšiu podporu a otázky:
- Prezrite si [dokumentáciu Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Skontrolujte [komunitné zdroje MCP](https://modelcontextprotocol.io/)

## Čo ďalej

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.