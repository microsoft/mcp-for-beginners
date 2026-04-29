# ការរួមបញ្ចូលអេនធើរភ្លាញ

ពេលដែលកំពុងបង្កើតម៉ាស៊ីនមេ MCP នៅក្នុងបទបរិបទអេនធើរភ្លាញ អ្នកជាញឹកញាប់ត្រូវការរួមបញ្ចូលជាមួយវេទិកា និងសេវាកម្ម AI ដែលមានរួចមក។ ផ្នែកនេះគ្របដណ្តប់ពីរបៀបរួមបញ្ចូល MCP ជាមួយប្រព័ន្ធអេនធើរភ្លាញដូចជា Azure OpenAI និង Microsoft AI Foundry ដែលអនុញ្ញាតឲ្យមានសមត្ថភាព AI មានវិញ្ញាសាទំនើប និង ការរៀបចំឧបករណ៍។

## ការណែនាំ

នៅក្នុងមេរៀននេះ អ្នកនឹងរៀនពីរបៀបរួមបញ្ចូល Model Context Protocol (MCP) ជាមួយប្រព័ន្ធ AI អេនធើរភ្លាញ ដោយផ្តោតលើ Azure OpenAI និង Microsoft AI Foundry។ ការរួមបញ្ចូលទាំងនេះអនុញ្ញាតឲ្យអ្នកអាចទាក់ទាញគំរូ AI ដែលមានប្លែកៗ និងឧបករណ៍ ខណៈពេលរក្សាស្របច្បាប់និងភាពបត់បែននៃ MCP។

## គោលបំណងការសិក្សា

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច:

- រួមបញ្ចូល MCP ជាមួយ Azure OpenAI ដើម្បីប្រើប្រាស់សមត្ថភាព AI របស់វា។
- អនុវត្តការរៀបចំឧបករណ៍ MCP ជាមួយ Azure OpenAI។
- បញ្ចូល MCP ជាមួយ Microsoft AI Foundry សម្រាប់សមត្ថភាពភ្នាក់ងារច្នៃប្រឌិត AI ទាន់សម័យ។
- ប្រើប្រាស់ Azure Machine Learning (ML) សម្រាប់ការបញ្ចូលស៊ុម ML និងចុះបញ្ជីគំរូក្នុងនាមឧបករណ៍ MCP។

## ការរួមបញ្ចូល Azure OpenAI

Azure OpenAI ផ្តល់ការចូលដំណើរការទៅកាន់គំរូ AI មានអំណាចដូចជា GPT-4 និងផ្សេងៗទៀត។ ការរួមបញ្ចូល MCP ជាមួយ Azure OpenAI អនុញ្ញាតឲ្យអ្នកប្រើប្រាស់គំរូទាំងនេះ ខណៈដែលរក្សាសមត្ថភាពបត់បែននៃការរៀបចំឧបករណ៍របស់ MCP។

### ការអនុវត្តជាភាសា C#

នៅក្នុងកូដខាងក្រោម យើងបង្ហាញពីរបៀបរួមបញ្ចូល MCP ជាមួយ Azure OpenAI ដោយប្រើ Azure OpenAI SDK ។

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

នៅក្នុងកូដខាងលើ យើងបាន:

- កំណត់អតិថិជន Azure OpenAI ជាមួយចំណុចចេញ, ឈ្មោះការដាក់ជូន និងកូនសោ API។
- បង្កើតវិធីសាស្រ្ត `GetCompletionWithToolsAsync` ដើម្បីទទួលការបញ្ចប់ជាមួយការគាំទ្រឧបករណ៍។
- គ្រប់គ្រងការហៅឧបករណ៍ក្នុងការឆ្លើយតប។

អ្នកត្រូវបានលើកទឹកចិត្តអោយអនុវត្តតុល្យភាពការគ្រប់គ្រងឧបករណ៍ពិតប្រាកដដោយផ្អែកទៅលើការកំណត់ម៉ាស៊ីនមេ MCP របស់អ្នក។

## ការរួមបញ្ចូល Microsoft AI Foundry

