# Getting Started with MCP

## Overview 

This lesson provides practical guidance on setting up MCP environments and building your first MCP applications. You'll learn how to set up the necessary tools and frameworks, build basic MCP servers and clients, and test your implementations.

## Learning Objectives

By the end of this lesson, you will be able to:
- Set up development environments for MCP in .NET, Java, and Python
- Build and deploy basic MCP servers with custom tools
- Create MCP clients that connect to servers and models
- Test and debug MCP implementations
- Understand common setup challenges and their solutions

## Setting Up Your MCP Environment

### Prerequisites

Before diving into MCP development, ensure you have:

1. **Development Environment**: For your chosen language (.NET, Java, or Python)
2. **IDE/Editor**: Visual Studio, VS Code, IntelliJ, Eclipse, or PyCharm
3. **Package Managers**: NuGet, Maven/Gradle, or pip
4. **API Keys**: For any AI services you plan to use (e.g., Azure OpenAI Service)

### Installation and Setup

#### .NET Setup

```csharp
// Create a new .NET project for your MCP server
dotnet new webapi -n McpDotNetServer

// Change to the project directory
cd McpDotNetServer

// Add the MCP NuGet packages
dotnet add package Microsoft.Mcp.Server
dotnet add package Microsoft.Mcp.Tools
```

#### Java Setup

```bash
# Using Maven - Create a new Java project with Maven
mvn archetype:generate -DgroupId=com.example.mcp -DartifactId=mcp-java-server -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# Add MCP dependencies to pom.xml
<dependencies>
    <dependency>
        <groupId>com.mcp</groupId>
        <artifactId>mcp-server</artifactId>
        <version>1.0.0</version>
    </dependency>
</dependencies>
```

#### Python Setup

```bash
# Create a virtual environment
python -m venv mcp-env

# Activate the virtual environment
# On Windows:
mcp-env\Scripts\activate
# On macOS/Linux:
source mcp-env/bin/activate

# Install MCP packages
pip install mcp-server mcp-client
```

## Creating Your First MCP Server

An MCP server provides tools that extend the capabilities of AI models. Let's start by creating a simple MCP server with a calculator tool.

### .NET Implementation

```csharp
using Microsoft.Mcp.Server;
using Microsoft.Mcp.Tools;
using System.Text.Json;

namespace McpCalculatorServer
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            
            // Add MCP services
            builder.Services.AddMcpServer(options => {
                options.ServerName = "Calculator MCP Server";
                options.ServerVersion = "1.0.0";
            });
            
            // Register calculator tool
            builder.Services.AddMcpTool<CalculatorTool>();
            
            var app = builder.Build();
            
            // Configure the MCP middleware pipeline
            app.UseMcpServer();
            
            app.Run("http://localhost:5000");
        }
    }
    
    public class CalculatorTool : IMcpTool
    {
        public string Name => "calculator";
        public string Description => "Performs basic arithmetic operations";
        
        public object GetSchema()
        {
            return new {
                type = "object",
                properties = new {
                    operation = new {
                        type = "string",
                        enum = new[] { "add", "subtract", "multiply", "divide" }
                    },
                    a = new { type = "number" },
                    b = new { type = "number" }
                },
                required = new[] { "operation", "a", "b" }
            };
        }
        
        public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
        {
            // Parse parameters
            var operation = request.Parameters.GetProperty("operation").GetString();
            var a = request.Parameters.GetProperty("a").GetDouble();
            var b = request.Parameters.GetProperty("b").GetDouble();
            
            double result = 0;
            
            // Perform calculation
            switch (operation)
            {
                case "add":
                    result = a + b;
                    break;
                case "subtract":
                    result = a - b;
                    break;
                case "multiply":
                    result = a * b;
                    break;
                case "divide":
                    if (b == 0)
                        throw new ToolExecutionException("Cannot divide by zero");
                    result = a / b;
                    break;
                default:
                    throw new ToolExecutionException($"Unknown operation: {operation}");
            }
            
            // Return result
            return new ToolResponse {
                Result = JsonSerializer.SerializeToElement(new { result })
            };
        }
    }
}
```

### Java Implementation

