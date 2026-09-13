# MCP server s transportem stdio

> **⚠️ Důležitá aktualizace**: Od specifikace MCP 2025-06-18 byl samostatný SSE (Server-Sent Events) transport **zrušen** a nahrazen transportem "Streamable HTTP". Současná specifikace MCP definuje dva hlavní transportní mechanismy:
> 1. **stdio** - Standardní vstup/výstup (doporučeno pro lokální servery)
> 2. **Streamable HTTP** - Pro vzdálené servery, které mohou interně používat SSE
>
> Tato lekce byla aktualizována tak, aby se zaměřila na **stdio transport**, což je doporučený přístup pro většinu implementací MCP serverů.

Transport stdio umožňuje MCP serverům komunikovat s klienty přes standardní vstupní a výstupní toky. Jedná se o nejčastěji používaný a doporučený transportní mechanismus v současné specifikaci MCP, který poskytuje jednoduchý a efektivní způsob, jak stavět MCP servery, které lze snadno integrovat s různými klientskými aplikacemi.

## Přehled

Tato lekce pokrývá, jak stavět a využívat MCP servery pomocí transportu stdio.

## Učební cíle

Po dokončení této lekce budete schopni:

- Vytvořit MCP server pomocí stdio transportu.
- Ladit MCP server pomocí Inspectoru.
- Využívat MCP server ve Visual Studio Code.
- Porozumět současným transportním mechanismům MCP a proč je stdio doporučeno.


## stdio transport - Jak to funguje

Transport stdio je jedním ze dvou standardních transportů ve specifikaci MCP
`2026-07-28`. Funguje takto:

- **Jednoduchá komunikace**: Server čte JSON-RPC zprávy ze standardního vstupu (`stdin`) a odesílá zprávy na standardní výstup (`stdout`).
- **Procesově založený**: Klient spouští MCP server jako podsystém.
- **Formát zprávy**: Zprávy jsou jednotlivé JSON-RPC požadavky, notifikace nebo odpovědi, oddělené novými řádky.
- **Protokolování**: Server MŮŽE zapisovat UTF-8 řetězce do standardní chyby (`stderr`) pro účely logování.

### Klíčové požadavky:
- Zprávy MUSÍ být odděleny novými řádky a NESMÍ obsahovat vložené nové řádky
- Server NESMÍ zapisovat na `stdout` nic, co není platná MCP zpráva
- Klient NESMÍ zapisovat do `stdin` serveru nic, co není platná MCP zpráva

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
- Vytvoříme instanci serveru s základní konfigurací a schopnostmi
- Vytvoříme instanci `StdioServerTransport` a připojíme k ní server, čímž umožníme komunikaci přes stdin/stdout

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

- Vytvoříme instanci serveru pomocí MCP SDK
- Definujeme nástroje pomocí dekorátorů
- Používáme context manager stdio_server pro správu transportu

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

- Nepotřebují nastavení webového serveru ani HTTP endpointy
- Jsou spouštěny klientem jako podsystémy
- Komunikují přes stdin/stdout toky
- Jsou jednodušší na implementaci a ladění

## Cvičení: Vytvoření stdio serveru

Při vytváření našeho serveru musíme mít na paměti dvě věci:

- Nepotřebujeme použít webový server k vystavení endpointů pro připojení a zprávy.
## Lab: Vytvoření jednoduchého MCP stdio serveru

V tomto labu vytvoříme jednoduchý MCP server pomocí doporučeného stdio transportu. Tento server bude zpřístupňovat nástroje, které klienti mohou volat pomocí standardního Model Context Protocol.

### Požadavky

- Python 3.8 nebo novější
- MCP Python SDK: `pip install mcp`
- Základní znalost asynchronního programování

Začněme tvorbou našeho prvního MCP stdio serveru:

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

## Klíčové rozdíly oproti zrušenému SSE přístupu

**Stdio transport (současný standard):**
- Jednoduchý model podsystému – klient spouští server jako podřízený proces
- Komunikace přes stdin/stdout pomocí JSON-RPC zpráv
- Není potřeba nastavovat HTTP server
- Lepší výkon a bezpečnost
- Jednodušší ladění a vývoj

**SSE transport (zrušeno od MCP 2025-06-18):**
- Vyžaduje HTTP server se SSE endpointy
- Složitější nastavení s webovou serverovou infrastrukturou
- Dodatečné bezpečnostní požadavky pro HTTP endpointy
- Teď nahrazeno Streamable HTTP pro webové scénáře

### Vytvoření serveru se stdio transportem

Abychom vytvořili náš stdio server, musíme:

1. **Importovat potřebné knihovny** - potřebujeme komponenty MCP serveru a stdio transportu
2. **Vytvořit instanci serveru** - definovat server s jeho schopnostmi
3. **Definovat nástroje** - přidat funkcionalitu, kterou chceme zpřístupnit
4. **Nastavit transport** - nakonfigurovat stdio komunikaci
5. **Spustit server** - startovat server a zpracovávat zprávy

Postupně tuto sestavu vytvoříme:

### Krok 1: Vytvoření základního stdio serveru

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Nakonfigurujte protokolování
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Vytvořte server
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

Svůj server můžete testovat pomocí MCP Inspectoru:

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

MCP Inspector je užitečný nástroj pro ladění a testování MCP serverů. Zde je, jak ho použít s vaším stdio serverem:

1. **Nainstalujte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Spusťte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Otestujte server**: Inspector poskytuje webové rozhraní, kde můžete:
   - Prohlížet schopnosti serveru
   - Testovat nástroje s různými parametry
   - Sledovat JSON-RPC zprávy
   - Ladit problémy s připojením

### Použití VS Code

