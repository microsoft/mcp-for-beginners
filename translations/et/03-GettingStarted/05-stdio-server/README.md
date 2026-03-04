# MCP-server stdio transpordiga

> **⚠️ Tähtis uuendus**: MCP spetsifikatsiooni 2025-06-18 seisuga on iseseisev SSE (Server-Sent Events) transport **ära toodud** ja asendatud „Streamable HTTP” transpordiga. Praegune MCP spetsifikatsioon määratleb kaks peamist transpordimehhanismi:
> 1. **stdio** - standardne sisend/väljund (soovitatav kohalikele serveritele)
> 2. **Streamable HTTP** - kaugserverite jaoks, mis võivad kasutada SSE-d sisemiselt
>
> See õppetund on uuendatud keskenduma **stdio transpordile**, mis on soovitatav enamikus MCP serverite rakendustes.

Stdio transport võimaldab MCP serveritel suhelda klientidega standardse sisendi ja väljundi kaudu. See on enim kasutatav ja soovitatav transpordimehhanism praeguses MCP spetsifikatsioonis, pakkudes lihtsat ja tõhusat viisi MCP serverite loomiseks, mida saab hõlpsasti integreerida erinevate kliendirakendustega.

## Ülevaade

Selles õppetunnis käsitleme, kuidas luua ja tarbida MCP servereid kasutades stdio transporti.

## Õpieesmärgid

Selle õppetunni lõpuks oskad:

- Luua MCP serveri, kasutades stdio transporti.
- Siluda MCP serverit, kasutades Inspectorit.
- Tarbida MCP serverit Visual Studio Code'is.
- Mõista praeguseid MCP transpordimehhanisme ja miks stdio on soovitatav.

## stdio transport – Kuidas see töötab

Stdio transport on üks kahest toetatud transporditüübist praeguses MCP spetsifikatsioonis (2025-06-18). Siin on, kuidas see töötab:

- **Lihtne kommunikatsioon**: server loeb JSON-RPC sõnumeid standardse sisendi (`stdin`) kaudu ja saadab sõnumeid standardse väljundi (`stdout`) kaudu.
- **Protsessipõhine**: klient käivitab MCP serveri alamprotsessina.
- **Sõnumite formaat**: sõnumid on üksikud JSON-RPC päringud, teavitused või vastused, mis on reavahetustega piiratud.
- **Logimine**: server VÕIB kirjutada UTF-8 stringe standardse vea voogu (`stderr`) logimise eesmärgil.

### Põhinõuded:
- Sõnumid PEAVAD olema reavahetustega piiratud ja EI TOHI sisaldada manustatud reavahetusi
- Server EI TOHI kirjutada midagi `stdout`-i, mis ei ole kehtiv MCP sõnum
- Klient EI TOHI kirjutada serveri `stdin`-i midagi, mis ei ole kehtiv MCP sõnum

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

Eelnevas koodis:

- Impordime MCP SDK-st `Server` klassi ja `StdioServerTransport`-i
- Loome serveri instantsi põhilise konfiguratsiooni ja võimekustega

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

- Loome serveri instantsi, kasutades MCP SDK-d
- Määratleme tööriistad dekoratiivide abil
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

Peamine erinevus SSE-st on see, et stdio serverid:

- Ei vaja veebiserveri seadistust ega HTTP otspunktide olemasolu
- Käivitatakse kliendi poolt alamprotsessidena
- Suhelda stdin/stdout voogude kaudu
- On lihtsamini teostatavad ja silutavad

## Harjutus: stdio serveri loomine

Serveri loomiseks tuleb meeles pidada kahte asja:

- Peame kasutama veebiserverit ühendus- ja sõnumi otspunktide eksponeerimiseks.

## Labor: Lihtsa MCP stdio serveri loomine

Selles laboris loome lihtsa MCP serveri, kasutades soovitatud stdio transporti. See server eksponeerib tööriistu, mida kliendid saavad kutsuda standardse Model Context Protocol-i abil.

### Eeldused

- Python 3.8 või uuem
- MCP Python SDK: `pip install mcp`
- Põhilised teadmised asünkroonsest programmeerimisest

Alustame oma esimese MCP stdio serveri loomisega:

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

## Peamised erinevused aegunud SSE lähenemisest

