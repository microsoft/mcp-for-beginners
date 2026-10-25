# Ettevõtte integratsioon

Kui ehitate MCP-servereid ettevõtte kontekstis, peate sageli integreerima olemasolevate tehisintellekti platvormide ja teenustega. See jaotis selgitab, kuidas integreerida MCP ettevõttesüsteemidega nagu Azure OpenAI ja Microsoft AI Foundry, võimaldades arenenud tehisintellekti võimekust ja tööriistade orkestreerimist.

## Sissejuhatus

Selles õppetükis õpite, kuidas integreerida Model Context Protocoli (MCP) ettevõtte tehisintellekti süsteemidega, keskendudes Azure OpenAI-le ja Microsoft AI Foundry'le. Need integratsioonid võimaldavad teil kasutada võimsaid tehisintellekti mudeleid ja tööriistu, säilitades samal ajal MCP paindlikkuse ja laiendatavuse.

## Õpieesmärgid

Selle õppetüki lõpuks suudate:

- Integreerida MCP Azure OpenAI-ga, et kasutada selle tehisintellekti võimekust.
- Rakendada MCP tööriistade orkestreerimist Azure OpenAI abil.
- Ühendada MCP Microsoft AI Foundry'ga, et saada arenenud AI-agendi võimekust.
- Kasutada Azure Machine Learningut (ML) ML-töövoogude täitmiseks ja mudelite registreerimiseks MCP-tööriistadena.

## Azure OpenAI integreerimine

Microsoft Foundry pakub juurdepääsu ajakohastele AI-mudelitele, nagu GPT-5.1.
MCP integreerimine Foundry mudelitega säilitab MCP tööriistade
orkestreerimise paindlikkuse, kasutades hallatud mudeli juurutust.

### C# rakendus

Selles koodilõigus demonstreerime, kuidas integreerida MCP Azure OpenAI-ga, kasutades Azure OpenAI SDK-d.

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

Eelnevas koodis oleme:

- Konfigureerinud Azure OpenAI kliendi lõpp-punkti, juurutuse nime ja API-võtmega.
- Loodud meetod `GetCompletionWithToolsAsync` täidiste saamiseks tööriistatoega.
- Käsitles tööriistakõnesid vastuses.

Soovitame teil rakendada tegeliku tööriistakäsitluse loogika vastavalt teie konkreetsele MCP-serveri seadistusele.

## Microsoft Foundry integreerimine

Microsoft Foundry pakub platvormi AI-agentide ehitamiseks ja juurutamiseks. MCP integreerimine Microsoft Foundry'ga võimaldab teil kasutada selle võimekust, säilitades samal ajal MCP paindlikkuse.

Alljärgnevas koodis töötame välja Agendi integratsiooni, mis töötleb päringuid ja käsitleb tööriistakõnesid MCP abil.

### Java implementatsioon

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

Eelnevas koodis oleme:

- Loodud klass `AIFoundryMcpBridge`, mis integreerub nii AI Foundry'ga kui ka MCP-ga.
- Rakendatud meetod `processAgentRequest`, mis töötleb AI Foundry agendi päringut.
- Käsitles tööriistakõnesid, käivitades need MCP-kliendi kaudu ja edastades tulemused tagasi AI Foundry agendile.

## MCP integreerimine Azure ML-iga

MCP integreerimine Azure Machine Learningu (ML) võimaldab teil kasutada Azure'i võimsaid ML-võimekusi, säilitades samal ajal MCP paindlikkuse. Seda integratsiooni saab kasutada ML-töövoogude täitmiseks, mudelite registreerimiseks tööriistadena ning arvutusressursside haldamiseks.

### Python implementatsioon

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

Eelnevas koodis oleme:

- Loodud klass `EnterpriseAiIntegration`, mis integreerib MCP-i Azure ML-iga.
- Rakendatud meetod `execute_ml_pipeline`, mis töötleb sisendandmeid MCP-tööriistade abil ja esitab ML-töövoo Azure ML-ile.
- Rakendatud meetod `register_ml_model_as_tool`, mis registreerib Azure ML-mudeli MCP-tööriistana, sealhulgas loob vajaliku juurutuskeskkonna ja arvutusressursid.
- Kaardistatud Azure ML andmetüübid JSON-skeemi tüüpidega tööriistade registreerimiseks.
- Kasutatud asünkroonset programmeerimist, et toime tulla potentsiaalselt pikaajaliste operatsioonidega, nagu ML-töövoogude täitmine ja mudelite registreerimine.

## Mis järgmiseks

- [5.2 Mitmemodaalsus](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->