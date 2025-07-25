<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "73240f845b99df9401fffd21c09a5f7b",
  "translation_date": "2025-07-16T23:25:19+00:00",
  "source_file": "05-AdvancedTopics/mcp-integration/README.md",
  "language_code": "ru"
}
-->
# Корпоративная интеграция

При создании MCP серверов в корпоративной среде часто требуется интеграция с существующими AI платформами и сервисами. В этом разделе рассматривается, как интегрировать MCP с корпоративными системами, такими как Azure OpenAI и Microsoft AI Foundry, что позволяет использовать расширенные возможности ИИ и оркестрацию инструментов.

## Введение

В этом уроке вы узнаете, как интегрировать Model Context Protocol (MCP) с корпоративными AI системами, с акцентом на Azure OpenAI и Microsoft AI Foundry. Эти интеграции позволяют использовать мощные AI модели и инструменты, сохраняя при этом гибкость и расширяемость MCP.

## Цели обучения

К концу этого урока вы сможете:

- Интегрировать MCP с Azure OpenAI для использования его AI возможностей.
- Реализовать оркестрацию инструментов MCP с Azure OpenAI.
- Совместно использовать MCP с Microsoft AI Foundry для расширенных возможностей AI агентов.
- Использовать Azure Machine Learning (ML) для выполнения ML пайплайнов и регистрации моделей в качестве инструментов MCP.

## Интеграция с Azure OpenAI

Azure OpenAI предоставляет доступ к мощным AI моделям, таким как GPT-4 и другим. Интеграция MCP с Azure OpenAI позволяет использовать эти модели, сохраняя гибкость оркестрации инструментов MCP.

### Реализация на C#

В этом фрагменте кода показано, как интегрировать MCP с Azure OpenAI с помощью Azure OpenAI SDK.

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

В приведённом выше коде мы:

- Настроили клиент Azure OpenAI с указанием конечной точки, имени развертывания и API ключа.
- Создали метод `GetCompletionWithToolsAsync` для получения ответов с поддержкой инструментов.
- Обработали вызовы инструментов в ответе.

Рекомендуется реализовать логику обработки инструментов в соответствии с вашей конкретной конфигурацией MCP сервера.

## Интеграция с Microsoft AI Foundry

Azure AI Foundry предоставляет платформу для создания и развертывания AI агентов. Интеграция MCP с AI Foundry позволяет использовать её возможности, сохраняя гибкость MCP.

В приведённом ниже коде мы разрабатываем интеграцию агента, который обрабатывает запросы и управляет вызовами инструментов с помощью MCP.

### Реализация на Java

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

В приведённом выше коде мы:

- Создали класс `AIFoundryMcpBridge`, который интегрируется как с AI Foundry, так и с MCP.
- Реализовали метод `processAgentRequest`, который обрабатывает запрос агента AI Foundry.
- Обработали вызовы инструментов, выполняя их через MCP клиент и отправляя результаты обратно агенту AI Foundry.

## Интеграция MCP с Azure ML

Интеграция MCP с Azure Machine Learning (ML) позволяет использовать мощные возможности Azure ML, сохраняя гибкость MCP. Эта интеграция может применяться для выполнения ML пайплайнов, регистрации моделей в качестве инструментов и управления вычислительными ресурсами.

### Реализация на Python

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

В приведённом выше коде мы:

- Создали класс `EnterpriseAiIntegration`, который интегрирует MCP с Azure ML.
- Реализовали метод `execute_ml_pipeline`, который обрабатывает входные данные с помощью инструментов MCP и запускает ML пайплайн в Azure ML.
- Реализовали метод `register_ml_model_as_tool`, который регистрирует модель Azure ML в качестве инструмента MCP, включая создание необходимой среды развертывания и вычислительных ресурсов.
- Выполнили сопоставление типов данных Azure ML с типами JSON схемы для регистрации инструментов.
- Использовали асинхронное программирование для обработки потенциально длительных операций, таких как выполнение ML пайплайнов и регистрация моделей.

## Что дальше

- [5.2 Мультимодальность](../mcp-multi-modality/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.