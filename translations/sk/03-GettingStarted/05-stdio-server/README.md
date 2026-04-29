# MCP Server so stdio transportom

> **⚠️ Dôležitá aktualizácia**: Od špecifikácie MCP 2025-06-18 je samostatný SSE (Server-Sent Events) transport **zrušený** a nahradený transportom "Streamable HTTP". Súčasná špecifikácia MCP definuje dva hlavné mechanizmy transportu:
> 1. **stdio** - Štandardný vstup/výstup (odporúčaný pre lokálne servery)
> 2. **Streamable HTTP** - Pre vzdialené servery, ktoré môžu interne používať SSE
>
> Tento kurz bol aktualizovaný tak, aby sa zameral na **stdio transport**, ktorý je odporúčaný prístup pre väčšinu implementácií MCP serverov.

Štandardný vstup/výstup (stdio) transport umožňuje MCP serverom komunikovať s klientmi cez štandardné vstupné a výstupné prúdy. Je to najpoužívanejší a odporúčaný transportný mechanizmus v súčasnej špecifikácii MCP a poskytuje jednoduchý a efektívny spôsob, ako budovať MCP servery, ktoré je možné ľahko integrovať s rôznymi aplikačnými klientmi.

## Prehľad

Tento kurz pokrýva, ako vytvoriť a používať MCP servery pomocou stdio transportu.

## Ciele učenia

Na konci tohto kurzu budete schopní:

- Vytvoriť MCP server pomocou stdio transportu.
- Ladiť MCP server pomocou Inspektora.
- Používať MCP server cez Visual Studio Code.
- Pochopiť súčasné transportné mechanizmy MCP a prečo je odporúčaný stdio transport.


## stdio Transport - Ako to funguje

stdio transport je jeden z dvoch podporovaných typov transportu v aktuálnej špecifikácii MCP (2025-06-18). Tu je jeho fungovanie:

- **Jednoduchá komunikácia**: Server číta JSON-RPC správy zo štandardného vstupu (`stdin`) a posiela správy na štandardný výstup (`stdout`).
- **Procesový model**: Klient spustí MCP server ako podproces.
- **Formát správ**: Správy sú samostatné JSON-RPC požiadavky, notifikácie alebo odpovede, oddelené novými riadkami.
- **Logovanie**: Server MÔŽE zapisovať UTF-8 reťazce do štandardnej chyby (`stderr`) na účely logovania.

### Kľúčové požiadavky:
- Správy MUSIA byť oddelené novými riadkami a NESMÚ obsahovať vložené nové riadky
- Server NESMIE nič zapisovať na `stdout`, čo nie je platná MCP správa
- Klient NESMIE zapisovať na serverov `stdin` nič, čo nie je platná MCP správa

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

V predchádzajúcom kóde:

- Importujeme triedu `Server` a `StdioServerTransport` z MCP SDK
- Vytvárame inštanciu servera s základnou konfiguráciou a schopnosťami
- Vytvárame inštanciu `StdioServerTransport` a pripájame server na ňu, čím umožňujeme komunikáciu cez stdin/stdout

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

- Vytvárame inštanciu servera pomocou MCP SDK
- Definujeme nástroje pomocou dekorátorov
- Používame kontextový manažér stdio_server na riadenie transportu

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

Hlavný rozdiel oproti SSE je v tom, že stdio servery:

- Nepotrebujú nastavenie webového servera alebo HTTP endpointov
- Sú spustené klientom ako podprocesy
- Komunikujú cez stdin/stdout prúdy
- Sú jednoduchšie na implementáciu a ladenie

## Cvičenie: Vytvorenie stdio servera

Pri tvorbe nášho servera musíme mať na pamäti dve veci:

- Potrebujeme použiť webový server na sprístupnenie endpointov pre spojenie a správy.
## Laboratórium: Vytvorenie jednoduchého MCP stdio servera

V tomto laboratóriu vytvoríme jednoduchý MCP server používajúci odporúčaný stdio transport. Tento server sprístupní nástroje, ktoré môžu klienti volať pomocou štandardného Model Context Protocol.

### Predpoklady

- Python 3.8 alebo novší
- MCP Python SDK: `pip install mcp`
- Základné znalosti asynchrónneho programovania

Začnime vytváraním nášho prvého MCP stdio servera:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Nakonfigurujte protokolovanie
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

## Kľúčové rozdiely oproti deprecated prístupu SSE

