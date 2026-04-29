# Getting Started with MCP

Welcome to your first steps with the Model Context Protocol (MCP)! Whether you new to MCP or you wan sabi am well well, dis guide go carry you waka through the important setup and development process. You go learn how MCP dey enable ai models and applications to work well well together, and how to quick quick ready your environment to build and test MCP-powered solutions.

> TLDR; If you dey build AI apps, you sabi say you fit add tools and other resources to your LLM (large language model), to make the LLM sabi pass before. But if you put those tools and resources for one server, the app and the server fit be used by any client, whether dem get LLM or no get.

## Overview

Dis lesson go show you how to set up MCP environments and build your first MCP apps. You go learn how to set up the tools and frameworks wey you need, build basic MCP servers, create host apps, and test how you implement dem.

The Model Context Protocol (MCP) na open protocol wey standardize how applications go provide context to LLMs. Think of MCP like USB-C port for AI apps - e dey give one standard way to connect AI models to different data sources and tools.

## Learning Objectives

By the time you finish dis lesson, you go fit:

- Set up development environments for MCP for C#, Java, Python, TypeScript, and Rust
- Build and deploy basic MCP servers with custom features (resources, prompts, and tools)
- Create host applications wey go connect to MCP servers
- Test and debug MCP implementations

## Setting Up Your MCP Environment

Before you start to work with MCP, e get as e be say you go first prepare your development environment and understand the basic way wey e go flow. Dis section go guide you through the first setup steps to make sure say you start well with MCP.

### Prerequisites

Before you dive into MCP development, make sure say you get:

