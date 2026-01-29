# এন্টারপ্রাইজ ইন্টিগ্রেশন

এমসিপি সার্ভার (MCP Servers) তৈরি করার সময়, এন্টারপ্রাইজ প্রেক্ষাপটে প্রায়ই বিদ্যমান এআই প্ল্যাটফর্ম এবং পরিষেবাগুলোর সাথে ইন্টিগ্রেশন প্রয়োজন হয়। এই অংশে এমসিপি-কে Azure OpenAI এবং Microsoft AI Foundry-এর মতো এন্টারপ্রাইজ সিস্টেমের সাথে ইন্টিগ্রেট করার পদ্ধতি আলোচনা করা হয়েছে, যা উন্নত এআই সক্ষমতা এবং টুল অর্কেস্ট্রেশন সক্ষম করে।

## ভূমিকা

এই পাঠে, আপনি শিখবেন কীভাবে Model Context Protocol (MCP)-কে এন্টারপ্রাইজ এআই সিস্টেমের সাথে ইন্টিগ্রেট করতে হয়, বিশেষত Azure OpenAI এবং Microsoft AI Foundry-এর উপর ফোকাস করে। এই ইন্টিগ্রেশনগুলো আপনাকে শক্তিশালী এআই মডেল এবং টুল ব্যবহার করার সুযোগ দেয়, একইসাথে এমসিপি-র নমনীয়তা এবং সম্প্রসারণযোগ্যতা বজায় রাখে।

## শেখার লক্ষ্যসমূহ

এই পাঠ শেষে, আপনি সক্ষম হবেন:

- Azure OpenAI-এর সাথে এমসিপি ইন্টিগ্রেট করে এর এআই সক্ষমতাগুলো ব্যবহার করতে।
- Azure OpenAI-এর সাথে এমসিপি টুল অর্কেস্ট্রেশন বাস্তবায়ন করতে।
- Microsoft AI Foundry-এর সাথে এমসিপি সংযুক্ত করে উন্নত এআই এজেন্ট সক্ষমতা অর্জন করতে।
- Azure Machine Learning (ML)-এর সাহায্যে এমএল পাইপলাইন কার্যকর করা এবং মডেলগুলোকে এমসিপি টুল হিসেবে নিবন্ধন করতে।

## Azure OpenAI ইন্টিগ্রেশন

Azure OpenAI শক্তিশালী এআই মডেল যেমন GPT-4 এবং অন্যান্য মডেলের অ্যাক্সেস প্রদান করে। এমসিপি-কে Azure OpenAI-এর সাথে ইন্টিগ্রেট করলে আপনি এই মডেলগুলো ব্যবহার করতে পারবেন, একইসাথে এমসিপি-র টুল অর্কেস্ট্রেশনের নমনীয়তা বজায় থাকবে।

### C# ইমপ্লিমেন্টেশন

এই কোড স্নিপেটে, আমরা Azure OpenAI SDK ব্যবহার করে এমসিপি-কে Azure OpenAI-এর সাথে ইন্টিগ্রেট করার পদ্ধতি দেখিয়েছি।

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

উপরের কোডে আমরা:

- Azure OpenAI ক্লায়েন্টকে এন্ডপয়েন্ট, ডিপ্লয়মেন্ট নাম এবং API কী দিয়ে কনফিগার করেছি।
- `GetCompletionWithToolsAsync` নামক একটি মেথড তৈরি করেছি, যা টুল সাপোর্ট সহ কমপ্লিশন প্রদান করে।
- রেসপন্সে টুল কল হ্যান্ডেল করেছি।

আপনার নির্দিষ্ট এমসিপি সার্ভার সেটআপ অনুযায়ী টুল হ্যান্ডলিং লজিক বাস্তবায়ন করার জন্য আপনাকে উৎসাহিত করা হচ্ছে।

## Microsoft AI Foundry ইন্টিগ্রেশন

Azure AI Foundry একটি প্ল্যাটফর্ম যা এআই এজেন্ট তৈরি এবং ডিপ্লয় করার সুযোগ দেয়। এমসিপি-কে AI Foundry-এর সাথে ইন্টিগ্রেট করলে আপনি এর সক্ষমতাগুলো ব্যবহার করতে পারবেন, একইসাথে এমসিপি-র নমনীয়তা বজায় থাকবে।

নিচের কোডে, আমরা একটি এজেন্ট ইন্টিগ্রেশন তৈরি করেছি, যা রিকোয়েস্ট প্রক্রিয়া করে এবং এমসিপি ব্যবহার করে টুল কল হ্যান্ডেল করে।

### Java ইমপ্লিমেন্টেশন

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

উপরের কোডে আমরা:

- `AIFoundryMcpBridge` নামক একটি ক্লাস তৈরি করেছি, যা AI Foundry এবং এমসিপি উভয়ের সাথে ইন্টিগ্রেট করে।
- `processAgentRequest` নামক একটি মেথড ইমপ্লিমেন্ট করেছি, যা AI Foundry এজেন্ট রিকোয়েস্ট প্রক্রিয়া করে।
- টুল কল হ্যান্ডেল করেছি, যা এমসিপি ক্লায়েন্টের মাধ্যমে কার্যকর করা হয় এবং ফলাফল AI Foundry এজেন্টে জমা দেয়।

## Azure ML-এর সাথে এমসিপি ইন্টিগ্রেশন

Azure Machine Learning (ML)-এর সাথে এমসিপি ইন্টিগ্রেশন আপনাকে Azure-এর শক্তিশালী এমএল সক্ষমতাগুলো ব্যবহার করার সুযোগ দেয়, একইসাথে এমসিপি-র নমনীয়তা বজায় রাখে। এই ইন্টিগ্রেশনটি এমএল পাইপলাইন কার্যকর করা, মডেলগুলোকে টুল হিসেবে নিবন্ধন করা এবং কম্পিউট রিসোর্স ম্যানেজ করার জন্য ব্যবহার করা যেতে পারে।

### Python ইমপ্লিমেন্টেশন

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

উপরের কোডে আমরা:

- `EnterpriseAiIntegration` নামক একটি ক্লাস তৈরি করেছি, যা এমসিপি-কে Azure ML-এর সাথে ইন্টিগ্রেট করে।
- `execute_ml_pipeline` নামক একটি মেথড ইমপ্লিমেন্ট করেছি, যা এমসিপি টুল ব্যবহার করে ইনপুট ডেটা প্রক্রিয়া করে এবং Azure ML-এ একটি এমএল পাইপলাইন জমা দেয়।
- `register_ml_model_as_tool` নামক একটি মেথড ইমপ্লিমেন্ট করেছি, যা একটি Azure ML মডেলকে এমসিপি টুল হিসেবে নিবন্ধন করে, যার মধ্যে প্রয়োজনীয় ডিপ্লয়মেন্ট পরিবেশ এবং কম্পিউট রিসোর্স তৈরি করা অন্তর্ভুক্ত।
- টুল নিবন্ধনের জন্য Azure ML ডেটা টাইপগুলোকে JSON স্কিমা টাইপে ম্যাপ করেছি।
- অ্যাসিঙ্ক্রোনাস প্রোগ্রামিং ব্যবহার করেছি, যা দীর্ঘমেয়াদী অপারেশন যেমন এমএল পাইপলাইন কার্যকর এবং মডেল নিবন্ধন পরিচালনা করতে সহায়ক।

## পরবর্তী ধাপ

- [5.2 মাল্টি মোডালিটি](../mcp-multi-modality/README.md)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।