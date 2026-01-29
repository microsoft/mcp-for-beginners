# MCP Java Client - Calculator Demo

Ovaj projekt pokazuje kako napraviti Java klijenta koji se povezuje i komunicira s MCP (Model Context Protocol) serverom. U ovom primjeru povezujemo se na kalkulator server iz Poglavlja 01 i izvršavamo različite matematičke operacije.

## Preduvjeti

Prije pokretanja ovog klijenta, potrebno je:

1. **Pokrenuti Calculator Server** iz Poglavlja 01:
   - Otvorite direktorij kalkulator servera: `03-GettingStarted/01-first-server/solution/java/`
   - Izgradite i pokrenite kalkulator server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Server bi trebao biti dostupan na `http://localhost:8080`

2. Imati instaliran **Java 21 ili noviju verziju**
3. Imati **Maven** (uključen preko Maven Wrappera)

## Što je SDKClient?

`SDKClient` je Java aplikacija koja pokazuje kako:
- Povezati se na MCP server koristeći Server-Sent Events (SSE) transport
- Prikazati dostupne alate s servera
- Daljinski pozivati različite funkcije kalkulatora
- Obraditi odgovore i prikazati rezultate

## Kako radi

Klijent koristi Spring AI MCP framework za:

1. **Uspostavljanje veze**: Kreira WebFlux SSE klijentski transport za povezivanje s kalkulator serverom
2. **Inicijalizaciju klijenta**: Postavlja MCP klijenta i uspostavlja vezu
3. **Otkrivanje alata**: Prikazuje sve dostupne kalkulator operacije
4. **Izvršavanje operacija**: Poziva različite matematičke funkcije s primjerima podataka
5. **Prikaz rezultata**: Prikazuje rezultate svake kalkulacije

## Struktura projekta

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

## Ključne ovisnosti

Projekt koristi sljedeće ključne ovisnosti:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Ova ovisnost pruža:
- `McpClient` - Glavno klijentsko sučelje
- `WebFluxSseClientTransport` - SSE transport za web komunikaciju
- MCP protokol sheme i tipove zahtjeva/odgovora

## Izgradnja projekta

Izgradite projekt koristeći Maven wrapper:

```cmd
.\mvnw clean install
```

## Pokretanje klijenta

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Napomena**: Provjerite da je kalkulator server pokrenut na `http://localhost:8080` prije nego što izvršite bilo koju od ovih naredbi.

## Što klijent radi

Kada pokrenete klijenta, on će:

1. **Povezati se** na kalkulator server na `http://localhost:8080`
2. **Prikazati alate** - Prikazuje sve dostupne kalkulator operacije
3. **Izvršiti izračune**:
   - Zbrajanje: 5 + 3 = 8
   - Oduzimanje: 10 - 4 = 6
   - Množenje: 6 × 7 = 42
   - Dijeljenje: 20 ÷ 4 = 5
   - Potencija: 2^8 = 256
   - Korijen kvadratni: √16 = 4
   - Apsolutna vrijednost: |-5.5| = 5.5
   - Pomoć: Prikazuje dostupne operacije

## Očekivani ispis

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

**Napomena**: Možete vidjeti Maven upozorenja o zaostalim threadovima na kraju - to je normalno za reaktivne aplikacije i ne znači grešku.

## Razumijevanje koda

### 1. Postavljanje transporta
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Ovo kreira SSE (Server-Sent Events) transport koji se povezuje na kalkulator server.

### 2. Kreiranje klijenta
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Kreira sinkroni MCP klijent i inicijalizira vezu.

### 3. Pozivanje alata
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Poziva "add" alat s parametrima a=5.0 i b=3.0.

## Rješavanje problema

### Server nije pokrenut
Ako dobijete greške pri povezivanju, provjerite je li kalkulator server iz Poglavlja 01 pokrenut:
```
Error: Connection refused
```
**Rješenje**: Prvo pokrenite kalkulator server.

### Port je zauzet
Ako je port 8080 zauzet:
```
Error: Address already in use
```
**Rješenje**: Zaustavite druge aplikacije koje koriste port 8080 ili promijenite port servera.

### Greške pri izgradnji
Ako naiđete na greške pri izgradnji:
```cmd
.\mvnw clean install -DskipTests
```

## Saznajte više

- [Spring AI MCP Dokumentacija](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specifikacija](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentacija](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.