**Stdio transport (súčasný štandard):**
- Jednoduchý model podprocesu - klient spúšťa server ako dcérsky proces
- Komunikácia cez stdin/stdout pomocou JSON-RPC správ
- Nie je potrebné nastavovanie HTTP servera
- Lepší výkon a bezpečnosť
- Jednoduchšie ladenie a vývoj

**SSE transport (deprecated od MCP 2025-06-18):**
- Vyžadoval HTTP server s SSE endpointmi
- Zložitejšie nastavenie s webovým serverom
- Ďalšie bezpečnostné opatrenia pre HTTP endpointy
- Teraz nahradený Streamable HTTP pre webové scenáre

### Vytvorenie servera so stdio transportom

Aby sme vytvorili náš stdio server, musíme:

1. **Importovať potrebné knižnice** - Potrebujeme komponenty MCP servera a stdio transport
2. **Vytvoriť inštanciu servera** - Definovať server s jeho schopnosťami
3. **Definovať nástroje** - Pridať funkcie, ktoré chceme sprístupniť
4. **Nastaviť transport** - Konfigurovať stdio komunikáciu
5. **Spustiť server** - Spustiť server a spracovávať správy

Postupujme krok za krokom:

### Krok 1: Vytvorenie základného stdio servera

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Nakonfigurujte protokolovanie
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

### Krok 2: Pridanie ďalších nástrojov

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

Uložte kód ako `server.py` a spustite ho z príkazovej riadky:

```bash
python server.py
```

Server sa spustí a bude čakať na vstup zo stdin. Komunikuje pomocou JSON-RPC správ cez stdio transport.

### Krok 4: Testovanie pomocou Inspektora

Server môžete testovať pomocou MCP Inspektora:

1. Nainštalujte Inspektora: `npx @modelcontextprotocol/inspector`
2. Spustite Inspektora a nasmerujte ho na váš server
3. Otestujte nástroje, ktoré ste vytvorili

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Ladenie vášho stdio servera

### Použitie MCP Inspektora

MCP Inspektor je užitočný nástroj na ladenie a testovanie MCP serverov. Tu je, ako ho použiť so vaším stdio serverom:

1. **Inštalácia Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Spustenie Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testovanie servera**: Inspektor poskytuje webové rozhranie, kde môžete:
   - Prezerať schopnosti servera
   - Testovať nástroje s rôznymi parametrami
   - Monitorovať JSON-RPC správy
   - Ladiť problémy s pripojením

### Použitie VS Code

Môžete tiež ladiť váš MCP server priamo vo VS Code:

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

2. Nastavte breakpointy v kóde servera
3. Spustite debugger a testujte pomocou Inspektora

### Bežné tipy na ladenie

- Používajte `stderr` pre logovanie - nikdy nezapisujte do `stdout`, ktorý je vyhradený pre MCP správy
- Zabezpečte, že všetky JSON-RPC správy sú oddelené novými riadkami
- Najskôr testujte jednoduché nástroje pred pridávaním zložitej funkcionality
- Používajte Inspektora na overenie formátu správ

## Použitie vášho stdio servera vo VS Code

Keď ste vytvorili svoj MCP stdio server, môžete ho integrovať do VS Code a používať s Claude alebo inými MCP kompatibilnými klientmi.

### Konfigurácia

