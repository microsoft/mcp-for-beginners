# การผสานรวมในระดับองค์กร

เมื่อสร้าง MCP Servers ในบริบทขององค์กร คุณมักจะต้องผสานรวมกับแพลตฟอร์มและบริการ AI ที่มีอยู่แล้ว ส่วนนี้จะครอบคลุมถึงวิธีการผสาน MCP เข้ากับระบบองค์กร เช่น Azure OpenAI และ Microsoft AI Foundry เพื่อเพิ่มความสามารถด้าน AI ขั้นสูงและการจัดการเครื่องมือ

## บทนำ

ในบทเรียนนี้ คุณจะได้เรียนรู้วิธีผสาน Model Context Protocol (MCP) เข้ากับระบบ AI ขององค์กร โดยเน้นที่ Azure OpenAI และ Microsoft AI Foundry การผสานรวมเหล่านี้ช่วยให้คุณสามารถใช้โมเดล AI และเครื่องมือที่ทรงพลังได้ ในขณะที่ยังคงความยืดหยุ่นและความสามารถในการขยายของ MCP

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- ผสาน MCP เข้ากับ Azure OpenAI เพื่อใช้ความสามารถด้าน AI ของมัน
- ใช้ MCP ในการจัดการเครื่องมือร่วมกับ Azure OpenAI
- ผสาน MCP เข้ากับ Microsoft AI Foundry เพื่อเพิ่มความสามารถของ AI agent
- ใช้ Azure Machine Learning (ML) ในการรัน ML pipelines และลงทะเบียนโมเดลเป็นเครื่องมือของ MCP

## การผสาน Azure OpenAI

Azure OpenAI ให้การเข้าถึงโมเดล AI ที่ทรงพลัง เช่น GPT-4 และอื่น ๆ การผสาน MCP เข้ากับ Azure OpenAI ช่วยให้คุณสามารถใช้โมเดลเหล่านี้ได้ ในขณะที่ยังคงความยืดหยุ่นของการจัดการเครื่องมือของ MCP

### การใช้งานด้วย C#

ในตัวอย่างโค้ดนี้ เราจะแสดงวิธีผสาน MCP เข้ากับ Azure OpenAI โดยใช้ Azure OpenAI SDK

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

ในโค้ดข้างต้น เราได้:

- กำหนดค่า Azure OpenAI client ด้วย endpoint, deployment name และ API key
- สร้างเมธอด `GetCompletionWithToolsAsync` เพื่อรับผลลัพธ์พร้อมการสนับสนุนเครื่องมือ
- จัดการการเรียกใช้เครื่องมือใน response

คุณควรพัฒนา logic การจัดการเครื่องมือจริงตามการตั้งค่า MCP server ของคุณเอง

## การผสาน Microsoft AI Foundry

Azure AI Foundry เป็นแพลตฟอร์มสำหรับสร้างและปรับใช้ AI agents การผสาน MCP เข้ากับ AI Foundry ช่วยให้คุณสามารถใช้ความสามารถของมันได้ ในขณะที่ยังคงความยืดหยุ่นของ MCP

ในโค้ดด้านล่าง เราได้พัฒนา Agent integration ที่ประมวลผลคำขอและจัดการการเรียกใช้เครื่องมือโดยใช้ MCP

### การใช้งานด้วย Java

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

ในโค้ดข้างต้น เราได้:

- สร้างคลาส `AIFoundryMcpBridge` ที่ผสานรวมกับทั้ง AI Foundry และ MCP
- ใช้เมธอด `processAgentRequest` เพื่อประมวลผลคำขอของ AI Foundry agent
- จัดการการเรียกใช้เครื่องมือโดยการรันผ่าน MCP client และส่งผลลัพธ์กลับไปยัง AI Foundry agent

## การผสาน MCP กับ Azure ML

การผสาน MCP เข้ากับ Azure Machine Learning (ML) ช่วยให้คุณสามารถใช้ความสามารถ ML ที่ทรงพลังของ Azure ได้ ในขณะที่ยังคงความยืดหยุ่นของ MCP การผสานนี้สามารถใช้เพื่อรัน ML pipelines, ลงทะเบียนโมเดลเป็นเครื่องมือ และจัดการทรัพยากรการประมวลผล

### การใช้งานด้วย Python

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

ในโค้ดข้างต้น เราได้:

- สร้างคลาส `EnterpriseAiIntegration` ที่ผสาน MCP เข้ากับ Azure ML
- ใช้เมธอด `execute_ml_pipeline` เพื่อประมวลผลข้อมูลอินพุตโดยใช้เครื่องมือ MCP และส่ง ML pipeline ไปยัง Azure ML
- ใช้เมธอด `register_ml_model_as_tool` เพื่อลงทะเบียนโมเดล Azure ML เป็นเครื่องมือ MCP รวมถึงการสร้างสภาพแวดล้อมการปรับใช้และทรัพยากรการประมวลผลที่จำเป็น
- แมปประเภทข้อมูลของ Azure ML กับประเภท JSON schema สำหรับการลงทะเบียนเครื่องมือ
- ใช้การเขียนโปรแกรมแบบอะซิงโครนัสเพื่อจัดการกับการดำเนินการที่อาจใช้เวลานาน เช่น การรัน ML pipeline และการลงทะเบียนโมเดล

## ขั้นตอนถัดไป

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้