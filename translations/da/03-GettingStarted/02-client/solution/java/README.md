# MCP Java Client - Calculator Demo

Dette projekt viser, hvordan man opretter en Java-klient, der forbinder til og interagerer med en MCP (Model Context Protocol) server. I dette eksempel forbinder vi til calculator-serveren fra Kapitel 01 og udfører forskellige matematiske operationer.

## Forudsætninger

Før du kører denne klient, skal du:

1. **Starte Calculator Serveren** fra Kapitel 01:
   - Gå til calculator-serverens mappe: `03-GettingStarted/01-first-server/solution/java/`
   - Byg og kør calculator-serveren:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Serveren skal køre på `http://localhost:8080`

2. **Java 21 eller nyere** installeret på dit system
3. **Maven** (inkluderet via Maven Wrapper)

## Hvad er SDKClient?

`SDKClient` er en Java-applikation, der demonstrerer, hvordan man:
- Forbinder til en MCP-server ved hjælp af Server-Sent Events (SSE) transport
- Lister tilgængelige værktøjer fra serveren
- Kalder forskellige calculator-funktioner eksternt
- Håndterer svar og viser resultater

## Sådan fungerer det

Klienten bruger Spring AI MCP framework til at:

1. **Etablere forbindelse**: Opretter en WebFlux SSE klienttransport til at forbinde til calculator-serveren
2. **Initialisere klient**: Sætter MCP-klienten op og etablerer forbindelsen
3. **Find værktøjer**: Lister alle tilgængelige calculator-operationer
4. **Udfør operationer**: Kalder forskellige matematiske funktioner med eksempeldata
5. **Vis resultater**: Viser resultaterne af hver beregning

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

## Vigtige afhængigheder

Projektet bruger følgende nøgleafhængigheder:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Denne afhængighed indeholder:
- `McpClient` - Hovedklientens interface
- `WebFluxSseClientTransport` - SSE transport til webbaseret kommunikation
- MCP protokol skemaer og request/response typer

## Byg projektet

Byg projektet med Maven wrapperen:

```cmd
.\mvnw clean install
```

## Kør klienten

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: Sørg for, at calculator-serveren kører på `http://localhost:8080` før du kører nogen af disse kommandoer.

## Hvad klienten gør

Når du kører klienten, vil den:

1. **Forbinde** til calculator-serveren på `http://localhost:8080`
2. **Liste værktøjer** - Viser alle tilgængelige calculator-operationer
3. **Udføre beregninger**:
   - Addition: 5 + 3 = 8
   - Subtraktion: 10 - 4 = 6
   - Multiplikation: 6 × 7 = 42
   - Division: 20 ÷ 4 = 5
   - Potens: 2^8 = 256
   - Kvadratrod: √16 = 4
   - Absolut værdi: |-5.5| = 5.5
   - Hjælp: Viser tilgængelige operationer

## Forventet output

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

**Note**: Du kan se Maven advarsler om tilbageværende tråde til sidst - det er normalt for reaktive applikationer og indikerer ikke en fejl.

## Forstå koden

### 1. Transportopsætning
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Dette opretter en SSE (Server-Sent Events) transport, der forbinder til calculator-serveren.

### 2. Oprettelse af klient
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Opretter en synkron MCP-klient og initialiserer forbindelsen.

### 3. Kald af værktøjer
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Kalder "add" værktøjet med parametrene a=5.0 og b=3.0.

## Fejlfinding

### Serveren kører ikke
Hvis du får forbindelsesfejl, så sørg for, at calculator-serveren fra Kapitel 01 kører:
```
Error: Connection refused
```
**Løsning**: Start calculator-serveren først.

### Porten er allerede i brug
Hvis port 8080 er optaget:
```
Error: Address already in use
```
**Løsning**: Stop andre programmer, der bruger port 8080, eller ændr serveren til at bruge en anden port.

### Byggefejl
Hvis du støder på byggefejl:
```cmd
.\mvnw clean install -DskipTests
```

## Lær mere

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.