- **Development Environment**: For your chosen language (C#, Java, Python, TypeScript, or Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, or any modern code editor
- **Package Managers**: NuGet, Maven/Gradle, pip, npm/yarn, or Cargo
- **API Keys**: For any AI services wey you plan to use inside your host apps

## Basic MCP Server Structure

One MCP server normally get:

- **Server Configuration**: Setup port, authentication, and other settings
- **Resources**: Data and context wey LLMs fit use
- **Tools**: Wetin models fit call to do work
- **Prompts**: Templates to generate or organize text

See example wey simple for TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Make one MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add one addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add one dynamic greeting resource
server.resource(
  "file",
  // Di 'list' parameter dey control how di resource dey list di files wey dey available. If you set am to undefined, e go stop di listing for dis resource.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Add one file resource wey go read di file contents
server.resource(
  "file",
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => {
    let text;
    try {
      text = await fs.readFile(path, "utf8");
    } catch (err) {
      text = `Error reading file: ${err.message}`;
    }
    return {
      contents: [{
        uri: uri.href,
        text
      }]
    };
  }
);

server.prompt(
  "review-code",
  { code: z.string() },
  ({ code }) => ({
    messages: [{
      role: "user",
      content: {
        type: "text",
        text: `Please review this code:\n\n${code}`
      }
    }]
  })
);

// Start to dey receive messages for stdin and dey send messages for stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

For the code we show before, we:

- Import the necessary classes from the MCP TypeScript SDK.
- Create and configure one new MCP server instance.
- Register one custom tool (`calculator`) with a handler function.
- Start the server to listen for incoming MCP requests.

## Testing and Debugging

Before you begin to test your MCP server, e good make you sabi the tools wey dey and the best way to debug. Testing well go make sure say your server dey work as e suppose and e go help you find and fix wahala quick. The next section go talk about the correct ways to check if your MCP implementation dey okay.

MCP get tools to help you test and debug your servers:

- **Inspector tool**, dis graphical interface dey allow you connect to your server and test your tools, prompts and resources.
- **curl**, you fit also connect to your server with command line tool like curl or other clients wey fit create and run HTTP commands.

### Using MCP Inspector

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) na visual testing tool wey go help you:

1. **Discover Server Capabilities**: Automatically detect available resources, tools, and prompts
2. **Test Tool Execution**: Try different parameters and see responses in real-time
3. **View Server Metadata**: Check server info, schemas, and configurations

```bash
# ex TypeScript, di way wey you go take install an run MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

When you run those commands, the MCP Inspector go open one local web interface for your browser. You fit expect to see dashboard wey dey show your registered MCP servers, their available tools, resources, and prompts. The interface go help you test tool execution, inspect server metadata, and see real-time responses, e go make am easy to check and debug your MCP server implementations.

See one screenshot of how e fit be:

![MCP Inspector server connection](../../../../translated_images/pcm/connected.73d1e042c24075d3.webp)

## Common Setup Issues and Solutions

| Issue | Possible Solution |
|-------|-------------------|
| Connection refused | Check if server dey run and port dey correct |
| Tool execution errors | Review parameter validation and error handling |
| Authentication failures | Check API keys and permissions |
| Schema validation errors | Make sure parameters match the defined schema |
| Server not starting | Check for port wahala or missing dependencies |
| CORS errors | Configure correct CORS headers for cross-origin requests |
| Authentication issues | Check token validity and permissions |

## Local Development

For local development and testing, you fit run MCP servers direct for your machine:

1. **Start the server process**: Run your MCP server app
2. **Configure networking**: Make sure the server fit dey accessible on the port wey you expect
3. **Connect clients**: Use local connection URLs like `http://localhost:3000`

```bash
# Exampul: De run TypeScript MCP server for local area
npm run start
# Server dey run for http://localhost:3000
```

## Building your first MCP Server

We don talk about [Core concepts](../../01-CoreConcepts/README.md) for one previous lesson, now na time to put that wah knowledge to work.

### Wetin one server fit do

Before we start to write code, make we just remember wetin one server fit do:

MCP server fit for example:

- Access local files and databases
- Connect to remote APIs
- Perform calculations
- Join with other tools and services
- Provide user interface for interaction

Good, now we sabi wetin e fit do, make we start to write code.

## Exercise: Creating a server

To create server, you need follow these steps:

- Install the MCP SDK.
- Create one project and set up the project structure.
- Write the server code.
- Test the server.

### -1- Create project

#### TypeScript

```sh
# Make project folder and start npm project
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Make project folder
mkdir calculator-server
cd calculator-server
# Open di folder for Visual Studio Code - No do dis if you use oda IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

For Java, create one Spring Boot project:

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d javaVersion=21 \
  -d type=maven-project \
  -d groupId=com.example \
  -d artifactId=calculator-server \
  -d name=McpServer \
  -d packageName=com.microsoft.mcp.sample.server \
  -o calculator-server.zip
```

Extract the zip file:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# if you want fit remove di test wey no dey use
rm -rf src/test/java
```

Add this complete configuration to your *pom.xml* file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Spring Boot parent for dependency management -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.0</version>
        <relativePath />
    </parent>

    <!-- Project coordinates -->
    <groupId>com.example</groupId>
    <artifactId>calculator-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>Calculator Server</name>
    <description>Basic calculator MCP service for beginners</description>

    <!-- Properties -->
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>

    <!-- Spring AI BOM for version management -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>1.0.0-SNAPSHOT</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- Dependencies -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
    </dependencies>

    <!-- Build configuration -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <release>21</release>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Repositories for Spring AI snapshots -->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <releases>
                <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>
</project>
```

#### Rust

```sh
mkdir calculator-server
cd calculator-server
cargo init
```

### -2- Add dependencies

Now wey you don create your project, make we add dependencies next:

#### TypeScript

```sh
# If you never install am before, make you install TypeScript for everywhere
npm install typescript -g

# Make you install the MCP SDK and Zod to check schema correct correct
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Make virtual environment and install di tins wey e need
python -m venv venv
venv\Scripts\activate
pip install "mcp[cli]"
```

#### Java

```bash
cd calculator-server
./mvnw clean install -DskipTests
```

#### Rust

```sh
cargo add rmcp --features server,transport-io
cargo add serde
cargo add tokio --features rt-multi-thread
```

### -3- Create project files

#### TypeScript

Open the *package.json* file and replace the content with this one below to make sure say you fit build and run the server:

```json
{
  "name": "calculator-server",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "npm run build && node ./build/index.js",
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "A simple calculator server using Model Context Protocol",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.16.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/node": "^24.0.14",
    "typescript": "^5.8.3"
  }
}
```

Create *tsconfig.json* with this content:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

Create one directory for your source code:

```sh
mkdir src
touch src/index.ts
```

#### Python

Create file *server.py*

```sh
touch server.py
```

#### .NET

Install the required NuGet packages:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

For Java Spring Boot project, the project structure go create automatically.

#### Rust

For Rust, *src/main.rs* file go dey create by default when you run `cargo init`. Open the file and delete the default code.

### -4- Create server code

#### TypeScript

Create *index.ts* file and put the following code:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Make one MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Now you get server, but e no do much, make we fix am.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Mak one MCP server
mcp = FastMCP("Demo")
```

#### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

// add features
```

#### Java

For Java, create the core server parts. First, change the main application class:

*src/main/java/com/microsoft/mcp/sample/server/McpServerApplication.java*:

```java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

Create the calculator service *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

```java
package com.microsoft.mcp.sample.server.service;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

/**
 * Service for basic calculator operations.
 * This service provides simple calculator functionality through MCP.
 */
@Service
public class CalculatorService {

    /**
     * Add two numbers
     * @param a The first number
     * @param b The second number
     * @return The sum of the two numbers
     */
    @Tool(description = "Add two numbers together")
    public String add(double a, double b) {
        double result = a + b;
        return formatResult(a, "+", b, result);
    }

    /**
     * Subtract one number from another
     * @param a The number to subtract from
     * @param b The number to subtract
     * @return The result of the subtraction
     */
    @Tool(description = "Subtract the second number from the first number")
    public String subtract(double a, double b) {
        double result = a - b;
        return formatResult(a, "-", b, result);
    }

    /**
     * Multiply two numbers
     * @param a The first number
     * @param b The second number
     * @return The product of the two numbers
     */
    @Tool(description = "Multiply two numbers together")
    public String multiply(double a, double b) {
        double result = a * b;
        return formatResult(a, "*", b, result);
    }

    /**
     * Divide one number by another
     * @param a The numerator
     * @param b The denominator
     * @return The result of the division
     */
    @Tool(description = "Divide the first number by the second number")
    public String divide(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a / b;
        return formatResult(a, "/", b, result);
    }

    /**
     * Calculate the power of a number
     * @param base The base number
     * @param exponent The exponent
     * @return The result of raising the base to the exponent
     */
    @Tool(description = "Calculate the power of a number (base raised to an exponent)")
    public String power(double base, double exponent) {
        double result = Math.pow(base, exponent);
        return formatResult(base, "^", exponent, result);
    }

    /**
     * Calculate the square root of a number
     * @param number The number to find the square root of
     * @return The square root of the number
     */
    @Tool(description = "Calculate the square root of a number")
    public String squareRoot(double number) {
        if (number < 0) {
            return "Error: Cannot calculate square root of a negative number";
        }
        double result = Math.sqrt(number);
        return String.format("√%.2f = %.2f", number, result);
    }

    /**
     * Calculate the modulus (remainder) of division
     * @param a The dividend
     * @param b The divisor
     * @return The remainder of the division
     */
    @Tool(description = "Calculate the remainder when one number is divided by another")
    public String modulus(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a % b;
        return formatResult(a, "%", b, result);
    }

    /**
     * Calculate the absolute value of a number
     * @param number The number to find the absolute value of
     * @return The absolute value of the number
     */
    @Tool(description = "Calculate the absolute value of a number")
    public String absolute(double number) {
        double result = Math.abs(number);
        return String.format("|%.2f| = %.2f", number, result);
    }

    /**
     * Get help about available calculator operations
     * @return Information about available operations
     */
    @Tool(description = "Get help about available calculator operations")
    public String help() {
        return "Basic Calculator MCP Service\n\n" +
               "Available operations:\n" +
               "1. add(a, b) - Adds two numbers\n" +
               "2. subtract(a, b) - Subtracts the second number from the first\n" +
               "3. multiply(a, b) - Multiplies two numbers\n" +
               "4. divide(a, b) - Divides the first number by the second\n" +
               "5. power(base, exponent) - Raises a number to a power\n" +
               "6. squareRoot(number) - Calculates the square root\n" + 
               "7. modulus(a, b) - Calculates the remainder of division\n" +
               "8. absolute(number) - Calculates the absolute value\n\n" +
               "Example usage: add(5, 3) will return 5 + 3 = 8";
    }

    /**
     * Format the result of a calculation
     */
    private String formatResult(double a, String operator, double b, double result) {
        return String.format("%.2f %s %.2f = %.2f", a, operator, b, result);
    }
}
```

**Optional parts for a production-ready service:**

Create startup config *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

```java
package com.microsoft.mcp.sample.server.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StartupConfig {
    
    @Bean
    public CommandLineRunner startupInfo() {
        return args -> {
            System.out.println("\n" + "=".repeat(60));
            System.out.println("Calculator MCP Server is starting...");
            System.out.println("SSE endpoint: http://localhost:8080/sse");
            System.out.println("Health check: http://localhost:8080/actuator/health");
            System.out.println("=".repeat(60) + "\n");
        };
    }
}
```

Create health controller *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

```java
package com.microsoft.mcp.sample.server.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestController
public class HealthController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "UP");
        response.put("timestamp", LocalDateTime.now().toString());
        response.put("service", "Calculator MCP Server");
        return ResponseEntity.ok(response);
    }
}
```

Create exception handler *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

```java
package com.microsoft.mcp.sample.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleIllegalArgumentException(IllegalArgumentException ex) {
        ErrorResponse error = new ErrorResponse(
            "Invalid_Input", 
            "Invalid input parameter: " + ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }

    public static class ErrorResponse {
        private String code;
        private String message;

        public ErrorResponse(String code, String message) {
            this.code = code;
            this.message = message;
        }

        // Di getters dem
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Create custom banner *src/main/resources/banner.txt*:

```text
_____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
Calculator MCP Server v1.0
Spring Boot MCP Application
```

</details>

#### Rust

Add dis code to the top of *src/main.rs* file. E go import the libraries and modules wey your MCP server need.

```rust
use rmcp::{
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
    ServerHandler, ServiceExt,
};
use std::error::Error;
```

The calculator server go simple one wey go add two numbers join. Make we create struct to represent calculator request.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Next, create struct to represent the calculator server. Dis struct go hold tool router, wey dey register tools.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Now, we fit implement the `Calculator` struct to create new server instance and implement server handler to give server info.

```rust
#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}
```

Finally, we go implement main function to start the server. Dis one go create `Calculator` instance and serve am over standard input/output.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

The server don ready to give basic info about itself. Next, we go add tool to do addition.

### -5- Adding a tool and a resource

Add tool and resource by adding this code:

#### TypeScript

```typescript
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);
```

Your tool dey take parameters `a` and `b` and run function wey produce response like:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Your resource go dey accessed through string "greeting" and e go take parameter `name` and produce response like the tool:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Add one tool for add tins
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add one dynamic greet resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

For the code wey pass before we:

- Define tool `add` wey dey take parameters `a` and `b`, both na integers.
- Create resource called `greeting` wey dey take parameter `name`.

#### .NET

Add dis one for your Program.cs file:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Tools don already create for the previous step.

#### Rust

Add new tool inside `impl Calculator` block:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Final code

Make we add the last code wey we need so the server fit start:

#### TypeScript

```typescript
// Strat to dey receive messages for stdin and dey send messages for stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Here be the full code:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Build one MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Add one addition tool
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add one dynamic greeting resource
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Start to dey receive messages for stdin and send messages for stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Make one MCP server
mcp = FastMCP("Demo")


# Put one addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add one dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Main run block - dis one na wetin e need to run di server
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Create Program.cs file with this content:

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Your complete main app class suppose look like this:

```java
// McpServerApplication.java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

#### Rust

The final code for Rust server suppose look like dis:

```rust
use rmcp::{
    ServerHandler, ServiceExt,
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
};
use std::error::Error;

#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}

#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}

#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
    
    #[tool(description = "Adds a and b")]
    async fn add(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a + b).to_string()
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

### -7- Test the server

Start the server with dis command:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> To use MCP Inspector, use `mcp dev server.py` which go automatic launch the Inspector and give the required proxy session token. If you dey use `mcp run server.py`, you go need start the Inspector manually and configure the connection.

#### .NET

Make sure say you dey your project directory:

```sh
cd McpCalculatorServer
dotnet run
```

#### Java

```bash
./mvnw clean install -DskipTests
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### Rust

Run these commands to format and run the server:

```sh
cargo fmt
cargo run
```

### -8- Run using the inspector

The inspector na beta tool wey fit start your server and let you interact with am so you fit test say e dey work. Make we start am now:

> [!NOTE]
> e fit look different for the "command" field as e get the command wey e dey run server with your specific runtime/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

or add am to your *package.json* like this: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` then run `npm run inspector`

#### Python

Python wrap one Node.js tool wey dem call inspector. You fit run the tool like this:

```sh
mcp dev server.py
```

But e no get all the methods wey the tool get so e better make you run the Node.js tool directly like dis:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

If you dey use tool or IDE wey fit configure commands and arguments to run scripts,
make sure to set `python` for `Command` field and `server.py` as `Arguments`. Dis go make sure say di script dey run well.

#### .NET

Make sure say you dey inside your project directory:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Make sure say your calculator server dey run
Den run di inspector:

```cmd
npx @modelcontextprotocol/inspector
```

For di inspector web interface:

1. Select "SSE" as di transport type
2. Set di URL to: `http://localhost:8080/sse`
3. Click "Connect"

![Connect](../../../../translated_images/pcm/tool.163d33e3ee307e20.webp)

**You don connect to di server now**
**Di Java server testing section don complete now**

Di next section na about how to interact with di server.

You go see di user interface like dis:

![Connect](../../../../translated_images/pcm/connect.141db0b2bd05f096.webp)

1. Connect to di server by selecting di Connect button
  When you connect to di server, you go see dis:

  ![Connected](../../../../translated_images/pcm/connected.73d1e042c24075d3.webp)

1. Select "Tools" and "listTools", you go see "Add" show, select "Add" and fill di parameter values.

  You go see dis response, wey be say na result from "add" tool:

  ![Result of running add](../../../../translated_images/pcm/ran-tool.a5a6ee878c1369ec.webp)

Congrats, you don fit create and run your first server!

#### Rust

To run di Rust server with di MCP Inspector CLI, use dis command:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Official SDKs

MCP get official SDKs for many languages:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Maintained with collaboration with Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Maintained with collaboration with Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Di official TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Di official Python implementation
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Di official Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Maintained with collaboration with Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Di official Rust implementation

## Key Takeaways

- Setting up MCP development environment easy with language-specific SDKs
- Building MCP servers mean to create and register tools with clear schemas
- Testing and debugging important for reliable MCP implementations

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Assignment

Create simple MCP server with any tool you like:

1. Implement di tool for your preferred language (.NET, Java, Python, TypeScript, or Rust).
2. Define input parameters and return values.
3. Run di inspector tool to confirm say di server dey work as e suppose.
4. Test di implementation with different inputs.

## Solution

[Solution](./solution/README.md)

## Additional Resources

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## What's next

Next: [Getting Started with MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg know say automated translations fit get errors or inaccuracies. Di original document inside di original language na di correct source. For important matter, e better make professional human translation dey used. We no go responsible for any misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->