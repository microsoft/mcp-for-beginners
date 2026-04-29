# MCP server stdio transpordiga

> **⚠️ Tähtis uuendus**: MCP spetsifikatsiooni 2025-06-18 seisuga on eraldiseisev SSE (Server-Sent Events) transport **ära kaotatud** ning asendatud "Streamable HTTP" transpordiga. Praegune MCP spetsifikatsioon määratleb kaks peamist transpordimehhanismi:
> 1. **stdio** - Standard sisend/väljund (soovitatav kohalikele serveritele)
> 2. **Streamable HTTP** - kaugsuhtlus, mis võib sisemiselt kasutada SSE-d
>
> See õppetund keskendub uuendatult **stdio transpordile**, mis on enamiku MCP serveri rakenduste jaoks soovitatav.

Stdio transport võimaldab MCP serveritel suhelda klientidega standardse sisendi ja väljundi voogude kaudu. See on praeguse MCP spetsifikatsiooni kõige enamkasutatavam ja soovitatav transpordimehhanism, mis pakub lihtsat ja tõhusat viisi MCP serverite loomiseks ning võimaldab hõlpsat integreerimist erinevate kliendirakendustega.

## Ülevaade

See õppetund käsitleb, kuidas luua ja kasutada MCP servereid stdio transpordi abil.

## Õpieesmärgid

Selle õppetunni lõpuks oskad sa:

- Luua MCP serveri stdio transpordi abil.
- Siluda MCP serverit Inspectoriga.
- Kasutada MCP serverit Visual Studio Code'is.
- Mõista MCP transpordimehhanisme ning miks stdio on soovitatav.

## stdio transport - kuidas see töötab

Stdio transport on üks kahest toetatud transporditüübist praeguses MCP spetsifikatsioonis (2025-06-18). See töötab järgmiselt:

- **Lihtne suhtlus**: server loeb JSON-RPC sõnumeid standard sisendist (`stdin`) ja saadab sõnumeid standard väljundisse (`stdout`).
- **Protsessipõhine**: klient käivitab MCP serveri alamprotsessina.
- **Sõnumite formaat**: sõnumid on eraldiseisvad JSON-RPC päringud, teated või vastused, mis on eraldatud reavahetustega.
- **Logimine**: server VÕIB kirjutada logimiseks UTF-8 stringe standardveasse (`stderr`).

### Peamised nõuded:
- Sõnumeid TULEB eraldada reavahetustega ja nende sees EI TOHI olla manustatud reavahetusi
- Server EI TOHI kirjutada `stdout`-i mitte kehtivaid MCP sõnumeid
- Klient EI TOHI kirjutada serveri `stdin`-i mitte kehtivaid MCP sõnumeid

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

Eelnevas koodis:

- Impordime MCP SDK-st klassi `Server` ja transpordi `StdioServerTransport`
- Loome serveri eksemplari baaskonfiguratsiooni ja võimetega
- Loome `StdioServerTransport` eksemplari ning ühendame serveri sellega, võimaldades suhtlust stdin/stdout kaudu

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Loo serveri eksemplar
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

Eelnevas koodis:

- Loome MCP SDK abil serveri instantsi
- Määratleme tööriistad dekoratsioonide abil
- Kasutame stdio_server kontekstihaldurit transpordi haldamiseks

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

Peamine erinevus SSE-st seisneb selles, et stdio serverid:

- Ei vaja veebiserveri seadistust ega HTTP otspunktide loomiseks
- Käivitatakse kliendi poolt alamprotsessina
- Suhtlevad stdin/stdout voogude kaudu
- On lihtsamad rakendada ja siluda

## Harjutus: stdio serveri loomine

Serveri loomiseks tuleb pidada silmas kahte asja:

- Me vajame veebiserverit ühenduse ja sõnumite otspunktide eksponeerimiseks.
## Labor: Lihtsa MCP stdio serveri loomine

Selles laboris loome lihtsa MCP serveri, kasutades soovitatavat stdio transporti. See server eksponeerib tööriistu, mida kliendid saavad kutsuda standardse Model Context Protocoli kaudu.

### Eeltingimused

- Python 3.8 või uuem
- MCP Pythoni SDK: `pip install mcp`
- Baasteadmised asünkroonsest programmeerimisest

Alustame esimese MCP stdio serveri loomisega:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigureeri logimine
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loo server
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
    # Kasuta stdio transporti
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Peamised erinevused SSE (ära antud) lähenemisest

