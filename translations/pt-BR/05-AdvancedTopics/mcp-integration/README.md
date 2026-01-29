# Integração Empresarial

Ao construir servidores MCP em um contexto empresarial, muitas vezes é necessário integrar com plataformas e serviços de IA já existentes. Esta seção aborda como integrar o MCP com sistemas empresariais como Azure OpenAI e Microsoft AI Foundry, permitindo capacidades avançadas de IA e orquestração de ferramentas.

## Introdução

Nesta lição, você aprenderá como integrar o Model Context Protocol (MCP) com sistemas de IA empresariais, com foco no Azure OpenAI e no Microsoft AI Foundry. Essas integrações permitem aproveitar modelos e ferramentas de IA poderosos, mantendo a flexibilidade e extensibilidade do MCP.

## Objetivos de Aprendizado

Ao final desta lição, você será capaz de:

- Integrar o MCP com o Azure OpenAI para utilizar suas capacidades de IA.
- Implementar a orquestração de ferramentas do MCP com o Azure OpenAI.
- Combinar o MCP com o Microsoft AI Foundry para capacidades avançadas de agentes de IA.
- Utilizar o Azure Machine Learning (ML) para executar pipelines de ML e registrar modelos como ferramentas do MCP.

## Integração com Azure OpenAI

O Azure OpenAI fornece acesso a modelos de IA poderosos como o GPT-4 e outros. Integrar o MCP com o Azure OpenAI permite utilizar esses modelos enquanto mantém a flexibilidade da orquestração de ferramentas do MCP.

### Implementação em C#

Neste trecho de código, demonstramos como integrar o MCP com o Azure OpenAI usando o SDK do Azure OpenAI.

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

No código acima, nós:

- Configuramos o cliente do Azure OpenAI com o endpoint, nome da implantação e chave de API.
- Criamos um método `GetCompletionWithToolsAsync` para obter respostas com suporte a ferramentas.
- Lidamos com chamadas de ferramentas na resposta.

Recomenda-se implementar a lógica real de manipulação de ferramentas com base na configuração específica do seu servidor MCP.

## Integração com Microsoft AI Foundry

O Azure AI Foundry fornece uma plataforma para construir e implantar agentes de IA. Integrar o MCP com o AI Foundry permite aproveitar suas capacidades enquanto mantém a flexibilidade do MCP.

No código abaixo, desenvolvemos uma integração de agente que processa solicitações e lida com chamadas de ferramentas usando o MCP.

### Implementação em Java

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

No código acima, nós:

- Criamos uma classe `AIFoundryMcpBridge` que integra tanto com o AI Foundry quanto com o MCP.
- Implementamos um método `processAgentRequest` que processa uma solicitação de agente do AI Foundry.
- Lidamos com chamadas de ferramentas executando-as através do cliente MCP e enviando os resultados de volta ao agente do AI Foundry.

## Integração do MCP com Azure ML

Integrar o MCP com o Azure Machine Learning (ML) permite aproveitar as poderosas capacidades de ML do Azure enquanto mantém a flexibilidade do MCP. Essa integração pode ser usada para executar pipelines de ML, registrar modelos como ferramentas e gerenciar recursos computacionais.

### Implementação em Python

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

No código acima, nós:

- Criamos uma classe `EnterpriseAiIntegration` que integra o MCP com o Azure ML.
- Implementamos um método `execute_ml_pipeline` que processa dados de entrada usando ferramentas do MCP e submete um pipeline de ML ao Azure ML.
- Implementamos um método `register_ml_model_as_tool` que registra um modelo do Azure ML como uma ferramenta do MCP, incluindo a criação do ambiente de implantação necessário e recursos computacionais.
- Mapeamos tipos de dados do Azure ML para tipos de esquema JSON para o registro de ferramentas.
- Utilizamos programação assíncrona para lidar com operações potencialmente demoradas, como a execução de pipelines de ML e o registro de modelos.

## O que vem a seguir

- [5.2 Multi modalidade](../mcp-multi-modality/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.