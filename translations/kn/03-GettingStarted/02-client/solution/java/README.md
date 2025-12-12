<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7074b9f4c8cd147c1c10f569d8508c82",
  "translation_date": "2025-12-11T13:37:16+00:00",
  "source_file": "03-GettingStarted/02-client/solution/java/README.md",
  "language_code": "kn"
}
-->
# MCP ಜಾವಾ ಕ್ಲೈಂಟ್ - ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಡೆಮೊ

ಈ ಪ್ರಾಜೆಕ್ಟ್ ಒಂದು MCP (ಮಾದರಿ ಸಾಂದರ್ಭಿಕ ಪ್ರೋಟೋಕಾಲ್) ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದಿ, ಅದರೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುವ ಜಾವಾ ಕ್ಲೈಂಟ್ ಅನ್ನು ಹೇಗೆ ರಚಿಸುವುದನ್ನು ತೋರಿಸುತ್ತದೆ. ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಅಧ್ಯಾಯ 01 ರ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದಿ ವಿವಿಧ ಗಣಿತೀಯ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವೆವು.

## ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

ಈ ಕ್ಲೈಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡುವ ಮೊದಲು, ನೀವು:

1. **ಅಧ್ಯಾಯ 01 ರಿಂದ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ**:
   - ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಡೈರೆಕ್ಟರಿಯ ಕಡೆಗೆ ನವಿಗೇಟ್ ಮಾಡಿ: `03-GettingStarted/01-first-server/solution/java/`
   - ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಅನ್ನು ನಿರ್ಮಿಸಿ ಮತ್ತು ಚಾಲನೆ ಮಾಡಿ:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - ಸರ್ವರ್ `http://localhost:8080` ನಲ್ಲಿ ಚಾಲನೆಯಲ್ಲಿರಬೇಕು

2. ನಿಮ್ಮ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ **ಜಾವಾ 21 ಅಥವಾ ಅದಕ್ಕಿಂತ ಮೇಲಿನ ಆವೃತ್ತಿ** ಇನ್‌ಸ್ಟಾಲ್ ಆಗಿರಬೇಕು
3. **ಮೇವನ್** (ಮೇವನ್ ರ್ಯಾಪರ್ ಮೂಲಕ ಸೇರಿಸಲಾಗಿದೆ)

## SDKClient ಎಂದರೆ ಏನು?

`SDKClient` ಒಂದು ಜಾವಾ ಅಪ್ಲಿಕೇಶನ್ ಆಗಿದ್ದು, ಇದು ಹೇಗೆ:
- MCP ಸರ್ವರ್‌ಗೆ Server-Sent Events (SSE) ಸಾರಿಗೆ ಬಳಸಿ ಸಂಪರ್ಕ ಹೊಂದುವುದು
- ಸರ್ವರ್‌ನಿಂದ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು
- ವಿವಿಧ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಕಾರ್ಯಗಳನ್ನು ದೂರದಿಂದ ಕರೆ ಮಾಡುವುದು
- ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ ಫಲಿತಾಂಶಗಳನ್ನು ಪ್ರದರ್ಶಿಸುವುದು

## ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ

ಕ್ಲೈಂಟ್ ಸ್ಪ್ರಿಂಗ್ AI MCP ಫ್ರೇಮ್ವರ್ಕ್ ಅನ್ನು ಬಳಸುತ್ತದೆ:

1. **ಸಂಪರ್ಕ ಸ್ಥಾಪನೆ**: ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದಲು WebFlux SSE ಕ್ಲೈಂಟ್ ಸಾರಿಗೆ ರಚಿಸುತ್ತದೆ
2. **ಕ್ಲೈಂಟ್ ಪ್ರಾರಂಭ**: MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ ಸಂಪರ್ಕವನ್ನು ಸ್ಥಾಪಿಸುತ್ತದೆ
3. **ಉಪಕರಣಗಳನ್ನು ಕಂಡುಹಿಡಿಯುವುದು**: ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಕಾರ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ
4. **ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು**: ಮಾದರಿ ಡೇಟಾ ಬಳಸಿ ವಿವಿಧ ಗಣಿತೀಯ ಕಾರ್ಯಗಳನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ
5. **ಫಲಿತಾಂಶಗಳನ್ನು ಪ್ರದರ್ಶಿಸುವುದು**: ಪ್ರತಿ ಲೆಕ್ಕಾಚಾರದ ಫಲಿತಾಂಶಗಳನ್ನು ತೋರಿಸುತ್ತದೆ

## ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ

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

## ಪ್ರಮುಖ ಅವಲಂಬನೆಗಳು

ಪ್ರಾಜೆಕ್ಟ್ ಕೆಳಗಿನ ಪ್ರಮುಖ ಅವಲಂಬನೆಗಳನ್ನು ಬಳಸುತ್ತದೆ:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

ಈ ಅವಲಂಬನೆ ನೀಡುತ್ತದೆ:
- `McpClient` - ಮುಖ್ಯ ಕ್ಲೈಂಟ್ ಇಂಟರ್ಫೇಸ್
- `WebFluxSseClientTransport` - ವೆಬ್ ಆಧಾರಿತ ಸಂವಹನಕ್ಕಾಗಿ SSE ಸಾರಿಗೆ
- MCP ಪ್ರೋಟೋಕಾಲ್ ಸ್ಕೀಮಾಗಳು ಮತ್ತು ವಿನಂತಿ/ಪ್ರತಿಕ್ರಿಯೆ ಪ್ರಕಾರಗಳು

