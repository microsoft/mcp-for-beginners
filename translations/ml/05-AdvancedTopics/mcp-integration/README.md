# എന്റർപ്രൈസ് ഇന്റഗ്രേഷൻ

എന്റർപ്രൈസ് സാഹചര്യത്തിൽ MCP സർവറുകൾ നിർമ്മിക്കുമ്പോൾ, നിലവിലുള്ള AI പ്ലാറ്റ്ഫോമുകളുമായും സേവനങ്ങളുമായും ഇന്റഗ്രേറ്റ് ചെയ്യേണ്ടതുണ്ടാകാറുണ്ട്. ഈ വിഭാഗം MCP-നെ Azure OpenAI, Microsoft AI Foundry പോലുള്ള എന്റർപ്രൈസ് സിസ്റ്റങ്ങളുമായി എങ്ങനെ ഇന്റഗ്രേറ്റ് ചെയ്യാമെന്ന് വിശദീകരിക്കുന്നു, അതിലൂടെ ആധുനിക AI കഴിവുകളും ടൂൾ ഓർക്കസ്ട്രേഷനും സാധ്യമാക്കുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ, നിങ്ങൾ Model Context Protocol (MCP) എന്റർപ്രൈസ് AI സിസ്റ്റങ്ങളുമായി, പ്രത്യേകിച്ച് Azure OpenAI, Microsoft AI Foundry എന്നിവയുമായി എങ്ങനെ ഇന്റഗ്രേറ്റ് ചെയ്യാമെന്ന് പഠിക്കും. ഈ ഇന്റഗ്രേഷനുകൾ ശക്തമായ AI മോഡലുകളും ടൂളുകളും ഉപയോഗപ്പെടുത്താൻ സഹായിക്കുന്നതോടൊപ്പം MCP-യുടെ ഫ്ലെക്സിബിലിറ്റിയും വിപുലീകരണ ശേഷിയും നിലനിർത്തുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിക്കുമ്പോൾ, നിങ്ങൾക്ക് കഴിയും:

- MCP-നെ Azure OpenAI-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് അതിന്റെ AI കഴിവുകൾ ഉപയോഗപ്പെടുത്തുക.
- Azure OpenAI-യുമായി MCP ടൂൾ ഓർക്കസ്ട്രേഷൻ നടപ്പിലാക്കുക.
- MCP-നെ Microsoft AI Foundry-യുമായി സംയോജിപ്പിച്ച് ആധുനിക AI ഏജന്റ് കഴിവുകൾ പ്രാപിക്കുക.
- Azure Machine Learning (ML) ഉപയോഗിച്ച് ML പൈപ്പ്ലൈനുകൾ നടപ്പിലാക്കുകയും മോഡലുകൾ MCP ടൂളുകളായി രജിസ്റ്റർ ചെയ്യുകയും ചെയ്യുക.

## Azure OpenAI ഇന്റഗ്രേഷൻ

Azure OpenAI GPT-4 പോലുള്ള ശക്തമായ AI മോഡലുകളിലേക്ക് ആക്‌സസ് നൽകുന്നു. MCP-നെ Azure OpenAI-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുന്നത് ഈ മോഡലുകൾ ഉപയോഗപ്പെടുത്താൻ സഹായിക്കുന്നതോടൊപ്പം MCP-യുടെ ടൂൾ ഓർക്കസ്ട്രേഷൻ ഫ്ലെക്സിബിലിറ്റിയും നിലനിർത്തുന്നു.

### C# നടപ്പാക്കൽ

ഈ കോഡ് സ്നിപ്പറ്റിൽ, Azure OpenAI SDK ഉപയോഗിച്ച് MCP-നെ Azure OpenAI-യുമായി എങ്ങനെ ഇന്റഗ്രേറ്റ് ചെയ്യാമെന്ന് കാണിക്കുന്നു.

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

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- Azure OpenAI ക്ലയന്റിനെ എൻഡ്‌പോയിന്റ്, ഡിപ്ലോയ്മെന്റ് നാമം, API കീ എന്നിവ ഉപയോഗിച്ച് കോൺഫിഗർ ചെയ്തു.
- ടൂൾ പിന്തുണയോടെ പൂർത്തീകരണങ്ങൾ നേടാൻ `GetCompletionWithToolsAsync` എന്ന മെത്തഡ് സൃഷ്ടിച്ചു.
- പ്രതികരണത്തിൽ ടൂൾ കോളുകൾ കൈകാര്യം ചെയ്തു.

നിങ്ങളുടെ പ്രത്യേക MCP സർവർ ക്രമീകരണത്തിന്റെ അടിസ്ഥാനത്തിൽ യഥാർത്ഥ ടൂൾ കൈകാര്യം ചെയ്യൽ ലജിക് നടപ്പിലാക്കാൻ പ്രോത്സാഹിപ്പിക്കുന്നു.

