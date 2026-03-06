# MCP Server so stdio transportom

> **⚠️ Dôležitá aktualizácia**: Od špecifikácie MCP 2025-06-18 je samostatný SSE (Server-Sent Events) transport **zrušený** a nahradený transportom "Streamable HTTP". Súčasná špecifikácia MCP definuje dva hlavné mechanizmy transportu:
> 1. **stdio** - štandardný vstup/výstup (odporúčaný pre lokálne servery)
> 2. **Streamable HTTP** - pre vzdialené servery, ktoré môžu používať SSE interne
>
> Táto lekcia bola aktualizovaná tak, aby sa zamerala na **stdio transport**, ktorý je odporúčaným prístupom pre väčšinu implementácií MCP serverov.

Stdio transport umožňuje MCP serverom komunikovať s klientmi prostredníctvom štandardných vstupných a výstupných prúdov. Je to najbežnejšie používaný a odporúčaný mechanizmus transportu v súčasnej špecifikácii MCP, ktorý poskytuje jednoduchý a efektívny spôsob tvorby MCP serverov, ktoré je možné ľahko integrovať s rôznymi klientsymi aplikáciami.

## Prehľad

Táto lekcia pokrýva, ako vytvoriť a používať MCP servery so stdio transportom.

## Ciele učenia sa

Na konci tejto lekcie budete schopní:

- Vytvoriť MCP server pomocou stdio transportu.
- Ladenie MCP servera pomocou Inspectoru.
- Používať MCP server vo Visual Studio Code.
- Pochopiť aktuálne mechanizmy MCP transportu a prečo je stdio odporúčaný.


## stdio transport – Ako to funguje

Stdio transport je jeden z dvoch podporovaných typov transportu v súčasnej špecifikácii MCP (2025-06-18). Takto funguje:

- **Jednoduchá komunikácia**: server číta JSON-RPC správy zo štandardného vstupu (`stdin`) a posiela správy na štandardný výstup (`stdout`).
- **Procesový model**: klient spúšťa MCP server ako podproces.
- **Formát správ**: správy sú jednotlivé JSON-RPC požiadavky, oznámenia alebo odpovede, oddeľované odriadkovaním.
- **Logovanie**: server MÔŽE zapisovať UTF-8 reťazce na štandardnú chybu (`stderr`) na účely logovania.

### Kľúčové požiadavky:
- Správy MUSIA byť oddelené odriadkovaním a NESMÚ obsahovať vložené odriadkovania
- Server NESMIE zapisovať na `stdout` nič, čo nie je platná MCP správa
- Klient NESMIE zapisovať na `stdin` servera nič, čo nie je platná MCP správa

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

V predchádzajúcom kóde:

- Importujeme triedu `Server` a `StdioServerTransport` z MCP SDK
- Vytvoríme inštanciu servera s základnou konfiguráciou a schopnosťami

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Vytvorte inštanciu servera
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

V predchádzajúcom kóde:

- Vytvoríme inštanciu servera pomocou MCP SDK
- Definujeme nástroje pomocou dekorátorov
- Používame kontextový manažér stdio_server na ovládanie transportu

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

Hlavný rozdiel oproti SSE je, že stdio servery:

- Nevyžadujú nastavenie webového servera ani HTTP endpointy
- Sú spustené ako podprocesy klientom
- Komunikujú cez prúdy stdin/stdout
- Sú jednoduchšie na implementáciu a ladenie

## Cvičenie: Vytvorenie stdio serveru

Aby sme vytvorili náš server, musíme mať na pamäti dve veci:

- Potrebujeme webový server pre vystavenie endpointov pre pripojenie a správy.
## Lab: Vytvorenie jednoduchého MCP stdio servera

V tomto laboratóriu vytvoríme jednoduchý MCP server pomocou odporúčaného stdio transportu. Tento server vystaví nástroje, ktoré klienti môžu volať pomocou štandardného Model Context Protocol.

### Požiadavky

- Python 3.8 alebo novší
- MCP Python SDK: `pip install mcp`
- Základné znalosti asynchrónneho programovania

Začnime vytvorením nášho prvého MCP stdio servera:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigurujte protokolovanie
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Vytvorte server
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
    # Použite stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Kľúčové rozdiely oproti zrušenému SSE prístupu

**Stdio transport (súčasný štandard):**
- Jednoduchý model podprocesu – klient spúšťa server ako detský proces
- Komunikácia cez stdin/stdout pomocou JSON-RPC správ
- Nie je potrebné nastavovať HTTP server
- Lepší výkon a bezpečnosť
- Jednoduchšie ladenie a vývoj

