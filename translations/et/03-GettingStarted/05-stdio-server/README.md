# MCP Server koos stdio transpordiga

> **⚠️ Tähtis uuendus**: Alates MCP spetsifikatsioonist 2025-06-18 on iseseisev SSE (Server-Sent Events) transport **aegunud** ja asendatud "Streamable HTTP" transpordiga. Praegune MCP spetsifikatsioon määratleb kaks peamist transpordimehhanismi:
> 1. **stdio** - Standardne sisend/väljund (soovitatav kohalikele serveritele)
> 2. **Streamable HTTP** - Kaugserveritele, mis võivad sisemiselt kasutada SSE-d
>
> See õppetund on uuendatud, et keskenduda **stdio transpordile**, mis on enamikule MCP serveri rakendustele soovitatav lähenemine.

Stdio transport võimaldab MCP serveritel suhelda klientidega standardsete sisend- ja väljundvoogude kaudu. See on praeguse MCP spetsifikatsiooni kõige sagedamini kasutatav ja soovitatav transpordimehhanism, pakkudes lihtsat ja tõhusat viisi MCP serverite loomiseks, mida saab hõlpsasti integreerida erinevate kliendirakendustega.

## Ülevaade

See õppetund käsitleb MCP serverite loomist ja kasutamist stdio transpordi abil.

## Õpieesmärgid

Selle õppetunni lõpuks oskate:

- Luua MCP serveri stdio transpordi abil.
- Siluda MCP serverit Inspektori abil.
- Kasutada MCP serverit Visual Studio Code'is.
- Mõista praeguseid MCP transpordimehhanisme ja miks stdio on soovitatav.

## stdio transport - Kuidas see töötab

Stdio transport on üks kahest toetatud transporditüübist praeguses MCP spetsifikatsioonis (2025-06-18). Siin on, kuidas see töötab:

- **Lihtne suhtlus**: Server loeb JSON-RPC sõnumeid standardse sisendi (`stdin`) kaudu ja saadab sõnumeid standardse väljundi (`stdout`) kaudu.
- **Protsessipõhine**: Klient käivitab MCP serveri alamprotsessina.
- **Sõnumiformaat**: Sõnumid on üksikud JSON-RPC päringud, teated või vastused, eraldatud reavahetustega.
- **Logimine**: Server VÕIB kirjutada UTF-8 stringe standardse vea (`stderr`) väljundisse logimise eesmärgil.

### Peamised nõuded:
- Sõnumid PEAVAD olema eraldatud reavahetustega ja EI TOHI sisaldada sisseehitatud reavahetusi.
- Server EI TOHI kirjutada `stdout`-i midagi, mis pole kehtiv MCP sõnum.
- Klient EI TOHI kirjutada serveri `stdin`-i midagi, mis pole kehtiv MCP sõnum.

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

- Impordime `Server` klassi ja `StdioServerTransport` MCP SDK-st.
- Loome serveri eksemplari põhilise konfiguratsiooni ja võimekustega.

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

Eelnevas koodis:

- Loome serveri eksemplari MCP SDK abil.
- Määratleme tööriistad dekoraatorite abil.
- Kasutame stdio_server kontekstihaldurit transpordi haldamiseks.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Peamine erinevus SSE-st on see, et stdio serverid:

- Ei vaja veebiserveri seadistust ega HTTP lõpp-punkte.
- Käivitatakse kliendi poolt alamprotsessidena.
- Suhtlevad stdin/stdout voogude kaudu.
- On lihtsamad rakendada ja siluda.

## Harjutus: stdio serveri loomine

Serveri loomiseks peame meeles pidama kahte asja:

- Peame kasutama veebiserverit ühenduste ja sõnumite lõpp-punktide avamiseks.
## Labor: Lihtsa MCP stdio serveri loomine

Selles laboris loome lihtsa MCP serveri, kasutades soovitatud stdio transporti. See server pakub tööriistu, mida kliendid saavad kasutada standardse Model Context Protocoli abil.

### Eeltingimused

- Python 3.8 või uuem
- MCP Python SDK: `pip install mcp`
- Põhiline arusaam asünkroonsest programmeerimisest

Alustame oma esimese MCP stdio serveri loomist:

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

## Peamised erinevused aegunud SSE lähenemisest

