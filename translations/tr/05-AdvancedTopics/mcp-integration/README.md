# Kurumsal Entegrasyon

Kurumsal bağlamda MCP Sunucuları oluştururken, genellikle mevcut yapay zeka platformları ve hizmetleriyle entegrasyon sağlamanız gerekir. Bu bölüm, MCP'yi Azure OpenAI ve Microsoft AI Foundry gibi kurumsal sistemlerle entegre ederek gelişmiş yapay zeka yetenekleri ve araç orkestrasyonu sağlamayı ele alır.

## Giriş

Bu derste, Model Context Protocol (MCP)'yi Azure OpenAI ve Microsoft AI Foundry gibi kurumsal yapay zeka sistemleriyle nasıl entegre edeceğinizi öğreneceksiniz. Bu entegrasyonlar, güçlü yapay zeka modelleri ve araçlardan yararlanmanıza olanak tanırken MCP'nin esnekliğini ve genişletilebilirliğini korumanızı sağlar.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- MCP'yi Azure OpenAI ile entegre ederek yapay zeka yeteneklerinden yararlanmak.
- MCP araç orkestrasyonunu Azure OpenAI ile uygulamak.
- MCP'yi Microsoft AI Foundry ile birleştirerek gelişmiş yapay zeka ajan yetenekleri sağlamak.
- Azure Machine Learning (ML)'i kullanarak ML iş akışlarını çalıştırmak ve modelleri MCP araçları olarak kaydetmek.

## Azure OpenAI Entegrasyonu

Azure OpenAI, GPT-4 gibi güçlü yapay zeka modellerine erişim sağlar. MCP'yi Azure OpenAI ile entegre etmek, bu modellerden yararlanmanıza olanak tanırken MCP'nin araç orkestrasyonunun esnekliğini korur.

### C# Uygulaması

Bu kod örneğinde, Azure OpenAI SDK kullanarak MCP'yi Azure OpenAI ile nasıl entegre edeceğimizi gösteriyoruz.

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

Yukarıdaki kodda şunları yaptık:

- Azure OpenAI istemcisini uç nokta, dağıtım adı ve API anahtarı ile yapılandırdık.
- Araç desteği ile tamamlama almak için `GetCompletionWithToolsAsync` adlı bir yöntem oluşturduk.
- Yanıttaki araç çağrılarını ele aldık.

Kendi MCP sunucu kurulumunuza göre araç işleme mantığını uygulamanız önerilir.

## Microsoft AI Foundry Entegrasyonu

Azure AI Foundry, yapay zeka ajanları oluşturmak ve dağıtmak için bir platform sağlar. MCP'yi AI Foundry ile entegre etmek, MCP'nin esnekliğini korurken bu platformun yeteneklerinden yararlanmanıza olanak tanır.

Aşağıdaki kodda, MCP kullanarak istekleri işleyen ve araç çağrılarını ele alan bir Ajan entegrasyonu geliştiriyoruz.

### Java Uygulaması

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

Yukarıdaki kodda şunları yaptık:

- Hem AI Foundry hem de MCP ile entegre olan bir `AIFoundryMcpBridge` sınıfı oluşturduk.
- AI Foundry ajan isteğini işleyen bir `processAgentRequest` yöntemi uyguladık.
- Araç çağrılarını MCP istemcisi aracılığıyla çalıştırarak ve sonuçları AI Foundry ajanına geri göndererek ele aldık.

## MCP'yi Azure ML ile Entegre Etmek

MCP'yi Azure Machine Learning (ML) ile entegre etmek, Azure'un güçlü ML yeteneklerinden yararlanmanıza olanak tanırken MCP'nin esnekliğini korur. Bu entegrasyon, ML iş akışlarını çalıştırmak, modelleri araç olarak kaydetmek ve hesaplama kaynaklarını yönetmek için kullanılabilir.

### Python Uygulaması

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

Yukarıdaki kodda şunları yaptık:

- MCP'yi Azure ML ile entegre eden bir `EnterpriseAiIntegration` sınıfı oluşturduk.
- MCP araçlarını kullanarak giriş verilerini işleyen ve Azure ML'ye bir ML iş akışı gönderen bir `execute_ml_pipeline` yöntemi uyguladık.
- Azure ML modelini MCP aracı olarak kaydeden, gerekli dağıtım ortamını ve hesaplama kaynaklarını oluşturan bir `register_ml_model_as_tool` yöntemi uyguladık.
- Azure ML veri türlerini araç kaydı için JSON şema türlerine eşledik.
- ML iş akışı çalıştırma ve model kaydı gibi uzun sürebilecek işlemleri ele almak için asenkron programlama kullandık.

## Sıradaki Adımlar

- [5.2 Çok Modluluk](../mcp-multi-modality/README.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.