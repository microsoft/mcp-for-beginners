# MCP server se stdio transportem

> **⚠️ Důležitá aktualizace**: Od MCP specifikace 2025-06-18 byl samostatný SSE (Server-Sent Events) transport **zrušen** a nahrazen transportem "Streamable HTTP". Aktuální MCP specifikace definuje dva hlavní transportní mechanismy:
> 1. **stdio** - Standardní vstup/výstup (doporučeno pro lokální servery)
> 2. **Streamable HTTP** - Pro vzdálené servery, které mohou interně používat SSE
>
> Tato lekce byla aktualizována tak, aby se zaměřila na **stdio transport**, což je doporučený přístup pro většinu implementací MCP serverů.

Stdio transport umožňuje MCP serverům komunikovat s klienty přes standardní vstupní a výstupní proudy. Jedná se o nejčastěji používaný a doporučený transportní mechanismus v aktuální specifikaci MCP, který poskytuje jednoduchý a efektivní způsob tvorby MCP serverů, které lze snadno integrovat s různými klientskými aplikacemi.

## Přehled

Tato lekce pokrývá, jak vytvářet a používat MCP servery pomocí stdio transportu.

## Cíle učení

Na konci této lekce budete schopni:

- Vytvořit MCP server pomocí stdio transportu.
- Ladit MCP server pomocí inspektora.
- Používat MCP server ve Visual Studio Code.
- Pochopit aktuální MCP transportní mechanismy a proč je doporučené stdio.

## stdio Transport – Jak to funguje

Stdio transport je jeden ze dvou podporovaných typů transportu v aktuální MCP specifikaci (2025-06-18). Zde je, jak funguje:

- **Jednoduchá komunikace**: Server čte JSON-RPC zprávy ze standardního vstupu (`stdin`) a odesílá zprávy na standardní výstup (`stdout`).
- **Procesní model**: Klient spouští MCP server jako podsproces.
- **Formát zpráv**: Zprávy jsou jednotlivé JSON-RPC požadavky, notifikace nebo odpovědi, oddělené novými řádky.
- **Logování**: Server MŮŽE zapisovat UTF-8 řetězce na standardní chyby (`stderr`) pro účely logování.

### Klíčové požadavky:
- Zprávy MUSÍ být odděleny novými řádky a NESMÍ obsahovat vložené nové řádky
- Server NESMÍ zapisovat na `stdout` nic, co není platnou MCP zprávou
- Klient NESMÍ zapisovat na serverův `stdin` nic, co není platnou MCP zprávou

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

- Importujeme třídu `Server` a `StdioServerTransport` z MCP SDK
- Vytvoříme instanci serveru se základní konfigurací a schopnostmi

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
- Používáme kontextový správce stdio_server pro správu transportu

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

- Nepotřebují nastavení webového serveru nebo HTTP endpointů
- Jsou spouštěny klientem jako podsprocesy
- Komunikují přes stdin/stdout proudy
- Jsou jednodušší na implementaci a ladění

## Cvičení: Vytvoření stdio serveru

Pro vytvoření našeho serveru musíme mít na paměti dvě věci:

- Potřebujeme webový server pro zpřístupnění endpointů pro připojení a zprávy.

## Laboratoř: Vytvoření jednoduchého MCP stdio serveru

V této laboratoři vytvoříme jednoduchý MCP server pomocí doporučeného stdio transportu. Tento server zpřístupní nástroje, které mohou klienti volat pomocí standardního Model Context Protocolu.

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
    # Použijte stdio přenos
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

**Stdio transport (aktuální standard):**
- Jednoduchý model podsprocesu – klient spouští server jako potomka
- Komunikace přes stdin/stdout používající JSON-RPC zprávy
- Není potřeba nastavovat HTTP server
- Lepší výkon a bezpečnost
- Jednodušší ladění a vývoj

