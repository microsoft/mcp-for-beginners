# Basic Calculator MCP Service

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

The project includes a LangChain4j example client in `com.microsoft.mcp.sample.client.LangChain4jClient` that demonstrates how to integrate the calculator service with LangChain4j and GitHub models:

### Prerequisites

1. **GitHub Token Setup**:
   
   To use GitHub's AI models (like phi-4), you need a GitHub personal access token:

   a. Go to your GitHub account settings: https://github.com/settings/tokens
   
   b. Click "Generate new token" → "Generate new token (classic)"
   
   c. Give your token a descriptive name
   
   d. Select the following scopes:
      - `repo` (Full control of private repositories)
      - `read:org` (Read org and team membership, read org projects)
      - `gist` (Create gists)
      - `user:email` (Access user email addresses (read-only))
   
   e. Click "Generate token" and copy your new token
   
   f. Set it as an environment variable:
      
      On Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      On macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. For persistent setup, add it to your environment variables through system settings

2. Add the LangChain4j GitHub dependency to your project (already included in pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Ensure the calculator server is running on `localhost:8080`

### Running the LangChain4j Client

This example demonstrates:
- Connecting to the calculator MCP server via SSE transport
- Using LangChain4j to create a chat bot that leverages calculator operations
- Integrating with GitHub AI models (now using phi-4 model)

The client sends the following sample queries to demonstrate functionality:
1. Calculating the sum of two numbers
2. Finding the square root of a number
3. Getting help information about available calculator operations

Run the example and check the console output to see how the AI model uses the calculator tools to respond to queries.

### GitHub Model Configuration

The LangChain4j client is configured to use GitHub's phi-4 model with the following settings:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

To use different GitHub models, simply change the `modelName` parameter to another supported model (e.g., "claude-3-haiku-20240307", "llama-3-70b-8192", etc.).

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

<!-- For GitHub models support -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-github</artifactId>
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

![MCP Inspector Screenshot](../../../../../../translated_images/en/tool.c75a0b2380efcf1a.webp)

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

### Common Issues with GitHub Token

1. **Token Permission Issues**: If you get a 403 Forbidden error, check that your token has the correct permissions as outlined in the prerequisites.

2. **Token Not Found**: If you get a "No API key found" error, ensure the GITHUB_TOKEN environment variable is properly set.

3. **Rate Limiting**: GitHub API has rate limits. If you encounter a rate limit error (status code 429), wait a few minutes before trying again.

4. **Token Expiration**: GitHub tokens can expire. If you receive authentication errors after some time, generate a new token and update your environment variable.

If you need further assistance, check the [LangChain4j documentation](https://github.com/langchain4j/langchain4j) or [GitHub API documentation](https://docs.github.com/en/rest).

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.