## Microsoft AI Foundry ഇന്റഗ്രേഷൻ

Azure AI Foundry AI ഏജന്റുകൾ നിർമ്മിക്കുകയും ഡിപ്ലോയുചെയ്യുകയും ചെയ്യാനുള്ള പ്ലാറ്റ്ഫോം നൽകുന്നു. MCP-നെ AI Foundry-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുന്നത് അതിന്റെ കഴിവുകൾ ഉപയോഗപ്പെടുത്താൻ സഹായിക്കുന്നതോടൊപ്പം MCP-യുടെ ഫ്ലെക്സിബിലിറ്റിയും നിലനിർത്തുന്നു.

താഴെ കൊടുത്തിരിക്കുന്ന കോഡിൽ, MCP ഉപയോഗിച്ച് അഭ്യർത്ഥനകൾ പ്രോസസ്സ് ചെയ്ത് ടൂൾ കോളുകൾ കൈകാര്യം ചെയ്യുന്ന ഒരു ഏജന്റ് ഇന്റഗ്രേഷൻ വികസിപ്പിക്കുന്നു.

### ജാവ നടപ്പാക്കൽ

```java
// ജാവ എഐ ഫൗണ്ട്രി ഏജന്റ് ഇന്റഗ്രേഷൻ
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
        // എഐ ഫൗണ്ട്രി ഏജന്റ് അഭ്യർത്ഥന പ്രോസസ്സ് ചെയ്യുക
        AgentResponse initialResponse = agentClient.processRequest(request);
        
        // ഏജന്റ് ടൂളുകൾ ഉപയോഗിക്കാൻ അഭ്യർത്ഥിച്ചിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക
        if (initialResponse.getToolCalls() != null && !initialResponse.getToolCalls().isEmpty()) {
            // ഓരോ ടൂൾ കോൾക്കും അനുയോജ്യമായ MCP ടൂളിലേക്ക് റൂട്ടുചെയ്യുക
            for (AgentToolCall toolCall : initialResponse.getToolCalls()) {
                String toolName = toolCall.getName();
                Map<String, Object> parameters = toolCall.getArguments();
                
                // MCP ഉപയോഗിച്ച് ടൂൾ പ്രവർത്തിപ്പിക്കുക
                ToolResponse mcpResponse = mcpClient.executeTool(toolName, parameters);
                
                // എഐ ഫൗണ്ട്രിക്ക് ടൂൾ പ്രതികരണം സൃഷ്ടിക്കുക
                AgentToolResponse toolResponse = new AgentToolResponse(
                    toolCall.getId(),
                    mcpResponse.getResult()
                );
                
                // ടൂൾ പ്രതികരണം വീണ്ടും ഏജന്റിന് സമർപ്പിക്കുക
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- AI Foundry-യുമായും MCP-യുമായും ഇന്റഗ്രേറ്റ് ചെയ്യുന്ന `AIFoundryMcpBridge` ക്ലാസ് സൃഷ്ടിച്ചു.
- AI Foundry ഏജന്റ് അഭ്യർത്ഥന പ്രോസസ്സ് ചെയ്യുന്ന `processAgentRequest` മെത്തഡ് നടപ്പിലാക്കി.
- MCP ക്ലയന്റ് വഴി ടൂൾ കോളുകൾ നടപ്പിലാക്കി ഫലങ്ങൾ AI Foundry ഏജന്റിന് തിരികെ സമർപ്പിച്ചു.

## MCP-നെ Azure ML-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്യൽ

MCP-നെ Azure Machine Learning (ML) ഉപയോഗിച്ച് ഇന്റഗ്രേറ്റ് ചെയ്യുന്നത് Azure-യുടെ ശക്തമായ ML കഴിവുകൾ ഉപയോഗപ്പെടുത്താൻ സഹായിക്കുന്നു, MCP-യുടെ ഫ്ലെക്സിബിലിറ്റിയും നിലനിർത്തുന്നു. ഈ ഇന്റഗ്രേഷൻ ML പൈപ്പ്ലൈനുകൾ നടപ്പിലാക്കാനും മോഡലുകൾ ടൂളുകളായി രജിസ്റ്റർ ചെയ്യാനും കംപ്യൂട്ട് റിസോഴ്‌സുകൾ മാനേജ് ചെയ്യാനും ഉപയോഗിക്കാം.

### പൈതൺ നടപ്പാക്കൽ

```python
# പൈതൺ അസ്യൂർ എഐ ഇന്റഗ്രേഷൻ
from mcp_client import McpClient
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment, AmlCompute
import os
import asyncio

