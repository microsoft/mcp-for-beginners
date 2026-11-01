# Yrityksen integraatiot

Rakentaessasi MCP-palvelimia yritysympäristössä, sinun on usein integroitava olemassa oleviin AI-alustoihin ja palveluihin. Tässä osiossa käsitellään, kuinka integroida MCP yritysjärjestelmiin kuten Azure OpenAI ja Microsoft AI Foundry, mahdollistaen edistyneet tekoälyominaisuudet ja työkalujen orkestroinnin.

## Johdanto

Tässä oppitunnissa opit, miten Model Context Protocol (MCP) integroidaan yrityksen tekoälyjärjestelmiin, erityisesti Azure OpenAI:hin ja Microsoft AI Foundryyn. Nämä integraatiot mahdollistavat tehokkaiden tekoälymallien ja työkalujen hyödyntämisen samalla kun säilytetään MCP:n joustavuus ja laajennettavuus.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Integroida MCP:n Azure OpenAI:hin tekoälyominaisuuksien hyödyntämiseksi.
- Toteuttaa MCP:n työkalujen orkestrointi Azure OpenAI:n kanssa.
- Yhdistää MCP Microsoft AI Foundryyn edistyneiden tekoälyagenttien mahdollistamiseksi.
- Hyödyntää Azure Machine Learningiä (ML) ML-putkien suorittamiseen ja mallien rekisteröintiin MCP-työkaluina.

## Azure OpenAI -integraatio

Microsoft Foundry tarjoaa pääsyn nykyisiin tekoälymalleihin kuten GPT-5.1.
MCP:n integrointi Foundry-mallien kanssa säilyttää MCP-työkalujen orkestroinnin joustavuuden
samalla kun käytössä on hallinnoitu mallien käyttöönotto.

### C#-toteutus

Tässä koodiesimerkissä demonstroimme, miten MCP integroidaan Azure OpenAI:hin käyttäen Azure OpenAI SDK:ta.

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

Edellä olevassa koodissa olemme:

- Määrittäneet Azure OpenAI -asiakkaan käyttämään päätepistettä, käyttöönoton nimeä ja API-avainta.
- Luoneet metodin `GetCompletionWithToolsAsync` saadaksemme täydennyksiä työkalutuen kanssa.
- Käsitelleet työkalukutsut vastauksessa.

Sinua kehotetaan toteuttamaan varsinaiset työkalukäsittelylogiikat oman MCP-palvelimesi mukaan.

## Microsoft Foundry -integraatio

Microsoft Foundry tarjoaa alustan tekoälyagenttien rakentamiseen ja käyttöönottoon. MCP:n integroiminen Microsoft Foundryyn mahdollistaa sen ominaisuuksien hyödyntämisen säilyttäen samalla MCP:n joustavuuden.

Seuraavassa koodissa kehitämme Agentti-integraation, joka käsittelee pyyntöjä ja työkalukutsuja MCP:n avulla.

### Java-toteutus

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

Edellä olevassa koodissa olemme:

- Luoneet `AIFoundryMcpBridge`-luokan, joka integroituu sekä AI Foundryyn että MCP:hen.
- Toteuttaneet metodin `processAgentRequest`, joka käsittelee AI Foundryn agenttipyynnön.
- Käsitelleet työkalukutsut suorittamalla ne MCP-asiakkaan kautta ja lähettämällä tulokset takaisin AI Foundryn agentille.

## MCP:n integrointi Azure ML:ään

MCP:n integrointi Azure Machine Learningiin (ML) mahdollistaa Azuren tehokkaiden ML-ominaisuuksien hyödyntämisen säilyttäen MCP:n joustavuuden. Tätä integraatiota voidaan käyttää ML-putkien suorittamiseen, mallien rekisteröintiin työkaluina ja laskentaresurssien hallintaan.

### Python-toteutus

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

Edellä olevassa koodissa olemme:

- Luoneet `EnterpriseAiIntegration`-luokan, joka integroi MCP:n Azure ML:n kanssa.
- Toteuttaneet `execute_ml_pipeline`-metodin, joka käsittelee syötteen MCP-työkalujen avulla ja lähettää ML-putken suoritettavaksi Azure ML:lle.
- Toteuttaneet `register_ml_model_as_tool`-metodin, joka rekisteröi Azure ML -mallin MCP-työkaluna, mukaan lukien tarvittavan käyttöönottoyhteyden ja laskentaresurssit.
- Kartoitamme Azure ML:n tietotyypit JSON-skeematyyppien mukaisesti työkalujen rekisteröinnissä.
- Käytämme asynkronista ohjelmointia pitkien operaatioiden, kuten ML-putken suorituksen ja mallin rekisteröinnin, käsittelyyn.

## Mitä seuraavaksi

- [5.2 Monimuotoisuus](../mcp-multi-modality/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->