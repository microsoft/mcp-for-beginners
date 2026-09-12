# Ενσωμάτωση Model Context Protocol (MCP) με το Microsoft Foundry

Αυτός ο οδηγός δείχνει πώς να ενσωματώσετε τους διακομιστές Model Context Protocol (MCP) με τους πράκτορες του Microsoft Foundry, επιτρέποντας ισχυρή ορχήστρωση εργαλείων και δυνατότητες επιχειρησιακής AI.

## Εισαγωγή

Το Model Context Protocol (MCP) είναι ένα ανοιχτό πρότυπο που επιτρέπει στις εφαρμογές AI να συνδέονται με ασφάλεια σε εξωτερικές πηγές δεδομένων και εργαλεία. Όταν ενσωματώνεται με το Microsoft Foundry, το MCP επιτρέπει στους πράκτορες να έχουν πρόσβαση και να αλληλεπιδρούν με διάφορες εξωτερικές υπηρεσίες, APIs και πηγές δεδομένων με έναν τυποποιημένο τρόπο.

Αυτή η ενσωμάτωση συνδυάζει την ευελιξία του οικοσυστήματος εργαλείων του MCP με το στιβαρό πλαίσιο πρακτόρων του Microsoft Foundry, παρέχοντας λύσεις AI επιπέδου επιχείρησης με εκτεταμένες δυνατότητες προσαρμογής.

**Σημείωση:** Εάν θέλετε να χρησιμοποιήσετε το MCP στην Υπηρεσία Πρακτόρων Microsoft Foundry, προς το παρόν υποστηρίζονται μόνο οι εξής περιοχές: westus, westus2, uaenorth, southindia και switzerlandnorth

## Μαθησιακοί Στόχοι

Μέχρι το τέλος αυτού του οδηγού, θα είστε σε θέση να:

- Κατανοήσετε το Model Context Protocol και τα οφέλη του
- Ρυθμίσετε διακομιστές MCP για χρήση με πράκτορες Microsoft Foundry
- Δημιουργήσετε και να διαμορφώσετε πράκτορες με ενσωμάτωση εργαλείων MCP
- Εφαρμόσετε πρακτικά παραδείγματα χρησιμοποιώντας πραγματικούς διακομιστές MCP
- Διαχειριστείτε τις απαντήσεις εργαλείων και τις αναφορές σε συνομιλίες πρακτόρων

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε:

- Μια συνδρομή Azure με πρόσβαση στο Microsoft Foundry
- Python 3.10+ ή .NET 8.0+
- Το Azure CLI εγκατεστημένο και ρυθμισμένο
- Κατάλληλες άδειες για δημιουργία πόρων AI

## Τι είναι το Model Context Protocol (MCP);

Το Model Context Protocol είναι ένας τυποποιημένος τρόπος για εφαρμογές AI να συνδέονται σε εξωτερικές πηγές δεδομένων και εργαλεία. Τα βασικά οφέλη περιλαμβάνουν:

- **Τυποποιημένη Ενσωμάτωση**: Συνεπές περιβάλλον εργασίας σε διάφορα εργαλεία και υπηρεσίες
- **Ασφάλεια**: Μηχανισμοί ασφαλούς αυθεντικοποίησης και αδειοδότησης
- **Ευελιξία**: Υποστήριξη για διάφορες πηγές δεδομένων, APIs, και προσαρμοσμένα εργαλεία
- **Επεκτασιμότητα**: Ευκολία στην προσθήκη νέων δυνατοτήτων και ενσωματώσεων

## Ρύθμιση MCP με Microsoft Foundry

### Διαμόρφωση Περιβάλλοντος

Επιλέξτε το προτιμώμενο περιβάλλον ανάπτυξής σας:

