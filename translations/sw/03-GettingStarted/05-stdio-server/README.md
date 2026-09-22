# Seva ya MCP na usafirishaji wa stdio

> **⚠️ Sasisho Muhimu**: Kuanzia Tafsiri ya MCP 2025-06-18, usafirishaji wa SSE (Server-Sent Events) wa pekee umeachwa rasmi na kubadilishwa na usafirishaji wa "Streamable HTTP". Tafsiri ya sasa ya MCP inaeleza njia kuu mbili za usafirishaji:
> 1. **stdio** - Ingizo/Matokeo ya kawaida (inapendekezwa kwa seva za ndani)
> 2. **Streamable HTTP** - Kwa seva za mbali ambazo zinaweza kutumia SSE kwa ndani
>
> Somo hili limebadilishwa ili kuzingatia **usafirishaji wa stdio**, ambao ni njia inayopendekezwa kwa utekelezaji wa seva nyingi za MCP.

Usafirishaji wa stdio unaruhusu seva za MCP kuwasiliana na wateja kupitia mito ya ingizo na matokeo ya kawaida. Hii ni njia inayotumika zaidi na inayopendekezwa kwa sasa katika tafsiri ya MCP, ikitoa njia rahisi na yenye ufanisi ya kujenga seva za MCP zinazoweza kuunganishwa kwa urahisi na programu mbalimbali za wateja.

## Muhtasari

Somo hili linahusu jinsi ya kujenga na kutumia seva za MCP kwa kutumia usafirishaji wa stdio.

## Malengo ya Kujifunza

Mwishoni mwa somo hili, utaweza:

- Kujenga seva ya MCP kwa kutumia usafirishaji wa stdio.
- Kutatua matatizo ya seva ya MCP kwa kutumia Inspector.
- Kutumia seva ya MCP kwa kutumia Visual Studio Code.
- Kuelewa njia za usafirishaji za MCP za sasa na kwanini stdio inapendekezwa.


## Usafirishaji wa stdio - Jinsi Inavyofanya Kazi

Usafirishaji wa stdio ni mojawapo ya njia mbili za kawaida za usafirishaji katika Tafsiri ya MCP
`2026-07-28`. Hivi ndivyo inavyofanya kazi:

- **Mawasiliano Rahisi**: seva husoma ujumbe wa JSON-RPC kutoka kwenye ingizo la kawaida (`stdin`) na kutuma ujumbe kwa matokeo ya kawaida (`stdout`).
- **Inayotegemea Mchakato**: mteja anazindua seva ya MCP kama mchakato mdogo.
- **Muundo wa Ujumbe**: Ujumbe ni maombi, taarifa, au majibu ya JSON-RPC binafsi, yamegawanywa kwa mistari mipya.
- **Kuingiza Habari**: seva INAWEZA kuandika mistari ya UTF-8 kwenye makosa ya kawaida (`stderr`) kwa madhumuni ya kuingiza habari.

### Mahitaji Muhimu:
- Ujumbe LAHITAJI kugawanywa kwa mistari mipya na HAURUHUSIWI kuwa na mistari mipya ndani yao
- Seva HAIBARIKI chochote kwenye `stdout` ambacho si ujumbe halali wa MCP
- Mteja HAANDIKI chochote kwenye `stdin` ya seva ambacho si ujumbe halali wa MCP

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

Katika msimbo ulio hapo juu:

- Tunaleta darasa `Server` na `StdioServerTransport` kutoka MCP SDK
- Tunaunda mfano wa seva na usanidi na uwezo wa msingi
- Tunaunda mfano wa `StdioServerTransport` na kuunganisha seva nayo, kuwezesha mawasiliano kupitia stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Tengeneza mfano wa seva
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

Katika msimbo ulio hapo juu tulifanya:

- Kuunda mfano wa seva kwa kutumia MCP SDK
- Kutoa zana kwa kutumia decorators
- Kutumia meneja wa muktadha stdio_server kushughulikia usafirishaji

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

Tofauti kuu na SSE ni kuwa seva za stdio:

- Hazihitaji usanidi wa seva ya wavuti au maeneo ya HTTP
- Zinazinduliwa kama michakato midogo na mteja
- Huwasiliana kupitia mito ya stdin/stdout
- Ni rahisi kutekeleza na kutatua matatizo

## Zoho: Kuunda Server ya stdio

Ili kuunda seva yetu, tunahitaji kuweka mambo mawili akilini:

- Tunahitaji kutumia seva ya wavuti kufunua maeneo ya muunganisho na ujumbe.
## Maabara: Kuunda seva rahisi ya MCP stdio

Katika maabara hii, tutaunda seva rahisi ya MCP kwa kutumia usafirishaji wa stdio unaopendekezwa. Seva hii itaonyesha zana ambazo wateja wanaweza kuitumia kwa kutumia Model Context Protocol ya kawaida.

### Mahitaji ya awali

- Python 3.8 au baadaye
- MCP Python SDK: `pip install mcp`
- Uelewa wa msingi wa programu zisizo za kawaida (async)

