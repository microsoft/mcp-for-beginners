# MCP Server na Usafirishaji wa stdio

> **⚠️ Sasisho Muhimu**: Kuanzia MCP Specification 2025-06-18, usafirishaji wa SSE (Server-Sent Events) umepitwa na wakati na kubadilishwa na usafirishaji wa "Streamable HTTP". Maelezo ya sasa ya MCP yanafafanua njia mbili kuu za usafirishaji:
> 1. **stdio** - Ingizo/utoaji wa kawaida (inapendekezwa kwa seva za ndani)
> 2. **Streamable HTTP** - Kwa seva za mbali zinazoweza kutumia SSE ndani
>
> Somo hili limeboreshwa kuzingatia usafirishaji wa **stdio**, ambao ni njia inayopendekezwa kwa utekelezaji wa seva nyingi za MCP.

Usafirishaji wa stdio unaruhusu seva za MCP kuwasiliana na wateja kupitia mito ya ingizo na utoaji wa kawaida. Hii ni njia inayotumika zaidi na inayopendekezwa katika maelezo ya sasa ya MCP, ikitoa njia rahisi na bora ya kujenga seva za MCP zinazoweza kuunganishwa kwa urahisi na programu mbalimbali za wateja.

## Muhtasari

Somo hili linaelezea jinsi ya kujenga na kutumia seva za MCP kwa kutumia usafirishaji wa stdio.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kujenga seva ya MCP kwa kutumia usafirishaji wa stdio.
- Kufanyia uchunguzi seva ya MCP kwa kutumia Inspector.
- Kutumia seva ya MCP ndani ya Visual Studio Code.
- Kuelewa mifumo ya sasa ya usafirishaji wa MCP na kwa nini stdio inapendekezwa.

## Usafirishaji wa stdio - Jinsi Unavyofanya Kazi

Usafirishaji wa stdio ni mojawapo ya aina mbili za usafirishaji zinazoungwa mkono katika maelezo ya sasa ya MCP (2025-06-18). Hivi ndivyo unavyofanya kazi:

- **Mawasiliano Rahisi**: Seva inasoma ujumbe wa JSON-RPC kutoka kwa ingizo la kawaida (`stdin`) na kutuma ujumbe kwa utoaji wa kawaida (`stdout`).
- **Mfumo wa Mchakato**: Mteja huzindua seva ya MCP kama mchakato wa chini.
- **Muundo wa Ujumbe**: Ujumbe ni maombi ya JSON-RPC, arifa, au majibu, yaliyotenganishwa na mistari mipya.
- **Kumbukumbu**: Seva INAWEZA kuandika maandishi ya UTF-8 kwa kosa la kawaida (`stderr`) kwa madhumuni ya kumbukumbu.

### Mahitaji Muhimu:
- Ujumbe LAZIMA utenganishwe na mistari mipya na HAUTAKIWI kuwa na mistari mipya ndani yake
- Seva HAITAKIWI kuandika chochote kwa `stdout` ambacho si ujumbe halali wa MCP
- Mteja HAUTAKIWI kuandika chochote kwa `stdin` ya seva ambacho si ujumbe halali wa MCP

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

Katika msimbo uliotangulia:

- Tunaingiza darasa la `Server` na `StdioServerTransport` kutoka kwa MCP SDK
- Tunaunda mfano wa seva na usanidi wa msingi na uwezo

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

Katika msimbo uliotangulia tunafanya:

- Kuunda mfano wa seva kwa kutumia MCP SDK
- Kufafanua zana kwa kutumia mapambo
- Kutumia meneja wa muktadha wa stdio_server kushughulikia usafirishaji

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

Tofauti kuu kutoka kwa SSE ni kwamba seva za stdio:

- Hazihitaji usanidi wa seva ya wavuti au viingilio vya HTTP
- Huzinduliwa kama michakato ya chini na mteja
- Huwasiliana kupitia mito ya stdin/stdout
- Ni rahisi kutekeleza na kufanyia uchunguzi

## Zoezi: Kujenga Seva ya stdio

Ili kujenga seva yetu, tunahitaji kuzingatia mambo mawili:

- Tunahitaji kutumia seva ya wavuti kufichua viingilio kwa ajili ya muunganisho na ujumbe.

## Maabara: Kujenga seva rahisi ya MCP stdio

Katika maabara hii, tutaunda seva rahisi ya MCP kwa kutumia usafirishaji wa stdio unaopendekezwa. Seva hii itafichua zana ambazo wateja wanaweza kupiga simu kwa kutumia Model Context Protocol ya kawaida.

### Mahitaji ya Awali

- Python 3.8 au zaidi
- MCP Python SDK: `pip install mcp`
- Uelewa wa msingi wa programu ya async

Tuanzishe kwa kujenga seva yetu ya kwanza ya MCP stdio:

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

## Tofauti kuu kutoka kwa mbinu ya SSE iliyopitwa na wakati

