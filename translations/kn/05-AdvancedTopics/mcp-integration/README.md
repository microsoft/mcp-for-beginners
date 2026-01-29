# ಎಂಟರ್‌ಪ್ರೈಸ್ ಇಂಟಿಗ್ರೇಶನ್

ಎಂಟರ್‌ಪ್ರೈಸ್ ಸಂದರ್ಭದಲ್ಲಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವಾಗ, ನೀವು ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ AI ವೇದಿಕೆಗಳು ಮತ್ತು ಸೇವೆಗಳೊಂದಿಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡಬೇಕಾಗುತ್ತದೆ. ಈ ವಿಭಾಗವು MCP ಅನ್ನು ಎಂಟರ್‌ಪ್ರೈಸ್ ವ್ಯವಸ್ಥೆಗಳಾದ Azure OpenAI ಮತ್ತು Microsoft AI Foundry ಜೊತೆಗೆ ಹೇಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವುದು ಎಂಬುದನ್ನು ಒಳಗೊಂಡಿದೆ, ಇದು ಉನ್ನತ AI ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಉಪಕರಣ ಸಂಯೋಜನೆಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನೀವು Model Context Protocol (MCP) ಅನ್ನು ಎಂಟರ್‌ಪ್ರೈಸ್ AI ವ್ಯವಸ್ಥೆಗಳಾದ Azure OpenAI ಮತ್ತು Microsoft AI Foundry ಜೊತೆಗೆ ಹೇಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವುದು ಎಂಬುದನ್ನು ಕಲಿಯುತ್ತೀರಿ. ಈ ಇಂಟಿಗ್ರೇಶನ್‌ಗಳು ಶಕ್ತಿಶಾಲಿ AI ಮಾದರಿಗಳು ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಲು ಅವಕಾಶ ನೀಡುತ್ತವೆ, ಜೊತೆಗೆ MCP ಯ ಲವಚಿಕತೆ ಮತ್ತು ವಿಸ್ತರಣಾಶೀಲತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳುತ್ತವೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- MCP ಅನ್ನು Azure OpenAI ಜೊತೆಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡಿ ಅದರ AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳುವುದು.
- Azure OpenAI ಜೊತೆಗೆ MCP ಉಪಕರಣ ಸಂಯೋಜನೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು.
- MCP ಅನ್ನು Microsoft AI Foundry ಜೊತೆಗೆ ಸಂಯೋಜಿಸಿ ಉನ್ನತ AI ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಹೊಂದಿಸುವುದು.
- Azure Machine Learning (ML) ಅನ್ನು ಬಳಸಿಕೊಂಡು ML ಪೈಪ್ಲೈನ್ಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು ಮತ್ತು ಮಾದರಿಗಳನ್ನು MCP ಉಪಕರಣಗಳಾಗಿ ನೋಂದಾಯಿಸುವುದು.

## Azure OpenAI ಇಂಟಿಗ್ರೇಶನ್

Azure OpenAI GPT-4 ಮತ್ತು ಇತರ ಶಕ್ತಿಶಾಲಿ AI ಮಾದರಿಗಳಿಗೆ ಪ್ರವೇಶವನ್ನು ಒದಗಿಸುತ್ತದೆ. MCP ಅನ್ನು Azure OpenAI ಜೊತೆಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವುದರಿಂದ ನೀವು ಈ ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಬಹುದು, ಜೊತೆಗೆ MCP ಯ ಉಪಕರಣ ಸಂಯೋಜನೆಯ ಲವಚಿಕತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಬಹುದು.

### C# ಅನುಷ್ಠಾನ

ಈ ಕೋಡ್ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು Azure OpenAI SDK ಬಳಸಿ MCP ಅನ್ನು Azure OpenAI ಜೊತೆಗೆ ಹೇಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವುದು ಎಂಬುದನ್ನು ತೋರಿಸುತ್ತೇವೆ.

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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- Azure OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಎಂಡ್‌ಪಾಯಿಂಟ್, ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಹೆಸರು ಮತ್ತು API ಕೀ ಬಳಸಿ ಸಂರಚಿಸಿದ್ದೇವೆ.
- `GetCompletionWithToolsAsync` ಎಂಬ ವಿಧಾನವನ್ನು ರಚಿಸಿ ಉಪಕರಣ ಬೆಂಬಲದೊಂದಿಗೆ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳನ್ನು ಪಡೆಯುವಂತೆ ಮಾಡಿದ್ದೇವೆ.
- ಪ್ರತಿಕ್ರಿಯೆಯಲ್ಲಿ ಉಪಕರಣ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸಿದ್ದೇವೆ.

