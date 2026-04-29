# ការរួមបញ្ចូល Model Context Protocol (MCP) ជាមួយ Azure AI Foundry

មេរៀននេះបង្ហាញពីរបៀបរួមបញ្ចូលម៉ាស៊ីនបម្រើ Model Context Protocol (MCP) ជាមួយភ្នាក់ងារ Azure AI Foundry ដែលអាចអនុញ្ញាតឲ្យមានការរៀបចំបច្ចេកវិទ្យាឧបករណ៍ដែលមានប្រសិទ្ធភាព និងសមត្ថភាព AI សម្រាប់សហគ្រាស។

## ការបរិច្ឆេទ

Model Context Protocol (MCP) គឺជាមាត្រដ្ឋានបើកដែលអនុញ្ញាតឲ្យកម្មវិធី AI បានភ្ជាប់យ៉ាងសុវត្ថិភាពទៅកាន់ប្រភពទិន្នន័យ និងឧបករណ៍ខាងក្រៅ។ ពេលរួមបញ្ចូលជាមួយ Azure AI Foundry, MCP អនុញ្ញាតឲ្យភ្នាក់ងារជួសជុល និងធ្វើប្រតិបត្តិការជាមួយសេវាកម្មខាងក្រៅផ្សេងៗ API និងប្រភពទិន្នន័យតាមរបៀបស្តង់ដា។

ការរួមបញ្ចូលនេះបញ្ចូលសំប៉ាញឧបករណ៍ MCP យ៉ាងត្រៀមខ្លួនរួមជាមួយស៊ុមភ្នាក់ងាររឹងមាំរបស់ Azure AI Foundry, ផ្ដល់ដំណោះស្រាយ AI សម្រាប់សហគ្រាសជាមួយសមត្ថភាពបត់បែនយ៉ាងទូលំទូលាយ។

**សំគាល់៖** ប្រសិនបើអ្នកចង់ប្រើ MCP នៅក្នុងសេវា Azure AI Foundry Agent សូមដឹងថា តំបន់ខាងក្រោមទាន់តែគាំទ្រ៖ westus, westus2, uaenorth, southindia និង switzerlandnorth

## គោលបំណងសិក្សា

នៅចុងមេរៀននេះ អ្នកនឹងអាច៖

- ហ្វ្វាញយល់ពី Model Context Protocol និងអត្ថប្រយោជន៍របស់វា
- បង្កើតម៉ាស៊ីនបម្រើ MCP សម្រាប់ប្រើជាមួយភ្នាក់ងារ Azure AI Foundry
- បង្កើតនិងកំណត់រចនាសម្ព័ន្ធភ្នាក់ងារជាមួយការរួមបញ្ចូលឧបករណ៍ MCP
- អនុវត្តឧទាហរណ៍ជាក់ស្តែងដោយប្រើម៉ាស៊ីនបម្រើ MCP ពិតប្រាកដ
- គ្រប់គ្រងចម្លើយឧបករណ៍ និងឯកសារយោងក្នុងការសន្ទនារបស់ភ្នាក់ងារ

## តម្រូវការមុនការចាប់ផ្តើម

មុនចាប់ផ្តើម សូមប្រាកដថាអ្នកមាន៖

- សេវាកម្ម Azure ដែលមានចូលដំណើរការ AI Foundry
- Python 3.10+ ឬ .NET 8.0+
- កម្មវិធី Azure CLI ដែលបានដំឡើងនិងកំណត់រចនាសម្ព័ន្ធ
- សិទ្ធិត្រឹមត្រូវសម្រាប់បង្កើតធនធាន AI

## តើ Model Context Protocol (MCP) ជាអ្វី?

Model Context Protocol គឺជារបៀបស្តង់ដារមួយសម្រាប់កម្មវិធី AI ភ្ជាប់ទៅកាន់ប្រភពទិន្នន័យ និងឧបករណ៍ខាងក្រៅ។ អត្ថប្រយោជន៍សំខាន់រួមមាន៖

- **ការរួមបញ្ចូលស្តង់ដារ**៖ ចំណុចប្រទាក់ដូចគ្នាសម្រាប់ឧបករណ៍និងសេវាកម្មផ្សេងៗ
- **សុវត្ថិភាព**៖ មេកានិចសម្រាប់ការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ និងការអនុញ្ញាតយ៉ាងសុវត្ថិភាព
- **បត់បែន**៖ គាំទ្រប្រភពទិន្នន័យជាច្រើន API និងឧបករណ៍ប្ដូរតាមតម្រូវការ
- **ពង្រីកបានងាយ**៖ ងាយស្រួលបន្ថែមសមត្ថភាពនិងការរួមបញ្ចូលថ្មីៗ

## ការកំណត់ MCP ជាមួយ Azure AI Foundry

### ការកំណត់បរិយាកាស

ជ្រើសរើសបរិយាកាសអភិវឌ្ឍដែលអ្នកចូលចិត្ត៖