**Stdio transport (praegune standard):**
- Lihtne alamprotsessi mudel - klient käivitab serveri alamprotsessina.
- Suhtlus stdin/stdout kaudu, kasutades JSON-RPC sõnumeid.
- HTTP serveri seadistust pole vaja.
- Parem jõudlus ja turvalisus.
- Lihtsam silumine ja arendus.

**SSE transport (aegunud alates MCP 2025-06-18):**
- Vajas HTTP serverit SSE lõpp-punktidega.
- Keerulisem seadistus veebiserveri infrastruktuuriga.
- Täiendavad turvalisuse kaalutlused HTTP lõpp-punktide jaoks.
- Nüüd asendatud Streamable HTTP-ga veebipõhiste stsenaariumide jaoks.

### Serveri loomine stdio transpordiga

Stdio serveri loomiseks peame:

1. **Impordima vajalikud teegid** - Vajame MCP serveri komponente ja stdio transporti.
2. **Looma serveri eksemplari** - Määratleme serveri selle võimekustega.
3. **Määratlema tööriistad** - Lisame funktsionaalsuse, mida soovime pakkuda.
4. **Seadistama transpordi** - Konfigureerime stdio suhtluse.
5. **Käivitama serveri** - Käivitame serveri ja haldame sõnumeid.

Ehitage see samm-sammult:

### Samm 1: Looge põhiline stdio server

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

### Samm 2: Lisage rohkem tööriistu

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

Salvestage kood failina `server.py` ja käivitage see käsurealt:

```bash
python server.py
```

Server käivitub ja ootab sisendit stdin kaudu. See suhtleb JSON-RPC sõnumite kaudu stdio transpordiga.

### Samm 4: Testimine Inspektoriga

Saate oma serverit testida MCP Inspektori abil:

1. Installige Inspektor: `npx @modelcontextprotocol/inspector`
2. Käivitage Inspektor ja suunake see oma serverile.
3. Testige loodud tööriistu.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Oma stdio serveri silumine

### MCP Inspektori kasutamine

MCP Inspektor on väärtuslik tööriist MCP serverite silumiseks ja testimiseks. Siin on, kuidas seda kasutada oma stdio serveriga:

1. **Installige Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Käivitage Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testige oma serverit**: Inspektor pakub veebiliidest, kus saate:
   - Vaadata serveri võimekusi.
   - Testida tööriistu erinevate parameetritega.
   - Jälgida JSON-RPC sõnumeid.
   - Siluda ühenduse probleeme.

### VS Code'i kasutamine

Saate oma MCP serverit otse VS Code'is siluda:

1. Looge käivitamise konfiguratsioon `.vscode/launch.json` failis:
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

2. Määrake koodis murdepunktid.
3. Käivitage silur ja testige Inspektoriga.

### Tavalised silumisnõuanded

- Kasutage `stderr` logimiseks - ärge kunagi kirjutage `stdout`-i, kuna see on reserveeritud MCP sõnumitele.
- Veenduge, et kõik JSON-RPC sõnumid oleksid reavahetustega eraldatud.
- Testige esmalt lihtsaid tööriistu enne keerukama funktsionaalsuse lisamist.
- Kasutage Inspektorit sõnumiformaatide kontrollimiseks.

## Oma stdio serveri kasutamine VS Code'is

Kui olete oma MCP stdio serveri loonud, saate selle integreerida VS Code'iga, et kasutada seda Claude'i või teiste MCP-ühilduvate klientidega.

### Konfiguratsioon

