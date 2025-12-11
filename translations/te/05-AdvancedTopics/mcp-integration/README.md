<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f84eaea79c8fa9ab318a494f40891814",
  "translation_date": "2025-12-11T15:49:46+00:00",
  "source_file": "05-AdvancedTopics/mcp-integration/README.md",
  "language_code": "te"
}
-->
# ఎంటర్ప్రైజ్ ఇంటిగ్రేషన్

ఎంటర్ప్రైజ్ సందర్భంలో MCP సర్వర్లను నిర్మించేటప్పుడు, మీరు తరచుగా ఉన్న AI ప్లాట్‌ఫారమ్‌లు మరియు సేవలతో ఇంటిగ్రేట్ చేయాల్సి ఉంటుంది. ఈ విభాగం MCPని Azure OpenAI మరియు Microsoft AI Foundry వంటి ఎంటర్ప్రైజ్ సిస్టమ్‌లతో ఎలా ఇంటిగ్రేట్ చేయాలో కవర్ చేస్తుంది, ఇది అధునాతన AI సామర్థ్యాలు మరియు టూల్ ఆర్కెస్ట్రేషన్‌ను సాధ్యమవుతుంది.

## పరిచయం

ఈ పాఠంలో, మీరు Model Context Protocol (MCP)ని ఎంటర్ప్రైజ్ AI సిస్టమ్‌లతో, ముఖ్యంగా Azure OpenAI మరియు Microsoft AI Foundryతో ఎలా ఇంటిగ్రేట్ చేయాలో నేర్చుకుంటారు. ఈ ఇంటిగ్రేషన్లు శక్తివంతమైన AI మోడల్స్ మరియు టూల్స్‌ను ఉపయోగించడానికి అనుమతిస్తాయి, అదే సమయంలో MCP యొక్క సౌలభ్యం మరియు విస్తరణ సామర్థ్యాన్ని నిలుపుకుంటాయి.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- MCPని Azure OpenAIతో ఇంటిగ్రేట్ చేసి దాని AI సామర్థ్యాలను ఉపయోగించుకోవడం.
- Azure OpenAIతో MCP టూల్ ఆర్కెస్ట్రేషన్‌ను అమలు చేయడం.
- MCPని Microsoft AI Foundryతో కలిపి అధునాతన AI ఏజెంట్ సామర్థ్యాలను పొందడం.
- Azure Machine Learning (ML)ని ఉపయోగించి ML పైప్లైన్లను అమలు చేయడం మరియు మోడల్స్‌ను MCP టూల్స్‌గా నమోదు చేయడం.

## Azure OpenAI ఇంటిగ్రేషన్

Azure OpenAI GPT-4 మరియు ఇతర శక్తివంతమైన AI మోడల్స్‌కు ప్రాప్యతను అందిస్తుంది. MCPని Azure OpenAIతో ఇంటిగ్రేట్ చేయడం ద్వారా మీరు ఈ మోడల్స్‌ను ఉపయోగించవచ్చు, అదే సమయంలో MCP యొక్క టూల్ ఆర్కెస్ట్రేషన్ సౌలభ్యాన్ని నిలుపుకుంటారు.

### C# అమలు

ఈ కోడ్ స్నిపెట్‌లో, మేము Azure OpenAI SDK ఉపయోగించి MCPని Azure OpenAIతో ఎలా ఇంటిగ్రేట్ చేయాలో చూపిస్తున్నాము.

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

ముందటి కోడ్‌లో మేము:

- Azure OpenAI క్లయింట్‌ను ఎండ్‌పాయింట్, డిప్లాయ్‌మెంట్ పేరు మరియు API కీతో కాన్ఫిగర్ చేసాము.
- టూల్ సపోర్ట్‌తో కంప్లీషన్లు పొందడానికి `GetCompletionWithToolsAsync` అనే మెథడ్‌ను సృష్టించాము.
- ప్రతిస్పందనలో టూల్ కాల్స్‌ను హ్యాండిల్ చేసాము.

మీ ప్రత్యేక MCP సర్వర్ సెటప్ ఆధారంగా వాస్తవ టూల్ హ్యాండ్లింగ్ లాజిక్‌ను అమలు చేయమని మిమ్మల్ని ప్రోత్సహిస్తున్నాము.

