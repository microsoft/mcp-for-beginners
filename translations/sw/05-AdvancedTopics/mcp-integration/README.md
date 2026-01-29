# Ujumuishaji wa Biashara

Unapojenga Seva za MCP katika muktadha wa biashara, mara nyingi unahitaji kuunganisha na majukwaa na huduma za AI zilizopo. Sehemu hii inashughulikia jinsi ya kuunganisha MCP na mifumo ya biashara kama Azure OpenAI na Microsoft AI Foundry, kuwezesha uwezo wa hali ya juu wa AI na uratibu wa zana.

## Utangulizi

Katika somo hili, utajifunza jinsi ya kuunganisha Model Context Protocol (MCP) na mifumo ya AI ya biashara, ukilenga Azure OpenAI na Microsoft AI Foundry. Ujumuishaji huu unakuruhusu kutumia mifano na zana zenye nguvu za AI huku ukidumisha kubadilika na upanuzi wa MCP.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuunganisha MCP na Azure OpenAI ili kutumia uwezo wake wa AI.
- Kutekeleza uratibu wa zana za MCP na Azure OpenAI.
- Kuchanganya MCP na Microsoft AI Foundry kwa uwezo wa hali ya juu wa mawakala wa AI.
- Kutumia Azure Machine Learning (ML) kwa utekelezaji wa mabomba ya ML na kusajili mifano kama zana za MCP.

## Ujumuishaji wa Azure OpenAI

Azure OpenAI inatoa ufikiaji wa mifano yenye nguvu ya AI kama GPT-4 na mingine. Kuunganisha MCP na Azure OpenAI kunakuruhusu kutumia mifano hii huku ukidumisha kubadilika kwa uratibu wa zana za MCP.

### Utekelezaji wa C#

Katika kipande hiki cha msimbo, tunaonyesha jinsi ya kuunganisha MCP na Azure OpenAI kwa kutumia Azure OpenAI SDK.

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

Katika msimbo uliotangulia tumefanya yafuatayo:

- Tumesanidi mteja wa Azure OpenAI na endpoint, jina la deployment, na API key.
- Tumeunda mbinu `GetCompletionWithToolsAsync` ili kupata majibu yenye msaada wa zana.
- Tumeshughulikia miito ya zana katika majibu.

Unahimizwa kutekeleza mantiki halisi ya kushughulikia zana kulingana na usanidi maalum wa seva yako ya MCP.

## Ujumuishaji wa Microsoft AI Foundry

Azure AI Foundry inatoa jukwaa la kujenga na kupeleka mawakala wa AI. Kuunganisha MCP na AI Foundry kunakuruhusu kutumia uwezo wake huku ukidumisha kubadilika kwa MCP.

Katika msimbo wa chini, tunatengeneza ujumuishaji wa Wakala unaoshughulikia maombi na kushughulikia miito ya zana kwa kutumia MCP.

### Utekelezaji wa Java

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

Katika msimbo uliotangulia, tumefanya yafuatayo:

- Tumeunda darasa `AIFoundryMcpBridge` linalounganisha AI Foundry na MCP.
- Tumetekeleza mbinu `processAgentRequest` inayoshughulikia ombi la wakala wa AI Foundry.
- Tumeshughulikia miito ya zana kwa kuitekeleza kupitia mteja wa MCP na kuwasilisha matokeo kwa wakala wa AI Foundry.

## Kuunganisha MCP na Azure ML

Kuunganisha MCP na Azure Machine Learning (ML) kunakuruhusu kutumia uwezo wa hali ya juu wa ML wa Azure huku ukidumisha kubadilika kwa MCP. Ujumuishaji huu unaweza kutumika kutekeleza mabomba ya ML, kusajili mifano kama zana, na kusimamia rasilimali za kompyuta.

### Utekelezaji wa Python

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

Katika msimbo uliotangulia, tumefanya yafuatayo:

- Tumeunda darasa `EnterpriseAiIntegration` linalounganisha MCP na Azure ML.
- Tumetekeleza mbinu `execute_ml_pipeline` inayoshughulikia data ya pembejeo kwa kutumia zana za MCP na kuwasilisha bomba la ML kwa Azure ML.
- Tumetekeleza mbinu `register_ml_model_as_tool` inayosajili mfano wa Azure ML kama zana ya MCP, ikijumuisha kuunda mazingira ya deployment yanayohitajika na rasilimali za kompyuta.
- Tumefanya ramani ya aina za data za Azure ML kwa aina za JSON schema kwa usajili wa zana.
- Tumetumia programu ya asynchronous kushughulikia shughuli zinazoweza kuchukua muda mrefu kama utekelezaji wa mabomba ya ML na usajili wa mifano.

## Nini cha Kufanya Baadaye

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya binadamu ya kitaalamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.