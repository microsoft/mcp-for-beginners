# MCP Server na usafirishaji wa stdio

> **⚠️ Sasisho Muhimu**: Kuanzia Sifa ya MCP 2025-06-18, usafirishaji wa SSE wa pekee (Server-Sent Events) umeondolewa rasmi na kubadilishwa na usafirishaji wa "Streamable HTTP". Sifa ya MCP ya sasa inabainisha njia mbili kuu za usafirishaji:
> 1. **stdio** - Kuingiza/kunyoosha kwa kawaida (inashauriwa kwa seva za ndani)
> 2. **Streamable HTTP** - Kwa seva za mbali zinazoweza kutumia SSE ndani
>
> Somo hili limebadilishwa kuzingatia **usafirishaji wa stdio**, ambao ndiyo njia inayopendekezwa kwa utekelezaji wengi wa seva za MCP.

Usafirishaji wa stdio unaruhusu seva za MCP kuwasiliana na wateja kupitia milisho ya kuingiza na kutoa kwa kawaida. Hii ndiyo njia inayotumiwa zaidi na inayopendekezwa katika sifa ya MCP ya sasa, ikitoa njia rahisi na yenye ufanisi ya kujenga seva za MCP zinazoweza kuunganishwa kwa urahisi na programu mbalimbali za wateja.

## Muhtasari

Somo hili linashughulikia jinsi ya kujenga na kutumia Seva za MCP kwa kutumia usafirishaji wa stdio.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kujenga Seva ya MCP kwa kutumia usafirishaji wa stdio.
- Kutatua matatizo ya Seva ya MCP kwa kutumia Mchunguzi (Inspector).
- Kutumia Seva ya MCP kwa kutumia Visual Studio Code.
- Kuelewa mifumo ya usafirishaji wa MCP ya sasa na kwanini stdio inapendekezwa.


## Usafirishaji wa stdio - Jinsi Inavyofanya Kazi

Usafirishaji wa stdio ni mojawapo ya aina mbili za usafirishaji zinazotangazwa katika sifa ya MCP ya sasa (2025-06-18). Hapa ni jinsi unavyofanya kazi:

- **Mawasiliano Rahisi**: Seva husoma ujumbe za JSON-RPC kutoka kuingiza kwa kawaida (`stdin`) na kutuma ujumbe kwa kutoa kwa kawaida (`stdout`).
- **Kufanya kazi kama mchakato-chini**: Mteja huanzisha seva ya MCP kama mchakato mdogo (subprocess).
- **Muundo wa Ujumbe**: Ujumbe ni maombi, arifa, au majibu ya JSON-RPC yaliyoachwa kwa mistari mipya.
- **Kufuatilia**: Seva INAWEZA kuandika mistari ya UTF-8 kwa kosa la kawaida (`stderr`) kwa ajili ya kufuatilia.

### Mahitaji Muhimu:
- Ujumbe LAZIMA uachwe kwa mistari mipya na HAUZUIZI kuwa na mistari mipya iliyo ndani yake
- Seva HAIPASWI kuandika chochote kwa `stdout` ambacho si ujumbe halali wa MCP
- Mteja HAIPASWI kuandika chochote kwa `stdin` ya seva ambacho si ujumbe halali wa MCP

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

Katika msimbo uliopita:

- Tunaingiza darasa `Server` na `StdioServerTransport` kutoka MCP SDK
- Tunaunda mfano wa seva na usanidi wa msingi na uwezo

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Unda mfano wa seva
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

Katika msimbo uliopita sisi:

- Tunaunda mfano wa seva kwa kutumia MCP SDK
- Tufafanue zana kwa kutumia mapambo ya func (decorators)
- Tunutumie meneja wa muktadha (context manager) wa stdio_server kushughulikia usafirishaji

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

Tofauti kuu na SSE ni kwamba seva za stdio:

