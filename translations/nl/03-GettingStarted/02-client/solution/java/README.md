# MCP Java Client - Calculator Demo

Dit project laat zien hoe je een Java-client maakt die verbinding maakt met en communiceert met een MCP (Model Context Protocol) server. In dit voorbeeld verbinden we met de rekenmachine-server uit Hoofdstuk 01 en voeren we verschillende wiskundige bewerkingen uit.

## Vereisten

Voordat je deze client start, moet je:

1. **Start de Calculator Server** uit Hoofdstuk 01:
   - Navigeer naar de map van de calculator server: `03-GettingStarted/01-first-server/solution/java/`
   - Bouw en start de calculator server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - De server zou moeten draaien op `http://localhost:8080`

2. **Java 21 of hoger** geïnstalleerd op je systeem
3. **Maven** (meegeleverd via Maven Wrapper)

## Wat is de SDKClient?

De `SDKClient` is een Java-applicatie die laat zien hoe je:
- Verbindt met een MCP-server via Server-Sent Events (SSE) transport
- Beschikbare tools van de server opvraagt
- Verschillende calculatorfuncties op afstand aanroept
- Antwoorden verwerkt en resultaten toont

## Hoe werkt het

De client gebruikt het Spring AI MCP-framework om:

1. **Verbinding te maken**: Maakt een WebFlux SSE client transport aan om verbinding te maken met de calculator server
2. **Client te initialiseren**: Zet de MCP client op en maakt de verbinding
3. **Tools te ontdekken**: Toont alle beschikbare calculatorbewerkingen
4. **Bewerkingen uit te voeren**: Roept verschillende wiskundige functies aan met voorbeeldgegevens
5. **Resultaten te tonen**: Laat de uitkomsten van elke berekening zien

## Projectstructuur

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

## Belangrijke afhankelijkheden

Het project gebruikt de volgende belangrijke afhankelijkheden:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Deze afhankelijkheid biedt:
- `McpClient` - De hoofdclient interface
- `WebFluxSseClientTransport` - SSE transport voor webgebaseerde communicatie
- MCP protocol schema’s en request/response types

## Het project bouwen

Bouw het project met de Maven wrapper:

```cmd
.\mvnw clean install
```

## De client uitvoeren

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Opmerking**: Zorg dat de calculator server draait op `http://localhost:8080` voordat je een van deze commando’s uitvoert.

## Wat de client doet

Wanneer je de client start, zal deze:

1. **Verbinden** met de calculator server op `http://localhost:8080`
2. **Tools tonen** - Laat alle beschikbare calculatorbewerkingen zien
3. **Berekeningen uitvoeren**:
   - Optellen: 5 + 3 = 8
   - Aftrekken: 10 - 4 = 6
   - Vermenigvuldigen: 6 × 7 = 42
   - Delen: 20 ÷ 4 = 5
   - Machtsverheffen: 2^8 = 256
   - Worteltrekken: √16 = 4
   - Absolute waarde: |-5.5| = 5.5
   - Help: Toont beschikbare bewerkingen

## Verwachte output

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

**Opmerking**: Mogelijk zie je aan het einde Maven-waarschuwingen over achtergebleven threads - dit is normaal bij reactieve applicaties en betekent geen fout.

## De code begrijpen

### 1. Transport instellen
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Dit maakt een SSE (Server-Sent Events) transport aan dat verbinding maakt met de calculator server.

### 2. Client aanmaken
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Maakt een synchrone MCP client aan en initialiseert de verbinding.

### 3. Tools aanroepen
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Roep de "add" tool aan met parameters a=5.0 en b=3.0.

## Problemen oplossen

### Server draait niet
Als je verbindingsfouten krijgt, controleer dan of de calculator server uit Hoofdstuk 01 draait:
```
Error: Connection refused
```
**Oplossing**: Start eerst de calculator server.

### Poort al in gebruik
Als poort 8080 bezet is:
```
Error: Address already in use
```
**Oplossing**: Stop andere applicaties die poort 8080 gebruiken of wijzig de server om een andere poort te gebruiken.

### Build fouten
Als je buildfouten tegenkomt:
```cmd
.\mvnw clean install -DskipTests
```

## Meer informatie

- [Spring AI MCP Documentatie](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specificatie](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentatie](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.