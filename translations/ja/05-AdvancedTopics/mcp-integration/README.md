# エンタープライズ統合

エンタープライズ環境でMCPサーバーを構築する際、既存のAIプラットフォームやサービスと統合する必要があることがよくあります。このセクションでは、Azure OpenAIやMicrosoft AI FoundryのようなエンタープライズシステムとMCPを統合し、高度なAI機能やツールのオーケストレーションを実現する方法について説明します。

## はじめに

このレッスンでは、Model Context Protocol (MCP) をエンタープライズAIシステムと統合する方法を学びます。特にAzure OpenAIとMicrosoft AI Foundryに焦点を当てます。これらの統合により、強力なAIモデルやツールを活用しながら、MCPの柔軟性と拡張性を維持することができます。

## 学習目標

このレッスンの終わりまでに、以下ができるようになります：

- Azure OpenAIとMCPを統合し、そのAI機能を活用する。
- Azure OpenAIを使用したMCPツールのオーケストレーションを実装する。
- Microsoft AI FoundryとMCPを組み合わせ、高度なAIエージェント機能を実現する。
- Azure Machine Learning (ML) を活用してMLパイプラインを実行し、モデルをMCPツールとして登録する。

## Azure OpenAIとの統合

Azure OpenAIは、GPT-4などの強力なAIモデルへのアクセスを提供します。MCPをAzure OpenAIと統合することで、これらのモデルを活用しながら、MCPのツールオーケストレーションの柔軟性を維持することができます。

### C# 実装

以下のコードスニペットでは、Azure OpenAI SDKを使用してMCPをAzure OpenAIと統合する方法を示します。

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

上記のコードでは以下を行っています：

- エンドポイント、デプロイメント名、APIキーを使用してAzure OpenAIクライアントを設定。
- ツールサポート付きで補完を取得するためのメソッド`GetCompletionWithToolsAsync`を作成。
- レスポンス内でツール呼び出しを処理。

実際のツール処理ロジックは、特定のMCPサーバー設定に基づいて実装することをお勧めします。

## Microsoft AI Foundryとの統合

Azure AI Foundryは、AIエージェントの構築とデプロイのためのプラットフォームを提供します。MCPをAI Foundryと統合することで、その機能を活用しながらMCPの柔軟性を維持することができます。

以下のコードでは、リクエストを処理し、MCPを使用してツール呼び出しを処理するエージェント統合を開発します。

### Java 実装

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

上記のコードでは以下を行っています：

- AI FoundryとMCPの両方と統合する`AIFoundryMcpBridge`クラスを作成。
- AI Foundryエージェントリクエストを処理するメソッド`processAgentRequest`を実装。
- MCPクライアントを介してツール呼び出しを実行し、その結果をAI Foundryエージェントに返す処理を実装。

## Azure MLとのMCP統合

Azure Machine Learning (ML) とMCPを統合することで、Azureの強力なML機能を活用しながらMCPの柔軟性を維持することができます。この統合により、MLパイプラインの実行、モデルのツールとしての登録、コンピュートリソースの管理が可能になります。

### Python 実装

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

上記のコードでは以下を行っています：

- MCPとAzure MLを統合する`EnterpriseAiIntegration`クラスを作成。
- MCPツールを使用して入力データを処理し、Azure MLにMLパイプラインを送信する`execute_ml_pipeline`メソッドを実装。
- Azure MLモデルをMCPツールとして登録する`register_ml_model_as_tool`メソッドを実装。この中で必要なデプロイ環境やコンピュートリソースを作成。
- Azure MLのデータ型をJSONスキーマ型にマッピングしてツール登録を実現。
- MLパイプラインの実行やモデル登録のような長時間実行される可能性のある操作を非同期プログラミングで処理。

## 次のステップ

- [5.2 マルチモダリティ](../mcp-multi-modality/README.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。