Azure AI Foundry ផ្តល់វេទិកាសម្រាប់សាងសង់ និងដាក់ឱ្យដំណើរការភ្នាក់ងារ AI។ ការរួមបញ្ចូល MCP ជាមួយ AI Foundry អនុញ្ញាតឲ្យអ្នកទាក់ទាញសមត្ថភាពរបស់វា ខណៈរក្សាសមត្ថភាពបត់បែននៃ MCP។

នៅក្នុងកូដខាងក្រោម យើងបង្កើតការរួមបញ្ចូលភ្នាក់ងារ ដែលដំណើរការសំណើ និងគ្រប់គ្រងការហៅឧបករណ៍ដោយប្រើ MCP។

### ការអនុវត្តជាភាសា Java

```java
// ការរួមបញ្ចូលភ្នាក់ងារជំនាញ Java AI Foundry
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
        // ដំណើរការសំណើរពីភ្នាក់ងារជំនាញ AI Foundry
        AgentResponse initialResponse = agentClient.processRequest(request);
        
        // ពិនិត្យមើលថាតើភ្នាក់ងារបានស្នើឲ្យប្រើឧបករណ៍ឬអត់
        if (initialResponse.getToolCalls() != null && !initialResponse.getToolCalls().isEmpty()) {
            // សម្រាប់ការហៅឧបករណ៍នីមួយៗ នាំវាទៅឧបករណ៍ MCP ដែលសមរម្យ
            for (AgentToolCall toolCall : initialResponse.getToolCalls()) {
                String toolName = toolCall.getName();
                Map<String, Object> parameters = toolCall.getArguments();
                
                // ប្រតិបត្តិឧបករណ៍ជាមួយ MCP
                ToolResponse mcpResponse = mcpClient.executeTool(toolName, parameters);
                
                // បង្កើតចម្លើយឧបករណ៍សម្រាប់ AI Foundry
                AgentToolResponse toolResponse = new AgentToolResponse(
                    toolCall.getId(),
                    mcpResponse.getResult()
                );
                
                // ស្នើសុំចម្លើយឧបករណ៍ត្រឡប់ទៅភ្នាក់ងារ
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

នៅក្នុងកូដខាងលើ យើងបាន:

- បង្កើតថ្នាក់ `AIFoundryMcpBridge` ដែលរួមបញ្ចូលជាមួយ AI Foundry និង MCP។
- អនុវត្តវិធីសាស្រ្ត `processAgentRequest` ដែលដំណើរការសំណើភ្នាក់ងារ AI Foundry។
- គ្រប់គ្រងការហៅឧបករណ៍ដោយអនុវត្តវាតាមអតិថិជន MCP ហើយផ្ញើលទ្ធផលត្រឡប់ទៅភ្នាក់ងារ AI Foundry។

## ការរួមបញ្ចូល MCP ជាមួយ Azure ML

ការរួមបញ្ចូល MCP ជាមួយ Azure Machine Learning (ML) អនុញ្ញាតឲ្យអ្នកប្រើប្រាស់សមត្ថភាព ML មានអំណាចរបស់ Azure ខណៈរក្សាការបត់បែនរបស់ MCP។ ការរួមបញ្ចូលនេះអាចប្រើប្រាស់ដំណើរការស៊ុម ML ធ្វើចុះបញ្ជីគំរូក្នុងនាមឧបករណ៍ និងគ្រប់គ្រងធនធានកុំព្យូទ័រ។

### ការអនុវត្តជាភាសា Python

```python
# ការរួមបញ្ចូល Python Azure AI
from mcp_client import McpClient
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment, AmlCompute
import os
import asyncio