**Usafirishaji wa Stdio (Kiwango cha Sasa):**
- Mfano rahisi wa mchakato wa chini - mteja huzindua seva kama mchakato wa mtoto
- Mawasiliano kupitia stdin/stdout kwa kutumia ujumbe wa JSON-RPC
- Hakuna usanidi wa seva ya HTTP unaohitajika
- Utendaji bora na usalama
- Rahisi kufanyia uchunguzi na maendeleo

**Usafirishaji wa SSE (Uliopitwa na Wakati kuanzia MCP 2025-06-18):**
- Ulitaka seva ya HTTP na viingilio vya SSE
- Usanidi mgumu zaidi na miundombinu ya seva ya wavuti
- Masuala ya ziada ya usalama kwa viingilio vya HTTP
- Sasa imebadilishwa na Streamable HTTP kwa hali za wavuti

### Kujenga seva kwa usafirishaji wa stdio

Ili kujenga seva yetu ya stdio, tunahitaji:

1. **Kuleta maktaba zinazohitajika** - Tunahitaji vipengele vya seva ya MCP na usafirishaji wa stdio
2. **Kuunda mfano wa seva** - Kufafanua seva na uwezo wake
3. **Kufafanua zana** - Kuongeza utendaji tunaotaka kufichua
4. **Kusanidi usafirishaji** - Kusimamia mawasiliano ya stdio
5. **Kuendesha seva** - Kuanza seva na kushughulikia ujumbe

Tuanzishe hatua kwa hatua:

### Hatua ya 1: Unda seva ya msingi ya stdio

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

### Hatua ya 2: Ongeza zana zaidi

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

### Hatua ya 3: Kuendesha seva

Hifadhi msimbo kama `server.py` na uendeshe kutoka kwa mstari wa amri:

```bash
python server.py
```

Seva itaanza na kusubiri ingizo kutoka kwa stdin. Inawasiliana kwa kutumia ujumbe wa JSON-RPC kupitia usafirishaji wa stdio.

### Hatua ya 4: Kupima kwa Inspector

Unaweza kupima seva yako kwa kutumia MCP Inspector:

1. Sakinisha Inspector: `npx @modelcontextprotocol/inspector`
2. Endesha Inspector na uelekeze kwa seva yako
3. Pima zana ulizounda

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Kufanyia uchunguzi seva yako ya stdio

### Kutumia MCP Inspector

MCP Inspector ni zana muhimu kwa kufanyia uchunguzi na kupima seva za MCP. Hivi ndivyo unavyoweza kuitumia na seva yako ya stdio:

1. **Sakinisha Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Endesha Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Pima seva yako**: Inspector hutoa kiolesura cha wavuti ambapo unaweza:
   - Kuona uwezo wa seva
   - Kupima zana kwa vigezo tofauti
   - Kufuatilia ujumbe wa JSON-RPC
   - Kufanyia uchunguzi masuala ya muunganisho

### Kutumia VS Code

Unaweza pia kufanyia uchunguzi seva yako ya MCP moja kwa moja ndani ya VS Code:

1. Unda usanidi wa kuzindua ndani ya `.vscode/launch.json`:
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

2. Weka alama za kusimamisha katika msimbo wa seva yako
3. Endesha kifuatiliaji na upime kwa Inspector

### Vidokezo vya kawaida vya kufanyia uchunguzi

- Tumia `stderr` kwa kumbukumbu - usiandike chochote kwa `stdout` kwani imehifadhiwa kwa ujumbe wa MCP
- Hakikisha ujumbe wote wa JSON-RPC umetenganishwa na mistari mipya
- Pima kwa zana rahisi kwanza kabla ya kuongeza utendaji tata
- Tumia Inspector kuthibitisha muundo wa ujumbe

## Kutumia seva yako ya stdio ndani ya VS Code

Baada ya kujenga seva yako ya MCP stdio, unaweza kuijumuisha na VS Code ili kuitumia na Claude au wateja wengine wanaoendana na MCP.

### Usanidi

