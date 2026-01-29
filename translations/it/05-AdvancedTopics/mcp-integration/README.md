# Integrazione Aziendale

Quando si costruiscono server MCP in un contesto aziendale, spesso è necessario integrarli con piattaforme e servizi di intelligenza artificiale esistenti. Questa sezione spiega come integrare MCP con sistemi aziendali come Azure OpenAI e Microsoft AI Foundry, abilitando funzionalità avanzate di intelligenza artificiale e orchestrazione degli strumenti.

## Introduzione

In questa lezione, imparerai come integrare il Model Context Protocol (MCP) con sistemi di intelligenza artificiale aziendali, concentrandoti su Azure OpenAI e Microsoft AI Foundry. Queste integrazioni ti permettono di sfruttare potenti modelli e strumenti di intelligenza artificiale mantenendo la flessibilità e l'estensibilità di MCP.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Integrare MCP con Azure OpenAI per sfruttare le sue capacità di intelligenza artificiale.
- Implementare l'orchestrazione degli strumenti MCP con Azure OpenAI.
- Combinare MCP con Microsoft AI Foundry per funzionalità avanzate di agenti di intelligenza artificiale.
- Utilizzare Azure Machine Learning (ML) per eseguire pipeline di ML e registrare modelli come strumenti MCP.

## Integrazione con Azure OpenAI

Azure OpenAI fornisce accesso a potenti modelli di intelligenza artificiale come GPT-4 e altri. Integrare MCP con Azure OpenAI ti consente di utilizzare questi modelli mantenendo la flessibilità dell'orchestrazione degli strumenti di MCP.

### Implementazione in C#

In questo esempio di codice, mostriamo come integrare MCP con Azure OpenAI utilizzando l'SDK di Azure OpenAI.

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

Nel codice precedente abbiamo:

- Configurato il client Azure OpenAI con l'endpoint, il nome della distribuzione e la chiave API.
- Creato un metodo `GetCompletionWithToolsAsync` per ottenere completamenti con supporto per gli strumenti.
- Gestito le chiamate agli strumenti nella risposta.

Ti invitiamo a implementare la logica effettiva di gestione degli strumenti in base alla configurazione specifica del tuo server MCP.

## Integrazione con Microsoft AI Foundry

Azure AI Foundry offre una piattaforma per costruire e distribuire agenti di intelligenza artificiale. Integrare MCP con AI Foundry ti consente di sfruttare le sue capacità mantenendo la flessibilità di MCP.

Nel codice seguente, sviluppiamo un'integrazione con un agente che elabora richieste e gestisce chiamate agli strumenti utilizzando MCP.

### Implementazione in Java

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

Nel codice precedente abbiamo:

- Creato una classe `AIFoundryMcpBridge` che si integra sia con AI Foundry che con MCP.
- Implementato un metodo `processAgentRequest` che elabora una richiesta di un agente AI Foundry.
- Gestito le chiamate agli strumenti eseguendole tramite il client MCP e inviando i risultati all'agente AI Foundry.

## Integrazione di MCP con Azure ML

Integrare MCP con Azure Machine Learning (ML) ti consente di sfruttare le potenti capacità di ML di Azure mantenendo la flessibilità di MCP. Questa integrazione può essere utilizzata per eseguire pipeline di ML, registrare modelli come strumenti e gestire risorse di calcolo.

### Implementazione in Python

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

Nel codice precedente abbiamo:

- Creato una classe `EnterpriseAiIntegration` che integra MCP con Azure ML.
- Implementato un metodo `execute_ml_pipeline` che elabora i dati di input utilizzando strumenti MCP e invia una pipeline di ML ad Azure ML.
- Implementato un metodo `register_ml_model_as_tool` che registra un modello di Azure ML come strumento MCP, inclusa la creazione dell'ambiente di distribuzione e delle risorse di calcolo necessarie.
- Mappato i tipi di dati di Azure ML ai tipi di schema JSON per la registrazione degli strumenti.
- Utilizzato la programmazione asincrona per gestire operazioni potenzialmente lunghe come l'esecuzione di pipeline di ML e la registrazione dei modelli.

## Cosa fare dopo

- [5.2 Multi modalità](../mcp-multi-modality/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.