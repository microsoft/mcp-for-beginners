# நிறுவன ஒருங்கிணைப்பு

நிறுவன சூழலில் MCP சர்வர்களை உருவாக்கும்போது, உள்ள AI தளங்கள் மற்றும் சேவைகளுடன் ஒருங்கிணைக்க வேண்டிய அவசியம் ஏற்படும். இந்த பகுதி MCP-ஐ Azure OpenAI மற்றும் Microsoft AI Foundry போன்ற நிறுவன அமைப்புகளுடன் ஒருங்கிணைப்பது குறித்து விளக்குகிறது, இது மேம்பட்ட AI திறன்கள் மற்றும் கருவி ஒருங்கிணைப்பை செயல்படுத்த உதவுகிறது.

## அறிமுகம்

இந்த பாடத்தில், Model Context Protocol (MCP)-ஐ Azure OpenAI மற்றும் Microsoft AI Foundry போன்ற நிறுவன AI அமைப்புகளுடன் ஒருங்கிணைப்பது எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள். இந்த ஒருங்கிணைப்புகள் சக்திவாய்ந்த AI மாதிரிகள் மற்றும் கருவிகளை பயன்படுத்துவதற்கு அனுமதிக்கின்றன, அதேசமயம் MCP-இன் நெகிழ்வுத்தன்மை மற்றும் விரிவாக்கத்தன்மையை பராமரிக்கின்றன.

## கற்றல் நோக்கங்கள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- Azure OpenAI-யுடன் MCP-ஐ ஒருங்கிணைத்து அதன் AI திறன்களை பயன்படுத்த முடியும்.
- Azure OpenAI-யுடன் MCP கருவி ஒருங்கிணைப்பை செயல்படுத்த முடியும்.
- மேம்பட்ட AI முகவர் திறன்களுக்காக MCP-ஐ Microsoft AI Foundry-யுடன் இணைக்க முடியும்.
- Azure Machine Learning (ML)-ஐ பயன்படுத்தி ML குழாய்கள் செயல்படுத்தவும், MCP கருவிகளாக மாதிரிகளை பதிவு செய்யவும் முடியும்.

## Azure OpenAI ஒருங்கிணைப்பு

Azure OpenAI GPT-4 போன்ற சக்திவாய்ந்த AI மாதிரிகளுக்கு அணுகலை வழங்குகிறது. MCP-ஐ Azure OpenAI-யுடன் ஒருங்கிணைப்பது, MCP-இன் கருவி ஒருங்கிணைப்பின் நெகிழ்வுத்தன்மையை பராமரிக்கும்போது இந்த மாதிரிகளை பயன்படுத்த அனுமதிக்கிறது.

### C# செயல்பாடு

இந்த குறியீட்டு துணுக்கில், Azure OpenAI SDK-ஐ பயன்படுத்தி MCP-ஐ Azure OpenAI-யுடன் ஒருங்கிணைப்பது எப்படி என்பதை விளக்குகிறோம்.

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

மேற்கண்ட குறியீட்டில், நாம்:

- Azure OpenAI கிளையண்டை முடுக்கம், பிரசார பெயர் மற்றும் API விசையுடன் அமைத்துள்ளோம்.
- `GetCompletionWithToolsAsync` என்ற முறை உருவாக்கி, கருவி ஆதரவு கொண்ட முடிவுகளை பெறுகிறோம்.
- பதிலில் உள்ள கருவி அழைப்புகளை கையாளுகிறோம்.

உங்கள் MCP சர்வர் அமைப்பின் அடிப்படையில், உண்மையான கருவி கையாளும் தற்காலிகத்தை செயல்படுத்த நீங்கள் ஊக்குவிக்கப்படுகிறீர்கள்.

## Microsoft AI Foundry ஒருங்கிணைப்பு

Azure AI Foundry AI முகவர்களை உருவாக்கவும், பரப்பவும் ஒரு தளத்தை வழங்குகிறது. MCP-ஐ AI Foundry-யுடன் ஒருங்கிணைப்பது அதன் திறன்களை பயன்படுத்த அனுமதிக்கிறது, அதேசமயம் MCP-இன் நெகிழ்வுத்தன்மையை பராமரிக்கிறது.

கீழே உள்ள குறியீட்டில், MCP-ஐ பயன்படுத்தி கோரிக்கைகளை செயல்படுத்தவும், கருவி அழைப்புகளை கையாளவும் ஒரு முகவர் ஒருங்கிணைப்பை உருவாக்குகிறோம்.

### Java செயல்பாடு

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

மேற்கண்ட குறியீட்டில், நாம்:

- AI Foundry மற்றும் MCP-இன் ஒருங்கிணைப்புடன் `AIFoundryMcpBridge` வகுப்பை உருவாக்கியுள்ளோம்.
- AI Foundry முகவர் கோரிக்கையை செயல்படுத்த `processAgentRequest` என்ற முறையை செயல்படுத்தியுள்ளோம்.
- MCP கிளையண்டை பயன்படுத்தி கருவி அழைப்புகளை செயல்படுத்தி, முடிவுகளை AI Foundry முகவருக்கு திருப்பியுள்ளோம்.

## Azure ML உடன் MCP ஒருங்கிணைப்பு

Azure Machine Learning (ML)-ஐ MCP-யுடன் ஒருங்கிணைப்பது Azure-இன் சக்திவாய்ந்த ML திறன்களை MCP-இன் நெகிழ்வுத்தன்மையை பராமரிக்கும்போது பயன்படுத்த அனுமதிக்கிறது. இந்த ஒருங்கிணைப்பு ML குழாய்களை செயல்படுத்த, MCP கருவிகளாக மாதிரிகளை பதிவு செய்ய மற்றும் கணினி வளங்களை நிர்வகிக்க பயன்படுத்தப்படலாம்.

### Python செயல்பாடு

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

மேற்கண்ட குறியீட்டில், நாம்:

- MCP-ஐ Azure ML-யுடன் ஒருங்கிணைக்கும் `EnterpriseAiIntegration` வகுப்பை உருவாக்கியுள்ளோம்.
- MCP கருவிகளைப் பயன்படுத்தி உள்ளீட்டு தரவுகளை செயல்படுத்தி, Azure ML-க்கு ML குழாயை சமர்ப்பிக்கும் `execute_ml_pipeline` முறையை செயல்படுத்தியுள்ளோம்.
- Azure ML மாதிரியை MCP கருவியாக பதிவு செய்ய `register_ml_model_as_tool` முறையை செயல்படுத்தியுள்ளோம், இதில் தேவையான பிரசார சூழல் மற்றும் கணினி வளங்களை உருவாக்குவது அடங்கும்.
- Azure ML தரவுத் வகைகளை JSON schema வகைகளுக்கு வரைபடம் செய்து கருவி பதிவுக்கு பயன்படுத்தியுள்ளோம்.
- ML குழாய் செயல்படுத்தல் மற்றும் மாதிரி பதிவு போன்ற நீண்ட நேரம் செயல்படும் செயல்பாடுகளை கையாள அசிங்க்ரோனஸ் நிரலாக்கத்தை பயன்படுத்தியுள்ளோம்.

## அடுத்தது என்ன

- [5.2 பல முறைமைகள்](../mcp-multi-modality/README.md)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.