- Hazihitaji usanidi wa seva ya wavuti au viunganishi vya HTTP
- Huanzishwa kama michakato ndogo na mteja
- Wanasiliana kupitia milisho ya stdin/stdout
- Ni rahisi kutekeleza na kutatua matatizo

## Zoef: Kuunda Seva ya stdio

Ili kuunda seva yetu, tunahitaji kuzingatia vitu viwili:

- Tunahitaji kutumia seva ya wavuti kufungua viunganishi kwa ajili ya muunganisho na ujumbe.
## Maabara: Kuunda seva rahisi ya MCP stdio

Katika maabara hii, tutaunda seva rahisi ya MCP kwa kutumia usafirishaji wa stdio unaopendekezwa. Seva hii itaonyesha zana ambazo wateja wanaweza kuitumia kutumia itifaki ya Model Context Protocol ya kawaida.

### Mahitaji ya awali

- Python 3.8 au zaidi
- MCP Python SDK: `pip install mcp`
- Uelewa wa msingi wa programu za cha asynchronous

Tuanze kwa kuunda seva yetu ya kwanza ya MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Sanidi kuandika kumbukumbu
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

## Tofauti kuu na njia iliyokataliwa ya SSE

**Usafirishaji wa Stdio (Kiwango cha Sasa):**
- Mfano rahisi wa mchakato - mteja huanzisha seva kama mchakato mdogo
- Mawasiliano kupitia stdin/stdout kwa ujumbe za JSON-RPC
- Hakuna usanidi wa seva ya HTTP unahitajika
- Utendaji bora na usalama
- Rahisi kutatua matatizo na kuendeleza

**Usafirishaji wa SSE (Umeondolewa rasmi kuanzia MCP 2025-06-18):**
- Ulilazimisha seva ya HTTP na viunganishi vya SSE
- Usanidi tata zaidi wa miundombinu ya seva ya wavuti
- Mambo zaidi ya usalama kwa viunganishi vya HTTP
- Sasa umebadilishwa na Streamable HTTP kwa mazingira ya wavuti

### Kuunda seva kwa usafirishaji wa stdio

Ili kuunda seva yetu ya stdio, tunahitaji:

1. **Kuleta maktaba zinazohitajika** - Tunahitaji vipengele vya seva ya MCP na usafirishaji wa stdio
2. **Kuunda mfano wa seva** - Fafanua seva na uwezo wake
3. **Fafanua zana** - Ongeza kazi tunayotaka kuonyesha
4. **Sanidi usafirishaji** - Pangilia mawasiliano ya stdio
5. **Anzisha seva** - Anzisha seva na shughulikia ujumbe

Tujenge hatua kwa hatua:

### Hatua 1: Unda seva rahisi ya stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Sanidi uandikishaji wa kumbukumbu
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

### Hatua 3: Anzisha seva

Hifadhi msimbo kama `server.py` na uendeshwe kutoka kwenye mstari wa amri (command line):

```bash
python server.py
```

Seva itaanzishwa na kusubiri kuingizwa kutoka `stdin`. Husiliana kwa kutumia ujumbe za JSON-RPC juu ya usafirishaji wa stdio.

### Hatua 4: Kuangalia na Mchunguzi (Inspector)

Unaweza kujaribu seva yako kwa kutumia MCP Inspector:

1. Sakinisha Mchunguzi: `npx @modelcontextprotocol/inspector`
2. Endesha Mchunguzi na uelekeze kwa seva yako
3. Jaribu zana ulizotengeneza

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Kukagua shida za seva yako ya stdio

### Kutumia MCP Inspector

MCP Inspector ni chombo muhimu kwa kuchakata matatizo na kujaribu seva za MCP. Hapa ni jinsi ya kuitumia na seva yako ya stdio:

