# MCP server stdio transpordiga

> **⚠️ Tähtis uuendus**: Alates MCP spetsifikatsioonist 2025-06-18 on iseseisev SSE (Server-Sent Events) transport **väljajäänud** ja asendatud "voogedastatava HTTP" transpordiga. Praegune MCP spetsifikatsioon määratleb kaks peamist transpordimehhanismi:
> 1. **stdio** - Standardne sisend/väljund (soovitatav kohalikele serveritele)
> 2. **Voogedastatav HTTP** - Kaugsuhetes kasutatav, mis võib kasutada sisemiselt SSE-d
>
> See õppetund keskendub **stdio transpordile**, mis on soovitatud viis enamikule MCP serveri rakendustele.

Stdio transport võimaldab MCP serveritel suhelda klientidega läbi standardsete sisend- ja väljundvoogude. See on praeguse MCP spetsifikatsiooni kõige laialdasemalt kasutatud ja soovitatud transpordimehhanism, mis pakub lihtsat ja tõhusat viisi MCP serverite ehitamiseks, mida saab hõlpsasti integreerida erinevatesse kliendirakendustesse.

## Ülevaade

See õppetund käsitleb, kuidas ehitada ja kasutada MCP servereid stdio transpordiga.

## Õpieesmärgid

Õppetunni lõpuks oskad sa:

- Ehita MCP server stdio transpordiga.
- Silu MCP serverit kasutades Inspectorit.
- Kasutada MCP serverit Visual Studio Code’i abil.
- Mõista praeguseid MCP transpordimehhanisme ja miks stdio on soovitatav.


## stdio transport – kuidas see töötab

Stdio transport on üks kahest standardtraanspordist MCP spetsifikatsioonis
`2026-07-28`. Siin on, kuidas see toimib:

- **Lihtne suhtlus**: Server loeb JSON-RPC sõnumeid standard sisendist (`stdin`) ja saadab sõnumeid standard väljundisse (`stdout`).
- **Protsessipõhine**: Klient käivitab MCP serveri alamprotsessina.
- **Sõnumi formaat**: Sõnumid on üksikud JSON-RPC päringud, teated või vastused, mis on eraldatud reavahetusega.
- **Logimine**: Server VÕIB kirjutada UTF-8 stringe standardveasse (`stderr`) logimiseks.

### Olulised nõuded:
- Sõnumid PEAVAD olema reavahetusega eraldatud ja EI TOHI sisaldada sisemisi reavahetusi
- Server EI TOHI kirjutada `stdout`-i midagi, mis ei ole kehtiv MCP sõnum
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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Eelnevas koodis:

- Toome `Server` klassi ja `StdioServerTransport` MCP SDK-st
- Loome serveri instantsi põhilise konfiguratsiooni ja võimekustega
- Loome `StdioServerTransport` instantsi ja ühendame serveri sellega, võimaldades sidet stdin/stdout kaudu

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

Eelnevas koodis me:

- Loome serveri instantsi MCP SDK abil
- Defineerime tööriistad dekoratsioonidega
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

Peamine erinevus SSE-st on see, et stdio serverid:

- Ei vaja veebiserveri seadistust ega HTTP lõpp-punkte
- Käivitatakse alamprotsessidena kliendi poolt
- Suhtlevad stdin/stdout voogude kaudu
- On lihtsamini teostatavad ja silutavad

## Harjutus: stdio serveri loomine

Serveri loomiseks tuleb silmas pidada kahte asja:

- Peame kasutama veebiserverit ühenduse ja sõnumite lõpp-punktide avaldamiseks.
## Labor: Lihtsa MCP stdio serveri loomine

Selles laboris loome lihtsa MCP serveri, kasutades soovitatud stdio transporti. See server avaldab tööriistu, mida kliendid saavad helistada standardse Model Context Protocoli kaudu.

### Nõuded

- Python 3.8 või uuem
- MCP Python SDK: `pip install mcp`
- Põhiline arusaamine asünkroonsest programmeerimisest

Alustame esimese MCP stdio serveri loomisest:

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
    # Kasuta stdio transpordiks
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Peamised erinevused väljajäetud SSE lähenemisest

