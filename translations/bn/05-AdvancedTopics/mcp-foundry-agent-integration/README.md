# Model Context Protocol (MCP) Azure AI Foundry-এর সাথে ইন্টিগ্রেশন

এই গাইডটি দেখাবে কিভাবে Model Context Protocol (MCP) সার্ভারগুলোকে Azure AI Foundry এজেন্টের সাথে সংযুক্ত করা যায়, যা শক্তিশালী টুল অর্কেস্ট্রেশন এবং এন্টারপ্রাইজ AI সক্ষমতা প্রদান করে।

## পরিচিতি

Model Context Protocol (MCP) একটি ওপেন স্ট্যান্ডার্ড যা AI অ্যাপ্লিকেশনগুলোকে নিরাপদে বাহ্যিক ডেটা সোর্স এবং টুলের সাথে সংযোগ করার সুযোগ দেয়। Azure AI Foundry-এর সাথে ইন্টিগ্রেট করলে, MCP এজেন্টগুলোকে বিভিন্ন বাহ্যিক সার্ভিস, API এবং ডেটা সোর্সের সাথে স্ট্যান্ডার্ডাইজড উপায়ে অ্যাক্সেস এবং ইন্টারঅ্যাক্ট করার সুযোগ দেয়।

এই ইন্টিগ্রেশন MCP-এর টুল ইকোসিস্টেমের নমনীয়তা এবং Azure AI Foundry-এর শক্তিশালী এজেন্ট ফ্রেমওয়ার্ককে একত্রিত করে, যা বিস্তৃত কাস্টমাইজেশন ক্ষমতা সহ এন্টারপ্রাইজ-গ্রেড AI সলিউশন প্রদান করে।

**Note:** Azure AI Foundry Agent Service-এ MCP ব্যবহার করতে চাইলে, বর্তমানে শুধুমাত্র নিম্নলিখিত অঞ্চলগুলো সমর্থিত: westus, westus2, uaenorth, southindia এবং switzerlandnorth

## শেখার উদ্দেশ্য

এই গাইড শেষ করার পর, আপনি সক্ষম হবেন:

- Model Context Protocol এবং এর সুবিধাগুলো বুঝতে
- Azure AI Foundry এজেন্টের সাথে ব্যবহারের জন্য MCP সার্ভার সেটআপ করতে
- MCP টুল ইন্টিগ্রেশন সহ এজেন্ট তৈরি ও কনফিগার করতে
- বাস্তব MCP সার্ভার ব্যবহার করে প্র্যাকটিক্যাল উদাহরণ বাস্তবায়ন করতে
- এজেন্ট কথোপকথনে টুল রেসপন্স এবং উত্স পরিচালনা করতে

## পূর্বশর্ত

শুরু করার আগে নিশ্চিত করুন আপনার কাছে:

- AI Foundry অ্যাক্সেস সহ একটি Azure সাবস্ক্রিপশন
- Python 3.10+ অথবা .NET 8.0+
- Azure CLI ইনস্টল ও কনফিগার করা
- AI রিসোর্স তৈরি করার যথাযথ অনুমতি

## Model Context Protocol (MCP) কী?

Model Context Protocol হলো AI অ্যাপ্লিকেশনগুলোকে বাহ্যিক ডেটা সোর্স এবং টুলের সাথে সংযোগ করার জন্য একটি স্ট্যান্ডার্ডাইজড পদ্ধতি। এর প্রধান সুবিধাসমূহ:

- **স্ট্যান্ডার্ডাইজড ইন্টিগ্রেশন**: বিভিন্ন টুল ও সার্ভিসের জন্য সঙ্গতিপূর্ণ ইন্টারফেস
- **নিরাপত্তা**: নিরাপদ অথেনটিকেশন ও অথরাইজেশন মেকানিজম
- **নমনীয়তা**: বিভিন্ন ডেটা সোর্স, API এবং কাস্টম টুল সমর্থন
- **বিস্তারণযোগ্যতা**: নতুন ক্ষমতা ও ইন্টিগ্রেশন সহজে যোগ করার সুযোগ

## Azure AI Foundry-এর সাথে MCP সেটআপ

### পরিবেশ কনফিগারেশন

