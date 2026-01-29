# Ενσωμάτωση σε Επιχειρησιακό Περιβάλλον

Όταν δημιουργείτε MCP Servers σε ένα επιχειρησιακό πλαίσιο, συχνά χρειάζεται να ενσωματώσετε υπάρχουσες πλατφόρμες και υπηρεσίες AI. Αυτή η ενότητα καλύπτει πώς να ενσωματώσετε το MCP με επιχειρησιακά συστήματα όπως το Azure OpenAI και το Microsoft AI Foundry, επιτρέποντας προηγμένες δυνατότητες AI και οργάνωση εργαλείων.

## Εισαγωγή

Σε αυτό το μάθημα, θα μάθετε πώς να ενσωματώσετε το Model Context Protocol (MCP) με επιχειρησιακά συστήματα AI, εστιάζοντας στο Azure OpenAI και το Microsoft AI Foundry. Αυτές οι ενσωματώσεις σας επιτρέπουν να αξιοποιήσετε ισχυρά μοντέλα και εργαλεία AI, διατηρώντας παράλληλα την ευελιξία και επεκτασιμότητα του MCP.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του μαθήματος, θα είστε σε θέση να:

- Ενσωματώσετε το MCP με το Azure OpenAI για να αξιοποιήσετε τις δυνατότητες AI του.
- Υλοποιήσετε οργάνωση εργαλείων MCP με το Azure OpenAI.
- Συνδυάσετε το MCP με το Microsoft AI Foundry για προηγμένες δυνατότητες AI agents.
- Αξιοποιήσετε το Azure Machine Learning (ML) για την εκτέλεση ML pipelines και την καταχώρηση μοντέλων ως εργαλεία MCP.

## Ενσωμάτωση Azure OpenAI

Το Azure OpenAI παρέχει πρόσβαση σε ισχυρά μοντέλα AI όπως το GPT-4 και άλλα. Η ενσωμάτωση του MCP με το Azure OpenAI σας επιτρέπει να αξιοποιήσετε αυτά τα μοντέλα, διατηρώντας παράλληλα την ευελιξία της οργάνωσης εργαλείων του MCP.

### Υλοποίηση σε C#

Σε αυτό το απόσπασμα κώδικα, δείχνουμε πώς να ενσωματώσετε το MCP με το Azure OpenAI χρησιμοποιώντας το Azure OpenAI SDK.

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

Στον παραπάνω κώδικα έχουμε:

- Ρυθμίσει τον πελάτη Azure OpenAI με το endpoint, το όνομα ανάπτυξης και το API key.
- Δημιουργήσει μια μέθοδο `GetCompletionWithToolsAsync` για να λαμβάνουμε αποτελέσματα με υποστήριξη εργαλείων.
- Διαχειριστεί τις κλήσεις εργαλείων στην απόκριση.

Σας ενθαρρύνουμε να υλοποιήσετε τη λογική διαχείρισης εργαλείων με βάση τη συγκεκριμένη ρύθμιση του MCP server σας.

## Ενσωμάτωση Microsoft AI Foundry

Το Azure AI Foundry παρέχει μια πλατφόρμα για τη δημιουργία και ανάπτυξη AI agents. Η ενσωμάτωση του MCP με το AI Foundry σας επιτρέπει να αξιοποιήσετε τις δυνατότητές του, διατηρώντας παράλληλα την ευελιξία του MCP.

Στον παρακάτω κώδικα, αναπτύσσουμε μια ενσωμάτωση Agent που επεξεργάζεται αιτήματα και διαχειρίζεται κλήσεις εργαλείων χρησιμοποιώντας το MCP.

### Υλοποίηση σε Java

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

Στον παραπάνω κώδικα έχουμε:

- Δημιουργήσει μια κλάση `AIFoundryMcpBridge` που ενσωματώνεται τόσο με το AI Foundry όσο και με το MCP.
- Υλοποιήσει μια μέθοδο `processAgentRequest` που επεξεργάζεται ένα αίτημα agent του AI Foundry.
- Διαχειριστεί τις κλήσεις εργαλείων εκτελώντας τις μέσω του MCP client και υποβάλλοντας τα αποτελέσματα πίσω στον agent του AI Foundry.

## Ενσωμάτωση MCP με Azure ML

Η ενσωμάτωση του MCP με το Azure Machine Learning (ML) σας επιτρέπει να αξιοποιήσετε τις ισχυρές δυνατότητες ML του Azure, διατηρώντας παράλληλα την ευελιξία του MCP. Αυτή η ενσωμάτωση μπορεί να χρησιμοποιηθεί για την εκτέλεση ML pipelines, την καταχώρηση μοντέλων ως εργαλεία και τη διαχείριση πόρων υπολογισμού.

### Υλοποίηση σε Python

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

Στον παραπάνω κώδικα έχουμε:

- Δημιουργήσει μια κλάση `EnterpriseAiIntegration` που ενσωματώνει το MCP με το Azure ML.
- Υλοποιήσει μια μέθοδο `execute_ml_pipeline` που επεξεργάζεται δεδομένα εισόδου χρησιμοποιώντας εργαλεία MCP και υποβάλλει ένα ML pipeline στο Azure ML.
- Υλοποιήσει μια μέθοδο `register_ml_model_as_tool` που καταχωρεί ένα μοντέλο Azure ML ως εργαλείο MCP, συμπεριλαμβανομένης της δημιουργίας του απαραίτητου περιβάλλοντος ανάπτυξης και των πόρων υπολογισμού.
- Χαρτογραφήσει τύπους δεδομένων του Azure ML σε τύπους JSON schema για την καταχώρηση εργαλείων.
- Χρησιμοποιήσει ασύγχρονο προγραμματισμό για τη διαχείριση πιθανών μακροχρόνιων λειτουργιών όπως η εκτέλεση ML pipelines και η καταχώρηση μοντέλων.

## Τι ακολουθεί

- [5.2 Multi modality](../mcp-multi-modality/README.md)

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε κάθε προσπάθεια για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.