**Stdio transport (praegune standard):**
- Lihtne alamprotsessi mudel - klient käivitab serveri lapsprotsessina
- Suhtlus stdin/stdout kaudu JSON-RPC sõnumitega
- HTTP serveri seadistust ei ole vaja
- Parem jõudlus ja turvalisus
- Lihtsam silumine ja arendus

**SSE transport (väljajäänud alates MCP 2025-06-18):**
- Nõuab HTTP serverit SSE lõpp-punktidega
- Keerulisem seadistus koos veebiserveri infrastruktuuriga
- Täiendavad turvaküsimused HTTP lõpp-punktide osas
- Asendatud voogedastatava HTTP-ga veebipõhistes olukordades

### Serveri loomine stdio transpordiga

Stdio serveri loomiseks peame:

1. **Impordime vajalikud teegid** - MCP serveri komponendid ja stdio transport
2. **Loome serveri instantsi** - Määratleme serveri koos võimekustega
3. **Defineerime tööriistad** - Lisame funktsionaalsuse, mida avaldada soovime
4. **Seadistame transpordi** - Konfigureerime stdio side
5. **Käivitame serveri** - Alustame serverit ja käsitleme sõnumeid

Teeme seda samm-sammult:

### Samm 1: Lihtsa stdio serveri loomine

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

### Samm 2: Rohkem tööriistu lisama

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

Server käivitub ja ootab sisendit stdin-ist. Side toimub JSON-RPC sõnumitega stdio transpordi kaudu.

### Samm 4: Testimine Inspectoriga

Võid oma serverit testida, kasutades MCP Inspectorit:

1. Paigalda Inspector: `npx @modelcontextprotocol/inspector`
2. Käivita Inspector ja suuna see oma serverile
3. Testi loodud tööriistu

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Sinu stdio serveri silumine

### MCP Inspectori kasutamine

MCP Inspector on väärtuslik tööriist MCP serverite silumiseks ja testimiseks. Siin on, kuidas seda kasutada koos sinu stdio serveriga:

1. **Paigalda Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käivita Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testi serverit**: Inspector pakub veebiliidest, kus saad:
   - Vaadata serveri võimekusi
   - Testida tööriistu erinevate parameetritega
   - Jälgida JSON-RPC sõnumeid
   - Siluda ühenduse probleeme

### VS Code kasutamine

Võid ka siluda oma MCP serverit otse VS Codes:

1. Loo `.vscode/launch.json` käivitamiskonfiguratsioon:
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

2. Sea murdepunkte oma serveri koodis
3. Käivita silur ja testi Inspectoriga

### Üldised silumisnõuanded

- Kasuta logimiseks `stderr`-i – ära kirjuta kunagi `stdout`-i, see on reserveeritud MCP sõnumitele
- Veendu, et kõik JSON-RPC sõnumid on reavahetusega eraldatud
- Testi esmalt lihtsate tööriistadega enne keerukama funktsionaalsuse lisamist
- Kasuta Inspectorit sõnumite formaatide kontrollimiseks

## Oma stdio serveri kasutamine VS Codes

Kui oled üles ehitanud MCP stdio serveri, saad selle integreerida VS Code’ga, et kasutada seda Claude’i või teiste MCP-kompatible klientidega.

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

2. **Taaskäivita Claude**: Sule ja ava Claude uuesti, et laadida uus serverikonfiguratsioon.

3. **Testi ühendust**: Alusta vestlust Claude’iga ja proovi kasutada oma serveri tööriistu:
   - "Kas sa saad mind tervitada kasutades tervitustööriista?"
   - "Arvuta 15 ja 27 summa"
   - "Mis info on serveri kohta?"

### TypeScripti stdio serveri näide

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

// Lisa tööriistu
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

- Ehita MCP servereid kasutades praegust **stdio transporti** (soovitatud lähenemine)
- Mõista, miks SSE transpordist loobuti stdio ja voogedastatava HTTP kasuks
- Loo tööriistu, mida MCP kliendid saavad kutsuda
- Silu oma serverit MCP Inspectori abil
- Integreeri oma stdio server VS Code'i ja Claude’iga

Stdio transport pakub lihtsamat, turvalisemat ja tõhusamat viisi MCP serverite ehitamiseks võrreldes väljajäetud SSE lähenemisega. See on soovitatud transport enamikule MCP serveri rakendustele alates 2025-06-18 spetsifikatsioonist.