Tuanze kwa kuunda seva yetu ya kwanza ya MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Sanidi uandikishaji wa kumbukumbu
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Unda seva
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
    # Tumia usafirishaji wa stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Tofauti kuu na mbinu iliyobadilishwa ya SSE

**Usafirishaji wa Stdio (Kiwango cha sasa):**
- Mfano rahisi wa mchakato mdogo - mteja anazindua seva kama mchakato wa mtoto
- Mawasiliano kupitia stdin/stdout kwa ujumbe wa JSON-RPC
- Hakuna usanidi wa seva ya HTTP unaohitajika
- Utendaji bora na usalama
- Rahisi kutatua matatizo na kuendeleza

**Usafirishaji wa SSE (Umeachwa rasmi kuanzia MCP 2025-06-18):**
- Seva ya HTTP inayohitajika na maeneo ya SSE
- Usanidi mgumu zaidi na miundombinu ya seva ya wavuti
- Mambo ya ziada ya usalama kwa maeneo ya HTTP
- Sasa imebadilishwa na Streamable HTTP kwa matukio yanayotegemea wavuti

### Kuunda seva na usafirishaji wa stdio

Ili kuunda seva yetu ya stdio, tunahitaji:

1. **Leta maktaba zinazohitajika** - Tunahitaji vipengele vya seva ya MCP na usafirishaji wa stdio
2. **Unda mfano wa seva** - Tambua seva na uwezo wake
3. **Tambua zana** - Ongeza uwezo tunayotaka kufungua
4. **Weka usafirishaji** - Sanidi mawasiliano ya stdio
5. **Anzisha seva** - Anzisha seva na shughulikia ujumbe

Tujenge hatua kwa hatua:

### Hatua 1: Unda seva ya stdio ya msingi

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Sanidi ufuatiliaji
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tengeneza seva
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

### Hatua 2: Ongeza zana zaidi

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

### Hatua 3: Kuendesha seva

Hifadhi msimbo kama `server.py` na uendeshe kutoka mstari wa amri:

```bash
python server.py
```

Seva itaanza na kusubiri ingizo kutoka stdin. Inawasiliana kwa kutumia ujumbe wa JSON-RPC kupitia usafirishaji wa stdio.

### Hatua 4: Kupima na Inspector

Unaweza kupima seva yako kwa kutumia MCP Inspector:

1. Weka Inspector: `npx @modelcontextprotocol/inspector`
2. Endesha Inspector na uelekeze katika seva yako
3. Pima zana ulizozitengeneza

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Kutatua matatizo ya seva yako ya stdio

### Kutumia MCP Inspector

MCP Inspector ni zana muhimu kwa kutatua matatizo na kupima seva za MCP. Hivi ndivyo ya kutumia na seva yako ya stdio:

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
   - Kufuatilia ujumbe za JSON-RPC
   - Kutatua matatizo ya muunganisho

### Kutumia VS Code

Pia unaweza kutatua matatizo ya seva yako ya MCP moja kwa moja katika VS Code:

1. Unda usanidi wa kuanzisha katika `.vscode/launch.json`:
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

2. Weka pointi za kukomesha (breakpoints) kwenye msimbo wako wa seva
3. Endesha debug na upime kwa Inspector

### Vidokezo vya kawaida vya kutatua matatizo

- Tumia `stderr` kwa kuingiza habari - usiandike `stdout` kama ni kwa ujumbe wa MCP pekee
- Hakikisha ujumbe wote wa JSON-RPC umegawanywa kwa mistari mipya
- Pima na zana rahisi kwanza kabla ya kuongeza uwezo mgumu
- Tumia Inspector kuthibitisha miundo ya ujumbe

## Kutumia seva yako ya stdio katika VS Code


Mara tu baada ya kujenga seva yako ya stdio ya MCP, unaweza kuisanifisha na VS Code kuitumia na Claude au wateja wengine wanaounga mkono MCP.

### Usanidi