```java
package com.example.mcp;

import com.mcp.server.McpServer;
import com.mcp.tools.Tool;
import com.mcp.tools.ToolRequest;
import com.mcp.tools.ToolResponse;
import com.mcp.tools.ToolExecutionException;

public class CalculatorServer {
    public static void main(String[] args) {
        // Create and configure MCP server
        McpServer server = new McpServer.Builder()
            .setName("Calculator MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .build();
        
        // Register calculator tool
        server.registerTool(new CalculatorTool());
        
        // Start server
        server.start();
        System.out.println("Calculator MCP Server started on port 5000");
    }
}

class CalculatorTool implements Tool {
    @Override
    public String getName() {
        return "calculator";
    }
    
    @Override
    public String getDescription() {
        return "Performs basic arithmetic operations";
    }
    
    @Override
    public Object getSchema() {
        // Define parameter schema
        Map<String, Object> schema = new HashMap<>();
        schema.put("type", "object");
        
        Map<String, Object> properties = new HashMap<>();
        
        Map<String, Object> operation = new HashMap<>();
        operation.put("type", "string");
        operation.put("enum", Arrays.asList("add", "subtract", "multiply", "divide"));
        properties.put("operation", operation);
        
        Map<String, Object> a = new HashMap<>();
        a.put("type", "number");
        properties.put("a", a);
        
        Map<String, Object> b = new HashMap<>();
        b.put("type", "number");
        properties.put("b", b);
        
        schema.put("properties", properties);
        schema.put("required", Arrays.asList("operation", "a", "b"));
        
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        // Extract parameters
        String operation = request.getParameters().get("operation").asText();
        double a = request.getParameters().get("a").asDouble();
        double b = request.getParameters().get("b").asDouble();
        
        double result = 0;
        
        // Perform calculation
        switch (operation) {
            case "add":
                result = a + b;
                break;
            case "subtract":
                result = a - b;
                break;
            case "multiply":
                result = a * b;
                break;
            case "divide":
                if (b == 0) {
                    throw new ToolExecutionException("Cannot divide by zero");
                }
                result = a / b;
                break;
            default:
                throw new ToolExecutionException("Unknown operation: " + operation);
        }
        
        // Create response
        Map<String, Object> response = new HashMap<>();
        response.put("result", result);
        
        return new ToolResponse.Builder()
            .setResult(response)
            .build();
    }
}
```

### Python Implementation

```python
from mcp_server import McpServer
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
import json

class CalculatorTool(Tool):
    def get_name(self):
        return "calculator"
        
    def get_description(self):
        return "Performs basic arithmetic operations"
    
    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract", "multiply", "divide"]
                },
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["operation", "a", "b"]
        }
    
    def execute(self, request: ToolRequest) -> ToolResponse:
        # Extract parameters
        params = request.parameters
        operation = params.get("operation")
        a = params.get("a")
        b = params.get("b")
        
        # Perform calculation
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                raise ToolExecutionException("Cannot divide by zero")
            result = a / b
        else:
            raise ToolExecutionException(f"Unknown operation: {operation}")
        
        # Return result
        return ToolResponse(
            result={"result": result}
        )

# Create and start server
if __name__ == "__main__":
    # Initialize server
    server = McpServer(
        name="Calculator MCP Server",
        version="1.0.0",
        port=5000
    )
    
    # Register tools
    server.register_tool(CalculatorTool())
    
    # Start server
    server.start()
    print("Calculator MCP Server running on port 5000")
```

## Building an MCP Client

Now let's create a client application that connects to our MCP server and uses the calculator tool.

### .NET Client

```csharp
using Microsoft.Mcp.Client;
using System;
using System.Threading.Tasks;

namespace McpCalculatorClient
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Create MCP client
            var client = new McpClient("http://localhost:5000");
            
            // Define a prompt that requires calculation
            string prompt = "What is 135 * 28?";
            
            Console.WriteLine($"User: {prompt}");
            
            // Send request with access to the calculator tool
            var response = await client.SendPromptAsync(prompt, 
                new McpToolOptions { AllowedTools = ["calculator"] });
            
            Console.WriteLine($"AI: {response.GeneratedText}");
            
            // Display tool usage information
            if (response.ToolCalls?.Count > 0)
            {
                Console.WriteLine("\nTool calls made:");
                foreach (var toolCall in response.ToolCalls)
                {
                    Console.WriteLine($"- {toolCall.ToolName} with parameters: {toolCall.Parameters}");
                    Console.WriteLine($"  Result: {toolCall.Result}");
                }
            }
        }
    }
}
```

### Java Client

