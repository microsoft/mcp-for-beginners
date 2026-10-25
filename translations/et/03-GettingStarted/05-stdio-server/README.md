# MCP-server stdio-transportiga

> **⚠️ Tähtis uuendus**: Alates MCP spetsifikatsioonist 2025-06-18 on eraldiseisev SSE (Server-Sent Events) transport olnud **hülgatud** ja asendatud "Streamable HTTP" transpordiga. Praegune MCP spetsifikatsioon määratleb kaks peamist transpordimehhanismi:
> 1. **stdio** - Standardne sisend/väljund (soovitatav lokaalsetele serveritele)
> 2. **Streamable HTTP** - Kaugserveritele, mis võivad sisemiselt kasutada SSE-d
>
> See õppetund on uuendatud, keskendudes **stdio-transpordile**, mis on soovitatav lähenemine enamikule MCP-serverite kasutusjuhtudest.

Stdio-transport võimaldab MCP-serveritel suhelda klientidega läbi standardsete sisendi- ja väljundivoogude. See on praeguses MCP spetsifikatsioonis enim kasutatav ja soovitatud transpordimehhanism, pakkudes lihtsat ja efektiivset viisi MCP-serverite ehitamiseks, mida on lihtne integreerida erinevate kliendirakendustega.

## Ülevaade

See õppetund käsitleb, kuidas ehitada ja tarbida MCP-servereid, kasutades stdio-transporti.

## Õpieesmärgid

Selle õppetunni lõpuks suudate:

- Ehitada MCP-serveri, kasutades stdio-transporti.
- Siluda MCP-serverit, kasutades Inspectorit.
- Kasutada MCP-serverit Visual Studio Code'i abil.
- Mõista praeguseid MCP-transpordimehhanisme ja miks stdio on soovitatav.


## stdio-transport - kuidas see töötab

Stdio-transport on üks kahest standardtranspordist MCP spetsifikatsioonis
`2026-07-28`. Siin on, kuidas see töötab:

- **Lihtne suhtlus**: Server loeb JSON-RPC sõnumeid standardsisendist (`stdin`) ja saadab sõnumeid standardväljundisse (`stdout`).
- **Protsessipõhine**: Klient käivitab MCP-serveri alamprotsessina.
- **Sõnumi formaat**: Sõnumid on eraldiseisvad JSON-RPC päringud, teavitused või vastused, mis on eraldatud reavahetustega.
- **Logimine**: Server VÕIB kirjutada UTF-8 stringe standardveale (`stderr`) logimise eesmärgil.

### Peamised nõuded:
- Sõnumid PEAVAD olema reavahetustega eraldatud ja EI TOHI sisaldada manustatud reavahetusi
- Server EI TOHI kirjutada midagi `stdout`, mis ei ole kehtiv MCP-sõnum
- Klient EI TOHI kirjutada serveri `stdin` midagi, mis ei ole kehtiv MCP-sõnum

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

- Impordime klassi `Server` ja `StdioServerTransport` MCP SDK-st
- Loome serveri instantsi põhilise konfiguratsiooni ja võimekustega
- Loome `StdioServerTransport` instantsi ja ühendame serveri sellega, võimaldades suhtlust üle stdin/stdout

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

Eelnevas koodis me:

- Loome serveri instantsi, kasutades MCP SDK-d
- Määratleme tööriistad, kasutades dekoraatoreid
- Kasutame stdio_server kontekstihaldurit transpordi käsitlemiseks

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

Peamine erinevus SSE-st on see, et stdio-serverid:

- Ei nõua veebiserveri seadistust ega HTTP-endpointe
- Käivitatakse kliendi poolt alamprotsessidena
- Suhtlevad läbi stdin/stdout-voogude
- On lihtsamad rakendada ja siluda

## Harjutus: stdio-serveri loomine

Serveri loomiseks peame meeles pidama kahte asja:

- Peame kasutama veebiserverit, et avaldada ühenduse ja sõnumite jaoks lõpp-punktid.
## Labor: Lihtsa MCP stdio-serveri loomine

Selles laboris loome lihtsa MCP-serveri, kasutades soovitatud stdio-transporti. See server avaldab tööriistad, mida kliendid saavad kutsuda, kasutades standardset Model Context Protocol'i.

### Eeltingimused

- Python 3.8 või uuem
- MCP Python SDK: `pip install mcp`
- Põhiline arusaam asünkroonsest programmeerimisest

Alustame oma esimese MCP stdio-serveri loomisega:

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