1. **Unda faili ya usanidi wa MCP** katika `%APPDATA%\Claude\claude_desktop_config.json` (Windows) au `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Anzisha upya Claude**: Funga na ufungue tena Claude ili kupakia usanidi mpya wa seva.

3. **Pima muunganisho**: Anzisha mazungumzo na Claude na ujaribu kutumia zana za seva yako:
   - "Je, unaweza kunisalimia kwa kutumia zana ya salamu?"
   - "Hesabu jumla ya 15 na 27"
   - "Ni taarifa gani za seva?"

### Mfano wa seva ya stdio ya TypeScript

Hapa kuna mfano kamili wa TypeScript kwa marejeleo:

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

### Mfano wa seva ya stdio ya .NET

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

## Muhtasari

Katika somo hili lililoboreshwa, umejifunza jinsi ya:

- Kujenga seva za MCP kwa kutumia usafirishaji wa **stdio** (njia inayopendekezwa)
- Kuelewa kwa nini usafirishaji wa SSE ulipitwa na wakati na kubadilishwa na stdio na Streamable HTTP
- Kuunda zana ambazo zinaweza kupigiwa simu na wateja wa MCP
- Kufanyia uchunguzi seva yako kwa kutumia MCP Inspector
- Kujumuisha seva yako ya stdio na VS Code na Claude

Usafirishaji wa stdio unatoa njia rahisi, salama zaidi, na yenye utendaji bora ya kujenga seva za MCP ikilinganishwa na mbinu ya SSE iliyopitwa na wakati. Ni usafirishaji unaopendekezwa kwa utekelezaji wa seva nyingi za MCP kuanzia maelezo ya 2025-06-18.

### .NET

1. Tuunde zana kadhaa kwanza, kwa hili tutaunda faili *Tools.cs* yenye maudhui yafuatayo:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Zoezi: Kupima seva yako ya stdio

Sasa kwa kuwa umejenga seva yako ya stdio, hebu tuipime ili kuhakikisha inafanya kazi vizuri.

### Mahitaji ya Awali

1. Hakikisha umeweka MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Msimbo wa seva yako unapaswa kuhifadhiwa (mfano, kama `server.py`)

### Kupima kwa Inspector

1. **Anzisha Inspector na seva yako**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Fungua kiolesura cha wavuti**: Inspector itafungua dirisha la kivinjari linaloonyesha uwezo wa seva yako.

3. **Pima zana**: 
   - Jaribu zana ya `get_greeting` kwa majina tofauti
   - Pima zana ya `calculate_sum` kwa namba mbalimbali
   - Piga zana ya `get_server_info` ili kuona metadata ya seva

4. **Fuatilia mawasiliano**: Inspector inaonyesha ujumbe wa JSON-RPC unaobadilishana kati ya mteja na seva.

### Unachopaswa kuona

Seva yako ikianza vizuri, unapaswa kuona:
- Uwezo wa seva umeorodheshwa katika Inspector
- Zana zinapatikana kwa kupima
- Ubadilishanaji wa ujumbe wa JSON-RPC uliofanikiwa
- Majibu ya zana yanaonyeshwa katika kiolesura

### Masuala ya kawaida na suluhisho

**Seva haitaanza:**
- Hakikisha utegemezi wote umesakinishwa: `pip install mcp`
- Thibitisha sintaksia ya Python na upangaji
- Angalia ujumbe wa makosa kwenye koni

**Zana hazionekani:**
- Hakikisha mapambo ya `@server.tool()` yapo
- Thibitisha kuwa kazi za zana zimefafanuliwa kabla ya `main()`
- Hakikisha seva imewekwa vizuri

**Masuala ya muunganisho:**
- Hakikisha seva inatumia usafirishaji wa stdio kwa usahihi
- Angalia kuwa hakuna michakato mingine inayozuia
- Thibitisha sintaksia ya amri ya Inspector

## Kazi

Jaribu kujenga seva yako na uwezo zaidi. Tazama [ukurasa huu](https://api.chucknorris.io/) ili, kwa mfano, kuongeza zana inayopiga API. Wewe ndiye unayeamua jinsi seva inavyopaswa kuonekana. Furahia :)

## Suluhisho

[Suluhisho](./solution/README.md) Hapa kuna suluhisho linalowezekana lenye msimbo unaofanya kazi.

## Mambo Muhimu

Mambo muhimu kutoka sura hii ni haya yafuatayo:

- Usafirishaji wa stdio ni njia inayopendekezwa kwa seva za MCP za ndani.
- Usafirishaji wa stdio unaruhusu mawasiliano ya moja kwa moja kati ya seva za MCP na wateja kwa kutumia mito ya ingizo na utoaji wa kawaida.
- Unaweza kutumia Inspector na Visual Studio Code kutumia seva za stdio moja kwa moja, na kufanya uchunguzi na ujumuishaji kuwa rahisi.

## Sampuli 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Rasilimali za Ziada

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Nini Kinachofuata

## Hatua Zifuatazo

Sasa kwa kuwa umejifunza jinsi ya kujenga seva za MCP kwa usafirishaji wa stdio, unaweza kuchunguza mada za hali ya juu zaidi:

- **Ijayo**: [Usafirishaji wa HTTP Streaming na MCP (Streamable HTTP)](../06-http-streaming/README.md) - Jifunze kuhusu njia nyingine ya usafirishaji inayoungwa mkono kwa seva za mbali
- **Hali ya Juu**: [MCP Security Best Practices](../../02-Security/README.md) - Tekeleza usalama katika seva zako za MCP
- **Uzalishaji**: [Mikakati ya Utekelezaji](../09-deployment/README.md) - Tekeleza seva zako kwa matumizi ya uzalishaji

## Rasilimali za Ziada

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Maelezo rasmi
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - Marejeleo ya SDK kwa lugha zote
- [Community Examples](../../06-CommunityContributions/README.md) - Sampuli zaidi za seva kutoka kwa jamii

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.