**SSE transport (zrušený od MCP 2025-06-18):**
- Vyžadoval HTTP server s SSE endpointmi
- Komplexnejšie nastavenie webovej infraštruktúry
- Ďalšie bezpečnostné opatrenia pre HTTP endpointy
- Teraz nahradené Streamable HTTP pre webové scenáre

### Vytvorenie servera so stdio transportom

Aby sme vytvorili náš stdio server, potrebujeme:

1. **Importovať požadované knižnice** – potrebujeme MCP server komponenty a stdio transport
2. **Vytvoriť inštanciu servera** – definovať server so schopnosťami
3. **Definovať nástroje** – pridať funkcie, ktoré chceme vystaviť
4. **Nastaviť transport** – nakonfigurovať stdio komunikáciu
5. **Spustiť server** – naštartovať server a spracovať správy

Postupne to zostavme:

### Krok 1: Vytvorenie základného stdio servera

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurujte protokolovanie
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Vytvorte server
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

### Krok 2: Pridanie nástrojov

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

### Krok 3: Spustenie servera

Uložte kód ako `server.py` a spustite ho z príkazového riadku:

```bash
python server.py
```

Server sa spustí a bude čakať na vstup zo stdin. Komunikuje pomocou JSON-RPC správ cez stdio transport.

### Krok 4: Testovanie pomocou Inspectoru

Server môžete otestovať pomocou MCP Inspector:

1. Nainštalujte Inspector: `npx @modelcontextprotocol/inspector`
2. Spustite Inspector a nasmerujte ho na svoj server
3. Otestujte nástroje, ktoré ste vytvorili

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Ladenie vášho stdio servera

### Použitie MCP Inspectoru

MCP Inspector je cenný nástroj na ladenie a testovanie MCP serverov. Tu je, ako ho používať so svojim stdio serverom:

1. **Inštalácia Inspectoru**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Spustenie Inspectoru**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testovanie servera**: Inspector poskytuje webové rozhranie, kde môžete:
   - Zobraziť schopnosti servera
   - Testovať nástroje s rôznymi parametrami
   - Monitorovať JSON-RPC správy
   - Ladiť problémy s pripojením

### Použitie VS Code

Môžete tiež ladiť MCP server priamo vo VS Code:

1. Vytvorte launch konfiguráciu v `.vscode/launch.json`:
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

2. Nastavte breakpointy vo vašom kóde servera
3. Spustite debugger a testujte s Inspectorom

### Bežné tipy na ladenie

- Používajte `stderr` na logovanie – nikdy nezapisujte na `stdout`, ktorý je vyhradený pre MCP správy
- Uistite sa, že všetky JSON-RPC správy sú oddelené odriadkovaním
- Najskôr testujte jednoduché nástroje pred pridaním zložitejších funkcií
- Používajte Inspector na overenie formátu správ

## Používanie vášho stdio servera vo VS Code

Keď ste vytvorili MCP stdio server, môžete ho integrovať s VS Code, aby ste ho používali s Claude alebo inými MCP-kompatibilnými klientmi.

### Konfigurácia

