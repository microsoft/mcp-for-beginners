# Integrarea Model Context Protocol (MCP) cu Microsoft Foundry

Acest ghid demonstrează cum să integrați serverele Model Context Protocol (MCP) cu agenții Microsoft Foundry, permițând orchestrarea puternică a instrumentelor și capabilități AI de nivel enterprise.

## Introducere

Model Context Protocol (MCP) este un standard deschis care permite aplicațiilor AI să se conecteze în mod securizat la surse de date și instrumente externe. Integrat cu Microsoft Foundry, MCP oferă agenților acces și interacțiune cu diverse servicii externe, API-uri și surse de date într-un mod standardizat.

Această integrare combină flexibilitatea ecosistemului de instrumente MCP cu cadrul robust pentru agenți Microsoft Foundry, furnizând soluții AI de nivel enterprise cu capacități extinse de personalizare.

**Notă:** Dacă doriți să utilizați MCP în Microsoft Foundry Agent Service, momentan sunt acceptate doar următoarele regiuni: westus, westus2, uaenorth, southindia și switzerlandnorth

## Obiective de învățare

La finalul acestui ghid veți putea:

- Înțelege Model Context Protocol și avantajele sale
- Configura servere MCP pentru utilizare cu agenții Microsoft Foundry
- Crea și configura agenți cu integrare a instrumentelor MCP
- Implementa exemple practice folosind servere reale MCP
- Gestiona răspunsurile instrumentelor și citările în conversațiile agenților

## Cerințe preliminare

Înainte de a începe, asigurați-vă că aveți:

- Un abonament Azure cu acces la Microsoft Foundry
- Python 3.10+ sau .NET 8.0+
- Azure CLI instalat și configurat
- Permisiunile necesare pentru a crea resurse AI

## Ce este Model Context Protocol (MCP)?

Model Context Protocol este o metodă standardizată ca aplicațiile AI să se conecteze la surse externe de date și instrumente. Beneficiile principale includ:

- **Integrare Standardizată**: Interfață coerentă pentru diferite instrumente și servicii
- **Securitate**: Mecanisme sigure de autentificare și autorizare
- **Flexibilitate**: Suport pentru surse diverse de date, API-uri și instrumente personalizate
- **Extensibilitate**: Ușor de adăugat funcționalități și integrări noi

## Configurarea MCP cu Microsoft Foundry

### Configurarea mediului

Alegeți mediul de dezvoltare preferat:

- [Implementare Python](#implementare-python)
- [Implementare .NET](#codeblock5)

---

## Implementare Python

***Notă*** Puteți rula acest [notebook](./mcp_support_python.ipynb)

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

### 4. Inițializarea clientului proiectului

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Crearea instrumentului MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Opțional: specificați instrumentele permise
)
```

### 6. Exemplu complet Python

```python
with project_client:
    agents_client = project_client.agents

    # Creează un nou agent cu instrumentele MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Creează un fir pentru comunicare
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Creează un mesaj pentru fir
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Gestionează aprobările pentru instrumente și rulează agentul
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

    # Afișează conversația
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

***Notă*** Puteți rula acest [notebook](./mcp_support_dotnet.ipynb)

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

### 4. Crearea definiției instrumentului MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Crearea agentului cu instrumentele MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Exemplu complet .NET

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

## Opțiuni de configurare a instrumentului MCP

Când configurați instrumentele MCP pentru agentul vostru, puteți specifica mai mulți parametri importanți:

### Configurare Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identificator pentru serverul MCP
    server_url="https://api.example.com/mcp", # Punct de acces al serverului MCP
    allowed_tools=[],                       # Opțional: specificați uneltele permise
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

## Soluționarea problemelor comune

### 1. Probleme de conectare
- Verificați dacă URL-ul serverului MCP este accesibil
- Verificați acreditările de autentificare
- Asigurați conectivitatea de rețea

### 2. Eșecuri la apelurile instrumentelor
- Revizuiți argumentele instrumentelor și formatarea
- Verificați cerințele specifice serverului
- Implementați o tratare adecvată a erorilor

### 3. Probleme de performanță
- Optimizați frecvența apelurilor instrumentelor
- Implementați caching acolo unde este potrivit
- Monitorizați timpii de răspuns ai serverului

## Pași următori

Pentru a vă îmbunătăți integrarea MCP:

1. **Explorați servere MCP personalizate**: Construiți propriile servere MCP pentru surse de date proprietare
2. **Implementați securitate avansată**: Adăugați OAuth2 sau mecanisme personalizate de autentificare
3. **Monitorizare și analiză**: Implementați logare și monitorizare pentru utilizarea instrumentelor
4. **Scalați soluția**: Luați în considerare balansarea încărcării și arhitecturile distribuite ale serverului MCP

## Resurse suplimentare

- [Documentația Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Exemple Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Prezentare generală Microsoft Foundry Agents](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Specificația MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Suport

Pentru suport suplimentar și întrebări:
- Consultați [documentația Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Verificați [resursele comunității MCP](https://modelcontextprotocol.io/)

## Ce urmează

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->