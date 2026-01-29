# Vállalati Integráció

Amikor MCP szervereket építünk vállalati környezetben, gyakran szükség van a meglévő AI platformokkal és szolgáltatásokkal való integrációra. Ez a rész bemutatja, hogyan integrálható az MCP olyan vállalati rendszerekkel, mint az Azure OpenAI és a Microsoft AI Foundry, lehetővé téve fejlett AI képességek és eszközök összehangolását.

## Bevezetés

Ebben a leckében megtanulod, hogyan integrálható a Model Context Protocol (MCP) vállalati AI rendszerekkel, különös tekintettel az Azure OpenAI-ra és a Microsoft AI Foundry-ra. Ezek az integrációk lehetővé teszik, hogy erőteljes AI modelleket és eszközöket használj, miközben megőrzöd az MCP rugalmasságát és bővíthetőségét.

## Tanulási célok

A lecke végére képes leszel:

- Integrálni az MCP-t az Azure OpenAI-val, hogy kihasználhasd annak AI képességeit.
- Megvalósítani az MCP eszközök összehangolását az Azure OpenAI-val.
- Kombinálni az MCP-t a Microsoft AI Foundry-val fejlett AI ügynök képességek érdekében.
- Kihasználni az Azure Machine Learning (ML) lehetőségeit ML folyamatok végrehajtására és modellek MCP eszközként való regisztrálására.

## Azure OpenAI integráció

Az Azure OpenAI hozzáférést biztosít olyan erőteljes AI modellekhez, mint például a GPT-4 és mások. Az MCP és az Azure OpenAI integrációja lehetővé teszi ezeknek a modelleknek a használatát, miközben megőrzöd az MCP eszközök összehangolásának rugalmasságát.

### C# megvalósítás

Az alábbi kódrészlet bemutatja, hogyan integrálható az MCP az Azure OpenAI-val az Azure OpenAI SDK használatával.

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

A fenti kódban:

- Konfiguráltuk az Azure OpenAI klienst az endpoint, a telepítési név és az API kulcs megadásával.
- Létrehoztunk egy `GetCompletionWithToolsAsync` metódust, amely eszköztámogatással kér le kiegészítéseket.
- Kezeltük az eszköz hívásokat a válaszban.

Javasoljuk, hogy az eszközkezelési logikát a saját MCP szerver beállításaid alapján valósítsd meg.

## Microsoft AI Foundry integráció

Az Azure AI Foundry egy platformot biztosít AI ügynökök építésére és telepítésére. Az MCP és az AI Foundry integrációja lehetővé teszi, hogy kihasználhasd annak képességeit, miközben megőrzöd az MCP rugalmasságát.

Az alábbi kódban egy ügynök integrációt fejlesztünk, amely kéréseket dolgoz fel és eszköz hívásokat kezel az MCP segítségével.

### Java megvalósítás

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

A fenti kódban:

- Létrehoztunk egy `AIFoundryMcpBridge` osztályt, amely integrálja az AI Foundry-t és az MCP-t.
- Megvalósítottunk egy `processAgentRequest` metódust, amely feldolgozza az AI Foundry ügynök kéréseit.
- Kezeltük az eszköz hívásokat azáltal, hogy azokat az MCP kliensen keresztül hajtjuk végre, és az eredményeket visszaküldjük az AI Foundry ügynöknek.

## MCP integráció az Azure ML-lel

Az MCP és az Azure Machine Learning (ML) integrációja lehetővé teszi, hogy kihasználhasd az Azure erőteljes ML képességeit, miközben megőrzöd az MCP rugalmasságát. Ez az integráció használható ML folyamatok végrehajtására, modellek eszközként való regisztrálására és számítási erőforrások kezelésére.

### Python megvalósítás

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

A fenti kódban:

- Létrehoztunk egy `EnterpriseAiIntegration` osztályt, amely integrálja az MCP-t az Azure ML-lel.
- Megvalósítottunk egy `execute_ml_pipeline` metódust, amely MCP eszközök segítségével dolgozza fel a bemeneti adatokat, és ML folyamatot küld be az Azure ML-nek.
- Megvalósítottunk egy `register_ml_model_as_tool` metódust, amely egy Azure ML modellt regisztrál MCP eszközként, beleértve a szükséges telepítési környezet és számítási erőforrások létrehozását.
- Leképeztük az Azure ML adattípusokat JSON séma típusokra az eszköz regisztrációhoz.
- Aszinkron programozást használtunk a potenciálisan hosszú ideig tartó műveletek, például ML folyamatok végrehajtása és modellek regisztrálása kezelésére.

## Hogyan tovább

- [5.2 Többmodalitás](../mcp-multi-modality/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.