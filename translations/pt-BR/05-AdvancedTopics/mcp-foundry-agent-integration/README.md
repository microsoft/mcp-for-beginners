# Integração do Model Context Protocol (MCP) com Azure AI Foundry

Este guia demonstra como integrar servidores Model Context Protocol (MCP) com agentes Azure AI Foundry, possibilitando uma orquestração poderosa de ferramentas e capacidades de IA corporativa.

## Introdução

Model Context Protocol (MCP) é um padrão aberto que permite que aplicações de IA se conectem de forma segura a fontes de dados e ferramentas externas. Quando integrado ao Azure AI Foundry, o MCP permite que agentes acessem e interajam com diversos serviços externos, APIs e fontes de dados de maneira padronizada.

Essa integração combina a flexibilidade do ecossistema de ferramentas do MCP com a estrutura robusta de agentes do Azure AI Foundry, oferecendo soluções de IA corporativas com amplas possibilidades de personalização.

**Note:** Se você deseja usar MCP no Azure AI Foundry Agent Service, atualmente apenas as seguintes regiões são suportadas: westus, westus2, uaenorth, southindia e switzerlandnorth

## Objetivos de Aprendizagem

Ao final deste guia, você será capaz de:

- Compreender o Model Context Protocol e seus benefícios
- Configurar servidores MCP para uso com agentes Azure AI Foundry
- Criar e configurar agentes com integração de ferramentas MCP
- Implementar exemplos práticos usando servidores MCP reais
- Gerenciar respostas de ferramentas e citações em conversas dos agentes

## Pré-requisitos

Antes de começar, certifique-se de que você possui:

- Uma assinatura Azure com acesso ao AI Foundry
- Python 3.10+ ou .NET 8.0+
- Azure CLI instalado e configurado
- Permissões adequadas para criar recursos de IA

## O que é Model Context Protocol (MCP)?

Model Context Protocol é uma forma padronizada para aplicações de IA se conectarem a fontes de dados e ferramentas externas. Os principais benefícios incluem:

- **Integração Padronizada**: Interface consistente entre diferentes ferramentas e serviços
- **Segurança**: Mecanismos seguros de autenticação e autorização
- **Flexibilidade**: Suporte a diversas fontes de dados, APIs e ferramentas personalizadas
- **Extensibilidade**: Facilidade para adicionar novas funcionalidades e integrações

## Configurando MCP com Azure AI Foundry

### Configuração do Ambiente

Escolha seu ambiente de desenvolvimento preferido:

- [Implementação em Python](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)
- [Implementação em .NET](../../../../05-AdvancedTopics/mcp-foundry-agent-integration)

---

## Implementação em Python

***Note*** Você pode executar este [notebook](mcp_support_python.ipynb)

### 1. Instalar Pacotes Necessários

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importar Dependências

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Configurar as Definições do MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicializar o Cliente do Projeto

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Criar a Ferramenta MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Optional: specify allowed tools
)
```

### 6. Exemplo Completo em Python

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

## Implementação em .NET

***Note*** Você pode executar este [notebook](mcp_support_dotnet.ipynb)

### 1. Instalar Pacotes Necessários

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importar Dependências

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Configurar as Definições

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Criar a Definição da Ferramenta MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Criar Agente com Ferramentas MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Exemplo Completo em .NET

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

## Opções de Configuração da Ferramenta MCP

Ao configurar ferramentas MCP para seu agente, você pode especificar vários parâmetros importantes:

### Configuração em Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identifier for the MCP server
    server_url="https://api.example.com/mcp", # MCP server endpoint
    allowed_tools=[],                       # Optional: specify allowed tools
)
```

### Configuração em .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autenticação e Headers

Ambas as implementações suportam headers personalizados para autenticação:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Solução de Problemas Comuns

### 1. Problemas de Conexão
- Verifique se a URL do servidor MCP está acessível
- Confira as credenciais de autenticação
- Garanta a conectividade de rede

### 2. Falhas em Chamadas de Ferramentas
- Revise os argumentos e a formatação das chamadas
- Verifique requisitos específicos do servidor
- Implemente tratamento adequado de erros

### 3. Problemas de Desempenho
- Otimize a frequência das chamadas às ferramentas
- Utilize cache quando apropriado
- Monitore os tempos de resposta do servidor

## Próximos Passos

Para aprimorar ainda mais sua integração MCP:

1. **Explore Servidores MCP Personalizados**: Construa seus próprios servidores MCP para fontes de dados proprietárias
2. **Implemente Segurança Avançada**: Adicione OAuth2 ou mecanismos personalizados de autenticação
3. **Monitore e Analise**: Implemente logging e monitoramento do uso das ferramentas
4. **Escale Sua Solução**: Considere balanceamento de carga e arquiteturas distribuídas para servidores MCP

## Recursos Adicionais

- [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Exemplos do Model Context Protocol](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Visão Geral dos Agentes Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Especificação MCP](https://spec.modelcontextprotocol.io/)

## Suporte

Para suporte adicional e dúvidas:
- Consulte a [documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Verifique os [recursos da comunidade MCP](https://modelcontextprotocol.io/)

## O que vem a seguir

- [5.14 MCP Context Engineering](../mcp-contextengineering/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.