1. **Vytvorte konfiguračný súbor MCP** v `%APPDATA%\Claude\claude_desktop_config.json` (Windows) alebo `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Reštartujte Claude**: zatvorte a znovu otvorte Claude, aby sa načítala nová konfigurácia servera.

3. **Otestujte pripojenie**: začnite konverzáciu s Claudom a skúste používať nástroje vášho servera:
   - "Môžeš ma pozdraviť pomocou nástroja pozdrav?"
   - "Vypočítaj súčet 15 a 27"
   - "Aká je info o serveri?"

### Príklad TypeScript stdio servera

Tu je kompletný príklad v TypeScripte na referenciu:

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

// Pridať nástroje
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

### Príklad .NET stdio servera

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

## Zhrnutie

V tejto aktualizovanej lekcii ste sa naučili:

- Vytvárať MCP servery pomocou aktuálneho **stdio transportu** (odporúčaný prístup)
- Pochopiť, prečo bol SSE transport zrušený v prospech stdio a Streamable HTTP
- Tvorbu nástrojov, ktoré môžu vyvolať MCP klienti
- Ladenie servera pomocou MCP Inspectoru
- Integráciu vašeho stdio servera s VS Code a Claude

Stdio transport poskytuje jednoduchší, bezpečnejší a výkonnejší spôsob tvorby MCP serverov v porovnaní so zrušeným SSE prístupom. Je odporúčaný pre väčšinu implementácií MCP serverov podľa špecifikácie z 2025-06-18.


### .NET

1. Najprv si vytvoríme nástroje, na to vytvoríme súbor *Tools.cs* s nasledujúcim obsahom:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Cvičenie: Testovanie vášho stdio servera

Teraz, keď ste vytvorili svoj stdio server, otestujeme ho, aby sme sa uistili, že správne funguje.

### Požiadavky

1. Uistite sa, že máte nainštalovaný MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Váš serverový kód by mal byť uložený (napr. ako `server.py`)

### Testovanie pomocou Inspectoru

1. **Spustite Inspector so svojim serverom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorte webové rozhranie**: Inspector otvorí prehliadač, ktorý vám ukáže schopnosti servera.

3. **Testujte nástroje**: 
   - Vyskúšajte nástroj `get_greeting` s rôznymi menami
   - Testujte nástroj `calculate_sum` s rôznymi číslami
   - Zavolajte nástroj `get_server_info` pre zobrazenie metadát servera

4. **Sledujte komunikáciu**: Inspector zobrazuje JSON-RPC správy vymieňané medzi klientom a serverom.

### Čo by ste mali vidieť

Keď sa server správne spustí, mali by ste vidieť:
- Schopnosti servera uvedené v Inspectorovi
- Dostupné nástroje na testovanie
- Úspešné výmeny JSON-RPC správ
- Zobrazené odpovede nástrojov v rozhraní

### Bežné problémy a riešenia

**Server sa nespustí:**
- Skontrolujte, či sú všetky závislosti nainštalované: `pip install mcp`
- Overte syntax Pythonu a odsadenie
- Pozrite si chybové hlásenia v konzole

**Nástroje sa nezobrazujú:**
- Uistite sa, že máte dekorátory `@server.tool()`
- Skontrolujte, či sú nástrojové funkcie definované pred volaním `main()`
- Overte správnu konfiguráciu servera

**Problémy s pripojením:**
- Uistite sa, že server používa správne stdio transport
- Skontrolujte, či vám iné procesy neprekážajú
- Overte syntax príkazu Inspectoru

## Zadanie úlohy

Vyskúšajte rozšíriť svoj server o ďalšie schopnosti. Pozrite si [túto stránku](https://api.chucknorris.io/), kde môžete napríklad pridať nástroj, ktorý volá API. Rozhodnite sa, ako má server vyzerať. Prajeme veľa zábavy :)
## Riešenie

[Riešenie](./solution/README.md) Tu je možné riešenie s funkčným kódom.

## Kľúčové zistenia

Hlavné body z tejto kapitoly sú nasledovné:

- Stdio transport je odporúčaný mechanizmus pre lokálne MCP servery.
- Stdio transport umožňuje hladkú komunikáciu medzi MCP servermi a klientmi pomocou štandardných vstupných a výstupných prúdov.
- Môžete použiť ako Inspector, tak Visual Studio Code na priamu prácu so stdio servermi, čo veľmi uľahčuje ladenie a integráciu.

## Ukážky 

- [Java kalkulačka](../samples/java/calculator/README.md)
- [.Net kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulačka](../samples/javascript/README.md)
- [TypeScript kalkulačka](../samples/typescript/README.md)
- [Python kalkulačka](../../../../03-GettingStarted/samples/python) 

## Ďalšie zdroje

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Čo ďalej

## Ďalšie kroky

Teraz, keď ste sa naučili vytvárať MCP servery so stdio transportom, môžete preskúmať pokročilejšie témy:

- **Ďalej**: [HTTP Streaming s MCP (Streamable HTTP)](../06-http-streaming/README.md) - Naučte sa o ďalšom podporovanom mechanizme transportu pre vzdialené servery
- **Pokročilé**: [Najlepšie bezpečnostné praktiky MCP](../../02-Security/README.md) - Implementujte bezpečnosť vo svojich MCP serveroch
- **Produkcia**: [Stratégie nasadenia](../09-deployment/README.md) - Nasadte svoje servery do produkcie

## Ďalšie zdroje

- [MCP špecifikácia 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Oficiálna špecifikácia
- [MCP SDK dokumentácia](https://github.com/modelcontextprotocol/sdk) - Referencie SDK pre všetky jazyky
- [Príklady od komunity](../../06-CommunityContributions/README.md) - Viac príkladov serverov od komunity

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča odborný ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->