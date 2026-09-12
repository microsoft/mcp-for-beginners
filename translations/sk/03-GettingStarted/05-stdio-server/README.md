# MCP Server so štandardným vstupom a výstupom (stdio) ako transportom

> **⚠️ Dôležitá aktualizácia**: Od špecifikácie MCP 2025-06-18 bol samostatný transport SSE (Server-Sent Events) **zrušený** a nahradený transportom „Streamable HTTP“. Súčasná špecifikácia MCP definuje dva hlavné transportné mechanizmy:
> 1. **stdio** - Štandardný vstup/výstup (odporúčané pre lokálne servery)
> 2. **Streamable HTTP** - Pre vzdialené servery, ktoré môžu používať SSE interne
>
> Táto lekcia bola aktualizovaná a zameriava sa na **stdio transport**, ktorý je odporúčaným prístupom pre väčšinu implementácií MCP serverov.

Transport stdio umožňuje MCP serverom komunikovať s klientmi prostredníctvom štandardných vstupných a výstupných tokov. Je to najčastejšie používaný a odporúčaný transportný mechanizmus v aktuálnej špecifikácii MCP, poskytujúci jednoduchý a efektívny spôsob, ako vytvárať MCP servery, ktoré sa dajú ľahko integrovať s rôznymi klientskymi aplikáciami.

## Prehľad

Táto lekcia pokrýva, ako vytvárať a používať MCP servery so štandardným vstupno-výstupným transportom (stdio).

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Vytvoriť MCP server používajúci stdio transport.
- Ladiť MCP server pomocou Inspectoru.
- Používať MCP server vo Visual Studio Code.
- Pochopiť aktuálne mechanizmy MCP transportu a prečo je stdio odporúčané.


## stdio Transport - Ako funguje

stdio transport je jedným z dvoch štandardných transportov v MCP špecifikácii
`2026-07-28`. Funguje takto:

- **Jednoduchá komunikácia**: Server číta JSON-RPC správy zo štandardného vstupu (`stdin`) a posiela správy na štandardný výstup (`stdout`).
- **Proces založený**: Klient spúšťa MCP server ako podproces.
- **Formát správ**: Správy sú jednotlivé JSON-RPC požiadavky, notifikácie alebo odpovede, oddelené novými riadkami.
- **Logovanie**: Server MÔŽE zapisovať UTF-8 reťazce na štandardný chybový výstup (`stderr`) na účely logovania.

### Kľúčové požiadavky:
- Správy MUSIA byť oddelené novými riadkami a NESMÚ obsahovať vložené nové riadky
- Server NESMIE zapisovať do `stdout` nič, čo nie je platná MCP správa
- Klient NESMIE zapisovať do serverovho `stdin` nič, čo nie je platná MCP správa

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
- Vytvoríme inštanciu servera s základnou konfiguráciou a schopnosťami
- Vytvoríme inštanciu `StdioServerTransport` a pripojíme k nej server, čo umožňuje komunikáciu cez stdin/stdout

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
- Použijeme kontextový manažér stdio_server na riadenie transportu

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

Kľúčový rozdiel oproti SSE je, že stdio servery:

- Nepotrebujú nastavenie webového servera ani HTTP endpointy
- Sú spustené klientom ako podprocesy
- Komunikujú cez stdin/stdout toky
- Sú jednoduchšie na implementáciu a ladenie

## Cvičenie: Vytvorenie stdio servera

Pri tvorbe servera musíme mať na pamäti dve veci:

- Potrebujeme použiť webový server, ktorý sprístupní endpointy pre pripojenie a správy.
## Laboratórium: Vytvorenie jednoduchého MCP stdio servera

V tomto laboratóriu vytvoríme jednoduchý MCP server s odporúčaným stdio transportom. Tento server sprístupní nástroje, ktoré môžu klienti volať pomocou štandardného protokolu Model Context Protocol.

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

## Kľúčové rozdiely oproti zastaranému prístupu SSE