- [Υλοποίηση Python](#υλοποίηση-python)
- [Υλοποίηση .NET](#codeblock5)

---

## Υλοποίηση Python

***Σημείωση*** Μπορείτε να τρέξετε αυτό το [notebook](./mcp_support_python.ipynb)

### 1. Εγκατάσταση Απαραίτητων Πακέτων

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Εισαγωγή Εξαρτήσεων

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Διαμόρφωση Ρυθμίσεων MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Αρχικοποίηση Πελάτη Έργου

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Δημιουργία Εργαλείου MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Προαιρετικό: καθορίστε τα επιτρεπόμενα εργαλεία
)
```

### 6. Πλήρες Παράδειγμα Python

```python
with project_client:
    agents_client = project_client.agents

    # Δημιουργήστε έναν νέο πράκτορα με εργαλεία MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Δημιουργήστε ένα νήμα για επικοινωνία
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Δημιουργήστε μήνυμα για το νήμα
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Διαχειριστείτε τις εγκρίσεις εργαλείων και εκτελέστε τον πράκτορα
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

    # Εμφανίστε τη συνομιλία
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

## Υλοποίηση .NET

***Σημείωση*** Μπορείτε να τρέξετε αυτό το [notebook](./mcp_support_dotnet.ipynb)

### 1. Εγκατάσταση Απαραίτητων Πακέτων

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Εισαγωγή Εξαρτήσεων

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Διαμόρφωση Ρυθμίσεων

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Δημιουργία Ορισμού Εργαλείου MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Δημιουργία Πράκτορα με Εργαλεία MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Πλήρες Παράδειγμα .NET

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

## Επιλογές Διαμόρφωσης Εργαλείων MCP

Κατά τη διαμόρφωση των εργαλείων MCP για τον πράκτορά σας, μπορείτε να καθορίσετε αρκετές σημαντικές παραμέτρους:

### Διαμόρφωση Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Αναγνωριστικό για τον διακομιστή MCP
    server_url="https://api.example.com/mcp", # Τελικό σημείο διακομιστή MCP
    allowed_tools=[],                       # Προαιρετικό: καθορίστε τα επιτρεπόμενα εργαλεία
)
```

### Διαμόρφωση .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Αυθεντικοποίηση και Headers

Και οι δύο υλοποιήσεις υποστηρίζουν προσαρμοσμένα headers για αυθεντικοποίηση:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Αντιμετώπιση Συνήθων Προβλημάτων

### 1. Προβλήματα Σύνδεσης
- Επιβεβαιώστε ότι το URL του διακομιστή MCP είναι προσβάσιμο
- Ελέγξτε τα διαπιστευτήρια αυθεντικοποίησης
- Διασφαλίστε τη συνδεσιμότητα δικτύου

### 2. Αποτυχίες Κλήσης Εργαλείων
- Επανεξετάστε τα ορίσματα και τη μορφοποίηση εργαλείων
- Ελέγξτε τις απαιτήσεις ειδικές για τον διακομιστή
- Εφαρμόστε σωστή διαχείριση σφαλμάτων

### 3. Προβλήματα Απόδοσης
- Βελτιστοποιήστε τη συχνότητα κλήσης εργαλείων
- Εφαρμόστε caching όπου είναι κατάλληλο
- Παρακολουθήστε τους χρόνους απόκρισης διακομιστή

## Επόμενα Βήματα

Για περαιτέρω βελτίωση της ενσωμάτωσής σας με MCP:

1. **Εξερευνήστε Προσαρμοσμένους Διακομιστές MCP**: Δημιουργήστε τους δικούς σας διακομιστές MCP για ιδιόκτητες πηγές δεδομένων
2. **Εφαρμόστε Προχωρημένη Ασφάλεια**: Προσθέστε μηχανισμούς OAuth2 ή προσαρμοσμένης αυθεντικοποίησης
3. **Παρακολούθηση και Αναλύσεις**: Εφαρμόστε καταγραφές και παρακολούθηση για τη χρήση εργαλείων
4. **Κλιμάκωση της Λύσης Σας**: Σκεφτείτε ζυγοστάθμιση φορτίου και κατανεμημένες αρχιτεκτονικές διακομιστών MCP

## Πρόσθετοι Πόροι

- [Τεκμηρίωση Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Δείγματα Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Επισκόπηση Πρακτόρων Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Προδιαγραφή MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Υποστήριξη

Για επιπλέον υποστήριξη και ερωτήσεις:
- Ανατρέξτε στην [τεκμηρίωση Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Ελέγξτε τους [πόρους της κοινότητας MCP](https://modelcontextprotocol.io/)

## Τι ακολουθεί 

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->