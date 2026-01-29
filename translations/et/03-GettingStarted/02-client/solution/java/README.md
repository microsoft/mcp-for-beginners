# MCP Java Client - Kalkulaatori Demo

See projekt näitab, kuidas luua Java klient, mis ühendub MCP (Model Context Protocol) serveriga ja suhtleb sellega. Selles näites ühendume 1. peatüki kalkulaatori serveriga ja teeme erinevaid matemaatilisi operatsioone.

## Eeltingimused

Enne kliendi käivitamist veendu, et:

1. **Käivita Kalkulaatori Server** 1. peatükist:
   - Liigu kalkulaatori serveri kataloogi: `03-GettingStarted/01-first-server/solution/java/`
   - Ehita ja käivita kalkulaatori server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Server peaks töötama aadressil `http://localhost:8080`

2. **Java 21 või uuem** peab olema süsteemis installitud
3. **Maven** (kaasas Maven Wrapperi kaudu)

## Mis on SDKClient?

`SDKClient` on Java rakendus, mis näitab, kuidas:
- Ühendada MCP serveriga kasutades Server-Sent Events (SSE) transporti
- Loetleda serveris saadaval olevad tööriistad
- Kaugelt kutsuda erinevaid kalkulaatori funktsioone
- Käsitleda vastuseid ja kuvada tulemusi

## Kuidas see töötab

Klient kasutab Spring AI MCP raamistikku, et:

1. **Ühenduse loomine**: Loob WebFlux SSE kliendi transpordi, et ühendada kalkulaatori serveriga
2. **Kliendi initsialiseerimine**: Seadistab MCP kliendi ja loob ühenduse
3. **Tööriistade avastamine**: Loetleb kõik saadaval olevad kalkulaatori operatsioonid
4. **Operatsioonide täitmine**: Kutsutakse erinevaid matemaatilisi funktsioone näidisandmetega
5. **Tulemuste kuvamine**: Näitab iga arvutuse tulemusi

## Projekti struktuur

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

## Olulised sõltuvused

Projekt kasutab järgmisi olulisi sõltuvusi:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

See sõltuvus pakub:
- `McpClient` - Peamine kliendi liides
- `WebFluxSseClientTransport` - SSE transport veebipõhiseks suhtluseks
- MCP protokolli skeemid ja päringu/vastuse tüübid

## Projekti ehitamine

Ehita projekt kasutades Maven Wrapperit:

```cmd
.\mvnw clean install
```

## Kliendi käivitamine

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Märkus**: Veendu, et kalkulaatori server töötab aadressil `http://localhost:8080` enne nende käskude täitmist.

## Mida klient teeb

Kui käivitate kliendi, siis see:

1. **Ühendub** kalkulaatori serveriga aadressil `http://localhost:8080`
2. **Loetleb tööriistad** - Näitab kõiki saadaval olevaid kalkulaatori operatsioone
3. **Teostab arvutusi**:
   - Liitmine: 5 + 3 = 8
   - Lahutamine: 10 - 4 = 6
   - Korrutamine: 6 × 7 = 42
   - Jagamine: 20 ÷ 4 = 5
   - Astendamine: 2^8 = 256
   - Ruutjuur: √16 = 4
   - Absoluutväärtus: |-5.5| = 5.5
   - Abi: Näitab saadaval olevaid operatsioone

## Oodatav väljund

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

**Märkus**: Võite näha Maveni hoiatusi lõpus rippuvate lõimede kohta - see on reaktiivsete rakenduste puhul normaalne ega tähenda viga.

## Koodi mõistmine

### 1. Transpordi seadistamine
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
See loob SSE (Server-Sent Events) transpordi, mis ühendub kalkulaatori serveriga.

### 2. Kliendi loomine
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Loob sünkroonse MCP kliendi ja initsialiseerib ühenduse.

### 3. Tööriistade kutsumine
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Kutsutakse "add" tööriista parameetritega a=5.0 ja b=3.0.

## Tõrkeotsing

### Server ei tööta
Kui ilmnevad ühenduse vead, veendu, et 1. peatüki kalkulaatori server töötab:
```
Error: Connection refused
```
**Lahendus**: Käivita esmalt kalkulaatori server.

### Port on juba kasutusel
Kui port 8080 on hõivatud:
```
Error: Address already in use
```
**Lahendus**: Peata teised rakendused, mis kasutavad porti 8080, või muuda serveri porti.

### Ehitamisvead
Kui ilmnevad ehitamisvead:
```cmd
.\mvnw clean install -DskipTests
```

## Lisainfo

- [Spring AI MCP Dokumentatsioon](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Spetsifikatsioon](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentatsioon](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.