# MCP Server s stdio transportem

> **⚠️ Důležitá aktualizace**: Od MCP specifikace 2025-06-18 byl samostatný SSE (Server-Sent Events) transport **zastaralý** a nahrazen "Streamable HTTP" transportem. Současná MCP specifikace definuje dva hlavní transportní mechanismy:
> 1. **stdio** - Standardní vstup/výstup (doporučeno pro lokální servery)
> 2. **Streamable HTTP** - Pro vzdálené servery, které mohou SSE používat interně
>
> Tato lekce byla aktualizována s důrazem na **stdio transport**, který je doporučeným přístupem pro většinu implementací MCP serverů.

Stdio transport umožňuje MCP serverům komunikovat s klienty prostřednictvím standardních vstupních a výstupních toků. Jedná se o nejčastěji používaný a doporučený transportní mechanismus v aktuální MCP specifikaci, který poskytuje jednoduchý a efektivní způsob, jak vybudovat MCP servery, jež lze snadno integrovat s různými klientskými aplikacemi.

## Přehled

Tato lekce pokrývá, jak vytvořit a používat MCP servery pomocí stdio transportu.

## Cíle učení

Na konci této lekce budete schopni:

- Vytvořit MCP server pomocí stdio transportu.
- Ladit MCP server pomocí Inspectoru.
- Používat MCP server ve Visual Studio Code.
- Pochopit současné MCP transportní mechanismy a proč je stdio doporučeno.

## stdio Transport - Jak funguje

Stdio transport je jeden ze dvou podporovaných typů transportu v aktuální MCP specifikaci (2025-06-18). Funguje takto:

- **Jednoduchá komunikace**: Server čte JSON-RPC zprávy ze standardního vstupu (`stdin`) a odesílá zprávy na standardní výstup (`stdout`).
- **Procesně založený**: Klient spouští MCP server jako podproces.
- **Formát zpráv**: Zprávy jsou samostatné JSON-RPC požadavky, notifikace nebo odpovědi, oddělené novými řádky.
- **Logging**: Server MŮŽE zapisovat UTF-8 řetězce na standardní chybový výstup (`stderr`) pro účely logování.

### Klíčové požadavky:
- Zprávy MUSÍ být odděleny novými řádky a NESMÍ obsahovat vložené nové řádky
- Server NESMÍ zapisovat na `stdout` nic, co není platná MCP zpráva
- Klient NESMÍ zapisovat na serverův `stdin` nic, co není platná MCP zpráva

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

V předchozím kódu:

- Importujeme třídu `Server` a `StdioServerTransport` z MCP SDK
- Vytváříme instanci serveru s základní konfigurací a schopnostmi
- Vytváříme instanci `StdioServerTransport` a připojujeme k ní server, čímž umožňujeme komunikaci přes stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Vytvořit instanci serveru
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

- Vytváříme instanci serveru pomocí MCP SDK
- Definujeme nástroje pomocí dekorátorů
- Používáme kontextový manažer stdio_server k obsluze transportu

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Hlavní rozdíl oproti SSE je, že stdio servery:

- Nevyžadují nastavení webového serveru nebo HTTP endpointů
- Jsou spouštěny jako podprocesy klientem
- Komunikují přes stdin/stdout proudy
- Jsou jednodušší na implementaci a ladění

## Cvičení: Vytvoření stdio serveru

Při vytváření našeho serveru je třeba mít na paměti dvě věci:

- Je potřeba použít webový server k zpřístupnění endpointů pro připojení a zprávy.

## Laboratoř: Vytvoření jednoduchého MCP stdio serveru

V této laboratoři vytvoříme jednoduchý MCP server pomocí doporučeného stdio transportu. Tento server zpřístupní nástroje, které klienti mohou volat pomocí standardního Model Context Protocolu.

### Předpoklady

- Python 3.8 nebo novější
- MCP Python SDK: `pip install mcp`
- Základní znalost asynchronního programování

Začněme vytvořením našeho prvního MCP stdio serveru:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Nakonfigurujte protokolování
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Vytvořte server
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
    # Použijte stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Klíčové rozdíly oproti zastaralému SSE přístupu

