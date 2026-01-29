# MCP Java Client - Calculator Demo

Dis project dey show how pesin fit take create Java client wey go connect and work wit MCP (Model Context Protocol) server. For dis example, we go connect to di calculator server wey dey Chapter 01 and do different kind mathematical operations.

## Wetin You Need Before You Start

Before you go fit run dis client, you go need:

1. **Start di Calculator Server** wey dey Chapter 01:
   - Go di calculator server folder: `03-GettingStarted/01-first-server/solution/java/`
   - Build and run di calculator server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Di server suppose dey run for `http://localhost:8080`

2. **Java 21 or higher** wey don dey your system
3. **Maven** (wey dey inside Maven Wrapper)

## Wetin Be SDKClient?

Di `SDKClient` na Java application wey dey show how pesin fit:
- Connect to MCP server using Server-Sent Events (SSE) transport
- See di tools wey dey available for di server
- Call different calculator functions from far place
- Handle di response and show di result

## How E Dey Work

Di client dey use Spring AI MCP framework to:

1. **Make Connection**: E go create WebFlux SSE client transport wey go connect to di calculator server
2. **Set Up Client**: E go arrange di MCP client and make di connection
3. **Find Tools**: E go list all di calculator operations wey dey available
4. **Do Operations**: E go call different mathematical functions wit sample data
5. **Show Results**: E go display di result of each calculation

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

Dis project dey use di following key dependencies:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Dis dependency dey provide:
- `McpClient` - Di main client interface
- `WebFluxSseClientTransport` - SSE transport for web communication
- MCP protocol schemas and request/response types

## How to Build di Project

Use Maven wrapper to build di project:

```cmd
.\mvnw clean install
```

## How to Run di Client

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: Make sure say di calculator server dey run for `http://localhost:8080` before you run any of dis commands.

## Wetin di Client Dey Do

When you run di client, e go:

1. **Connect** to di calculator server for `http://localhost:8080`
2. **List Tools** - E go show all di calculator operations wey dey available
3. **Do Calculations**:
   - Addition: 5 + 3 = 8
   - Subtraction: 10 - 4 = 6
   - Multiplication: 6 × 7 = 42
   - Division: 20 ÷ 4 = 5
   - Power: 2^8 = 256
   - Square Root: √16 = 4
   - Absolute Value: |-5.5| = 5.5
   - Help: E go show di operations wey dey available

## Wetin You Go See As Output

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

**Note**: You fit see Maven warnings about threads wey still dey linger for di end - dis na normal for reactive applications and e no mean say error dey.

## Understand di Code

### 1. Transport Setup
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Dis one dey create SSE (Server-Sent Events) transport wey go connect to di calculator server.

### 2. Client Creation
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Dis one dey create synchronous MCP client and e go set up di connection.

### 3. Calling Tools
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Dis one dey call di "add" tool wit parameters a=5.0 and b=3.0.

## How to Solve Problems

### Server No Dey Run
If you see connection errors, make sure say di calculator server wey dey Chapter 01 dey run:
```
Error: Connection refused
```
**Solution**: Start di calculator server first.

### Port Don Full
If port 8080 dey busy:
```
Error: Address already in use
```
**Solution**: Stop di other applications wey dey use port 8080 or change di server to use another port.

### Build Errors
If you see build errors:
```cmd
.\mvnw clean install -DskipTests
```

## Learn More

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg make you sabi say automatic translation fit get mistake or no dey correct well. Di original dokyument for di language wey dem write am first na di main source wey you go trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->