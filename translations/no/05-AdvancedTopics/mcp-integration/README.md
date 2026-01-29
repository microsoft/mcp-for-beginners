# Bedriftsintegrasjon

Når du bygger MCP-servere i en bedriftskontekst, må du ofte integrere med eksisterende AI-plattformer og -tjenester. Denne seksjonen dekker hvordan du kan integrere MCP med bedriftsystemer som Azure OpenAI og Microsoft AI Foundry, og dermed muliggjøre avanserte AI-funksjoner og verktøyorkestrering.

## Introduksjon

I denne leksjonen vil du lære hvordan du integrerer Model Context Protocol (MCP) med bedrifts-AI-systemer, med fokus på Azure OpenAI og Microsoft AI Foundry. Disse integrasjonene lar deg utnytte kraftige AI-modeller og verktøy samtidig som du opprettholder fleksibiliteten og utvidbarheten til MCP.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Integrere MCP med Azure OpenAI for å utnytte dets AI-funksjoner.
- Implementere MCP-verktøyorkestrering med Azure OpenAI.
- Kombinere MCP med Microsoft AI Foundry for avanserte AI-agentfunksjoner.
- Utnytte Azure Machine Learning (ML) for å kjøre ML-pipelines og registrere modeller som MCP-verktøy.

## Azure OpenAI-integrasjon

Azure OpenAI gir tilgang til kraftige AI-modeller som GPT-4 og andre. Ved å integrere MCP med Azure OpenAI kan du utnytte disse modellene samtidig som du opprettholder fleksibiliteten til MCPs verktøyorkestrering.

### C#-implementasjon

I denne kodeeksempelet viser vi hvordan du integrerer MCP med Azure OpenAI ved hjelp av Azure OpenAI SDK.

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

I koden ovenfor har vi:

- Konfigurert Azure OpenAI-klienten med endepunkt, distribusjonsnavn og API-nøkkel.
- Opprettet en metode `GetCompletionWithToolsAsync` for å hente fullføringer med verktøystøtte.
- Håndtert verktøykall i responsen.

Du oppfordres til å implementere den faktiske logikken for verktøyhåndtering basert på din spesifikke MCP-serveroppsett.

## Microsoft AI Foundry-integrasjon

Azure AI Foundry gir en plattform for å bygge og distribuere AI-agenter. Ved å integrere MCP med AI Foundry kan du utnytte dens funksjoner samtidig som du opprettholder fleksibiliteten til MCP.

I koden nedenfor utvikler vi en agentintegrasjon som behandler forespørsler og håndterer verktøykall ved hjelp av MCP.

### Java-implementasjon

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

I koden ovenfor har vi:

- Opprettet en `AIFoundryMcpBridge`-klasse som integrerer både AI Foundry og MCP.
- Implementert en metode `processAgentRequest` som behandler en AI Foundry-agentforespørsel.
- Håndtert verktøykall ved å utføre dem gjennom MCP-klienten og sende resultatene tilbake til AI Foundry-agenten.

## Integrering av MCP med Azure ML

Ved å integrere MCP med Azure Machine Learning (ML) kan du utnytte Azures kraftige ML-funksjoner samtidig som du opprettholder fleksibiliteten til MCP. Denne integrasjonen kan brukes til å kjøre ML-pipelines, registrere modeller som verktøy og administrere databehandlingsressurser.

### Python-implementasjon

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

I koden ovenfor har vi:

- Opprettet en `EnterpriseAiIntegration`-klasse som integrerer MCP med Azure ML.
- Implementert en `execute_ml_pipeline`-metode som behandler inndata ved hjelp av MCP-verktøy og sender en ML-pipeline til Azure ML.
- Implementert en `register_ml_model_as_tool`-metode som registrerer en Azure ML-modell som et MCP-verktøy, inkludert opprettelse av nødvendig distribusjonsmiljø og databehandlingsressurser.
- Kartlagt Azure ML-datatyper til JSON-skjema-typer for verktøyregistrering.
- Brukt asynkron programmering for å håndtere potensielt langvarige operasjoner som ML-pipelinekjøring og modellregistrering.

## Hva nå

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.