# MCP Server na usafirishaji wa stdio

> **⚠️ Sasisho Muhimu**: Kuanzia MCP Maelezo ya Sifa 2025-06-18, usafirishaji wa SSE (Matukio yaliyopewa Server) wa pekee umefutwa kabisa na kubadilishwa na usafirishaji wa "Streamable HTTP". Mekanismo mbili kuu za usafirishaji zilizoainishwa katika maelezo ya MCP ya sasa ni:
> 1. **stdio** - Kuingia/kuondoka kwa kawaida (inayopendekezwa kwa seva za ndani)
> 2. **Streamable HTTP** - Kwa seva za mbali zinazoweza kutumia SSE ndani
>
> Somo hili limesasishwa ili kuzingatia **usafirishaji wa stdio**, njia inayopendekezwa kwa utekelezaji mwingi wa seva za MCP.

Usafirishaji wa stdio unaruhusu seva za MCP kuwasiliana na wateja kupitia vyanzo vya kuingiza na kuondoa vya kawaida. Huu ndio mekanismo ya usafirishaji inayotumiwa zaidi na kupendekezwa katika maelezo ya MCP ya sasa, ukitoa njia rahisi na bora ya kuunda seva za MCP zinazoweza kuunganishwa kirahisi na programu mbalimbali za wateja.

## Muhtasari

Somo hili linaelezea jinsi ya kujenga na kutumia Seva za MCP kwa kutumia usafirishaji wa stdio.

## Malengo ya Kujifunza

Mwisho wa somo hili, utakuwa na uwezo wa:

- Kujenga Seva ya MCP kwa kutumia usafirishaji wa stdio.
- Kutatua matatizo ya Seva ya MCP kwa kutumia Inspector.
- Kutumia Seva ya MCP kwa kutumia Visual Studio Code.
- Kuelewa mekanismo za usafirishaji wa MCP wa sasa na kwa nini stdio inapendekezwa.

## Usafirishaji wa stdio - Jinsi Unavyofanya Kazi

Usafirishaji wa stdio ni mojawapo ya aina mbili za usafirishaji zinazotegemezwa katika maelezo ya MCP ya sasa (2025-06-18). Hapa ni jinsi unavyofanya kazi:

- **Mawasiliano Rahisi**: Seva husoma ujumbe za JSON-RPC kutoka katika kuingiza kifaa cha kawaida (`stdin`) na kutuma ujumbe kwa kuondoa kifaa cha kawaida (`stdout`).
- **Mchakato wa msingi**: Mteja huanzisha seva ya MCP kama mchakato mdogo.
- **Muundo wa Ujumbe**: Ujumbe ni maombi, taarifa, au majibu ya JSON-RPC kwa kila moja, yamegawanywa na mistari mipya.
- **Kufuatilia**: Seva INAWEZA kuandika nyuzi za UTF-8 kwenye kosa la kawaida (`stderr`) kwa madhumuni ya kufuatilia.

### Mahitaji Muhimu:
- Ujumbe LAZIMA ugawanywe kwa mistari mipya na LASI KUWA na mistari mipya iliyojumuishwa ndani ya ujumbe mmoja
- Seva HAIFANYI KUANDIKIA chochote `stdout` ambacho si ujumbe halali wa MCP
- Mteja HAANDIKI chochote kwa seva `stdin` ambacho si ujumbe halali wa MCP

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

Katika msimbo uliotangulia:

- Tunaleta darasa la `Server` na `StdioServerTransport` kutoka MCP SDK
- Tunaunda mfano wa seva na usanidi wa msingi na uwezo
- Tunaunda mfano wa `StdioServerTransport` na kuunganisha seva nayo, kuwezesha mawasiliano kupitia stdin/stdout

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

Katika msimbo uliotangulia tunafanya:

- Kuunda mfano wa seva kwa kutumia MCP SDK
- Kuelezea zana kwa kutumia vivutio vya kazi
- Kutumia muktadha wa stdio_server kushughulikia usafirishaji

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

- Hazihitaji usanidi wa seva ya wavuti au njia za HTTP
- Huanzishwa kama michakato ndogo na mteja
- Huwasiliana kupitia vifurushi vya stdin/stdout
- Ni rahisi kutekeleza na kutatua matatizo

## Mazoezi: Kuunda seva ya stdio

Ili kuunda seva yetu, tunapaswa kuzingatia mambo mawili:

- Tunahitaji kutumia seva ya wavuti kutoa njia za kuunganishwa na ujumbe.
## Maabara: Kuunda seva rahisi ya MCP stdio

Katika maabara hii, tutaunda seva rahisi ya MCP kwa kutumia usafirishaji wa stdio unaopendekezwa. Seva hii itatoa zana ambazo wateja wanaweza kuitumia kwa kutumia Itifaki ya Muktadha wa Mfano wa kawaida.

### Mahitaji ya awali

- Python 3.8 au zaidi
- MCP Python SDK: `pip install mcp`
- Uelewa wa msingi wa programu za async