class EnterpriseAiIntegration:
    def __init__(self, mcp_server_url, subscription_id, resource_group, workspace_name):
        # MCP ക്ലയന്റ് സജ്ജമാക്കുക
        self.mcp_client = McpClient(server_url=mcp_server_url)
        
        # അസ്യൂർ ML ക്ലയന്റ് സജ്ജമാക്കുക
        self.credential = DefaultAzureCredential()
        self.ml_client = MLClient(
            self.credential,
            subscription_id,
            resource_group,
            workspace_name
        )
    
    async def execute_ml_pipeline(self, pipeline_name, input_data):
        """Executes an ML pipeline in Azure ML"""
        # ആദ്യം MCP ടൂളുകൾ ഉപയോഗിച്ച് ഇൻപുട്ട് ഡാറ്റ പ്രോസസ്സ് ചെയ്യുക
        processed_data = await self.mcp_client.execute_tool(
            "dataPreprocessor",
            {
                "data": input_data,
                "operations": ["normalize", "clean", "transform"]
            }
        )
        
        # പൈപ്പ്‌ലൈൻ അസ്യൂർ ML-ലേക്ക് സമർപ്പിക്കുക
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
        
        # ജോബ് വിവരങ്ങൾ തിരികെ നൽകുക
        return {
            "job_id": pipeline_job.id,
            "status": pipeline_job.status,
            "creation_time": pipeline_job.creation_context.created_at
        }
    
    async def register_ml_model_as_tool(self, model_name, model_version="latest"):
        """Registers an Azure ML model as an MCP tool"""
        # മോഡൽ വിശദാംശങ്ങൾ നേടുക
        if model_version == "latest":
            model = self.ml_client.models.get(name=model_name, label="latest")
        else:
            model = self.ml_client.models.get(name=model_name, version=model_version)
        
        # ഡിപ്ലോയ്മെന്റ് പരിസ്ഥിതി സൃഷ്ടിക്കുക
        env = Environment(
            name="mcp-model-env",
            conda_file="./environments/inference-env.yml"
        )
        
        # കംപ്യൂട്ട് സജ്ജമാക്കുക
        compute = self.ml_client.compute.get("mcp-inference")
        
        # മോഡൽ ഓൺലൈൻ എന്റ്പോയിന്റായി ഡിപ്ലോയ് ചെയ്യുക
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
        
        # മോഡൽ സ്കീമയുടെ അടിസ്ഥാനത്തിൽ MCP ടൂൾ സ്കീമ സൃഷ്ടിക്കുക
        tool_schema = {
            "type": "object",
            "properties": {},
            "required": []
        }
        
        # മോഡൽ സ്കീമയുടെ അടിസ്ഥാനത്തിൽ ഇൻപുട്ട് പ്രോപ്പർട്ടികൾ ചേർക്കുക
        for input_name, input_spec in model.signature.inputs.items():
            tool_schema["properties"][input_name] = {
                "type": self._map_ml_type_to_json_type(input_spec.type)
            }
            tool_schema["required"].append(input_name)
        
        # MCP ടൂളായി രജിസ്റ്റർ ചെയ്യുക
        # യഥാർത്ഥ നടപ്പിലാക്കലിൽ, നിങ്ങൾ എന്റ്പോയിന്റ് വിളിക്കുന്ന ഒരു ടൂൾ സൃഷ്ടിക്കും
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- MCP-നെ Azure ML-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുന്ന `EnterpriseAiIntegration` ക്ലാസ് സൃഷ്ടിച്ചു.
- MCP ടൂളുകൾ ഉപയോഗിച്ച് ഇൻപുട്ട് ഡാറ്റ പ്രോസസ്സ് ചെയ്ത് Azure ML-യിലേക്ക് ML പൈപ്പ്ലൈൻ സമർപ്പിക്കുന്ന `execute_ml_pipeline` മെത്തഡ് നടപ്പിലാക്കി.
- Azure ML മോഡൽ MCP ടൂളായി രജിസ്റ്റർ ചെയ്യുന്നതിനുള്ള `register_ml_model_as_tool` മെത്തഡ് നടപ്പിലാക്കി, ആവശ്യമായ ഡിപ്ലോയ്മെന്റ് പരിസ്ഥിതിയും കംപ്യൂട്ട് റിസോഴ്‌സുകളും സൃഷ്ടിച്ചും.
- ടൂൾ രജിസ്ട്രേഷനായി Azure ML ഡാറ്റാ ടൈപ്പുകൾ JSON സ്കീമ ടൈപ്പുകളായി മാപ്പ് ചെയ്തു.
- ML പൈപ്പ്ലൈൻ നടപ്പാക്കലും മോഡൽ രജിസ്ട്രേഷനും പോലുള്ള ദൈർഘ്യമേറിയ പ്രവർത്തനങ്ങൾ അസിങ്ക്രണസ് പ്രോഗ്രാമിംഗ് ഉപയോഗിച്ച് കൈകാര്യം ചെയ്തു.

## അടുത്തത് എന്താണ്

- [5.2 മൾട്ടി മോഡാലിറ്റി](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->