1. **Sakinisha Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Endesha Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Jaribu seva yako**: Inspector hutoa kiolesura cha wavuti ambapo unaweza:
   - Kuona uwezo wa seva
   - Kujaribu zana na vigezo tofauti
   - Kufuatilia ujumbe za JSON-RPC
   - Kutambua matatizo ya muunganisho

### Kutumia VS Code

Unaweza pia kutatua matatizo ya seva yako ya MCP moja kwa moja ndani ya VS Code:

1. Tengeneza usanidi wa kuanzisha `.vscode/launch.json`:
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

2. Weka alama za kukatiza (breakpoints) kwenye msimbo wa seva
3. Endesha mtafutaji (debugger) na jaribu na Inspector

### Vidokezo vya kawaida vya utatuzi

- Tumia `stderr` kwa ajili ya kufuatilia - kamwe usiandike `stdout` kwa kuwa imehifadhiwa kwa ujumbe za MCP
- Hakikisha ujumbe wote wa JSON-RPC umeachwa kwa mistari mipya
- Jaribu na zana rahisi kwanza kabla ya kuongeza kazi ngumu
- Tumia Inspector kuthibitisha muundo wa ujumbe

## Matumizi ya seva yako ya stdio ndani ya VS Code

Baada ya kujenga seva yako ya MCP stdio, unaweza kuunganisha na VS Code kuitumia na Claude au wateja wengine wanaoendana na MCP.

### Usanidi

