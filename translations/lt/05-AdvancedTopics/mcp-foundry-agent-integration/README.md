# Modelio konteksto protokolo (MCP) integracija su Microsoft Foundry

Šiame vadove demonstruojama, kaip integruoti Modelio konteksto protokolo (MCP) serverius su Microsoft Foundry agentais, suteikiant galingą įrankių orkestraciją ir įmonių dirbtinio intelekto galimybes.

## Įvadas

Modelio konteksto protokolas (MCP) yra atviro standarto sprendimas, leidžiantis DI programoms saugiai jungtis prie išorinių duomenų šaltinių ir įrankių. Integruotas su Microsoft Foundry, MCP leidžia agentams standartizuotu būdu prieiti prie įvairių išorinių paslaugų, API ir duomenų šaltinių bei sąveikauti su jais.

Ši integracija sujungia MCP įrankių ekosistemos lankstumą su Microsoft Foundry tvirtu agentų karkasu, teikdama įmonių lygio DI sprendimus su plačiomis pritaikymo galimybėmis.

**Pastaba:** Jei norite naudoti MCP Microsoft Foundry Agent paslaugoje, šiuo metu palaikomi tik šie regionai: westus, westus2, uaenorth, southindia ir switzerlandnorth

## Mokymosi tikslai

Baigę šį vadovą, galėsite:

- Suprasti Modelio konteksto protokolą ir jo privalumus
- Paruošti MCP serverius naudojimui su Microsoft Foundry agentais
- Kurti ir konfigūruoti agentus su MCP įrankių integracija
- Įgyvendinti praktinius pavyzdžius naudojant tikrus MCP serverius
- Tvarkyti įrankių atsakymus ir citatas agentų pokalbiuose

## Prieš pradedant

Prieš pradėdami įsitikinkite, kad turite:

- Azure prenumeratą su prieiga prie Microsoft Foundry
- Python 3.10+ arba .NET 8.0+
- Įdiegta ir sukonfigūruota Azure CLI
- Tinkamas leidimas kurti DI išteklius

## Kas yra Modelio konteksto protokolas (MCP)?

Modelio konteksto protokolas yra standartizuotas būdas DI programoms jungtis prie išorinių duomenų šaltinių ir įrankių. Pagrindiniai privalumai:

- **Standartizuota integracija**: Vienoda sąsaja skirtingiems įrankiams ir paslaugoms
- **Saugumas**: Saugus autentifikavimas ir autorizacijos mechanizmai
- **Lankstumas**: Palaikymas įvairiems duomenų šaltiniams, API ir pasirinktinėms priemonėms
- **Išplečiamumas**: Lengva pridėti naujas funkcijas ir integracijas

## MCP nustatymas su Microsoft Foundry

### Aplinkos konfigūracija

Pasirinkite savo pageidaujamą kūrimo aplinką:

- [Python įgyvendinimas](#python-įgyvendinimas)
- [.NET įgyvendinimas](#codeblock5)

---

## Python įgyvendinimas

***Pastaba*** Šį [užrašų knygelę](./mcp_support_python.ipynb) galite paleisti

### 1. Įdiekite reikalingas paketus

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

### 4. Inicializuokite projektų klientą

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
    allowed_tools=[],  # Pasirinktinai: nurodykite leidžiamus įrankius
)
```

### 6. Pilnas Python pavyzdys

```python
with project_client:
    agents_client = project_client.agents

    # Sukurkite naują agentą su MCP įrankiais
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Sukurkite siūlą komunikacijai
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Sukurkite žinutę siūlui
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Tvarkykite įrankių patvirtinimus ir paleiskite agentą
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

    # Rodyti pokalbį
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

***Pastaba*** Šį [užrašų knygelę](./mcp_support_dotnet.ipynb) galite paleisti

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

### 6. Pilnas .NET pavyzdys

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

## MCP įrankio konfigūracijos parinktys

Konfigūruodami MCP įrankius savo agentui, galite nurodyti keletą svarbių parametrų:

### Python konfigūracija

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP serverio identifikatorius
    server_url="https://api.example.com/mcp", # MCP serverio galinis taškas
    allowed_tools=[],                       # Pasirenkama: nurodykite leidžiamus įrankius
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

Abi įgyvendinimo versijos palaiko pasirinktinės autentifikacijos antraštes:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Dažnai pasitaikančių problemų sprendimas

### 1. Ryšio problemos
- Patikrinkite, ar MCP serverio URL yra pasiekiamas
- Patikrinkite autentifikacijos kredencialus
- Įsitikinkite tinklo ryšiu

### 2. Įrankio kvietimo klaidos
- Peržiūrėkite įrankio argumentus ir formatavimą
- Patikrinkite serverio specifinius reikalavimus
- Įgyvendinkite tinkamą klaidų valdymą

### 3. Veikimo našumo problemos
- Optimizuokite įrankio kvietimų dažnumą
- Naudokite kešavimą, kai tai tinkama
- Stebėkite serverio atsako laikus

## Tolimesni žingsniai

Norėdami toliau tobulinti MCP integraciją:

1. **Ištirkite pasirinktinius MCP serverius**: Kurkite savo MCP serverius nuosaviems duomenų šaltiniams
2. **Įgyvendinkite pažangų saugumą**: Pridėkite OAuth2 arba pasirinktinius autentifikacijos mechanizmus
3. **Stebėjimas ir analizė**: Įgyvendinkite žurnalavimą ir įrankių naudojimo stebėjimą
4. **Mastelio didinimas**: Apsvarstykite apkrovos balansavimą ir paskirstytas MCP serverių architektūras

## Papildomi ištekliai

- [Microsoft Foundry dokumentacija](https://learn.microsoft.com/azure/ai-foundry/)
- [Modelio konteksto protokolo pavyzdžiai](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry agentų apžvalga](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP specifikacija](https://modelcontextprotocol.io/specification/2026-07-28/)

## Pagalba

Dėl papildomos pagalbos ir klausimų:
- Peržiūrėkite [Microsoft Foundry dokumentaciją](https://learn.microsoft.com/azure/ai-foundry/)
- Patikrinkite [MCP bendruomenės išteklius](https://modelcontextprotocol.io/)

## Kas toliau

- [5.14 MCP kontekstų inžinerija](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->