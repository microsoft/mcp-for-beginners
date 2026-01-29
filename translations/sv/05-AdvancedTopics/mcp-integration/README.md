# Företagsintegration

När du bygger MCP-servrar i en företagskontext behöver du ofta integrera med befintliga AI-plattformar och tjänster. Den här sektionen täcker hur du integrerar MCP med företagssystem som Azure OpenAI och Microsoft AI Foundry, vilket möjliggör avancerade AI-funktioner och verktygsorkestrering.

## Introduktion

I denna lektion kommer du att lära dig hur du integrerar Model Context Protocol (MCP) med företags-AI-system, med fokus på Azure OpenAI och Microsoft AI Foundry. Dessa integrationer gör det möjligt att utnyttja kraftfulla AI-modeller och verktyg samtidigt som du behåller MCP:s flexibilitet och utbyggbarhet.

## Lärandemål

Efter denna lektion kommer du att kunna:

- Integrera MCP med Azure OpenAI för att utnyttja dess AI-funktioner.
- Implementera MCP-verktygsorkestrering med Azure OpenAI.
- Kombinera MCP med Microsoft AI Foundry för avancerade AI-agentfunktioner.
- Utnyttja Azure Machine Learning (ML) för att köra ML-pipelines och registrera modeller som MCP-verktyg.

## Azure OpenAI-integration

Azure OpenAI ger tillgång till kraftfulla AI-modeller som GPT-4 och andra. Genom att integrera MCP med Azure OpenAI kan du utnyttja dessa modeller samtidigt som du behåller MCP:s flexibilitet för verktygsorkestrering.

### C#-implementation

I detta kodexempel demonstrerar vi hur man integrerar MCP med Azure OpenAI med hjälp av Azure OpenAI SDK.

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

I den föregående koden har vi:

- Konfigurerat Azure OpenAI-klienten med slutpunkt, distributionsnamn och API-nyckel.
- Skapat en metod `GetCompletionWithToolsAsync` för att få svar med verktygsstöd.
- Hanterat verktygsanrop i svaret.

Du uppmuntras att implementera den faktiska logiken för verktygshantering baserat på din specifika MCP-serverkonfiguration.

## Microsoft AI Foundry-integration

Azure AI Foundry erbjuder en plattform för att bygga och distribuera AI-agenter. Genom att integrera MCP med AI Foundry kan du utnyttja dess funktioner samtidigt som du behåller MCP:s flexibilitet.

I koden nedan utvecklar vi en agentintegration som bearbetar förfrågningar och hanterar verktygsanrop med MCP.

### Java-implementation

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

I den föregående koden har vi:

- Skapat en klass `AIFoundryMcpBridge` som integrerar både AI Foundry och MCP.
- Implementerat en metod `processAgentRequest` som bearbetar en AI Foundry-agentförfrågan.
- Hanterat verktygsanrop genom att köra dem via MCP-klienten och skicka resultaten tillbaka till AI Foundry-agenten.

## Integrera MCP med Azure ML

Genom att integrera MCP med Azure Machine Learning (ML) kan du utnyttja Azures kraftfulla ML-funktioner samtidigt som du behåller MCP:s flexibilitet. Denna integration kan användas för att köra ML-pipelines, registrera modeller som verktyg och hantera beräkningsresurser.

### Python-implementation

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

I den föregående koden har vi:

- Skapat en klass `EnterpriseAiIntegration` som integrerar MCP med Azure ML.
- Implementerat en metod `execute_ml_pipeline` som bearbetar indata med MCP-verktyg och skickar en ML-pipeline till Azure ML.
- Implementerat en metod `register_ml_model_as_tool` som registrerar en Azure ML-modell som ett MCP-verktyg, inklusive att skapa den nödvändiga distributionsmiljön och beräkningsresurser.
- Mappat Azure ML-datatyper till JSON-schema-typer för verktygsregistrering.
- Använt asynkron programmering för att hantera potentiellt långvariga operationer som ML-pipelinekörning och modellregistrering.

## Vad händer härnäst

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.