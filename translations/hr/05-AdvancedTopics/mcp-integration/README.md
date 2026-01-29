# Integracija u poduzeću

Prilikom izgradnje MCP poslužitelja u kontekstu poduzeća, često je potrebno integrirati se s postojećim AI platformama i uslugama. Ovaj odjeljak objašnjava kako integrirati MCP s poslovnim sustavima poput Azure OpenAI i Microsoft AI Foundry, omogućujući napredne AI mogućnosti i orkestraciju alata.

## Uvod

U ovoj lekciji naučit ćete kako integrirati Model Context Protocol (MCP) s poslovnim AI sustavima, s naglaskom na Azure OpenAI i Microsoft AI Foundry. Ove integracije omogućuju vam korištenje moćnih AI modela i alata uz zadržavanje fleksibilnosti i proširivosti MCP-a.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Integrirati MCP s Azure OpenAI kako biste iskoristili njegove AI mogućnosti.
- Implementirati orkestraciju alata MCP-a s Azure OpenAI.
- Kombinirati MCP s Microsoft AI Foundry za napredne mogućnosti AI agenata.
- Iskoristiti Azure Machine Learning (ML) za izvršavanje ML cjevovoda i registraciju modela kao MCP alata.

## Integracija s Azure OpenAI

Azure OpenAI omogućuje pristup moćnim AI modelima poput GPT-4 i drugih. Integracija MCP-a s Azure OpenAI omogućuje vam korištenje ovih modela uz zadržavanje fleksibilnosti MCP-ove orkestracije alata.

### Implementacija u C#

U ovom primjeru koda prikazujemo kako integrirati MCP s Azure OpenAI koristeći Azure OpenAI SDK.

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

U prethodnom kodu smo:

- Konfigurirali Azure OpenAI klijent s krajnjom točkom, nazivom implementacije i API ključem.
- Kreirali metodu `GetCompletionWithToolsAsync` za dobivanje odgovora s podrškom za alate.
- Obradili pozive alata u odgovoru.

Preporučuje se implementirati stvarnu logiku obrade alata na temelju specifične konfiguracije vašeg MCP poslužitelja.

## Integracija s Microsoft AI Foundry

Azure AI Foundry pruža platformu za izgradnju i implementaciju AI agenata. Integracija MCP-a s AI Foundry omogućuje vam iskorištavanje njegovih mogućnosti uz zadržavanje fleksibilnosti MCP-a.

U donjem primjeru koda razvijamo integraciju agenta koja obrađuje zahtjeve i upravlja pozivima alata koristeći MCP.

### Implementacija u Javi

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

U prethodnom kodu smo:

- Kreirali klasu `AIFoundryMcpBridge` koja integrira AI Foundry i MCP.
- Implementirali metodu `processAgentRequest` koja obrađuje zahtjev AI Foundry agenta.
- Obradili pozive alata izvršavajući ih putem MCP klijenta i vraćajući rezultate natrag AI Foundry agentu.

## Integracija MCP-a s Azure ML

Integracija MCP-a s Azure Machine Learning (ML) omogućuje vam iskorištavanje moćnih ML mogućnosti Azure-a uz zadržavanje fleksibilnosti MCP-a. Ova integracija može se koristiti za izvršavanje ML cjevovoda, registraciju modela kao alata i upravljanje računalnim resursima.

### Implementacija u Pythonu

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

U prethodnom kodu smo:

- Kreirali klasu `EnterpriseAiIntegration` koja integrira MCP s Azure ML.
- Implementirali metodu `execute_ml_pipeline` koja obrađuje ulazne podatke koristeći MCP alate i predaje ML cjevovod Azure ML-u.
- Implementirali metodu `register_ml_model_as_tool` koja registrira Azure ML model kao MCP alat, uključujući stvaranje potrebnog okruženja za implementaciju i računalnih resursa.
- Mapirali Azure ML tipove podataka na JSON sheme za registraciju alata.
- Koristili asinhrono programiranje za obradu potencijalno dugotrajnih operacija poput izvršavanja ML cjevovoda i registracije modela.

## Što dalje

- [5.2 Višestruka modalnost](../mcp-multi-modality/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.