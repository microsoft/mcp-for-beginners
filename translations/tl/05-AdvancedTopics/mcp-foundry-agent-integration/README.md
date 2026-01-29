# Model Context Protocol (MCP) Integration sa Azure AI Foundry

Ipinapakita ng gabay na ito kung paano i-integrate ang Model Context Protocol (MCP) servers sa Azure AI Foundry agents, na nagbibigay-daan sa makapangyarihang tool orchestration at enterprise AI capabilities.

## Panimula

Ang Model Context Protocol (MCP) ay isang bukas na pamantayan na nagpapahintulot sa mga AI application na ligtas na kumonekta sa mga panlabas na pinagkukunan ng datos at mga tool. Kapag na-integrate sa Azure AI Foundry, pinapayagan ng MCP ang mga agent na ma-access at makipag-ugnayan sa iba't ibang panlabas na serbisyo, API, at pinagkukunan ng datos sa isang standardized na paraan.

Pinagsasama ng integrasyong ito ang kakayahang umangkop ng MCP tool ecosystem at ang matibay na agent framework ng Azure AI Foundry, na nagbibigay ng enterprise-grade AI solutions na may malawak na kakayahan sa pag-customize.

**Note:** Kung nais mong gamitin ang MCP sa Azure AI Foundry Agent Service, sa kasalukuyan ay sinusuportahan lamang ang mga sumusunod na rehiyon: westus, westus2, uaenorth, southindia at switzerlandnorth

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng gabay na ito, magagawa mong:

- Maunawaan ang Model Context Protocol at ang mga benepisyo nito
- Mag-set up ng MCP servers para gamitin kasama ang Azure AI Foundry agents
- Gumawa at mag-configure ng mga agent na may MCP tool integration
- Magpatupad ng mga praktikal na halimbawa gamit ang totoong MCP servers
- Pangasiwaan ang mga tugon ng tool at mga citation sa mga pag-uusap ng agent

## Mga Kinakailangan

Bago magsimula, siguraduhing mayroon kang:

- Isang Azure subscription na may access sa AI Foundry
- Python 3.10+ o .NET 8.0+
- Azure CLI na naka-install at naka-configure
- Angkop na mga pahintulot para gumawa ng AI resources

## Ano ang Model Context Protocol (MCP)?

Ang Model Context Protocol ay isang standardized na paraan para sa mga AI application na kumonekta sa mga panlabas na pinagkukunan ng datos at mga tool. Kabilang sa mga pangunahing benepisyo nito ang:

- **Standardized Integration**: Pare-parehong interface sa iba't ibang tool at serbisyo
- **Seguridad**: Ligtas na authentication at authorization na mga mekanismo
- **Kakayahang Umangkop**: Suporta para sa iba't ibang pinagkukunan ng datos, API, at custom na mga tool
- **Extensibility**: Madaling magdagdag ng mga bagong kakayahan at integrasyon

## Pag-setup ng MCP sa Azure AI Foundry

### Pag-configure ng Kapaligiran

Pumili ng iyong nais na development environment:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** Maaari mong patakbuhin ang [notebook](mcp_support_python.ipynb)

### 1. I-install ang Mga Kinakailangang Package

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. I-import ang Mga Dependencies

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. I-configure ang Mga Setting ng MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. I-initialize ang Project Client

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Gumawa ng MCP Tool

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Kumpletong Halimbawa sa Python

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

***Note*** Maaari mong patakbuhin ang [notebook](mcp_support_dotnet.ipynb)

### 1. I-install ang Mga Kinakailangang Package

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. I-import ang Mga Dependencies

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. I-configure ang Mga Setting

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Gumawa ng MCP Tool Definition

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Gumawa ng Agent na may MCP Tools

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Kumpletong Halimbawa sa .NET

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

## Mga Opsyon sa Pag-configure ng MCP Tool

Kapag nag-configure ng MCP tools para sa iyong agent, maaari mong tukuyin ang ilang mahahalagang parameter:

### Python Configuration

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET Configuration

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Authentication at Headers

Sinusuportahan ng parehong implementasyon ang custom headers para sa authentication:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Pag-aayos ng Karaniwang Mga Isyu

### 1. Mga Isyu sa Koneksyon
- Siguraduhing naa-access ang MCP server URL
- Suriin ang mga authentication credentials
- Tiyakin ang koneksyon sa network

### 2. Mga Pagkabigo sa Pagtawag ng Tool
- Suriin ang mga argumento at format ng tool
- Tingnan ang mga partikular na pangangailangan ng server
- Magpatupad ng tamang error handling

### 3. Mga Isyu sa Performance
- I-optimize ang dalas ng pagtawag sa tool
- Magpatupad ng caching kung kinakailangan
- Subaybayan ang oras ng tugon ng server

## Mga Susunod na Hakbang

Para lalo pang pagandahin ang iyong MCP integration:

1. **Suriin ang Custom MCP Servers**: Gumawa ng sarili mong MCP servers para sa proprietary na pinagkukunan ng datos
2. **Magpatupad ng Advanced Security**: Magdagdag ng OAuth2 o custom na mga mekanismo ng authentication
3. **Mag-monitor at Mag-analisa**: Magpatupad ng logging at monitoring para sa paggamit ng tool
4. **I-scale ang Iyong Solusyon**: Isaalang-alang ang load balancing at distributed MCP server architectures

## Karagdagang Mga Mapagkukunan

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol Samples](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## Suporta

Para sa karagdagang suporta at mga tanong:
- Suriin ang [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- Tingnan ang [MCP community resources](https://modelcontextprotocol.io/)

## Ano ang susunod

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.