আপনার পছন্দসই ডেভেলপমেন্ট পরিবেশ নির্বাচন করুন:

- [Python Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [.NET Implementation](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Python Implementation

***Note*** আপনি এই [নোটবুকটি](mcp_support_python.ipynb) চালাতে পারেন

### ১. প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### ২. ডিপেন্ডেন্সি ইমপোর্ট করুন

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### ৩. MCP সেটিংস কনফিগার করুন

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### ৪. প্রজেক্ট ক্লায়েন্ট ইনিশিয়ালাইজ করুন

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### ৫. MCP টুল তৈরি করুন

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### ৬. সম্পূর্ণ Python উদাহরণ

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

***Note*** আপনি এই [নোটবুকটি](mcp_support_dotnet.ipynb) চালাতে পারেন

### ১. প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### ২. ডিপেন্ডেন্সি ইমপোর্ট করুন

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### ৩. সেটিংস কনফিগার করুন

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### ৪. MCP টুল ডেফিনিশন তৈরি করুন

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### ৫. MCP টুলসহ এজেন্ট তৈরি করুন

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### ৬. সম্পূর্ণ .NET উদাহরণ

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

## MCP টুল কনফিগারেশন অপশনসমূহ

আপনার এজেন্টের জন্য MCP টুল কনফিগার করার সময়, আপনি কয়েকটি গুরুত্বপূর্ণ প্যারামিটার নির্দিষ্ট করতে পারেন:

### Python কনফিগারেশন

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### .NET কনফিগারেশন

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## অথেনটিকেশন এবং হেডারস

উভয় ইমপ্লিমেন্টেশনই অথেনটিকেশনের জন্য কাস্টম হেডার সমর্থন করে:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## সাধারণ সমস্যার সমাধান

### ১. সংযোগ সমস্যা
- MCP সার্ভারের URL অ্যাক্সেসযোগ্য কিনা যাচাই করুন
- অথেনটিকেশন ক্রেডেনশিয়াল চেক করুন
- নেটওয়ার্ক সংযোগ নিশ্চিত করুন

### ২. টুল কল ব্যর্থতা
- টুল আর্গুমেন্ট এবং ফরম্যাটিং পর্যালোচনা করুন
- সার্ভার-নির্দিষ্ট প্রয়োজনীয়তা যাচাই করুন
- সঠিক এরর হ্যান্ডলিং বাস্তবায়ন করুন

### ৩. পারফরম্যান্স সমস্যা
- টুল কলের ফ্রিকোয়েন্সি অপটিমাইজ করুন
- যেখানে প্রয়োজন ক্যাশিং ব্যবহার করুন
- সার্ভার রেসপন্স টাইম মনিটর করুন

## পরবর্তী ধাপ

আপনার MCP ইন্টিগ্রেশন আরও উন্নত করতে:

1. **কাস্টম MCP সার্ভার এক্সপ্লোর করুন**: নিজস্ব MCP সার্ভার তৈরি করুন প্রোপাইটারি ডেটা সোর্সের জন্য
2. **উন্নত নিরাপত্তা বাস্তবায়ন করুন**: OAuth2 বা কাস্টম অথেনটিকেশন মেকানিজম যোগ করুন
3. **মনিটরিং ও অ্যানালিটিক্স**: টুল ব্যবহারের জন্য লগিং ও মনিটরিং বাস্তবায়ন করুন
4. **আপনার সলিউশন স্কেল করুন**: লোড ব্যালেন্সিং এবং বিতরণকৃত MCP সার্ভার আর্কিটেকচার বিবেচনা করুন

## অতিরিক্ত রিসোর্স

- [Azure AI Foundry ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol স্যাম্পলস](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Azure AI Foundry Agents ওভারভিউ](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP স্পেসিফিকেশন](https://spec.modelcontextprotocol.io/)

## সাপোর্ট

অতিরিক্ত সাপোর্ট এবং প্রশ্নের জন্য:
- [Azure AI Foundry ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-foundry/) পর্যালোচনা করুন
- [MCP কমিউনিটি রিসোর্স](https://modelcontextprotocol.io/) দেখুন

## পরবর্তী কী

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।