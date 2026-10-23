# אינטגרציה ארגונית

בעת בניית שרתי MCP בהקשר ארגוני, לעיתים קרובות יש צורך באינטגרציה עם פלטפורמות ושירותי בינה מלאכותית קיימים. חלק זה מתאר כיצד לשלב את MCP עם מערכות ארגוניות כמו Azure OpenAI ו-Microsoft AI Foundry, המאפשרים יכולות בינה מלאכותית מתקדמות ותזמור כלים.

## מבוא

בשיעור זה תלמד כיצד לשלב את פרוטוקול הקשר הדגם (MCP) עם מערכות בינה מלאכותית ארגוניות, תוך התמקדות ב-Azure OpenAI וב-Microsoft AI Foundry. אינטגרציות אלו מאפשרות לך לנצל דגמים וכלים חזקים של בינה מלאכותית תוך שמירה על הגמישות וההרחבה של MCP.

## יעדי הלמידה

בסיום שיעור זה תוכל:

- לשלב את MCP עם Azure OpenAI כדי לנצל את יכולות הבינה המלאכותית שלה.
- לבצע תזמור כלים של MCP עם Azure OpenAI.
- לשלב את MCP עם Microsoft AI Foundry עבור יכולות סוכני בינה מלאכותית מתקדמות.
- לנצל את Azure Machine Learning (ML) לביצוע צינורות ML ולהרשמת דגמים ככלים של MCP.

## אינטגרציה עם Azure OpenAI

Microsoft Foundry מספקת גישה לדגמי בינה מלאכותית עדכניים כגון GPT-5.1.
שילוב MCP עם דגמי Foundry שומר על גמישות תזמור הכלים של MCP 
תוך שימוש בפריסה מנוהלת של הדגם.

### מימוש ב-C#

בקטע קוד זה אנו מדגימים כיצד לשלב את MCP עם Azure OpenAI באמצעות ערכת הפיתוח של Azure OpenAI.

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

בקוד שלמעלה ביצענו:

- הגדרנו את לקוח Azure OpenAI עם נקודת הקצה, שם הפריסה ומפתח ה-API.
- יצרנו שיטת `GetCompletionWithToolsAsync` לקבלת השלמות עם תמיכה בכלים.
- טיפלנו בקריאות כלים בתגובה.

מומלץ לך ליישם את הלוגיקה האמיתית לטיפול בכלים בהתבסס על תצורת שרת ה-MCP הספציפית שלך.

## אינטגרציה עם Microsoft Foundry

Microsoft Foundry מספק פלטפורמה לבניית סוכני בינה מלאכותית ופריסתם. שילוב MCP עם Microsoft Foundry מאפשר לך לנצל את יכולותיה תוך שמירה על גמישות MCP.

בקוד הבא, אנו מפתחים אינטגרציה של סוכן שמטפל בבקשות ומטפל בקריאות כלים באמצעות MCP.

### מימוש ב-Java

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

בקוד לעיל ביצענו:

- יצירת מחלקה `AIFoundryMcpBridge` שמשלבת גם עם AI Foundry וגם עם MCP.
- יישום שיטה `processAgentRequest` המעבדת בקשות מסוכן AI Foundry.
- טיפול בקריאות כלים על ידי הרצתן דרך לקוח MCP והחזרת התוצאות לסוכן AI Foundry.

## שילוב MCP עם Azure ML

שילוב MCP עם Azure Machine Learning (ML) מאפשר לך לנצל את יכולות ה-ML החזקות של Azure תוך שמירה על גמישות MCP. אינטגרציה זו מאפשרת ביצוע צינורות ML, הרשמת דגמים ככלים וניהול משאבי חישוב.

### מימוש בפייתון

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

בקוד שלמעלה ביצענו:

- יצירת מחלקה `EnterpriseAiIntegration` שמשלבת MCP עם Azure ML.
- יישום שיטה `execute_ml_pipeline` המעבדת נתוני קלט באמצעות כלי MCP ומשגרת צינור ML ל-Azure ML.
- יישום שיטה `register_ml_model_as_tool` הרשמת דגם Azure ML ככלי MCP, כולל יצירת סביבת הפריסה ומשאבי החישוב הנדרשים.
- מיפוי סוגי נתונים של Azure ML לסוגי סכמת JSON עבור רישום הכלי.
- שימוש בתכנות אסינכרוני לטיפול בתהליכים שעשויים להיות ארוכים כמו הפעלת צינורות ML ורישום דגמים.

## מה הלאה

- [5.2 מולטימודליות](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->