**Stdio Transport (současný standard):**
- Jednoduchý model podprocesu - klient spouští server jako podsouborový proces
- Komunikace přes stdin/stdout pomocí JSON-RPC zpráv
- Nepotřebuje nastavení HTTP serveru
- Lepší výkon a bezpečnost
- Snazší ladění a vývoj

**SSE Transport (zastaralý od MCP 2025-06-18):**
- Vyžadoval HTTP server s SSE endpointy
- Komplikovanější nastavení s webovou serverovou infrastrukturou
- Další bezpečnostní úvahy pro HTTP endpointy
- Nyní nahrazen Streamable HTTP pro webové scénáře

### Vytvoření serveru se stdio transportem

Abyste mohli vytvořit náš stdio server, potřebujeme:

1. **Importovat potřebné knihovny** - Potřebujeme MCP server komponenty a stdio transport
2. **Vytvořit instanci serveru** - Definovat server s jeho schopnostmi
3. **Definovat nástroje** - Přidat funkce, které chceme zpřístupnit
4. **Nastavit transport** - Konfigurovat stdio komunikaci
5. **Spustit server** - Spustit server a zpracovávat zprávy

Postupujme krok za krokem:

### Krok 1: Vytvoření základního stdio serveru

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurace protokolování
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Vytvořit server
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

Uložte kód jako `server.py` a spusťte ho z příkazové řádky:

```bash
python server.py
```

Server se spustí a bude čekat na vstup ze stdin. Komunikuje pomocí JSON-RPC zpráv přes stdio transport.

### Krok 4: Testování pomocí Inspectoru

Server můžete otestovat pomocí MCP Inspectoru:

1. Nainstalujte Inspector: `npx @modelcontextprotocol/inspector`
2. Spusťte Inspector a nasměrujte ho na svůj server
3. Otestujte vytvořené nástroje

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Ladění vašeho stdio serveru

### Použití MCP Inspectoru

MCP Inspector je užitečný nástroj pro ladění a testování MCP serverů. Zde je návod, jak ho použít s vaším stdio serverem:

1. **Nainstalujte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Spusťte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Otestujte server**: Inspector poskytuje webové rozhraní, kde můžete:
   - Zobrazit schopnosti serveru
   - Testovat nástroje s různými parametry
   - Monitorovat JSON-RPC zprávy
   - Ladit problémy s připojením

### Použití VS Code

Můžete také ladit MCP server přímo ve VS Code:

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

2. Nastavte breakpointy ve svém kódu serveru
3. Spusťte debugger a testujte s Inspector

### Běžné tipy pro ladění

- Používejte `stderr` pro logování - nikdy nezapisujte do `stdout`, protože je vyhrazen pro MCP zprávy
- Ujistěte se, že všechny JSON-RPC zprávy jsou odděleny novými řádky
- Nejprve testujte s jednoduchými nástroji, než přidáte složitější funkce
- Použijte Inspector k ověření formátu zpráv

## Používání vašeho stdio serveru ve VS Code

Jakmile vytvoříte svůj MCP stdio server, můžete ho integrovat s VS Code pro použití s Claude nebo jinými MCP-kompatibilními klienty.

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

3. **Otestujte připojení**: Zahajte konverzaci s Claudem a zkuste použít nástroje vašeho serveru:
   - "Můžeš mě pozdravit pomocí nástroje greeting?"
   - "Vypočítej součet 15 a 27"
   - "Jaké jsou informace o serveru?"

### Příklad TypeScript stdio serveru

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

// Přidat nástroje
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

### Příklad .NET stdio serveru

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Shrnutí

V této aktualizované lekci jste se naučili:

- Vytvářet MCP servery pomocí aktuálního **stdio transportu** (doporučený přístup)
- Proč byl SSE transport nahrazen stdio a Streamable HTTP
- Vytvářet nástroje, které mohou volat MCP klienti
- Ladit server pomocí MCP Inspectoru
- Integrovat váš stdio server s VS Code a Claude