**SSE transport (zrušený od MCP 2025-06-18):**
- Vyžadoval HTTP server s SSE endpointy
- Složitější nastavení s webovou serverovou infrastrukturou
- Další bezpečnostní ohledy pro HTTP endpointy
- Nyní nahrazen Streamable HTTP pro scénáře založené na webu

### Vytvoření serveru se stdio transportem

Chceme-li vytvořit náš stdio server, musíme:

1. **Importovat potřebné knihovny** – Potřebujeme komponenty MCP serveru a stdio transportu
2. **Vytvořit instanci serveru** – Definovat server s jeho schopnostmi
3. **Definovat nástroje** – Přidat funkce, které chceme zpřístupnit
4. **Nastavit transport** – Konfigurovat stdio komunikaci
5. **Spustit server** – Spustit server a zpracovávat zprávy

Postupujme krok za krokem:

### Krok 1: Vytvoření základního stdio serveru

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurujte protokolování
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

Uložte kód jako `server.py` a spusťte jej z příkazové řádky:

```bash
python server.py
```

Server se spustí a bude čekat na vstup ze stdin. Komunikuje pomocí JSON-RPC zpráv přes stdio transport.

### Krok 4: Testování pomocí inspektora

Server můžete testovat pomocí MCP Inspectoru:

1. Nainstalujte inspektora: `npx @modelcontextprotocol/inspector`
2. Spusťte inspektora a nasměrujte ho na váš server
3. Testujte nástroje, které jste vytvořili

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Ladění vašeho stdio serveru

### Použití MCP Inspectoru

MCP Inspector je cenný nástroj pro ladění a testování MCP serverů. Zde je, jak jej používat pro váš stdio server:

1. **Nainstalujte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Spusťte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testujte server**: Inspector poskytuje webové rozhraní, kde můžete:
   - Zobrazit schopnosti serveru
   - Testovat nástroje s různými parametry
   - Monitorovat JSON-RPC zprávy
   - Ladit problémy s připojením

### Použití VS Code

Můžete také ladit MCP server přímo ve VS Code:

1. Vytvořte konfigurační soubor spuštění v `.vscode/launch.json`:
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

2. Nastavte breakpointy ve svém serverovém kódu
3. Spusťte debugger a testujte pomocí Inspectoru

### Běžné tipy pro ladění

- Používejte `stderr` pro logování – nikdy nezapisujte do `stdout`, protože je vyhrazeno pro MCP zprávy
- Ujistěte se, že všechny JSON-RPC zprávy jsou odděleny novými řádky
- Nejprve testujte jednoduché nástroje, než přidáte složitější funkcionalitu
- Používejte Inspector k ověření formátu zpráv

## Použití vašeho stdio serveru ve VS Code

Jakmile vytvoříte MCP stdio server, můžete jej integrovat s VS Code a používat s Claude nebo jinými MCP kompatibilními klienty.

### Konfigurace

