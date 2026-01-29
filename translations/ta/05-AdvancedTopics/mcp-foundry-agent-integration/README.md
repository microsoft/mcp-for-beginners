# மாடல் சூழல் நெறிமுறை (MCP) மற்றும் Azure AI Foundry ஒருங்கிணைப்பு

இந்த வழிகாட்டி, மாடல் சூழல் நெறிமுறை (MCP) சேவையகங்களை Azure AI Foundry முகவர்களுடன் ஒருங்கிணைப்பது எப்படி என்பதை விளக்குகிறது, சக்திவாய்ந்த கருவி ஒருங்கிணைப்பு மற்றும் நிறுவன AI திறன்களை இயக்குகிறது.

## அறிமுகம்

மாடல் சூழல் நெறிமுறை (MCP) என்பது AI பயன்பாடுகள் வெளிப்புற தரவூட்டங்கள் மற்றும் கருவிகளுடன் பாதுகாப்பாக இணைவதற்கான திறந்த தரநிலை ஆகும். Azure AI Foundry உடன் MCP ஒருங்கிணைக்கும்போது, MCP முகவர்களுக்கு பல்வேறு வெளிப்புற சேவைகள், APIகள் மற்றும் தரவூட்டங்களுடன் ஒரு தரநிலை முறை மூலம் அணுகவும் தொடர்பு கொள்ளவும் அனுமதிக்கிறது.

இந்த ஒருங்கிணைப்பு MCP கருவி சூழலின் நெகிழ்வுத்தன்மையை Azure AI Foundryயின் வலுவான முகவர் கட்டமைப்புடன் இணைத்து, விரிவான தனிப்பயனாக்க திறன்களுடன் நிறுவன தரமான AI தீர்வுகளை வழங்குகிறது.

**குறிப்பு:** Azure AI Foundry Agent Service-ல் MCP பயன்படுத்த விரும்பினால், தற்போது கீழே உள்ள பகுதிகள் மட்டுமே ஆதரிக்கப்படுகின்றன: westus, westus2, uaenorth, southindia மற்றும் switzerlandnorth

## கற்றல் நோக்கங்கள்

இந்த வழிகாட்டியை முடிக்கும்போது, நீங்கள்:

- மாடல் சூழல் நெறிமுறையை மற்றும் அதன் நன்மைகளை புரிந்து கொள்ள
- Azure AI Foundry முகவர்களுடன் MCP சேவையகங்களை அமைக்க
- MCP கருவி ஒருங்கிணைப்புடன் முகவர்களை உருவாக்கவும் அமைக்கவும்
- உண்மையான MCP சேவையகங்களைப் பயன்படுத்தி நடைமுறை உதாரணங்களை செயல்படுத்த
- முகவர் உரையாடல்களில் கருவி பதில்கள் மற்றும் மேற்கோள்களை கையாள

## முன் தேவைகள்

தொடங்குவதற்கு முன், உங்களிடம் இருக்க வேண்டும்:

- Azure சந்தாதாரத்துடன் AI Foundry அணுகல்
- Python 3.10+ அல்லது .NET 8.0+
- Azure CLI நிறுவப்பட்டு அமைக்கப்பட்டிருக்க வேண்டும்
- AI வளங்களை உருவாக்க தேவையான அனுமதிகள்

## மாடல் சூழல் நெறிமுறை (MCP) என்றால் என்ன?

மாடல் சூழல் நெறிமுறை என்பது AI பயன்பாடுகள் வெளிப்புற தரவூட்டங்கள் மற்றும் கருவிகளுடன் இணைவதற்கான தரநிலை முறை ஆகும். முக்கிய நன்மைகள்:

- **தரநிலை ஒருங்கிணைப்பு**: பல்வேறு கருவிகள் மற்றும் சேவைகளுக்கு ஒரே மாதிரியான இடைமுகம்
- **பாதுகாப்பு**: பாதுகாப்பான அங்கீகாரம் மற்றும் அனுமதி முறைமைகள்
- **நெகிழ்வுத்தன்மை**: பல்வேறு தரவூட்டங்கள், APIகள் மற்றும் தனிப்பயன் கருவிகளுக்கு ஆதரவு
- **விரிவாக்கத்தன்மை**: புதிய திறன்கள் மற்றும் ஒருங்கிணைப்புகளை எளிதாகச் சேர்க்க

## Azure AI Foundry உடன் MCP அமைத்தல்

### சூழல் அமைப்பு

உங்கள் விருப்பமான மேம்பாட்டு சூழலைத் தேர்ந்தெடுக்கவும்:

- [Python செயல்பாடு](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET செயல்பாடு](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python செயல்பாடு

***குறிப்பு*** நீங்கள் இந்த [குறிப்பேடு](./mcp_support_python.ipynb) இயக்கலாம்

### 1. தேவையான தொகுதிகளை நிறுவவும்

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. சார்புகளை இறக்குமதி செய்யவும்

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP அமைப்புகளை உள்ளமைக்கவும்

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. திட்டக் கிளையண்டை தொடங்கவும்

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP கருவியை உருவாக்கவும்

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Python உதாரணத்தை முடிக்கவும்

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

## .NET செயல்பாடு

***குறிப்பு*** நீங்கள் இந்த [குறிப்பேடு](./mcp_support_dotnet.ipynb) இயக்கலாம்

### 1. தேவையான தொகுதிகளை நிறுவவும்

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. சார்புகளை இறக்குமதி செய்யவும்

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. அமைப்புகளை உள்ளமைக்கவும்

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP கருவி வரையறையை உருவாக்கவும்

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP கருவிகளுடன் முகவர்களை உருவாக்கவும்

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. .NET உதாரணத்தை முடிக்கவும்

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

## MCP கருவி அமைப்பு விருப்பங்கள்

உங்கள் முகவருக்கான MCP கருவிகளை அமைக்கும் போது, பல முக்கிய அளவுருக்களை குறிப்பிடலாம்:

### Python அமைப்பு

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET அமைப்பு

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## அங்கீகாரம் மற்றும் தலைப்புகள்

இரு செயல்பாடுகளும் அங்கீகாரத்திற்கான தனிப்பயன் தலைப்புகளை ஆதரிக்கின்றன:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## பொதுவான சிக்கல்களை தீர்க்க

### 1. இணைப்பு சிக்கல்கள்
- MCP சேவையக URL அணுகக்கூடியதா என்பதை சரிபார்க்கவும்
- அங்கீகார சான்றுகளை சரிபார்க்கவும்
- நெட்வொர்க் இணைப்பை உறுதிப்படுத்தவும்

### 2. கருவி அழைப்பு தோல்விகள்
- கருவி வாதங்கள் மற்றும் வடிவமைப்புகளை மதிப்பீடு செய்யவும்
- சேவையக-குறிப்பிட்ட தேவைகளை சரிபார்க்கவும்
- சரியான பிழை கையாளுதலை செயல்படுத்தவும்

### 3. செயல்திறன் சிக்கல்கள்
- கருவி அழைப்பு அதிர்வெண் மேம்படுத்தவும்
- தேவையான இடங்களில் கேஷிங் செயல்படுத்தவும்
- சேவையக பதில் நேரங்களை கண்காணிக்கவும்

## அடுத்த படிகள்

உங்கள் MCP ஒருங்கிணைப்பை மேலும் மேம்படுத்த:

1. **தனிப்பயன் MCP சேவையகங்களை ஆராயவும்**: சொந்தமான தரவூட்டங்களுக்கு MCP சேவையகங்களை உருவாக்கவும்
2. **மேம்பட்ட பாதுகாப்பை செயல்படுத்தவும்**: OAuth2 அல்லது தனிப்பயன் அங்கீகார முறைமைகளைச் சேர்க்கவும்
3. **கண்காணிப்பு மற்றும் பகுப்பாய்வு**: கருவி பயன்பாட்டிற்கான பதிவு மற்றும் கண்காணிப்பை செயல்படுத்தவும்
4. **தீர்வை அளவீடு செய்யவும்**: சுமை சமநிலை மற்றும் பகிர்ந்த MCP சேவையக கட்டமைப்புகளை பரிசீலிக்கவும்

## கூடுதல் வளங்கள்

- [Azure AI Foundry ஆவணங்கள்](https://learn.microsoft.com/azure/ai-foundry/)
- [மாடல் சூழல் நெறிமுறை மாதிரிகள்](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry முகவர்கள் மேற்பார்வை](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP விவரக்குறிப்பு](https://spec.modelcontextprotocol.io/)

## ஆதரவு

கூடுதல் ஆதரவு மற்றும் கேள்விகளுக்கு:
- [Azure AI Foundry ஆவணங்களை](https://learn.microsoft.com/azure/ai-foundry/) மதிப்பீடு செய்யவும்
- [MCP சமூக வளங்களை](https://modelcontextprotocol.io/) சரிபார்க்கவும்

## அடுத்தது என்ன 

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.