## ಪ್ರಾಜೆಕ್ಟ್ ನಿರ್ಮಾಣ

ಮೇವನ್ ರ್ಯಾಪರ್ ಬಳಸಿ ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು ನಿರ್ಮಿಸಿ:

```cmd
.\mvnw clean install
```

## ಕ್ಲೈಂಟ್ ಚಾಲನೆ

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**ಗಮನಿಸಿ**: ಈ ಆಜ್ಞೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಮೊದಲು ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ `http://localhost:8080` ನಲ್ಲಿ ಚಾಲನೆಯಲ್ಲಿರಬೇಕು.

## ಕ್ಲೈಂಟ್ ಏನು ಮಾಡುತ್ತದೆ

ನೀವು ಕ್ಲೈಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿದಾಗ, ಅದು:

1. `http://localhost:8080` ನಲ್ಲಿ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್‌ಗೆ **ಸಂಪರ್ಕ** ಹೊಂದುತ್ತದೆ
2. **ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ** - ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಕಾರ್ಯಗಳನ್ನು ತೋರಿಸುತ್ತದೆ
3. **ಲೆಕ್ಕಾಚಾರಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ**:
   - ಸೇರ್ಪಡೆ: 5 + 3 = 8
   - ವ್ಯತ್ಯಾಸ: 10 - 4 = 6
   - ಗುಣಾಕಾರ: 6 × 7 = 42
   - ಭಾಗಾಕಾರ: 20 ÷ 4 = 5
   - ಶಕ್ತಿ: 2^8 = 256
   - ವರ್ಗಮೂಲ: √16 = 4
   - ಪರಮಾಣು ಮೌಲ್ಯ: |-5.5| = 5.5
   - ಸಹಾಯ: ಲಭ್ಯವಿರುವ ಕಾರ್ಯಗಳನ್ನು ತೋರಿಸುತ್ತದೆ

## ನಿರೀಕ್ಷಿತ ಔಟ್‌ಪುಟ್

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

**ಗಮನಿಸಿ**: ಕೊನೆಯಲ್ಲಿ ಮೇವನ್ ಲಿಂಗರಿಂಗ್ ಥ್ರೆಡ್ಗಳ ಬಗ್ಗೆ ಎಚ್ಚರಿಕೆಗಳು ಕಾಣಬಹುದು - ಇದು ಪ್ರತಿಕ್ರಿಯಾತ್ಮಕ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಸಾಮಾನ್ಯ ಮತ್ತು ದೋಷವಲ್ಲ.

## ಕೋಡ್ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು

### 1. ಸಾರಿಗೆ ಸೆಟ್ ಅಪ್
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
ಇದು ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದುವ SSE (ಸರ್ವರ್-ಸೆಂಟ್ ಇವೆಂಟ್ಸ್) ಸಾರಿಗೆ ರಚಿಸುತ್ತದೆ.

### 2. ಕ್ಲೈಂಟ್ ರಚನೆ
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
ಸಿಂಕ್ರೋನಸ್ MCP ಕ್ಲೈಂಟ್ ರಚಿಸಿ ಸಂಪರ್ಕವನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ.

### 3. ಉಪಕರಣಗಳನ್ನು ಕರೆ ಮಾಡುವುದು
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು a=5.0 ಮತ್ತು b=3.0 ಇರುವ "add" ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ.

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### ಸರ್ವರ್ ಚಾಲನೆಯಲ್ಲಿಲ್ಲ
ಸಂಪರ್ಕ ದೋಷಗಳು ಬಂದರೆ, ಅಧ್ಯಾಯ 01 ರ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಚಾಲನೆಯಲ್ಲಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:
```
Error: Connection refused
```
**ಪರಿಹಾರ**: ಮೊದಲು ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ.

### ಪೋರ್ಟ್ ಈಗಾಗಲೇ ಬಳಕೆಯಲ್ಲಿದೆ
ಪೋರ್ಟ್ 8080 ಬ್ಯುಸಿ ಇದ್ದರೆ:
```
Error: Address already in use
```
**ಪರಿಹಾರ**: ಪೋರ್ಟ್ 8080 ಬಳಸುತ್ತಿರುವ ಇತರ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿಲ್ಲಿಸಿ ಅಥವಾ ಸರ್ವರ್ ಅನ್ನು ಬೇರೆ ಪೋರ್ಟ್ ಬಳಸುವಂತೆ ಬದಲಾಯಿಸಿ.

### ನಿರ್ಮಾಣ ದೋಷಗಳು
ನಿರ್ಮಾಣ ದೋಷಗಳು ಎದುರಾದರೆ:
```cmd
.\mvnw clean install -DskipTests
```

## ಇನ್ನಷ್ಟು ತಿಳಿದುಕೊಳ್ಳಿ

- [Spring AI MCP ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [ಮಾದರಿ ಸಾಂದರ್ಭಿಕ ಪ್ರೋಟೋಕಾಲ್ ಸ್ಪೆಸಿಫಿಕೇಶನ್](https://modelcontextprotocol.io/)
- [Spring WebFlux ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->