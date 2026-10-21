# Enterprise Integration

Kapag bumubuo ng mga MCP Server sa isang enterprise na konteksto, madalas mong kailangang isama ang mga umiiral na AI platform at serbisyo. Tinutukoy ng seksyong ito kung paano isasama ang MCP sa mga enterprise system gaya ng Azure OpenAI at Microsoft AI Foundry, na nagpapahintulot sa mga advanced na kakayahan ng AI at orchestrasyon ng mga tool.

## Panimula

Sa araling ito, matututuhan mo kung paano isasama ang Model Context Protocol (MCP) sa mga enterprise AI system, na nakatuon sa Azure OpenAI at Microsoft AI Foundry. Pinapayagan ka ng mga integrasyong ito na gamitin ang makapangyarihang mga AI model at tool habang pinapanatili ang kakayahang bumagay at mapalawak ng MCP.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Isama ang MCP sa Azure OpenAI upang magamit ang mga kakayahan nito sa AI.
- Ipatupad ang orchestrasyon ng tool ng MCP gamit ang Azure OpenAI.
- Pagsamahin ang MCP sa Microsoft AI Foundry para sa mga advanced na kakayahan ng AI agent.
- Gamitin ang Azure Machine Learning (ML) para sa pagpapatupad ng mga ML pipeline at pagrehistro ng mga modelo bilang mga tool ng MCP.

## Integrasyon ng Azure OpenAI

Nagbibigay ang Microsoft Foundry ng access sa kasalukuyang mga AI model tulad ng GPT-5.1.
Pinapanatili ng pagsasama ng MCP sa mga Foundry model ang kakayahang bumagay ng orchestrasyon ng tool ng MCP habang gumagamit ng managed model deployment.


### Implementasyon sa C#

Sa snippet ng code na ito, ipinapakita namin kung paano isasama ang MCP sa Azure OpenAI gamit ang Azure OpenAI SDK.

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

Sa nakaraang code ay:

- Inayos ang Azure OpenAI client gamit ang endpoint, deployment name, at API key.
- Lumilikha ng isang paraan `GetCompletionWithToolsAsync` upang kumuha ng mga completion na may suporta sa tool.
- Pinangasiwaan ang mga tawag sa tool sa tugon.

Hinihikayat kang ipatupad ang aktwal na lohika ng paghawak ng tool batay sa iyong partikular na setup ng MCP server.

## Integrasyon ng Microsoft Foundry

Nagbibigay ang Microsoft Foundry ng isang platform para sa pagbuo at pag-deploy ng mga AI agent. Ang pagsasama ng MCP sa Microsoft Foundry ay nagbibigay-daan sa iyo upang magamit ang mga kakayahan nito habang pinapanatili ang kakayahang bumagay ng MCP.

Sa code sa ibaba, bumubuo kami ng isang Agent integration na nagpoproseso ng mga kahilingan at humahawak ng mga tawag sa tool gamit ang MCP.

### Implementasyon sa Java

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

Sa nakaraang code ay:

- Lumilikha ng isang `AIFoundryMcpBridge` class na nagsasama ng parehong AI Foundry at MCP.
- Nagpatupad ng isang paraan `processAgentRequest` na nagpoproseso ng kahilingan ng AI Foundry agent.
- Pinangasiwaan ang mga tawag sa tool sa pamamagitan ng pagpapatupad nito gamit ang MCP client at pagsusumite ng mga resulta pabalik sa AI Foundry agent.

## Pagsasama ng MCP sa Azure ML

Ang pagsasama ng MCP sa Azure Machine Learning (ML) ay nagpapahintulot sa iyo na gamitin ang makapangyarihang kakayahan ng ML ng Azure habang pinapanatili ang kakayahang bumagay ng MCP. Maaari itong gamitin upang magsagawa ng ML pipeline, magrehistro ng mga modelo bilang mga tool, at pamahalaan ang compute resources.

### Implementasyon sa Python

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

Sa nakaraang code ay:

- Lumilikha ng isang `EnterpriseAiIntegration` class na nagsasama ng MCP sa Azure ML.
- Nagpatupad ng isang `execute_ml_pipeline` na paraan na nagpoproseso ng input data gamit ang mga tool ng MCP at nagpapasa ng ML pipeline sa Azure ML.
- Nagpatupad ng isang `register_ml_model_as_tool` na paraan na nagrerehistro ng isang Azure ML model bilang MCP tool, kabilang ang paglikha ng kinakailangang deployment environment at compute resources.
- Inikot ang mga data type ng Azure ML sa mga JSON schema type para sa pagrehistro ng tool.
- Gumamit ng asynchronous programming upang hawakan ang mga posibleng pangmatagalang operasyon tulad ng pagpapatupad ng ML pipeline at pagrehistro ng modelo.

## Ano ang susunod

- [5.2 Multi modality](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->