# ਐਂਟਰਪ੍ਰਾਈਜ਼ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਜਦੋਂ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸੰਦਰਭ ਵਿੱਚ MCP ਸਰਵਰ ਬਣਾਉਂਦੇ ਹੋ, ਤਾਂ ਅਕਸਰ ਮੌਜੂਦਾ AI ਪਲੇਟਫਾਰਮਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਇਸ ਭਾਗ ਵਿੱਚ ਇਹ ਕਵਰ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ MCP ਨੂੰ Azure OpenAI ਅਤੇ Microsoft AI Foundry ਵਰਗੇ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸਿਸਟਮਾਂ ਨਾਲ ਕਿਵੇਂ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਤਕਨੀਕੀ AI ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਟੂਲ ਆਰਕੇਸਟਰੇਸ਼ਨ ਨੂੰ ਯੋਗ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਨੂੰ ਐਂਟਰਪ੍ਰਾਈਜ਼ AI ਸਿਸਟਮਾਂ ਨਾਲ ਕਿਵੇਂ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ ਹੈ, ਖਾਸ ਕਰਕੇ Azure OpenAI ਅਤੇ Microsoft AI Foundry 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦੇ ਹੋਏ। ਇਹ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਤੁਹਾਨੂੰ ਸ਼ਕਤੀਸ਼ਾਲੀ AI ਮਾਡਲਾਂ ਅਤੇ ਟੂਲਾਂ ਦਾ ਲਾਭ ਲੈਣ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ ਜਦਕਿ MCP ਦੀ ਲਚੀਲਤਾ ਅਤੇ ਵਿਸਤਾਰਯੋਗਤਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦੇ ਹਨ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- Azure OpenAI ਨਾਲ MCP ਨੂੰ ਇੰਟੀਗ੍ਰੇਟ ਕਰਕੇ ਇਸ ਦੀਆਂ AI ਸਮਰੱਥਾਵਾਂ ਦਾ ਉਪਯੋਗ ਕਰਨਾ।
- Azure OpenAI ਨਾਲ MCP ਟੂਲ ਆਰਕੇਸਟਰੇਸ਼ਨ ਨੂੰ ਲਾਗੂ ਕਰਨਾ।
- Microsoft AI Foundry ਨਾਲ MCP ਨੂੰ ਜੋੜ ਕੇ ਉੱਨਤ AI ਏਜੰਟ ਸਮਰੱਥਾਵਾਂ ਪ੍ਰਾਪਤ ਕਰਨਾ।
- Azure Machine Learning (ML) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ML ਪਾਈਪਲਾਈਨਾਂ ਚਲਾਉਣ ਅਤੇ ਮਾਡਲਾਂ ਨੂੰ MCP ਟੂਲਾਂ ਵਜੋਂ ਰਜਿਸਟਰ ਕਰਨਾ।

## Azure OpenAI ਇੰਟੀਗ੍ਰੇਸ਼ਨ

Azure OpenAI ਸ਼ਕਤੀਸ਼ਾਲੀ AI ਮਾਡਲਾਂ ਜਿਵੇਂ GPT-4 ਆਦਿ ਤੱਕ ਪਹੁੰਚ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। MCP ਨੂੰ Azure OpenAI ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ ਤੁਹਾਨੂੰ ਇਹ ਮਾਡਲ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਜਦਕਿ MCP ਦੇ ਟੂਲ ਆਰਕੇਸਟਰੇਸ਼ਨ ਦੀ ਲਚੀਲਤਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ।

### C# ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ

ਇਸ ਕੋਡ ਸਨਿੱਪਟ ਵਿੱਚ, ਅਸੀਂ ਦਿਖਾਇਆ ਹੈ ਕਿ Azure OpenAI SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਨੂੰ Azure OpenAI ਨਾਲ ਕਿਵੇਂ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ ਹੈ।

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਐਂਡਪੌਇੰਟ, ਡਿਪਲੌਇਮੈਂਟ ਨਾਂ ਅਤੇ API ਕੁੰਜੀ ਨਾਲ Azure OpenAI ਕਲਾਇੰਟ ਨੂੰ ਕਨਫਿਗਰ ਕੀਤਾ।
- `GetCompletionWithToolsAsync` ਨਾਮਕ ਇੱਕ ਵਿਧੀ ਬਣਾਈ ਜੋ ਟੂਲ ਸਹਾਇਤਾ ਨਾਲ ਕਮਪਲੀਸ਼ਨ ਪ੍ਰਾਪਤ ਕਰਦੀ ਹੈ।
- ਜਵਾਬ ਵਿੱਚ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਹੈਂਡਲ ਕੀਤਾ।

ਤੁਹਾਨੂੰ ਆਪਣੇ ਖਾਸ MCP ਸਰਵਰ ਸੈਟਅੱਪ ਦੇ ਆਧਾਰ 'ਤੇ ਅਸਲ ਟੂਲ ਹੈਂਡਲਿੰਗ ਲੌਜਿਕ ਲਾਗੂ ਕਰਨ ਲਈ ਪ੍ਰੇਰਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