## Põhilised erinevused hülgatud SSE-lähenemisest

**Stdio-transport (praegune standard):**
- Lihtne alamprotsessi mudel - klient käivitab serveri alamprotsessina
- Suhtlus läbi stdin/stdout, kasutades JSON-RPC sõnumeid
- HTTP-serveri seadistust ei nõuta
- Pakub paremat jõudlust ja turvalisust
- Lihtsam silumine ja arendamine

**SSE-transport (hülgatud alates MCP 2025-06-18):**
- Nõudis HTTP-serverit koos SSE-lõpp-punktidega
- Keerulisem seadistus veebiserveri infrastruktuuriga
- Täiendavad turvaküsimused HTTP-lõpp-punktide puhul
- Nüüd asendatud Streamable HTTP-ga veebipõhiste stsenaariumide jaoks

### Serveri loomine stdio-transpordiga

Stdio-serveri loomiseks peame:

1. **Impordi vajalikud teegid** - Vajame MCP-serveri komponente ja stdio-transporti
2. **Loo serveri instants** - Määra server selle võimekustega
3. **Määra tööriistad** - Lisa funktsionaalsus, mida soovime avaldada
4. **Sea üles transport** - Konfigureeri stdio-sidet
5. **Käivita server** - Käivita server ja käsitle sõnumeid

Teeme seda samm-sammult:

### Samm 1: Loo lihtne stdio-server

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

### Samm 2: Lisa rohkem tööriistu

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

Server käivitub ja ootab sisendit stdin-ilt. See suhtleb, kasutades JSON-RPC sõnumeid stdio-transpordi kaudu.

### Samm 4: Testimine Inspectoriga

Saad testida oma serverit, kasutades MCP Inspectorit:

1. Paigalda Inspector: `npx @modelcontextprotocol/inspector`
2. Käivita Inspector ja suuna see sinu serveri poole
3. Testi loodud tööriistu

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Sinu stdio-serveri silumine

### MCP Inspectori kasutamine

MCP Inspector on väärtuslik tööriist MCP-serverite silumiseks ja testimiseks. Siin on, kuidas seda kasutada koos sinu stdio-serveriga:

1. **Paigalda Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käivita Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testi oma serverit**: Inspector pakub veebi-liidest, kus saad:
   - Vaadata serveri võimeid
   - Testida tööriistu erinevate parameetritega
   - Jälgida JSON-RPC sõnumeid
   - Siluda ühenduse probleeme

### VS Code'i kasutamine

Sa saad samuti siluda oma MCP-serverit otse VS Code'is:

1. Loo käivituskonfiguratsioon failis `.vscode/launch.json`:
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

2. Sea katkestuspunkte oma serverikoodis
3. Käivita silur ja testi Inspectoriga

### Levinumad silumisnipid

- Kasuta `stderr` logimiseks - ära kunagi kirjuta `stdout`, kuna see on reserveeritud MCP-sõnumitele
- Veendu, et kõik JSON-RPC sõnumid on reavahetustega eraldatud
- Testi esmalt lihtsate tööriistadega enne keeruka funktsionaalsuse lisamist
- Kasuta Inspectorit sõnumite formaatide kontrollimiseks

## Sinu stdio-serveri kasutamine VS Code'is

Pärast MCP stdio-serveri ülesehitamist saad selle integreerida VS Code'iga, et kasutada seda Claude'i või teiste MCP-ühilduvate klientidega.

### Konfiguratsioon