**Stdio Transport (Súčasný štandard):**
- Jednoduchý model podprocesu - klient spúšťa server ako dcérsky proces
- Komunikácia cez stdin/stdout pomocou JSON-RPC správ
- Nie je potrebné nastavovať HTTP server
- Lepší výkon a bezpečnosť
- Jednoduchšie ladenie a vývoj

**SSE Transport (Zrušený od MCP 2025-06-18):**
- Vyžaduje HTTP server so SSE endpointmi
- Zložitejšie nastavenie s webovým serverom
- Dodatočné bezpečnostné opatrenia pre HTTP endpointy
- Teraz nahradený Streamable HTTP pre scenáre webu

### Vytvorenie servera so stdio transportom

Aby sme vytvorili náš stdio server, musíme:

1. **Importovať potrebné knižnice** - potrebujeme komponenty MCP servera a stdio transport
2. **Vytvoriť inštanciu servera** - definovať server so schopnosťami
3. **Definovať nástroje** - pridať funkcionalitu, ktorú chceme sprístupniť
4. **Nastaviť transport** - nakonfigurovať stdio komunikáciu
5. **Spustiť server** - štartovať server a spracovávať správy

Postupujme krok za krokom:

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

Uložte kód ako `server.py` a spustite ho z príkazového riadku:

```bash
python server.py
```

Server sa spustí a bude čakať na vstup zo stdin. Komunikuje pomocou JSON-RPC správ cez stdio transport.

### Krok 4: Testovanie s Inspectorom

Server môžete otestovať použitím MCP Inspector:

1. Nainštalujte Inspector: `npx @modelcontextprotocol/inspector`
2. Spustite Inspector a nasmerujte ho na váš server
3. Otestujte nástroje, ktoré ste vytvorili

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Ladenie vášho stdio servera

### Použitie MCP Inspector

MCP Inspector je hodnotný nástroj na ladenie a testovanie MCP serverov. Tu je postup, ako ho použiť so serverom stdio:

1. **Nainštalujte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Spustite Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testujte váš server**: Inspector poskytuje webové rozhranie, kde môžete:
   - Zobraziť schopnosti servera
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

2. Nastavte breakpointy vo vašom serverovom kóde
3. Spustite debugger a testujte s Inspectorom

### Bežné tipy na ladenie

- Používajte `stderr` pre logovanie - nikdy nezapisujte do `stdout`, lebo je vyhradený pre MCP správy
- Uistite sa, že všetky JSON-RPC správy sú oddelené novým riadkom
- Najskôr testujte jednoduché nástroje pred pridávaním komplexnej funkcionality
- Používajte Inspector na overenie formátov správ

## Používanie vášho stdio servera vo VS Code

Akonáhle ste vytvorili svoj MCP stdio server, môžete ho integrovať do VS Code a používať s Claude alebo inými MCP-kompatibilnými klientmi.

### Konfigurácia

