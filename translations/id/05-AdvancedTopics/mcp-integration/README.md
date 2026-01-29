# Integrasi Perusahaan

Saat membangun MCP Server dalam konteks perusahaan, sering kali Anda perlu mengintegrasikan dengan platform dan layanan AI yang sudah ada. Bagian ini membahas cara mengintegrasikan MCP dengan sistem perusahaan seperti Azure OpenAI dan Microsoft AI Foundry, memungkinkan kemampuan AI canggih dan orkestrasi alat.

## Pendahuluan

Dalam pelajaran ini, Anda akan mempelajari cara mengintegrasikan Model Context Protocol (MCP) dengan sistem AI perusahaan, dengan fokus pada Azure OpenAI dan Microsoft AI Foundry. Integrasi ini memungkinkan Anda memanfaatkan model dan alat AI yang kuat sambil tetap mempertahankan fleksibilitas dan kemampuan perluasan MCP.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Mengintegrasikan MCP dengan Azure OpenAI untuk memanfaatkan kemampuan AI-nya.
- Menerapkan orkestrasi alat MCP dengan Azure OpenAI.
- Menggabungkan MCP dengan Microsoft AI Foundry untuk kemampuan agen AI yang lebih canggih.
- Memanfaatkan Azure Machine Learning (ML) untuk menjalankan pipeline ML dan mendaftarkan model sebagai alat MCP.

## Integrasi Azure OpenAI

Azure OpenAI menyediakan akses ke model AI yang kuat seperti GPT-4 dan lainnya. Mengintegrasikan MCP dengan Azure OpenAI memungkinkan Anda memanfaatkan model-model ini sambil tetap mempertahankan fleksibilitas orkestrasi alat MCP.

### Implementasi C#

Dalam cuplikan kode ini, kami menunjukkan cara mengintegrasikan MCP dengan Azure OpenAI menggunakan Azure OpenAI SDK.

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

Dalam kode di atas, kami telah:

- Mengonfigurasi klien Azure OpenAI dengan endpoint, nama deployment, dan API key.
- Membuat metode `GetCompletionWithToolsAsync` untuk mendapatkan hasil dengan dukungan alat.
- Menangani pemanggilan alat dalam respons.

Anda disarankan untuk menerapkan logika penanganan alat yang sesuai berdasarkan pengaturan server MCP Anda.

## Integrasi Microsoft AI Foundry

Azure AI Foundry menyediakan platform untuk membangun dan menerapkan agen AI. Mengintegrasikan MCP dengan AI Foundry memungkinkan Anda memanfaatkan kemampuannya sambil tetap mempertahankan fleksibilitas MCP.

Dalam kode di bawah ini, kami mengembangkan integrasi Agen yang memproses permintaan dan menangani pemanggilan alat menggunakan MCP.

### Implementasi Java

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

Dalam kode di atas, kami telah:

- Membuat kelas `AIFoundryMcpBridge` yang mengintegrasikan AI Foundry dan MCP.
- Menerapkan metode `processAgentRequest` yang memproses permintaan agen AI Foundry.
- Menangani pemanggilan alat dengan mengeksekusinya melalui klien MCP dan mengirimkan hasilnya kembali ke agen AI Foundry.

## Integrasi MCP dengan Azure ML

Mengintegrasikan MCP dengan Azure Machine Learning (ML) memungkinkan Anda memanfaatkan kemampuan ML Azure yang kuat sambil tetap mempertahankan fleksibilitas MCP. Integrasi ini dapat digunakan untuk menjalankan pipeline ML, mendaftarkan model sebagai alat, dan mengelola sumber daya komputasi.

### Implementasi Python

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

Dalam kode di atas, kami telah:

- Membuat kelas `EnterpriseAiIntegration` yang mengintegrasikan MCP dengan Azure ML.
- Menerapkan metode `execute_ml_pipeline` yang memproses data masukan menggunakan alat MCP dan mengirimkan pipeline ML ke Azure ML.
- Menerapkan metode `register_ml_model_as_tool` yang mendaftarkan model Azure ML sebagai alat MCP, termasuk membuat lingkungan deployment dan sumber daya komputasi yang diperlukan.
- Memetakan tipe data Azure ML ke tipe skema JSON untuk pendaftaran alat.
- Menggunakan pemrograman asinkron untuk menangani operasi yang berpotensi memakan waktu lama seperti eksekusi pipeline ML dan pendaftaran model.

## Langkah Selanjutnya

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.