1. **Loo MCP konfiguratsioonifail** aadressil `%APPDATA%\Claude\claude_desktop_config.json` (Windows) või `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Taaskäivita Claude**: Sule Claude ja ava see uuesti, et laadida uus serverikonfiguratsioon.

3. **Testi ühendust**: Alusta vestlust Claude'iga ja proovi kasutada oma serveri tööriistu:
   - "Kas sa saad mind tervitada, kasutades tervitustööriista?"
   - "Arvuta 15 ja 27 summa"
   - "Mis on serveri info?"

### TypeScript stdio-serveri näide

Siin on täielik TypeScripti näide viitamiseks:

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

### .NET stdio-serveri näide

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

Selles uuendatud õppetükis õppisite, kuidas:

- Ehitada MCP-servereid, kasutades praegust **stdio-transporti** (soovitatav lähenemine)
- Mõista, miks SSE-transport hülgati ja asendati stdio ning Streamable HTTP-ga
- Loo tööriistu, mida MCP-kliendid saavad kutsuda
- Siluda oma serverit, kasutades MCP Inspectorit
- Integreerida oma stdio-server VS Code'iga ja Claude'iga

Stdio-transport pakub lihtsamat, turvalisemat ja parema jõudlusega viisi MCP-serverite ehitamiseks võrreldes hülgatud SSE-lähenemisega. See on soovitatud transport enamikule MCP-serveri rakendustele alates 2025-06-18 spetsifikatsioonist.


### .NET

1. Loome kõigepealt mõned tööriistad; selleks loome faili *Tools.cs* järgmise sisuga:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjutus: Oma stdio-serveri testimine

Nüüd, kui olete oma stdio-serveri üles ehitanud, testime seda, et veenduda, et see töötab õigesti.

### Eeltingimused

1. Veendu, et sul on MCP Inspector paigaldatud:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Sinu serveri kood peaks olema salvestatud (nt `server.py`)

### Testimine Inspectoriga

1. **Käivita Inspector koos oma serveriga**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ava veebi-liides**: Inspector avab brauseriakna, mis kuvab sinu serveri võimeid.

3. **Testi tööriistu**: 
   - Proovi `get_greeting` tööriista erinevate nimedega
   - Testi `calculate_sum` tööriista erinevate numbritega
   - Kutsu `get_server_info` tööriista, et näha serveri metaandmeid

4. **Jälgi suhtlust**: Inspector näitab JSON-RPC sõnumeid, mis vahetuvad kliendi ja serveri vahel.

### Mida peaksid nägema

Kui sinu server käivitub õigesti, peaksid nägema:
- Serveri võimekused loetletud Inspectoris
- Saadaval olevad tööriistad testimiseks
- Edukad JSON-RPC sõnumite vahetused
- Tööriistade vastused kuvatud liideses

### Levinumad probleemid ja lahendused

**Server ei käivitu:**
- Kontrolli, et kõik sõltuvused on paigaldatud: `pip install mcp`
- Kontrolli Python'i süntaksit ja taandumist
- Otsi veateateid konsoolist

**Tööriistad ei ilmu:**
- Veendu, et `@server.tool()` dekoraatorid on olemas
- Kontrolli, et tööriistade funktsioonid on defineeritud enne `main()`
- Veendu, et server on õigesti konfigureeritud

**Ühenduse probleemid:**
- Veendu, et server kasutab stdio-transporti õigesti
- Kontrolli, et mitte ükski teine protsess ei sekku
- Kontrolli Inspectori käsu süntaksit

## Ülesanne

Proovi laiendada oma serverit rohkemate võimekustega. Vaata [seda lehekülge](https://api.chucknorris.io/), et näiteks lisada tööriist, mis kutsub API-t. Sina otsustad, milline server välja nägema peaks. Head lõbu :)
## Lahendus

[Lahendus](./solution/README.md) Siin on võimalik lahendus töötava koodiga.

## Peamised järeldused

Selle peatüki peamised järeldused on järgmised:

- Stdio-transport on soovitatav mehhanism lokaalsetele MCP-serveritele.
- Stdio-transport võimaldab sujuvat suhtlust MCP-serverite ja klientide vahel, kasutades standardseid sisendi- ja väljundivooge.
- Võid kasutada nii Inspectorit kui Visual Studio Code'i, et kasutada stdio-servereid otse, muutes silumise ja integreerimise lihtsaks.

## Näited 

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.NET kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python) 

## Täiendavad ressursid

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mis järgmiseks

## Järgmised sammud

Nüüd, kui olete õppinud, kuidas ehitada MCP-servereid stdio-transpordiga, saate uurida keerukamaid teemasid:

- **Järgmine**: [HTTP-voogedastus MCP-ga (Streamable HTTP)](../06-http-streaming/README.md) - Saa teada teisest toetatud transpordimehhanismist kaugserverite jaoks
- **Edasijõudnud**: [MCP turvalisuse parimad tavad](../../02-Security/README.md) - Rakenda turvalisust oma MCP-serverites
- **Tootmises**: [Paigaldusstrateegiad](../09-deployment/README.md) - Juuruta oma serverid tootmiskeskkonda

## Täiendavad ressursid

- [MCP spetsifikatsioon 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Praegune spetsifikatsioon
- [MCP SDK dokumentatsioon](https://github.com/modelcontextprotocol/sdk) - SDK viited kõigile keeltele
- [Kogukonna näited](../../06-CommunityContributions/README.md) - Rohkem serverinäiteid kogukonnalt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->