# 企业集成

在企业环境中构建 MCP 服务器时，通常需要与现有的 AI 平台和服务进行集成。本节将介绍如何将 MCP 与企业系统（如 Azure OpenAI 和 Microsoft AI Foundry）集成，以实现高级 AI 功能和工具编排。

## 简介

在本课程中，您将学习如何将模型上下文协议（MCP）与企业 AI 系统集成，重点关注 Azure OpenAI 和 Microsoft AI Foundry。这些集成使您能够利用强大的 AI 模型和工具，同时保持 MCP 的灵活性和可扩展性。

## 学习目标

完成本课程后，您将能够：

- 将 MCP 与 Azure OpenAI 集成，以利用其 AI 功能。
- 使用 Azure OpenAI 实现 MCP 工具编排。
- 将 MCP 与 Microsoft AI Foundry 结合，提供高级 AI 代理功能。
- 利用 Azure 机器学习（ML）执行 ML 管道并将模型注册为 MCP 工具。

## Azure OpenAI 集成

Azure OpenAI 提供了对强大 AI 模型（如 GPT-4 等）的访问权限。将 MCP 与 Azure OpenAI 集成可以在保持 MCP 工具编排灵活性的同时利用这些模型。

### C# 实现

以下代码片段展示了如何使用 Azure OpenAI SDK 将 MCP 与 Azure OpenAI 集成。

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

在上述代码中，我们：

- 配置了 Azure OpenAI 客户端，包括端点、部署名称和 API 密钥。
- 创建了一个方法 `GetCompletionWithToolsAsync`，用于获取支持工具的补全结果。
- 处理了响应中的工具调用。

建议您根据具体的 MCP 服务器设置实现实际的工具处理逻辑。

## Microsoft AI Foundry 集成

Azure AI Foundry 提供了一个构建和部署 AI 代理的平台。将 MCP 与 AI Foundry 集成可以在保持 MCP 灵活性的同时利用其功能。

以下代码展示了一个代理集成，它处理请求并使用 MCP 处理工具调用。

### Java 实现

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

在上述代码中，我们：

- 创建了一个 `AIFoundryMcpBridge` 类，该类与 AI Foundry 和 MCP 都进行了集成。
- 实现了一个方法 `processAgentRequest`，用于处理 AI Foundry 代理请求。
- 通过 MCP 客户端执行工具调用，并将结果提交回 AI Foundry 代理。

## MCP 与 Azure ML 的集成

将 MCP 与 Azure 机器学习（ML）集成可以在保持 MCP 灵活性的同时利用 Azure 强大的 ML 功能。此集成可用于执行 ML 管道、将模型注册为工具以及管理计算资源。

### Python 实现

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

在上述代码中，我们：

- 创建了一个 `EnterpriseAiIntegration` 类，将 MCP 与 Azure ML 集成。
- 实现了一个 `execute_ml_pipeline` 方法，使用 MCP 工具处理输入数据并将 ML 管道提交到 Azure ML。
- 实现了一个 `register_ml_model_as_tool` 方法，将 Azure ML 模型注册为 MCP 工具，包括创建必要的部署环境和计算资源。
- 将 Azure ML 数据类型映射到 JSON schema 类型以进行工具注册。
- 使用异步编程处理可能耗时较长的操作，例如 ML 管道执行和模型注册。

## 下一步

- [5.2 多模态](../mcp-multi-modality/README.md)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。