# Integrazione del Model Context Protocol (MCP) con Azure AI Foundry

Questa guida mostra come integrare i server Model Context Protocol (MCP) con gli agenti di Azure AI Foundry, abilitando potenti orchestrazioni di strumenti e funzionalità AI aziendali.

## Introduzione

Model Context Protocol (MCP) è uno standard aperto che consente alle applicazioni AI di connettersi in modo sicuro a fonti di dati esterne e strumenti. Integrato con Azure AI Foundry, MCP permette agli agenti di accedere e interagire con vari servizi esterni, API e fonti di dati in modo standardizzato.

Questa integrazione unisce la flessibilità dell’ecosistema di strumenti MCP con il solido framework agenti di Azure AI Foundry, offrendo soluzioni AI di livello enterprise con ampie possibilità di personalizzazione.

**Nota:** Se vuoi usare MCP nel servizio Azure AI Foundry Agent, attualmente sono supportate solo le seguenti regioni: westus, westus2, uaenorth, southindia e switzerlandnorth

## Obiettivi di Apprendimento

Al termine di questa guida, sarai in grado di:

- Comprendere il Model Context Protocol e i suoi vantaggi
- Configurare server MCP per l’uso con agenti Azure AI Foundry
- Creare e configurare agenti con integrazione di strumenti MCP
- Implementare esempi pratici utilizzando server MCP reali
- Gestire risposte degli strumenti e citazioni nelle conversazioni degli agenti

## Prerequisiti

Prima di iniziare, assicurati di avere:

- Un abbonamento Azure con accesso a AI Foundry
- Python 3.10+ o .NET 8.0+
- Azure CLI installata e configurata
- Permessi adeguati per creare risorse AI

## Cos’è il Model Context Protocol (MCP)?

Model Context Protocol è un metodo standardizzato per le applicazioni AI per connettersi a fonti di dati esterne e strumenti. I principali vantaggi includono:

- **Integrazione Standardizzata**: Interfaccia coerente tra diversi strumenti e servizi
- **Sicurezza**: Meccanismi sicuri di autenticazione e autorizzazione
- **Flessibilità**: Supporto per varie fonti dati, API e strumenti personalizzati
- **Estendibilità**: Facile aggiunta di nuove funzionalità e integrazioni

## Configurazione di MCP con Azure AI Foundry

### Configurazione dell’Ambiente

Scegli il tuo ambiente di sviluppo preferito:

- [Implementazione Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Implementazione .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Implementazione Python

***Nota*** Puoi eseguire questo [notebook](mcp_support_python.ipynb)

### 1. Installa i Pacchetti Necessari

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importa le Dipendenze

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Configura le Impostazioni MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inizializza il Client del Progetto

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Crea lo Strumento MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Esempio Completo in Python

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

## Implementazione .NET

***Nota*** Puoi eseguire questo [notebook](mcp_support_dotnet.ipynb)

### 1. Installa i Pacchetti Necessari

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importa le Dipendenze

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Configura le Impostazioni

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Crea la Definizione dello Strumento MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Crea l’Agente con Strumenti MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Esempio Completo in .NET

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

## Opzioni di Configurazione degli Strumenti MCP

Quando configuri gli strumenti MCP per il tuo agente, puoi specificare diversi parametri importanti:

### Configurazione Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Configurazione .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autenticazione e Header

Entrambe le implementazioni supportano header personalizzati per l’autenticazione:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Risoluzione dei Problemi Comuni

### 1. Problemi di Connessione
- Verifica che l’URL del server MCP sia accessibile
- Controlla le credenziali di autenticazione
- Assicurati della connettività di rete

### 2. Fallimenti nelle Chiamate agli Strumenti
- Controlla gli argomenti e il formato delle chiamate agli strumenti
- Verifica i requisiti specifici del server
- Implementa una corretta gestione degli errori

### 3. Problemi di Prestazioni
- Ottimizza la frequenza delle chiamate agli strumenti
- Implementa caching dove opportuno
- Monitora i tempi di risposta del server

## Passi Successivi

Per migliorare ulteriormente la tua integrazione MCP:

1. **Esplora Server MCP Personalizzati**: Crea i tuoi server MCP per fonti dati proprietarie
2. **Implementa Sicurezza Avanzata**: Aggiungi OAuth2 o meccanismi di autenticazione personalizzati
3. **Monitoraggio e Analisi**: Implementa logging e monitoraggio per l’uso degli strumenti
4. **Scala la Tua Soluzione**: Considera il bilanciamento del carico e architetture distribuite per i server MCP

## Risorse Aggiuntive

- [Documentazione Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Esempi Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Panoramica Agenti Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Specifiche MCP](https://spec.modelcontextprotocol.io/)

## Supporto

Per supporto aggiuntivo e domande:
- Consulta la [documentazione Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Verifica le [risorse della community MCP](https://modelcontextprotocol.io/)

## Cosa c’è dopo

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.