ನಿಮ್ಮ ವಿಶೇಷ MCP ಸರ್ವರ್ ಸೆಟ್ಟಪ್ ಆಧಾರಿತವಾಗಿ ನಿಜವಾದ ಉಪಕರಣ ನಿರ್ವಹಣಾ ಲಾಜಿಕ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಪ್ರೋತ್ಸಾಹಿಸಲಾಗಿದೆ.

## Microsoft AI Foundry ಇಂಟಿಗ್ರೇಶನ್

Azure AI Foundry AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಮತ್ತು ನಿಯೋಜಿಸಲು ವೇದಿಕೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ. MCP ಅನ್ನು AI Foundry ಜೊತೆಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವುದರಿಂದ ನೀವು ಅದರ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಬಹುದು, ಜೊತೆಗೆ MCP ಯ ಲವಚಿಕತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಬಹುದು.

ಕೆಳಗಿನ ಕೋಡ್‌ನಲ್ಲಿ, ನಾವು MCP ಬಳಸಿ ವಿನಂತಿಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವ ಮತ್ತು ಉಪಕರಣ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಏಜೆಂಟ್ ಇಂಟಿಗ್ರೇಶನ್ ಅನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸುತ್ತೇವೆ.

### ಜಾವಾ ಅನುಷ್ಠಾನ

```java
// ಜಾವಾ AI ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ಏಕೀಕರಣ
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
        // AI ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ವಿನಂತಿಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ
        AgentResponse initialResponse = agentClient.processRequest(request);
        
        // ಏಜೆಂಟ್ ಸಾಧನಗಳನ್ನು ಬಳಸಲು ವಿನಂತಿಸಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
        if (initialResponse.getToolCalls() != null && !initialResponse.getToolCalls().isEmpty()) {
            // ಪ್ರತಿ ಸಾಧನ ಕರೆಗಾಗಿ, ಅದನ್ನು ಸೂಕ್ತ MCP ಸಾಧನಕ್ಕೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡಿ
            for (AgentToolCall toolCall : initialResponse.getToolCalls()) {
                String toolName = toolCall.getName();
                Map<String, Object> parameters = toolCall.getArguments();
                
                // MCP ಬಳಸಿ ಸಾಧನವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
                ToolResponse mcpResponse = mcpClient.executeTool(toolName, parameters);
                
                // AI ಫೌಂಡ್ರಿಗಾಗಿ ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ರಚಿಸಿ
                AgentToolResponse toolResponse = new AgentToolResponse(
                    toolCall.getId(),
                    mcpResponse.getResult()
                );
                
                // ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಏಜೆಂಟ್‌ಗೆ ಹಿಂತಿರುಗಿಸಿ ಸಲ್ಲಿಸಿ
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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- AI Foundry ಮತ್ತು MCP ಎರಡರನ್ನೂ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವ `AIFoundryMcpBridge` ಕ್ಲಾಸ್ ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ.
- AI Foundry ಏಜೆಂಟ್ ವಿನಂತಿಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವ `processAgentRequest` ವಿಧಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿದ್ದೇವೆ.
- MCP ಕ್ಲೈಂಟ್ ಮೂಲಕ ಉಪಕರಣಗಳನ್ನು ನಿರ್ವಹಿಸಿ ಫಲಿತಾಂಶಗಳನ್ನು AI Foundry ಏಜೆಂಟ್‌ಗೆ ಹಿಂತಿರುಗಿಸಿದ್ದೇವೆ.

## MCP ಅನ್ನು Azure ML ಜೊತೆಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವುದು

MCP ಅನ್ನು Azure Machine Learning (ML) ಜೊತೆಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವುದರಿಂದ ನೀವು Azure ಯ ಶಕ್ತಿಶಾಲಿ ML ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಬಹುದು, ಜೊತೆಗೆ MCP ಯ ಲವಚಿಕತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಬಹುದು. ಈ ಇಂಟಿಗ್ರೇಶನ್ ML ಪೈಪ್ಲೈನ್ಗಳನ್ನು ನಿರ್ವಹಿಸಲು, ಮಾದರಿಗಳನ್ನು ಉಪಕರಣಗಳಾಗಿ ನೋಂದಾಯಿಸಲು ಮತ್ತು ಗಣನೆ ಸಂಪನ್ಮೂಲಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸಬಹುದು.

### ಪೈಥಾನ್ ಅನುಷ್ಠಾನ

```python
# ಪೈಥಾನ್ ಅಜೂರ್ ಎಐ ಸಂಯೋಜನೆ
from mcp_client import McpClient
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment, AmlCompute
import os
import asyncio

