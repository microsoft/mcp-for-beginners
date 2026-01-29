# Įmonių integracija

Kuriant MCP serverius įmonių kontekste, dažnai reikia integruoti esamas AI platformas ir paslaugas. Šiame skyriuje aptariama, kaip integruoti MCP su įmonių sistemomis, tokiomis kaip Azure OpenAI ir Microsoft AI Foundry, siekiant įgalinti pažangias AI galimybes ir įrankių koordinavimą.

## Įvadas

Šioje pamokoje sužinosite, kaip integruoti Model Context Protocol (MCP) su įmonių AI sistemomis, daugiausia dėmesio skiriant Azure OpenAI ir Microsoft AI Foundry. Šios integracijos leidžia pasinaudoti galingais AI modeliais ir įrankiais, išlaikant MCP lankstumą ir pritaikomumą.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Integruoti MCP su Azure OpenAI, kad galėtumėte naudotis jo AI galimybėmis.
- Įgyvendinti MCP įrankių koordinavimą su Azure OpenAI.
- Derinti MCP su Microsoft AI Foundry, siekiant pažangių AI agentų galimybių.
- Pasinaudoti Azure Machine Learning (ML) vykdant ML procesus ir registruojant modelius kaip MCP įrankius.

## Azure OpenAI integracija

Azure OpenAI suteikia prieigą prie galingų AI modelių, tokių kaip GPT-4 ir kitų. Integravus MCP su Azure OpenAI, galima naudotis šiais modeliais, išlaikant MCP įrankių koordinavimo lankstumą.

### C# įgyvendinimas

Šiame kodo pavyzdyje demonstruojame, kaip integruoti MCP su Azure OpenAI naudojant Azure OpenAI SDK.

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

Ankstesniame kode mes:

- Supratome, kaip sukonfigūruoti Azure OpenAI klientą, naudojant galinį tašką, diegimo pavadinimą ir API raktą.
- Sukūrėme metodą `GetCompletionWithToolsAsync`, kad gautume užbaigimus su įrankių palaikymu.
- Apdorojome įrankių kvietimus atsakyme.

Rekomenduojama įgyvendinti faktinę įrankių apdorojimo logiką, atsižvelgiant į jūsų specifinį MCP serverio nustatymą.

## Microsoft AI Foundry integracija

Azure AI Foundry suteikia platformą AI agentų kūrimui ir diegimui. Integravus MCP su AI Foundry, galima pasinaudoti jo galimybėmis, išlaikant MCP lankstumą.

Žemiau pateiktame kode kuriame agento integraciją, kuri apdoroja užklausas ir valdo įrankių kvietimus naudodama MCP.

### Java įgyvendinimas

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

Ankstesniame kode mes:

- Sukūrėme klasę `AIFoundryMcpBridge`, kuri integruojasi tiek su AI Foundry, tiek su MCP.
- Įgyvendinome metodą `processAgentRequest`, kuris apdoroja AI Foundry agento užklausą.
- Apdorojome įrankių kvietimus, vykdydami juos per MCP klientą ir pateikdami rezultatus atgal AI Foundry agentui.

## MCP integracija su Azure ML

Integravus MCP su Azure Machine Learning (ML), galima pasinaudoti galingomis Azure ML galimybėmis, išlaikant MCP lankstumą. Ši integracija gali būti naudojama ML procesų vykdymui, modelių registravimui kaip įrankių ir kompiuterinių resursų valdymui.

### Python įgyvendinimas

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

Ankstesniame kode mes:

- Sukūrėme klasę `EnterpriseAiIntegration`, kuri integruoja MCP su Azure ML.
- Įgyvendinome metodą `execute_ml_pipeline`, kuris apdoroja įvesties duomenis naudodamas MCP įrankius ir pateikia ML procesą Azure ML.
- Įgyvendinome metodą `register_ml_model_as_tool`, kuris registruoja Azure ML modelį kaip MCP įrankį, įskaitant reikalingos diegimo aplinkos ir kompiuterinių resursų sukūrimą.
- Susiejome Azure ML duomenų tipus su JSON schemos tipais, skirtus įrankių registracijai.
- Naudojome asinchroninį programavimą, kad apdorotume galimai ilgai trunkančias operacijas, tokias kaip ML procesų vykdymas ir modelių registracija.

## Kas toliau

- [5.2 Daugiarūšis modalumas](../mcp-multi-modality/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.