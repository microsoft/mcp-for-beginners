# MCP Java Client - Demo kalkulačky

Tento projekt ukazuje, ako vytvoriť Java klienta, ktorý sa pripája a komunikuje so serverom MCP (Model Context Protocol). V tomto príklade sa pripojíme k serveru kalkulačky z kapitoly 01 a vykonáme rôzne matematické operácie.

## Požiadavky

Pred spustením tohto klienta je potrebné:

1. **Spustiť server kalkulačky** z kapitoly 01:
   - Prejdite do adresára servera kalkulačky: `03-GettingStarted/01-first-server/solution/java/`
   - Skompilujte a spustite server kalkulačky:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Server by mal bežať na adrese `http://localhost:8080`

2. Mať nainštalovanú **Javu 21 alebo novšiu**
3. Mať k dispozícii **Maven** (zahrnutý cez Maven Wrapper)

## Čo je SDKClient?

`SDKClient` je Java aplikácia, ktorá demonštruje, ako:
- Pripojiť sa k MCP serveru pomocou Server-Sent Events (SSE) transportu
- Získať zoznam dostupných nástrojov zo servera
- Vzdialene volať rôzne funkcie kalkulačky
- Spracovať odpovede a zobraziť výsledky

## Ako to funguje

Klient využíva Spring AI MCP framework na:

1. **Nadviazanie spojenia**: Vytvorí WebFlux SSE klienta na pripojenie k serveru kalkulačky
2. **Inicializáciu klienta**: Nastaví MCP klienta a nadviaže spojenie
3. **Objavenie nástrojov**: Zobrazí všetky dostupné operácie kalkulačky
4. **Vykonanie operácií**: Zavolá rôzne matematické funkcie s ukážkovými dátami
5. **Zobrazenie výsledkov**: Ukáže výsledky jednotlivých výpočtov

## Štruktúra projektu

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

## Kľúčové závislosti

Projekt používa nasledujúce hlavné závislosti:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Táto závislosť poskytuje:
- `McpClient` - Hlavné rozhranie klienta
- `WebFluxSseClientTransport` - SSE transport pre webovú komunikáciu
- MCP protokolové schémy a typy požiadaviek/odpovedí

## Kompilácia projektu

Projekt zostavte pomocou Maven wrappera:

```cmd
.\mvnw clean install
```

## Spustenie klienta

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Poznámka**: Pred spustením týchto príkazov sa uistite, že server kalkulačky beží na `http://localhost:8080`.

## Čo klient robí

Po spustení klienta:

1. **Pripojí sa** k serveru kalkulačky na `http://localhost:8080`
2. **Zobrazí nástroje** - vypíše všetky dostupné operácie kalkulačky
3. **Vykoná výpočty**:
   - Sčítanie: 5 + 3 = 8
   - Odčítanie: 10 - 4 = 6
   - Násobenie: 6 × 7 = 42
   - Delenie: 20 ÷ 4 = 5
   - Mocnina: 2^8 = 256
   - Druhá odmocnina: √16 = 4
   - Absolútna hodnota: |-5.5| = 5.5
   - Pomocník: Zobrazí dostupné operácie

## Očakávaný výstup

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

**Poznámka**: Na konci sa môžu zobraziť varovania Maven o pretrvávajúcich vláknach – je to bežné pri reaktívnych aplikáciách a neznamená to chybu.

## Pochopenie kódu

### 1. Nastavenie transportu
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Týmto sa vytvorí SSE (Server-Sent Events) transport, ktorý sa pripojí k serveru kalkulačky.

### 2. Vytvorenie klienta
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Vytvorí sa synchronný MCP klient a inicializuje sa spojenie.

### 3. Volanie nástrojov
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Volá sa nástroj "add" s parametrami a=5.0 a b=3.0.

## Riešenie problémov

### Server nebeží
Ak sa vyskytne chyba pripojenia, uistite sa, že server kalkulačky z kapitoly 01 beží:
```
Error: Connection refused
```
**Riešenie**: Najprv spustite server kalkulačky.

### Port je už obsadený
Ak je port 8080 obsadený:
```
Error: Address already in use
```
**Riešenie**: Zastavte iné aplikácie používajúce port 8080 alebo upravte server, aby používal iný port.

### Chyby pri kompilácii
Ak sa vyskytnú chyby pri zostavovaní:
```cmd
.\mvnw clean install -DskipTests
```

## Viac informácií

- [Spring AI MCP Dokumentácia](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Špecifikácia Model Context Protocol](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentácia](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.