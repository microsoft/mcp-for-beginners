# Podniková integrace

Při vytváření MCP serverů v podnikových prostředích je často potřeba integrovat je s existujícími AI platformami a službami. Tato sekce se zabývá tím, jak integrovat MCP s podnikovými systémy, jako jsou Azure OpenAI a Microsoft AI Foundry, a umožnit tak pokročilé AI schopnosti a orchestraci nástrojů.

## Úvod

V této lekci se naučíte, jak integrovat Model Context Protocol (MCP) s podnikovými AI systémy, se zaměřením na Azure OpenAI a Microsoft AI Foundry. Tyto integrace vám umožní využívat výkonné AI modely a nástroje, přičemž si zachováte flexibilitu a rozšiřitelnost MCP.

## Cíle učení

Na konci této lekce budete schopni:

- Integrovat MCP s Azure OpenAI a využívat jeho AI schopnosti.
- Implementovat orchestraci nástrojů MCP s Azure OpenAI.
- Kombinovat MCP s Microsoft AI Foundry pro pokročilé schopnosti AI agentů.
- Využívat Azure Machine Learning (ML) k provádění ML pipeline a registraci modelů jako nástrojů MCP.

## Integrace Azure OpenAI

Azure OpenAI poskytuje přístup k výkonným AI modelům, jako je GPT-4 a další. Integrace MCP s Azure OpenAI vám umožní využívat tyto modely a zároveň si zachovat flexibilitu orchestrací nástrojů MCP.

### Implementace v C#

V tomto ukázkovém kódu demonstrujeme, jak integrovat MCP s Azure OpenAI pomocí Azure OpenAI SDK.

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

V předchozím kódu jsme:

- Nakonfigurovali klienta Azure OpenAI s endpointem, názvem nasazení a API klíčem.
- Vytvořili metodu `GetCompletionWithToolsAsync` pro získání odpovědí s podporou nástrojů.
- Zpracovali volání nástrojů v odpovědi.

Doporučujeme implementovat vlastní logiku pro zpracování nástrojů na základě specifického nastavení vašeho MCP serveru.

## Integrace Microsoft AI Foundry

Azure AI Foundry poskytuje platformu pro vytváření a nasazování AI agentů. Integrace MCP s AI Foundry vám umožní využívat jeho schopnosti a zároveň si zachovat flexibilitu MCP.

V níže uvedeném kódu vyvíjíme integraci agenta, který zpracovává požadavky a volání nástrojů pomocí MCP.

### Implementace v Javě

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

V předchozím kódu jsme:

- Vytvořili třídu `AIFoundryMcpBridge`, která integruje AI Foundry a MCP.
- Implementovali metodu `processAgentRequest`, která zpracovává požadavky agenta AI Foundry.
- Zpracovali volání nástrojů jejich provedením prostřednictvím klienta MCP a odesláním výsledků zpět agentovi AI Foundry.

## Integrace MCP s Azure ML

Integrace MCP s Azure Machine Learning (ML) vám umožní využívat výkonné ML schopnosti Azure a zároveň si zachovat flexibilitu MCP. Tato integrace může být použita k provádění ML pipeline, registraci modelů jako nástrojů a správě výpočetních zdrojů.

### Implementace v Pythonu

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

V předchozím kódu jsme:

- Vytvořili třídu `EnterpriseAiIntegration`, která integruje MCP s Azure ML.
- Implementovali metodu `execute_ml_pipeline`, která zpracovává vstupní data pomocí nástrojů MCP a odesílá ML pipeline do Azure ML.
- Implementovali metodu `register_ml_model_as_tool`, která registruje model Azure ML jako nástroj MCP, včetně vytvoření potřebného prostředí pro nasazení a výpočetních zdrojů.
- Mapovali datové typy Azure ML na typy JSON schématu pro registraci nástrojů.
- Použili asynchronní programování pro zpracování potenciálně dlouhotrvajících operací, jako je provádění ML pipeline a registrace modelů.

## Co dál

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.