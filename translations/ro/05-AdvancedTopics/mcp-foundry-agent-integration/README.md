# Integrarea Model Context Protocol (MCP) cu Azure AI Foundry

Acest ghid arată cum să integrezi serverele Model Context Protocol (MCP) cu agenții Azure AI Foundry, oferind o orchestrare puternică a uneltelor și capabilități AI pentru mediul enterprise.

## Introducere

Model Context Protocol (MCP) este un standard deschis care permite aplicațiilor AI să se conecteze în mod securizat la surse externe de date și unelte. Integrat cu Azure AI Foundry, MCP permite agenților să acceseze și să interacționeze cu diverse servicii externe, API-uri și surse de date într-un mod standardizat.

Această integrare combină flexibilitatea ecosistemului de unelte MCP cu cadrul robust al agenților Azure AI Foundry, oferind soluții AI de nivel enterprise cu posibilități extinse de personalizare.

**Note:** Dacă dorești să folosești MCP în Azure AI Foundry Agent Service, în prezent sunt suportate doar următoarele regiuni: westus, westus2, uaenorth, southindia și switzerlandnorth

## Obiective de învățare

La finalul acestui ghid vei putea:

- Înțelege Model Context Protocol și beneficiile sale
- Configura servere MCP pentru utilizare cu agenții Azure AI Foundry
- Crea și configura agenți cu integrare MCP pentru unelte
- Implementa exemple practice folosind servere MCP reale
- Gestiona răspunsurile uneltelor și citările în conversațiile agenților

## Cerințe preliminare

Înainte de a începe, asigură-te că ai:

- Un abonament Azure cu acces la AI Foundry
- Python 3.10+ sau .NET 8.0+
- Azure CLI instalat și configurat
- Permisiunile necesare pentru a crea resurse AI

## Ce este Model Context Protocol (MCP)?

Model Context Protocol este o metodă standardizată prin care aplicațiile AI se conectează la surse externe de date și unelte. Beneficiile cheie includ:

- **Integrare standardizată**: Interfață consistentă pentru diferite unelte și servicii
- **Securitate**: Mecanisme sigure de autentificare și autorizare
- **Flexibilitate**: Suport pentru diverse surse de date, API-uri și unelte personalizate
- **Extensibilitate**: Ușor de adăugat noi capabilități și integrări

## Configurarea MCP cu Azure AI Foundry

### Configurarea mediului

Alege mediul de dezvoltare preferat:

- [Implementare Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Implementare .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Implementare Python

***Note*** Poți rula acest [notebook](mcp_support_python.ipynb)

### 1. Instalarea pachetelor necesare

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importarea dependențelor

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Configurarea setărilor MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inițializarea clientului de proiect

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Crearea uneltei MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Exemplu complet în Python

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

## Implementare .NET

***Note*** Poți rula acest [notebook](mcp_support_dotnet.ipynb)

### 1. Instalarea pachetelor necesare

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importarea dependențelor

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Configurarea setărilor

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Crearea definiției uneltei MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Crearea agentului cu unelte MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Exemplu complet în .NET

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

## Opțiuni de configurare pentru uneltele MCP

Când configurezi uneltele MCP pentru agentul tău, poți specifica mai mulți parametri importanți:

### Configurare Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Configurare .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autentificare și antete

Ambele implementări suportă antete personalizate pentru autentificare:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Depanarea problemelor comune

### 1. Probleme de conexiune
- Verifică dacă URL-ul serverului MCP este accesibil
- Verifică credențialele de autentificare
- Asigură-te că există conectivitate de rețea

### 2. Eșecuri la apelul uneltei
- Revizuiește argumentele și formatul apelului uneltei
- Verifică cerințele specifice serverului
- Implementează o gestionare corectă a erorilor

### 3. Probleme de performanță
- Optimizează frecvența apelurilor către unelte
- Folosește caching acolo unde este potrivit
- Monitorizează timpii de răspuns ai serverului

## Pașii următori

Pentru a-ți îmbunătăți integrarea MCP:

1. **Explorează servere MCP personalizate**: Construiește propriile servere MCP pentru surse de date proprietare
2. **Implementează securitate avansată**: Adaugă OAuth2 sau mecanisme personalizate de autentificare
3. **Monitorizare și analiză**: Implementează logare și monitorizare pentru utilizarea uneltelor
4. **Scalează soluția**: Ia în considerare echilibrarea încărcării și arhitecturi distribuite pentru serverele MCP

## Resurse suplimentare

- [Documentația Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Exemple Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Prezentare generală Azure AI Foundry Agents](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Specificația MCP](https://spec.modelcontextprotocol.io/)

## Suport

Pentru suport suplimentar și întrebări:
- Consultă [documentația Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Verifică [resursele comunității MCP](https://modelcontextprotocol.io/)

## Ce urmează

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.