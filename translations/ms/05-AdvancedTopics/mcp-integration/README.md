# Integrasi Perusahaan

Apabila membina Pelayan MCP dalam konteks perusahaan, anda sering perlu mengintegrasikan dengan platform dan perkhidmatan AI sedia ada. Bahagian ini merangkumi cara untuk mengintegrasikan MCP dengan sistem perusahaan seperti Azure OpenAI dan Microsoft AI Foundry, membolehkan keupayaan AI yang canggih dan orkestrasi alat.

## Pengenalan

Dalam pelajaran ini, anda akan mempelajari cara mengintegrasikan Model Context Protocol (MCP) dengan sistem AI perusahaan, dengan fokus pada Azure OpenAI dan Microsoft AI Foundry. Integrasi ini membolehkan anda memanfaatkan model dan alat AI yang berkuasa sambil mengekalkan fleksibiliti dan kebolehlanjutan MCP.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Mengintegrasikan MCP dengan Azure OpenAI untuk menggunakan keupayaan AI-nya.
- Melaksanakan orkestrasi alat MCP dengan Azure OpenAI.
- Menggabungkan MCP dengan Microsoft AI Foundry untuk keupayaan agen AI yang canggih.
- Memanfaatkan Azure Machine Learning (ML) untuk melaksanakan saluran paip ML dan mendaftarkan model sebagai alat MCP.

## Integrasi Azure OpenAI

Azure OpenAI menyediakan akses kepada model AI yang berkuasa seperti GPT-4 dan lain-lain. Mengintegrasikan MCP dengan Azure OpenAI membolehkan anda menggunakan model-model ini sambil mengekalkan fleksibiliti orkestrasi alat MCP.

### Pelaksanaan C#

Dalam petikan kod ini, kami menunjukkan cara mengintegrasikan MCP dengan Azure OpenAI menggunakan SDK Azure OpenAI.

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

Dalam kod di atas, kami telah:

- Mengkonfigurasi klien Azure OpenAI dengan titik akhir, nama penyebaran, dan kunci API.
- Mencipta kaedah `GetCompletionWithToolsAsync` untuk mendapatkan penyelesaian dengan sokongan alat.
- Mengendalikan panggilan alat dalam respons.

Anda digalakkan untuk melaksanakan logik pengendalian alat sebenar berdasarkan persediaan pelayan MCP anda.

## Integrasi Microsoft AI Foundry

Azure AI Foundry menyediakan platform untuk membina dan menyebarkan agen AI. Mengintegrasikan MCP dengan AI Foundry membolehkan anda memanfaatkan keupayaannya sambil mengekalkan fleksibiliti MCP.

Dalam kod di bawah, kami membangunkan integrasi Agen yang memproses permintaan dan mengendalikan panggilan alat menggunakan MCP.

### Pelaksanaan Java

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

Dalam kod di atas, kami telah:

- Mencipta kelas `AIFoundryMcpBridge` yang mengintegrasikan dengan kedua-dua AI Foundry dan MCP.
- Melaksanakan kaedah `processAgentRequest` yang memproses permintaan agen AI Foundry.
- Mengendalikan panggilan alat dengan melaksanakannya melalui klien MCP dan menyerahkan hasilnya kembali kepada agen AI Foundry.

## Mengintegrasikan MCP dengan Azure ML

Mengintegrasikan MCP dengan Azure Machine Learning (ML) membolehkan anda memanfaatkan keupayaan ML Azure yang berkuasa sambil mengekalkan fleksibiliti MCP. Integrasi ini boleh digunakan untuk melaksanakan saluran paip ML, mendaftarkan model sebagai alat, dan mengurus sumber pengkomputeran.

### Pelaksanaan Python

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

Dalam kod di atas, kami telah:

- Mencipta kelas `EnterpriseAiIntegration` yang mengintegrasikan MCP dengan Azure ML.
- Melaksanakan kaedah `execute_ml_pipeline` yang memproses data input menggunakan alat MCP dan menyerahkan saluran paip ML kepada Azure ML.
- Melaksanakan kaedah `register_ml_model_as_tool` yang mendaftarkan model Azure ML sebagai alat MCP, termasuk mencipta persekitaran penyebaran dan sumber pengkomputeran yang diperlukan.
- Memetakan jenis data Azure ML kepada jenis skema JSON untuk pendaftaran alat.
- Menggunakan pengaturcaraan asinkron untuk mengendalikan operasi yang berpotensi mengambil masa lama seperti pelaksanaan saluran paip ML dan pendaftaran model.

## Apa yang seterusnya

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.