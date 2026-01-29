# MCP Java Client - ਕੈਲਕੁਲੇਟਰ ਡੈਮੋ

ਇਹ ਪ੍ਰੋਜੈਕਟ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ ਇੱਕ ਜਾਵਾ ਕਲਾਇੰਟ ਬਣਾਇਆ ਜਾਵੇ ਜੋ MCP (ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ) ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਹੈ ਅਤੇ ਉਸ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਦਾ ਹੈ। ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਚੈਪਟਰ 01 ਦੇ ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਨਾਲ ਜੁੜ ਕੇ ਵੱਖ-ਵੱਖ ਗਣਿਤੀ ਕਾਰਵਾਈਆਂ ਕਰਾਂਗੇ।

## ਲੋੜੀਂਦੀਆਂ ਚੀਜ਼ਾਂ

ਇਸ ਕਲਾਇੰਟ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਤੁਹਾਨੂੰ ਇਹ ਕਰਨਾ ਹੋਵੇਗਾ:

1. **ਚੈਪਟਰ 01 ਤੋਂ ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ**:
   - ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ: `03-GettingStarted/01-first-server/solution/java/`
   - ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਬਣਾਓ ਅਤੇ ਚਲਾਓ:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - ਸਰਵਰ `http://localhost:8080` 'ਤੇ ਚੱਲ ਰਿਹਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ

2. ਤੁਹਾਡੇ ਸਿਸਟਮ 'ਤੇ **Java 21 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ** ਇੰਸਟਾਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ
3. **Maven** (Maven Wrapper ਰਾਹੀਂ ਸ਼ਾਮਲ)

## SDKClient ਕੀ ਹੈ?

`SDKClient` ਇੱਕ ਜਾਵਾ ਐਪਲੀਕੇਸ਼ਨ ਹੈ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ:
- MCP ਸਰਵਰ ਨਾਲ Server-Sent Events (SSE) ਟਰਾਂਸਪੋਰਟ ਰਾਹੀਂ ਜੁੜਿਆ ਜਾਵੇ
- ਸਰਵਰ ਤੋਂ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕੀਤੀ ਜਾਵੇ
- ਵੱਖ-ਵੱਖ ਕੈਲਕੁਲੇਟਰ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਰਿਮੋਟਲੀ ਕਾਲ ਕੀਤਾ ਜਾਵੇ
- ਜਵਾਬਾਂ ਨੂੰ ਸੰਭਾਲਿਆ ਜਾਵੇ ਅਤੇ ਨਤੀਜੇ ਦਿਖਾਏ ਜਾਣ

## ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

ਕਲਾਇੰਟ Spring AI MCP ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ:

1. **ਕਨੈਕਸ਼ਨ ਸਥਾਪਿਤ ਕਰਨਾ**: ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ WebFlux SSE ਕਲਾਇੰਟ ਟਰਾਂਸਪੋਰਟ ਬਣਾਉਂਦਾ ਹੈ
2. **ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕਰਨਾ**: MCP ਕਲਾਇੰਟ ਸੈੱਟਅੱਪ ਕਰਦਾ ਹੈ ਅਤੇ ਕਨੈਕਸ਼ਨ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ
3. **ਟੂਲਾਂ ਦੀ ਖੋਜ**: ਸਾਰੇ ਉਪਲਬਧ ਕੈਲਕੁਲੇਟਰ ਓਪਰੇਸ਼ਨਾਂ ਦੀ ਸੂਚੀ ਦਿਖਾਉਂਦਾ ਹੈ
4. **ਕਾਰਵਾਈਆਂ ਕਰਨਾ**: ਨਮੂਨਾ ਡੇਟਾ ਨਾਲ ਵੱਖ-ਵੱਖ ਗਣਿਤੀ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
5. **ਨਤੀਜੇ ਦਿਖਾਉਣਾ**: ਹਰ ਗਣਨਾ ਦੇ ਨਤੀਜੇ ਦਿਖਾਉਂਦਾ ਹੈ

## ਪ੍ਰੋਜੈਕਟ ਦੀ ਬਣਤਰ

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

## ਮੁੱਖ ਡਿਪੈਂਡੈਂਸੀਜ਼

ਪ੍ਰੋਜੈਕਟ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਮੁੱਖ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

ਇਹ ਡਿਪੈਂਡੈਂਸੀ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ:
- `McpClient` - ਮੁੱਖ ਕਲਾਇੰਟ ਇੰਟਰਫੇਸ
- `WebFluxSseClientTransport` - ਵੈੱਬ-ਆਧਾਰਿਤ ਸੰਚਾਰ ਲਈ SSE ਟਰਾਂਸਪੋਰਟ
- MCP ਪ੍ਰੋਟੋਕੋਲ ਸਕੀਮਾਂ ਅਤੇ ਰਿਕਵੇਸਟ/ਰਿਸਪਾਂਸ ਕਿਸਮਾਂ

## ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣਾ

Maven wrapper ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ:

```cmd
.\mvnw clean install
```

