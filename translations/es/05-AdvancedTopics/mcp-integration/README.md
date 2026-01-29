# Integración Empresarial

Al construir servidores MCP en un contexto empresarial, a menudo necesitas integrarte con plataformas y servicios de IA existentes. Esta sección cubre cómo integrar MCP con sistemas empresariales como Azure OpenAI y Microsoft AI Foundry, habilitando capacidades avanzadas de IA y orquestación de herramientas.

## Introducción

En esta lección, aprenderás cómo integrar el Protocolo de Contexto de Modelos (MCP) con sistemas de IA empresariales, centrándote en Azure OpenAI y Microsoft AI Foundry. Estas integraciones te permiten aprovechar modelos y herramientas de IA potentes mientras mantienes la flexibilidad y extensibilidad de MCP.

## Objetivos de Aprendizaje

Al final de esta lección, serás capaz de:

- Integrar MCP con Azure OpenAI para utilizar sus capacidades de IA.
- Implementar la orquestación de herramientas MCP con Azure OpenAI.
- Combinar MCP con Microsoft AI Foundry para capacidades avanzadas de agentes de IA.
- Aprovechar Azure Machine Learning (ML) para ejecutar pipelines de ML y registrar modelos como herramientas MCP.

## Integración con Azure OpenAI

Azure OpenAI proporciona acceso a modelos de IA potentes como GPT-4 y otros. Integrar MCP con Azure OpenAI te permite utilizar estos modelos mientras mantienes la flexibilidad de la orquestación de herramientas de MCP.

### Implementación en C#

En este fragmento de código, demostramos cómo integrar MCP con Azure OpenAI utilizando el SDK de Azure OpenAI.

```csharp
// .NET Azure OpenAI Integration
using Microsoft.Mcp.Client;
using Azure.AI.OpenAI;
using Microsoft.Extensions.Configuration;
using System.Threading.Tasks;

namespace EnterpriseIntegration
{
    public class AzureOpenAiMcpClient
    {
        private readonly string _endpoint;
        private readonly string _apiKey;
        private readonly string _deploymentName;
        
        public AzureOpenAiMcpClient(IConfiguration config)
        {
            _endpoint = config["AzureOpenAI:Endpoint"];
            _apiKey = config["AzureOpenAI:ApiKey"];
            _deploymentName = config["AzureOpenAI:DeploymentName"];
        }
        
        public async Task<string> GetCompletionWithToolsAsync(string prompt, params string[] allowedTools)
        {
            // Create OpenAI client
            var client = new OpenAIClient(new Uri(_endpoint), new AzureKeyCredential(_apiKey));
            
            // Create completion options with tools
            var completionOptions = new ChatCompletionsOptions
            {
                DeploymentName = _deploymentName,
                Messages = { new ChatMessage(ChatRole.User, prompt) },
                Temperature = 0.7f,
                MaxTokens = 800
            };
            
            // Add tool definitions
            foreach (var tool in allowedTools)
            {
                completionOptions.Tools.Add(new ChatCompletionsFunctionToolDefinition
                {
                    Name = tool,
                    // In a real implementation, you'd add the tool schema here
                });
            }
            
            // Get completion response
            var response = await client.GetChatCompletionsAsync(completionOptions);
            
            // Handle tool calls in the response
            foreach (var toolCall in response.Value.Choices[0].Message.ToolCalls)
            {
                // Implementation to handle Azure OpenAI tool calls with MCP
                // ...
            }
            
            return response.Value.Choices[0].Message.Content;
        }
    }
}
```

En el código anterior hemos:

- Configurado el cliente de Azure OpenAI con el endpoint, nombre de implementación y clave de API.
- Creado un método `GetCompletionWithToolsAsync` para obtener completaciones con soporte de herramientas.
- Gestionado las llamadas a herramientas en la respuesta.

Se recomienda implementar la lógica real de manejo de herramientas según la configuración específica de tu servidor MCP.

## Integración con Microsoft AI Foundry

Azure AI Foundry proporciona una plataforma para construir y desplegar agentes de IA. Integrar MCP con AI Foundry te permite aprovechar sus capacidades mientras mantienes la flexibilidad de MCP.

En el siguiente código, desarrollamos una integración de agentes que procesa solicitudes y gestiona llamadas a herramientas utilizando MCP.

### Implementación en Java

```java
// Java AI Foundry Agent Integration
package com.example.mcp.enterprise;

import com.microsoft.aifoundry.AgentClient;
import com.microsoft.aifoundry.AgentToolResponse;
import com.microsoft.aifoundry.models.AgentRequest;
import com.microsoft.aifoundry.models.AgentResponse;
import com.mcp.client.McpClient;
import com.mcp.tools.ToolRequest;
import com.mcp.tools.ToolResponse;

public class AIFoundryMcpBridge {
    private final AgentClient agentClient;
    private final McpClient mcpClient;
    
    public AIFoundryMcpBridge(String aiFoundryEndpoint, String mcpServerUrl) {
        this.agentClient = new AgentClient(aiFoundryEndpoint);
        this.mcpClient = new McpClient.Builder()
            .setServerUrl(mcpServerUrl)
            .build();
    }
    
    public AgentResponse processAgentRequest(AgentRequest request) {
        // Process the AI Foundry Agent request
        AgentResponse initialResponse = agentClient.processRequest(request);
        
        // Check if the agent requested to use tools
        if (initialResponse.getToolCalls() != null && !initialResponse.getToolCalls().isEmpty()) {
            // For each tool call, route it to the appropriate MCP tool
            for (AgentToolCall toolCall : initialResponse.getToolCalls()) {
                String toolName = toolCall.getName();
                Map<String, Object> parameters = toolCall.getArguments();
                
                // Execute the tool using MCP
                ToolResponse mcpResponse = mcpClient.executeTool(toolName, parameters);
                
                // Create tool response for AI Foundry
                AgentToolResponse toolResponse = new AgentToolResponse(
                    toolCall.getId(),
                    mcpResponse.getResult()
                );
                
                // Submit tool response back to the agent
                initialResponse = agentClient.submitToolResponse(
                    request.getConversationId(), 
                    toolResponse
                );
            }
        }
        
        return initialResponse;
    }
}
```

