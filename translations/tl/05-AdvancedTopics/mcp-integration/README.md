# Enterprise Integration

Kapag gumagawa ng MCP Servers sa konteksto ng enterprise, madalas na kinakailangan ang integrasyon sa mga umiiral na AI platform at serbisyo. Ang seksyong ito ay tumatalakay kung paano i-integrate ang MCP sa mga enterprise system tulad ng Azure OpenAI at Microsoft AI Foundry, upang paganahin ang advanced na AI capabilities at tool orchestration.

## Panimula

Sa araling ito, matututunan mo kung paano i-integrate ang Model Context Protocol (MCP) sa mga enterprise AI system, na nakatuon sa Azure OpenAI at Microsoft AI Foundry. Ang mga integrasyong ito ay nagbibigay-daan sa paggamit ng makapangyarihang AI models at tools habang pinapanatili ang flexibility at extensibility ng MCP.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng araling ito, magagawa mo ang sumusunod:

- I-integrate ang MCP sa Azure OpenAI upang magamit ang AI capabilities nito.
- Ipatupad ang MCP tool orchestration gamit ang Azure OpenAI.
- Pagsamahin ang MCP sa Microsoft AI Foundry para sa advanced na AI agent capabilities.
- Gamitin ang Azure Machine Learning (ML) para sa pag-execute ng ML pipelines at pagrehistro ng mga modelo bilang MCP tools.

## Integrasyon ng Azure OpenAI

Ang Azure OpenAI ay nagbibigay ng access sa makapangyarihang AI models tulad ng GPT-4 at iba pa. Ang integrasyon ng MCP sa Azure OpenAI ay nagbibigay-daan sa paggamit ng mga modelong ito habang pinapanatili ang flexibility ng MCP's tool orchestration.

### Implementasyon sa C#

Sa code snippet na ito, ipinapakita namin kung paano i-integrate ang MCP sa Azure OpenAI gamit ang Azure OpenAI SDK.

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

Sa naunang code, ginawa namin ang sumusunod:

- Kinonfigura ang Azure OpenAI client gamit ang endpoint, deployment name, at API key.
- Lumikha ng method na `GetCompletionWithToolsAsync` para makakuha ng completions na may suporta sa tools.
- Hinandle ang tool calls sa response.

Hinihikayat kang ipatupad ang aktwal na tool handling logic batay sa iyong partikular na MCP server setup.

## Integrasyon ng Microsoft AI Foundry

Ang Azure AI Foundry ay nagbibigay ng platform para sa pagbuo at pag-deploy ng AI agents. Ang integrasyon ng MCP sa AI Foundry ay nagbibigay-daan sa paggamit ng mga kakayahan nito habang pinapanatili ang flexibility ng MCP.

Sa code sa ibaba, nag-develop kami ng Agent integration na nagpoproseso ng mga request at hinahandle ang tool calls gamit ang MCP.

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

Sa naunang code, ginawa namin ang sumusunod:

- Lumikha ng `AIFoundryMcpBridge` class na nag-iintegrate sa parehong AI Foundry at MCP.
- Nagpatupad ng method na `processAgentRequest` na nagpoproseso ng AI Foundry agent request.
- Hinandle ang tool calls sa pamamagitan ng pag-execute nito gamit ang MCP client at pagsusumite ng mga resulta pabalik sa AI Foundry agent.

## Integrasyon ng MCP sa Azure ML

Ang integrasyon ng MCP sa Azure Machine Learning (ML) ay nagbibigay-daan sa paggamit ng makapangyarihang ML capabilities ng Azure habang pinapanatili ang flexibility ng MCP. Ang integrasyong ito ay maaaring gamitin para sa pag-execute ng ML pipelines, pagrehistro ng mga modelo bilang tools, at pamamahala ng compute resources.

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

Sa naunang code, ginawa namin ang sumusunod:

- Lumikha ng `EnterpriseAiIntegration` class na nag-iintegrate ng MCP sa Azure ML.
- Nagpatupad ng `execute_ml_pipeline` method na nagpoproseso ng input data gamit ang MCP tools at nagsusumite ng ML pipeline sa Azure ML.
- Nagpatupad ng `register_ml_model_as_tool` method na nagrerehistro ng Azure ML model bilang MCP tool, kabilang ang paglikha ng kinakailangang deployment environment at compute resources.
- Nagmap ng Azure ML data types sa JSON schema types para sa tool registration.
- Gumamit ng asynchronous programming para i-handle ang mga posibleng matagal na operasyon tulad ng ML pipeline execution at model registration.

## Ano ang susunod

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.