Tuanzishe kwa kuunda seva yetu ya kwanza ya MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Sanidi uandikishaji wa kumbukumbu
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tengeneza seva
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

## Tofauti kuu na njia iliyofutwa ya SSE

**Usafirishaji wa Stdio (Kiwango cha Sasa):**
- Mfano rahisi wa mchakato mdogo - mteja huanzisha seva kama mchakato mdogo
- Mawasiliano kupitia stdin/stdout kwa ujumbe wa JSON-RPC
- Hakuna usanidi wa seva ya HTTP unaohitajika
- Utendaji bora na usalama
- Urahisi wa kutatua matatizo na maendeleo

**Usafirishaji wa SSE (Umepuuzwa kuanzia MCP 2025-06-18):**
- Ulihitaji seva ya HTTP na njia za SSE
- Usaidizi mgumu zaidi na miundombinu ya seva ya wavuti
- Mambo ya ziada ya usalama kwa njia za HTTP
- Sasa umebadilishwa na Streamable HTTP kwa hali za wavuti

### Kuunda seva na usafirishaji wa stdio

Ili kuunda seva yetu ya stdio, tunapaswa:

1. **Kuleta maktaba zinazohitajika** - Tunahitaji vipengee vya seva ya MCP na usafirishaji wa stdio
2. **Kuunda mfano wa seva** - Elezea seva na uwezo wake
3. **Kuelezea zana** - Ongeza uwezo tunataka kutoa
4. **Kuweka usafirishaji** - Sanidi mawasiliano ya stdio
5. **Kuanza seva** - Anzisha seva na shughulikia ujumbe

Tujenge hatua kwa hatua:

### Hatua ya 1: Unda seva ya msingi ya stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Sanidi uandishi wa kumbukumbu
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Unda serveri
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

### Hatua ya 3: Kukimbia seva

Hifadhi msimbo kama `server.py` na uikimbie kutoka mstari wa amri:

```bash
python server.py
```

Seva itaanza na kusubiri maingizo kutoka stdin. Huwasiliana kwa kutumia ujumbe wa JSON-RPC kupitia usafirishaji wa stdio.

### Hatua ya 4: Kupima na Inspector

Unaweza kupima seva yako kwa kutumia MCP Inspector:

1. Sakinisha Inspector: `npx @modelcontextprotocol/inspector`
2. Endesha Inspector na uelekeze seva yako
3. Jaribu zana ulizotengeneza

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Kutatua matatizo ya seva yako ya stdio

### Kutumia MCP Inspector

MCP Inspector ni zana muhimu kwa kutatua matatizo na kupima seva za MCP. Hapa ni jinsi ya kuitumia na seva yako ya stdio:

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
   - Kupima zana kwa vigezo tofauti
   - Kufuatilia ujumbe wa JSON-RPC
   - Kubaini matatizo ya muunganisho

### Kutumia VS Code

Unaweza pia kutatua matatizo ya seva yako ya MCP moja kwa moja katika VS Code:

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

2. Weka pointi za kusimama ndani ya msimbo wa seva yako
3. Endesha debugger na ujaribu na Inspector

### Vidokezo vya kawaida vya utatuzi

- Tumia `stderr` kwa kufuatilia - kamwe usiandike `stdout` kwa sababu ni ya ujumbe wa MCP pekee
- Hakikisha ujumbe wote wa JSON-RPC umegawanywa kwa mistari mipya
- Jaribu zana rahisi kwanza kabla ya kuongeza utendaji mgumu
- Tumia Inspector kuthibitisha muundo wa ujumbe

## Kutumia seva yako ya stdio katika VS Code

Mara baada ya kujenga seva yako ya MCP stdio, unaweza kuiunganisha na VS Code kuitumia na Claude au wateja wengine wanaoendana na MCP.

### Usanidi