**Stdio transport (praegune standard):**
- Lihtne alamprotsessi mudel - klient käivitab serveri alamprotsessina
- Suhtlus stdin/stdout kaudu JSON-RPC sõnumitega
- HTTP serverit ei ole vaja seadistada
- Parem jõudlus ja turvalisus
- Lihtsam siluda ja arendada

**SSE transport (ära antud MCP 2025-06-18 seisuga):**
- Nõudis HTTP serverit SSE otspunktidega
- Keerulisem seadistamine veebiserveri infrastruktuuriga
- Täiendavad turvaküsimused HTTP otspunktide juures
- Asendatud Streamable HTTP-ga veebipõhiste stsenaariumite jaoks

### stdio transpordiga serveri loomine

Serveri loomiseks peame:

1. **Impordima vajalikud teegid** - MCP serveri komponendid ja stdio transport
2. **Looma serveri instantsi** - määratlema server koos võimetega
3. **Määratlema tööriistad** - lisama funktsionaalsust, mida eksponeerida
4. **Seadistama transpordi** - konfigureerima stdio suhtlust
5. **Käivita server** - alustama serverit ja töötlema sõnumeid

Ehitage see samm-sammult:

### Samm 1: Loome baasilise stdio serveri

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigureeri logimine
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loo server
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

### Samm 2: Lisame rohkem tööriistu

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

### Samm 3: Serveri käivitamine

Salvesta kood failina `server.py` ja käivita see käsurealt:

```bash
python server.py
```

Server käivitub ja ootab sisendit stdin-st. Suhtleb JSON-RPC sõnumitega stdio transpordi kaudu.

### Samm 4: Testimine Inspectoriga

Serverit saad testida MCP Inspectoriga:

1. Paigalda Inspector: `npx @modelcontextprotocol/inspector`
2. Käivita Inspector ja suuna see oma serverile
3. Testi loodud tööriistu

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## oma stdio serveri silumine

### MCP Inspectoriga

MCP Inspector on väärtuslik vahend MCP serverite silumiseks ja testimiseks. Nii saad seda kasutada stdio serveriga:

1. **Paigalda Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käivita Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testi oma serverit**: Inspector pakub veebiliidest, kus saad:
   - Vaadata serveri võimeid
   - Testida tööriistu erinevate parameetritega
   - Jälgida JSON-RPC sõnumeid
   - Siluda ühenduvusprobleeme

### Kasutades VS Code

VS Code'is saad oma MCP serverit samuti otse siluda:

1. Loo `.vscode/launch.json` käivituskonfiguratsioon:
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

2. Määra murdepunkte serveri koodi
3. Käivita silur ja testi Inspectoriga

### Sageli kasulikud silumishoiatused

- Kasuta logimiseks `stderr`-i - ära kirjuta kunagi `stdout`-i, kuna see on reserveeritud MCP sõnumitele
- Veendu, et kõik JSON-RPC sõnumid oleksid reavahetusega eraldatud
- Testi esmalt lihtsate tööriistadega enne keerukamate lisamist
- Kontrolli sõnumiformaate Inspectoriga

## stdio serveri kasutamine VS Code'is

Kui oled MCP stdio serveri valmis teinud, saad selle integreerida VS Code’i, et kasutada seda koos Claude'i või muud MCP ühilduva kliendiga.

### Konfiguratsioon

