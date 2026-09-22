# Basic Calculator MCP Service

> [!NOTE]
> This sample uses the legacy HTTP+SSE transport and targets an SDK compatible
> with MCP `2025-11-25`. New remote servers should use `2026-07-28` Streamable
> HTTP support.

This service provides basic calculator operations through the Model Context Protocol (MCP) using Spring Boot with WebFlux transport. It's designed as a simple example for beginners learning about MCP implementations.

For more information, see the [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) reference documentation.

## Overview

The service showcases:
- Support for SSE (Server-Sent Events)
- Automatic tool registration using Spring AI's `@Tool` annotation
- Basic calculator functions:
  - Addition, subtraction, multiplication, division
  - Power calculation and square root
  - Modulus (remainder) and absolute value
  - Help function for operation descriptions

## Features

This calculator service offers the following capabilities:

1. **Basic Arithmetic Operations**:
   - Addition of two numbers
   - Subtraction of one number from another
   - Multiplication of two numbers
   - Division of one number by another (with zero division check)

2. **Advanced Operations**:
   - Power calculation (raising a base to an exponent)
   - Square root calculation (with negative number check)
   - Modulus (remainder) calculation
   - Absolute value calculation

3. **Help System**:
   - Built-in help function explaining all available operations

## Using the Service

The service exposes the following API endpoints through the MCP protocol:

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract the second number from the first
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide the first number by the second (with zero check)
- `power(base, exponent)`: Calculate the power of a number
- `squareRoot(number)`: Calculate the square root (with negative number check)
- `modulus(a, b)`: Calculate the remainder when dividing
- `absolute(number)`: Calculate the absolute value
- `help()`: Get information about available operations

## Test Client

A simple test client is included in the `com.microsoft.mcp.sample.client` package. The `SampleCalculatorClient` class demonstrates the available operations of the calculator service.

## Using the LangChain4j Client

The project includes a LangChain4j example client in
`com.microsoft.mcp.sample.client.LangChain4jClient` that demonstrates how to
integrate the calculator service with a Microsoft Foundry model.

### Prerequisites

1. Create a Microsoft Foundry resource and deploy an active model such as
   `gpt-5.1`.
2. Set the model endpoint, API key, and deployment name:

   ```bash
   export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
   export AZURE_OPENAI_API_KEY="<api-key>"
   export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
   ```

3. Check the
   [Microsoft Foundry model retirement schedule](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
   before selecting a deployment.
4. Ensure the calculator server is running on `localhost:8080`.

### Running the LangChain4j Client

This example demonstrates:
- Connecting to the calculator MCP server via SSE transport
- Using LangChain4j to create a chat bot that leverages calculator operations
- Integrating with a deployed Microsoft Foundry model

The client sends the following sample queries to demonstrate functionality:
1. Calculating the sum of two numbers
2. Finding the square root of a number
3. Getting help information about available calculator operations

Run the example and check the console output to see how the AI model uses the calculator tools to respond to queries.

### Microsoft Foundry Model Configuration

The LangChain4j client uses the Azure OpenAI v1-compatible endpoint exposed by
Microsoft Foundry:

```java
String endpoint = System.getenv("AZURE_OPENAI_ENDPOINT");
ChatLanguageModel model = OpenAiOfficialChatModel.builder()
   .baseUrl(endpoint.replaceAll("/+$", "") + "/openai/v1/")
   .apiKey(System.getenv("AZURE_OPENAI_API_KEY"))
   .isAzure(true)
   .modelName(System.getenv().getOrDefault("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"))
    .timeout(Duration.ofSeconds(60))
    .build();
```

`AZURE_OPENAI_DEPLOYMENT` must match the name assigned when the model was
deployed, which may differ from the underlying model name.

## Dependencies

The project requires the following key dependencies:

```xml
<!-- For MCP Server -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- For LangChain4j integration -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>${langchain4j.version}</version>
</dependency>

<!-- For Microsoft Foundry's OpenAI-compatible endpoint -->
<dependency>
    <groupId>dev.langchain4j</groupId>
   <artifactId>langchain4j-open-ai-official</artifactId>
    <version>${langchain4j.version}</version>
</dependency>
```

## Building the Project

Build the project using Maven:
```bash
./mvnw clean install -DskipTests
```

## Running the Server

### Using Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Using MCP Inspector

The MCP Inspector is a helpful tool for interacting with MCP services. To use it with this calculator service:

1. **Install and run MCP Inspector** in a new terminal window:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Access the web UI** by clicking the URL displayed by the app (typically http://localhost:6274)

3. **Configure the connection**:
   - Set the transport type to "SSE"
   - Set the URL to your running server's SSE endpoint: `http://localhost:8080/sse`
   - Click "Connect"

4. **Use the tools**:
   - Click "List Tools" to see available calculator operations
   - Select a tool and click "Run Tool" to execute an operation

![MCP Inspector Screenshot](images/tool.png)

### Using Docker

The project includes a Dockerfile for containerized deployment:

1. **Build the Docker image**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

This will:
- Build a multi-stage Docker image with Maven 3.9.9 and Eclipse Temurin 24 JDK
- Create an optimized container image
- Expose the service on port 8080
- Start the MCP calculator service inside the container

You can access the service at `http://localhost:8080` once the container is running.

## Troubleshooting

### Common Model Connection Issues

1. **Authentication errors**: Confirm `AZURE_OPENAI_API_KEY` belongs to the
   resource identified by `AZURE_OPENAI_ENDPOINT`.
2. **Deployment not found**: Confirm `AZURE_OPENAI_DEPLOYMENT` exactly matches
   the deployment name in Microsoft Foundry.
3. **Rate limiting**: Review the deployment quota and retry after the interval
   returned by the service.

For more help, see the
[LangChain4j documentation](https://github.com/langchain4j/langchain4j) and
[Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/).
