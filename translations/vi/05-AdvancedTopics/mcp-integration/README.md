# Tích hợp Doanh nghiệp

Khi xây dựng các máy chủ MCP trong bối cảnh doanh nghiệp, bạn thường cần tích hợp với các nền tảng và dịch vụ AI hiện có. Phần này hướng dẫn cách tích hợp MCP với các hệ thống doanh nghiệp như Azure OpenAI và Microsoft AI Foundry, giúp kích hoạt các khả năng AI tiên tiến và điều phối công cụ.

## Giới thiệu

Trong bài học này, bạn sẽ học cách tích hợp Giao thức Ngữ cảnh Mô hình (MCP) với các hệ thống AI doanh nghiệp, tập trung vào Azure OpenAI và Microsoft AI Foundry. Những tích hợp này cho phép bạn tận dụng các mô hình và công cụ AI mạnh mẽ đồng thời duy trì tính linh hoạt và khả năng mở rộng của MCP.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Tích hợp MCP với Azure OpenAI để sử dụng các khả năng AI của nó.
- Triển khai điều phối công cụ MCP với Azure OpenAI.
- Kết hợp MCP với Microsoft AI Foundry để có các khả năng tác nhân AI tiên tiến.
- Tận dụng Azure Machine Learning (ML) để thực thi các pipeline ML và đăng ký mô hình dưới dạng công cụ MCP.

## Tích hợp Azure OpenAI

Azure OpenAI cung cấp quyền truy cập vào các mô hình AI mạnh mẽ như GPT-4 và các mô hình khác. Tích hợp MCP với Azure OpenAI cho phép bạn sử dụng các mô hình này đồng thời duy trì tính linh hoạt của điều phối công cụ MCP.

### Triển khai C#

Trong đoạn mã dưới đây, chúng tôi minh họa cách tích hợp MCP với Azure OpenAI bằng Azure OpenAI SDK.

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

Trong đoạn mã trên, chúng tôi đã:

- Cấu hình client Azure OpenAI với endpoint, tên triển khai và API key.
- Tạo một phương thức `GetCompletionWithToolsAsync` để lấy kết quả với hỗ trợ công cụ.
- Xử lý các cuộc gọi công cụ trong phản hồi.

Bạn được khuyến khích triển khai logic xử lý công cụ thực tế dựa trên thiết lập máy chủ MCP cụ thể của mình.

## Tích hợp Microsoft AI Foundry

Azure AI Foundry cung cấp một nền tảng để xây dựng và triển khai các tác nhân AI. Tích hợp MCP với AI Foundry cho phép bạn tận dụng các khả năng của nó đồng thời duy trì tính linh hoạt của MCP.

Trong đoạn mã dưới đây, chúng tôi phát triển một tích hợp Tác nhân xử lý các yêu cầu và xử lý các cuộc gọi công cụ bằng MCP.

### Triển khai Java

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

Trong đoạn mã trên, chúng tôi đã:

- Tạo một lớp `AIFoundryMcpBridge` tích hợp với cả AI Foundry và MCP.
- Triển khai một phương thức `processAgentRequest` để xử lý yêu cầu của tác nhân AI Foundry.
- Xử lý các cuộc gọi công cụ bằng cách thực thi chúng thông qua client MCP và gửi kết quả trở lại tác nhân AI Foundry.

## Tích hợp MCP với Azure ML

Tích hợp MCP với Azure Machine Learning (ML) cho phép bạn tận dụng các khả năng ML mạnh mẽ của Azure đồng thời duy trì tính linh hoạt của MCP. Tích hợp này có thể được sử dụng để thực thi các pipeline ML, đăng ký mô hình dưới dạng công cụ và quản lý tài nguyên tính toán.

### Triển khai Python

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

Trong đoạn mã trên, chúng tôi đã:

- Tạo một lớp `EnterpriseAiIntegration` tích hợp MCP với Azure ML.
- Triển khai một phương thức `execute_ml_pipeline` để xử lý dữ liệu đầu vào bằng các công cụ MCP và gửi một pipeline ML đến Azure ML.
- Triển khai một phương thức `register_ml_model_as_tool` để đăng ký một mô hình Azure ML dưới dạng công cụ MCP, bao gồm việc tạo môi trường triển khai và tài nguyên tính toán cần thiết.
- Ánh xạ các kiểu dữ liệu Azure ML sang các kiểu JSON schema để đăng ký công cụ.
- Sử dụng lập trình bất đồng bộ để xử lý các hoạt động có thể kéo dài như thực thi pipeline ML và đăng ký mô hình.

## Tiếp theo

- [5.2 Đa phương thức](../mcp-multi-modality/README.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.