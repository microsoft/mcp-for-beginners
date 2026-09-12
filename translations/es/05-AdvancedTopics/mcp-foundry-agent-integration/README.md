# Integración del Protocolo de Contexto de Modelo (MCP) con Microsoft Foundry

Esta guía demuestra cómo integrar servidores del Protocolo de Contexto de Modelo (MCP) con agentes de Microsoft Foundry, habilitando una potente orquestación de herramientas y capacidades empresariales de IA.

## Introducción

El Protocolo de Contexto de Modelo (MCP) es un estándar abierto que permite a las aplicaciones de IA conectarse de manera segura a fuentes de datos externas y herramientas. Cuando se integra con Microsoft Foundry, MCP permite que los agentes accedan e interactúen con diversos servicios externos, APIs y fuentes de datos de forma estandarizada.

Esta integración combina la flexibilidad del ecosistema de herramientas de MCP con el sólido marco de agentes de Microsoft Foundry, proporcionando soluciones de IA de grado empresarial con amplias capacidades de personalización.

**Nota:** Si desea usar MCP en el Servicio de Agentes de Microsoft Foundry, actualmente solo se admiten las siguientes regiones: westus, westus2, uaenorth, southindia y switzerlandnorth

## Objetivos de aprendizaje

Al final de esta guía, podrá:

- Entender el Protocolo de Contexto de Modelo y sus beneficios
- Configurar servidores MCP para usarlos con agentes Microsoft Foundry
- Crear y configurar agentes con integración de herramientas MCP
- Implementar ejemplos prácticos usando servidores MCP reales
- Manejar respuestas de herramientas y citas en conversaciones de agentes

## Requisitos previos

Antes de comenzar, asegúrese de tener:

- Una suscripción de Azure con acceso a Microsoft Foundry
- Python 3.10+ o .NET 8.0+
- Azure CLI instalado y configurado
- Permisos adecuados para crear recursos de IA

## ¿Qué es el Protocolo de Contexto de Modelo (MCP)?

El Protocolo de Contexto de Modelo es una forma estandarizada para que las aplicaciones de IA se conecten a fuentes de datos y herramientas externas. Sus beneficios clave incluyen:

- **Integración estandarizada**: Interfaz coherente entre diferentes herramientas y servicios
- **Seguridad**: Mecanismos seguros de autenticación y autorización
- **Flexibilidad**: Soporte para varias fuentes de datos, APIs y herramientas personalizadas
- **Extensibilidad**: Fácil incorporación de nuevas capacidades e integraciones

## Configurando MCP con Microsoft Foundry

### Configuración del entorno

Elija su entorno de desarrollo preferido:

