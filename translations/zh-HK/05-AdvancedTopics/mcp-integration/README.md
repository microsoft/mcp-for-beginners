# 企業整合

在企業環境中構建 MCP 伺服器時，通常需要與現有的 AI 平台和服務進行整合。本節將介紹如何將 MCP 與企業系統（如 Azure OpenAI 和 Microsoft AI Foundry）整合，以實現高級 AI 功能和工具協作。

## 簡介

在本課程中，您將學習如何將模型上下文協議（MCP）與企業 AI 系統整合，重點是 Azure OpenAI 和 Microsoft AI Foundry。這些整合能讓您在保持 MCP 靈活性和可擴展性的同時，充分利用強大的 AI 模型和工具。

## 學習目標

完成本課程後，您將能夠：

- 將 MCP 與 Azure OpenAI 整合，利用其 AI 功能。
- 使用 Azure OpenAI 實現 MCP 工具協作。
- 將 MCP 與 Microsoft AI Foundry 結合，實現高級 AI 代理功能。
- 利用 Azure 機器學習（ML）執行 ML 管道並將模型註冊為 MCP 工具。

## Azure OpenAI 整合

Azure OpenAI 提供了如 GPT-4 等強大的 AI 模型。將 MCP 與 Azure OpenAI 整合，能讓您在保持 MCP 工具協作靈活性的同時，利用這些模型。

### C# 實現

以下程式碼片段展示了如何使用 Azure OpenAI SDK 將 MCP 與 Azure OpenAI 整合。

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

在上述程式碼中，我們：

- 配置了 Azure OpenAI 客戶端，包括端點、部署名稱和 API 金鑰。
- 創建了一個方法 `GetCompletionWithToolsAsync`，用於獲取支持工具的補全結果。
- 處理了回應中的工具調用。

建議您根據具體的 MCP 伺服器設置實現實際的工具處理邏輯。

## Microsoft AI Foundry 整合

Azure AI Foundry 提供了一個構建和部署 AI 代理的平台。將 MCP 與 AI Foundry 整合，能讓您在保持 MCP 靈活性的同時，利用其功能。

以下程式碼展示了如何開發一個代理整合，處理請求並使用 MCP 處理工具調用。

### Java 實現

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

在上述程式碼中，我們：

- 創建了一個 `AIFoundryMcpBridge` 類，整合了 AI Foundry 和 MCP。
- 實現了一個方法 `processAgentRequest`，用於處理 AI Foundry 代理請求。
- 通過 MCP 客戶端執行工具調用，並將結果提交回 AI Foundry 代理。

## MCP 與 Azure ML 的整合

將 MCP 與 Azure 機器學習（ML）整合，能讓您在保持 MCP 靈活性的同時，利用 Azure 強大的 ML 功能。此整合可用於執行 ML 管道、將模型註冊為工具以及管理計算資源。

### Python 實現

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

在上述程式碼中，我們：

- 創建了一個 `EnterpriseAiIntegration` 類，將 MCP 與 Azure ML 整合。
- 實現了一個 `execute_ml_pipeline` 方法，使用 MCP 工具處理輸入數據並提交 ML 管道到 Azure ML。
- 實現了一個 `register_ml_model_as_tool` 方法，將 Azure ML 模型註冊為 MCP 工具，包括創建必要的部署環境和計算資源。
- 將 Azure ML 數據類型映射到 JSON 架構類型以進行工具註冊。
- 使用異步編程處理可能耗時的操作，如 ML 管道執行和模型註冊。

## 下一步

- [5.2 多模態](../mcp-multi-modality/README.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。