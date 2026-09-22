# Basic Calculator MCP Service

> [!NOTE]
> Dis example dey use di old HTTP+SSE transport and im dey target SDK wey dey compatible
> wit MCP `2025-11-25`. New remote servers suppose use `2026-07-28` Streamable
> HTTP support.

Dis service dey provide basic calculator operations through di Model Context Protocol (MCP) wey dey use Spring Boot wit WebFlux transport. E design as simple example for beginners wey dey learn about MCP implementations.

For more info, see di [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) reference documentation.

## Overview

Di service dey show:
- Support for SSE (Server-Sent Events)
- Automatic tool registration using Spring AI's `@Tool` annotation
- Basic calculator functions:
  - Addition, subtraction, multiplication, division
  - Power calculation and square root
  - Modulus (remainder) and absolute value
  - Help function for operation descriptions

## Features

Dis calculator service get di following capabilities:

1. **Basic Arithmetic Operations**:
   - Addition of two numbers
   - Subtraction of one number from another
   - Multiplication of two numbers
   - Division of one number by another (wit zero division check)

2. **Advanced Operations**:
   - Power calculation (raising a base to an exponent)
   - Square root calculation (wit negative number check)
   - Modulus (remainder) calculation
   - Absolute value calculation

3. **Help System**:
   - Built-in help function wey dey explain all available operations

## Using the Service

Di service dey expose di following API endpoints through di MCP protocol:

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract di second number from di first
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide di first number by di second (wit zero check)
- `power(base, exponent)`: Calculate di power of number
- `squareRoot(number)`: Calculate di square root (wit negative number check)
- `modulus(a, b)`: Calculate di remainder wen you divide
- `absolute(number)`: Calculate di absolute value
- `help()`: Get information about di available operations

## Test Client

Simple test client dey inside di `com.microsoft.mcp.sample.client` package. Di `SampleCalculatorClient` class dey show di available operations of di calculator service.

## Using the LangChain4j Client

Di project get LangChain4j example client for `com.microsoft.mcp.sample.client.LangChain4jClient` wey dey show how to integrate di calculator service wit LangChain4j and GitHub models:

### Prerequisites

1. **GitHub Token Setup**:
   
   To use GitHub AI models (like phi-4), you need GitHub personal access token:

   a. Go your GitHub account settings: https://github.com/settings/tokens
   
   b. Click "Generate new token" → "Generate new token (classic)"
   
   c. Give your token better name wey explain am well
   
   d. Select these scopes:
      - `repo` (Full control of private repositories)
      - `read:org` (Read org and team membership, read org projects)
      - `gist` (Create gists)
      - `user:email` (Access user email addresses (read-only))
   
   e. Click "Generate token" and copy your new token
   
   f. Set am as environment variable:
      
      For Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      For macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. For permanent setup, add am to your environment variables through system settings

2. Add LangChain4j GitHub dependency to your project (e don already dey inside pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Make sure sey di calculator server dey run for `localhost:8080`

### Running the LangChain4j Client

Dis example dey show:
- Connecting to di calculator MCP server using SSE transport
- Using LangChain4j to create chat bot wey dey use calculator operations
- Integrating wit GitHub AI models (now dey use phi-4 model)

Di client dey send these sample queries to show how e dey work:
1. Calculate sum of two numbers
2. Find square root of number
3. Get help information about available calculator operations

Run di example and check console output to see how AI model dey use calculator tools respond to queries.

### GitHub Model Configuration

LangChain4j client dey configured to use GitHub phi-4 model wit dis settings:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

To use different GitHub models, just change di `modelName` parameter to another model wey e support (e.g., "claude-3-haiku-20240307", "llama-3-70b-8192", etc.).

## Dependencies

Di project need these main dependencies:

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

Build di project using Maven:
```bash
./mvnw clean install -DskipTests
```

## Running the Server

### Using Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Using MCP Inspector

MCP Inspector na better tool for interacting wit MCP services. To use am wit dis calculator service:

1. **Install and run MCP Inspector** for new terminal window:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Access di web UI** by clicking di URL wey di app show (normally http://localhost:6274)

3. **Configure di connection**:
   - Set transport type to "SSE"
   - Set URL to your server SSE endpoint: `http://localhost:8080/sse`
   - Click "Connect"

4. **Use di tools**:
   - Click "List Tools" to see available calculator operations
   - Select tool and click "Run Tool" to perform operation

![MCP Inspector Screenshot](../../../../../../translated_images/pcm/tool.c75a0b2380efcf1a.webp)

### Using Docker

Di project get Dockerfile for containerized deployment:

1. **Build di Docker image**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Run di Docker container**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Dis one go:
- Build multi-stage Docker image wit Maven 3.9.9 and Eclipse Temurin 24 JDK
- Create optimized container image
- Expose service for port 8080
- Start MCP calculator service inside di container

You fit access di service at `http://localhost:8080` after di container start run.

## Troubleshooting

### Common Issues with GitHub Token

1. **Token Permission Issues**: If you see 403 Forbidden error, check say your token get correct permissions as we talk for prerequisites.

2. **Token Not Found**: If you see "No API key found" error, make sure GITHUB_TOKEN environment variable set well.

3. **Rate Limiting**: GitHub API get rate limits. If you get rate limit error (status code 429), wait small time before you try again.

4. **Token Expiration**: GitHub tokens fit expire. If you get authentication errors afta some time, generate new token and update your environment variable.

If you need more help, check [LangChain4j documentation](https://github.com/langchain4j/langchain4j) or [GitHub API documentation](https://docs.github.com/en/rest).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->