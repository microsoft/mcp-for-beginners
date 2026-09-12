# মডেল কনটেক্সট প্রোটোকল (MCP) এর সাথে Microsoft Foundry এর ইন্টিগ্রেশন

এই গাইডটি দেখায় কিভাবে মডেল কনটেক্সট প্রোটোকল (MCP) সার্ভারগুলোকে Microsoft Foundry এজেন্টের সাথে ইন্টিগ্রেট করা যায়, যা শক্তিশালী টুল অর্কেস্ট্রেশন এবং এন্টারপ্রাইজ AI ক্ষমতা সক্ষম করে।

## পরিচিতি

মডেল কনটেক্সট প্রোটোকল (MCP) একটি ওপেন স্ট্যান্ডার্ড যা AI অ্যাপ্লিকেশনগুলোকে সুরক্ষিতভাবে বাহ্যিক ডেটা সোর্স এবং টুলগুলোর সাথে সংযোগ স্থাপন করতে সক্ষম করে। Microsoft Foundry-র সাথে ইন্টিগ্রেট করলে MCP এজেন্টগুলোকে বিভিন্ন বাহ্যিক সার্ভিস, API এবং ডেটা সোর্সে স্ট্যান্ডার্ডIZED পদ্ধতিতে অ্যাক্সেস এবং ইন্টার‍্যাক্ট করার সুযোগ দেয়।

এই ইন্টিগ্রেশন MCP এর টুল ইকোসিস্টেমের নমনীয়তাকে Microsoft Foundry-র শক্তিশালী এজেন্ট ফ্রেমওয়ার্কের সঙ্গে মিলিয়ে এন্টারপ্রাইজ-গ্রেড AI সলিউশন প্রদান করে, বিস্তৃত কাস্টমাইজেশন সুবিধা সহ।

**নোট:** Microsoft Foundry Agent Service-এ MCP ব্যবহারের জন্য বর্তমানে শুধুমাত্র নিম্নলিখিত অঞ্চলগুলো সমর্থিত: westus, westus2, uaenorth, southindia এবং switzerlandnorth

## শেখার লক্ষ্যসমূহ

এই গাইডের শেষ পর্যন্ত, আপনি সক্ষম হবেন:

- মডেল কনটেক্সট প্রোটোকল এবং এর সুবিধা বোঝা
- Microsoft Foundry এজেন্টের সাথে MCP সার্ভার সেটআপ করা
- MCP টুল ইন্টিগ্রেশন সহ এজেন্ট তৈরি এবং কনফিগার করা
- বাস্তব MCP সার্ভার ব্যবহার করে প্র্যাকটিক্যাল উদাহরণ বাস্তবায়ন করা
- এজেন্ট আলাপে টুলস’র রেস্পন্স এবং উদ্ধৃতি পরিচালনা করা

## পূর্বপ্রয়োজনীয়তা

শুরু করার আগে নিশ্চিত করুন আপনার কাছে আছে:

- Microsoft Foundry অ্যাক্সেস সহ একটি Azure সাবস্ক্রিপশন
- Python 3.১০+ অথবা .NET 8.0+
- Azure CLI ইনস্টল ও কনফিগার করা
- AI রিসোর্স তৈরি করার উপযুক্ত অনুমতি

## মডেল কনটেক্সট প্রোটোকল (MCP) কি?

মডেল কনটেক্সট প্রোটোকল একটি স্ট্যান্ডার্ড পদ্ধতি যা AI অ্যাপ্লিকেশনগুলোকে বাহ্যিক ডেটা সোর্স এবং টুলের সাথে সংযুক্ত করতে দেয়। প্রধান সুবিধাসমূহ হলো:

- **স্ট্যান্ডার্ডাইজড ইন্টিগ্রেশন**: বিভিন্ন টুল ও সার্ভিসে সামঞ্জস্যপূর্ণ ইন্টারফেস
- **সুরক্ষা**: সুরক্ষিত অথেন্টিকেশন এবং অথরাইজেশন প্রক্রিয়া
- **নমনীয়তা**: বিভিন্ন ডেটা সোর্স, API এবং কাস্টম টুলকে সমর্থন
- **বিস্তারণযোগ্যতা**: নতুন ক্ষমতা ও ইন্টিগ্রেশন সহজেই যোগ করার সুবিধা

## Microsoft Foundry এর সাথে MCP সেটআপ

### পরিবেশ কনফিগারেশন

আপনার পছন্দসই ডেভেলপমেন্ট পরিবেশ নির্বাচন করুন:

- [Python Implementation](#python-implementation)
- [.NET Implementation](#codeblock5)

---

## Python Implementation

***নোট*** আপনি এই [নোটবুকটি](./mcp_support_python.ipynb) চালাতে পারেন

### ১. প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### ২. ডিপেন্ডেন্সি ইম্পোর্ট করুন

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

### ৪. প্রোজেক্ট ক্লায়েন্ট ইনিশিয়ালাইজ করুন

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
    allowed_tools=[],  # ঐচ্ছিক: অনুমোদিত সরঞ্জামগুলি নির্ধারণ করুন
)
```

### ৬. সম্পূর্ণ Python উদাহরণ

```python
with project_client:
    agents_client = project_client.agents

    # MCP টুলস দিয়ে একটি নতুন এজেন্ট তৈরি করুন
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # যোগাযোগের জন্য থ্রেড তৈরি করুন
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # থ্রেডের জন্য বার্তা তৈরি করুন
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # টুল অনুমোদনগুলি পরিচালনা করুন এবং এজেন্ট চালান
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

    # কথোপকথন প্রদর্শন করুন
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

***নোট*** আপনি এই [নোটবুকটি](./mcp_support_dotnet.ipynb) চালাতে পারেন

### ১. প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### ২. ডিপেন্ডেন্সি ইম্পোর্ট করুন

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

### ৫. MCP টুল সহ এজেন্ট তৈরি করুন

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

## MCP টুল কনফিগারেশন অপশন

আপনার এজেন্টের জন্য MCP টুল কনফিগার করার সময়, আপনি বেশ কিছু গুরুত্বপূর্ণ প্যারামিটার নির্দিষ্ট করতে পারেন:

### Python কনফিগারেশন

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # MCP সার্ভারের জন্য শনাক্তকারী
    server_url="https://api.example.com/mcp", # MCP সার্ভার এন্ডপয়েন্ট
    allowed_tools=[],                       # ঐচ্ছিক: অনুমোদিত সরঞ্জাম নির্দিষ্ট করুন
)
```

### .NET কনফিগারেশন

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## অথেন্টিকেশন এবং হেডারস

উভয় ইম্প্লিমেন্টেশনেই কাস্টম হেডারস সহ অথেন্টিকেশন সমর্থিত:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## সাধারণ সমস্যা সমাধান

### ১. সংযোগ সমস্যা
- MCP সার্ভার URL অ্যাক্সেসযোগ্য কিনা যাচাই করুন
- অথেন্টিকেশন ক্রেডেনশিয়াল চেক করুন
- নেটওয়ার্ক সংযোগ নিশ্চিত করুন

### ২. টুল কল ব্যর্থতা
- টুল আর্গুমেন্ট এবং ফরম্যাটিং পর্যালোচনা করুন
- সার্ভার-নির্দিষ্ট চাহিদা চেক করুন
- সঠিক ত্রুটি পরিচালনা বাস্তবায়ন করুন

### ৩. পারফরম্যান্স সমস্যা
- টুল কলের ফ্রিকোয়েন্সি অপ্টিমাইজ করুন
- প্রয়োজনে ক্যাশিং বাস্তবায়ন করুন
- সার্ভার রেসপন্স সময় মনিটর করুন

## পরবর্তী ধাপ

আপনার MCP ইন্টিগ্রেশন আরও উন্নত করতে:

১. **কাস্টম MCP সার্ভার অন্বেষণ করুন**: নিজস্ব MCP সার্ভার তৈরি করুন প্রোপাইটারি ডেটা সোর্সের জন্য
২. **উন্নত সিকিউরিটি বাস্তবায়ন করুন**: OAuth2 অথবা কাস্টম অথেন্টিকেশন মেকানিজম যোগ করুন
৩. **মনিটরিং এবং অ্যানালিটিক্স**: টুল ব্যবহারের জন্য লগিং এবং মনিটরিং বাস্তবায়ন করুন
৪. **আপনার সলিউশন স্কেল করুন**: লোড ব্যালেন্সিং এবং ডিস্ট্রিবিউটেড MCP সার্ভার আর্কিটেকচার বিবেচনা করুন

## অতিরিক্ত সম্পদ

- [Microsoft Foundry ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-foundry/)
- [Model Context Protocol স্যাম্পলস](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Microsoft Foundry Agents ওভারভিউ](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [MCP স্পেসিফিকেশন](https://modelcontextprotocol.io/specification/2026-07-28/)

## সহায়তা

অতিরিক্ত সহায়তা ও প্রশ্নের জন্য:
- [Microsoft Foundry ডকুমেন্টেশন পর্যালোচনা করুন](https://learn.microsoft.com/azure/ai-foundry/)
- [MCP কমিউনিটি রিসোর্স চেক করুন](https://modelcontextprotocol.io/)

## পরবর্তীতে কী

- [5.14 MCP কনটেক্সট ইঞ্জিনিয়ারিং](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->