- [Implementación en Python](#implementación-en-python)
- [Implementación en .NET](#codeblock5)

---

## Implementación en Python

***Nota*** Puede ejecutar este [notebook](./mcp_support_python.ipynb)

### 1. Instalar paquetes requeridos

```bash
pip install azure-ai-projects -U
pip install azure-ai-agents==1.1.0b4 -U
pip install azure-identity -U
pip install mcp==1.11.0 -U
```

### 2. Importar dependencias

```python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import McpTool, RequiredMcpToolCall, SubmitToolApprovalAction, ToolApproval
```

### 3. Configurar ajustes de MCP

```python
mcp_server_url = os.environ.get("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
mcp_server_label = os.environ.get("MCP_SERVER_LABEL", "mslearn")
```

### 4. Inicializar cliente del proyecto

```python
project_client = AIProjectClient(
    endpoint="https://your-project-endpoint.services.ai.azure.com/api/projects/your-project",
    credential=DefaultAzureCredential(),
)
```

### 5. Crear herramienta MCP

```python
mcp_tool = McpTool(
    server_label=mcp_server_label,
    server_url=mcp_server_url,
    allowed_tools=[],  # Opcional: especificar herramientas permitidas
)
```

### 6. Ejemplo completo en Python

```python
with project_client:
    agents_client = project_client.agents

    # Crear un nuevo agente con herramientas MCP
    agent = agents_client.create_agent(
        model="Your AOAI Model Deployment",
        name="my-mcp-agent",
        instructions="You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
        tools=mcp_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")
    print(f"MCP Server: {mcp_tool.server_label} at {mcp_tool.server_url}")

    # Crear hilo para comunicación
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Crear mensaje para hilo
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What's difference between Azure OpenAI and OpenAI?",
    )
    print(f"Created message, ID: {message.id}")

    # Gestionar aprobaciones de herramientas y ejecutar agente
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

    # Mostrar conversación
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

## Implementación en .NET

***Nota*** Puede ejecutar este [notebook](./mcp_support_dotnet.ipynb)

### 1. Instalar paquetes requeridos

```csharp
#r "nuget: Azure.AI.Agents.Persistent, 1.1.0-beta.4"
#r "nuget: Azure.Identity, 1.14.2"
```

### 2. Importar dependencias

```csharp
using Azure.AI.Agents.Persistent;
using Azure.Identity;
```

### 3. Configurar ajustes

```csharp
var projectEndpoint = "https://your-project-endpoint.services.ai.azure.com/api/projects/your-project";
var modelDeploymentName = "Your AOAI Model Deployment";
var mcpServerUrl = "https://learn.microsoft.com/api/mcp";
var mcpServerLabel = "mslearn";
PersistentAgentsClient agentClient = new(projectEndpoint, new DefaultAzureCredential());
```

### 4. Crear definición de herramienta MCP

```csharp
MCPToolDefinition mcpTool = new(mcpServerLabel, mcpServerUrl);
```

### 5. Crear agente con herramientas MCP

```csharp
PersistentAgent agent = await agentClient.Administration.CreateAgentAsync(
   model: modelDeploymentName,
   name: "my-learn-agent",
   instructions: "You are a helpful agent that can use MCP tools to assist users. Use the available MCP tools to answer questions and perform tasks.",
   tools: [mcpTool]
   );
```

### 6. Ejemplo completo en .NET

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

## Opciones de configuración para herramientas MCP

Al configurar herramientas MCP para su agente, puede especificar varios parámetros importantes:

### Configuración en Python

```python
mcp_tool = McpTool(
    server_label="unique_server_name",      # Identificador para el servidor MCP
    server_url="https://api.example.com/mcp", # Punto final del servidor MCP
    allowed_tools=[],                       # Opcional: especificar herramientas permitidas
)
```

### Configuración en .NET

```csharp
MCPToolDefinition mcpTool = new(
    "unique_server_name",                   // Server label
    "https://api.example.com/mcp"          // MCP server URL
);
```

## Autenticación y encabezados

Ambas implementaciones soportan encabezados personalizados para autenticación:

### Python
```python
mcp_tool.update_headers("SuperSecret", "123456")
```

### .NET
```csharp
MCPToolResource mcpToolResource = new(mcpServerLabel);
mcpToolResource.UpdateHeader("SuperSecret", "123456");
```

## Resolución de problemas comunes

### 1. Problemas de conexión
- Verifique que la URL del servidor MCP sea accesible
- Revise las credenciales de autenticación
- Asegure la conectividad de red

### 2. Fallos en llamadas a herramientas
- Revise los argumentos y formato de las herramientas
- Verifique requisitos específicos del servidor
- Implemente manejo adecuado de errores

### 3. Problemas de rendimiento
- Optimice la frecuencia de llamadas a herramientas
- Implemente caché donde sea apropiado
- Monitoree los tiempos de respuesta del servidor

## Próximos pasos

Para mejorar aún más su integración MCP:

1. **Explorar servidores MCP personalizados**: Cree sus propios servidores MCP para fuentes de datos propietarias
2. **Implementar seguridad avanzada**: Añada OAuth2 o mecanismos de autenticación personalizados
3. **Monitoreo y análisis**: Implemente registros y monitoreo del uso de herramientas
4. **Escalar su solución**: Considere balanceo de carga y arquitecturas distribuidas para servidores MCP

## Recursos adicionales

- [Documentación de Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Ejemplos del Protocolo de Contexto de Modelo](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/model-context-protocol-samples)
- [Resumen de Agentes de Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/agents/)
- [Especificación MCP](https://modelcontextprotocol.io/specification/2026-07-28/)

## Soporte

Para soporte adicional y preguntas:
- Revise la [documentación de Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- Consulte los [recursos comunitarios de MCP](https://modelcontextprotocol.io/)

## Qué sigue 

- [5.14 Ingeniería de Contexto MCP](../mcp-contextengineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->