```java
package com.example.mcp.client;

import com.mcp.client.McpClient;
import com.mcp.models.McpRequest;
import com.mcp.models.McpResponse;
import com.mcp.models.McpToolCall;

public class CalculatorClient {
    public static void main(String[] args) {
        // Create MCP client
        McpClient client = new McpClient.Builder()
            .setServerUrl("http://localhost:5000")
            .build();
            
        // Define prompt
        String prompt = "What is 135 * 28?";
        
        System.out.println("User: " + prompt);
        
        // Create request
        McpRequest request = new McpRequest.Builder()
            .setPrompt(prompt)
            .addTool("calculator")
            .build();
            
        // Send request and get response
        McpResponse response = client.sendRequest(request);
        
        // Display response
        System.out.println("AI: " + response.getGeneratedText());
        
        // Display tool usage information
        if (!response.getToolCalls().isEmpty()) {
            System.out.println("\nTool calls made:");
            for (McpToolCall toolCall : response.getToolCalls()) {
                System.out.println("- " + toolCall.getToolName() + 
                    " with parameters: " + toolCall.getParameters());
                System.out.println("  Result: " + toolCall.getResult());
            }
        }
    }
}
```

### Python Client

```python
from mcp_client import McpClient

# Initialize the MCP client
client = McpClient(server_url="http://localhost:5000")

# Define prompt
prompt = "What is 135 * 28?"

print(f"User: {prompt}")

# Send the request to the MCP server
response = client.send_prompt(
    prompt=prompt,
    allowed_tools=["calculator"]
)

# Display response
print(f"AI: {response.generated_text}")

# Display tool usage information
if response.tool_calls:
    print("\nTool calls made:")
    for tool_call in response.tool_calls:
        print(f"- {tool_call.tool_name} with parameters: {tool_call.parameters}")
        print(f"  Result: {tool_call.result}")
```

## Testing and Debugging

### Testing MCP Servers

To ensure your MCP server works correctly:

1. **Direct API Testing**:
   - Use tools like Postman or cURL to send requests directly to your MCP server
   - Verify tool schemas and execution paths

2. **MCP Inspector Tool**:
   ```bash
   # Install MCP Inspector (Python)
   pip install mcp-inspector
   
   # Launch inspector
   mcp-inspector --server-url http://localhost:5000
   ```

3. **Unit Tests**:
   - Test each tool independently
   - Validate parameter validation and error handling

### Common Setup Issues and Solutions

| Issue | Possible Solution |
|-------|-------------------|
| Connection refused | Check if server is running and port is correct |
| Tool execution errors | Review parameter validation and error handling |
| Authentication failures | Verify API keys and permissions |
| Schema validation errors | Ensure parameters match the defined schema |
| Server not starting | Check for port conflicts or missing dependencies |

## Deploying MCP Servers

### Local Development

For local testing and development, run MCP servers directly in your IDE or terminal.

### Container Deployment

Use Docker for containerized deployment:

```dockerfile
# Dockerfile for Python MCP Server
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "calculator_server.py"]
```

### Cloud Deployment

Deploy MCP servers to cloud platforms:

1. **Azure App Service**:
   - Supports .NET, Java, and Python
   - Easy integration with Azure services

2. **AWS Lambda**:
   - Serverless deployment option
   - Pay-per-use pricing model

3. **Kubernetes**:
   - For high-availability deployments
   - Scalable and resilient

## Exploring Pre-Built Integrations

Several pre-built MCP integrations are available:

1. **Azure OpenAI MCP Host**:
   - Connects to Azure OpenAI models
   - Supports tool calling capabilities

2. **Hugging Face Integration**:
   - Uses open-source models
   - Local deployment options

3. **Database Connectors**:
   - SQL and NoSQL database tools
   - Data retrieval and manipulation

## Key Takeaways

- Setting up an MCP development environment is straightforward with language-specific SDKs
- Building MCP servers involves creating and registering tools with clear schemas
- MCP clients connect to servers and models to leverage extended capabilities
- Testing and debugging are essential for reliable MCP implementations
- Deployment options range from local development to cloud-based solutions

## Exercise

Create a simple MCP server with a tool of your choice:
1. Implement the tool in your preferred language (.NET, Java, or Python)
2. Define input parameters and return values
3. Build a simple client that uses your tool
4. Test the implementation with various inputs

## Additional Resources

- [MCP GitHub Repository](https://github.com/microsoft/mcp-for-beginners)

---

Next: [Practical Implementation](../03-PracticalImplementation/README.md)