1. **Loo MCP konfiguratsioonifail** asukohas `%APPDATA%\Claude\claude_desktop_config.json` (Windows) või `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Taaskäivita Claude**: Sule ja ava Claude uuesti, et laadida uus serveri konfiguratsioon.

3. **Testi ühendust**: Alusta vestlust Claude'iga ja proovi serveri tööriistu:
   - "Kas saaksid tervitada mind tervitustööriista abil?"
   - "Arvuta 15 ja 27 summa"
   - "Mis info sul serveri kohta on?"

### TypeScript stdio serveri näide

Siin on viitamiseks täielik TypeScript näidis:

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

// Lisa tööriistad
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

### .NET stdio serveri näide

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

## Kokkuvõte

Selles uuendatud õppetunnis õppisid sa:

- MCP serverite loomist kasutades praegust **stdio transporti** (soovitatav lahendus)
- Mõistma miks SSE transport kaotati ja miks üle mindi stdio ja Streamable HTTP peale
- Tööriistade loomist, mida MCP kliendid saavad kutsuda
- Oma serveri silumist MCP Inspectoriga
- oma stdio serveri integreerimist VS Code'i ja Claude'iga

Stdio transport pakub lihtsamat, turvalisemat ja jõudluslikult paremat viisi MCP serverite loomiseks võrreldes kadunud SSE lähenemisega. See on soovitatav transport enamikele MCP serveri rakendustele alates 2025-06-18 spetsifikatsioonist.


### .NET

1. Alustame tööriistade loomisega, selleks loome faili *Tools.cs* järgmise sisuga:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjutus: oma stdio serveri testimine

Nüüd, kui oled oma stdio serveri valmis teinud, testime seda, et veenduda selle korrektsuses.

### Eeltingimused

1. Veendu, et MCP Inspector on paigaldatud:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Serveri kood peaks olema salvestatud (näiteks failina `server.py`)

### Testimine Inspectoriga

1. **Käivita Inspector koos oma serveriga**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ava veebiliides**: Inspector avab brauseriakna, kus kuvatakse serveri võimed.

3. **Testi tööriistu**: 
   - Proovi tööriista `get_greeting` erinevate nimedega
   - Testi tööriista `calculate_sum` erinevate arvudega
   - Kutsu `get_server_info` tööriista serveri metaandmete saamiseks

4. **Jälgi suhtlust**: Inspector kuvab klientide ja serveri vahel vahetatavaid JSON-RPC sõnumeid.

### Mida peaksid nägema

Kui server käivitub korrektselt, peaksid nägema:
- Serveri võimekirja Inspectoris
- Testimiseks saadaolevaid tööriistu
- Edukaid JSON-RPC sõnumite vahetusi
- Tööriistade vastuseid liideses

### Levinud probleemid ja lahendused

**Server ei käivitu:**
- Kontrolli, et kõik sõltuvused on paigaldatud: `pip install mcp`
- Kontrolli Pythoni süntaksit ja taandarveid
- Otsi konsoolist veateateid

**Tööriistad ei ilmu:**
- Veendu, et `@server.tool()` dekoratsioonid on olemas
- Kontrolli, et tööriistafunktsioonid on defineeritud enne `main()` funktsiooni
- Veendu, et server on korrektselt seadistatud

**Ühendusprobleemid:**
- Veendu, et server kasutab stdio transporti korrektselt
- Kontrolli, et teised protsessid ei sega
- Kontrolli Inspector'i käsu süntaksit

## Ülesanne

Proovi lisada oma serverile rohkem võimeid. Vaata [seda lehte](https://api.chucknorris.io/), et näiteks lisada tööriist, mis kutsub API-d. Sa otsustad, milline server peaks välja nägema. Head katsetamist :)
## Lahendus

[Lahendus](./solution/README.md) Siin on võimalik lahendus töötava koodiga.

## Olulised võtmedõppetunnid

Selle peatüki võtmemõtted on järgmised:

- Stdio transport on soovitatav mehhanism kohalikele MCP serveritele.
- Stdio transport võimaldab sujuvat suhtlust MCP serverite ja klientide vahel, kasutades standard sisendi ja väljundi vooge.
- Saad kasutada nii Inspectorit kui ka Visual Studio Code'i stdio serverite otseks kasutamiseks, muutes silumise ja integreerimise lihtsaks.

## Näited 

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python) 

## Täiendavad ressursid

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mis järgmiseks

## Järgmised sammud

Nüüd, kui sa tead, kuidas luua MCP servereid stdio transpordiga, võid uurida edasijõudnumaid teemasid:

- **Edasi**: [HTTP voogesitus MCP-ga (Streamable HTTP)](../06-http-streaming/README.md) - Õpi teise toetatud transpordimehhanismi kohta kaugsuhtluseks
- **Edasijõudnutele**: [MCP turvapraktikad](../../02-Security/README.md) - Rakenda turvalisust MCP serverites
- **Tootmisse**: [Deploy strateegiad](../09-deployment/README.md) - Serverite tootmiskeskkonda paigaldamine

## Täiendavad ressursid

- [MCP spetsifikatsioon 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Ametlik spetsifikatsioon
- [MCP SDK dokumentatsioon](https://github.com/modelcontextprotocol/sdk) - SDK viited kõigi keelte jaoks
- [Kogukonna näited](../../06-CommunityContributions/README.md) - Rohkem serverite näiteid kogukonnalt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame täpsust, palun olge teadlik, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada ametlikuks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tekkivate arusaamatuste või väär tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->