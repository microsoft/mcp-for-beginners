# MCP Server s transportem stdio

> **⚠️ Důležitá aktualizace**: Od specifikace MCP 2025-06-18 byl samostatný transport SSE (Server-Sent Events) **zastaralý** a nahrazen transportem "Streamable HTTP". Aktuální specifikace MCP definuje dva hlavní transportní mechanismy:
> 1. **stdio** - Standardní vstup/výstup (doporučeno pro lokální servery)
> 2. **Streamable HTTP** - Pro vzdálené servery, které mohou interně používat SSE
>
> Tato lekce byla aktualizována, aby se zaměřila na **transport stdio**, což je doporučený přístup pro většinu implementací MCP serverů.

Transport stdio umožňuje MCP serverům komunikovat s klienty prostřednictvím standardních vstupních a výstupních proudů. Jedná se o nejčastěji používaný a doporučený transportní mechanismus v aktuální specifikaci MCP, který poskytuje jednoduchý a efektivní způsob, jak vytvářet MCP servery, které lze snadno integrovat s různými klientskými aplikacemi.

## Přehled

Tato lekce se zabývá tím, jak vytvořit a používat MCP servery s transportem stdio.

## Cíle učení

Na konci této lekce budete schopni:

- Vytvořit MCP server s transportem stdio.
- Ladit MCP server pomocí Inspektoru.
- Používat MCP server ve Visual Studio Code.
- Porozumět aktuálním transportním mechanismům MCP a důvodům, proč je stdio doporučeno.

## Transport stdio - Jak funguje

Transport stdio je jedním ze dvou podporovaných typů transportu v aktuální specifikaci MCP (2025-06-18). Zde je, jak funguje:

- **Jednoduchá komunikace**: Server čte zprávy JSON-RPC ze standardního vstupu (`stdin`) a odesílá zprávy na standardní výstup (`stdout`).
- **Procesní model**: Klient spouští MCP server jako podproces.
- **Formát zpráv**: Zprávy jsou jednotlivé požadavky, oznámení nebo odpovědi JSON-RPC, oddělené novými řádky.
- **Logování**: Server MŮŽE zapisovat řetězce UTF-8 na standardní chybu (`stderr`) pro účely logování.

### Klíčové požadavky:
- Zprávy MUSÍ být odděleny novými řádky a NESMÍ obsahovat vložené nové řádky.
- Server NESMÍ zapisovat na `stdout` nic, co není platná zpráva MCP.
- Klient NESMÍ zapisovat na `stdin` serveru nic, co není platná zpráva MCP.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

V předchozím kódu:

- Importujeme třídu `Server` a `StdioServerTransport` z MCP SDK.
- Vytváříme instanci serveru se základní konfigurací a schopnostmi.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

V předchozím kódu:

- Vytváříme instanci serveru pomocí MCP SDK.
- Definujeme nástroje pomocí dekorátorů.
- Používáme kontextový manažer `stdio_server` pro zpracování transportu.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Hlavní rozdíl oproti SSE je, že servery stdio:

- Nevyžadují nastavení webového serveru nebo HTTP endpointů.
- Jsou spouštěny jako podprocesy klientem.
- Komunikují prostřednictvím proudů stdin/stdout.
- Jsou jednodušší na implementaci a ladění.

## Cvičení: Vytvoření serveru stdio

Pro vytvoření našeho serveru musíme mít na paměti dvě věci:

- Musíme použít webový server k vystavení endpointů pro připojení a zprávy.

## Laboratoř: Vytvoření jednoduchého MCP serveru stdio

V této laboratoři vytvoříme jednoduchý MCP server pomocí doporučeného transportu stdio. Tento server bude vystavovat nástroje, které mohou klienti volat pomocí standardního protokolu Model Context Protocol.

### Předpoklady

- Python 3.8 nebo novější.
- MCP Python SDK: `pip install mcp`.
- Základní znalost asynchronního programování.

Začněme vytvořením našeho prvního MCP serveru stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Klíčové rozdíly oproti zastaralému přístupu SSE

**Transport stdio (aktuální standard):**
- Jednoduchý model podprocesu - klient spouští server jako podproces.
- Komunikace přes stdin/stdout pomocí zpráv JSON-RPC.
- Není potřeba nastavení HTTP serveru.
- Lepší výkon a bezpečnost.
- Snadnější ladění a vývoj.