1. **Looge MCP konfiguratsioonifail** aadressil `%APPDATA%\Claude\claude_desktop_config.json` (Windows) või `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Taaskäivitage Claude**: Sulgege ja avage Claude uuesti, et laadida uus serveri konfiguratsioon.

3. **Testige ühendust**: Alustage vestlust Claude'iga ja proovige kasutada oma serveri tööriistu:
   - "Kas sa saad mind tervitada tervitustööriista abil?"
   - "Arvuta 15 ja 27 summa."
   - "Mis on serveri info?"

### TypeScript stdio serveri näide

Siin on täielik TypeScript näide viitamiseks:

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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Kokkuvõte

Selles uuendatud õppetunnis õppisite:

- MCP serverite loomist praeguse **stdio transpordi** abil (soovitatav lähenemine).
- Mõistma, miks SSE transport asendati stdio ja Streamable HTTP-ga.
- Looma tööriistu, mida MCP kliendid saavad kasutada.
- Siluma oma serverit MCP Inspektori abil.
- Integreerima oma stdio serveri VS Code'i ja Claude'iga.

Stdio transport pakub lihtsamat, turvalisemat ja tõhusamat viisi MCP serverite loomiseks võrreldes aegunud SSE lähenemisega. See on soovitatav transport enamikule MCP serveri rakendustele alates 2025-06-18 spetsifikatsioonist.

### .NET

1. Loome esmalt mõned tööriistad, selleks loome faili *Tools.cs* järgmise sisuga:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Harjutus: Oma stdio serveri testimine

Nüüd, kui olete oma stdio serveri loonud, testime seda, et veenduda selle korrektses töös.

### Eeltingimused

1. Veenduge, et MCP Inspektor on installitud:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Teie serveri kood peaks olema salvestatud (nt `server.py`).

### Testimine Inspektoriga

1. **Käivitage Inspektor oma serveriga**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Avage veebiliides**: Inspektor avab brauseriakna, kus kuvatakse teie serveri võimekused.

3. **Testige tööriistu**: 
   - Proovige `get_greeting` tööriista erinevate nimedega.
   - Testige `calculate_sum` tööriista erinevate numbritega.
   - Kutsuge `get_server_info` tööriista, et näha serveri metaandmeid.

4. **Jälgige suhtlust**: Inspektor kuvab JSON-RPC sõnumeid, mida klient ja server vahetavad.

### Mida peaksite nägema

Kui teie server käivitub korrektselt, peaksite nägema:
- Serveri võimekused loetletud Inspektoris.
- Tööriistad testimiseks saadaval.
- Edukad JSON-RPC sõnumivahetused.
- Tööriistade vastused kuvatud liideses.

### Tavalised probleemid ja lahendused

**Server ei käivitu:**
- Kontrollige, et kõik sõltuvused on installitud: `pip install mcp`.
- Kontrollige Python'i süntaksit ja taandamist.
- Otsige veateateid konsoolis.

**Tööriistad ei ilmu:**
- Veenduge, et `@server.tool()` dekoraatorid on olemas.
- Kontrollige, et tööriistade funktsioonid on määratletud enne `main()`.
- Veenduge, et server on korrektselt konfigureeritud.

**Ühenduse probleemid:**
- Veenduge, et server kasutab stdio transporti korrektselt.
- Kontrollige, et teised protsessid ei segaks.
- Kontrollige Inspektori käsusüntaksit.

## Ülesanne

Proovige oma serverit täiendada rohkemate võimekustega. Vaadake [seda lehte](https://api.chucknorris.io/), et näiteks lisada tööriist, mis kutsub API-d. Te otsustate, milline server peaks olema. Head katsetamist :)

## Lahendus

[Lahendus](./solution/README.md) Siin on võimalik lahendus koos töötava koodiga.

## Peamised õppetunnid

Selle peatüki peamised õppetunnid on järgmised:

- Stdio transport on soovitatav mehhanism kohalikele MCP serveritele.
- Stdio transport võimaldab MCP serveritel ja klientidel suhelda standardsete sisend- ja väljundvoogude kaudu.
- Saate kasutada nii Inspektorit kui ka Visual Studio Code'i stdio serverite otsekasutamiseks, muutes silumise ja integreerimise lihtsaks.

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

Nüüd, kui olete õppinud MCP serverite loomist stdio transpordiga, saate uurida keerukamaid teemasid:

- **Järgmine**: [HTTP voogedastus MCP-ga (Streamable HTTP)](../06-http-streaming/README.md) - Õppige tundma teist toetatud transpordimehhanismi kaugserverite jaoks.
- **Keerukas**: [MCP turvalisuse parimad tavad](../../02-Security/README.md) - Rakendage turvalisust oma MCP serverites.
- **Tootmine**: [Paigaldusstrateegiad](../09-deployment/README.md) - Paigaldage oma serverid tootmiskasutuseks.

## Lisamaterjalid

- [MCP spetsifikatsioon 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Ametlik spetsifikatsioon.
- [MCP SDK dokumentatsioon](https://github.com/modelcontextprotocol/sdk) - SDK viited kõigile keeltele.
- [Kogukonna näited](../../06-CommunityContributions/README.md) - Rohkem serveri näiteid kogukonnalt.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.