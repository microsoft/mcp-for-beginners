# Basic Calculator MCP Service

> [!NOTE]
> This Java solution uses the legacy HTTP+SSE transport and targets an SDK
> compatible with MCP `2025-11-25`. It is retained for matching course code;
> new remote servers should use `2026-07-28` Streamable HTTP support.

This service provides basic calculator operations through the Model Context Protocol (MCP) using Spring Boot with WebFlux transport. It's designed as a simple example for beginners learning about MCP implementations.

For more information, see the [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) reference documentation.


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
- `help()`: List the available calculator operations

## Prerequisites

- Java 21 (JDK), for example [Eclipse Temurin](https://adoptium.net/) or `brew install openjdk@21` on macOS. Maven is not required, the included Maven wrapper (`mvnw`) downloads it.
- [Node.js](https://nodejs.org/) for `npx`, to test the server with the MCP Inspector.

## Dependencies

The project requires the following key dependencies:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Building the Project

Build the project using the Maven wrapper:

```bash
./mvnw clean install -DskipTests
```

On Windows use `mvnw.cmd clean install -DskipTests`.

## Running the Server

### Using Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

The server listens on port 8080. Keep it running while you test it, because the inspector connects to it over HTTP. You can check that it is up with `curl http://localhost:8080/health`.

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

### Using MCP Inspector in CLI mode

With the server running, you can also test it from the command line:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:8080/sse --transport sse --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

You should see the following output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "\"1.00 + 2.00 = 3.00\""
    }
  ],
  "isError": false
}
```