**Transport SSE (zastaralý od MCP 2025-06-18):**
- Vyžadoval HTTP server s endpointy SSE.
- Složitější nastavení s infrastrukturou webového serveru.
- Další bezpečnostní úvahy pro HTTP endpointy.
- Nyní nahrazen Streamable HTTP pro webové scénáře.

### Vytvoření serveru s transportem stdio

Pro vytvoření serveru stdio musíme:

1. **Importovat potřebné knihovny** - Potřebujeme komponenty MCP serveru a transport stdio.
2. **Vytvořit instanci serveru** - Definovat server s jeho schopnostmi.
3. **Definovat nástroje** - Přidat funkce, které chceme vystavit.
4. **Nastavit transport** - Konfigurovat komunikaci stdio.
5. **Spustit server** - Spustit server a zpracovávat zprávy.

Postupujme krok za krokem:

### Krok 1: Vytvoření základního serveru stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Krok 2: Přidání dalších nástrojů

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Krok 3: Spuštění serveru

Uložte kód jako `server.py` a spusťte ho z příkazového řádku:

```bash
python server.py
```

Server se spustí a bude čekat na vstup ze stdin. Komunikuje pomocí zpráv JSON-RPC přes transport stdio.

### Krok 4: Testování pomocí Inspektoru

Server můžete otestovat pomocí MCP Inspektoru:

1. Nainstalujte Inspektor: `npx @modelcontextprotocol/inspector`.
2. Spusťte Inspektor a nasměrujte ho na váš server.
3. Otestujte nástroje, které jste vytvořili.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Ladění vašeho serveru stdio

### Použití MCP Inspektoru

MCP Inspektor je cenný nástroj pro ladění a testování MCP serverů. Zde je, jak ho použít s vaším serverem stdio:

1. **Nainstalujte Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Spusťte Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Otestujte váš server**: Inspektor poskytuje webové rozhraní, kde můžete:
   - Zobrazit schopnosti serveru.
   - Testovat nástroje s různými parametry.
   - Monitorovat zprávy JSON-RPC.
   - Ladit problémy s připojením.

### Použití VS Code

Můžete také ladit váš MCP server přímo ve VS Code:

1. Vytvořte konfiguraci spuštění v `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Nastavte body přerušení ve vašem kódu serveru.
3. Spusťte debugger a testujte pomocí Inspektoru.

### Tipy pro ladění

- Používejte `stderr` pro logování - nikdy nezapisujte na `stdout`, protože je vyhrazeno pro zprávy MCP.
- Ujistěte se, že všechny zprávy JSON-RPC jsou odděleny novými řádky.
- Testujte nejprve jednoduché nástroje, než přidáte složitější funkce.
- Používejte Inspektor k ověření formátů zpráv.

## Používání vašeho serveru stdio ve VS Code

Jakmile vytvoříte svůj MCP server stdio, můžete ho integrovat s VS Code a používat ho s Claude nebo jinými klienty kompatibilními s MCP.

### Konfigurace

1. **Vytvořte konfigurační soubor MCP** na `%APPDATA%\Claude\claude_desktop_config.json` (Windows) nebo `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Restartujte Claude**: Zavřete a znovu otevřete Claude, aby načetl novou konfiguraci serveru.

3. **Otestujte připojení**: Zahajte konverzaci s Claude a zkuste použít nástroje vašeho serveru:
   - "Můžeš mě pozdravit pomocí nástroje pro pozdravy?"
   - "Spočítej součet 15 a 27."
   - "Jaké jsou informace o serveru?"

### Příklad serveru stdio v TypeScriptu

Zde je kompletní příklad v TypeScriptu pro referenci:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Příklad serveru stdio v .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Shrnutí

V této aktualizované lekci jste se naučili:

- Vytvářet MCP servery pomocí aktuálního **transportu stdio** (doporučený přístup).
- Porozumět důvodům, proč byl transport SSE zastaralý ve prospěch stdio a Streamable HTTP.
- Vytvářet nástroje, které mohou volat klienti MCP.
- Ladit váš server pomocí MCP Inspektoru.
- Integrovat váš server stdio s VS Code a Claude.