Můžete také debugovat svůj MCP server přímo ve VS Code:

1. Vytvořte launch konfiguraci v `.vscode/launch.json`:
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

2. Nastavte breakpointy ve vašem serverovém kódu
3. Spusťte debugger a testujte s Inspector

### Obvyklé tipy pro ladění

- Používejte `stderr` pro logování - nikdy nezapisujte na `stdout`, protože je vyhrazen pro MCP zprávy
- Zajistěte, aby všechny JSON-RPC zprávy byly oddělené novými řádky
- Nejprve testujte s jednoduchými nástroji před přidáním složitější funkčnosti
- Používejte Inspector k ověřování formátů zpráv

## Využití vašeho stdio serveru ve VS Code

Jakmile vytvoříte svůj MCP stdio server, můžete ho integrovat s VS Code a používat s Claude nebo jinými klienty kompatibilními s MCP.

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

2. **Restartujte Claude**: Zavřete a znovu otevřete Claude pro načtení nové konfigurace serveru.

3. **Otestujte připojení**: Zahajte konverzaci s Claudem a zkuste použít nástroje vašeho serveru:
   - "Umíš mě pozdravit pomocí nástroje pro pozdravy?"
   - "Spočítej součet 15 a 27"
   - "Jaké jsou informace o serveru?"

### Příklad stdio serveru v TypeScriptu

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

### Příklad stdio serveru v .NET

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

- Stavět MCP servery používající současný **stdio transport** (doporučený přístup)
- Porozumět, proč byl SSE transport zrušen ve prospěch stdio a Streamable HTTP
- Vytvářet nástroje, které mohou být volány MCP klienty
- Ladit server pomocí MCP Inspectoru
- Integrovat váš stdio server s VS Code a Claude

Transport stdio poskytuje jednodušší, bezpečnější a výkonnější způsob, jak stavět MCP servery ve srovnání se zrušeným SSE přístupem. Je to doporučený transport pro většinu implementací MCP serverů dle specifikace 2025-06-18.


### .NET

1. Nejprve si vytvoříme nějaké nástroje, k tomu vytvoříme soubor *Tools.cs* s následujícím obsahem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Cvičení: Testování vašeho stdio serveru

Jakmile máte postavený svůj stdio server, vyzkoušíme ho, aby fungoval správně.

### Požadavky

1. Ujistěte se, že máte nainstalovaný MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Váš kód serveru by měl být uložený (např. jako `server.py`)

### Testování pomocí Inspectoru

1. **Spusťte Inspector spolu se serverem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otevřete webové rozhraní**: Inspector otevře v prohlížeči okno zobrazující schopnosti vašeho serveru.

3. **Testujte nástroje**: 
   - Vyzkoušejte nástroj `get_greeting` s různými jmény
   - Otestujte nástroj `calculate_sum` s různými čísly
   - Zavolejte nástroj `get_server_info` pro zobrazení metadat serveru

4. **Sledujte komunikaci**: Inspector ukazuje JSON-RPC zprávy vyměňované mezi klientem a serverem.

### Co byste měli vidět

Když se server správně spustí, měli byste vidět:
- Schopnosti serveru zobrazené v Inspectoru
- Dostupné nástroje k testování
- Úspěšné výměny JSON-RPC zpráv
- Odpovědi nástrojů zobrazené v rozhraní

### Časté problémy a řešení

**Server se nenastartuje:**
- Zkontrolujte, že máte nainstalovány všechny závislosti: `pip install mcp`
- Ověřte syntaxi a odsazení v Pythonu
- Hledejte chybová hlášení v konzoli

**Nástroje se nezobrazují:**
- Ujistěte se, že máte dekorátory `@server.tool()`
- Zkontrolujte, že funkce nástrojů jsou definovány před funkcí `main()`
- Ověřte, že server je správně nakonfigurován

**Problémy s připojením:**
- Zajistěte, že server správně používá stdio transport
- Zkontrolujte, že žádné jiné procesy nezasahují
- Ověřte syntax příkazu Inspectoru

## Úkol

Zkuste rozšířit svůj server o více schopností. Podívejte se na [tuto stránku](https://api.chucknorris.io/), kde můžete například přidat nástroj, který volá API. Vy rozhodnete, jak bude server vypadat. Bavte se :)
## Řešení

[Řešení](./solution/README.md) Zde je možné řešení s funkčním kódem.

## Klíčové poznatky

Klíčové poznatky z této kapitoly jsou následující:

- Transport stdio je doporučený mechanismus pro lokální MCP servery.
- Transport stdio umožňuje plynulou komunikaci mezi MCP servery a klienty pomocí standardních vstupních a výstupních toků.
- Můžete použít jak Inspector, tak Visual Studio Code, abyste přímo využívali stdio servery, což usnadňuje ladění a integraci.

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

Nyní, když jste se naučili stavět MCP servery s stdio transportem, můžete prozkoumat pokročilejší témata:

- **Dále**: [HTTP Streamování s MCP (Streamable HTTP)](../06-http-streaming/README.md) - Naučte se o dalším podporovaném transportním mechanismu pro vzdálené servery
- **Pokročilé**: [Nejlepší bezpečnostní praktiky MCP](../../02-Security/README.md) - Implementujte bezpečnost do vašich MCP serverů
- **Produkční**: [Strategie nasazení](../09-deployment/README.md) - Nasazení serverů do produkčního prostředí

## Další zdroje

- [Specifikace MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Současná specifikace
- [Dokumentace MCP SDK](https://github.com/modelcontextprotocol/sdk) - Dokumentace SDK pro všechny jazyky
- [Ukázky komunity](../../06-CommunityContributions/README.md) - Další příklady serverů od komunity

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->