class EnterpriseAiIntegration:
    def __init__(self, mcp_server_url, subscription_id, resource_group, workspace_name):
        # កំណត់ឡើង MCP client
        self.mcp_client = McpClient(server_url=mcp_server_url)
        
        # កំណត់ឡើង Azure ML client
        self.credential = DefaultAzureCredential()
        self.ml_client = MLClient(
            self.credential,
            subscription_id,
            resource_group,
            workspace_name
        )
    
    async def execute_ml_pipeline(self, pipeline_name, input_data):
        """Executes an ML pipeline in Azure ML"""
        # ដំណើរការដំបូងទិន្នន័យបញ្ចូលដោយប្រើឧបករណ៍ MCP
        processed_data = await self.mcp_client.execute_tool(
            "dataPreprocessor",
            {
                "data": input_data,
                "operations": ["normalize", "clean", "transform"]
            }
        )
        
        # ស្នើសុំ pipeline ទៅ Azure ML
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
        
        # ត្រឡប់ព័ត៌មានការងារ
        return {
            "job_id": pipeline_job.id,
            "status": pipeline_job.status,
            "creation_time": pipeline_job.creation_context.created_at
        }
    
    async def register_ml_model_as_tool(self, model_name, model_version="latest"):
        """Registers an Azure ML model as an MCP tool"""
        # ទទួលព័ត៌មានលម្អិតម៉ូដែល
        if model_version == "latest":
            model = self.ml_client.models.get(name=model_name, label="latest")
        else:
            model = self.ml_client.models.get(name=model_name, version=model_version)
        
        # បង្កើតបរិស្ថានប្រើប្រាស់
        env = Environment(
            name="mcp-model-env",
            conda_file="./environments/inference-env.yml"
        )
        
        # កំណត់ឡើង compute
        compute = self.ml_client.compute.get("mcp-inference")
        
        # បញ្ចូលម៉ូដែលជាច្រោះអ៊ិនធើណេតអនឡាញ
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
        
        # បង្កើត schema ឧបករណ៍ MCP ដោយផ្អែកលើ schema ម៉ូដែល
        tool_schema = {
            "type": "object",
            "properties": {},
            "required": []
        }
        
        # បន្ថែមលក្ខណៈបញ្ចូលដោយផ្អែកលើ schema ម៉ូដែល
        for input_name, input_spec in model.signature.inputs.items():
            tool_schema["properties"][input_name] = {
                "type": self._map_ml_type_to_json_type(input_spec.type)
            }
            tool_schema["required"].append(input_name)
        
        # ចុះបញ្ជីជាឧបករណ៍ MCP
        # ក្នុងការអនុវត្តពិត អ្នកនឹងបង្កើតឧបករណ៍មួយដែលហៅទៅ endpoint
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

នៅក្នុងកូដខាងលើ យើងបាន:

- បង្កើតថ្នាក់ `EnterpriseAiIntegration` ដែលរួមបញ្ចូល MCP ជាមួយ Azure ML។
- អនុវត្តវិធីសាស្រ្ត `execute_ml_pipeline` ដែលដំណើរការទិន្នន័យបញ្ចូលដោយប្រើឧបករណ៍ MCP ហើយដាក់ស៊ុម ML ទៅកាន់ Azure ML។
- អនុវត្តវិធីសាស្រ្ត `register_ml_model_as_tool` ដែលចុះបញ្ជីគំរូ Azure ML ក្នុងនាមឧបករណ៍ MCP រួមបញ្ចូលការបង្កើតបរិយាកាសដាក់ជូន និងធនធានកុំព្យូទ័រដែលចាំបាច់។
- បំពាក់ប្រភេទទិន្នន័យ Azure ML ទៅប្រភេទ JSON Schema សម្រាប់ចុះបញ្ជីឧបករណ៍។
- ប្រើការសរសេរកូដមិនស្របពេល (asynchronous programming) ដើម្បីគ្រប់គ្រងប្រតិបត្តិការដែលអាចចំណាយពេលយូរដូចជាការដំណើរការស៊ុម ML និងការចុះបញ្ជីគំរូ។

## អ្នកអាចធ្វើបន្ទាប់

- [5.2 ការប្រើប្រាស់ម៉ូដទីតាប់ចម្រុះ](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ឲ្យដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាម្ចាស់ខ្លួនគួរត្រូវបានយកទៅជាមូលដ្ឋានផ្លូវការជាដំបូង។ សម្រាប់ព័ត៌មានសំខាន់ សូមផ្តល់អនុសាសន៍ឲ្យបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុស ណាមួយដែលកើតមានពីការប្រើប្រាស់បកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->