## Microsoft AI Foundry ఇంటిగ్రేషన్

Azure AI Foundry AI ఏజెంట్లను నిర్మించడానికి మరియు డిప్లాయ్ చేయడానికి ఒక ప్లాట్‌ఫారమ్‌ను అందిస్తుంది. MCPని AI Foundryతో ఇంటిగ్రేట్ చేయడం ద్వారా మీరు దాని సామర్థ్యాలను ఉపయోగించవచ్చు, అదే సమయంలో MCP యొక్క సౌలభ్యాన్ని నిలుపుకుంటారు.

క్రింద ఉన్న కోడ్‌లో, మేము MCP ఉపయోగించి అభ్యర్థనలను ప్రాసెస్ చేసి టూల్ కాల్స్‌ను హ్యాండిల్ చేసే ఏజెంట్ ఇంటిగ్రేషన్‌ను అభివృద్ధి చేస్తున్నాము.

### Java అమలు

```java
// జావా AI ఫౌండ్రీ ఏజెంట్ ఇంటిగ్రేషన్
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
        // AI ఫౌండ్రీ ఏజెంట్ అభ్యర్థనను ప్రాసెస్ చేయండి
        AgentResponse initialResponse = agentClient.processRequest(request);
        
        // ఏజెంట్ టూల్స్ ఉపయోగించమని అభ్యర్థించిందా అని తనిఖీ చేయండి
        if (initialResponse.getToolCalls() != null && !initialResponse.getToolCalls().isEmpty()) {
            // ప్రతి టూల్ కాల్ కోసం, దాన్ని సరైన MCP టూల్‌కు రూట్ చేయండి
            for (AgentToolCall toolCall : initialResponse.getToolCalls()) {
                String toolName = toolCall.getName();
                Map<String, Object> parameters = toolCall.getArguments();
                
                // MCP ఉపయోగించి టూల్‌ను అమలు చేయండి
                ToolResponse mcpResponse = mcpClient.executeTool(toolName, parameters);
                
                // AI ఫౌండ్రీ కోసం టూల్ ప్రతిస్పందన సృష్టించండి
                AgentToolResponse toolResponse = new AgentToolResponse(
                    toolCall.getId(),
                    mcpResponse.getResult()
                );
                
                // టూల్ ప్రతిస్పందనను తిరిగి ఏజెంట్‌కు సమర్పించండి
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

ముందటి కోడ్‌లో మేము:

- AI Foundry మరియు MCP రెండింటితో ఇంటిగ్రేట్ అయ్యే `AIFoundryMcpBridge` క్లాస్‌ను సృష్టించాము.
- AI Foundry ఏజెంట్ అభ్యర్థనను ప్రాసెస్ చేసే `processAgentRequest` అనే మెథడ్‌ను అమలు చేసాము.
- MCP క్లయింట్ ద్వారా టూల్ కాల్స్‌ను అమలు చేసి ఫలితాలను AI Foundry ఏజెంట్‌కు తిరిగి సమర్పించడం ద్వారా టూల్ కాల్స్‌ను హ్యాండిల్ చేసాము.

## MCPని Azure MLతో ఇంటిగ్రేట్ చేయడం

MCPని Azure Machine Learning (ML)తో ఇంటిగ్రేట్ చేయడం ద్వారా మీరు Azure యొక్క శక్తివంతమైన ML సామర్థ్యాలను ఉపయోగించవచ్చు, అదే సమయంలో MCP యొక్క సౌలభ్యాన్ని నిలుపుకుంటారు. ఈ ఇంటిగ్రేషన్ ML పైప్లైన్లను అమలు చేయడానికి, మోడల్స్‌ను టూల్స్‌గా నమోదు చేయడానికి మరియు కంప్యూట్ వనరులను నిర్వహించడానికి ఉపయోగించవచ్చు.

### Python అమలు

```python
# పైథాన్ అజ్యూర్ AI ఇంటిగ్రేషన్
from mcp_client import McpClient
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment, AmlCompute
import os
import asyncio

