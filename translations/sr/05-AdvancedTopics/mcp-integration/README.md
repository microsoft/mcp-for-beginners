# Ентерпрајз интеграција

Када креирате MCP сервере у контексту предузећа, често је потребно интегрисати их са постојећим AI платформама и услугама. Овај одељак покрива како интегрисати MCP са системима као што су Azure OpenAI и Microsoft AI Foundry, омогућавајући напредне AI могућности и оркестрацију алата.

## Увод

У овој лекцији ћете научити како да интегришете Model Context Protocol (MCP) са AI системима у предузећима, са фокусом на Azure OpenAI и Microsoft AI Foundry. Ове интеграције вам омогућавају да искористите моћне AI моделе и алате, уз задржавање флексибилности и проширивости MCP-а.

## Циљеви учења

На крају ове лекције, бићете у могућности да:

- Интегришете MCP са Azure OpenAI ради коришћења његових AI могућности.
- Имплементирате оркестрацију алата MCP-а са Azure OpenAI.
- Комбинујете MCP са Microsoft AI Foundry за напредне могућности AI агената.
- Искористите Azure Machine Learning (ML) за извршавање ML цевовода и регистрацију модела као MCP алата.

## Интеграција са Azure OpenAI

Azure OpenAI пружа приступ моћним AI моделима као што је GPT-4 и други. Интеграција MCP-а са Azure OpenAI омогућава вам да користите ове моделе уз задржавање флексибилности оркестрације алата MCP-а.

### Имплементација у C#

У овом делу кода демонстрирамо како интегрисати MCP са Azure OpenAI користећи Azure OpenAI SDK.

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

У претходном коду смо:

- Конфигурисали Azure OpenAI клијент са крајњом тачком, именом деплоја и API кључем.
- Креирали метод `GetCompletionWithToolsAsync` за добијање комплета са подршком за алате.
- Обрадили позиве алата у одговору.

Препоручује се да имплементирате стварну логику обраде алата на основу специфичне конфигурације вашег MCP сервера.

## Интеграција са Microsoft AI Foundry

Azure AI Foundry пружа платформу за креирање и деплојовање AI агената. Интеграција MCP-а са AI Foundry омогућава вам да искористите његове могућности уз задржавање флексибилности MCP-а.

У следећем коду развијамо интеграцију агента која обрађује захтеве и управља позивима алата користећи MCP.

### Имплементација у Јави

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

У претходном коду смо:

- Креирали класу `AIFoundryMcpBridge` која интегрише AI Foundry и MCP.
- Имплементирали метод `processAgentRequest` који обрађује захтеве AI Foundry агента.
- Управљали позивима алата извршавајући их преко MCP клијента и враћајући резултате назад AI Foundry агенту.

## Интеграција MCP-а са Azure ML

Интеграција MCP-а са Azure Machine Learning (ML) омогућава вам да искористите моћне ML могућности Azure-а уз задржавање флексибилности MCP-а. Ова интеграција може се користити за извршавање ML цевовода, регистрацију модела као алата и управљање ресурсима за рачунање.

### Имплементација у Пајтону

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

У претходном коду смо:

- Креирали класу `EnterpriseAiIntegration` која интегрише MCP са Azure ML.
- Имплементирали метод `execute_ml_pipeline` који обрађује улазне податке користећи MCP алате и шаље ML цевовод Azure ML-у.
- Имплементирали метод `register_ml_model_as_tool` који региструје Azure ML модел као MCP алат, укључујући креирање неопходног окружења за деплојовање и ресурса за рачунање.
- Мапирали Azure ML типове података на JSON шеме за регистрацију алата.
- Користили асинхроно програмирање за обраду потенцијално дуготрајних операција као што су извршавање ML цевовода и регистрација модела.

## Шта следи

- [5.2 Вишемодалност](../mcp-multi-modality/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из коришћења овог превода.