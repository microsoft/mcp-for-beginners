# 엔터프라이즈 통합

엔터프라이즈 환경에서 MCP 서버를 구축할 때 기존 AI 플랫폼 및 서비스와 통합해야 하는 경우가 많습니다. 이 섹션에서는 Azure OpenAI 및 Microsoft AI Foundry와 같은 엔터프라이즈 시스템과 MCP를 통합하여 고급 AI 기능과 도구 오케스트레이션을 구현하는 방법을 다룹니다.

## 소개

이 강의에서는 Model Context Protocol (MCP)을 엔터프라이즈 AI 시스템과 통합하는 방법을 배웁니다. 특히 Azure OpenAI와 Microsoft AI Foundry를 중심으로 설명합니다. 이러한 통합을 통해 강력한 AI 모델과 도구를 활용하면서 MCP의 유연성과 확장성을 유지할 수 있습니다.

## 학습 목표

이 강의를 마치면 다음을 수행할 수 있습니다:

- MCP를 Azure OpenAI와 통합하여 AI 기능을 활용하기.
- Azure OpenAI를 사용하여 MCP 도구 오케스트레이션 구현하기.
- MCP와 Microsoft AI Foundry를 결합하여 고급 AI 에이전트 기능 활용하기.
- Azure Machine Learning (ML)을 활용하여 ML 파이프라인을 실행하고 모델을 MCP 도구로 등록하기.

## Azure OpenAI 통합

Azure OpenAI는 GPT-4와 같은 강력한 AI 모델에 접근할 수 있는 기능을 제공합니다. MCP를 Azure OpenAI와 통합하면 이러한 모델을 활용하면서 MCP의 도구 오케스트레이션 유연성을 유지할 수 있습니다.

### C# 구현

다음 코드 스니펫은 Azure OpenAI SDK를 사용하여 MCP를 Azure OpenAI와 통합하는 방법을 보여줍니다.

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

위 코드에서 우리는 다음을 수행했습니다:

- 엔드포인트, 배포 이름, API 키를 사용하여 Azure OpenAI 클라이언트를 구성했습니다.
- 도구 지원을 포함한 결과를 가져오는 `GetCompletionWithToolsAsync` 메서드를 생성했습니다.
- 응답에서 도구 호출을 처리했습니다.

구체적인 MCP 서버 설정에 따라 실제 도구 처리 로직을 구현하는 것이 권장됩니다.

## Microsoft AI Foundry 통합

Azure AI Foundry는 AI 에이전트를 구축하고 배포할 수 있는 플랫폼을 제공합니다. MCP를 AI Foundry와 통합하면 MCP의 유연성을 유지하면서 Foundry의 기능을 활용할 수 있습니다.

아래 코드에서는 MCP를 사용하여 요청을 처리하고 도구 호출을 처리하는 에이전트 통합을 개발합니다.

### Java 구현

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

위 코드에서 우리는 다음을 수행했습니다:

- AI Foundry와 MCP를 모두 통합하는 `AIFoundryMcpBridge` 클래스를 생성했습니다.
- AI Foundry 에이전트 요청을 처리하는 `processAgentRequest` 메서드를 구현했습니다.
- MCP 클라이언트를 통해 도구 호출을 실행하고 결과를 AI Foundry 에이전트에 다시 제출했습니다.

## Azure ML과 MCP 통합

MCP를 Azure Machine Learning (ML)과 통합하면 Azure의 강력한 ML 기능을 활용하면서 MCP의 유연성을 유지할 수 있습니다. 이 통합은 ML 파이프라인 실행, 모델을 도구로 등록, 컴퓨팅 리소스 관리에 사용될 수 있습니다.

### Python 구현

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

위 코드에서 우리는 다음을 수행했습니다:

- MCP와 Azure ML을 통합하는 `EnterpriseAiIntegration` 클래스를 생성했습니다.
- MCP 도구를 사용하여 입력 데이터를 처리하고 Azure ML에 ML 파이프라인을 제출하는 `execute_ml_pipeline` 메서드를 구현했습니다.
- Azure ML 모델을 MCP 도구로 등록하는 `register_ml_model_as_tool` 메서드를 구현했습니다. 여기에는 필요한 배포 환경 및 컴퓨팅 리소스 생성이 포함됩니다.
- 도구 등록을 위해 Azure ML 데이터 유형을 JSON 스키마 유형으로 매핑했습니다.
- ML 파이프라인 실행 및 모델 등록과 같은 잠재적으로 오래 걸리는 작업을 처리하기 위해 비동기 프로그래밍을 사용했습니다.

## 다음 단계

- [5.2 멀티 모달리티](../mcp-multi-modality/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.