# Ettevõtte integratsioon

MCP-serverite loomisel ettevõtte kontekstis on tihti vaja integreerida olemasolevate tehisintellekti platvormide ja teenustega. Selles jaotises käsitletakse, kuidas integreerida MCP ettevõtte süsteemidega, nagu Azure OpenAI ja Microsoft AI Foundry, et võimaldada täiustatud tehisintellekti võimekust ja tööriistade orkestreerimist.

## Sissejuhatus

Selles õppetükis õpid, kuidas integreerida Model Context Protocol (MCP) ettevõtte tehisintellekti süsteemidega, keskendudes Azure OpenAI-le ja Microsoft AI Foundry-le. Need integratsioonid võimaldavad kasutada võimsaid tehisintellekti mudeleid ja tööriistu, säilitades samal ajal MCP paindlikkuse ja laiendatavuse.

## Õppe-eesmärgid

Selle õppetüki lõpuks oskad:

- Integreerida MCP Azure OpenAI-ga, et kasutada selle tehisintellekti võimekust.
- Rakendada MCP tööriistade orkestreerimist Azure OpenAI-ga.
- Kombineerida MCP Microsoft AI Foundry-ga, et saavutada täiustatud tehisintellekti agentide võimekust.
- Kasutada Azure Machine Learningut (ML), et käivitada ML-torustikke ja registreerida mudeleid MCP tööriistadena.

## Azure OpenAI integratsioon

Azure OpenAI pakub juurdepääsu võimsatele tehisintellekti mudelitele, nagu GPT-4 ja teised. MCP integreerimine Azure OpenAI-ga võimaldab neid mudeleid kasutada, säilitades samal ajal MCP tööriistade orkestreerimise paindlikkuse.

### C#-i teostus

Järgmises koodinäites demonstreerime, kuidas integreerida MCP Azure OpenAI-ga, kasutades Azure OpenAI SDK-d.

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

Eeltoodud koodis oleme:

- Konfigureerinud Azure OpenAI kliendi, määrates lõpp-punkti, juurutusnime ja API-võtme.
- Loonud meetodi `GetCompletionWithToolsAsync`, et saada tulemusi koos tööriistade toega.
- Töötlenud vastuses olevaid tööriistakõnesid.

Soovitame sul rakendada tegelik tööriistade käsitlemise loogika vastavalt oma MCP serveri seadistusele.

## Microsoft AI Foundry integratsioon

Azure AI Foundry pakub platvormi tehisintellekti agentide loomiseks ja juurutamiseks. MCP integreerimine AI Foundry-ga võimaldab kasutada selle võimalusi, säilitades samal ajal MCP paindlikkuse.

Allolevas koodis arendame agendi integratsiooni, mis töötleb päringuid ja käsitleb tööriistakõnesid MCP abil.

### Java teostus

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

Eeltoodud koodis oleme:

- Loonud klassi `AIFoundryMcpBridge`, mis integreerib nii AI Foundry kui ka MCP.
- Rakendanud meetodi `processAgentRequest`, mis töötleb AI Foundry agendi päringut.
- Töötlenud tööriistakõnesid, täites need MCP kliendi kaudu ja edastades tulemused tagasi AI Foundry agendile.

## MCP integreerimine Azure ML-iga

MCP integreerimine Azure Machine Learninguga (ML) võimaldab kasutada Azure'i võimsaid ML-võimekusi, säilitades samal ajal MCP paindlikkuse. Seda integratsiooni saab kasutada ML-torustike käivitamiseks, mudelite registreerimiseks tööriistadena ja arvutusressursside haldamiseks.

### Python teostus

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

Eeltoodud koodis oleme:

- Loonud klassi `EnterpriseAiIntegration`, mis integreerib MCP Azure ML-iga.
- Rakendanud meetodi `execute_ml_pipeline`, mis töötleb sisendandmeid MCP tööriistade abil ja esitab ML-torustiku Azure ML-ile.
- Rakendanud meetodi `register_ml_model_as_tool`, mis registreerib Azure ML mudeli MCP tööriistana, sealhulgas vajaliku juurutuskeskkonna ja arvutusressursside loomise.
- Kaardistanud Azure ML andmetüübid JSON-skeemi tüüpideks tööriistade registreerimiseks.
- Kasutanud asünkroonset programmeerimist, et hallata potentsiaalselt pikaajalisi toiminguid, nagu ML-torustike käivitamine ja mudelite registreerimine.

## Mis edasi?

- [5.2 Mitmeliikmelisus](../mcp-multi-modality/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.