**Stdio transport (praegune standard):**
- Lihtne alamprotsessi mudel – klient käivitab serveri lapsprotsessina
- Kommunikatsioon stdin/stdout kaudu JSON-RPC sõnumitega
- HTTP serverit ei ole vaja seadistada
- Parem jõudlus ja turvalisus
- Lihtsam siluda ja arendada

**SSE transport (ära toodud seisuga MCP 2025-06-18):**
- Vajas HTTP serverit koos SSE otspunktidega
- Keerukam seadistus veebiserveri infrastruktuuriga
- Täiendavad turvakaalutlused HTTP otspunktide jaoks
- Asendatud Streamable HTTP-ga veebi-põhiste stsenaariumite jaoks

### stdio transpordiga serveri loomine

Serveri loomiseks tuleb:

1. **Impordida vajalikud teegid** – vajame MCP serveri komponente ja stdio transporti
2. **Luua serveri instants** – määratleda server ja selle võimekus
3. **Määratleda tööriistad** – lisada funktsionaalsus, mida soovime eksponeerida
4. **Seadistada transport** – konfigureerida stdio kommunikatsioon
5. **Käivitada server** – alustada serverit ja käsitleda sõnumeid

Loome selle samm-sammult:

### Samm 1: Põhilise stdio serveri loomine

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

### Samm 2: Rohkem tööriistu lisamine

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

Salvesta kood faili `server.py` ja käivita see käsurealt:

```bash
python server.py
```

Server käivitub ja ootab sisendeid stdin-ist. Suhtleb JSON-RPC sõnumite kaudu stdio transpordi peal.

### Samm 4: Testimine Inspectoriga

Saad oma serverit testida MCP Inspectoriga:

1. Paigalda Inspector: `npx @modelcontextprotocol/inspector`
2. Käivita Inspector ja suuna see oma serveri poole
3. Testi loodud tööriistu

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Stdio serveri silumine

### MCP Inspectori kasutamine

MCP Inspector on kasulik tööriist MCP serverite silumiseks ja testimiseks. Siin on, kuidas seda stdio serveri puhul kasutada:

1. **Paigalda Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käivita Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testi serverit**: Inspector pakub veebiliidest, kus saad:
   - Vaadata serveri võimekust
   - Testida tööriistu erinevate parameetritega
   - Jälgida JSON-RPC sõnumeid
   - Siluda ühendusprobleeme

### VS Code'i kasutamine

Sa saad MCP serverit siluda ka otse VS Code’is:

1. Loo konfiguratsioon failis `.vscode/launch.json`:
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

2. Sea murdepunktid serverikoodis
3. Käivita silur ja testi Inspectoriga

### Levinumad silumise nõuanded

- Kasuta logimiseks `stderr` – ära kunagi kirjuta `stdout`-i, see on reserveeritud MCP sõnumitele
- Veendu, et kõik JSON-RPC sõnumid on reavahetustega piiratud
- Testi esmalt lihtsate tööriistadega enne keerukamate lisamist
- Kasuta Inspectori, et kontrollida sõnumite formaate

## Oma stdio serveri tarbimine VS Code’is

Kui oled oma MCP stdio serveri loonud, saad selle integreerida VS Code’i, et kasutada seda Claude’i või teiste MCP-ühilduvate klientidega.

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

3. **Testi ühendust**: Alusta Claudega vestlust ja proovi kasutada serveri tööriistu:
   - „Kas sa saad mind tervitada tervitustööriista abil?”
   - „Arvuta 15 ja 27 summa.”
   - „Mis on serveri info?”

### TypeScript stdio serveri näide

Siin on täielik TypeScript näidis:

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

Selles uuendatud õppetunnis õppisid:

- MCP serverite loomist, kasutades praegust **stdio transporti** (soovitatud lähenemine)
- Miks SSE transport asendati stdio ja Streamable HTTP-ga
- Tööriistade loomist, mida MCP kliendid saavad kutsuda
- Serveri silumist MCP Inspectori abil
- Oma stdio serveri integreerimist VS Code’i ja Claude’iga

Stdio transport pakub lihtsamat, turvalisemat ja parema jõudlusega võimalust MCP serverite loomiseks võrreldes aegunud SSE lähenemisega. See on soovitatav transport enamikule MCP serverite rakendustele 2025-06-18 spetsifikatsiooni seisuga.

