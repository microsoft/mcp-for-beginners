# MCP Java Client - Calculator Demo

This project demonstrates how to create a Java client that connects to and interacts with an MCP (Model Context Protocol) server. In this example, we'll connect to the calculator server from Chapter 01 and perform various mathematical operations.

## Prerequisites

Before running this client, you need to:

1. **Start the Calculator Server** from Chapter 01:
   - Navigate to the calculator server directory: `03-GettingStarted/01-first-server/solution/java/`
   - Build and run the calculator server (from `03-GettingStarted/02-client/solution/java`), on Windows:
     ```cmd
     cd ..\..\..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
     On macOS/Linux:
     ```bash
     cd ../../../01-first-server/solution/java
     ./mvnw clean install -DskipTests
     java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - The server should be running on `http://localhost:8080`

2. **Java 21 or higher** installed on your system
3. **Maven** (included via Maven Wrapper)

## What is the SDKClient?

The `SDKClient` is a Java application that demonstrates how to:
- Connect to an MCP server using the Streamable HTTP transport
- List available tools from the server
- Call various calculator functions remotely
- Handle responses and display results

## How It Works

The client uses the Spring AI MCP framework to:

1. **Establish Connection**: Creates a WebFlux Streamable HTTP client transport to connect to the calculator server's `/mcp` endpoint
2. **Initialize Client**: Sets up the MCP client and establishes the connection
3. **Discover Tools**: Lists all available calculator operations
4. **Execute Operations**: Calls various mathematical functions with sample data
5. **Display Results**: Shows the results of each calculation

## Project Structure

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Key Dependencies

The project uses the following key dependencies:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-bom</artifactId>
            <version>2.0.2</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

This dependency (Spring AI 2.0.2 on Spring Boot 4.1.2, bringing in MCP Java SDK 2.1.0) provides:
- `McpClient` - The main client interface
- `WebClientStreamableHttpTransport` - Streamable HTTP transport for web-based communication (package `org.springframework.ai.mcp.client.webflux.transport`)
- MCP protocol schemas and request/response types

## Building the Project

Build the project using the Maven wrapper. On Windows:

```cmd
.\mvnw clean install
```

On macOS/Linux:

```bash
./mvnw clean install
```

## Running the Client

On Windows:

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

On macOS/Linux:

```bash
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: Make sure the calculator server is running on `http://localhost:8080` before executing any of these commands.

## What the Client Does

When you run the client, it will:

1. **Connect** to the calculator server at `http://localhost:8080`
2. **List Tools** - Shows all available calculator operations
3. **Perform Calculations**:
   - Addition: 5 + 3 = 8
   - Subtraction: 10 - 4 = 6
   - Multiplication: 6 × 7 = 42
   - Division: 20 ÷ 4 = 5
   - Power: 2^8 = 256
   - Square Root: √16 = 4
   - Absolute Value: |-5.5| = 5.5
   - Help: Shows available operations

## Expected Output

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Note**: The decimal separator depends on your locale (`8.00` or `8,00`). On macOS you may also see an `ERROR` log line saying that Netty cannot load `MacOSDnsServerAddressStreamProvider`; it falls back to the default DNS resolver and the client still works. You may see Maven warnings about lingering threads at the end - this is normal for reactive applications and doesn't indicate an error.

## Understanding the Code

### 1. Transport Setup
```java
var transport = WebClientStreamableHttpTransport.builder(WebClient.builder().baseUrl("http://localhost:8080")).build();
```
This creates a Streamable HTTP transport that connects to the calculator server's default MCP endpoint, `http://localhost:8080/mcp`.

### 2. Client Creation
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Creates a synchronous MCP client and initializes the connection.

### 3. Calling Tools
```java
CallToolResult resultAdd = client.callTool(CallToolRequest.builder("add").arguments(Map.of("a", 5.0, "b", 3.0)).build());
```
Calls the "add" tool with parameters a=5.0 and b=3.0.

## Troubleshooting

### Server Not Running
If you get connection errors, make sure the calculator server from Chapter 01 is running:
```
Error: Connection refused
```
**Solution**: Start the calculator server first.

### Port Already in Use
If port 8080 is busy:
```
Error: Address already in use
```
**Solution**: Stop other applications using port 8080 or modify the server to use a different port.

### Build Errors
If you encounter build errors:
```cmd
.\mvnw clean install -DskipTests
```

## Learn More

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)