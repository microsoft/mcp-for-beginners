# MCP stdio Server - .NET Řešení

> **⚠️ Důležité**: Toto řešení bylo aktualizováno tak, aby používalo **stdio transport**, jak je doporučeno ve specifikaci MCP 2025-06-18. Původní transport SSE byl ukončen.

## Přehled

Toto .NET řešení ukazuje, jak vytvořit MCP server s využitím aktuálního stdio transportu. Stdio transport je jednodušší, bezpečnější a poskytuje lepší výkon než zastaralý přístup SSE.

## Požadavky

- .NET 9.0 SDK nebo novější
- Základní znalost dependency injection v .NET

## Pokyny k nastavení

### Krok 1: Obnovení závislostí

```bash
dotnet restore
```

### Krok 2: Sestavení projektu

```bash
dotnet build
```

## Spuštění serveru

Stdio server funguje jinak než starý server založený na HTTP. Místo spuštění webového serveru komunikuje přes stdin/stdout:

```bash
dotnet run
```

**Důležité**: Server se může zdát, že "zamrzl" – to je normální! Čeká na JSON-RPC zprávy ze stdin.

## Testování serveru

### Metoda 1: Použití MCP Inspectoru (doporučeno)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Tímto:
1. Spustíte server jako podproces
2. Otevřete webové rozhraní pro testování
3. Můžete interaktivně testovat všechny nástroje serveru

### Metoda 2: Testování přímo z příkazové řádky

Můžete také testovat spuštěním Inspectoru přímo:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Dostupné nástroje

Server poskytuje tyto nástroje:

- **AddNumbers(a, b)**: Sečte dvě čísla
- **MultiplyNumbers(a, b)**: Vynásobí dvě čísla  
- **GetGreeting(name)**: Vytvoří personalizovaný pozdrav
- **GetServerInfo()**: Získá informace o serveru

### Testování s Claude Desktop

Pro použití tohoto serveru s Claude Desktop přidejte tuto konfiguraci do souboru `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Struktura projektu

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Klíčové rozdíly oproti HTTP/SSE

**stdio transport (aktuální):**
- ✅ Jednodušší nastavení – není potřeba webový server
- ✅ Lepší zabezpečení – žádné HTTP endpointy
- ✅ Používá `Host.CreateApplicationBuilder()` místo `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` místo `WithHttpTransport()`
- ✅ Konzolová aplikace místo webové aplikace
- ✅ Lepší výkon

**HTTP/SSE transport (zastaralý):**
- ❌ Vyžadoval ASP.NET Core webový server
- ❌ Potřeboval nastavení routingu `app.MapMcp()`
- ❌ Složitější konfigurace a závislosti
- ❌ Další bezpečnostní úvahy
- ❌ Nyní ukončeno ve specifikaci MCP 2025-06-18

## Funkce pro vývoj

- **Dependency Injection**: Plná podpora DI pro služby a logování
- **Strukturované logování**: Správné logování na stderr pomocí `ILogger<T>`
- **Atributy nástrojů**: Čistá definice nástrojů pomocí atributů `[McpServerTool]`
- **Podpora asynchronních operací**: Všechny nástroje podporují async operace
- **Zpracování chyb**: Elegantní zpracování chyb a logování

## Tipy pro vývoj

- Používejte `ILogger` pro logování (nikdy nepište přímo na stdout)
- Před testováním sestavte projekt pomocí `dotnet build`
- Testujte s Inspector pro vizuální ladění
- Veškeré logování automaticky směřuje na stderr
- Server zvládá signály pro elegantní ukončení

Toto řešení odpovídá aktuální specifikaci MCP a ukazuje osvědčené postupy pro implementaci stdio transportu v .NET.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese odpovědnost za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.