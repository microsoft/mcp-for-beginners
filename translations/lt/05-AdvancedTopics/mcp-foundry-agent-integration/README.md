# Modelio konteksto protokolo (MCP) integracija su Azure AI Foundry

Šiame vadove parodoma, kaip integruoti Modelio konteksto protokolo (MCP) serverius su Azure AI Foundry agentais, suteikiant galingą įrankių koordinavimą ir įmonės AI galimybes.

## Įvadas

Modelio konteksto protokolas (MCP) yra atviras standartas, leidžiantis AI programoms saugiai prisijungti prie išorinių duomenų šaltinių ir įrankių. Integravus su Azure AI Foundry, MCP suteikia agentams galimybę pasiekti ir sąveikauti su įvairiomis išorinėmis paslaugomis, API ir duomenų šaltiniais standartizuotu būdu.

Ši integracija sujungia MCP įrankių ekosistemos lankstumą su Azure AI Foundry tvirtu agentų pagrindu, suteikdama įmonės lygio AI sprendimus su plačiomis pritaikymo galimybėmis.

**Pastaba:** Jei norite naudoti MCP su Azure AI Foundry Agent Service, šiuo metu palaikomi tik šie regionai: westus, westus2, uaenorth, southindia ir switzerlandnorth.

## Mokymosi tikslai

Baigę šį vadovą, galėsite:

- Suprasti Modelio konteksto protokolą ir jo privalumus
- Paruošti MCP serverius naudojimui su Azure AI Foundry agentais
- Kurti ir konfigūruoti agentus su MCP įrankių integracija
- Įgyvendinti praktinius pavyzdžius naudojant realius MCP serverius
- Tvarkyti įrankių atsakymus ir citatas agentų pokalbiuose

## Reikalavimai

Prieš pradėdami, įsitikinkite, kad turite:

- Azure prenumeratą su AI Foundry prieiga
- Python 3.10+ arba .NET 8.0+
- Įdiegtą ir sukonfigūruotą Azure CLI
- Tinkamus leidimus kurti AI išteklius

## Kas yra Modelio konteksto protokolas (MCP)?

Modelio konteksto protokolas yra standartizuotas būdas AI programoms prisijungti prie išorinių duomenų šaltinių ir įrankių. Pagrindiniai privalumai:

- **Standartizuota integracija**: Nuosekli sąsaja tarp skirtingų įrankių ir paslaugų
- **Saugumas**: Saugūs autentifikavimo ir autorizacijos mechanizmai
- **Lankstumas**: Palaikymas įvairiems duomenų šaltiniams, API ir pritaikytiems įrankiams
- **Išplėstinumumas**: Lengvas naujų galimybių ir integracijų pridėjimas

## MCP nustatymas su Azure AI Foundry

### Aplinkos konfigūracija

Pasirinkite pageidaujamą kūrimo aplinką:

- [Python įgyvendinimas](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET įgyvendinimas](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python įgyvendinimas

***Pastaba*** Galite paleisti šį [notebook](mcp_support_python.ipynb)

### 1. Įdiekite reikalingus paketus

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importuokite priklausomybes

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Konfigūruokite MCP nustatymus

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicijuokite projekto klientą

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Sukurkite MCP įrankį

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Užbaikite Python pavyzdį

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

## .NET įgyvendinimas

***Pastaba*** Galite paleisti šį [notebook](mcp_support_dotnet.ipynb)

### 1. Įdiekite reikalingus paketus

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importuokite priklausomybes

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Konfigūruokite nustatymus

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Sukurkite MCP įrankio apibrėžimą

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Sukurkite agentą su MCP įrankiais

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Užbaikite .NET pavyzdį

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

## MCP įrankių konfigūracijos parinktys

Konfigūruojant MCP įrankius savo agentui, galite nurodyti kelis svarbius parametrus:

### Python konfigūracija

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET konfigūracija

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentifikacija ir antraštės

Abi įgyvendinimo versijos palaiko pritaikytas antraštes autentifikacijai:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Dažniausiai pasitaikančių problemų sprendimas

### 1. Ryšio problemos
- Patikrinkite, ar MCP serverio URL yra pasiekiamas
- Patikrinkite autentifikavimo kredencialus
- Įsitikinkite tinklo ryšiu

### 2. Įrankio kvietimo klaidos
- Peržiūrėkite įrankio argumentus ir formatavimą
- Patikrinkite serverio specifinius reikalavimus
- Įgyvendinkite tinkamą klaidų tvarkymą

### 3. Našumo problemos
- Optimizuokite įrankio kvietimų dažnį
- Naudokite talpyklą, kur tai tinkama
- Stebėkite serverio atsako laikus

## Kiti žingsniai

Norėdami dar labiau patobulinti MCP integraciją:

1. **Išbandykite pritaikytus MCP serverius**: Sukurkite savo MCP serverius, skirtus nuosaviems duomenų šaltiniams
2. **Įgyvendinkite pažangų saugumą**: Pridėkite OAuth2 arba pritaikytus autentifikavimo mechanizmus
3. **Stebėjimas ir analizė**: Įgyvendinkite įrankių naudojimo registravimą ir stebėjimą
4. **Sprendimo mastelio didinimas**: Apsvarstykite apkrovos balansavimą ir paskirstytas MCP serverių architektūras

## Papildomi ištekliai

- [Azure AI Foundry dokumentacija](https://learn.microsoft.com/azure/ai-foundry/)
- [Modelio konteksto protokolo pavyzdžiai](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry agentų apžvalga](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP specifikacija](https://spec.modelcontextprotocol.io/)

## Pagalba

Papildomai pagalbai ir klausimams:
- Peržiūrėkite [Azure AI Foundry dokumentaciją](https://learn.microsoft.com/azure/ai-foundry/)
- Patikrinkite [MCP bendruomenės išteklius](https://modelcontextprotocol.io/)

## Kas toliau

- [5.14 MCP konteksto inžinerija](../mcp-contextengineering/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.