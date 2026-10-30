# Интеграција у предузећима

Када правите МЦП сервере у контексту предузећа, често треба да их интегришете са постојећим AI платформама и услугама. Овај одељак обрађује како интегрисати МЦП са системима за предузећа као што су Azure OpenAI и Microsoft AI Foundry, омогућавајући напредне AI могућности и оркестрацију алата.

## Увод

У овој лекцији ћете научити како да интегришете Model Context Protocol (МЦП) са AI системима за предузећа, са фокусом на Azure OpenAI и Microsoft AI Foundry. Ове интеграције вам омогућавају да користите моћне AI моделе и алате док одржавате флексибилност и проширивост МЦП-а.

## Циљеви учења

До краја ове лекције ћете бити у могућности да:

- Интегришете МЦП са Azure OpenAI како бисте користили његове AI могућности.
- Имплементирате оркестрацију МЦП алата са Azure OpenAI.
- Комбинујете МЦП са Microsoft AI Foundry ради напредних AI могућности агената.
- Искористите Azure Machine Learning (ML) за извођење ML цевовода и регистрацију модела као МЦП алата.

## Интеграција Azure OpenAI

Microsoft Foundry пружа приступ актуелним AI моделима као што је GPT-5.1.
Интегрисање МЦП са Foundry моделима задржава флексибилност оркестрације МЦП алата
док користи управљано распоређивање модела.

### C# имплементација

У овом делу кода демонстрирамо како интегрисати МЦП са Azure OpenAI користећи Azure OpenAI SDK.

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

- Конфигурисали Azure OpenAI клијента са крајњом тачком, именом распоређивања и API кључем.
- Креирали метод `GetCompletionWithToolsAsync` за добијање допуна са подршком алата.
- Обрадили позиве алата у одговору.

Похаљавамо вас да имплементирате стварну логику за руковање алатима на основу ваше специфичне МЦП сервер конфигурације.

## Интеграција Microsoft Foundry

Microsoft Foundry пружа платформу за изградњу и распоређивање AI агената. Интеграција МЦП-а са Microsoft Foundry омогућава вам да искористите његове могућности док одржавате флексибилност МЦП-а.

У доњем коду развијамо интеграцију агента која процесуира захтеве и рукује позиве алата користећи МЦП.

### Java имплементација

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

- Креирали класу `AIFoundryMcpBridge` која интегрише и AI Foundry и МЦП.
- Имплементирали метод `processAgentRequest` који процесуира захтев AI Foundry агента.
- Обрадили позиве алата тако што смо их извршили преко МЦП клијента и вратили резултате AI Foundry агенту.

## Интеграција МЦП са Azure ML

Интеграција МЦП-а са Azure Machine Learning (ML) омогућава вам да искористите моћне ML могућности Azure-а док одржавате флексибилност МЦП-а. Ова интеграција се може користити за извођење ML цевовода, регистрацију модела као алата и управљање ресурсима за обраду.

### Python имплементација

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

- Креирали класу `EnterpriseAiIntegration` која интегрише МЦП са Azure ML.
- Имплементирали метод `execute_ml_pipeline` који процесуира улазне податке користећи МЦП алате и шаље ML цевовод Azure ML-у.
- Имплементирали метод `register_ml_model_as_tool` који региструје Azure ML модел као МЦП алат, укључујући креирање потребног окружења за разврставање и ресурса за обраду.
- Мапирали Azure ML типове података у JSON скему за регистрацију алата.
- Користили асинхрони програмски модел за руковање потенцијално дугорочним операцијама као што су извођење ML цевовода и регистрација модела.

## Шта следи

- [5.2 Мултимодалност](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->