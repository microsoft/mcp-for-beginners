# इन्टरप्राइज इन्टिग्रेशन

इन्टरप्राइज सन्दर्भमा MCP सर्भरहरू निर्माण गर्दा, प्रायः तपाईंले विद्यमान AI प्लेटफर्महरू र सेवाहरूसँग इन्टिग्रेट गर्नुपर्ने हुन्छ। यो खण्डले Azure OpenAI र Microsoft AI Foundry जस्ता इन्टरप्राइज प्रणालीहरूसँग MCP कसरी इन्टिग्रेट गर्ने भन्ने कुरा समेट्छ, जसले उन्नत AI क्षमताहरू र उपकरणहरूको समन्वयलाई सक्षम बनाउँछ।

## परिचय

यस पाठमा, तपाईंले Model Context Protocol (MCP) लाई इन्टरप्राइज AI प्रणालीहरूसँग, विशेष गरी Azure OpenAI र Microsoft AI Foundry सँग कसरी इन्टिग्रेट गर्ने भन्ने कुरा सिक्नुहुनेछ। यी इन्टिग्रेशनहरूले तपाईंलाई शक्तिशाली AI मोडेलहरू र उपकरणहरूको फाइदा लिन अनुमति दिन्छ, जबकि MCP को लचिलोपन र विस्तारयोग्यता कायम राख्छ।

## सिकाइका उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईंले निम्न कार्यहरू गर्न सक्षम हुनुहुनेछ:

- Azure OpenAI सँग MCP इन्टिग्रेट गरेर यसको AI क्षमताहरू प्रयोग गर्नुहोस्।
- Azure OpenAI सँग MCP उपकरण समन्वय कार्यान्वयन गर्नुहोस्।
- Microsoft AI Foundry सँग MCP संयोजन गरेर उन्नत AI एजेन्ट क्षमताहरू प्रयोग गर्नुहोस्।
- Azure Machine Learning (ML) लाई प्रयोग गरेर ML पाइपलाइनहरू कार्यान्वयन गर्नुहोस् र मोडेलहरू MCP उपकरणको रूपमा दर्ता गर्नुहोस्।

## Azure OpenAI इन्टिग्रेशन

Azure OpenAI ले GPT-4 जस्ता शक्तिशाली AI मोडेलहरूमा पहुँच प्रदान गर्दछ। MCP लाई Azure OpenAI सँग इन्टिग्रेट गर्दा, तपाईंले यी मोडेलहरूको फाइदा लिन सक्नुहुन्छ, जबकि MCP को उपकरण समन्वयको लचिलोपन कायम राख्न सक्नुहुन्छ।

### C# कार्यान्वयन

तलको कोड स्निपेटमा, हामी Azure OpenAI SDK प्रयोग गरेर MCP लाई Azure OpenAI सँग कसरी इन्टिग्रेट गर्ने देखाउँछौं।

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

माथिको कोडमा हामीले:

- Azure OpenAI क्लाइन्टलाई एन्डपोइन्ट, डिप्लोयमेन्ट नाम, र API कुञ्जीको साथ कन्फिगर गरेका छौं।
- `GetCompletionWithToolsAsync` नामक मेथड सिर्जना गरेका छौं, जसले उपकरणहरूको समर्थनसहित कम्प्लिसन प्राप्त गर्दछ।
- प्रतिक्रिया भित्र उपकरण कलहरू ह्यान्डल गरेका छौं।

तपाईंलाई आफ्नो विशेष MCP सर्भर सेटअपको आधारमा वास्तविक उपकरण ह्यान्डलिङ तर्क कार्यान्वयन गर्न प्रोत्साहित गरिन्छ।

## Microsoft AI Foundry इन्टिग्रेशन

Azure AI Foundry ले AI एजेन्टहरू निर्माण र डिप्लोय गर्नका लागि प्लेटफर्म प्रदान गर्दछ। MCP लाई AI Foundry सँग इन्टिग्रेट गर्दा, तपाईंले यसको क्षमताहरूको फाइदा लिन सक्नुहुन्छ, जबकि MCP को लचिलोपन कायम राख्न सक्नुहुन्छ।

तलको कोडमा, हामीले एउटा एजेन्ट इन्टिग्रेशन विकास गरेका छौं, जसले अनुरोधहरू प्रक्रिया गर्छ र MCP प्रयोग गरेर उपकरण कलहरू ह्यान्डल गर्छ।

### Java कार्यान्वयन

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

माथिको कोडमा, हामीले:

- `AIFoundryMcpBridge` नामक कक्षा सिर्जना गरेका छौं, जसले AI Foundry र MCP दुवैसँग इन्टिग्रेट गर्छ।
- `processAgentRequest` नामक मेथड कार्यान्वयन गरेका छौं, जसले AI Foundry एजेन्ट अनुरोध प्रक्रिया गर्छ।
- उपकरण कलहरू MCP क्लाइन्टमार्फत कार्यान्वयन गरेर र परिणामहरू AI Foundry एजेन्टमा फिर्ता पठाएर ह्यान्डल गरेका छौं।

## Azure ML सँग MCP इन्टिग्रेशन

Azure Machine Learning (ML) सँग MCP इन्टिग्रेट गर्दा, तपाईंले Azure को शक्तिशाली ML क्षमताहरूको फाइदा लिन सक्नुहुन्छ, जबकि MCP को लचिलोपन कायम राख्न सक्नुहुन्छ। यो इन्टिग्रेशन ML पाइपलाइनहरू कार्यान्वयन गर्न, मोडेलहरू उपकरणको रूपमा दर्ता गर्न, र कम्प्युट स्रोतहरू व्यवस्थापन गर्न प्रयोग गर्न सकिन्छ।

### Python कार्यान्वयन

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

माथिको कोडमा, हामीले:

- `EnterpriseAiIntegration` नामक कक्षा सिर्जना गरेका छौं, जसले MCP लाई Azure ML सँग इन्टिग्रेट गर्छ।
- `execute_ml_pipeline` नामक मेथड कार्यान्वयन गरेका छौं, जसले MCP उपकरणहरू प्रयोग गरेर इनपुट डाटा प्रक्रिया गर्छ र Azure ML मा ML पाइपलाइन सबमिट गर्छ।
- `register_ml_model_as_tool` नामक मेथड कार्यान्वयन गरेका छौं, जसले Azure ML मोडेललाई MCP उपकरणको रूपमा दर्ता गर्छ, जसमा आवश्यक डिप्लोयमेन्ट वातावरण र कम्प्युट स्रोतहरू सिर्जना गर्ने समावेश छ।
- उपकरण दर्ताका लागि Azure ML डाटा प्रकारहरूलाई JSON स्किमामा म्याप गरेका छौं।
- ML पाइपलाइन कार्यान्वयन र मोडेल दर्ता जस्ता सम्भावित लामो समय लाग्ने अपरेसनहरू ह्यान्डल गर्न असिन्क्रोनस प्रोग्रामिङ प्रयोग गरेका छौं।

## अब के गर्ने

- [5.2 मल्टि मोडालिटी](../mcp-multi-modality/README.md)

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।