1. **Tengeneza faili la usanidi la MCP** kwa `%APPDATA%\Claude\claude_desktop_config.json` (Windows) au `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Anzisha upya Claude**: Funga na fungua tena Claude ili kupakia usanidi mpya wa seva.

3. **Jaribu muunganisho**: Anzisha mazungumzo na Claude na jaribu kutumia zana za seva yako:
   - "Je, unaweza kunikaribisha kwa kutumia chombo cha salamu?"
   - "Hesabu jumla ya 15 na 27"
   - "Nini habari za seva?"

### Mfano wa seva ya stdio ya TypeScript

Hapa kuna mfano kamili wa TypeScript kama rejeleo:

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

Katika somo hili lililosasishwa, umejifunza jinsi ya:

- Kujenga seva za MCP kwa kutumia **usafirishaji wa stdio** wa sasa (njia inayopendekezwa)
- Kuelewa kwa nini usafirishaji wa SSE ulifutwa na kubadilishwa na stdio na Streamable HTTP
- Kuunda zana zinazoweza kuitwa na wateja wa MCP
- Kutatua matatizo ya seva yako kwa kutumia MCP Inspector
- Kuingiza seva yako ya stdio na VS Code na Claude

Usafirishaji wa stdio unatoa njia rahisi, salama, na yenye utendaji bora zaidi ya kujenga seva za MCP ikilinganishwa na njia iliyofutwa ya SSE. Ni usafirishaji unaopendekezwa kwa utekelezaji mwingi wa seva za MCP kuanzia sifa ya 2025-06-18.

### .NET

1. Hebu tuanze kwa kuunda zana, kwa hili tutaunda faili *Tools.cs* yenye maudhui yafuatayo:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Mazoezi: Kupima seva yako ya stdio

Sasa umejenga seva yako ya stdio, tuchunguze kama inafanya kazi ipasavyo.

### Mahitaji ya awali

1. Hakikisha MCP Inspector imewekwa:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Msimbo wa seva umehifadhiwa (mfano, kama `server.py`)

### Kupima na Inspector

1. **Anzisha Inspector pamoja na seva yako**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Fungua kiolesura cha wavuti**: Inspector itafungua dirisha la kivinjari linaonyesha uwezo wa seva yako.

3. **Jaribu zana**:
   - Jaribu chombo `get_greeting` kwa majina tofauti
   - Jaribu chombo `calculate_sum` kwa nambari mbalimbali
   - Ita chombo `get_server_info` kuona metadata ya seva

4. **Fuatilia mawasiliano**: Inspector inaonyesha ujumbe wa JSON-RPC unaobadilishana kati ya mteja na seva.

### Unachotakiwa kuona

Seva yako ikianza vizuri, unapaswa kuona:
- Uwezo wa seva umeorodheshwa ndani ya Inspector
- Zana zinapatikana kwa ajili ya kupima
- Mabadilishano ya ujumbe wa JSON-RPC yamefanikiwa
- Majibu ya chombo yanaonyeshwa kwenye kiolesura

### Masuala na suluhisho za kawaida

**Seva haiwezi kuanza:**
- Hakiki kama utegemezi wote umewekwa: `pip install mcp`
- Angalia syntax na uelekezaji wa Python
- Tazama ujumbe wa makosa kwenye koni

**Zana hazionekani:**
- Hakikisha kuna vivutio vya `@server.tool()`
- Hakiki kama zana zimeelezwa kabla ya `main()`
- Hakikisha seva imewekwa vizuri

**Matatizo ya muunganisho:**
- Hakikisha seva inatumia usafirishaji wa stdio vizuri
- Hakikisha hakuna michakato mingine inayovuruga
- Hakiki syntax ya amri ya Inspector

## Kazi

Jaribu kuongeza uwezo zaidi kwenye seva yako. Tazama [ukurasa huu](https://api.chucknorris.io/) kuongeza chombo kinachoitisha API. Uamuzi wa muonekano wa seva ni wako. Furahia :)

## Suluhisho

[Suluhisho](./solution/README.md) Hapa kuna suluhisho linalowezekana na msimbo unaofanya kazi.

## Muhimu wa Kumbuka

Muhimu wa kufikia kutoka sura hii ni yafuatayo:

- Usafirishaji wa stdio ni mekanismo inayopendekezwa kwa seva za MCP za ndani.
- Usafirishaji wa stdio unaruhusu mawasiliano bila mshono kati ya seva za MCP na wateja kwa kutumia vyanzo vya kuingiza na kuondoa vya kawaida.
- Unaweza kutumia Inspector na Visual Studio Code kwa kutumia seva za stdio moja kwa moja, na kufanya utatuzi na ushirikiano kuwa rahisi.

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

Sasa baada ya kujifunza jinsi ya kujenga seva za MCP kwa usafirishaji wa stdio, unaweza kuchunguza mada zaidi za hali ya juu:

- **Ijayo**: [HTTP Streaming na MCP (Streamable HTTP)](../06-http-streaming/README.md) - Jifunze kuhusu njia nyingine ya usafirishaji kwa seva za mbali
- **Kiwango cha Juu**: [MCP Mazingira ya Usalama Bora](../../02-Security/README.md) - Tekeleza usalama katika seva zako za MCP
- **Matumizi ya Uzalishaji**: [Mikakati ya Uenezaji](../09-deployment/README.md) - Tumia seva zako kwa matumizi ya uzalishaji

## Rasilimali za Ziada

- [MCP Maelezo ya Sifa 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Maelezo rasmi
- [MCP SDK Maelezo](https://github.com/modelcontextprotocol/sdk) - Marejeo ya SDK kwa lugha zote
- [Mifano ya Jamii](../../06-CommunityContributions/README.md) - Mifano zaidi ya seva kutoka kwa jamii

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Maandishi ya kujitolea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri kwa akili ya bandia [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri zilizofanywa kwa mashine zinaweza kuwa na makosa au ukosefu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaaluma inayofanywa na binadamu inapendekezwa. Hatuwezi kuwajibika kwa kueleweka vibaya au tafsiri potovu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->