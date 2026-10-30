# நிறுவன ஒருமைத்துவம்

ஒரு நிறுவன சூழலில் MCP சேவையகங்களை கட்டியெழுப்பும் போது, நீங்கள் பெரும்பாலும் உள்ளமைந்த AI தளங்களோடு மற்றும் சேவைகளோடு ஒருமைத்துவம் செய்ய தேவையிருக்கும். இந்த பகுதியில், MCP-ஐ Azure OpenAI மற்றும் Microsoft AI Foundry போன்ற நிறுவன அமைப்புகளுடன் எப்படி ஒருமை செய்யலாம் என்பதைக் கூறுகிறது, இது முன்னேற்றமான AI திறன்களையும் சாதன ஒழுங்குமுறையையும் செயல்படுத்த உதவுகிறது.

## அறிமுகம்

இந்த பாடத்தில், நீங்கள் Model Context Protocol (MCP)-ஐ Azure OpenAI மற்றும் Microsoft AI Foundry போன்ற நிறுவன AI அமைப்புகளோடு ஒருமை செய்வதற்கு கற்றுக்கொள்ளப்போகிறீர்கள். இந்த ஒருமித்தங்கள் சக்திவாய்ந்த AI மாதிரிகள் மற்றும் சாதனங்களை பயன்படுத்துவதற்கு உதவுகின்றன, அதே சமயம் MCP-இன் மென்மையான மற்றும் விரிவாக்கக்கூடிய தன்மையை காப்பாற்றுகின்றன.

## கற்றல் இலக்குகள்

இந்த பாடத்தின் முடிவில், நீங்கள் முடியும்:

- MCP-ஐ Azure OpenAI உடன் ஒருமை செய்து அதன் AI திறன்களை பயன்படுத்துதல்.
- Azure OpenAI உடன் MCP சாதன ஒழுங்குமுறையை செயல்படுத்துதல்.
- முன்னேற்றமான AI முகவர் திறன்களை வழங்க Microsoft AI Foundry உடன் MCP-ஐ இணைத்தல்.
- Azure Machine Learning (ML)-ஐ பயன்படுத்தி ML குழாய்களை இயக்கல் மற்றும் MCP சாதனங்களாக மாதிரிகளை பதிவு செய்தல்.

## Azure OpenAI ஒருமைத்துவம்

Microsoft Foundry தற்போதைய AI மாதிரிகள் போன்று GPT-5.1 க்கு அணுகலினை வழங்குகிறது.
MCP-ஐ Foundry மாதிரிகளுடன் இணைத்தல் MCP சாதன ஒழுங்குமுறையின் மென்மையான தன்மையை காப்பாற்றுகிறது
மற்றும் ஒருங்கிணைக்கப்பட்ட மாதிரி பரப்பணியை பயன்படுத்துகிறது.

### C# செயலாக்கம்

இந்த குறியீட்டில், Azure OpenAI SDK ஐ பயன்படுத்தி MCP-ஐ Azure OpenAI உடன் ஒருமைப்படுத்துவது எப்படி என்பதை விளக்குகிறோம்.

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

முன் குறியீட்டில் நாம்:

- Azure OpenAI கிளையண்டை அதின் கடைசி புள்ளி, தளவமைப்பின் பெயர் மற்றும் API விசையுடன் கட்டமைத்துள்ளோம்.
- சாதன ஆதரவுடன் முடிவுகளை பெற `GetCompletionWithToolsAsync` எனும் முறையை உருவாக்கியுள்ளோம்.
- பதிலில் சாதன அழைப்புகளை கையாளியுள்ளோம்.

உங்கள் குறிப்பிட்ட MCP சேவையக அமைப்பின் அடிப்படையில் உண்மை சாதன கையாளும் நினைவலை செயல்படுத்த அழைக்கப்படுகிறீர்கள்.

## Microsoft Foundry ஒருமைத்துவம்

Microsoft Foundry AI முகவர்களை உருவாக்கவும் செருகவும் ஒரு தளத்தை வழங்குகிறது. MCP-ஐ Microsoft Foundry உடன் இணைத்தல் அதன் திறன்களை பயன்படுத்த உதவுகிறது மற்றும் MCP-இன் மென்மையான தன்மையையும் காக்கிறது.

கீழே உள்ள குறியீட்டில், MCP பயன்படுத்தி கோரிக்கைகளை செயல்படுத்தும் மற்றும் சாதன அழைப்புகளை கையாளும் முகவர் ஒருங்கிணைப்பை உருவாக்குகிறோம்.

### ஜாவா செயலாக்கம்

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

முன் குறியீட்டில், நாம்:

- AI Foundry மற்றும் MCP இரண்டையும் ஒருங்கிணைக்கும் `AIFoundryMcpBridge` வகுப்பை உருவாக்கியுள்ளோம்.
- AI Foundry முகவர் கோரிக்கையை செயல்படுத்தும் `processAgentRequest` முறைமையை செயல்படுத்தியுள்ளோம்.
- சாதன அழைப்புகளை MCP கிளையண்ட் மூலம் இயக்கி, முடிவுகளை AI Foundry முகவருக்கு மீண்டும் அனுப்பி கையாளியுள்ளோம்.

## MCP-ஐ Azure ML உடன் ஒருமைகாரல்

MCP-ஐ Azure Machine Learning (ML) உடன் ஒருமையாக செயல்படுத்துதல் Azureன் சக்திவாய்ந்த ML திறன்களை பயன்படுத்தவும் MCP இன் மென்மையான தன்மையை காப்பாற்றவும் உதவுகிறது. இந்த ஒருமைத்து ML குழாய்களை இயக்க, மாதிரிகளை சாதனங்களாக பதிவு செய்ய மற்றும் கணினி வளங்களை நிர்வகிக்கும் பயன்பாடுகளை கொண்டுள்ளது.

### பைதான் செயலாக்கம்

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

முன் குறியீட்டில், நாம்:

- MCP-ஐ Azure ML உடன் ஒருங்கிணைக்கும் `EnterpriseAiIntegration` வகுப்பை உருவாக்கியுள்ளோம்.
- உள்ளீட்டு தரவு MCP சாதனங்களைக் கொண்டு செயல்படுத்தும் மற்றும் Azure ML க்கு ML குழாயை சமர்ப்பிக்கும் `execute_ml_pipeline` முறையை செயல்படுத்தியுள்ளோம்.
- Azure ML மாதிரியை MCP சாதனமாக பதிவு செய்யும் `register_ml_model_as_tool` முறையை உருவாக்கியுள்ளோம், தேவையான பரப்பணைப் பிணைய சூழல் மற்றும் கணினி வளங்களும் தோற்றுவிக்கப்பட்டுள்ளன.
- சாதன பதிவிற்கான JSON கட்டமைப்பிற்காக Azure ML தரவுத் தரவுகளை இடைமுகப்படுத்தியுள்ளோம்.
- ML குழாய் இயக்கம் மற்றும் மாதிரி பதிவின் நீடித்த செயல்பாடுகளை கையாள அசிங்க்ரோனஸ் நிரல் எழுதுதலை பயன்படுத்தியுள்ளோம்.

## அடுத்து என்ன

- [5.2 பன்முகத்தன்மை](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->