En el código anterior hemos:

- Creado una clase `AIFoundryMcpBridge` que se integra tanto con AI Foundry como con MCP.
- Implementado un método `processAgentRequest` que procesa una solicitud de agente de AI Foundry.
- Gestionado las llamadas a herramientas ejecutándolas a través del cliente MCP y enviando los resultados de vuelta al agente de AI Foundry.

## Integración de MCP con Azure ML

Integrar MCP con Azure Machine Learning (ML) te permite aprovechar las potentes capacidades de ML de Azure mientras mantienes la flexibilidad de MCP. Esta integración puede utilizarse para ejecutar pipelines de ML, registrar modelos como herramientas y gestionar recursos de cómputo.

### Implementación en Python

```python
# Python Azure AI Integration
from mcp_client import McpClient
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment, AmlCompute
import os
import asyncio

class EnterpriseAiIntegration:
    def __init__(self, mcp_server_url, subscription_id, resource_group, workspace_name):
        # Set up MCP client
        self.mcp_client = McpClient(server_url=mcp_server_url)
        
        # Set up Azure ML client
        self.credential = DefaultAzureCredential()
        self.ml_client = MLClient(
            self.credential,
            subscription_id,
            resource_group,
            workspace_name
        )
    
    async def execute_ml_pipeline(self, pipeline_name, input_data):
        """Executes an ML pipeline in Azure ML"""
        # First process the input data using MCP tools
        processed_data = await self.mcp_client.execute_tool(
            "dataPreprocessor",
            {
                "data": input_data,
                "operations": ["normalize", "clean", "transform"]
            }
        )
        
        # Submit the pipeline to Azure ML
        pipeline_job = self.ml_client.jobs.create_or_update(
            entity={
                "name": pipeline_name,
                "display_name": f"MCP-triggered {pipeline_name}",
                "experiment_name": "mcp-integration",
                "inputs": {
                    "processed_data": processed_data.result
                }
            }
        )
        
        # Return job information
        return {
            "job_id": pipeline_job.id,
            "status": pipeline_job.status,
            "creation_time": pipeline_job.creation_context.created_at
        }
    
    async def register_ml_model_as_tool(self, model_name, model_version="latest"):
        """Registers an Azure ML model as an MCP tool"""
        # Get model details
        if model_version == "latest":
            model = self.ml_client.models.get(name=model_name, label="latest")
        else:
            model = self.ml_client.models.get(name=model_name, version=model_version)
        
        # Create deployment environment
        env = Environment(
            name="mcp-model-env",
            conda_file="./environments/inference-env.yml"
        )
        
        # Set up compute
        compute = self.ml_client.compute.get("mcp-inference")
        
        # Deploy model as online endpoint
        deployment = self.ml_client.online_deployments.create_or_update(
            endpoint_name=f"mcp-{model_name}",
            deployment={
                "name": f"mcp-{model_name}-deployment",
                "model": model.id,
                "environment": env,
                "compute": compute,
                "scale_settings": {
                    "scale_type": "auto",
                    "min_instances": 1,
                    "max_instances": 3
                }
            }
        )
        
        # Create MCP tool schema based on model schema
        tool_schema = {
            "type": "object",
            "properties": {},
            "required": []
        }
        
        # Add input properties based on model schema
        for input_name, input_spec in model.signature.inputs.items():
            tool_schema["properties"][input_name] = {
                "type": self._map_ml_type_to_json_type(input_spec.type)
            }
            tool_schema["required"].append(input_name)
        
        # Register as MCP tool
        # In a real implementation, you would create a tool that calls the endpoint
        return {
            "model_name": model_name,
            "model_version": model.version,
            "endpoint": deployment.endpoint_uri,
            "tool_schema": tool_schema
        }
    
    def _map_ml_type_to_json_type(self, ml_type):
        """Maps ML data types to JSON schema types"""
        mapping = {
            "float": "number",
            "int": "integer",
            "bool": "boolean",
            "str": "string",
            "object": "object",
            "array": "array"
        }
        return mapping.get(ml_type, "string")
```

En el código anterior hemos:

- Creado una clase `EnterpriseAiIntegration` que integra MCP con Azure ML.
- Implementado un método `execute_ml_pipeline` que procesa datos de entrada utilizando herramientas MCP y envía un pipeline de ML a Azure ML.
- Implementado un método `register_ml_model_as_tool` que registra un modelo de Azure ML como una herramienta MCP, incluyendo la creación del entorno de despliegue necesario y los recursos de cómputo.
- Mapeado tipos de datos de Azure ML a tipos de esquema JSON para el registro de herramientas.
- Utilizado programación asincrónica para manejar operaciones potencialmente largas como la ejecución de pipelines de ML y el registro de modelos.

## ¿Qué sigue?

- [5.2 Multi modalidad](../mcp-multi-modality/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.