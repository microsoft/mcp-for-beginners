# Unternehmensintegration

Beim Aufbau von MCP-Servern im Unternehmenskontext müssen Sie häufig bestehende KI-Plattformen und -Dienste integrieren. In diesem Abschnitt erfahren Sie, wie Sie MCP mit Unternehmenssystemen wie Azure OpenAI und Microsoft AI Foundry integrieren können, um fortschrittliche KI-Funktionen und Tool-Orchestrierung zu ermöglichen.

## Einführung

In dieser Lektion lernen Sie, wie Sie das Model Context Protocol (MCP) mit Unternehmens-KI-Systemen integrieren, wobei der Schwerpunkt auf Azure OpenAI und Microsoft AI Foundry liegt. Diese Integrationen ermöglichen es Ihnen, leistungsstarke KI-Modelle und Tools zu nutzen, während Sie die Flexibilität und Erweiterbarkeit von MCP beibehalten.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- MCP mit Azure OpenAI zu integrieren, um dessen KI-Funktionen zu nutzen.
- MCP-Tool-Orchestrierung mit Azure OpenAI umzusetzen.
- MCP mit Microsoft AI Foundry zu kombinieren, um fortschrittliche KI-Agenten-Funktionen zu ermöglichen.
- Azure Machine Learning (ML) zu nutzen, um ML-Pipelines auszuführen und Modelle als MCP-Tools zu registrieren.

## Azure OpenAI-Integration

Azure OpenAI bietet Zugriff auf leistungsstarke KI-Modelle wie GPT-4 und andere. Die Integration von MCP mit Azure OpenAI ermöglicht es Ihnen, diese Modelle zu nutzen und gleichzeitig die Flexibilität der MCP-Tool-Orchestrierung beizubehalten.

### C#-Implementierung

In diesem Codebeispiel zeigen wir, wie MCP mit Azure OpenAI unter Verwendung des Azure OpenAI SDK integriert werden kann.

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

Im obigen Code haben wir:

- Den Azure OpenAI-Client mit Endpunkt, Bereitstellungsnamen und API-Schlüssel konfiguriert.
- Eine Methode `GetCompletionWithToolsAsync` erstellt, um Abschlüsse mit Tool-Unterstützung zu erhalten.
- Tool-Aufrufe in der Antwort verarbeitet.

Es wird empfohlen, die tatsächliche Logik zur Tool-Verarbeitung basierend auf Ihrer spezifischen MCP-Server-Konfiguration zu implementieren.

## Microsoft AI Foundry-Integration

Azure AI Foundry bietet eine Plattform zum Erstellen und Bereitstellen von KI-Agenten. Die Integration von MCP mit AI Foundry ermöglicht es Ihnen, dessen Funktionen zu nutzen und gleichzeitig die Flexibilität von MCP beizubehalten.

Im folgenden Code entwickeln wir eine Agenten-Integration, die Anfragen verarbeitet und Tool-Aufrufe mithilfe von MCP bearbeitet.

### Java-Implementierung

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

Im obigen Code haben wir:

- Eine Klasse `AIFoundryMcpBridge` erstellt, die sowohl mit AI Foundry als auch mit MCP integriert ist.
- Eine Methode `processAgentRequest` implementiert, die eine Anfrage eines AI Foundry-Agenten verarbeitet.
- Tool-Aufrufe bearbeitet, indem sie über den MCP-Client ausgeführt und die Ergebnisse an den AI Foundry-Agenten zurückgesendet werden.

## Integration von MCP mit Azure ML

Die Integration von MCP mit Azure Machine Learning (ML) ermöglicht es Ihnen, die leistungsstarken ML-Funktionen von Azure zu nutzen und gleichzeitig die Flexibilität von MCP beizubehalten. Diese Integration kann verwendet werden, um ML-Pipelines auszuführen, Modelle als Tools zu registrieren und Rechenressourcen zu verwalten.

### Python-Implementierung

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

Im obigen Code haben wir:

- Eine Klasse `EnterpriseAiIntegration` erstellt, die MCP mit Azure ML integriert.
- Eine Methode `execute_ml_pipeline` implementiert, die Eingabedaten mithilfe von MCP-Tools verarbeitet und eine ML-Pipeline an Azure ML übermittelt.
- Eine Methode `register_ml_model_as_tool` implementiert, die ein Azure ML-Modell als MCP-Tool registriert, einschließlich der Erstellung der erforderlichen Bereitstellungsumgebung und Rechenressourcen.
- Azure ML-Datentypen auf JSON-Schema-Typen für die Tool-Registrierung abgebildet.
- Asynchrone Programmierung verwendet, um potenziell langwierige Vorgänge wie die Ausführung von ML-Pipelines und die Modellregistrierung zu handhaben.

## Was kommt als Nächstes

- [5.2 Multi-Modality](../mcp-multi-modality/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.