# MCP Java Client - Calculator Demo

Ipinapakita ng proyektong ito kung paano gumawa ng Java client na kumokonekta at nakikipag-ugnayan sa isang MCP (Model Context Protocol) server. Sa halimbawang ito, kokonekta tayo sa calculator server mula sa Kabanata 01 at gagawa ng iba't ibang operasyong matematika.

## Mga Kinakailangan

Bago patakbuhin ang client na ito, kailangan mong:

1. **Simulan ang Calculator Server** mula sa Kabanata 01:
   - Pumunta sa direktoryo ng calculator server: `03-GettingStarted/01-first-server/solution/java/`
   - I-build at patakbuhin ang calculator server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Dapat tumatakbo ang server sa `http://localhost:8080`

2. **Java 21 o mas mataas** na naka-install sa iyong sistema
3. **Maven** (kasama sa pamamagitan ng Maven Wrapper)

## Ano ang SDKClient?

Ang `SDKClient` ay isang Java application na nagpapakita kung paano:
- Kumonekta sa isang MCP server gamit ang Server-Sent Events (SSE) transport
- Ilista ang mga available na tools mula sa server
- Tawagan ang iba't ibang calculator functions nang remote
- Pangasiwaan ang mga tugon at ipakita ang mga resulta

## Paano Ito Gumagana

Gumagamit ang client ng Spring AI MCP framework para:

1. **Mag-establish ng Koneksyon**: Gumagawa ng WebFlux SSE client transport para kumonekta sa calculator server
2. **I-initialize ang Client**: Inaayos ang MCP client at itinatag ang koneksyon
3. **I-discover ang Mga Tools**: Nililista ang lahat ng available na calculator operations
4. **Isagawa ang Mga Operasyon**: Tinatawagan ang iba't ibang mathematical functions gamit ang sample na data
5. **Ipakita ang Mga Resulta**: Ipinapakita ang mga resulta ng bawat kalkulasyon

## Istruktura ng Proyekto

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

## Pangunahing Mga Dependency

Ginagamit ng proyekto ang mga sumusunod na pangunahing dependency:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Ang dependency na ito ay nagbibigay ng:
- `McpClient` - Pangunahing client interface
- `WebFluxSseClientTransport` - SSE transport para sa web-based na komunikasyon
- MCP protocol schemas at mga uri ng request/response

## Pagbuo ng Proyekto

I-build ang proyekto gamit ang Maven wrapper:

```cmd
.\mvnw clean install
```

## Pagpapatakbo ng Client

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: Siguraduhing tumatakbo ang calculator server sa `http://localhost:8080` bago patakbuhin ang alinman sa mga utos na ito.

## Ano ang Ginagawa ng Client

Kapag pinatakbo mo ang client, ito ay:

1. **Kumokonekta** sa calculator server sa `http://localhost:8080`
2. **Naglilista ng Mga Tools** - Ipinapakita ang lahat ng available na calculator operations
3. **Gumagawa ng Mga Kalkulasyon**:
   - Addition: 5 + 3 = 8
   - Subtraction: 10 - 4 = 6
   - Multiplication: 6 × 7 = 42
   - Division: 20 ÷ 4 = 5
   - Power: 2^8 = 256
   - Square Root: √16 = 4
   - Absolute Value: |-5.5| = 5.5
   - Help: Ipinapakita ang mga available na operasyon

## Inaasahang Output

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

**Note**: Maaaring makakita ka ng mga babala mula sa Maven tungkol sa mga natitirang thread sa dulo - normal ito para sa mga reactive na aplikasyon at hindi nangangahulugang may error.

## Pag-unawa sa Code

### 1. Pagsasaayos ng Transport
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Gumagawa ito ng SSE (Server-Sent Events) transport na kumokonekta sa calculator server.

### 2. Paglikha ng Client
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Lumilikha ng synchronous MCP client at ini-initialize ang koneksyon.

### 3. Pagtawag sa Mga Tools
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Tinutawag ang "add" tool na may mga parameter na a=5.0 at b=3.0.

## Pag-troubleshoot

### Hindi Tumakbo ang Server
Kung nakakaranas ka ng mga error sa koneksyon, siguraduhing tumatakbo ang calculator server mula sa Kabanata 01:
```
Error: Connection refused
```
**Solusyon**: Simulan muna ang calculator server.

### Port Ay Ginagamit Na
Kung abala ang port 8080:
```
Error: Address already in use
```
**Solusyon**: Itigil ang ibang mga aplikasyon na gumagamit ng port 8080 o baguhin ang server upang gumamit ng ibang port.

### Mga Error sa Pagbuo
Kung nakakaranas ng mga error sa pagbuo:
```cmd
.\mvnw clean install -DskipTests
```

## Dagdag Pang Kaalaman

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.