Stdio transport poskytuje jednodušší, bezpečnější a výkonnější způsob tvorby MCP serverů ve srovnání se zastaralým SSE přístupem. Je doporučeným transportem pro většinu MCP serverových implementací podle specifikace 2025-06-18.


### .NET

1. Nejprve vytvoříme nějaké nástroje, k tomu vytvoříme soubor *Tools.cs* s následujícím obsahem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Cvičení: Testování vašeho stdio serveru

Nyní, když jste svůj stdio server postavili, vyzkoušejte ho, abyste se ujistili, že funguje správně.

### Předpoklady

1. Ujistěte se, že máte nainstalovaný MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Váš kód serveru by měl být uložen (např. jako `server.py`)

### Testování pomocí Inspectoru

1. **Spusťte Inspector se svým serverem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otevřete webové rozhraní**: Inspector otevře okno prohlížeče, kde uvidíte schopnosti svého serveru.

3. **Otestujte nástroje**: 
   - Vyzkoušejte nástroj `get_greeting` s různými jmény
   - Otestujte nástroj `calculate_sum` s různými čísly
   - Zavolejte nástroj `get_server_info`, abyste viděli metadata serveru

4. **Sledujte komunikaci**: Inspector zobrazuje JSON-RPC zprávy vyměňované mezi klientem a serverem.

### Co byste měli vidět

Pokud se server správně spustí, měli byste vidět:
- Schopnosti serveru uvedené v Inspectoru
- Nástroje dostupné k testování
- Úspěšné výměny JSON-RPC zpráv
- Odpovědi nástrojů zobrazené v rozhraní

### Běžné problémy a řešení

**Server se nespustí:**
- Zkontrolujte, zda jsou všechny závislosti nainstalovány: `pip install mcp`
- Ověřte syntaxi a odsazení v Pythonu
- Hledejte chybové zprávy v konzoli

**Nástroje se nezobrazují:**
- Ujistěte se, že jste použili dekorátory `@server.tool()`
- Zkontrolujte, zda jsou funkce nástrojů definovány před voláním `main()`
- Ověřte správnou konfiguraci serveru

**Problémy s připojením:**
- Ujistěte se, že server správně používá stdio transport
- Zkontrolujte, zda žádné jiné procesy nezasahují
- Ověřte správnost syntaxe příkazu Inspectoru

## Zadání

Zkuste rozšířit svůj server o další schopnosti. Viz [tuto stránku](https://api.chucknorris.io/) pro příklad, jak přidat nástroj, který volá API. Rozhodněte, jak by váš server měl vypadat. Bavte se :)

## Řešení

[Řešení](./solution/README.md) Zde je možné řešení s fungujícím kódem.

## Klíčové poznatky

Hlavními poznatky z této kapitoly jsou:

- stdio transport je doporučený mechanismus pro lokální MCP servery.
- Stdio transport umožňuje plynulou komunikaci mezi MCP servery a klienty pomocí standardních vstupních a výstupních toků.
- Můžete použít jak Inspector, tak Visual Studio Code k přímému používání stdio serverů, což usnadňuje ladění a integraci.

## Ukázky

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Další zdroje

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Co dál

## Další kroky

Nyní, když jste se naučili, jak vytvářet MCP servery s stdio transportem, můžete se podívat na pokročilejší témata:

- **Další:** [HTTP Streaming s MCP (Streamable HTTP)](../06-http-streaming/README.md) – Seznamte se s dalším podporovaným transportem pro vzdálené servery
- **Pokročilé:** [Bezpečnostní postupy MCP](../../02-Security/README.md) – Implementace bezpečnosti ve vašich MCP serverech
- **Produkční nasazení:** [Strategie nasazení](../09-deployment/README.md) – Nasazení serverů pro produkční použití

## Další zdroje

- [MCP Specifikace 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Oficiální specifikace
- [MCP SDK Dokumentace](https://github.com/modelcontextprotocol/sdk) – SDK odkazy pro všechny jazyky
- [Příklady komunity](../../06-CommunityContributions/README.md) – Další příklady serverů od komunity

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Neneseme odpovědnost za jakékoli nedorozumění nebo mylné výklady vzniklé v důsledku použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->