1. **Vytvořte MCP konfigurační soubor** na `%APPDATA%\Claude\claude_desktop_config.json` (Windows) nebo `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

3. **Otestujte připojení**: Začněte konverzaci s Claude a zkuste použít nástroje vašeho serveru:
   - „Můžeš mě pozdravit pomocí nástroje pro pozdrav?“
   - „Spočítej součet 15 a 27“
   - „Jaké jsou informace o serveru?“

### Příklad stdio serveru v TypeScriptu

Zde je kompletní příklad v TypeScriptu k nahlédnutí:

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

- Vytvářet MCP servery pomocí aktuálního **stdio transportu** (doporučený přístup)
- Pochopit, proč byl SSE transport zrušen ve prospěch stdio a Streamable HTTP
- Vytvářet nástroje, které mohou být volány MCP klienty
- Ladit server pomocí MCP Inspectoru
- Integrovat stdio server s VS Code a Claude

Stdio transport poskytuje jednodušší, bezpečnější a výkonnější způsob vytváření MCP serverů oproti zrušenému SSE přístupu. Je to doporučený transport pro většinu implementací MCP serverů podle specifikace 2025-06-18.

### .NET

1. Nejprve vytvoříme některé nástroje, pro které vytvoříme soubor *Tools.cs* s následujícím obsahem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Cvičení: Testování vašeho stdio serveru

Nyní, když jste vytvořili svůj stdio server, otestujme jej, abychom se ujistili, že funguje správně.

### Předpoklady

1. Ujistěte se, že máte nainstalovaný MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Váš serverový kód by měl být uložený (např. jako `server.py`)

### Testování pomocí Inspectoru

1. **Spusťte Inspector se svým serverem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otevřete webové rozhraní**: Inspector otevře prohlížeč s přehledem schopností vašeho serveru.

3. **Otestujte nástroje**:
   - Vyzkoušejte nástroj `get_greeting` s různými jmény
   - Otestujte nástroj `calculate_sum` s různými čísly
   - Zavolejte nástroj `get_server_info`, abyste viděli metadata serveru

4. **Monitorujte komunikaci**: Inspector ukazuje JSON-RPC zprávy vyměňované mezi klientem a serverem.

### Co byste měli vidět

Když se váš server správně spustí, měli byste vidět:
- Schopnosti serveru uvedené v Inspectoru
- Dostupné nástroje pro testování
- Úspěšné výměny JSON-RPC zpráv
- Odpovědi nástrojů zobrazené v rozhraní

### Běžné problémy a řešení

**Server se nespustí:**
- Zkontrolujte, že jsou všechny závislosti nainstalované: `pip install mcp`
- Ověřte syntaxi a odsazení v Pythonu
- Hledejte chybové zprávy v konzoli

**Nástroje se nezobrazují:**
- Ujistěte se, že dekorátory `@server.tool()` jsou přítomny
- Zkontrolujte, že funkce nástrojů jsou definovány před `main()`
- Ověřte správnou konfiguraci serveru

**Problémy s připojením:**
- Ujistěte se, že server používá stdio transport správně
- Zkontrolujte, že žádné jiné procesy nezasahují
- Ověřte syntaxi příkazu Inspectoru

## Zadání

Zkuste rozšířit svůj server o více schopností. Podívejte se na [tuto stránku](https://api.chucknorris.io/), abyste například přidali nástroj, který volá API. Rozhodněte, jak by měl server vypadat. Bavte se :)

## Řešení

[Řešení](./solution/README.md) Zde je možné řešení s funkčním kódem.

## Hlavní poznatky

Klíčové poznatky z této kapitoly jsou:

- Stdio transport je doporučovaný mechanismus pro lokální MCP servery.
- Stdio transport umožňuje plynulou komunikaci mezi MCP servery a klienty pomocí standardních vstupních a výstupních proudů.
- Můžete použít jak Inspector, tak Visual Studio Code k přímé práci se stdio servery, což usnadňuje ladění a integraci.

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

Nyní, když jste se naučili vytvářet MCP servery se stdio transportem, můžete prozkoumat pokročilejší témata:

- **Další**: [HTTP Streaming s MCP (Streamable HTTP)](../06-http-streaming/README.md) – Naučte se o dalším podporovaném transportním mechanismu pro vzdálené servery
- **Pokročilé**: [Nejlepší bezpečnostní praktiky MCP](../../02-Security/README.md) – Implementujte bezpečnost ve svých MCP serverech
- **Produkční provoz**: [Strategie nasazení](../09-deployment/README.md) – Nasazení serverů do produkčního provozu

## Další zdroje

- [MCP Specifikace 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Oficiální specifikace
- [MCP SDK dokumentace](https://github.com/modelcontextprotocol/sdk) – Reference SDK pro všechny jazyky
- [Příklady od komunity](../../06-CommunityContributions/README.md) – Více příkladů serverů od komunity

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybná vyložení vzniklé z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->