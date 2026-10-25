# Model Context Protocol (MCP) integreerimine Microsoft Foundryga

See juhend demonstreerib, kuidas integreerida Model Context Protocoli (MCP) serverid Microsoft Foundry agentidega, võimaldades võimsat tööriistade orkestreerimist ja ettevõtte tehisintellekti võimekust.

## Sissejuhatus

Model Context Protocol (MCP) on avatud standard, mis võimaldab tehisintellekti rakendustel turvaliselt ühendada väliste andmeallikate ja tööriistadega. Kui integreeritud Microsoft Foundryga, võimaldab MCP agentidel juurdepääsu ja suhtlemist erinevate väliste teenuste, API-de ja andmeallikatega standardiseeritud viisil.

See integratsioon ühendab MCP tööriistade ökosüsteemi paindlikkuse Microsoft Foundry tugeva agentide raamistikuga, pakkudes ettevõtte tasemel tehisintellekti lahendusi laialdaste kohandamisvõimalustega.

> **Märkus:** Kui soovite kasutada MCP-d Microsoft Foundry Agent Service'is, toetatakse hetkel ainult järgmisi regioone: westus, westus2, uaenorth, southindia ja switzerlandnorth

## Õpitulemused

Pärast selle juhendi läbimist oskate:

- Mõista Model Context Protocoli ja selle eeliseid
- Seada üles MCP serverid kasutamiseks Microsoft Foundry agentidega
- Luua ja konfigureerida agente MCP tööriistaintegratsiooniga
- Rakendada praktilisi näiteid, kasutades tegelikke MCP servereid
- Töötleda tööriistade vastuseid ja viiteid agendi vestlustes

## Eeltingimused

Enne alustamist veenduge, et teil on:

- Azure'i tellimus Microsoft Foundry juurdepääsuga
- Python 3.10+ või .NET 8.0+
- Azure CLI installitud ja konfigureeritud
- Sobivad õigused AI ressursside loomiseks

## Mis on Model Context Protocol (MCP)?

Model Context Protocol on standardiseeritud viis, mille abil tehisintellekti rakendused saavad ühendada väliste andmeallikate ja tööriistadega. Peamised eelised on:

- **Standardiseeritud integratsioon**: Ühtne liides erinevate tööriistade ja teenuste vahel
- **Turvalisus**: Turvalised autentimise ja autoriseerimise mehhanismid
- **Paindlikkus**: Tugi erinevatele andmeallikatele, API-dele ja kohandatud tööriistadele
- **Laiendatavus**: Uute võimekuste ja integratsioonide lihtne lisamine

## MCP seadistamine Microsoft Foundryga

### Keskkonna seadistus

Valige soovitud arenduskeskkond:

- [Pythoni implementatsioon](#python-implementation)
- [.NETi implementatsioon](#net-implementation)

---

## Pythoni implementatsioon

***Märkus*** Saate käivitada selle [märkmiku](./mcp_support_python.ipynb)

### 1. Vajalike pakettide installimine

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Sõltuvuste importimine

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP seadete konfigureerimine

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Projekti kliendi initsialiseerimine

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP tööriista loomine

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Täielik Pythoni näide

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

## .NETi implementatsioon

***Märkus*** Saate käivitada selle [märkmiku](./mcp_support_dotnet.ipynb)

### 1. Vajalike pakettide installimine

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Sõltuvuste importimine

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Seadete konfigureerimine

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP tööriista määratluse loomine

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Agendi loomine MCP tööriistadega

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Täielik .NET näide

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

## MCP tööriista konfigureerimisvalikud

MCP tööriistade konfigureerimisel teie agendi jaoks saate määrata mitmeid olulisi parameetreid:

### Pythoni konfiguratsioon

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET konfiguratsioon

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentimine ja päised

Mõlemad implementatsioonid toetavad autentimiseks kohandatud päiseid:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Levinud probleemide tõrkeotsing

### 1. Ühenduse probleemid
- Kontrollige, et MCP serveri URL oleks ligipääsetav
- Kontrollige autentimisandmeid
- Veenduge võrguühenduses

### 2. Tööriista kutsumise tõrked
- Kontrollige tööriista argumente ja vormingut
- Kontrollige serverispetsiifilisi nõudeid
- Rakendage sobiv veahaldus

### 3. Jõudlusprobleemid
- Optimeerige tööriistakutse sagedust
- Rakendage vajadusel vahemällu salvestamist
- Jälgige serveri vastuse aegu

## Edasised sammud

Oma MCP integratsiooni edasiseks täiustamiseks:

1. **Uurige kohandatud MCP servereid**: Looge oma MCP serverid ettevõtte enda andmeallikate jaoks
2. **Rakendage täiustatud turvalisust**: Lisage OAuth2 või kohandatud autentimismehhanismid
3. **Jälgimine ja analüütika**: Rakendage logimist ja jälgimist tööriistade kasutuse jaoks
4. **Skaalake oma lahendust**: Kaaluge koormuse jagamist ja hajutatud MCP serverite arhitektuure

## Täiendavad ressursid

- [Microsoft Foundry dokumentatsioon](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol näited](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry agentide ülevaade](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP spetsifikatsioon](https://modelcontextprotocol.io/specification/2026-07-28/)

## Tugi

Lisatoe ja küsimuste korral:
- Vaadake üle [Microsoft Foundry dokumentatsiooni](https://learn.microsoft.com/azure/ai-foundry/)
- Kontrollige [MCP kogukonna ressursse](https://modelcontextprotocol.io/)

## Mis järgmiseks 

- [5.14 MCP konteksti inseneritöö](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->