- [ការអនុវត្ត Python](#ការអនុវត្ត-python)
- [ការអនុវត្ត .NET](#codeblock5)

---

## ការអនុវត្ត Python

***សូមចំណាំ*** អ្នកអាចរត់ [សៀវភៅកំណត់ចំណាំ](./mcp_support_python.ipynb) នេះបាន។

### 1. ដំឡើងកញ្ចប់ដែលត្រូវការ

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. នាំចូលមេរោគ

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. កំណត់រចនាសម្ព័ន្ធ MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. ដំណើរការរូបការងារប្រតិបត្តិ

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. បង្កើតឧបករណ៍ MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # ជាជម្រើស៖ បញ្ជាក់ឧបករណ៍ដែលអនុញ្ញាត
)
```

### 6. ឧទាហរណ៍ Python ពេញលេញ

```python
with project_client:
    agents_client = project_client.agents

    # បង្កើតភ្នាក់ងារថ្មីជាមួយឧបករណ៍ MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # បង្កើតខ្សែThreads សម្រាប់ការប្រាស្រ័យទាក់ទង
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # បង្កើតសារទៅកាន់ខ្សែThreads
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # គ្រប់គ្រងការអនុម័តឧបករណ៍ និងដំណើរការភ្នាក់ងារ
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

    # បង្ហាញការសន្ទនា
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

## ការអនុវត្ត .NET

***សូមចំណាំ*** អ្នកអាចរត់ [សៀវភៅកំណត់ចំណាំ](./mcp_support_dotnet.ipynb) នេះបាន។

### 1. ដំឡើងកញ្ចប់ដែលត្រូវការ

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. នាំចូលមេរោគ

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. កំណត់រចនាសម្ព័ន្ធ

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. បង្កើតនិយមន័យឧបករណ៍ MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. បង្កើតភ្នាក់ងារជាមួយឧបករណ៍ MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. ឧទាហរណ៍ .NET ពេញលេញ

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

## ជម្រើសកំណត់រចនាសម្ព័ន្ធឧបករណ៍ MCP

ពេលកំណត់រចនាសម្ព័ន្ធឧបករណ៍ MCP សម្រាប់ភ្នាក់ងារបស់អ្នក អ្នកអាចបញ្ជាក់ប៉ារ៉ាម៉ែត្រសំខាន់ៗជាច្រើន៖

### ការកំណត់រចនាសម្ព័ន្ធ Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # អត្តសញ្ញាណសម្រាប់ម៉ាស៊ីនមេ MCP
    server_url="https://api.example.com/mcp", # ចំណុចចំនុចបេះដូងម៉ាស៊ីនមេ MCP
    allowed_tools=[],                       # ជម្រើស: បញ្ជាក់ឧបករណ៍ដែលអនុញ្ញាត
)
```

### ការកំណត់រចនាសម្ព័ន្ធ .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## ការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ និងក្បាលសំណុំបែបបទ

ទាំងពីររូបមន្តគាំទ្រក្បាលបែបបទប្ដូរជាផ្ទាល់ខ្លួនសម្រាប់ការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ៖

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## ការដោះស្រាយបញ្ហាញឹកញាប់

### 1. បញ្ហាការតភ្ជាប់
- ពិនិត្យមើលថា URL ម៉ាស៊ីនបម្រើ MCP អាចចូលដំណើរការបាន
- ពិនិត្យអត្តសញ្ញាណ Credentials
- ប្រាកដថាបណ្តាញអ៊ីនធឺណិតតភ្ជាប់បានល្អ

### 2. បញ្ហាការហៅឧបករណ៍បរាជ័យ
- ពិនិត្យអាគុយម៉ង់និងទ្រង់ទ្រាយនៃការហៅឧបករណ៍
- ពិនិត្យតម្រូវការពិសេសរបស់ម៉ាស៊ីនបម្រើ
- អនុវត្តការគ្រប់គ្រងករណីកើតមានកំហុសនិងក្លិន

### 3. បញ្ហាដំណើរការលឿន
- បង្កើតការប្រព្រឹត្តិការហៅឧបករណ៍ ទ្វេដងវិញឲ្យប្រសើរ
- អនុវត្តការចងចាំតម្លៃកន្លែងដែលសមរម្យ
- តាមដានពេលវេលាចម្លើយម៉ាស៊ីនបម្រើ

## ជំហានបន្ទាប់

ដើម្បីពង្រឹងការរួមបញ្ចូល MCP របស់អ្នកបន្ថែម៖

1. **ស្វែងយល់អំពីម៉ាស៊ីនបម្រើ MCP ផ្ទាល់ខ្លួន**៖ បង្កើតម៉ាស៊ីនបម្រើ MCP សម្រាប់ប្រភពទិន្នន័យផ្ទាល់ខ្លួន
2. **អនុវត្តសុវត្ថិភាពកម្រិតខ្ពស់**៖ បញ្ចូល OAuth2 ឬមេកានិចផ្ទៀងផ្ទាត់ខុសប្លែក
3. **តាមដាននិងវិភាគ**៖ អនុវត្តការចុះបញ្ជី និងតាមដានការប្រើប្រាស់ឧបករណ៍
4. **ពង្រីកដំណោះស្រាយរបស់អ្នក**៖ ពិចារណាអំពីការចែកបន្ទុកនិងរចនាសម្ព័ន្ធម៉ាស៊ីនបម្រើ MCP ចូលចិត្តចែកចាយ

## ឯកសារបន្ថែម

- [ឯកសារបស់ Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [គំរូ Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [ទិដ្ឋភាពទូទៅភ្នាក់ងារ Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [កិច្ចព្រមព្រៀង MCP](https://spec.modelcontextprotocol.io/)

## សេវាទាញ

សម្រាប់ការគាំទ្របន្ថែម និងសំណួរ៖
- ពិនិត្យឯកសារ [Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- ពិនិត្យធនធានសហគមន៍ [MCP](https://modelcontextprotocol.io/)

## តើជំហានបន្ទាប់ មានអ្វីខ្លះ

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:  
ឯកសារនេះបានប្រែសម្រួលដោយប្រើសេវាកម្មបปลម្ដាប់ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ថាការប្រែសម្រួលដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅភាសាមូលដ្ឋានគឺត្រូវបានគេពិចារណាថាជាឧទាហរណ៍នៅក្នុងប្រភពផ្លូវការជាចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ ត្រូវបានផ្តល់អនុសាសន៍ឱ្យប្រើការប្រែសម្រួលដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសពីការប្រើប្រាស់ការប្រែសម្រួលនេះនោះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->