### .NET

1. Loome esmalt mõned tööriistad, selleks loome faili *Tools.cs* järgmise sisuga:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjutus: Oma stdio serveri testimine

Nüüd, kui oled oma stdio serveri üles seadnud, testime selle õiget tööd.

### Eeltingimused

1. Veendu, et MCP Inspector on paigaldatud:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Sinu serverikood peaks olema salvestatud (nt failina `server.py`)

### Testimine Inspectoriga

1. **Käivita Inspector koos oma serveriga**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ava veebiliides**: Inspector avab brauseri akna, kus kuvatakse sinu serveri võimekused.

3. **Testi tööriistu**: 
   - Proovi `get_greeting` tööriista erinevate nimedega
   - Testi `calculate_sum` tööriista erinevate arvudega
   - Kutsu `get_server_info` tööriist serveri metaandmete vaatamiseks

4. **Jälgi sidet**: Inspector näitab JSON-RPC sõnumeid, mis vahetatakse kliendi ja serveri vahel.

### Mida näha võiksid

Kui su server käivitub õigesti, peaksid nägema:
- Serveri võimekused on loetletud Inspectoris
- Tööriistad, mida testida saab
- Edukad JSON-RPC sõnumite vahetused
- Tööriistade vastused kuvatud liideses

### Levinud probleemid ja lahendused

**Server ei käivitunud:**
- Kontrolli, kas kõik sõltuvused on paigaldatud: `pip install mcp`
- Kontrolli Python'i süntaksit ja taanet
- Otsi konsoolist veateateid

**Tööriistad ei ilmu:**
- Veendu, et `@server.tool()` dekoratsioonid on olemas
- Kontrolli, et tööriistafunktsioonid on defineeritud enne `main()` funktsiooni
- Veendu, et server on õigesti konfigureeritud

**Ühenduse probleemid:**
- Veendu, et server kasutab correctly stdio transporti
- Kontrolli, et ükski teine protsess ei sega tööd
- Kontrolli Inspectori käsu süntaksit

## Ülesanne

Proovi oma serverit täiendavalt võimekamaks teha. Näiteks vaata [seda lehte](https://api.chucknorris.io/) ja lisan tööriist, mis kutsub API-d. Otsustad ise, kuidas server välja näeb. Head lõbu :)
## Lahendus

[Lahendus](./solution/README.md) Siin on üks võimalik lahendus toimiva koodiga.

## Peamised võtmepunktid

Selle peatüki võtmekohad on:

- Stdio transport on soovitatud mehhanism kohalikele MCP serveritele.
- Stdio transport võimaldab sujuvat suhtlust MCP serverite ja klientide vahel kasutades standardseid sisend- ja väljundvoolusid.
- Võid kasutada nii Inspectorit kui Visual Studio Code’i stdio serverite otse tarbimiseks, mis teeb silumise ja integreerimise lihtsaks.

## Näidised 

- [Java Kalkulaator](../samples/java/calculator/README.md)
- [.Net Kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulaator](../samples/javascript/README.md)
- [TypeScript Kalkulaator](../samples/typescript/README.md)
- [Python Kalkulaator](../../../../03-GettingStarted/samples/python) 

## Täiendavad ressursid

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mis edasi

## Järgmised sammud

Nüüd, kui oled õppinud MCP servereid ehitama stdio transpordiga, võid uurida edasijõudnud teemasid:

- **Järgmine**: [HTTP voogedastus MCP-ga (voogedastatav HTTP)](../06-http-streaming/README.md) - Õpi teist toetatud transpordimehhanismi kaugsuhete serveritele
- **Edasijõudnutele**: [MCP turvalisuse parimad tavad](../../02-Security/README.md) - Rakenda turvalisust MCP serverites
- **Tootmiskeskkonda**: [Deployment strateegiad](../09-deployment/README.md) - Paiguta serverid tootmiskasutuseks

## Täiendavad ressursid

- [MCP spetsifikatsioon 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Praegune spetsifikatsioon
- [MCP SDK dokumentatsioon](https://github.com/modelcontextprotocol/sdk) - SDK viited kõigile keeltele
- [Kogukonna näited](../../06-CommunityContributions/README.md) - Rohkem serveri näiteid kogukonnast

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->