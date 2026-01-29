# Інтеграція в корпоративному середовищі

Під час створення MCP-серверів у корпоративному контексті часто виникає необхідність інтеграції з існуючими платформами та сервісами штучного інтелекту. У цьому розділі розглядається, як інтегрувати MCP із корпоративними системами, такими як Azure OpenAI та Microsoft AI Foundry, для забезпечення розширених можливостей штучного інтелекту та оркестрації інструментів.

## Вступ

У цьому уроці ви дізнаєтеся, як інтегрувати Протокол Контексту Моделі (MCP) із корпоративними системами штучного інтелекту, зосереджуючись на Azure OpenAI та Microsoft AI Foundry. Ці інтеграції дозволяють використовувати потужні моделі та інструменти штучного інтелекту, зберігаючи при цьому гнучкість і розширюваність MCP.

## Цілі навчання

До кінця цього уроку ви зможете:

- Інтегрувати MCP з Azure OpenAI для використання його можливостей штучного інтелекту.
- Реалізувати оркестрацію інструментів MCP за допомогою Azure OpenAI.
- Поєднувати MCP із Microsoft AI Foundry для розширених можливостей агентів штучного інтелекту.
- Використовувати Azure Machine Learning (ML) для виконання ML-пайплайнів і реєстрації моделей як інструментів MCP.

## Інтеграція з Azure OpenAI

Azure OpenAI надає доступ до потужних моделей штучного інтелекту, таких як GPT-4 та інших. Інтеграція MCP з Azure OpenAI дозволяє використовувати ці моделі, зберігаючи при цьому гнучкість оркестрації інструментів MCP.

### Реалізація на C#

У цьому фрагменті коду ми демонструємо, як інтегрувати MCP з Azure OpenAI за допомогою SDK Azure OpenAI.

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

У наведеному коді ми:

- Налаштували клієнт Azure OpenAI з використанням кінцевої точки, імені розгортання та ключа API.
- Створили метод `GetCompletionWithToolsAsync` для отримання завершень із підтримкою інструментів.
- Обробили виклики інструментів у відповіді.

Рекомендується реалізувати фактичну логіку обробки інструментів відповідно до вашої конкретної конфігурації MCP-сервера.

## Інтеграція з Microsoft AI Foundry

Azure AI Foundry надає платформу для створення та розгортання агентів штучного інтелекту. Інтеграція MCP з AI Foundry дозволяє використовувати його можливості, зберігаючи при цьому гнучкість MCP.

У наведеному нижче коді ми розробляємо інтеграцію агента, яка обробляє запити та виклики інструментів за допомогою MCP.

### Реалізація на Java

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

У наведеному коді ми:

- Створили клас `AIFoundryMcpBridge`, який інтегрується як з AI Foundry, так і з MCP.
- Реалізували метод `processAgentRequest`, який обробляє запит агента AI Foundry.
- Обробили виклики інструментів, виконуючи їх через клієнт MCP і передаючи результати назад агенту AI Foundry.

## Інтеграція MCP з Azure ML

Інтеграція MCP з Azure Machine Learning (ML) дозволяє використовувати потужні можливості ML Azure, зберігаючи при цьому гнучкість MCP. Ця інтеграція може використовуватися для виконання ML-пайплайнів, реєстрації моделей як інструментів і управління обчислювальними ресурсами.

### Реалізація на Python

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

У наведеному коді ми:

- Створили клас `EnterpriseAiIntegration`, який інтегрує MCP з Azure ML.
- Реалізували метод `execute_ml_pipeline`, який обробляє вхідні дані за допомогою інструментів MCP і надсилає ML-пайплайн до Azure ML.
- Реалізували метод `register_ml_model_as_tool`, який реєструє модель Azure ML як інструмент MCP, включаючи створення необхідного середовища розгортання та обчислювальних ресурсів.
- Здійснили відображення типів даних Azure ML у типи JSON-схеми для реєстрації інструментів.
- Використали асинхронне програмування для обробки потенційно тривалих операцій, таких як виконання ML-пайплайнів і реєстрація моделей.

## Що далі

- [5.2 Багатомодальність](../mcp-multi-modality/README.md)

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.