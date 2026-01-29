# MCP Java Client - Demo kalkulatorja

Ta projekt prikazuje, kako ustvariti Java klienta, ki se poveže in komunicira z MCP (Model Context Protocol) strežnikom. V tem primeru se bomo povezali s kalkulator strežnikom iz Poglavja 01 in izvedli različne matematične operacije.

## Predpogoji

Pred zagonom tega klienta morate:

1. **Zagnati kalkulator strežnik** iz Poglavja 01:
   - Pomaknite se v imenik kalkulator strežnika: `03-GettingStarted/01-first-server/solution/java/`
   - Sestavite in zaženite kalkulator strežnik:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Strežnik naj bo zagnan na `http://localhost:8080`

2. Imate nameščen **Java 21 ali novejšo različico**
3. Imate na voljo **Maven** (vključen preko Maven Wrapperja)

## Kaj je SDKClient?

`SDKClient` je Java aplikacija, ki prikazuje, kako:
- Povezati se z MCP strežnikom preko Server-Sent Events (SSE) transporta
- Pridobiti seznam razpoložljivih orodij s strežnika
- Oddajati različne funkcije kalkulatorja na daljavo
- Obdelati odgovore in prikazati rezultate

## Kako deluje

Klient uporablja Spring AI MCP ogrodje za:

1. **Vzpostavitev povezave**: Ustvari WebFlux SSE klient transport za povezavo s kalkulator strežnikom
2. **Inicializacijo klienta**: Nastavi MCP klienta in vzpostavi povezavo
3. **Odkritje orodij**: Prikaže vse razpoložljive kalkulator operacije
4. **Izvedbo operacij**: Pokliče različne matematične funkcije s primeri podatkov
5. **Prikaz rezultatov**: Prikaže rezultate vsakega izračuna

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

## Ključne odvisnosti

Projekt uporablja naslednje ključne odvisnosti:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Ta odvisnost zagotavlja:
- `McpClient` - glavni vmesnik klienta
- `WebFluxSseClientTransport` - SSE transport za spletno komunikacijo
- MCP protokolne sheme in tipe zahtevkov/odgovorov

## Sestavljanje projekta

Projekt sestavite z uporabo Maven wrapperja:

```cmd
.\mvnw clean install
```

## Zagon klienta

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Opomba**: Pred izvajanjem teh ukazov poskrbite, da je kalkulator strežnik zagnan na `http://localhost:8080`.

## Kaj klient počne

Ko zaženete klienta, bo:

1. **Povezal se** s kalkulator strežnikom na `http://localhost:8080`
2. **Prikazal orodja** - prikazal vse razpoložljive kalkulator operacije
3. **Izvedel izračune**:
   - Seštevanje: 5 + 3 = 8
   - Odštevanje: 10 - 4 = 6
   - Množenje: 6 × 7 = 42
   - Deljenje: 20 ÷ 4 = 5
   - Potenca: 2^8 = 256
   - Kvadratni koren: √16 = 4
   - Absolutna vrednost: |-5.5| = 5.5
   - Pomoč: prikaže razpoložljive operacije

## Pričakovani izhod

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

**Opomba**: Na koncu lahko vidite Maven opozorila o aktivnih nitih – to je običajno za reaktivne aplikacije in ne pomeni napake.

## Razumevanje kode

### 1. Nastavitev transporta
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Ustvari SSE (Server-Sent Events) transport, ki se poveže s kalkulator strežnikom.

### 2. Ustvarjanje klienta
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Ustvari sinhroni MCP klient in inicializira povezavo.

### 3. Klic orodij
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Pokliče orodje "add" s parametri a=5.0 in b=3.0.

## Reševanje težav

### Strežnik ni zagnan
Če prejmete napake povezave, preverite, da je kalkulator strežnik iz Poglavja 01 zagnan:
```
Error: Connection refused
```
**Rešitev**: Najprej zaženite kalkulator strežnik.

### Vrata so že zasedena
Če je vrata 8080 zasedena:
```
Error: Address already in use
```
**Rešitev**: Ustavite druge aplikacije, ki uporabljajo vrata 8080, ali spremenite vrata strežnika.

### Napake pri sestavljanju
Če naletite na napake pri sestavljanju:
```cmd
.\mvnw clean install -DskipTests
```

## Več informacij

- [Spring AI MCP Dokumentacija](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Specifikacija Model Context Protocol](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentacija](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.