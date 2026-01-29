# MCP Java Client - Ukázka kalkulačky

Tento projekt ukazuje, jak vytvořit Java klienta, který se připojuje a komunikuje s MCP (Model Context Protocol) serverem. V tomto příkladu se připojíme ke kalkulačnímu serveru z kapitoly 01 a provedeme různé matematické operace.

## Požadavky

Před spuštěním tohoto klienta je potřeba:

1. **Spustit kalkulační server** z kapitoly 01:
   - Přejděte do adresáře kalkulačního serveru: `03-GettingStarted/01-first-server/solution/java/`
   - Sestavte a spusťte kalkulační server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Server by měl běžet na adrese `http://localhost:8080`

2. Mít nainstalovanou **Javu 21 nebo novější**
3. Mít k dispozici **Maven** (součástí je Maven Wrapper)

## Co je SDKClient?

`SDKClient` je Java aplikace, která ukazuje, jak:
- Připojit se k MCP serveru pomocí Server-Sent Events (SSE) transportu
- Vypsat dostupné nástroje ze serveru
- Vzdáleně volat různé kalkulační funkce
- Zpracovat odpovědi a zobrazit výsledky

## Jak to funguje

Klient využívá Spring AI MCP framework k:

1. **Navázání spojení**: Vytvoří WebFlux SSE klientský transport pro připojení ke kalkulačnímu serveru
2. **Inicializaci klienta**: Nastaví MCP klienta a naváže spojení
3. **Objevení nástrojů**: Vylistuje všechny dostupné kalkulační operace
4. **Provedení operací**: Zavolá různé matematické funkce s ukázkovými daty
5. **Zobrazení výsledků**: Ukáže výsledky jednotlivých výpočtů

## Struktura projektu

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

## Klíčové závislosti

Projekt používá následující hlavní závislosti:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Tato závislost poskytuje:
- `McpClient` - hlavní klientské rozhraní
- `WebFluxSseClientTransport` - SSE transport pro webovou komunikaci
- MCP protokolové schémata a typy požadavků/odpovědí

## Sestavení projektu

Projekt sestavíte pomocí Maven wrapperu:

```cmd
.\mvnw clean install
```

## Spuštění klienta

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Poznámka**: Před spuštěním těchto příkazů se ujistěte, že kalkulační server běží na `http://localhost:8080`.

## Co klient dělá

Po spuštění klienta:

1. **Připojí se** ke kalkulačnímu serveru na `http://localhost:8080`
2. **Vylistuje nástroje** - zobrazí všechny dostupné kalkulační operace
3. **Provede výpočty**:
   - Sčítání: 5 + 3 = 8
   - Odčítání: 10 - 4 = 6
   - Násobení: 6 × 7 = 42
   - Dělení: 20 ÷ 4 = 5
   - Mocnina: 2^8 = 256
   - Druhá odmocnina: √16 = 4
   - Absolutní hodnota: |-5.5| = 5.5
   - Nápověda: Zobrazí dostupné operace

## Očekávaný výstup

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

**Poznámka**: Na konci se mohou objevit varování Maven o přetrvávajících vláknech – je to běžné u reaktivních aplikací a neznamená to chybu.

## Pochopení kódu

### 1. Nastavení transportu
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Tím se vytvoří SSE (Server-Sent Events) transport, který se připojí ke kalkulačnímu serveru.

### 2. Vytvoření klienta
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Vytvoří synchronní MCP klienta a inicializuje spojení.

### 3. Volání nástrojů
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Volá nástroj "add" s parametry a=5.0 a b=3.0.

## Řešení problémů

### Server neběží
Pokud se objeví chyby připojení, ujistěte se, že kalkulační server z kapitoly 01 běží:
```
Error: Connection refused
```
**Řešení**: Nejprve spusťte kalkulační server.

### Port je již obsazen
Pokud je port 8080 obsazen:
```
Error: Address already in use
```
**Řešení**: Ukončete jiné aplikace používající port 8080 nebo změňte port serveru.

### Chyby při sestavení
Pokud narazíte na chyby při sestavení:
```cmd
.\mvnw clean install -DskipTests
```

## Další zdroje

- [Spring AI MCP Dokumentace](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Specifikace Model Context Protocol](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentace](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.