Transport stdio poskytuje jednodušší, bezpečnější a výkonnější způsob, jak vytvářet MCP servery ve srovnání se zastaralým přístupem SSE. Je to doporučený transport pro většinu implementací MCP serverů podle specifikace z 2025-06-18.

### .NET

1. Nejprve vytvoříme několik nástrojů, k tomu vytvoříme soubor *Tools.cs* s následujícím obsahem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Cvičení: Testování vašeho serveru stdio

Nyní, když jste vytvořili svůj server stdio, otestujte ho, abyste se ujistili, že funguje správně.

### Předpoklady

1. Ujistěte se, že máte nainstalovaný MCP Inspektor:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Váš kód serveru by měl být uložen (např. jako `server.py`).

### Testování pomocí Inspektoru

1. **Spusťte Inspektor s vaším serverem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otevřete webové rozhraní**: Inspektor otevře okno prohlížeče zobrazující schopnosti vašeho serveru.

3. **Otestujte nástroje**: 
   - Vyzkoušejte nástroj `get_greeting` s různými jmény.
   - Otestujte nástroj `calculate_sum` s různými čísly.
   - Zavolejte nástroj `get_server_info`, abyste viděli metadata serveru.

4. **Monitorujte komunikaci**: Inspektor zobrazuje zprávy JSON-RPC, které si klient a server vyměňují.

### Co byste měli vidět

Když váš server správně funguje, měli byste vidět:
- Schopnosti serveru uvedené v Inspektoru.
- Nástroje dostupné pro testování.
- Úspěšné výměny zpráv JSON-RPC.
- Odpovědi nástrojů zobrazené v rozhraní.

### Běžné problémy a řešení

**Server se nespustí:**
- Zkontrolujte, zda jsou všechny závislosti nainstalovány: `pip install mcp`.
- Ověřte syntaxi Pythonu a odsazení.
- Hledejte chybové zprávy v konzoli.

**Nástroje se nezobrazují:**
- Ujistěte se, že jsou přítomny dekorátory `@server.tool()`.
- Zkontrolujte, zda jsou funkce nástrojů definovány před `main()`.
- Ověřte, že server je správně nakonfigurován.

**Problémy s připojením:**
- Ujistěte se, že server správně používá transport stdio.
- Zkontrolujte, zda žádné jiné procesy nezasahují.
- Ověřte syntaxi příkazu Inspektoru.

## Úkol

Zkuste rozšířit váš server o další schopnosti. Podívejte se na [tuto stránku](https://api.chucknorris.io/) a například přidejte nástroj, který volá API. Rozhodněte, jak by měl váš server vypadat. Bavte se :)

## Řešení

[Řešení](./solution/README.md) Zde je možné řešení s funkčním kódem.

## Klíčové poznatky

Klíčové poznatky z této kapitoly jsou následující:

- Transport stdio je doporučený mechanismus pro lokální MCP servery.
- Transport stdio umožňuje bezproblémovou komunikaci mezi MCP servery a klienty pomocí standardních vstupních a výstupních proudů.
- MCP servery můžete přímo používat a ladit pomocí Inspektoru a Visual Studio Code.

## Ukázky 

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python) 

## Další zdroje

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Co dál

## Další kroky

Nyní, když jste se naučili, jak vytvářet MCP servery s transportem stdio, můžete prozkoumat pokročilejší témata:

- **Další**: [HTTP Streaming s MCP (Streamable HTTP)](../06-http-streaming/README.md) - Naučte se o druhém podporovaném transportním mechanismu pro vzdálené servery.
- **Pokročilé**: [Nejlepší bezpečnostní praktiky MCP](../../02-Security/README.md) - Implementujte bezpečnost ve vašich MCP serverech.
- **Produkce**: [Strategie nasazení](../09-deployment/README.md) - Nasazení vašich serverů pro produkční použití.

## Další zdroje

- [Specifikace MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Oficiální specifikace.
- [Dokumentace MCP SDK](https://github.com/modelcontextprotocol/sdk) - Odkazy na SDK pro všechny jazyky.
- [Příklady komunity](../../06-CommunityContributions/README.md) - Další příklady serverů od komunity.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Nenese odpovědnost za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.