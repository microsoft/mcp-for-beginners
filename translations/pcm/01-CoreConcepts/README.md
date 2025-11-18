<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "904b59de1de9264801242d90a42cdd9d",
  "translation_date": "2025-11-18T19:39:01+00:00",
  "source_file": "01-CoreConcepts/README.md",
  "language_code": "pcm"
}
-->
# MCP Core Concepts: How to Sabi Model Context Protocol for AI Integration

[![MCP Core Concepts](../../../translated_images/02.8203e26c6fb5a797f38a10012061013ec66c95bb3260f6c9cfd2bf74b00860e1.pcm.png)](https://youtu.be/earDzWGtE84)

_(Click di image wey dey up to watch di video for dis lesson)_

Di [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) na one strong, standard way wey dem take make communication better between Large Language Models (LLMs) and tools, apps, plus data sources.  
Dis guide go show you di main things wey dey MCP. You go sabi di client-server setup, di main parts, how dem dey communicate, and di best way to use am.

- **User Consent Must Sure**: Before any data go dey accessed or any action go happen, di user gatz agree first. Di user gatz sabi wetin dem wan do with di data and wetin dem wan perform, plus di power to control permissions and authorizations.

- **Data Privacy Protection**: User data no fit show unless di user gree. Di data gatz dey protected with strong security from start to finish. Unauthorized data movement no suppose happen, and privacy gatz dey tight.

- **Tool Execution Safety**: Before any tool go run, di user gatz gree and sabi wetin di tool wan do, di parameters, and di possible effect. Strong security gatz dey to stop any mistake, unsafe, or bad tool execution.

- **Transport Layer Security**: All di communication channels gatz use correct encryption and authentication. Remote connections gatz use secure transport protocols and manage credentials well.

#### How to Implement MCP:

- **Permission Management**: Make sure say users fit control which servers, tools, and resources dem wan allow.
- **Authentication & Authorization**: Use secure methods like OAuth or API keys, plus manage tokens well and make dem expire when e reach time.  
- **Input Validation**: Check all di parameters and data wey dem dey input to make sure say e follow di rules and no get wahala like injection attacks.
- **Audit Logging**: Keep correct logs of all di operations for security and compliance.

## Overview

For dis lesson, we go look di main setup and di parts wey dey make di Model Context Protocol (MCP) work. You go sabi di client-server setup, di main parts, and how dem dey communicate for MCP.

## Wetin You Go Learn

By di end of dis lesson, you go:

- Sabi di MCP client-server setup.
- Know di roles and wetin Hosts, Clients, and Servers dey do.
- Understand di main features wey make MCP flexible for integration.
- Learn how information dey waka inside di MCP system.
- See practical examples with code for .NET, Java, Python, and JavaScript.

## MCP Architecture: Look Am Well

Di MCP system dey use client-server model. Dis kind setup make AI apps fit connect with tools, databases, APIs, and other resources well. Make we break am down.

For di base, MCP dey follow client-server setup where one host app fit connect to plenty servers:

```mermaid
flowchart LR
    subgraph "Your Computer"
        Host["Host with MCP (Visual Studio, VS Code, IDEs, Tools)"]
        S1["MCP Server A"]
        S2["MCP Server B"]
        S3["MCP Server C"]
        Host <-->|"MCP Protocol"| S1
        Host <-->|"MCP Protocol"| S2
        Host <-->|"MCP Protocol"| S3
        S1 <--> D1[("Local\Data Source A")]
        S2 <--> D2[("Local\Data Source B")]
    end
    subgraph "Internet"
        S3 <-->|"Web APIs"| D3[("Remote\Services")]
    end
```

- **MCP Hosts**: Programs like VSCode, Claude Desktop, IDEs, or AI tools wey wan access data through MCP.
- **MCP Clients**: Protocol clients wey dey connect one-on-one with servers.
- **MCP Servers**: Small programs wey dey expose specific features through di Model Context Protocol.
- **Local Data Sources**: Di files, databases, and services wey dey your computer wey MCP servers fit access securely.
- **Remote Services**: Systems wey dey online wey MCP servers fit connect to through APIs.

Di MCP Protocol dey use date-based versioning (YYYY-MM-DD format). Di current version na **2025-06-18**. You fit see di latest updates for di [protocol specification](https://modelcontextprotocol.io/specification/2025-06-18/)

### 1. Hosts

For MCP, **Hosts** na di AI apps wey users dey use to interact with di protocol. Hosts dey manage di connections to plenty MCP servers by creating MCP clients for each server. Examples of Hosts na:

- **AI Applications**: Claude Desktop, Visual Studio Code, Claude Code
- **Development Environments**: IDEs and code editors wey get MCP integration  
- **Custom Applications**: AI agents and tools wey dem build for specific purpose

**Hosts** dey do di following:

- **Manage AI Models**: Run or interact with LLMs to generate answers and manage AI workflows.
- **Handle Client Connections**: Create and manage one MCP client for each MCP server connection.
- **Control User Interface**: Manage conversation flow, user interactions, and how response go show.  
- **Security**: Manage permissions, security, and authentication.
- **User Consent**: Make sure users gree before data sharing or tool execution.

### 2. Clients

**Clients** na di part wey dey connect Hosts and MCP servers one-on-one. Each MCP client dey created by di Host to connect to one MCP server, so communication go dey organized and secure. Hosts fit connect to plenty servers at di same time because of di clients.

**Clients** dey do di following:

- **Protocol Communication**: Send JSON-RPC 2.0 requests to servers with instructions.
- **Feature Negotiation**: Agree on di features and protocol versions wey di server support.
- **Tool Execution**: Manage tool requests from models and process di results.
- **Real-time Updates**: Handle notifications and updates from servers.
- **Response Processing**: Process and format server responses for di user.

### 3. Servers

**Servers** na programs wey dey provide context, tools, and features to MCP clients. Dem fit dey run for di same machine as di Host or for another platform. Servers dey handle client requests and dey give structured responses. Dem dey expose specific features through di Model Context Protocol.

**Servers** dey do di following:

- **Feature Registration**: Show di features (resources, prompts, tools) wey dem get.
- **Request Processing**: Handle tool calls, resource requests, and prompts from clients.
- **Context Provision**: Provide information and data to make model responses better.
- **State Management**: Manage session state and handle interactions wey need memory.
- **Real-time Notifications**: Send updates about changes to di connected clients.

Anybody fit develop servers to add new features to di model, and dem fit run locally or remotely.

### 4. Server Primitives

For MCP, servers dey provide three main **primitives** wey define di basic things wey clients, hosts, and language models fit do together. Dis primitives dey show di kind information and actions wey di protocol fit handle.

MCP servers fit provide any of di following three primitives:

#### Resources 

**Resources** na data sources wey dey give information to AI apps. Dem fit be static or dynamic content wey go help di model understand and make better decisions:

- **Contextual Data**: Structured information for AI model use.
- **Knowledge Bases**: Documents, articles, manuals, and research papers.
- **Local Data Sources**: Files, databases, and local system information.  
- **External Data**: API responses, web services, and remote system data.
- **Dynamic Content**: Real-time data wey dey change based on conditions.

Resources dey identified by URIs and fit dey discovered through `resources/list` and retrieved through `resources/read` methods:

```text
file://documents/project-spec.md
database://production/users/schema
api://weather/current
```

#### Prompts

**Prompts** na templates wey dey help structure how language models dey interact. Dem dey provide standard ways to interact and workflows:

- **Template-based Interactions**: Pre-structured messages and conversation starters.
- **Workflow Templates**: Standard steps for common tasks.
- **Few-shot Examples**: Example-based templates for model instruction.
- **System Prompts**: Prompts wey define model behavior and context.
- **Dynamic Templates**: Prompts wey fit change based on di situation.

Prompts dey discovered via `prompts/list` and retrieved with `prompts/get`:

```markdown
Generate a {{task_type}} for {{product}} targeting {{audience}} with the following requirements: {{requirements}}
```

#### Tools

**Tools** na functions wey AI models fit use to do specific actions. Dem be di "verbs" for MCP, wey make models fit interact with external systems:

- **Executable Functions**: Operations wey models fit run with specific parameters.
- **External System Integration**: API calls, database queries, file operations, calculations.
- **Unique Identity**: Each tool get name, description, and parameter schema.
- **Structured I/O**: Tools dey accept validated parameters and return structured responses.
- **Action Capabilities**: Make models fit do real-world actions and get live data.

Tools dey defined with JSON Schema for parameter validation and discovered through `tools/list` and executed via `tools/call`:

```typescript
server.tool(
  "search_products", 
  {
    query: z.string().describe("Search query for products"),
    category: z.string().optional().describe("Product category filter"),
    max_results: z.number().default(10).describe("Maximum results to return")
  }, 
  async (params) => {
    // Execute search and return structured results
    return await productService.search(params);
  }
);
```

## Client Primitives

For MCP, **clients** fit provide primitives wey go allow servers request extra features from di host app. Dis client-side primitives dey make server implementations richer and interactive.

### Sampling

**Sampling** dey allow servers request language model completions from di client's AI app. Dis primitive dey make servers fit use LLM without needing their own model:

- **Model-Independent Access**: Servers fit request completions without managing model access.
- **Server-Initiated AI**: Servers fit generate content using di client's AI model.
- **Recursive LLM Interactions**: Fit handle complex cases where servers need AI help.
- **Dynamic Content Generation**: Servers fit create contextual responses using di host's model.

Sampling dey start through di `sampling/complete` method.

### Elicitation  

**Elicitation** dey allow servers request more information or confirmation from users through di client interface:

- **User Input Requests**: Servers fit ask for more info when dem need am.
- **Confirmation Dialogs**: Ask user to confirm sensitive actions.
- **Interactive Workflows**: Create step-by-step user interactions.
- **Dynamic Parameter Collection**: Collect missing or optional parameters during tool execution.

Elicitation dey happen through di `elicitation/request` method.

### Logging

**Logging** dey allow servers send structured log messages to clients for debugging, monitoring, and visibility:

- **Debugging Support**: Servers fit provide detailed logs for troubleshooting.
- **Operational Monitoring**: Send updates and performance metrics.
- **Error Reporting**: Provide error details and diagnostic info.
- **Audit Trails**: Keep logs of server operations and decisions.

Logging messages dey help make server operations clear and easy to debug.

## How Information Dey Flow for MCP

MCP dey define how information dey move between hosts, clients, servers, and models. To sabi dis flow go help you understand how user requests dey processed and how tools plus data dey join model responses.

- **Host Start Connection**  
  Di host app (like IDE or chat interface) go connect to MCP server, usually through STDIO, WebSocket, or other transport.

- **Capability Negotiation**  
  Di client (inside di host) and di server go exchange info about di features, tools, resources, and protocol versions wey dem support.

- **User Request**  
  Di user go interact with di host (e.g., type prompt or command). Di host go collect di input and send am to di client.

- **Resource or Tool Use**  
  - Di client fit request extra context or resources from di server to help di model.
  - If di model need tool (e.g., to fetch data or call API), di client go send di request to di server.

- **Server Execution**  
  Di server go handle di request, do di operation, and return di result to di client.

- **Response Generation**  
  Di client go use di server's response to create better model interaction.

- **Result Presentation**  
  Di host go show di final output to di user, including di model's text and tool results.

Dis flow dey make MCP support advanced, interactive, and context-aware AI apps by connecting models with tools and data sources.

## Protocol Architecture & Layers

MCP get two main layers wey dey work together to provide di communication framework:

### Data Layer

Di **Data Layer** dey implement di main MCP protocol using **JSON-RPC 2.0**. Dis layer dey define di message structure, meaning, and interaction patterns:

#### Main Parts:

- **JSON-RPC 2.0 Protocol**: All communication dey use JSON-RPC 2.0 message format for method calls, responses, and notifications.
- **Lifecycle Management**: E dey handle how connection go start, how dem go agree on wetin dem fit do, and how session go end between clients and servers.
- **Server Primitives**: E dey help servers provide di main functionality wey dem get through tools, resources, and prompts.
- **Client Primitives**: E dey help servers request sampling from LLMs, ask user for input, and send log messages.
- **Real-time Notifications**: E support notifications wey no dey wait for polling, so updates fit happen anytime.

#### Key Features:

- **Protocol Version Negotiation**: E dey use date-based versioning (YYYY-MM-DD) to make sure say e go work well.
- **Capability Discovery**: Clients and servers go share di features wey dem support when dem dey start connection.
- **Stateful Sessions**: E dey keep di connection state so e go fit remember context for plenty interactions.

### Transport Layer

Di **Transport Layer** dey manage how communication go happen, how messages go dey framed, and authentication between MCP participants:

#### Supported Transport Mechanisms:

1. **STDIO Transport**:
   - E dey use standard input/output streams for direct process communication.
   - E dey work well for local processes wey dey di same machine, no need network wahala.
   - Na di common way wey dem dey use for local MCP server implementations.

2. **Streamable HTTP Transport**:
   - E dey use HTTP POST for client-to-server messages.  
   - E fit use Server-Sent Events (SSE) for server-to-client streaming.
   - E dey allow remote server communication across networks.
   - E dey support standard HTTP authentication (bearer tokens, API keys, custom headers).
   - MCP dey recommend OAuth for secure token-based authentication.

#### Transport Abstraction:

Di transport layer dey hide di communication details from di data layer, so di same JSON-RPC 2.0 message format go work for all transport mechanisms. Dis abstraction dey make am easy for applications to switch between local and remote servers.

### Security Considerations

MCP implementations gatz follow some important security principles to make sure say interactions dey safe, trustworthy, and secure:

- **User Consent and Control**: Users gatz agree before any data go dey accessed or operations go happen. Dem suppose fit control wetin dem wan share and wetin dem wan authorize, with user-friendly interfaces wey go help dem review and approve activities.

- **Data Privacy**: User data no suppose dey exposed unless dem agree. E gatz dey protected with correct access controls. MCP implementations gatz make sure say unauthorized data transmission no go happen and privacy go dey intact.

- **Tool Safety**: Before any tool go run, user gatz agree. Users suppose sabi wetin di tool dey do, and strong security boundaries gatz dey to stop unsafe or unintended tool execution.

If MCP follow dis security principles, e go make sure say users go trust am, privacy go dey, and safety go dey intact while e dey allow strong AI integrations.

## Code Examples: Key Components

Below na code examples for some popular programming languages wey show how to implement key MCP server components and tools.

### .NET Example: Creating a Simple MCP Server with Tools

Dis na practical .NET code example wey dey show how to implement simple MCP server with custom tools. E dey show how to define and register tools, handle requests, and connect di server using di Model Context Protocol.

```csharp
using System;
using System.Threading.Tasks;
using ModelContextProtocol.Server;
using ModelContextProtocol.Server.Transport;
using ModelContextProtocol.Server.Tools;

public class WeatherServer
{
    public static async Task Main(string[] args)
    {
        // Create an MCP server
        var server = new McpServer(
            name: "Weather MCP Server",
            version: "1.0.0"
        );
        
        // Register our custom weather tool
        server.AddTool<string, WeatherData>("weatherTool", 
            description: "Gets current weather for a location",
            execute: async (location) => {
                // Call weather API (simplified)
                var weatherData = await GetWeatherDataAsync(location);
                return weatherData;
            });
        
        // Connect the server using stdio transport
        var transport = new StdioServerTransport();
        await server.ConnectAsync(transport);
        
        Console.WriteLine("Weather MCP Server started");
        
        // Keep the server running until process is terminated
        await Task.Delay(-1);
    }
    
    private static async Task<WeatherData> GetWeatherDataAsync(string location)
    {
        // This would normally call a weather API
        // Simplified for demonstration
        await Task.Delay(100); // Simulate API call
        return new WeatherData { 
            Temperature = 72.5,
            Conditions = "Sunny",
            Location = location
        };
    }
}

public class WeatherData
{
    public double Temperature { get; set; }
    public string Conditions { get; set; }
    public string Location { get; set; }
}
```

### Java Example: MCP Server Components

Dis example dey show di same MCP server and tool registration like di .NET example above, but e dey use Java.

```java
import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpToolDefinition;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.server.tool.ToolExecutionContext;
import io.modelcontextprotocol.server.tool.ToolResponse;

public class WeatherMcpServer {
    public static void main(String[] args) throws Exception {
        // Create an MCP server
        McpServer server = McpServer.builder()
            .name("Weather MCP Server")
            .version("1.0.0")
            .build();
            
        // Register a weather tool
        server.registerTool(McpToolDefinition.builder("weatherTool")
            .description("Gets current weather for a location")
            .parameter("location", String.class)
            .execute((ToolExecutionContext ctx) -> {
                String location = ctx.getParameter("location", String.class);
                
                // Get weather data (simplified)
                WeatherData data = getWeatherData(location);
                
                // Return formatted response
                return ToolResponse.content(
                    String.format("Temperature: %.1f°F, Conditions: %s, Location: %s", 
                    data.getTemperature(), 
                    data.getConditions(), 
                    data.getLocation())
                );
            })
            .build());
        
        // Connect the server using stdio transport
        try (StdioServerTransport transport = new StdioServerTransport()) {
            server.connect(transport);
            System.out.println("Weather MCP Server started");
            // Keep server running until process is terminated
            Thread.currentThread().join();
        }
    }
    
    private static WeatherData getWeatherData(String location) {
        // Implementation would call a weather API
        // Simplified for example purposes
        return new WeatherData(72.5, "Sunny", location);
    }
}

class WeatherData {
    private double temperature;
    private String conditions;
    private String location;
    
    public WeatherData(double temperature, String conditions, String location) {
        this.temperature = temperature;
        this.conditions = conditions;
        this.location = location;
    }
    
    public double getTemperature() {
        return temperature;
    }
    
    public String getConditions() {
        return conditions;
    }
    
    public String getLocation() {
        return location;
    }
}
```

### Python Example: Building an MCP Server

Dis example dey use fastmcp, so make sure say you don install am first:

```python
pip install fastmcp
```
Code Sample:

```python
#!/usr/bin/env python3
import asyncio
from fastmcp import FastMCP
from fastmcp.transports.stdio import serve_stdio

# Create a FastMCP server
mcp = FastMCP(
    name="Weather MCP Server",
    version="1.0.0"
)

@mcp.tool()
def get_weather(location: str) -> dict:
    """Gets current weather for a location."""
    return {
        "temperature": 72.5,
        "conditions": "Sunny",
        "location": location
    }

# Alternative approach using a class
class WeatherTools:
    @mcp.tool()
    def forecast(self, location: str, days: int = 1) -> dict:
        """Gets weather forecast for a location for the specified number of days."""
        return {
            "location": location,
            "forecast": [
                {"day": i+1, "temperature": 70 + i, "conditions": "Partly Cloudy"}
                for i in range(days)
            ]
        }

# Register class tools
weather_tools = WeatherTools()

# Start the server
if __name__ == "__main__":
    asyncio.run(serve_stdio(mcp))
```

### JavaScript Example: Creating an MCP Server

Dis example dey show how to create MCP server with JavaScript and how to register two tools wey dey related to weather.

```javascript
// Using the official Model Context Protocol SDK
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod"; // For parameter validation

// Create an MCP server
const server = new McpServer({
  name: "Weather MCP Server",
  version: "1.0.0"
});

// Define a weather tool
server.tool(
  "weatherTool",
  {
    location: z.string().describe("The location to get weather for")
  },
  async ({ location }) => {
    // This would normally call a weather API
    // Simplified for demonstration
    const weatherData = await getWeatherData(location);
    
    return {
      content: [
        { 
          type: "text", 
          text: `Temperature: ${weatherData.temperature}°F, Conditions: ${weatherData.conditions}, Location: ${weatherData.location}` 
        }
      ]
    };
  }
);

// Define a forecast tool
server.tool(
  "forecastTool",
  {
    location: z.string(),
    days: z.number().default(3).describe("Number of days for forecast")
  },
  async ({ location, days }) => {
    // This would normally call a weather API
    // Simplified for demonstration
    const forecast = await getForecastData(location, days);
    
    return {
      content: [
        { 
          type: "text", 
          text: `${days}-day forecast for ${location}: ${JSON.stringify(forecast)}` 
        }
      ]
    };
  }
);

// Helper functions
async function getWeatherData(location) {
  // Simulate API call
  return {
    temperature: 72.5,
    conditions: "Sunny",
    location: location
  };
}

async function getForecastData(location, days) {
  // Simulate API call
  return Array.from({ length: days }, (_, i) => ({
    day: i + 1,
    temperature: 70 + Math.floor(Math.random() * 10),
    conditions: i % 2 === 0 ? "Sunny" : "Partly Cloudy"
  }));
}

// Connect the server using stdio transport
const transport = new StdioServerTransport();
server.connect(transport).catch(console.error);

console.log("Weather MCP Server started");
```

Dis JavaScript example dey show how to create MCP client wey go connect to server, send prompt, and process di response including any tool calls wey dem make.

## Security and Authorization

MCP get some built-in ways to manage security and authorization for di protocol:

1. **Tool Permission Control**:  
  Clients fit decide which tools di model fit use during session. Dis one dey make sure say only tools wey dem authorize go dey accessible, e dey reduce risk of unsafe operations. Permissions fit dey change based on user preferences, organization policies, or di interaction context.

2. **Authentication**:  
  Servers fit require authentication before dem go allow access to tools, resources, or sensitive operations. E fit involve API keys, OAuth tokens, or other authentication methods. Dis one dey make sure say only trusted clients and users fit use di server capabilities.

3. **Validation**:  
  Parameter validation dey enforced for all tool calls. Each tool go define di expected types, formats, and constraints for di parameters, and di server go check di requests wey dey come. Dis one dey stop bad or malicious input from reaching di tools and e dey protect operations.

4. **Rate Limiting**:  
  To stop abuse and make sure say server resources dey used well, MCP servers fit limit how many times tools fit dey called or resources fit dey accessed. Rate limits fit dey per user, per session, or globally, e dey help stop denial-of-service attacks or too much resource usage.

With all dis mechanisms, MCP dey provide secure way to connect language models with tools and data sources, while e dey give users and developers control over access and usage.

## Protocol Messages & Communication Flow

MCP dey use structured **JSON-RPC 2.0** messages to make sure say communication between hosts, clients, and servers dey clear and reliable. Di protocol don define specific message patterns for different operations:

### Core Message Types:

#### **Initialization Messages**
- **`initialize` Request**: E dey start connection and dey negotiate protocol version and capabilities.
- **`initialize` Response**: E dey confirm di features wey e support and server information.  
- **`notifications/initialized`**: E dey signal say initialization don complete and session don ready.

#### **Discovery Messages**
- **`tools/list` Request**: E dey find di tools wey dey available from di server.
- **`resources/list` Request**: E dey list di resources (data sources) wey dey available.
- **`prompts/list` Request**: E dey collect di prompt templates wey dey available.

#### **Execution Messages**  
- **`tools/call` Request**: E dey run specific tool with di parameters wey dem provide.
- **`resources/read` Request**: E dey collect content from specific resource.
- **`prompts/get` Request**: E dey fetch prompt template with optional parameters.

#### **Client-side Messages**
- **`sampling/complete` Request**: Server dey request LLM completion from di client.
- **`elicitation/request`**: Server dey ask user for input through di client interface.
- **Logging Messages**: Server dey send structured log messages to di client.

#### **Notification Messages**
- **`notifications/tools/list_changed`**: Server dey notify client say tools don change.
- **`notifications/resources/list_changed`**: Server dey notify client say resources don change.  
- **`notifications/prompts/list_changed`**: Server dey notify client say prompts don change.

### Message Structure:

All MCP messages dey follow JSON-RPC 2.0 format with:
- **Request Messages**: Dem get `id`, `method`, and optional `params`.
- **Response Messages**: Dem get `id` and either `result` or `error`.  
- **Notification Messages**: Dem get `method` and optional `params` (no `id` or response dey expected).

Dis structured communication dey make sure say interactions dey reliable, traceable, and fit extend for advanced scenarios like real-time updates, tool chaining, and error handling.

## Key Takeaways

- **Architecture**: MCP dey use client-server architecture wey hosts dey manage plenty client connections to servers.
- **Participants**: Di ecosystem get hosts (AI applications), clients (protocol connectors), and servers (capability providers).
- **Transport Mechanisms**: Communication dey support STDIO (local) and Streamable HTTP with optional SSE (remote).
- **Core Primitives**: Servers dey expose tools (functions wey fit run), resources (data sources), and prompts (templates).
- **Client Primitives**: Servers fit request sampling (LLM completions), elicitation (user input), and logging from clients.
- **Protocol Foundation**: E dey use JSON-RPC 2.0 with date-based versioning (current: 2025-06-18).
- **Real-time Capabilities**: E dey support notifications for updates wey dey happen anytime and real-time synchronization.
- **Security First**: User gatz agree, data privacy gatz dey protected, and transport gatz dey secure.

## Exercise

Design one simple MCP tool wey go dey useful for your area. Define:
1. Wetin di tool go dey called.
2. Wetin parameters e go accept.
3. Wetin output e go return.
4. How model fit use dis tool solve user problems.


---

## Wetin go happen next

Next: [Chapter 2: Security](../02-Security/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important mata, e good make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->