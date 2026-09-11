# மாடல் கருத்து நெறிமுறை (MCP) மைக்ரோசாஃப்ட் ஃபௌன்ட்ரி உடன் ஒருங்கிணைப்பு

இந்த கையேடு மாடல் கருத்து நெறிமுறை (MCP) சேவைகளைக் கொண்டு மைக்ரோசாஃப்ட் ஃபௌன்ட்ரி முகவர்கள் ஆகியவற்றுடன் ஒருங்கிணைக்கும் முறையை விளக்குகிறது, சக்திவாய்ந்த கருவி ஒருங்கிணைப்பு மற்றும் நிறுவன ஏไஐ திறன்களை இயல்பாக்குகிறது.

## அறிமுகம்

மாடல் கருத்து நெறிமுறை (MCP) என்பது ஏไஐ பயன்பாடுகள் வெளிப்புற தரவுத் தளங்கள் மற்றும் கருவிகளுடன் பாதுகாப்பாக இணைக்க திறனளிக்கும் திறந்த நிலையான தரநிலையாகும். மைக்ரோசாஃப்ட் ஃபௌன்ட்ரி உடன் ஒருங்கிணைக்கப்படும்போது, MCP முகவர்கள் பல்வேறு வெளிப்புற சேவைகள், APIகள் மற்றும் தரவுத் தளங்களுடன் ஒருங்கிணைந்து தொடர்புகொள்ளும் வழியை வழங்கும்.

இந்த ஒருங்கிணைப்பு MCPயின் கருவி சூழல்பிரபஞ்சத்தின் சோர்வின்றி தழுவலுடன் மைக்ரோசாஃப்ட் ஃபௌன்ட்ரி இன் வலுவான முகவர் கட்டமைப்பை கலந்து, விரிவான தனிப்பயன்பாட்டு திறன்களுடன் நிறுவன தரம் வாய்ந்த ஏไஐ தீர்வுகளை வழங்குகிறது.

**குறிப்பு:** நீங்கள் Microsoft Foundry முகவர் சேவையில் MCP ஐப் பயன்படுத்த விரும்பினால், தற்போது பின்வரும் பிரதேசங்களே ஆதரிக்கப்படுகின்றன: westus, westus2, uaenorth, southindia மற்றும் switzerlandnorth

## கற்றல் குறிக்கோள்கள்

இந்த கையேட்டின் இறுதியில், நீங்கள் செய்யக்கூடியவை:

- மாடல் கருத்து நெறிமுறை மற்றும் அதன் நன்மைகளை புரிந்து கொள்வது
- மைக்ரோசாஃப்ட் ஃபௌன்ட்ரி முகவர்கள் உடன் பயன்படுத்த MCP ஸர்வர்களை அமைத்தல்
- MCP கருவி ஒருங்கிணைப்புடன் முகவர்களை உருவாக்கி அமைத்தல்
- உண்மையான MCP சேவைகளைப் பயன்படுத்தி நடைமுறை உதாரணங்களை செயல்படுத்தல்
- முகவர் அரட்டைகளில் கருவி பதில்களையும் மேற்கோள்களையும் கையாள்தல்

## முன் தேவைகள்

தொடங்குவதற்கு முன்பு, நீங்கள் பின்வற்றவற்றைக் கொண்டிருக்க வேண்டும்:

- மைக்ரோசாஃப்ட் ஃபௌன்ட்ரி அணுகல் கொண்ட Azure சந்தா
- Python 3.10+ அல்லது .NET 8.0+
- Azure CLI நிறுவப்பட்டு கட்டமைக்கப்பட்டிருக்க வேண்டும்
- ஏไஐ வளங்களை உருவாக்க தேவையான உரிமைகள்

## மாடல் கருத்து நெறிமுறை (MCP) என்பது என்ன?

மாடல் கருத்து நெறிமுறை என்பது ஏไஐ பயன்பாடுகள் வெளிப்புற தரவுத் தளங்கள் மற்றும் கருவிகளுடன் இணைக்க ஒரு தரநிலை முறையாகும். முக்கிய நன்மைகள்:

- **தரநிலை ஒருங்கிணைப்பு**: பல்வேறு கருவிகள் மற்றும் சேவைகளுக்கு ஒரே மாதிரியாக இடைமுகம் வழங்குதல்
- **பாதுகாப்பு**: பாதுகாப்பான அங்கீகாரம் மற்றும் அதிகாரச் சரிபார்ப்பு முறைகள்
- **இயல்திறன்**: பல்வேறு தரவுத் தளங்கள், APIகள் மற்றும் தனிப்பயன் கருவிகளை ஆதரித்தல்
- **விரிவாக்கக்கூறுதல்**: புதிய திறன்கள் மற்றும் ஒருங்கிணைப்புகளை எளிதில் சேர்க்க வாய்ப்பு

## மைக்ரோசாஃப்ட் ஃபௌன்ட்ரியுடன் MCP அமைத்தல்

### சூழல் அமைப்பு

உங்கள் விருப்பமான அபிவிருத்தி சூழலை தேர்ந்தெடுக்கவும்:

