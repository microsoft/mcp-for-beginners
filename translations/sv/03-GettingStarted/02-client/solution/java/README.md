# MCP Java Client - Calculator Demo

Det här projektet visar hur man skapar en Java-klient som ansluter till och interagerar med en MCP (Model Context Protocol) server. I det här exemplet ansluter vi till kalkylatorsservern från Kapitel 01 och utför olika matematiska operationer.

## Förutsättningar

Innan du kör den här klienten behöver du:

1. **Starta Calculator Server** från Kapitel 01:
   - Navigera till katalogen för kalkylatorsservern: `03-GettingStarted/01-first-server/solution/java/`
   - Bygg och kör kalkylatorsservern:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Servern ska vara igång på `http://localhost:8080`

2. **Java 21 eller högre** installerat på din dator
3. **Maven** (ingår via Maven Wrapper)

## Vad är SDKClient?

`SDKClient` är en Java-applikation som visar hur man:
- Ansluter till en MCP-server med Server-Sent Events (SSE) transport
- Listar tillgängliga verktyg från servern
- Anropar olika kalkylatorfunktioner på distans
- Hanterar svar och visar resultat

## Hur det fungerar

Klienten använder Spring AI MCP-ramverket för att:

1. **Etablera anslutning**: Skapar en WebFlux SSE-klienttransport för att ansluta till kalkylatorsservern
2. **Initiera klient**: Sätter upp MCP-klienten och etablerar anslutningen
3. **Upptäcka verktyg**: Listar alla tillgängliga kalkylatoroperationer
4. **Utföra operationer**: Anropar olika matematiska funktioner med exempeldata
5. **Visa resultat**: Visar resultaten av varje beräkning

## Projektstruktur

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

## Viktiga beroenden

Projektet använder följande viktiga beroenden:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Det här beroendet tillhandahåller:
- `McpClient` - Huvudgränssnittet för klienten
- `WebFluxSseClientTransport` - SSE-transport för webbaserad kommunikation
- MCP-protokollens scheman samt förfrågnings- och svarstyper

## Bygga projektet

Bygg projektet med Maven-wrappern:

```cmd
.\mvnw clean install
```

## Köra klienten

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: Se till att kalkylatorsservern körs på `http://localhost:8080` innan du kör något av dessa kommandon.

## Vad klienten gör

När du kör klienten kommer den att:

1. **Ansluta** till kalkylatorsservern på `http://localhost:8080`
2. **Lista verktyg** - Visar alla tillgängliga kalkylatoroperationer
3. **Utföra beräkningar**:
   - Addition: 5 + 3 = 8
   - Subtraktion: 10 - 4 = 6
   - Multiplikation: 6 × 7 = 42
   - Division: 20 ÷ 4 = 5
   - Potens: 2^8 = 256
   - Kvadratrot: √16 = 4
   - Absolutvärde: |-5.5| = 5.5
   - Hjälp: Visar tillgängliga operationer

## Förväntad utdata

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

**Note**: Du kan se Maven-varningar om kvarvarande trådar i slutet – detta är normalt för reaktiva applikationer och indikerar inte något fel.

## Förstå koden

### 1. Transportinställning
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Detta skapar en SSE (Server-Sent Events) transport som ansluter till kalkylatorsservern.

### 2. Skapa klient
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Skapar en synkron MCP-klient och initierar anslutningen.

### 3. Anropa verktyg
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Anropar verktyget "add" med parametrarna a=5.0 och b=3.0.

## Felsökning

### Servern körs inte
Om du får anslutningsfel, kontrollera att kalkylatorsservern från Kapitel 01 är igång:
```
Error: Connection refused
```
**Lösning**: Starta kalkylatorsservern först.

### Porten är redan upptagen
Om port 8080 är upptagen:
```
Error: Address already in use
```
**Lösning**: Stoppa andra program som använder port 8080 eller ändra servern till att använda en annan port.

### Byggfel
Om du stöter på byggfel:
```cmd
.\mvnw clean install -DskipTests
```

## Läs mer

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.