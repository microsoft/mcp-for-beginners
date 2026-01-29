# Intégration du Model Context Protocol (MCP) avec Azure AI Foundry

Ce guide montre comment intégrer les serveurs Model Context Protocol (MCP) avec les agents Azure AI Foundry, permettant une orchestration avancée des outils et des capacités d’IA d’entreprise.

## Introduction

Le Model Context Protocol (MCP) est une norme ouverte qui permet aux applications d’IA de se connecter de manière sécurisée à des sources de données et outils externes. Lorsqu’il est intégré à Azure AI Foundry, MCP permet aux agents d’accéder et d’interagir avec divers services externes, API et sources de données de façon standardisée.

Cette intégration combine la flexibilité de l’écosystème d’outils MCP avec le cadre robuste des agents Azure AI Foundry, offrant des solutions d’IA de niveau entreprise avec de larges possibilités de personnalisation.

**Note :** Si vous souhaitez utiliser MCP dans Azure AI Foundry Agent Service, seules les régions suivantes sont actuellement prises en charge : westus, westus2, uaenorth, southindia et switzerlandnorth

## Objectifs d’apprentissage

À la fin de ce guide, vous serez capable de :

- Comprendre le Model Context Protocol et ses avantages
- Configurer des serveurs MCP pour une utilisation avec les agents Azure AI Foundry
- Créer et configurer des agents avec intégration des outils MCP
- Mettre en œuvre des exemples pratiques avec de vrais serveurs MCP
- Gérer les réponses des outils et les citations dans les conversations des agents

## Prérequis

Avant de commencer, assurez-vous de disposer de :

- Un abonnement Azure avec accès à AI Foundry
- Python 3.10+ ou .NET 8.0+
- Azure CLI installé et configuré
- Les permissions nécessaires pour créer des ressources AI

## Qu’est-ce que le Model Context Protocol (MCP) ?

Le Model Context Protocol est une méthode standardisée permettant aux applications d’IA de se connecter à des sources de données et outils externes. Ses principaux avantages sont :

- **Intégration standardisée** : Interface cohérente entre différents outils et services
- **Sécurité** : Mécanismes d’authentification et d’autorisation sécurisés
- **Flexibilité** : Support de diverses sources de données, API et outils personnalisés
- **Extensibilité** : Facilité d’ajout de nouvelles fonctionnalités et intégrations

## Configuration de MCP avec Azure AI Foundry

### Configuration de l’environnement

Choisissez votre environnement de développement préféré :

- [Implémentation Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Implémentation .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Implémentation Python

***Note*** Vous pouvez exécuter ce [notebook](mcp_support_python.ipynb)

### 1. Installer les packages requis

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importer les dépendances

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Configurer les paramètres MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Initialiser le client du projet

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Créer l’outil MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Exemple complet en Python

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

## Implémentation .NET

***Note*** Vous pouvez exécuter ce [notebook](mcp_support_dotnet.ipynb)

### 1. Installer les packages requis

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importer les dépendances

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Configurer les paramètres

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Créer la définition de l’outil MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Créer un agent avec les outils MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Exemple complet en .NET

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

## Options de configuration des outils MCP

Lors de la configuration des outils MCP pour votre agent, vous pouvez spécifier plusieurs paramètres importants :

### Configuration Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Configuration .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Authentification et en-têtes

Les deux implémentations supportent des en-têtes personnalisés pour l’authentification :

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Résolution des problèmes courants

### 1. Problèmes de connexion
- Vérifiez que l’URL du serveur MCP est accessible
- Contrôlez les identifiants d’authentification
- Assurez-vous de la connectivité réseau

### 2. Échecs d’appel d’outil
- Vérifiez les arguments et leur format
- Contrôlez les exigences spécifiques du serveur
- Implémentez une gestion d’erreurs appropriée

### 3. Problèmes de performance
- Optimisez la fréquence des appels aux outils
- Mettez en place un cache si nécessaire
- Surveillez les temps de réponse du serveur

## Étapes suivantes

Pour améliorer davantage votre intégration MCP :

1. **Explorez les serveurs MCP personnalisés** : Créez vos propres serveurs MCP pour des sources de données propriétaires
2. **Implémentez une sécurité avancée** : Ajoutez OAuth2 ou des mécanismes d’authentification personnalisés
3. **Surveillance et analyses** : Mettez en place des journaux et un suivi de l’utilisation des outils
4. **Mettez à l’échelle votre solution** : Envisagez l’équilibrage de charge et des architectures distribuées pour les serveurs MCP

## Ressources supplémentaires

- [Documentation Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Exemples Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Présentation des agents Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Spécification MCP](https://spec.modelcontextprotocol.io/)

## Support

Pour un support supplémentaire et des questions :
- Consultez la [documentation Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Consultez les [ressources communautaires MCP](https://modelcontextprotocol.io/)

## Et après ?

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.