1. **Tengeneza faili la usanidi la MCP** kwenye `%APPDATA%\Claude\claude_desktop_config.json` (Windows) au `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

3. **Jaribu muunganisho**: Anza mazungumzo na Claude na jaribu kutumia zana za seva yako:
   - "Je, unaweza kunikabidhi kwa kutumia chombo cha salamu?"
   - "Hesabu jumla ya 15 na 27"
   - "Nini taarifa za seva?"

### Mfano wa seva ya stdio kwa TypeScript

Hapa kuna mfano kamili wa TypeScript kwa rejeleo:

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

// Ongeza zana
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

## Muhtasari

Katika somo hili lililosasishwa, ulijifunza jinsi ya:

- Kujenga seva za MCP ukitumia **usafirishaji wa stdio** wa sasa (njia inayopendekezwa)
- Kuelewa kwa nini usafirishaji wa SSE ulisitishwa kwa faida ya stdio na Streamable HTTP
- Kutengeneza zana zinazoweza kuitwa na wateja wa MCP
- Kuchanganua seva yako kwa kutumia MCP Inspector
- Kuunganisha seva yako ya stdio na VS Code na Claude

Usafirishaji wa stdio hutoa njia rahisi zaidi, salama zaidi, na yenye utendaji bora ya kujenga seva za MCP ikilinganishwa na njia ya SSE iliyokataliwa. Ni usafirishaji unaopendekezwa kwa utekelezaji mwingi wa seva za MCP kutoka kwa vipimo vya 2025-06-18.


### .NET

1. Hebu kwanza tutengeneze baadhi ya zana, kwa hili tutaunda faili *Tools.cs* yenye maudhui ifuatayo:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Mazoezi: Kupima seva yako ya stdio

Sasa umejenga seva yako ya stdio, hebu tuipime kuhakikisha inafanya kazi kwa usahihi.

### Mambo ya Kuandaa

1. Hakikisha umeweka MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Msimbo wa seva yako unapaswa kuhifadhiwa (kwa mfano, kama `server.py`)

### Kupima kwa Inspector

1. **Anzisha Inspector na seva yako**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Fungua kiolesura cha wavuti**: Inspector itafungua dirisha la kivinjari linaloonyesha uwezo wa seva yako.

3. **Jaribu zana**: 
   - Jaribu chombo cha `get_greeting` na majina tofauti
   - Jaribu chombo cha `calculate_sum` na nambari mbalimbali
   - Piga chombo cha `get_server_info` kuona metadata ya seva

4. **Fuatilia mawasiliano**: Inspector inaonyesha ujumbe za JSON-RPC zinazoambukizana kati ya mteja na seva.

### Kile unachopaswa kuona

Unapoanzisha seva yako kwa usahihi, unapaswa kuona:
- Uwezo wa seva ulioorodheshwa katika Inspector
- Zana zinazopatikana kwa majaribio
- Kubadilishana ujumbe wa JSON-RPC kufanikiwa
- Majibu ya zana yanaonyeshwa kwenye kiolesura

### Matatizo ya kawaida na suluhisho

**Seva haianzi:**
- Hakikisha utegemezi wote umewekwa: `pip install mcp`
- Hakiki syntax na usanidi wa Python
- Tafuta ujumbe za makosa kwenye konsole

**Zana hazionekani:**
- Hakikisha decorators `@server.tool()` zipo
- Hakiki kuwa kazi za zana zimetangazwa kabla ya `main()`
- Hakikisha seva imesanifiwa vizuri

**Matatizo ya muunganisho:**
- Hakikisha seva inatumia usafirishaji wa stdio kwa usahihi
- Hakiki kuwa hakuna michakato mingine inayoingilia
- Hakiki sintaksia ya amri ya Inspector

## Kazi ya Nyumbani

Jaribu kujenga seva yako yenye uwezo zaidi. Angalia [ukurasa huu](https://api.chucknorris.io/) kwa mfano, kuongeza chombo kinachopiga API. Uamuzi ni wako juu ya jinsi seva inavyotakiwa kuonekana. Furahia :)
## Suluhisho

[Suluhisho](./solution/README.md) Hapa kuna suluhisho linalowezekana na msimbo unaofanya kazi.

## Mambo Muhimu Kujifunza

Mambo muhimu ya kujifunza kutoka sura hii ni yafuatayo:

- Usafirishaji wa stdio ni mbinu inayopendekezwa kwa seva za MCP za ndani.
- Usafirishaji wa stdio unaruhusu mawasiliano bora baina ya seva za MCP na wateja kwa kutumia mito ya kawaida ya kuingiza na kutoa taarifa.
- Unaweza kutumia Inspector na Visual Studio Code moja kwa moja kwa seva za stdio, kufanya uchunguzi na kuunganisha kuwa rahisi.

## Sampuli 

- [Kalkuleta ya Java](../samples/java/calculator/README.md)
- [Kalkuleta ya .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkuleta ya JavaScript](../samples/javascript/README.md)
- [Kalkuleta ya TypeScript](../samples/typescript/README.md)
- [Kalkuleta ya Python](../../../../03-GettingStarted/samples/python) 

## Rasilimali Zaidi

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kinachofuata

## Hatua Zifuatazo

Sasa unajua jinsi ya kujenga seva za MCP kwa usafirishaji wa stdio, unaweza kuchunguza mada za hali ya juu zaidi:

- **Ifuatayo**: [Utoaji wa HTTP na MCP (Streamable HTTP)](../06-http-streaming/README.md) - Jifunze kuhusu njia nyingine ya usafirishaji inayounga mkono seva za mbali
- **Ya Juu zaidi**: [Mbinu Bora za Usalama wa MCP](../../02-Security/README.md) - Tekeleza usalama katika seva zako za MCP
- **Uzalishaji**: [Mikakati ya Usambazaji](../09-deployment/README.md) - Sambaza seva zako kwa matumizi ya uzalishaji

## Rasilimali Zaidi

- [Maelezo ya MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Maelezo ya sasa
- [Nyaraka za SDK ya MCP](https://github.com/modelcontextprotocol/sdk) - Marejeleo ya SDK kwa lugha zote
- [Mifano ya Jamii](../../06-CommunityContributions/README.md) - Mifano zaidi ya seva kutoka kwa jamii

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->