## Microsoft AI Foundry ਇੰਟੀਗ੍ਰੇਸ਼ਨ

Azure AI Foundry ਇੱਕ ਪਲੇਟਫਾਰਮ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ AI ਏਜੰਟ ਬਣਾਉਣ ਅਤੇ ਡਿਪਲੌਇ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। MCP ਨੂੰ AI Foundry ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ ਤੁਹਾਨੂੰ ਇਸ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਦਾ ਲਾਭ ਲੈਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਜਦਕਿ MCP ਦੀ ਲਚੀਲਤਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਏਜੰਟ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਵਿਕਸਿਤ ਕੀਤਾ ਹੈ ਜੋ ਬੇਨਤੀ ਪ੍ਰਕਿਰਿਆ ਕਰਦਾ ਹੈ ਅਤੇ MCP ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਹੈਂਡਲ ਕਰਦਾ ਹੈ।

### ਜਾਵਾ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `AIFoundryMcpBridge` ਕਲਾਸ ਬਣਾਈ ਜੋ AI Foundry ਅਤੇ MCP ਦੋਵਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਦੀ ਹੈ।
- ਇੱਕ ਵਿਧੀ `processAgentRequest` ਲਾਗੂ ਕੀਤੀ ਜੋ AI Foundry ਏਜੰਟ ਦੀ ਬੇਨਤੀ ਪ੍ਰਕਿਰਿਆ ਕਰਦੀ ਹੈ।
- ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਹੈਂਡਲ ਕੀਤਾ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ MCP ਕਲਾਇੰਟ ਰਾਹੀਂ ਚਲਾਇਆ ਅਤੇ ਨਤੀਜੇ ਵਾਪਸ AI Foundry ਏਜੰਟ ਨੂੰ ਭੇਜੇ।

## Azure ML ਨਾਲ MCP ਦਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

Azure Machine Learning (ML) ਨਾਲ MCP ਦਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਤੁਹਾਨੂੰ Azure ਦੀ ਸ਼ਕਤੀਸ਼ਾਲੀ ML ਸਮਰੱਥਾਵਾਂ ਦਾ ਲਾਭ ਲੈਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਜਦਕਿ MCP ਦੀ ਲਚੀਲਤਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ। ਇਹ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ML ਪਾਈਪਲਾਈਨਾਂ ਚਲਾਉਣ, ਮਾਡਲਾਂ ਨੂੰ ਟੂਲ ਵਜੋਂ ਰਜਿਸਟਰ ਕਰਨ ਅਤੇ ਕੰਪਿਊਟ ਸਰੋਤਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ।

### ਪਾਇਥਨ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `EnterpriseAiIntegration` ਕਲਾਸ ਬਣਾਈ ਜੋ MCP ਨੂੰ Azure ML ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਦੀ ਹੈ।
- ਇੱਕ `execute_ml_pipeline` ਵਿਧੀ ਲਾਗੂ ਕੀਤੀ ਜੋ ਇਨਪੁਟ ਡਾਟਾ ਨੂੰ MCP ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਕਿਰਿਆ ਕਰਦੀ ਹੈ ਅਤੇ Azure ML ਨੂੰ ML ਪਾਈਪਲਾਈਨ ਭੇਜਦੀ ਹੈ।
- ਇੱਕ `register_ml_model_as_tool` ਵਿਧੀ ਲਾਗੂ ਕੀਤੀ ਜੋ Azure ML ਮਾਡਲ ਨੂੰ MCP ਟੂਲ ਵਜੋਂ ਰਜਿਸਟਰ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਡਿਪਲੌਇਮੈਂਟ ਵਾਤਾਵਰਣ ਅਤੇ ਕੰਪਿਊਟ ਸਰੋਤ ਬਣਾਉਣਾ ਸ਼ਾਮਲ ਹੈ।
- ਟੂਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਲਈ Azure ML ਡਾਟਾ ਪ੍ਰਕਾਰਾਂ ਨੂੰ JSON ਸਕੀਮਾ ਪ੍ਰਕਾਰਾਂ ਨਾਲ ਮੈਪ ਕੀਤਾ।
- ਲੰਬੇ ਸਮੇਂ ਚੱਲਣ ਵਾਲੀਆਂ ਕਾਰਵਾਈਆਂ ਜਿਵੇਂ ML ਪਾਈਪਲਾਈਨ ਪ੍ਰਕਿਰਿਆ ਅਤੇ ਮਾਡਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਨੂੰ ਹੈਂਡਲ ਕਰਨ ਲਈ ਅਸਿੰਕ੍ਰੋਨਸ ਪ੍ਰੋਗਰਾਮਿੰਗ ਦੀ ਵਰਤੋਂ ਕੀਤੀ।

## ਅਗਲਾ ਕੀ ਹੈ

- [5.2 ਮਲਟੀ ਮੋਡੈਲਿਟੀ](../mcp-multi-modality/README.md)

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।