### .NET

1. Loome esmalt mõned tööriistad, selleks loome faili *Tools.cs* järgmise sisuga:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjutus: Oma stdio serveri testimine

Nüüd, kui oled oma stdio serveri loonud, testime seda, et veenduda selle õiges töös.

### Eeldused

1. Veendu, et MCP Inspector on paigaldatud:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Serveri kood peaks olema salvestatud (nt faili `server.py`)

### Testimine Inspectori abil

1. **Käivita Inspector koos serveriga**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ava veebiliides**: Inspector avab brauseriakna, kus näed serveri võimekusi.

3. **Testi tööriistu**: 
   - Proovi `get_greeting` tööriista erinevate nimedega
   - Testi `calculate_sum` tööriista erinevate arvudega
   - Kutsu `get_server_info` tööriista, et näha serveri metaandmeid

4. **Jälgi suhtlust**: Inspector kuvab klienti ja serverit vahetatavaid JSON-RPC sõnumeid.

### Mida näha ootama

Kui server käivitub korrektselt, peaksid nägema:
- Serveri võimekust Inspectoris listituna
- Testimiseks tööriistu saadaval
- Edukaid JSON-RPC sõnumite vahetusi
- Tööriistade vastuseid kasutajaliideses

### Levinumad probleemid ja lahendused

**Server ei käivitu:**
- Kontrolli, et kõik sõltuvused on paigaldatud: `pip install mcp`
- Kontrolli Python’i süntaksit ja taandeid
- Vaata konsoolist veateateid

**Tööriistad ei ilmu:**
- Kontrolli, et on olemas `@server.tool()` dekoratsioonid
- Veendu, et tööriistafunktsioonid on määratletud enne `main()` funktsiooni
- Kontrolli, kas server on korrektselt konfigureeritud

**Ühenduse probleemid:**
- Veendu, et server kasutab stdio transporti korrektselt
- Kontrolli, et teised protsessid ei sega
- Kontrolli Inspectori käskluse süntaksit

## Kodutöö

Proovi laiendada oma serverit rohkemate võimekustega. Vaata [seda lehte](https://api.chucknorris.io/), et näiteks lisada tööriist, mis kutsub API-d. Sa otsustad, kuidas server peaks välja nägema. Lõbutse hästi :)

## Lahendus

[Lahendus](./solution/README.md) Siin on võimalik lahendus koos töötava koodiga.

## Peamised tähelepanekud

Selle peatüki põhitõed on järgmised:

- Stdio transport on soovitatav mehhanism kohalikele MCP serveritele.
- Stdio transport võimaldab sujuvat suhtlust MCP serverite ja klientide vahel, kasutades standardseid sisendi ja väljundi vooge.
- Sa saad kas kasutada nii Inspectorit kui ka Visual Studio Code’i, et tarbida stdio servereid otse, muutes silumise ja integreerimise lihtsaks.

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)

## Lisamaterjalid

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mis edasi

## Järgmised sammud

Nüüd, kui oled õppinud MCP serverite loomist stdio transpordiga, võid sukelduda edasijõudnumatesse teemadesse:

- **Järgmine**: [HTTP voogedastus MCP-ga (Streamable HTTP)](../06-http-streaming/README.md) - Õpi teisest toetatud transpordimehhanismist kaugserverite jaoks
- **Edasijõudnutele**: [MCP turvalisuse parimad praktikad](../../02-Security/README.md) - Rakenda turvalisust oma MCP serverites
- **Tootmine**: [Deploy strateegiad](../09-deployment/README.md) - Paiguta oma server tootmiskeskkonda

## Lisamaterjalid

- [MCP spetsifikatsioon 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Ametlik spetsifikatsioon
- [MCP SDK dokumentatsioon](https://github.com/modelcontextprotocol/sdk) - SDK viited kõigile keeltele
- [Kogukonna näited](../../06-CommunityContributions/README.md) - Rohkem serverinäiteid kogukonnast

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tähelepanek**:
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada ametlikuks allikaks. Tähtsa teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta käesoleva tõlke kasutamisest tulenevate arusaamatuste või väärarusaamade eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->