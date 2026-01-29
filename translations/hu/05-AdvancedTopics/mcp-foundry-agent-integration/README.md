# Model Context Protocol (MCP) integráció az Azure AI Foundry-val

Ez az útmutató bemutatja, hogyan lehet integrálni a Model Context Protocol (MCP) szervereket az Azure AI Foundry ügynökeivel, lehetővé téve a hatékony eszközkoordinációt és vállalati szintű mesterséges intelligencia képességeket.

## Bevezetés

A Model Context Protocol (MCP) egy nyílt szabvány, amely lehetővé teszi az AI alkalmazások számára, hogy biztonságosan csatlakozzanak külső adatforrásokhoz és eszközökhöz. Az Azure AI Foundry-val való integráció során az MCP lehetővé teszi az ügynökök számára, hogy szabványos módon hozzáférjenek és kommunikáljanak különböző külső szolgáltatásokkal, API-kkal és adatforrásokkal.

Ez az integráció ötvözi az MCP eszközök ökoszisztémájának rugalmasságát az Azure AI Foundry robusztus ügynökkeretével, így vállalati szintű AI megoldásokat kínál széles körű testreszabási lehetőségekkel.

**Megjegyzés:** Ha az MCP-t az Azure AI Foundry Agent Service-ben szeretnéd használni, jelenleg csak a következő régiók támogatottak: westus, westus2, uaenorth, southindia és switzerlandnorth

## Tanulási célok

Az útmutató végére képes leszel:

- Megérteni a Model Context Protocol működését és előnyeit
- Beállítani MCP szervereket az Azure AI Foundry ügynökeivel való használathoz
- Ügynököket létrehozni és konfigurálni MCP eszközintegrációval
- Gyakorlati példákat megvalósítani valódi MCP szerverek használatával
- Kezelni az eszközválaszokat és hivatkozásokat az ügynöki beszélgetések során

## Előfeltételek

A kezdés előtt győződj meg róla, hogy rendelkezel:

- Azure előfizetéssel, amely hozzáférést biztosít az AI Foundry-hoz
- Python 3.10+ vagy .NET 8.0+ környezettel
- Telepített és konfigurált Azure CLI-vel
- Megfelelő jogosultságokkal AI erőforrások létrehozásához

## Mi az a Model Context Protocol (MCP)?

A Model Context Protocol egy szabványosított módja annak, hogy az AI alkalmazások külső adatforrásokhoz és eszközökhöz csatlakozzanak. Fő előnyei:

- **Szabványosított integráció**: Egységes felület különböző eszközök és szolgáltatások között
- **Biztonság**: Biztonságos hitelesítési és engedélyezési mechanizmusok
- **Rugalmasság**: Támogatja a különféle adatforrásokat, API-kat és egyedi eszközöket
- **Bővíthetőség**: Könnyen hozzáadhatók új funkciók és integrációk

## MCP beállítása az Azure AI Foundry-val

### Környezet konfigurálása

Válaszd ki a számodra megfelelő fejlesztői környezetet:

- [Python megvalósítás](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET megvalósítás](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python megvalósítás

***Megjegyzés*** Ezt a [notebookot](mcp_support_python.ipynb) is futtathatod

### 1. Szükséges csomagok telepítése

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Függőségek importálása

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP beállítások konfigurálása

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Projekt kliens inicializálása

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP eszköz létrehozása

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Teljes Python példa

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

## .NET megvalósítás

***Megjegyzés*** Ezt a [notebookot](mcp_support_dotnet.ipynb) is futtathatod

### 1. Szükséges csomagok telepítése

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Függőségek importálása

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Beállítások konfigurálása

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP eszköz definíció létrehozása

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Ügynök létrehozása MCP eszközökkel

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Teljes .NET példa

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

## MCP eszköz konfigurációs lehetőségek

Az MCP eszközök konfigurálásakor több fontos paramétert is megadhatsz az ügynököd számára:

### Python konfiguráció

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET konfiguráció

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Hitelesítés és fejléc beállítások

Mindkét megvalósítás támogatja az egyedi fejlécek használatát a hitelesítéshez:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Gyakori problémák elhárítása

### 1. Kapcsolódási problémák
- Ellenőrizd, hogy az MCP szerver URL elérhető-e
- Nézd át a hitelesítési adatokat
- Győződj meg a hálózati kapcsolat meglétéről

### 2. Eszközhívás hibák
- Vizsgáld meg az eszköz argumentumait és formátumát
- Ellenőrizd a szerver specifikus követelményeket
- Valósíts meg megfelelő hibakezelést

### 3. Teljesítmény problémák
- Optimalizáld az eszközhívások gyakoriságát
- Használj gyorsítótárazást, ahol indokolt
- Figyeld a szerver válaszidejét

## Következő lépések

Az MCP integrációd további fejlesztéséhez:

1. **Ismerd meg az egyedi MCP szervereket**: Építs saját MCP szervereket saját adatforrásokhoz
2. **Valósíts meg fejlett biztonságot**: Adj hozzá OAuth2 vagy egyedi hitelesítési mechanizmusokat
3. **Monitorozás és elemzés**: Valósíts meg naplózást és monitorozást az eszközhasználathoz
4. **Skálázd megoldásodat**: Gondolkodj terheléselosztásban és elosztott MCP szerver architektúrákban

## További források

- [Azure AI Foundry dokumentáció](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol minták](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry ügynökök áttekintése](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP specifikáció](https://spec.modelcontextprotocol.io/)

## Támogatás

További támogatásért és kérdések esetén:
- Tekintsd át az [Azure AI Foundry dokumentációt](https://learn.microsoft.com/azure/ai-foundry/)
- Nézd meg az [MCP közösségi forrásokat](https://modelcontextprotocol.io/)

## Mi következik

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.