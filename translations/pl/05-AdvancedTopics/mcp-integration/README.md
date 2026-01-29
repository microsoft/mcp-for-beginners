# Integracja w przedsiębiorstwie

Podczas tworzenia serwerów MCP w kontekście przedsiębiorstwa często konieczne jest zintegrowanie ich z istniejącymi platformami i usługami AI. W tej sekcji omówimy, jak zintegrować MCP z systemami przedsiębiorstwa, takimi jak Azure OpenAI i Microsoft AI Foundry, aby umożliwić zaawansowane możliwości AI oraz orkiestrację narzędzi.

## Wprowadzenie

W tej lekcji dowiesz się, jak zintegrować Model Context Protocol (MCP) z systemami AI w przedsiębiorstwie, koncentrując się na Azure OpenAI i Microsoft AI Foundry. Te integracje pozwalają wykorzystać potężne modele AI i narzędzia, jednocześnie zachowując elastyczność i rozszerzalność MCP.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zintegrować MCP z Azure OpenAI, aby korzystać z jego możliwości AI.
- Zaimplementować orkiestrację narzędzi MCP z Azure OpenAI.
- Połączyć MCP z Microsoft AI Foundry, aby uzyskać zaawansowane możliwości agentów AI.
- Wykorzystać Azure Machine Learning (ML) do uruchamiania potoków ML i rejestrowania modeli jako narzędzi MCP.

## Integracja z Azure OpenAI

Azure OpenAI zapewnia dostęp do potężnych modeli AI, takich jak GPT-4 i inne. Integracja MCP z Azure OpenAI pozwala korzystać z tych modeli, jednocześnie zachowując elastyczność orkiestracji narzędzi MCP.

### Implementacja w C#

W tym fragmencie kodu pokazujemy, jak zintegrować MCP z Azure OpenAI za pomocą Azure OpenAI SDK.

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

W powyższym kodzie:

- Skonfigurowaliśmy klienta Azure OpenAI z użyciem punktu końcowego, nazwy wdrożenia i klucza API.
- Utworzyliśmy metodę `GetCompletionWithToolsAsync`, aby uzyskać wyniki z obsługą narzędzi.
- Obsłużyliśmy wywołania narzędzi w odpowiedzi.

Zachęcamy do zaimplementowania rzeczywistej logiki obsługi narzędzi w oparciu o specyficzną konfigurację serwera MCP.

## Integracja z Microsoft AI Foundry

Azure AI Foundry oferuje platformę do tworzenia i wdrażania agentów AI. Integracja MCP z AI Foundry pozwala wykorzystać jej możliwości, jednocześnie zachowując elastyczność MCP.

W poniższym kodzie opracowujemy integrację agenta, który przetwarza żądania i obsługuje wywołania narzędzi za pomocą MCP.

### Implementacja w Javie

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

W powyższym kodzie:

- Utworzyliśmy klasę `AIFoundryMcpBridge`, która integruje się zarówno z AI Foundry, jak i MCP.
- Zaimplementowaliśmy metodę `processAgentRequest`, która przetwarza żądanie agenta AI Foundry.
- Obsłużyliśmy wywołania narzędzi, wykonując je za pomocą klienta MCP i przesyłając wyniki z powrotem do agenta AI Foundry.

## Integracja MCP z Azure ML

Integracja MCP z Azure Machine Learning (ML) pozwala wykorzystać potężne możliwości ML Azure, jednocześnie zachowując elastyczność MCP. Ta integracja może być używana do uruchamiania potoków ML, rejestrowania modeli jako narzędzi oraz zarządzania zasobami obliczeniowymi.

### Implementacja w Pythonie

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

W powyższym kodzie:

- Utworzyliśmy klasę `EnterpriseAiIntegration`, która integruje MCP z Azure ML.
- Zaimplementowaliśmy metodę `execute_ml_pipeline`, która przetwarza dane wejściowe za pomocą narzędzi MCP i przesyła potok ML do Azure ML.
- Zaimplementowaliśmy metodę `register_ml_model_as_tool`, która rejestruje model Azure ML jako narzędzie MCP, w tym tworzenie niezbędnego środowiska wdrożeniowego i zasobów obliczeniowych.
- Mapowaliśmy typy danych Azure ML na typy schematów JSON w celu rejestracji narzędzi.
- Wykorzystaliśmy programowanie asynchroniczne do obsługi potencjalnie długotrwałych operacji, takich jak uruchamianie potoków ML i rejestracja modeli.

## Co dalej

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.