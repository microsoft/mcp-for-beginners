# एंटरप्राइझ इंटिग्रेशन

एंटरप्राइझ संदर्भात MCP सर्व्हर्स तयार करताना, विद्यमान AI प्लॅटफॉर्म्स आणि सेवांसोबत एकत्रिकरण करणे आवश्यक असते. या विभागात MCP ला Azure OpenAI आणि Microsoft AI Foundry सारख्या एंटरप्राइझ सिस्टम्ससोबत कसे एकत्रित करायचे याबद्दल माहिती दिली आहे, ज्यामुळे प्रगत AI क्षमता आणि टूल ऑर्केस्ट्रेशन सक्षम होते.

## परिचय

या धड्यात तुम्ही Model Context Protocol (MCP) ला एंटरप्राइझ AI सिस्टम्ससोबत कसे एकत्रित करायचे ते शिकाल, ज्यामध्ये Azure OpenAI आणि Microsoft AI Foundry वर लक्ष केंद्रित केले आहे. या एकत्रीकरणांमुळे तुम्हाला शक्तिशाली AI मॉडेल्स आणि टूल्सचा लाभ घेता येतो, MCP च्या लवचिकता आणि विस्तारक्षमतेसह.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही खालील गोष्टी करू शकाल:

- Azure OpenAI सोबत MCP एकत्रित करून त्याच्या AI क्षमतांचा उपयोग करणे.
- Azure OpenAI सोबत MCP टूल ऑर्केस्ट्रेशन अंमलात आणणे.
- Microsoft AI Foundry सोबत MCP एकत्रित करून प्रगत AI एजंट क्षमतांचा लाभ घेणे.
- Azure Machine Learning (ML) चा उपयोग करून ML पाइपलाइन्स चालवणे आणि मॉडेल्स MCP टूल्स म्हणून नोंदवणे.

## Azure OpenAI एकत्रीकरण

Azure OpenAI GPT-4 आणि इतर शक्तिशाली AI मॉडेल्ससाठी प्रवेश प्रदान करते. MCP ला Azure OpenAI सोबत एकत्रित केल्याने तुम्हाला या मॉडेल्सचा उपयोग करता येतो, MCP च्या टूल ऑर्केस्ट्रेशनची लवचिकता टिकवून ठेवता येते.

### C# अंमलबजावणी

या कोड स्निपेटमध्ये, आम्ही Azure OpenAI SDK चा वापर करून MCP ला Azure OpenAI सोबत कसे एकत्रित करायचे ते दाखवतो.

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

वरील कोडमध्ये आम्ही:

- Azure OpenAI क्लायंटला एंडपॉइंट, डिप्लॉयमेंट नाव आणि API कीसह कॉन्फिगर केले आहे.
- `GetCompletionWithToolsAsync` नावाची पद्धत तयार केली आहे जी टूल्सच्या समर्थनासह पूर्णता मिळवते.
- प्रतिसादामध्ये टूल कॉल्स हाताळले आहेत.

तुमच्या विशिष्ट MCP सर्व्हर सेटअपच्या आधारे प्रत्यक्ष टूल हाताळणी लॉजिक अंमलात आणण्याची शिफारस केली जाते.

## Microsoft AI Foundry एकत्रीकरण

Azure AI Foundry AI एजंट्स तयार करण्यासाठी आणि तैनात करण्यासाठी एक प्लॅटफॉर्म प्रदान करते. MCP ला AI Foundry सोबत एकत्रित केल्याने तुम्हाला त्याच्या क्षमतांचा लाभ घेता येतो, MCP च्या लवचिकतेसह.

खालील कोडमध्ये, आम्ही MCP चा वापर करून विनंत्या प्रक्रिया करण्यासाठी आणि टूल कॉल्स हाताळण्यासाठी एजंट एकत्रीकरण विकसित करतो.

### Java अंमलबजावणी

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

वरील कोडमध्ये आम्ही:

- `AIFoundryMcpBridge` नावाचा वर्ग तयार केला आहे जो AI Foundry आणि MCP दोन्हींसोबत एकत्रित होतो.
- `processAgentRequest` नावाची पद्धत अंमलात आणली आहे जी AI Foundry एजंट विनंती प्रक्रिया करते.
- टूल कॉल्स MCP क्लायंटद्वारे अंमलात आणून आणि AI Foundry एजंटला निकाल परत करून हाताळले आहेत.

## Azure ML सोबत MCP एकत्रीकरण

Azure Machine Learning (ML) सोबत MCP एकत्रित केल्याने तुम्हाला Azure च्या शक्तिशाली ML क्षमतांचा लाभ घेता येतो, MCP च्या लवचिकतेसह. या एकत्रीकरणाचा उपयोग ML पाइपलाइन्स चालवण्यासाठी, मॉडेल्स टूल्स म्हणून नोंदवण्यासाठी आणि संगणन संसाधनांचे व्यवस्थापन करण्यासाठी केला जाऊ शकतो.

### Python अंमलबजावणी

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

वरील कोडमध्ये आम्ही:

- `EnterpriseAiIntegration` नावाचा वर्ग तयार केला आहे जो MCP ला Azure ML सोबत एकत्रित करतो.
- `execute_ml_pipeline` नावाची पद्धत अंमलात आणली आहे जी MCP टूल्सचा वापर करून इनपुट डेटा प्रक्रिया करते आणि Azure ML ला ML पाइपलाइन सबमिट करते.
- `register_ml_model_as_tool` नावाची पद्धत अंमलात आणली आहे जी Azure ML मॉडेल MCP टूल म्हणून नोंदवते, ज्यामध्ये आवश्यक तैनातीचे वातावरण आणि संगणन संसाधने तयार करणे समाविष्ट आहे.
- Azure ML डेटा प्रकार JSON स्कीमा प्रकारांमध्ये टूल नोंदणीसाठी मॅप केले आहेत.
- ML पाइपलाइन अंमलबजावणी आणि मॉडेल नोंदणीसारख्या संभाव्य दीर्घकालीन ऑपरेशन्स हाताळण्यासाठी असिंक्रोनस प्रोग्रामिंगचा वापर केला आहे.

## पुढे काय

- [5.2 मल्टी मोडॅलिटी](../mcp-multi-modality/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.