# एंटरप्राइज़ इंटीग्रेशन

जब एंटरप्राइज़ संदर्भ में MCP सर्वर बनाते हैं, तो अक्सर मौजूदा AI प्लेटफ़ॉर्म और सेवाओं के साथ इंटीग्रेशन की आवश्यकता होती है। इस सेक्शन में, MCP को Azure OpenAI और Microsoft AI Foundry जैसे एंटरप्राइज़ सिस्टम्स के साथ इंटीग्रेट करने के तरीके बताए गए हैं, जिससे उन्नत AI क्षमताओं और टूल ऑर्केस्ट्रेशन को सक्षम किया जा सके।

## परिचय

इस पाठ में, आप सीखेंगे कि Model Context Protocol (MCP) को एंटरप्राइज़ AI सिस्टम्स के साथ कैसे इंटीग्रेट किया जाए, विशेष रूप से Azure OpenAI और Microsoft AI Foundry पर ध्यान केंद्रित करते हुए। ये इंटीग्रेशन आपको शक्तिशाली AI मॉडल और टूल्स का उपयोग करने की अनुमति देते हैं, साथ ही MCP की फ्लेक्सिबिलिटी और एक्स्टेंसिबिलिटी को बनाए रखते हैं।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- Azure OpenAI के साथ MCP को इंटीग्रेट करके उसकी AI क्षमताओं का उपयोग करना।
- Azure OpenAI के साथ MCP टूल ऑर्केस्ट्रेशन को लागू करना।
- Microsoft AI Foundry के साथ MCP को जोड़कर उन्नत AI एजेंट क्षमताओं का उपयोग करना।
- Azure Machine Learning (ML) का उपयोग करके ML पाइपलाइनों को निष्पादित करना और MCP टूल्स के रूप में मॉडल्स को रजिस्टर करना।

## Azure OpenAI इंटीग्रेशन

Azure OpenAI GPT-4 जैसे शक्तिशाली AI मॉडल्स तक पहुंच प्रदान करता है। MCP को Azure OpenAI के साथ इंटीग्रेट करने से आप इन मॉडलों का उपयोग कर सकते हैं, साथ ही MCP के टूल ऑर्केस्ट्रेशन की फ्लेक्सिबिलिटी को बनाए रख सकते हैं।

### C# इंप्लीमेंटेशन

इस कोड स्निपेट में, हम Azure OpenAI SDK का उपयोग करके MCP को Azure OpenAI के साथ इंटीग्रेट करने का तरीका दिखाते हैं।

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

उपरोक्त कोड में हमने:

- Azure OpenAI क्लाइंट को एंडपॉइंट, डिप्लॉयमेंट नाम और API कुंजी के साथ कॉन्फ़िगर किया है।
- `GetCompletionWithToolsAsync` नामक एक मेथड बनाया है, जो टूल सपोर्ट के साथ कंप्लीशन प्राप्त करता है।
- प्रतिक्रिया में टूल कॉल्स को हैंडल किया है।

आपको अपने विशेष MCP सर्वर सेटअप के आधार पर वास्तविक टूल हैंडलिंग लॉजिक को लागू करने के लिए प्रोत्साहित किया जाता है।

## Microsoft AI Foundry इंटीग्रेशन

Azure AI Foundry एक ऐसा प्लेटफ़ॉर्म प्रदान करता है जो AI एजेंट्स को बनाने और डिप्लॉय करने में मदद करता है। MCP को AI Foundry के साथ इंटीग्रेट करने से आप इसकी क्षमताओं का लाभ उठा सकते हैं, साथ ही MCP की फ्लेक्सिबिलिटी को बनाए रख सकते हैं।

नीचे दिए गए कोड में, हम एक एजेंट इंटीग्रेशन विकसित करते हैं जो अनुरोधों को प्रोसेस करता है और MCP का उपयोग करके टूल कॉल्स को हैंडल करता है।

### Java इंप्लीमेंटेशन

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

उपरोक्त कोड में हमने:

- `AIFoundryMcpBridge` नामक एक क्लास बनाई है, जो AI Foundry और MCP दोनों के साथ इंटीग्रेट करती है।
- `processAgentRequest` नामक एक मेथड को लागू किया है, जो AI Foundry एजेंट अनुरोध को प्रोसेस करता है।
- टूल कॉल्स को MCP क्लाइंट के माध्यम से निष्पादित करके और परिणामों को AI Foundry एजेंट को सबमिट करके हैंडल किया है।

## Azure ML के साथ MCP इंटीग्रेशन

Azure Machine Learning (ML) के साथ MCP को इंटीग्रेट करने से आप Azure की शक्तिशाली ML क्षमताओं का लाभ उठा सकते हैं, साथ ही MCP की फ्लेक्सिबिलिटी को बनाए रख सकते हैं। इस इंटीग्रेशन का उपयोग ML पाइपलाइनों को निष्पादित करने, मॉडल्स को टूल्स के रूप में रजिस्टर करने और कंप्यूट संसाधनों को प्रबंधित करने के लिए किया जा सकता है।

### Python इंप्लीमेंटेशन

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

उपरोक्त कोड में हमने:

- `EnterpriseAiIntegration` नामक एक क्लास बनाई है, जो MCP को Azure ML के साथ इंटीग्रेट करती है।
- `execute_ml_pipeline` नामक एक मेथड को लागू किया है, जो MCP टूल्स का उपयोग करके इनपुट डेटा को प्रोसेस करता है और Azure ML पर एक ML पाइपलाइन सबमिट करता है।
- `register_ml_model_as_tool` नामक एक मेथड को लागू किया है, जो Azure ML मॉडल को MCP टूल के रूप में रजिस्टर करता है, जिसमें आवश्यक डिप्लॉयमेंट एनवायरनमेंट और कंप्यूट संसाधन बनाना शामिल है।
- टूल रजिस्ट्रेशन के लिए Azure ML डेटा प्रकारों को JSON स्कीमा प्रकारों में मैप किया है।
- असिंक्रोनस प्रोग्रामिंग का उपयोग किया है ताकि ML पाइपलाइन निष्पादन और मॉडल रजिस्ट्रेशन जैसी संभावित लंबी प्रक्रियाओं को संभाला जा सके।

## आगे क्या करें

- [5.2 मल्टी मोडलिटी](../mcp-multi-modality/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।