## ਕਲਾਇੰਟ ਚਲਾਉਣਾ

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**[!NOTE]**: ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ `http://localhost:8080` 'ਤੇ ਚੱਲ ਰਿਹਾ ਹੈ ਇਸ ਤੋਂ ਪਹਿਲਾਂ ਕਿ ਤੁਸੀਂ ਇਹ ਕਮਾਂਡਾਂ ਚਲਾਓ।

## ਕਲਾਇੰਟ ਕੀ ਕਰਦਾ ਹੈ

ਜਦੋਂ ਤੁਸੀਂ ਕਲਾਇੰਟ ਚਲਾਉਂਦੇ ਹੋ, ਇਹ:

1. ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਨਾਲ `http://localhost:8080` 'ਤੇ **ਜੁੜਦਾ ਹੈ**
2. **ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਦਿਖਾਉਂਦਾ ਹੈ** - ਸਾਰੇ ਉਪਲਬਧ ਕੈਲਕੁਲੇਟਰ ਓਪਰੇਸ਼ਨਾਂ ਨੂੰ ਵੇਖਾਉਂਦਾ ਹੈ
3. **ਗਣਨਾਵਾਂ ਕਰਦਾ ਹੈ**:
   - ਜੋੜ: 5 + 3 = 8
   - ਘਟਾਓ: 10 - 4 = 6
   - ਗੁਣਾ: 6 × 7 = 42
   - ਭਾਗ: 20 ÷ 4 = 5
   - ਘਾਤ: 2^8 = 256
   - ਵਰਗਮੂਲ: √16 = 4
   - ਪਰਮਾਣੂ ਮੁੱਲ: |-5.5| = 5.5
   - ਮਦਦ: ਉਪਲਬਧ ਓਪਰੇਸ਼ਨਾਂ ਨੂੰ ਦਿਖਾਉਂਦਾ ਹੈ

## ਉਮੀਦ ਕੀਤੀ ਨਤੀਜੇ

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

**[!NOTE]**: ਤੁਸੀਂ Maven ਵਾਰਨਿੰਗਜ਼ ਦੇਖ ਸਕਦੇ ਹੋ ਜੋ ਅੰਤ ਵਿੱਚ ਲੰਬੇ ਸਮੇਂ ਤੱਕ ਚੱਲ ਰਹੇ ਥ੍ਰੈਡਾਂ ਬਾਰੇ ਹੁੰਦੀਆਂ ਹਨ - ਇਹ ਰੀਐਕਟਿਵ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਸਧਾਰਣ ਗੱਲ ਹੈ ਅਤੇ ਇਹ ਕਿਸੇ ਗਲਤੀ ਦਾ ਸੰਕੇਤ ਨਹੀਂ ਹੈ।

## ਕੋਡ ਨੂੰ ਸਮਝਣਾ

### 1. ਟਰਾਂਸਪੋਰਟ ਸੈੱਟਅੱਪ
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
ਇਹ ਇੱਕ SSE (Server-Sent Events) ਟਰਾਂਸਪੋਰਟ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਹੈ।

### 2. ਕਲਾਇੰਟ ਬਣਾਉਣਾ
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
ਇੱਕ ਸਿੰਕ੍ਰੋਨਸ MCP ਕਲਾਇੰਟ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਕਨੈਕਸ਼ਨ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ।

### 3. ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨਾ
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
"add" ਟੂਲ ਨੂੰ ਪੈਰਾਮੀਟਰ a=5.0 ਅਤੇ b=3.0 ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ।

## ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ

### ਸਰਵਰ ਚੱਲ ਨਹੀਂ ਰਿਹਾ
ਜੇ ਤੁਹਾਨੂੰ ਕਨੈਕਸ਼ਨ ਦੀਆਂ ਗਲਤੀਆਂ ਮਿਲਦੀਆਂ ਹਨ, ਤਾਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਚੈਪਟਰ 01 ਤੋਂ ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ:
```
Error: Connection refused
```
**ਹੱਲ**: ਪਹਿਲਾਂ ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ।

### ਪੋਰਟ ਪਹਿਲਾਂ ਹੀ ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਹੈ
ਜੇ ਪੋਰਟ 8080 ਬਿਜੀ ਹੈ:
```
Error: Address already in use
```
**ਹੱਲ**: ਪੋਰਟ 8080 ਵਰਤ ਰਹੀਆਂ ਹੋਰ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬੰਦ ਕਰੋ ਜਾਂ ਸਰਵਰ ਨੂੰ ਵੱਖਰਾ ਪੋਰਟ ਵਰਤਣ ਲਈ ਬਦਲੋ।

### ਬਿਲਡ ਗਲਤੀਆਂ
ਜੇ ਤੁਹਾਨੂੰ ਬਿਲਡ ਗਲਤੀਆਂ ਆ ਰਹੀਆਂ ਹਨ:
```cmd
.\mvnw clean install -DskipTests
```

## ਹੋਰ ਸਿੱਖੋ

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।