1. **Tengeneza faili la usanidi la MCP** katika `%APPDATA%\Claude\claude_desktop_config.json` (Windows) au `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Fungua upya Claude**: Funga na fungua tena Claude ili ipakuze usanidi mpya wa seva.

3. **Jaribu muunganisho**: Anzisha mazungumzo na Claude na jaribu kutumia zana za seva yako:
   - "Je, unaweza kunipigia salamu ukitumia zana ya salamu?"
   - "Hesabu jumla ya 15 na 27"
   - "Je, ni taarifa gani kuhusu seva?"

### Mfano wa seva ya stdio kwa TypeScript

Hapa kuna mfano kamili wa TypeScript kwa ajili ya kumbukumbu:

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

### Mfano wa seva ya stdio kwa .NET

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

Katika somo hili lililosasishwa, umejifunza jinsi ya:

- Kujenga seva za MCP kwa kutumia **usafirishaji wa stdio** wa sasa (njia inayopendekezwa)
- Kuelewa kwa nini usafirishaji wa SSE umeachwa na kubadilishwa na stdio na Streamable HTTP
- Kuunda zana zinazoweza kuitwa na wateja wa MCP
- Kutatua matatizo ya seva yako kwa kutumia MCP Inspector
- Kuunganisha seva yako ya stdio na VS Code na Claude

Usafirishaji wa stdio unatoa njia rahisi, salama, na yenye ufanisi ya kujenga seva za MCP ukilinganisha na njia ya SSE iliyokataliwa. Ni usafirishaji unaopendekezwa kwa utekelezaji mingi wa seva za MCP kuanzia sifa ya 2025-06-18.


### .NET

1. Hebu tuanze kwa kuunda zana kwanza, kwa hili tutengeneza faili *Tools.cs* yenye maudhui yafuatayo:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Zoef: Kuangalia seva yako ya stdio

Sasa umejenga seva yako ya stdio, hebu ijaribu kuhakikisha inafanya kazi ipasavyo.

### Mahitaji ya awali

1. Hakikisha MCP Inspector imesakinishwa:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Msimbo wa seva yako unapaswa kuwa umehifadhiwa (mfano, `server.py`)

### Kujaribu na Inspector

1. **Anzisha Inspector kwa seva yako**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Fungua kiolesura cha wavuti**: Inspector itafungua dirisha la kivinjari linaonyesha uwezo wa seva yako.

3. **Jaribu zana**:
   - Jaribu zana ya `get_greeting` kwa majina tofauti
   - Jaribu zana ya `calculate_sum` kwa nambari mbalimbali
   - Piga simu zana ya `get_server_info` kuona metadata ya seva

4. **Fuata mawasiliano**: Inspector inaonyesha ujumbe za JSON-RPC zinazobenefitiwa kati ya mteja na seva.

### Utaratibu unaotarajiwa

Seva itapoanza kikamilifu, utaona:
- Uwezo wa seva umeorodheshwa kwenye Inspector
- Zana zinapatikana kwa majaribio
- Mabadilishano ya ujumbe za JSON-RPC yamefanikiwa
- Majibu ya zana yanaonyeshwa kwenye kiolesura

### Shida za kawaida na suluhisho

**Seva haiwezi kuanza:**
- Angalia kama vyanzo vyote vimesakinishwa: `pip install mcp`
- Hakikisha syntax ya Python na mkao ni sahihi
- Angalia ujumbe wa makosa kwenye console

**Zana hazionekani:**
- Hakikisha mapambo ya `@server.tool()` yapo
- Hakikisha zana zimetangazwa kabla ya `main()`
- Hakikisha seva imepangiliwa ipasavyo

**Shida za muunganisho:**
- Hakikisha seva inatumia usafirishaji wa stdio ipasavyo
- Angalia kama hakuna michakato mingine inakwamisha
- Hakikisha amri ya Inspector imeandikwa kwa usahihi

## Majukumu

Jaribu kuendeleza seva yako kwa uwezo zaidi. Angalia [ukurasa huu](https://api.chucknorris.io/) kuongeza zana inayopiga API. Uamuzi ni wako ni seva itakuwaje. Furahia :)

## Suluhisho

[Suluhisho](./solution/README.md) Hapa kuna suluhisho linalowezekana na msimbo unaofanya kazi.

## Muhimu wa Kuzingatia

Muhimu wa somo hili kwa kifupi ni:

- Usafirishaji wa stdio ndio njia inayopendekezwa kwa seva za MCP za ndani.
- Usafirishaji wa stdio unaruhusu mawasiliano rahisi kati ya seva za MCP na wateja kwa kutumia milisho ya kawaida ya kuingiza na kutoa.
- Unaweza kutumia Inspector na Visual Studio Code moja kwa moja kutumia seva za stdio, kufanya utatuzi na uunganishaji kuwa rahisi.

## Sampuli 

- [Kalkuleta ya Java](../samples/java/calculator/README.md)
- [Kalkuleta ya .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkuleta ya JavaScript](../samples/javascript/README.md)
- [Kalkuleta ya TypeScript](../samples/typescript/README.md)
- [Kalkuleta ya Python](../../../../03-GettingStarted/samples/python) 

## Rasilimali Zaidi

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Nini Kinachofuata

## Hatua Zifuatayo

Kwa sasa umejifunza jinsi ya kujenga seva za MCP na usafirishaji wa stdio, unaweza kuchunguza mada za hali ya juu:

- **Ifuatayo**: [HTTP Streaming na MCP (Streamable HTTP)](../06-http-streaming/README.md) - Jifunze kuhusu njia nyingine ya usafirishaji inayotumiwa kwa seva za mbali
- **Kiwango cha Juu**: [Mbinu Bora za Usalama wa MCP](../../02-Security/README.md) - Tekeleza usalama katika seva zako za MCP
- **Matumizi ya Kizalishaji**: [Mikakati ya Utekelezaji](../09-deployment/README.md) - Weka seva zako katika matumizi ya uzalishaji

## Rasilimali Zaidi

- [Sifa ya MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Sifa rasmi
- [Nyaraka za MCP SDK](https://github.com/modelcontextprotocol/sdk) - Marejeleo ya SDK kwa lugha zote
- [Mifano ya Jamii](../../06-CommunityContributions/README.md) - Mifano zaidi ya seva kutoka kwa jamii

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kauli ya Kukataa**:  
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu wa maana. Nyaraka ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->