# Intégration en entreprise

Lors de la création de serveurs MCP dans un contexte d'entreprise, il est souvent nécessaire de s'intégrer à des plateformes et services d'IA existants. Cette section explique comment intégrer MCP avec des systèmes d'entreprise tels qu'Azure OpenAI et Microsoft AI Foundry, permettant ainsi des capacités avancées d'IA et une orchestration d'outils.

## Introduction

Dans cette leçon, vous apprendrez à intégrer le Model Context Protocol (MCP) avec des systèmes d'IA d'entreprise, en mettant l'accent sur Azure OpenAI et Microsoft AI Foundry. Ces intégrations vous permettent de tirer parti de modèles et outils d'IA puissants tout en conservant la flexibilité et l'extensibilité de MCP.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Intégrer MCP avec Azure OpenAI pour exploiter ses capacités d'IA.
- Implémenter l'orchestration d'outils MCP avec Azure OpenAI.
- Combiner MCP avec Microsoft AI Foundry pour des capacités avancées d'agents d'IA.
- Exploiter Azure Machine Learning (ML) pour exécuter des pipelines ML et enregistrer des modèles en tant qu'outils MCP.

## Intégration avec Azure OpenAI

Azure OpenAI offre un accès à des modèles d'IA puissants comme GPT-4 et d'autres. Intégrer MCP avec Azure OpenAI vous permet d'utiliser ces modèles tout en conservant la flexibilité de l'orchestration d'outils de MCP.

### Implémentation en C#

Dans cet extrait de code, nous montrons comment intégrer MCP avec Azure OpenAI en utilisant le SDK Azure OpenAI.

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

Dans le code précédent, nous avons :

- Configuré le client Azure OpenAI avec l'endpoint, le nom du déploiement et la clé API.
- Créé une méthode `GetCompletionWithToolsAsync` pour obtenir des complétions avec prise en charge des outils.
- Géré les appels d'outils dans la réponse.

Nous vous encourageons à implémenter la logique réelle de gestion des outils en fonction de la configuration spécifique de votre serveur MCP.

## Intégration avec Microsoft AI Foundry

Azure AI Foundry fournit une plateforme pour créer et déployer des agents d'IA. Intégrer MCP avec AI Foundry vous permet de tirer parti de ses capacités tout en conservant la flexibilité de MCP.

Dans le code ci-dessous, nous développons une intégration d'agent qui traite les requêtes et gère les appels d'outils en utilisant MCP.

### Implémentation en Java

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

Dans le code précédent, nous avons :

- Créé une classe `AIFoundryMcpBridge` qui s'intègre à la fois avec AI Foundry et MCP.
- Implémenté une méthode `processAgentRequest` qui traite une requête d'agent AI Foundry.
- Géré les appels d'outils en les exécutant via le client MCP et en soumettant les résultats à l'agent AI Foundry.

## Intégration de MCP avec Azure ML

Intégrer MCP avec Azure Machine Learning (ML) vous permet de tirer parti des puissantes capacités de ML d'Azure tout en conservant la flexibilité de MCP. Cette intégration peut être utilisée pour exécuter des pipelines ML, enregistrer des modèles en tant qu'outils et gérer les ressources de calcul.

### Implémentation en Python

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

Dans le code précédent, nous avons :

- Créé une classe `EnterpriseAiIntegration` qui intègre MCP avec Azure ML.
- Implémenté une méthode `execute_ml_pipeline` qui traite les données d'entrée à l'aide des outils MCP et soumet un pipeline ML à Azure ML.
- Implémenté une méthode `register_ml_model_as_tool` qui enregistre un modèle Azure ML en tant qu'outil MCP, y compris la création de l'environnement de déploiement et des ressources de calcul nécessaires.
- Mappé les types de données Azure ML aux types de schéma JSON pour l'enregistrement des outils.
- Utilisé la programmation asynchrone pour gérer des opérations potentiellement longues comme l'exécution de pipelines ML et l'enregistrement de modèles.

## Et après

- [5.2 Multi modalité](../mcp-multi-modality/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.