- [Python செயலாக்கம்](#python-செயலாக்கம்)
- [.NET செயலாக்கம்](#codeblock5)

---

## Python செயலாக்கம்

***குறிப்பு*** நீங்கள் இந்த [நோட்புக்](./mcp_support_python.ipynb) ஓட்டலாம்

### 1. தேவையான தொகுதிகளை நிறுவுதல்

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. சார்ந்தவற்றை இறக்குமதி செய்தல்

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. MCP அமைப்புகளை கட்டமைத்தல்

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. திட்ட வாடிக்கையாளரை துவக்கம் செய்தல்

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. MCP கருவியை உருவாக்குதல்

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # விருப்பமாக: அனுமதிக்கப்பட்ட கருவிகளை குறிப்பிடுக
)
```

### 6. முழுமையான Python உதாரணம்

```python
with project_client:
    agents_client = project_client.agents

    # MCP கருவிகளுடன் புதிய முகவரியை உருவாக்கவும்
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # தொடர்பிற்கு திரெட்எ ஒன்றை உருவாக்கவும்
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # திரெடுக்கு செய்தியை உருவாக்கவும்
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # கருவி அங்கீகாரங்களை கையாளவும் மற்றும் முகவரியை இயக்கவும்
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

    # உரையாடலை காட்டு
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

## .NET செயலாக்கம்

***குறிப்பு*** நீங்கள் இந்த [நோட்புக்](./mcp_support_dotnet.ipynb) ஓட்டலாம்

### 1. தேவையான தொகுதிகளை நிறுவுதல்

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. சார்ந்தவற்றை இறக்குமதி செய்தல்

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. அமைப்புகளை கட்டமைத்தல்

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. MCP கருவி வரையறையை உருவாக்குதல்

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. MCP கருவிகளுடன் முகவரைப் படைத்தல்

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. முழுமையான .NET உதாரணம்

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

## MCP கருவி கட்டமைப்பு விருப்பங்கள்

உங்கள் முகவருக்கான MCP கருவிகளைக் கட்டமைக்கும் போது, சில முக்கியமான அளவுருக்களை குறிப்பிடலாம்:

### Python கட்டமைப்பு

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP சர்வருக்கான அடையாளம்
    server_url="https://api.example.com/mcp", # MCP சர்வர் முடிச்சிடுப்பு
    allowed_tools=[],                       # விருப்பம்: அனுமதிக்கப்பட்ட கருவிகளை குறிப்பிடவும்
)
```

### .NET கட்டமைப்பு

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## அங்கீகாரம் மற்றும் தலைப்புகள்

இரு செயலாக்கங்களும் அனுமதி வழங்க தனிப்பயன் தலைப்புகளை ஆதரிக்கின்றன:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## பொதுவான பிரச்சினைகளை தீர்க்குதல்

### 1. இணைப்பு பிரச்சினைகள்
- MCP சேவையகம் URL கிடைக்கக்கூடியதா என்று உறுதி செய்துகொள்ளவும்
- அங்கீகாரச் சான்றுகளை சரிபார்க்கவும்
- நெட்வொர்க் இணைப்பை உறுதி செய்யவும்

### 2. கருவி அழைப்பு தோல்விகள்
- கருவி வாதிர்களையும் வடிவமைப்பையும் மதிப்பாய்வு செய்யவும்
- சேவையக விருப்பங்களை சரிபார்க்கவும்
- சரியான பிழை கையாள்தலை செயல்படுத்தவும்

### 3. செயல்திறன் பிரச்சினைகள்
- கருவி அழைப்பின் அடிக்கடி பாவனையை மேம்படுத்தவும்
- தேவையான இடங்களில் கேஷை பயன்படுத்தவும்
- சேவையக பதில் நேரங்களை கண்காணிக்கவும்

## அடுத்த படிகள்

உங்கள் MCP ஒருங்கிணைப்பை மேலும் மேம்படுத்த:

1. **தனிப்பயன் MCP சேவைகளை ஆராயவும்**: சொந்த MCP சேவைகளை உருவாக்கி சொந்த தரவுத்தளங்களுக்கு இணைக்கவும்
2. **முன்னேற்றப்பட்ட பாதுகாப்பை செயல்படுத்தவும்**: OAuth2 அல்லது தனிப்பயன் அங்கீகார முறைகளை சேர்க்கவும்
3. **மாற்றங்கள் மற்றும் பகுப்பாய்வு**: கருவியின் பயன்பாட்டிற்கான பதிவு மற்றும் கண்காணிப்பு செயல்படுத்தவும்
4. **உங்கள் தீர்வை விரிவாக்கவும்**: பூசணி சமநிலைப்படுத்தல் மற்றும் விநியோகிக்கப்பட்ட MCP சேவையக கட்டமைப்புகளை பரிசீலிக்கவும்

## கூடுதல் வளங்கள்

- [Microsoft Foundry ஆவணங்கள்](https://learn.microsoft.com/azure/ai-foundry/)
- [மாடல் கருத்து நெறிமுறை எடுத்துக்கூறுகள்](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry முகவர்கள் சுருக்கம்](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP இலக்கணம்](https://modelcontextprotocol.io/specification/2026-07-28/)

## ஆதரவு

கூடுதல் ஆதரவு மற்றும் கேள்விகளுக்காக:
- [Microsoft Foundry ஆவணங்களை](https://learn.microsoft.com/azure/ai-foundry/) பரிசீலிக்கவும்
- [MCP சமூக வளங்களை](https://modelcontextprotocol.io/) சரிபார்க்கவும்

## அடுத்தது என்ன

- [5.14 MCP கருத்து பொறியியல்](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->