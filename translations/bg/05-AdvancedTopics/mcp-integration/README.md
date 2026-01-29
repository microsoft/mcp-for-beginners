# Интеграция в предприятието

При изграждането на MCP сървъри в контекста на предприятие често се налага интеграция със съществуващи AI платформи и услуги. Тази секция обхваща как да интегрирате MCP със системи като Azure OpenAI и Microsoft AI Foundry, за да активирате разширени AI възможности и оркестрация на инструменти.

## Въведение

В този урок ще научите как да интегрирате Model Context Protocol (MCP) с корпоративни AI системи, като се фокусирате върху Azure OpenAI и Microsoft AI Foundry. Тези интеграции ви позволяват да използвате мощни AI модели и инструменти, като същевременно запазвате гъвкавостта и разширяемостта на MCP.

## Цели на обучението

До края на този урок ще можете да:

- Интегрирате MCP с Azure OpenAI, за да използвате неговите AI възможности.
- Реализирате оркестрация на инструменти в MCP с Azure OpenAI.
- Комбинирате MCP с Microsoft AI Foundry за разширени възможности на AI агенти.
- Използвате Azure Machine Learning (ML) за изпълнение на ML пайплайни и регистриране на модели като MCP инструменти.

## Интеграция с Azure OpenAI

Azure OpenAI предоставя достъп до мощни AI модели като GPT-4 и други. Интеграцията на MCP с Azure OpenAI ви позволява да използвате тези модели, като същевременно запазвате гъвкавостта на оркестрацията на инструменти в MCP.

### Имплементация на C#

В този кодов фрагмент демонстрираме как да интегрирате MCP с Azure OpenAI, използвайки Azure OpenAI SDK.

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

В горния код сме:

- Конфигурирали Azure OpenAI клиента с крайна точка, име на разгръщане и API ключ.
- Създали метод `GetCompletionWithToolsAsync` за получаване на отговори с поддръжка на инструменти.
- Обработили извикванията на инструменти в отговора.

Препоръчваме ви да имплементирате действителната логика за обработка на инструменти според конкретната настройка на вашия MCP сървър.

## Интеграция с Microsoft AI Foundry

Azure AI Foundry предоставя платформа за изграждане и разгръщане на AI агенти. Интеграцията на MCP с AI Foundry ви позволява да използвате неговите възможности, като същевременно запазвате гъвкавостта на MCP.

В кода по-долу разработваме интеграция на агент, който обработва заявки и управлява извиквания на инструменти чрез MCP.

### Имплементация на Java

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

В горния код сме:

- Създали клас `AIFoundryMcpBridge`, който интегрира както AI Foundry, така и MCP.
- Имплементирали метод `processAgentRequest`, който обработва заявки на агент от AI Foundry.
- Обработили извикванията на инструменти, като ги изпълняваме чрез MCP клиента и връщаме резултатите обратно към агента на AI Foundry.

## Интеграция на MCP с Azure ML

Интеграцията на MCP с Azure Machine Learning (ML) ви позволява да използвате мощните ML възможности на Azure, като същевременно запазвате гъвкавостта на MCP. Тази интеграция може да се използва за изпълнение на ML пайплайни, регистриране на модели като инструменти и управление на изчислителни ресурси.

### Имплементация на Python

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

В горния код сме:

- Създали клас `EnterpriseAiIntegration`, който интегрира MCP с Azure ML.
- Имплементирали метод `execute_ml_pipeline`, който обработва входни данни чрез MCP инструменти и изпраща ML пайплайн към Azure ML.
- Имплементирали метод `register_ml_model_as_tool`, който регистрира ML модел от Azure като MCP инструмент, включително създаване на необходимата среда за разгръщане и изчислителни ресурси.
- Картирали типовете данни на Azure ML към JSON схеми за регистрация на инструменти.
- Използвали асинхронно програмиране за обработка на потенциално дълготрайни операции като изпълнение на ML пайплайни и регистрация на модели.

## Какво следва

- [5.2 Мултимодалност](../mcp-multi-modality/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.