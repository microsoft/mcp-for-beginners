# Model Context Protocol (MCP) Kuunganishwa na Azure AI Foundry

Mwongozo huu unaonyesha jinsi ya kuunganisha seva za Model Context Protocol (MCP) na mawakala wa Azure AI Foundry, kuwezesha usimamizi mzuri wa zana na uwezo wa AI wa biashara.

## Utangulizi

Model Context Protocol (MCP) ni kiwango wazi kinachowezesha programu za AI kuungana kwa usalama na vyanzo vya data na zana za nje. Wakati ikijiunga na Azure AI Foundry, MCP huruhusu mawakala kufikia na kuingiliana na huduma mbalimbali za nje, API, na vyanzo vya data kwa njia iliyopangwa.

Muunganiko huu unachanganya unyumbufu wa mfumo wa zana za MCP na mfumo thabiti wa mawakala wa Azure AI Foundry, ukitoa suluhisho za AI za kiwango cha biashara zenye uwezo mkubwa wa kubinafsisha.

**Note:** Ikiwa unataka kutumia MCP katika Huduma ya Mawakala ya Azure AI Foundry, kwa sasa maeneo yafuatayo pekee yanasaidiwa: westus, westus2, uaenorth, southindia na switzerlandnorth

## Malengo ya Kujifunza

Mwisho wa mwongozo huu, utaweza:

- Kuelewa Model Context Protocol na faida zake
- Kuweka seva za MCP kwa matumizi na mawakala wa Azure AI Foundry
- Kuunda na kusanidi mawakala kwa kuunganishwa kwa zana za MCP
- Kutekeleza mifano halisi kwa kutumia seva za MCP
- Kushughulikia majibu ya zana na marejeo katika mazungumzo ya mawakala

## Mahitaji ya Awali

Kabla ya kuanza, hakikisha una:

- Usajili wa Azure wenye ufikiaji wa AI Foundry
- Python 3.10+ au .NET 8.0+
- Azure CLI imewekwa na kusanidiwa
- Ruhusa zinazofaa za kuunda rasilimali za AI

## Model Context Protocol (MCP) ni Nini?

Model Context Protocol ni njia iliyopangwa kwa programu za AI kuungana na vyanzo vya data na zana za nje. Faida kuu ni:

- **Muunganisho wa Kiwango**: Kiolesura kinacholingana kwa zana na huduma tofauti
- **Usalama**: Mbinu salama za uthibitishaji na idhini
- **Unyumbufu**: Msaada kwa vyanzo mbalimbali vya data, API, na zana maalum
- **Uwezo wa Kuongezeka**: Rahisi kuongeza uwezo mpya na muunganisho

## Kuweka MCP na Azure AI Foundry

### Usanidi wa Mazingira

Chagua mazingira unayopendelea ya maendeleo:

- [Utekelezaji wa Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Utekelezaji wa .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Utekelezaji wa Python

***Note*** Unaweza kuendesha [daftari hili](mcp_support_python.ipynb)

### 1. Sakinisha Pakiti Zinazohitajika

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Ingiza Maktaba

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Sanidi Mipangilio ya MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Anzisha Mteja wa Mradi

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Unda Zana ya MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Mfano Kamili wa Python

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

## Utekelezaji wa .NET

***Note*** Unaweza kuendesha [daftari hili](mcp_support_dotnet.ipynb)

### 1. Sakinisha Pakiti Zinazohitajika

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Ingiza Maktaba

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Sanidi Mipangilio

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Unda Ufafanuzi wa Zana ya MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Unda Mwakala na Zana za MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Mfano Kamili wa .NET

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

## Chaguzi za Usanidi wa Zana za MCP

Unaposanidi zana za MCP kwa wakala wako, unaweza kubainisha vigezo kadhaa muhimu:

### Usanidi wa Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Usanidi wa .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Uthibitishaji na Vichwa vya Habari

Matoleo yote mawili yanaunga mkono vichwa vya habari maalum kwa uthibitishaji:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Kutatua Matatizo ya Kawaida

### 1. Matatizo ya Muunganisho
- Hakiki URL ya seva ya MCP inapatikana
- Angalia taarifa za uthibitishaji
- Hakikisha muunganisho wa mtandao uko sawa

### 2. Kushindwa kwa Mitoaji wa Zana
- Pitia hoja na muundo wa zana
- Angalia mahitaji maalum ya seva
- Tekeleza usimamizi sahihi wa makosa

### 3. Matatizo ya Utendaji
- Boresha mara za kuitwa kwa zana
- Tekeleza kuhifadhi data (caching) inapofaa
- Fuatilia nyakati za majibu ya seva

## Hatua Zifuatazo

Ili kuboresha zaidi muunganisho wako wa MCP:

1. **Chunguza Seva Maalum za MCP**: Jenga seva zako za MCP kwa vyanzo vya data vya kipekee
2. **Tekeleza Usalama wa Juu**: Ongeza OAuth2 au mbinu maalum za uthibitishaji
3. **Fuatilia na Tathmini**: Tekeleza uandikishaji na ufuatiliaji wa matumizi ya zana
4. **Panua Suluhisho Lako**: Fikiria usawazishaji mzigo na usanifu wa seva za MCP zilizosambazwa

## Rasilimali Zaidi

- [Nyaraka za Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Mifano ya Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Muhtasari wa Mawakala wa Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Maelezo ya MCP](https://spec.modelcontextprotocol.io/)

## Msaada

Kwa msaada zaidi na maswali:
- Pitia [nyaraka za Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Angalia [rasilimali za jamii ya MCP](https://modelcontextprotocol.io/)

## Nini Kifuatacho

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.