class EnterpriseAiIntegration:
    def __init__(self, mcp_server_url, subscription_id, resource_group, workspace_name):
        # MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
        self.mcp_client = McpClient(server_url=mcp_server_url)
        
        # ಅಜೂರ್ ಎಂಎಲ್ ಕ್ಲೈಂಟ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
        self.credential = DefaultAzureCredential()
        self.ml_client = MLClient(
            self.credential,
            subscription_id,
            resource_group,
            workspace_name
        )
    
    async def execute_ml_pipeline(self, pipeline_name, input_data):
        """Executes an ML pipeline in Azure ML"""
        # ಮೊದಲು ಇನ್‌ಪುಟ್ ಡೇಟಾವನ್ನು MCP ಉಪಕರಣಗಳ ಮೂಲಕ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ
        processed_data = await self.mcp_client.execute_tool(
            "dataPreprocessor",
            {
                "data": input_data,
                "operations": ["normalize", "clean", "transform"]
            }
        )
        
        # ಪೈಪ್‌ಲೈನ್ ಅನ್ನು ಅಜೂರ್ ಎಂಎಲ್ ಗೆ ಸಲ್ಲಿಸಿ
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
        
        # ಕೆಲಸದ ಮಾಹಿತಿಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
        return {
            "job_id": pipeline_job.id,
            "status": pipeline_job.status,
            "creation_time": pipeline_job.creation_context.created_at
        }
    
    async def register_ml_model_as_tool(self, model_name, model_version="latest"):
        """Registers an Azure ML model as an MCP tool"""
        # ಮಾದರಿ ವಿವರಗಳನ್ನು ಪಡೆಯಿರಿ
        if model_version == "latest":
            model = self.ml_client.models.get(name=model_name, label="latest")
        else:
            model = self.ml_client.models.get(name=model_name, version=model_version)
        
        # ನಿಯೋಜನೆ ಪರಿಸರವನ್ನು ರಚಿಸಿ
        env = Environment(
            name="mcp-model-env",
            conda_file="./environments/inference-env.yml"
        )
        
        # ಗಣನೆ ವ್ಯವಸ್ಥೆಯನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
        compute = self.ml_client.compute.get("mcp-inference")
        
        # ಮಾದರಿಯನ್ನು ಆನ್‌ಲೈನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಆಗಿ ನಿಯೋಜಿಸಿ
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
        
        # ಮಾದರಿ ಸ್ಕೀಮಾ ಆಧಾರಿತವಾಗಿ MCP ಉಪಕರಣ ಸ್ಕೀಮಾ ರಚಿಸಿ
        tool_schema = {
            "type": "object",
            "properties": {},
            "required": []
        }
        
        # ಮಾದರಿ ಸ್ಕೀಮಾ ಆಧಾರಿತವಾಗಿ ಇನ್‌ಪುಟ್ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಸೇರಿಸಿ
        for input_name, input_spec in model.signature.inputs.items():
            tool_schema["properties"][input_name] = {
                "type": self._map_ml_type_to_json_type(input_spec.type)
            }
            tool_schema["required"].append(input_name)
        
        # MCP ಉಪಕರಣವಾಗಿ ನೋಂದಣಿ ಮಾಡಿ
        # ನಿಜವಾದ ಅನುಷ್ಠಾನದಲ್ಲಿ, ನೀವು ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಕರೆ ಮಾಡುವ ಉಪಕರಣವನ್ನು ರಚಿಸುವಿರಿ
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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಅನ್ನು Azure ML ಜೊತೆಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡುವ `EnterpriseAiIntegration` ಕ್ಲಾಸ್ ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ.
- MCP ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಡೇಟಾವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವ ಮತ್ತು Azure ML ಗೆ ML ಪೈಪ್ಲೈನ್ ಸಲ್ಲಿಸುವ `execute_ml_pipeline` ವಿಧಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿದ್ದೇವೆ.
- Azure ML ಮಾದರಿಯನ್ನು MCP ಉಪಕರಣವಾಗಿ ನೋಂದಾಯಿಸುವ `register_ml_model_as_tool` ವಿಧಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿದ್ದೇವೆ, ಇದರಲ್ಲಿ ಅಗತ್ಯವಿರುವ ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಪರಿಸರ ಮತ್ತು ಗಣನೆ ಸಂಪನ್ಮೂಲಗಳನ್ನು ರಚಿಸುವುದೂ ಸೇರಿದೆ.
- ಉಪಕರಣ ನೋಂದಾಯಿಸಲು Azure ML ಡೇಟಾ ಪ್ರಕಾರಗಳನ್ನು JSON ಸ್ಕೀಮಾ ಪ್ರಕಾರಗಳಿಗೆ ನಕ್ಷೆ ಮಾಡಿದ್ದೇವೆ.
- ML ಪೈಪ್ಲೈನ್ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾದರಿ ನೋಂದಾಯಿಸುವಂತಹ ದೀರ್ಘಕಾಲಿಕ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಬಳಸಿದ್ದೇವೆ.

## ಮುಂದೇನು

- [5.2 ಮಲ್ಟಿ ಮೋಡಾಲಿಟಿ](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->