1. **Vytvorte konfiguračný súbor MCP** na `%APPDATA%\Claude\claude_desktop_config.json` (Windows) alebo `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Reštartujte Claude**: Zavrite a znova otvorte Claude, aby sa načítala nová konfigurácia servera.

3. **Otestujte pripojenie**: Začnite konverzáciu s Claudom a vyskúšajte nástroje vášho servera:
   - "Môžeš ma pozdraviť pomocou nástroja greeting?"
   - "Vypočítaj súčet 15 a 27"
   - "Aké sú informácie o servery?"

### Príklad TypeScript stdio servera

Tu je kompletný príklad v TypeScript pre referenciu:

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

V tomto aktualizovanom kurze ste sa naučili:

- Vytvárať MCP servery pomocou súčasného **stdio transportu** (odporúčaný prístup)
- Pochopiť, prečo bol SSE transport zrušený v prospech stdio a Streamable HTTP
- Vytvárať nástroje, ktoré môžu byť volané MCP klientmi
- Ladiť váš server pomocou MCP Inspektora
- Integrovať váš stdio server so VS Code a Claude

stdio transport poskytuje jednoduchší, bezpečnejší a výkonnejší spôsob vytvárania MCP serverov v porovnaní s deprecated SSE prístupom. Je to odporúčaný transport pre väčšinu implementácií MCP serverov podľa špecifikácie z 2025-06-18.


### .NET

1. Najskôr si vytvorme nejaké nástroje, na to vytvoríme súbor *Tools.cs* s nasledujúcim obsahom:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Cvičenie: Testovanie vášho stdio servera

Teraz keď ste vytvorili váš stdio server, poďme ho otestovať, aby sme sa uistili, že funguje správne.

### Predpoklady

1. Uistite sa, že máte nainštalovaný MCP Inspektor:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Váš kód servera je uložený (napr. ako `server.py`)

### Testovanie pomocou Inspektora

1. **Spustite Inspektora s vaším serverom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorte webové rozhranie**: Inspektor otvorí prehliadač s rozhraním zobrazujúcim schopnosti vášho servera.

3. **Testujte nástroje**: 
   - Vyskúšajte nástroj `get_greeting` s rôznymi menami
   - Otestujte nástroj `calculate_sum` s rôznymi číslami
   - Zavolajte nástroj `get_server_info` a pozrite si metadáta servera

4. **Monitorujte komunikáciu**: Inspektor zobrazuje JSON-RPC správy vymieňané medzi klientom a serverom.

### Čo by ste mali vidieť

Keď sa server správne spustí, mali by ste vidieť:
- Schopnosti servera zobrazené v Inspektore
- Dostupné nástroje na testovanie
- Úspešné výmeny JSON-RPC správ
- Odpovede nástrojov zobrazené v rozhraní

### Bežné problémy a riešenia

**Server sa nespustí:**
- Skontrolujte, či sú nainštalované všetky závislosti: `pip install mcp`
- Overte syntax a odsadenie v Pythone
- Sledujte chybové hlásenia v konzole

**Nástroje sa nezobrazujú:**
- Uistite sa, že dekorátory `@server.tool()` sú prítomné
- Skontrolujte, či sú funkcie nástrojov definované pred `main()`
- Overte správnu konfiguráciu servera

**Problémy s pripojením:**
- Uistite sa, že server používa správne stdio transport
- Skontrolujte, či žiadne iné procesy nezasahujú
- Overte správnosť príkazu Inspektora

## Zadanie

Skúste rozšíriť svoj server o viac schopností. Pozrite si [túto stránku](https://api.chucknorris.io/), kde môžete napríklad pridať nástroj, ktorý volá API. Vy rozhodnete, ako bude server vyzerať. Prajeme veľa zábavy :)
## Riešenie

[Riešenie](./solution/README.md) Tu je možné riešenie s funkčným kódom.

## Kľúčové poznatky

Hlavné poznatky z tejto kapitoly sú:

- stdio transport je odporúčaný mechanizmus pre lokálne MCP servery.
- stdio transport umožňuje plynulú komunikáciu medzi MCP servermi a klientmi cez štandardné vstupné a výstupné prúdy.
- Môžete použiť Inspektora aj Visual Studio Code na priame používanie stdio serverov, čo uľahčuje ladenie a integráciu.

## Ukážky

- [Java kalkulačka](../samples/java/calculator/README.md)
- [.Net kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulačka](../samples/javascript/README.md)
- [TypeScript kalkulačka](../samples/typescript/README.md)
- [Python kalkulačka](../../../../03-GettingStarted/samples/python) 

## Dodatočné zdroje

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Čo ďalej

## Ďalšie kroky

Keď ste sa naučili vytvárať MCP servery so stdio transportom, môžete preskúmať pokročilejšie témy:

- **Ďalej**: [HTTP streamovanie s MCP (Streamable HTTP)](../06-http-streaming/README.md) - Spoznajte ďalší podporovaný transport pre vzdialené servery
- **Pokročilé**: [Najlepšie bezpečnostné praktiky MCP](../../02-Security/README.md) - Implementujte bezpečnosť vo vašich MCP serveroch
- **Produkcia**: [Stratégie nasadenia](../09-deployment/README.md) - Nasadzujte svoje servery do produkcie

## Dodatočné zdroje

- [Špecifikácia MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Oficiálna špecifikácia
- [Dokumentácia MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referencie SDK pre všetky jazyky
- [Príklady komunity](../../06-CommunityContributions/README.md) - Viac príkladov serverov od komunity

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pri kritických informáciách sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->