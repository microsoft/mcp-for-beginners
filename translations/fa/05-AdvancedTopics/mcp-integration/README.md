# یکپارچه‌سازی سازمانی

هنگام ساخت سرورهای MCP در یک محیط سازمانی، اغلب نیاز به یکپارچه‌سازی با پلتفرم‌ها و خدمات هوش مصنوعی موجود دارید. این بخش به نحوه یکپارچه‌سازی MCP با سیستم‌های سازمانی مانند Azure OpenAI و Microsoft AI Foundry می‌پردازد که قابلیت‌های پیشرفته هوش مصنوعی و هماهنگی ابزارها را ممکن می‌سازد.

## مقدمه

در این درس، یاد خواهید گرفت که چگونه پروتکل Model Context Protocol (MCP) را با سیستم‌های هوش مصنوعی سازمانی، با تمرکز بر Azure OpenAI و Microsoft AI Foundry، یکپارچه کنید. این یکپارچه‌سازی‌ها به شما امکان می‌دهند از مدل‌ها و ابزارهای قدرتمند هوش مصنوعی بهره ببرید و در عین حال انعطاف‌پذیری و قابلیت گسترش MCP را حفظ کنید.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- MCP را با Azure OpenAI یکپارچه کنید تا از قابلیت‌های هوش مصنوعی آن استفاده کنید.
- هماهنگی ابزار MCP را با Azure OpenAI پیاده‌سازی کنید.
- MCP را با Microsoft AI Foundry برای قابلیت‌های پیشرفته عامل هوش مصنوعی ترکیب کنید.
- از Azure Machine Learning (ML) برای اجرای پایپ‌لاین‌های ML و ثبت مدل‌ها به عنوان ابزارهای MCP استفاده کنید.

## یکپارچه‌سازی Azure OpenAI

Azure OpenAI دسترسی به مدل‌های قدرتمند هوش مصنوعی مانند GPT-4 و دیگر مدل‌ها را فراهم می‌کند. یکپارچه‌سازی MCP با Azure OpenAI به شما امکان می‌دهد از این مدل‌ها استفاده کنید و در عین حال انعطاف‌پذیری هماهنگی ابزار MCP را حفظ کنید.

### پیاده‌سازی در C#

در این قطعه کد، نحوه یکپارچه‌سازی MCP با Azure OpenAI با استفاده از Azure OpenAI SDK نشان داده شده است.

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

در کد بالا ما:

- کلاینت Azure OpenAI را با نقطه پایانی، نام استقرار و کلید API پیکربندی کرده‌ایم.
- یک متد `GetCompletionWithToolsAsync` برای دریافت تکمیل‌ها با پشتیبانی ابزار ایجاد کرده‌ایم.
- فراخوانی ابزارها را در پاسخ مدیریت کرده‌ایم.

توصیه می‌شود منطق واقعی مدیریت ابزار را بر اساس تنظیمات خاص سرور MCP خود پیاده‌سازی کنید.

## یکپارچه‌سازی Microsoft AI Foundry

Azure AI Foundry یک پلتفرم برای ساخت و استقرار عوامل هوش مصنوعی فراهم می‌کند. یکپارچه‌سازی MCP با AI Foundry به شما امکان می‌دهد از قابلیت‌های آن بهره ببرید و در عین حال انعطاف‌پذیری MCP را حفظ کنید.

در کد زیر، یک یکپارچه‌سازی عامل توسعه داده‌ایم که درخواست‌ها را پردازش کرده و فراخوانی ابزارها را با استفاده از MCP مدیریت می‌کند.

### پیاده‌سازی در Java

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

در کد بالا ما:

- یک کلاس `AIFoundryMcpBridge` ایجاد کرده‌ایم که با هر دو AI Foundry و MCP یکپارچه می‌شود.
- یک متد `processAgentRequest` پیاده‌سازی کرده‌ایم که یک درخواست عامل AI Foundry را پردازش می‌کند.
- فراخوانی ابزارها را با اجرای آن‌ها از طریق کلاینت MCP و ارسال نتایج به عامل AI Foundry مدیریت کرده‌ایم.

## یکپارچه‌سازی MCP با Azure ML

یکپارچه‌سازی MCP با Azure Machine Learning (ML) به شما امکان می‌دهد از قابلیت‌های قدرتمند ML Azure بهره ببرید و در عین حال انعطاف‌پذیری MCP را حفظ کنید. این یکپارچه‌سازی می‌تواند برای اجرای پایپ‌لاین‌های ML، ثبت مدل‌ها به عنوان ابزار و مدیریت منابع محاسباتی استفاده شود.

### پیاده‌سازی در Python

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

در کد بالا ما:

- یک کلاس `EnterpriseAiIntegration` ایجاد کرده‌ایم که MCP را با Azure ML یکپارچه می‌کند.
- یک متد `execute_ml_pipeline` پیاده‌سازی کرده‌ایم که داده‌های ورودی را با استفاده از ابزارهای MCP پردازش کرده و یک پایپ‌لاین ML را به Azure ML ارسال می‌کند.
- یک متد `register_ml_model_as_tool` پیاده‌سازی کرده‌ایم که یک مدل Azure ML را به عنوان یک ابزار MCP ثبت می‌کند، شامل ایجاد محیط استقرار و منابع محاسباتی لازم.
- انواع داده‌های Azure ML را به انواع JSON schema برای ثبت ابزار نگاشت کرده‌ایم.
- از برنامه‌نویسی غیرهمزمان برای مدیریت عملیات بالقوه طولانی مانند اجرای پایپ‌لاین ML و ثبت مدل استفاده کرده‌ایم.

## گام‌های بعدی

- [5.2 چندوجهی بودن](../mcp-multi-modality/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.