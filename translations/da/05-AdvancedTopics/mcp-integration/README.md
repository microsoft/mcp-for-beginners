# Enterprise Integration

Når du bygger MCP-servere i en virksomhedskontekst, er det ofte nødvendigt at integrere med eksisterende AI-platforme og -tjenester. Denne sektion dækker, hvordan MCP kan integreres med virksomhedssystemer som Azure OpenAI og Microsoft AI Foundry, hvilket muliggør avancerede AI-funktioner og værktøjsorkestrering.

## Introduktion

I denne lektion lærer du, hvordan du integrerer Model Context Protocol (MCP) med virksomhedens AI-systemer, med fokus på Azure OpenAI og Microsoft AI Foundry. Disse integrationer giver dig mulighed for at udnytte kraftfulde AI-modeller og værktøjer, samtidig med at du bevarer MCP's fleksibilitet og udvidelsesmuligheder.

## Læringsmål

Ved afslutningen af denne lektion vil du kunne:

- Integrere MCP med Azure OpenAI for at udnytte dets AI-funktioner.
- Implementere MCP-værktøjsorkestrering med Azure OpenAI.
- Kombinere MCP med Microsoft AI Foundry for avancerede AI-agentfunktioner.
- Udnytte Azure Machine Learning (ML) til at udføre ML-pipelines og registrere modeller som MCP-værktøjer.

## Azure OpenAI Integration

Azure OpenAI giver adgang til kraftfulde AI-modeller som GPT-4 og andre. Integration af MCP med Azure OpenAI gør det muligt at udnytte disse modeller, samtidig med at MCP's værktøjsorkestrering bevares.

### C# Implementering

I denne kodeeksempel demonstrerer vi, hvordan MCP kan integreres med Azure OpenAI ved hjælp af Azure OpenAI SDK.

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

I den foregående kode har vi:

- Konfigureret Azure OpenAI-klienten med endpoint, deployment-navn og API-nøgle.
- Oprettet en metode `GetCompletionWithToolsAsync` til at hente completions med værktøjsunderstøttelse.
- Håndteret værktøjskald i svaret.

Du opfordres til at implementere den faktiske logik for værktøjshåndtering baseret på din specifikke MCP-serveropsætning.

## Microsoft AI Foundry Integration

Azure AI Foundry tilbyder en platform til opbygning og implementering af AI-agenter. Integration af MCP med AI Foundry gør det muligt at udnytte dens funktioner, samtidig med at MCP's fleksibilitet bevares.

I nedenstående kode udvikler vi en agentintegration, der behandler forespørgsler og håndterer værktøjskald ved hjælp af MCP.

### Java Implementering

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

I den foregående kode har vi:

- Oprettet en `AIFoundryMcpBridge`-klasse, der integrerer med både AI Foundry og MCP.
- Implementeret en metode `processAgentRequest`, der behandler en AI Foundry-agentforespørgsel.
- Håndteret værktøjskald ved at udføre dem via MCP-klienten og sende resultaterne tilbage til AI Foundry-agenten.

## Integration af MCP med Azure ML

Integration af MCP med Azure Machine Learning (ML) gør det muligt at udnytte Azures kraftfulde ML-funktioner, samtidig med at MCP's fleksibilitet bevares. Denne integration kan bruges til at udføre ML-pipelines, registrere modeller som værktøjer og administrere computressourcer.

### Python Implementering

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

I den foregående kode har vi:

- Oprettet en `EnterpriseAiIntegration`-klasse, der integrerer MCP med Azure ML.
- Implementeret en `execute_ml_pipeline`-metode, der behandler inputdata ved hjælp af MCP-værktøjer og sender en ML-pipeline til Azure ML.
- Implementeret en `register_ml_model_as_tool`-metode, der registrerer en Azure ML-model som et MCP-værktøj, herunder oprettelse af det nødvendige implementeringsmiljø og computressourcer.
- Kortlagt Azure ML-datatyper til JSON-schema-typer for værktøjsregistrering.
- Brugte asynkron programmering til at håndtere potentielt langvarige operationer som ML-pipeline-udførelse og modelregistrering.

## Hvad er næste skridt

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.