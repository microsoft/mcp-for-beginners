# Model Context Protocoli (MCP) integreerimine Azure AI Foundryga

See juhend näitab, kuidas integreerida Model Context Protocol (MCP) serverid Azure AI Foundry agentidega, võimaldades võimsat tööriistade orkestreerimist ja ettevõtte AI võimekust.

## Sissejuhatus

Model Context Protocol (MCP) on avatud standard, mis võimaldab AI rakendustel turvaliselt ühenduda väliste andmeallikate ja tööriistadega. MCP integreerimine Azure AI Foundryga võimaldab agentidel juurdepääsu erinevatele välisteenustele, API-dele ja andmeallikatele standardiseeritud viisil.

See integreerimine ühendab MCP tööriistade ökosüsteemi paindlikkuse Azure AI Foundry tugeva agentide raamistikuga, pakkudes ettevõtte tasemel AI lahendusi ulatuslike kohandamisvõimalustega.

**Märkus:** Kui soovite kasutada MCP-d Azure AI Foundry Agent Service'is, on praegu toetatud ainult järgmised piirkonnad: westus, westus2, uaenorth, southindia ja switzerlandnorth.

## Õpieesmärgid

Selle juhendi lõpuks oskate:

- Mõista Model Context Protocoli ja selle eeliseid
- Seadistada MCP servereid Azure AI Foundry agentide jaoks
- Luua ja konfigureerida agente MCP tööriistade integreerimisega
- Rakendada praktilisi näiteid, kasutades reaalseid MCP servereid
- Käsitleda tööriistade vastuseid ja viiteid agentide vestlustes

## Eeltingimused

Enne alustamist veenduge, et teil on:

- Azure'i tellimus koos AI Foundry juurdepääsuga
- Python 3.10+ või .NET 8.0+
- Paigaldatud ja konfigureeritud Azure CLI
- Sobivad õigused AI ressursside loomiseks

## Mis on Model Context Protocol (MCP)?

Model Context Protocol on standardiseeritud viis, kuidas AI rakendused ühenduvad väliste andmeallikate ja tööriistadega. Peamised eelised hõlmavad:

- **Standardiseeritud integreerimine**: Ühtne liides erinevate tööriistade ja teenuste jaoks
- **Turvalisus**: Turvalised autentimise ja autoriseerimise mehhanismid
- **Paindlikkus**: Tugi erinevatele andmeallikatele, API-dele ja kohandatud tööriistadele
- **Laiendatavus**: Lihtne lisada uusi funktsioone ja integreerimisi

## MCP seadistamine Azure AI Foundryga

### Keskkonna konfiguratsioon

Valige oma eelistatud arenduskeskkond:

- [Python Implementatsioon](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementatsioon](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementatsioon

***Märkus*** Võite käivitada selle [märkmiku](./mcp_support_python.ipynb)

### 1. Paigaldage vajalikud paketid

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importige sõltuvused

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigureerige MCP seaded

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Initsialiseerige projekti klient

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Looge MCP tööriist

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Täielik Python näide

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

## .NET Implementatsioon

***Märkus*** Võite käivitada selle [märkmiku](./mcp_support_dotnet.ipynb)

### 1. Paigaldage vajalikud paketid

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importige sõltuvused

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigureerige seaded

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Looge MCP tööriista definitsioon

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Looge agent MCP tööriistadega

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

## MCP tööriistade konfiguratsiooni valikud

Agentide MCP tööriistade konfigureerimisel saate määrata mitmeid olulisi parameetreid:

### Python konfiguratsioon

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

Mõlemad implementatsioonid toetavad kohandatud päiseid autentimiseks:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Tavaliste probleemide lahendamine

### 1. Ühenduse probleemid
- Kontrollige, kas MCP serveri URL on ligipääsetav
- Kontrollige autentimise mandaate
- Veenduge võrguühenduse olemasolus

### 2. Tööriista kutsete ebaõnnestumised
- Vaadake üle tööriista argumendid ja vormindus
- Kontrollige serverispetsiifilisi nõudeid
- Rakendage korrektne veakäsitlus

### 3. Jõudlusprobleemid
- Optimeerige tööriista kutsete sagedust
- Rakendage vahemällu salvestamist, kui see on asjakohane
- Jälgige serveri vastuseaegu

## Järgmised sammud

MCP integreerimise edasiseks täiustamiseks:

1. **Uurige kohandatud MCP servereid**: Looge oma MCP serverid privaatsete andmeallikate jaoks
2. **Rakendage täiustatud turvalisust**: Lisage OAuth2 või kohandatud autentimise mehhanismid
3. **Jälgimine ja analüütika**: Rakendage tööriistade kasutuse logimine ja jälgimine
4. **Lahenduse skaleerimine**: Kaaluge koormuse tasakaalustamist ja hajutatud MCP serveri arhitektuure

## Lisamaterjalid

- [Azure AI Foundry dokumentatsioon](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocoli näited](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry agentide ülevaade](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP spetsifikatsioon](https://spec.modelcontextprotocol.io/)

## Tugi

Lisatoe ja küsimuste korral:
- Vaadake [Azure AI Foundry dokumentatsiooni](https://learn.microsoft.com/azure/ai-foundry/)
- Kontrollige [MCP kogukonna ressursse](https://modelcontextprotocol.io/)

## Mis edasi

- [5.14 MCP konteksti inseneritöö](../mcp-contextengineering/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsuse, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.