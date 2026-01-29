# MCP stdio Server - .NET Riešenie

> **⚠️ Dôležité**: Toto riešenie bolo aktualizované na používanie **stdio transportu** podľa odporúčaní MCP špecifikácie z 2025-06-18. Pôvodný SSE transport bol vyradený.

## Prehľad

Toto .NET riešenie ukazuje, ako vytvoriť MCP server pomocou aktuálneho stdio transportu. Stdio transport je jednoduchší, bezpečnejší a poskytuje lepší výkon ako zastaraný SSE prístup.

## Požiadavky

- .NET 9.0 SDK alebo novší
- Základné pochopenie .NET dependency injection

## Inštrukcie na nastavenie

### Krok 1: Obnovenie závislostí

```bash
dotnet restore
```

### Krok 2: Zostavenie projektu

```bash
dotnet build
```

## Spustenie servera

Stdio server funguje inak ako starý server založený na HTTP. Namiesto spustenia webového servera komunikuje cez stdin/stdout:

```bash
dotnet run
```

**Dôležité**: Server sa môže zdať, že "zamrzol" - to je normálne! Čaká na JSON-RPC správy zo stdin.

## Testovanie servera

### Metóda 1: Použitie MCP Inspector (Odporúčané)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Toto vykoná:
1. Spustí váš server ako podproces
2. Otvorí webové rozhranie na testovanie
3. Umožní vám interaktívne testovať všetky nástroje servera

### Metóda 2: Priame testovanie cez príkazový riadok

Môžete tiež testovať spustením Inspectora priamo:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Dostupné nástroje

Server poskytuje tieto nástroje:

- **AddNumbers(a, b)**: Sčíta dve čísla
- **MultiplyNumbers(a, b)**: Vynásobí dve čísla  
- **GetGreeting(name)**: Vytvorí personalizovaný pozdrav
- **GetServerInfo()**: Poskytne informácie o serveri

### Testovanie s Claude Desktop

Ak chcete tento server používať s Claude Desktop, pridajte túto konfiguráciu do vášho `claude_desktop_config.json`:

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

## Štruktúra projektu

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Kľúčové rozdiely oproti HTTP/SSE

**stdio transport (Aktuálny):**
- ✅ Jednoduchšie nastavenie - nie je potrebný webový server
- ✅ Lepšia bezpečnosť - žiadne HTTP endpointy
- ✅ Používa `Host.CreateApplicationBuilder()` namiesto `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` namiesto `WithHttpTransport()`
- ✅ Konzolová aplikácia namiesto webovej aplikácie
- ✅ Lepší výkon

**HTTP/SSE transport (Zastaraný):**
- ❌ Vyžadoval ASP.NET Core webový server
- ❌ Potreboval nastavenie routingu `app.MapMcp()`
- ❌ Zložitejšia konfigurácia a závislosti
- ❌ Dodatočné bezpečnostné úvahy
- ❌ Teraz vyradený v MCP 2025-06-18

## Vývojové funkcie

- **Dependency Injection**: Plná podpora DI pre služby a logovanie
- **Štruktúrované logovanie**: Správne logovanie na stderr pomocou `ILogger<T>`
- **Tool Attributes**: Čistá definícia nástrojov pomocou `[McpServerTool]` atribútov
- **Podpora Async**: Všetky nástroje podporujú asynchrónne operácie
- **Spracovanie chýb**: Elegantné spracovanie chýb a logovanie

## Tipy pre vývoj

- Používajte `ILogger` na logovanie (nikdy nepíšte priamo na stdout)
- Pred testovaním zostavte projekt pomocou `dotnet build`
- Testujte pomocou Inspectora pre vizuálne ladenie
- Všetky logy idú automaticky na stderr
- Server spracováva signály na elegantné ukončenie

Toto riešenie nasleduje aktuálnu MCP špecifikáciu a demonštruje najlepšie praktiky pre implementáciu stdio transportu pomocou .NET.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.