class EnterpriseAiIntegration:
    def __init__(self, mcp_server_url, subscription_id, resource_group, workspace_name):
        # MCP క్లయింట్ సెట్ చేయండి
        self.mcp_client = McpClient(server_url=mcp_server_url)
        
        # అజ్యూర్ ML క్లయింట్ సెట్ చేయండి
        self.credential = DefaultAzureCredential()
        self.ml_client = MLClient(
            self.credential,
            subscription_id,
            resource_group,
            workspace_name
        )
    
    async def execute_ml_pipeline(self, pipeline_name, input_data):
        """Executes an ML pipeline in Azure ML"""
        # మొదట MCP టూల్స్ ఉపయోగించి ఇన్‌పుట్ డేటాను ప్రాసెస్ చేయండి
        processed_data = await self.mcp_client.execute_tool(
            "dataPreprocessor",
            {
                "data": input_data,
                "operations": ["normalize", "clean", "transform"]
            }
        )
        
        # పైప్‌లైన్‌ను అజ్యూర్ ML కు సమర్పించండి
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
        
        # జాబ్ సమాచారం తిరిగి ఇవ్వండి
        return {
            "job_id": pipeline_job.id,
            "status": pipeline_job.status,
            "creation_time": pipeline_job.creation_context.created_at
        }
    
    async def register_ml_model_as_tool(self, model_name, model_version="latest"):
        """Registers an Azure ML model as an MCP tool"""
        # మోడల్ వివరాలు పొందండి
        if model_version == "latest":
            model = self.ml_client.models.get(name=model_name, label="latest")
        else:
            model = self.ml_client.models.get(name=model_name, version=model_version)
        
        # డిప్లాయ్‌మెంట్ వాతావరణం సృష్టించండి
        env = Environment(
            name="mcp-model-env",
            conda_file="./environments/inference-env.yml"
        )
        
        # కంప్యూట్ సెట్ చేయండి
        compute = self.ml_client.compute.get("mcp-inference")
        
        # మోడల్‌ను ఆన్‌లైన్ ఎండ్‌పాయింట్‌గా డిప్లాయ్ చేయండి
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
        
        # మోడల్ స్కీమా ఆధారంగా MCP టూల్ స్కీమా సృష్టించండి
        tool_schema = {
            "type": "object",
            "properties": {},
            "required": []
        }
        
        # మోడల్ స్కీమా ఆధారంగా ఇన్‌పుట్ లక్షణాలు జోడించండి
        for input_name, input_spec in model.signature.inputs.items():
            tool_schema["properties"][input_name] = {
                "type": self._map_ml_type_to_json_type(input_spec.type)
            }
            tool_schema["required"].append(input_name)
        
        # MCP టూల్‌గా నమోదు చేయండి
        # నిజమైన అమలులో, మీరు ఎండ్‌పాయింట్‌ను కాల్ చేసే టూల్‌ను సృష్టిస్తారు
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

ముందటి కోడ్‌లో మేము:

- MCPని Azure MLతో ఇంటిగ్రేట్ చేసే `EnterpriseAiIntegration` క్లాస్‌ను సృష్టించాము.
- ఇన్‌పుట్ డేటాను MCP టూల్స్ ఉపయోగించి ప్రాసెస్ చేసి Azure MLకి ML పైప్లైన్‌ను సమర్పించే `execute_ml_pipeline` మెథడ్‌ను అమలు చేసాము.
- Azure ML మోడల్‌ను MCP టూల్‌గా నమోదు చేసే `register_ml_model_as_tool` మెథడ్‌ను అమలు చేసాము, ఇందులో అవసరమైన డిప్లాయ్‌మెంట్ వాతావరణం మరియు కంప్యూట్ వనరులను సృష్టించడం కూడా ఉంది.
- టూల్ నమోదు కోసం Azure ML డేటా రకాల్ని JSON స్కీమా రకాలుగా మ్యాప్ చేసాము.
- ML పైప్లైన్ అమలు మరియు మోడల్ నమోదు వంటి పొడవైన ఆపరేషన్లను నిర్వహించడానికి అసింక్రోనస్ ప్రోగ్రామింగ్‌ను ఉపయోగించాము.

## తదుపరి ఏమిటి

- [5.2 మల్టీ మోడాలిటీ](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->