1. **Vytvorte MCP konfiguračný súbor** na `%APPDATA%\Claude\claude_desktop_config.json` (Windows) alebo `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Reštartujte Claude**: Zatvorte a znova otvorte Claude, aby sa načítala nová konfigurácia servera.

3. **Otestujte spojenie**: Začnite konverzáciu s Claude a skúste použiť nástroje vášho servera:
   - "Môžeš ma pozdraviť pomocou nástroja pre pozdravy?"
   - "Vypočítaj súčet 15 a 27"
   - "Aké sú informácie o serveri?"

### Príklad TypeScript stdio servera

Tu je úplný príklad v TypeScript pre referenciu:

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
- Vytvárať nástroje, ktoré môžu volať MCP klienti
- Ladiť server použitím MCP Inspector
- Integrovať váš stdio server s VS Code a Claude

Stdio transport poskytuje jednoduchší, bezpečnejší a výkonnejší spôsob vytvárania MCP serverov v porovnaní so zrušeným SSE prístupom. Je to odporúčaný transport pre väčšinu implementácií MCP serverov podľa špecifikácie z 2025-06-18.


### .NET

1. Najskôr vytvorme niekoľko nástrojov, na toto vytvoríme súbor *Tools.cs* s nasledujúcim obsahom:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Cvičenie: Testovanie vášho stdio servera

Teraz, keď ste vytvorili váš stdio server, otestujeme ho, aby sme sa uistili, že správne funguje.

### Požiadavky

1. Uistite sa, že máte nainštalovaný MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Váš serverový kód by mal byť uložený (napr. ako `server.py`)

### Testovanie s Inspectorom

1. **Spustite Inspector spolu s vaším serverom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorte webové rozhranie**: Inspector otvorí prehliadačové okno zobrazujúce schopnosti vášho servera.

3. **Testujte nástroje**: 
   - Vyskúšajte nástroj `get_greeting` s rôznymi menami
   - Testujte nástroj `calculate_sum` s rôznymi číslami
   - Zavolajte nástroj `get_server_info` na zistenie metadát servera

4. **Sledujte komunikáciu**: Inspector ukazuje JSON-RPC správy vymieňané medzi klientom a serverom.

### Čo by ste mali vidieť

Keď sa váš server spustí správne, mali by ste vidieť:
- Zoznam schopností servera v Inspectorovi
- Dostupné nástroje na testovanie
- Úspešnú výmenu JSON-RPC správ
- Odpovede nástrojov zobrazené v rozhraní

### Bežné problémy a riešenia

**Server nezačne:**
- Skontrolujte, či sú nainštalované všetky závislosti: `pip install mcp`
- Overte syntax a odsadenie Python kódu
- Hľadajte chybové hlásenia v konzole

**Nástroje sa nezobrazujú:**
- Uistite sa, že sú prítomné dekorátory `@server.tool()`
- Skontrolujte, či sú funkcie nástrojov definované pred `main()`
- Overte správnu konfiguráciu servera

**Problémy s pripojením:**
- Skontrolujte správne použitie stdio transportu
- Uistite sa, že iné procesy nezasahujú do komunikácie
- Overte syntax príkazu pre Inspector

## Zadanie

Pokúste sa rozšíriť svoj server o ďalšie funkčnosti. Pozrite si [túto stránku](https://api.chucknorris.io/) napríklad na pridanie nástroja volajúceho nejaké API. Vy rozhodnite, ako bude server vyzerať. Bavte sa :)
## Riešenie

[Riešenie](./solution/README.md) Tu je možné riešenie s funkčným kódom.

## Kľúčové poznatky

Hlavné poznatky z tohto kapitoly sú:

- stdio transport je odporúčaný mechanizmus pre lokálne MCP servery.
- Stdio transport umožňuje plynulú komunikáciu medzi MCP servermi a klientmi pomocou štandardných vstupných a výstupných tokov.
- Môžete použiť Inspector aj Visual Studio Code na priame používanie stdio serverov, čo uľahčuje ladenie a integráciu.

## Ukážky 

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python) 

## Dodatočné zdroje

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Čo ďalej

## Ďalšie kroky

Teraz, keď ste sa naučili vytvárať MCP servery so stdio transportom, môžete preskúmať pokročilejšie témy:

- **Ďalej**: [HTTP Streaming s MCP (Streamable HTTP)](../06-http-streaming/README.md) - Naučte sa o druhom podporovanom transportnom mechanizme pre vzdialené servery
- **Pokročilé**: [Najlepšie bezpečnostné postupy MCP](../../02-Security/README.md) - Implementujte bezpečnosť vo vašich MCP serveroch
- **Produkcia**: [Stratégie nasadenia](../09-deployment/README.md) - Nasadte vaše servery pre produkčné použitie

## Dodatočné zdroje

- [MCP Špecifikácia 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Aktuálna špecifikácia
- [MCP SDK Dokumentácia](https://github.com/modelcontextprotocol/sdk) - Dokumentácia SDK pre všetky jazyky
- [Príklady komunity](../../06-CommunityContributions/README.md) - Viac príkladov serverov od komunity

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->