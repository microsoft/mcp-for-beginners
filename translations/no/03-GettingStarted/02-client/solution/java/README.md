# MCP Java Client - Kalkulatordemo

Dette prosjektet viser hvordan du lager en Java-klient som kobler til og samhandler med en MCP (Model Context Protocol) server. I dette eksempelet kobler vi til kalkulatorserveren fra Kapittel 01 og utfører ulike matematiske operasjoner.

## Forutsetninger

Før du kjører denne klienten, må du:

1. **Starte Kalkulatorserveren** fra Kapittel 01:
   - Gå til kalkulatorserver-mappen: `03-GettingStarted/01-first-server/solution/java/`
   - Bygg og kjør kalkulatorserveren:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Serveren skal kjøre på `http://localhost:8080`

2. **Java 21 eller nyere** installert på systemet ditt
3. **Maven** (inkludert via Maven Wrapper)

## Hva er SDKClient?

`SDKClient` er en Java-applikasjon som viser hvordan man kan:
- Koble til en MCP-server ved hjelp av Server-Sent Events (SSE) transport
- Liste tilgjengelige verktøy fra serveren
- Kalle ulike kalkulatorfunksjoner eksternt
- Håndtere svar og vise resultater

## Hvordan det fungerer

Klienten bruker Spring AI MCP-rammeverket til å:

1. **Etablere tilkobling**: Oppretter en WebFlux SSE-klienttransport for å koble til kalkulatorserveren
2. **Initialisere klient**: Setter opp MCP-klienten og etablerer tilkoblingen
3. **Oppdage verktøy**: Lister alle tilgjengelige kalkulatoroperasjoner
4. **Utføre operasjoner**: Kaller ulike matematiske funksjoner med eksempeldata
5. **Vise resultater**: Viser resultatene av hver beregning

## Prosjektstruktur

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

## Viktige avhengigheter

Prosjektet bruker følgende viktige avhengigheter:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Denne avhengigheten gir:
- `McpClient` - Hovedklientgrensesnittet
- `WebFluxSseClientTransport` - SSE-transport for webbasert kommunikasjon
- MCP-protokollskjemaer og forespørsels-/svar-typer

## Bygge prosjektet

Bygg prosjektet med Maven-wrapperen:

```cmd
.\mvnw clean install
```

## Kjøre klienten

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Merk**: Sørg for at kalkulatorserveren kjører på `http://localhost:8080` før du kjører noen av disse kommandoene.

## Hva klienten gjør

Når du kjører klienten, vil den:

1. **Koble til** kalkulatorserveren på `http://localhost:8080`
2. **Liste verktøy** - Viser alle tilgjengelige kalkulatoroperasjoner
3. **Utføre beregninger**:
   - Addisjon: 5 + 3 = 8
   - Subtraksjon: 10 - 4 = 6
   - Multiplikasjon: 6 × 7 = 42
   - Divisjon: 20 ÷ 4 = 5
   - Potens: 2^8 = 256
   - Kvadratrot: √16 = 4
   - Absoluttverdi: |-5.5| = 5.5
   - Hjelp: Viser tilgjengelige operasjoner

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

**Merk**: Du kan se Maven-advarsler om hengende tråder på slutten – dette er normalt for reaktive applikasjoner og indikerer ikke en feil.

## Forstå koden

### 1. Transportoppsett
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Dette oppretter en SSE (Server-Sent Events) transport som kobler til kalkulatorserveren.

### 2. Klientopprettelse
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Oppretter en synkron MCP-klient og initialiserer tilkoblingen.

### 3. Kalle verktøy
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Kaller "add"-verktøyet med parametrene a=5.0 og b=3.0.

## Feilsøking

### Server kjører ikke
Hvis du får tilkoblingsfeil, sørg for at kalkulatorserveren fra Kapittel 01 kjører:
```
Error: Connection refused
```
**Løsning**: Start kalkulatorserveren først.

### Porten er allerede i bruk
Hvis port 8080 er opptatt:
```
Error: Address already in use
```
**Løsning**: Stopp andre applikasjoner som bruker port 8080, eller endre serveren til å bruke en annen port.

### Byggefeil
Hvis du får byggefeil:
```cmd
.\mvnw clean install -DskipTests
```

## Lær mer

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.