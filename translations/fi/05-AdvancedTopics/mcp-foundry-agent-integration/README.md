# Model Context Protocol (MCP) -integrointi Azure AI Foundryn kanssa

Tässä oppaassa näytetään, miten Model Context Protocol (MCP) -palvelimet integroidaan Azure AI Foundryn agenteihin, mikä mahdollistaa tehokkaan työkalujen orkestroinnin ja yritystason tekoälyominaisuudet.

## Johdanto

Model Context Protocol (MCP) on avoin standardi, joka mahdollistaa tekoälysovellusten turvallisen yhteyden ulkoisiin tietolähteisiin ja työkaluihin. Kun MCP integroidaan Azure AI Foundryn kanssa, agentit voivat käyttää ja olla vuorovaikutuksessa eri ulkoisten palveluiden, API:en ja tietolähteiden kanssa yhtenäisellä tavalla.

Tämä integraatio yhdistää MCP:n työkaluekosysteemin joustavuuden Azure AI Foundryn vankan agenttikehyksen kanssa, tarjoten yritystason tekoälyratkaisuja laajoilla räätälöintimahdollisuuksilla.

**Note:** Jos haluat käyttää MCP:tä Azure AI Foundry Agent Service -palvelussa, tällä hetkellä tuetut alueet ovat: westus, westus2, uaenorth, southindia ja switzerlandnorth

## Oppimistavoitteet

Oppaan lopussa osaat:

- Ymmärtää Model Context Protocolin ja sen hyödyt
- Määrittää MCP-palvelimet käytettäväksi Azure AI Foundryn agenttien kanssa
- Luoda ja konfiguroida agentteja MCP-työkalujen integroinnilla
- Toteuttaa käytännön esimerkkejä oikeilla MCP-palvelimilla
- Käsitellä työkalujen vastauksia ja lähdeviitteitä agenttikeskusteluissa

## Ennen aloittamista

Varmista ennen aloittamista, että sinulla on:

- Azure-tilaus, jossa on pääsy AI Foundryyn
- Python 3.10+ tai .NET 8.0+
- Azure CLI asennettuna ja konfiguroituna
- Tarvittavat oikeudet AI-resurssien luomiseen

## Mikä on Model Context Protocol (MCP)?

Model Context Protocol on standardoitu tapa, jolla tekoälysovellukset voivat yhdistää ulkoisiin tietolähteisiin ja työkaluihin. Keskeiset hyödyt ovat:

- **Standardoitu integraatio**: Johdonmukainen rajapinta eri työkaluille ja palveluille
- **Turvallisuus**: Turvalliset todennus- ja valtuutusmekanismit
- **Joustavuus**: Tuki erilaisille tietolähteille, API:lle ja räätälöidyille työkaluilla
- **Laajennettavuus**: Helppo lisätä uusia ominaisuuksia ja integraatioita

## MCP:n käyttöönotto Azure AI Foundryn kanssa

### Ympäristön konfigurointi

Valitse haluamasi kehitysympäristö:

- [Python-toteutus](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET-toteutus](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python-toteutus

***Note*** Voit suorittaa tämän [notebookin](mcp_support_python.ipynb)

### 1. Asenna tarvittavat paketit

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Tuo riippuvuudet

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Määritä MCP-asetukset

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Alusta projektin asiakas

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Luo MCP-työkalu

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Täydellinen Python-esimerkki

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

## .NET-toteutus

***Note*** Voit suorittaa tämän [notebookin](mcp_support_dotnet.ipynb)

### 1. Asenna tarvittavat paketit

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Tuo riippuvuudet

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Määritä asetukset

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Luo MCP-työkalun määritelmä

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Luo agentti MCP-työkaluilla

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Täydellinen .NET-esimerkki

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

## MCP-työkalun konfigurointivaihtoehdot

Kun määrität MCP-työkaluja agentillesi, voit asettaa useita tärkeitä parametreja:

### Python-konfiguraatio

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET-konfiguraatio

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Todennus ja otsikot

Molemmat toteutukset tukevat mukautettuja otsikoita todennusta varten:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Yleiset ongelmat ja niiden ratkaisut

### 1. Yhteysongelmat
- Varmista, että MCP-palvelimen URL on saavutettavissa
- Tarkista todennustiedot
- Varmista verkkoyhteys

### 2. Työkalukutsujen epäonnistumiset
- Tarkista työkalun argumentit ja muotoilu
- Selvitä palvelinkohtaiset vaatimukset
- Toteuta asianmukainen virheenkäsittely

### 3. Suorituskykyongelmat
- Optimoi työkalukutsujen tiheys
- Käytä välimuistia tarvittaessa
- Seuraa palvelimen vasteaikoja

## Seuraavat askeleet

MCP-integraation kehittämiseksi edelleen:

1. **Tutustu räätälöityihin MCP-palvelimiin**: Rakenna omia MCP-palvelimia omille tietolähteillesi
2. **Ota käyttöön kehittynyt turvallisuus**: Lisää OAuth2- tai mukautetut todennusmekanismit
3. **Seuranta ja analytiikka**: Toteuta lokitus ja seuranta työkalujen käytölle
4. **Skaalaa ratkaisusi**: Harkitse kuormantasauksen ja hajautettujen MCP-palvelinarkkitehtuurien käyttöä

## Lisäresurssit

- [Azure AI Foundryn dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol -esimerkit](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundryn agenttien yleiskatsaus](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP-spesifikaatio](https://spec.modelcontextprotocol.io/)

## Tuki

Lisätukea ja kysymyksiä varten:
- Tutustu [Azure AI Foundryn dokumentaatioon](https://learn.microsoft.com/azure/ai-foundry/)
- Katso [MCP-yhteisön resurssit](https://modelcontextprotocol.io/)

## Mitä seuraavaksi

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.