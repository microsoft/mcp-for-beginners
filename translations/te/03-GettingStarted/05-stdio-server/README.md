# MCP సర్వర్ stdio ట్రాన్స్పోర్ట్‌తో

> **⚠️ ముఖ్యమైన నవీకరణ**: MCP స్పెసిఫికేషన్ 2025-06-18 నుండి, స్టాండలోన్ SSE (సర్వర్-సెంట్స్ ఈవెంట్స్) ట్రాన్స్పోర్ట్‌ను **నిలిపివేయబడింది** మరియు "Streamable HTTP" ట్రాన్స్పోర్ట్‌తో మార్చబడింది. ప్రస్తుత MCP స్పెసిఫికేషన్ రెండు ప్రధాన ట్రాన్స్పోర్ట్ మెకానిజంలను నిర్వచిస్తుంది:
> 1. **stdio** - స్టాండర్డ్ ఇన్‌పుట్/ఔట్‌పుట్ (స్థానిక సర్వర్ల కోసం సిఫార్సు చేయబడింది)
> 2. **Streamable HTTP** - ఇంటర్నల్‌గా SSE ఉపయోగించగల రిమోట్ సర్వర్ల కోసం
>
> ఈ పాఠం **stdio ట్రాన్స్పోర్ట్**‌ పై కేంద్రీకరించడానికి నవీకరించబడింది, ఇది చాలా MCP సర్వర్ అమలు కోసం సిఫార్సు చేయబడిన విధానం.

stdio ట్రాన్స్పోర్ట్ MCP సర్వర్లకు క్లయింట్లతో స్టాండర్డ్ ఇన్‌పుట్ మరియు ఔట్‌పుట్ స్ట్రీమ్స్ ద్వారా కమ్యూనికేట్ చేసేందుకు అనుమతిస్తుంది. ఇది ప్రస్తుత MCP స్పెసిఫికేషన్‌లో అత్యంత సాధారణంగా ఉపయోగింపబడే మరియు సిఫార్సు చేయబడిన ట్రాన్స్పోర్ట్ మెకానిజం, వివిధ క్లయింట్ అప్లికేషన్‌లతో సులభంగా ఇంటిగ్రేట్ కావడానికి సులభమైన మరియు సమర్థమైన మార్గాన్ని అందిస్తుంది.

## అవలోకనం

ఈ పాఠం stdio ట్రాన్స్పోర్ట్ ఉపయోగించి MCP సర్వర్లు ఎలా నిర్మించాలో మరియు ఉపయోగించాలో చేర్చుకుంటుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం చివరిలో, మీరు చేయగలుగుతారు:

- stdio ట్రాన్స్పోర్ట్ ఉపయోగించి MCP సర్వర్‌ను నిర్మించడం.
- Inspector ఉపయోగించి MCP సర్వర్‌ను డీబగ్ చేయడం.
- Visual Studio Code ఉపయోగించి MCP సర్వర్‌ను వినియోగించడం.
- ప్రస్తుత MCP ట్రాన్స్పోర్ట్ మెకానిజంలను మరియు stdio ఎందుకు సిఫార్సు చేయబడిందో అర్థం చేసుకోవడం.


## stdio ట్రాన్స్పోర్ట్ - ఇది ఎలా పని చేస్తుంది

stdio ట్రాన్స్పోర్ట్ ప్రస్తుత MCP స్పెసిఫికేషన్ (2025-06-18)లో మద్దతు పొందిన రెండు ట్రాన్స్పోర్ట్ రకాలలో ఒకటి. ఇది ఎలా పనిచేస్తుందో చూస్తే:

- **సాధారణ కమ్యూనికేషన్**: సర్వర్ JSON-RPC సందేశాలను స్టాండర్డ్ ఇన్‌పుట్ (`stdin`) నుండి చదివి, స్టాండర్డ్ ఔట్‌పుట్ (`stdout`) కు సందేశాలు పంపుతుంది.
- **ప్రొసెస్ ఆధారితం**: క్లయింట్ MCP సర్వర్‌ను సబ్‌ప్రొసెస్‌గా ప్రారంభిస్తుంది.
- **మెసేజ్ ఫార్మాట్**: సందేశాలు వేరువేరు JSON-RPC అభ్యర్థనలు, నోటిఫికేషన్లు లేదా ప్రతిస్పందనలు, న్యూ‌లైన్స్‌తో వేరుచేయబడినవి.
- **లాగింగ్**: సర్వర్ UTF-8 స్ట్రింగ్‌లను లాగింగ్ కోసం స్టాండర్డ్ ఎరర్ (`stderr`) కు వ్రాయవచ్చు.

### ముఖ్యమైన అవసరాలు:
- సందేశాలు తప్పక న్యూ‌లైన్‌ల ద్వారా విడదీయబడాలి మరియు లోపల ఎటువంటి న్యూ‌లైన్‌లు ఉండకూడదు
- సర్వర్ `stdout` కు చెలామణీ కాని MCP సందేశాలు వ్రాయకూడదు
- క్లయింట్ సర్వర్ `stdin` కు చెలామణీ కాని MCP సందేశాలు వ్రాయకూడదు

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

ముందస్తు కోడులో:

- మేము MCP SDK నుండి `Server` తరగతి మరియు `StdioServerTransport` ని దిగుమతి చేసుకుంటాము
- ప్రాథమిక కాన్ఫిగరేషన్ మరియు సామర్థ్యాలతో సర్వర్ ఉదాహరణను సృష్టిస్తాము
- `StdioServerTransport` ఉదాహరణను సృష్టించి సర్వర్‌ను దానికి కनेक్ట్ చేసి stdin/stdout ద్వారా కమ్యూనికేషన్ సక్రియం చేస్తాము

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# సర్వర్ ఉదాహరణను సృష్టించండి
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

ముందస్తు కోడులో:

- MCP SDK ఉపయోగించి సర్వర్ ఉదాహరణను సృష్టిస్తాము
- డెకొరేటర్స్ ఉపయోగించి టూల్స్ నిర్వచిస్తాము
- stdio_server కాంటెక్స్ట్ మేనేజర్ ఉపయోగించి ట్రాన్స్పోర్ట్ ను హ్యాండిల్ చేస్తాము

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

SSE నుండి ప్రధాన తేడా stdio సర్వర్లు:

- వెబ్ సర్వర్ సెటప్ లేదా HTTP ఎండ్పాయింట్లు అవసరం ఉండవు
- క్లయింట్ ద్వారా సబ్‌ప్రొసెస్‌లుగా ప్రారంభించబడతాయి
- stdin/stdout స్ట్రీమ్స్ ద్వారా కమ్యూనికేట్ చేస్తాయి
- అమలు మరియు డీబగ్గింగ్ సులభం

## వ్యాయామం: stdio సర్వర్ రూపొందించడం

మన సర్వర్ సృష్టించడానికి, రెండు విషయాలు మనం గుర్తుంచుకోవాలి:

- కనెక్షన్ మరియు సందేశాల ఎండ్పాయింట్లను ఎక్స్‌పోజ్ చేయడానికి వెబ్ సర్వర్ అవసరం.
## ప్రయోగశాల: ఒక సరళమైన MCP stdio సర్వర్ నిర్మాణం

ఈ ప్రయోగశాలలో, మేము సిఫార్సు చేయబడిన stdio ట్రాన్స్పోర్ట్ ఉపయోగించి ఒక సరళమైన MCP సర్వర్‌ను సృష్టిస్తాము. ఈ సర్వర్ క్లయింట్లు మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ ద్వారా పిలవగల టూల్స్‌ను అందిస్తుంది.

### ముందస్తు అవసరాలు

- Python 3.8 లేదా తదితర వర్షన్
- MCP Python SDK: `pip install mcp`
- అసింక్రోనస్ ప్రోగ్రామింగ్ ప్రాథమిక అవగాహన

మొదటి MCP stdio సర్వర్ సృష్టించడం ప్రారంభిద్దాం:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# లాగింగ్‌ను ఏర్పాటు చేయండి
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# సర్వర్‌ను సృష్టించండి
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
    # stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించండి
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## నిలిపివేయబడిన SSE పద్ధతితో ప్రధాన తేడాలు

**Stdio Transport (ప్రస్తుత ప్రమాణం):**
- సులభమైన సబ్‌ప్రొసెస్ మోడల్ - క్లయింట్ సర్వర్‌ను చైల్‌డ్ ప్రొసెస్‌గా ప్రారంభిస్తుంది
- stdin/stdout ద్వారా JSON-RPC సందేశాల కమ్యూనికేషన్
- HTTP సర్వర్ సెటప్ అవసరం లేదు
- మెరుగైన పనితీరు మరియు భద్రత
- సులభమైన డీబగ్గింగ్ మరియు అభివృద్ధి

**SSE Transport (MCP 2025-06-18 నుండి నిలిపివేయబడింది):**
- SSE ఎండ్పాయింట్లతో HTTP సర్వర్ అవసరం
- వెబ్ సర్వర్ ఇన్‌ఫ్రాస్ట్రక్చర్‌తో క్లిష్టమైన సెటప్
- HTTP ఎండ్పాయింట్ల కోసం అదనపు భద్రతా గమనికలు
- వెబ్ ఆధారిత సందర్భాలకు Streamable HTTP తో భర్తీ చేయబడింది

### stdio ట్రాన్స్పోర్ట్‌తో సర్వర్ సృష్టించడం

మన stdio సర్వర్‌ను సృష్టించడానికి, మేము చేయాల్సింది:

1. **అవసరమైన లైబ్రరీలను దిగుమతి చేయడం** - MCP సర్వర్ కాంపోనెంట్లు మరియు stdio ట్రాన్స్పోర్ట్ అవసరం
2. **సర్వర్ ఉదాహరణ సృష్టించండి** - సర్వర్ ఆప్షన్లు మరియు సామర్థ్యాలను నిర్వచించండి
3. **టూల్స్ నిర్వచించండి** - అందించే ఫంక్షనాలిటీని చేర్చండి
4. **ట్రాన్స్పోర్ట్ సెటప్ చేయండి** - stdio కమ్యూనికేషన్‌ను కాన్ఫిగర్ చేయండి
5. **సర్వర్ ప్రారంభించండి** - సర్వర్ నడపండి మరియు సందేశాలను హ్యాండిల్ చేయండి

దీన్ని దశల వారీగా నిర్మిద్దాం:

### దశ 1: సాధారణ stdio సర్వర్ సృష్టించండి

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# లాగ్లను సెటప్ చేయండి
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# సర్వర్‌ను సృష్టించండి
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

### దశ 2: మరిన్ని టూల్స్ చేర్చండి

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

### దశ 3: సర్వర్ నడపండి

కోడ్ను `server.py`గా సేవ్ చేసి కంమాండ్ లైన్లో నడపండి:

```bash
python server.py
```

సర్వర్ ప్రారంభమవుతుంది మరియు stdin నుండి ఇన్‌పుట్ కోసం వేచి ఉంటుంది. ఇది stdio ట్రాన్స్పోర్ట్ ద్వారా JSON-RPC సందేశాలతో కమ్యూనికేట్ చేస్తుంది.

### దశ 4: Inspector తో పరీక్షించడం

మీ సర్వర్‌ను MCP Inspector ఉపయోగించి పరీక్షించవచ్చు:

1. Inspector ను ఇన్‌స్టాల్ చేయండి: `npx @modelcontextprotocol/inspector`
2. Inspector నడపండి మరియు దాన్ని మీ సర్వర్‌కు పాయింట్ చేయండి
3. మీరు సృష్టించిన టూల్స్‌ను పరీక్షించండి

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## మీ stdio సర్వర్‌ను డీబగ్ చేయడం

### MCP Inspector ఉపయోగించడం

MCP Inspector MCP సర్వర్లను డీబగ్ చేయడం మరియు పరీక్షించడం కోసం విలువైన సాధనం. మీరు దీనిని మీ stdio సర్వర్‌తో ఎలా ఉపయోగించాలో ఇక్కడ ఉంది:

1. **Inspector ఇన్‌స్టాల్ చేయండి**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector నడపండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **మీ సర్వర్‌ను పరీక్షించండి**: Inspector వెబ్ ఇంటర్‌ఫేస్‌ను అందిస్తుంది, అక్కడ మీరు:
   - సర్వర్ సామర్థ్యాలను చూడవచ్చు
   - వివిధ పారామీటర్లతో టూల్స్‌ను పరీక్షించండి
   - JSON-RPC సందేశాలను పర్యవేక్షించండి
   - కనెక్షన్ సమస్యలను డీబగ్ చేయండి

### VS Code ఉపయోగించడం

మీ MCP సర్వర్‌ను నేరుగా VS Codeలో డీబగ్ చేయవచ్చు:

1. `.vscode/launch.json`లో లాంచ్ కాన్ఫిగరేషన్ సృష్టించండి:
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

2. సర్వర్ కోడ్లో బ్రేక్‌పాయింట్లు పెట్టండి
3. డీబగ్గర్ నడపండి మరియు Inspector‌తో పరీక్షించండి

### సాధారణ డీబగ్గింగ్ సూచనలు

- లాగింగ్ కోసం `stderr` ఉపయోగించండి - MCP సందేశాల కోసం మాత్రమే `stdout` రిజర్వ్ చేయండి
- అన్ని JSON-RPC సందేశాలు న్యూ‌లైన్‌లతో విడవాలి
- క్లిష్టమైన ఫంక్షనాలిటీ చేర్చే ముందు సరళమైన టూల్స్‌తో పరీక్షించండి
- సందేశ ఫార్మాట్ తనిఖీ చేయడానికి Inspector ఉపయోగించండి

## VS Codeలో మీ stdio సర్వర్‌ను వినియోగించడం

మీ MCP stdio సర్వర్‌ను నిర్మించిన తర్వాత, దాన్ని VS Codeతో ఇంటిగ్రేట్ చేసి Claude లేదా ఇతర MCP-అనుకూల క్లయింట్లతో ఉపయోగించవచ్చు.

### కాన్ఫిగరేషన్

1. Windows లో `%APPDATA%\Claude\claude_desktop_config.json` లేదా Mac లో `~/Library/Application Support/Claude/claude_desktop_config.json`లో MCP కాన్ఫిగరేషన్ ఫైల్ సృష్టించండి:

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

2. **Claude మళ్లీ ప్రారంభించండి**: కొత్త సర్వర్ కాన్ఫిగరేషన్‌ను లోడ్ చేయడానికి Claude ని మూసి మళ్లీ ప్రారంభించండి.

3. **కనెక్షన్‌ను పరీక్షించండి**: Claude తో సంభాషణ ప్రారంభించి మీ సర్వర్ టూల్స్‌ను ఉపయోగించి చూడండి:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio సర్వర్ ఉదాహరణ

పూర్తి TypeScript ఉదాహరణ ఇక్కడ ఉంది:

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

// సాధనాలు జోడించండి
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

### .NET stdio సర్వర్ ఉదాహరణ

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

## సారాంశం

ఈ నవీకరించిన పాఠంలో మీరు నేర్చుకున్నది:

- ప్రస్తుత **stdio ట్రాన్స్పోర్ట్** (సిఫార్సు చేయబడిన విధానం) ఉపయోగించి MCP సర్వర్లు నిర్మించడం
- SSE ట్రాన్స్పోర్ట్ ఎందుకు నిలిపివేయబడిందో stdio మరియు Streamable HTTP ప్రతిస్పందనగా అర్థం చేసుకోవడం
- MCP క్లయింట్లచే పిలవగల టూల్స్ సృష్టించడం
- MCP Inspector ఉపయోగించి సర్వర్‌ను డీబగ్ చేయడం
- VS Code మరియు Claude తో మీ stdio సర్వర్‌ను ఇంటిగ్రేట్ చేయడం

stdio ట్రాన్స్పోర్ట్ డిప్రికేటెడ్ SSE పద్ధతికి భిన్నంగా సులభం, భద్రమైన మరియు అధిక పనితీరు అందించే మార్గం. ఇది 2025-06-18 స్పెసిఫికేషన్ ప్రకారం చాలా MCP సర్వర్ అమలు కోసం సిఫార్సు చేయబడిన ట్రాన్స్పోర్ట్.

### .NET

1. ముందుగా కొన్ని టూల్స్ సృష్టిద్దాం, ఇది కోడ్‌ను *Tools.cs* అనే ఫైలుగా క్రింది కంటెంట్‌తో చేయబడుతుంది:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## వ్యాయామం: మీ stdio సర్వర్‌ను పరీక్షించడం

మీ stdio సర్వర్‌ను నిర్మించిన తరువాత, దాని సరైన పని చేస్తున్నదో లేదో పరీక్షిద్దాం.

### ముందు అవసరాలు

1. MCP Inspector ఇన్‌స్టాల్ చేయబడి ఉండాలి:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. మీ సర్వర్ కోడ్ సేవ్ అయి ఉండాలి (ఉదా: `server.py`)

### Inspector తో పరీక్షించడం

1. **మీ సర్వర్‌తో Inspector ప్రారంభించండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **వెబ్ ఇంటర్‌ఫేస్ ను తెరవండి**: Inspector బ్రౌజర్ విండో తెరుచుకుని మీ సర్వర్ సామర్థ్యాలను చూపుతుంది.

3. **టూల్స్‌ను పరీక్షించండి**: 
   - వివిధ పేర్లతో `get_greeting` టూల్ ట్రై చేయండి
   - అనేక సంఖ్యలతో `calculate_sum` టూల్ పరీక్షించండి
   - సర్వర్ మెటాడేటాను పొందడానికి `get_server_info` టూల్ పిలవండి

4. **కమ్యూనికేషన్‌ను పర్యవేక్షించండి**: Inspector క్లయింట్ మరియు సర్వర్ మధ్య మార్పిడీ అవుతోన్న JSON-RPC సందేశాలను చూపిస్తుంది.

### మీరు చూడవలసిన దృశ్యాలు

మీ సర్వర్ సక్రమంగా ప్రారంభించినప్పుడు చూసే విషయాలు:
- Inspector లో సర్వర్ సామర్థ్యాలు జాబితా
- టూల్స్ అందుబాటులో ఉండటం
- విజయవంతమైన JSON-RPC సందేశ మార్పిడి
- ఇంటర్‌ఫేసులో టూల్ ప్రతిస్పందనలు ప్రదర్శన

### సాధారణ సమస్యలు మరియు పరిష్కారాలు

**సర్వర్ ప్రారంభించకపోవడం:**
- అన్ని డిపెండెన్సీలు ఇన్‌స్టాల్ అయ్యాయో చూడండి: `pip install mcp`
- Python సింటాక్స్ మరియు ఇన్డెంటేషన్ తనిఖీ చేయండి
- కన్సోల్ లో ఎర్రర్ సందేశాలు చూడండి

**టూల్స్ కనిపించకపోవడం:**
- `@server.tool()` డెకరేటర్స్ ఉన్నాయో తనిఖీ చేయండి
- టూల్ ఫంక్షన్స్ `main()` కంటే ముందు నిర్వచించబడ్డాయో చూడండి
- సర్వర్ సరైన స్థితికి కాన్ఫిగర్ అయుందని ధృవీకరించండి

**కనెక్షన్ సమస్యలు:**
- సర్వర్ stdio ట్రాన్స్పోర్ట్‌ను సరైన రీతిలో ఉపయోగిస్తున్నదో ఒకసారి తనిఖీ చేయండి
- మరెవరు ప్రాసెస్లు జోక్య ముందుకు రాకుండా చూసుకోండి
- Inspector ఆదేశపు సింటాక్స్ సరైనదో ధృవీకరించండి

## అసైన్‌మెంట్

మీ సర్వర్‌ను మరింత సామర్థ్యాలతో నిర్మించడానికి ప్రయత్నించండి. ఉదాహరణకు, [ఈ పేజీ](https://api.chucknorris.io/) చూడండి, API పిలవడానికి ఒక టూల్ చేర్పండి. మీరు సర్వర్ ఎలా ఉండాలో నిర్ణయించండి. ఆనందించండి :)

## పరిష్కారం

[పరిష్కారం](./solution/README.md) ఇది పని చేయనీయ కోడ్‌తో కూడిన సాధ్యమైన పరిష్కారం.

## ముఖ్య విషయాలు

ఈ అధ్యాయం నుండి ముఖ్యమైన విషయాలు:

- stdio ట్రాన్స్పోర్ట్ స్థానిక MCP సర్వర్లకు సిఫార్సు చేయబడిన మెకానిజం.
- stdio ట్రాన్స్పోర్ట్ MCP సర్వర్ మరియు క్లయింట్ల మధ్య స్టాండర్డ్ ఇన్‌పుట్ మరియు ఔట్‌పుట్ స్ట్రీమ్స్ ద్వారా సులభ కమ్యూనికేషన్ అనుమతిస్తుంది.
- మీరు Inspector మరియు Visual Studio Code ని ఉపయోగించి stdio సర్వర్‌లను నేరుగా వినియోగించవచ్చు, ఇది డీబగ్గింగ్ మరియు ఇంటిగ్రేషన్‌ను సులభతరం చేస్తుంది.

## నమూనాలు

- [Java కాలిక్యులేటర్](../samples/java/calculator/README.md)
- [.Net కాలిక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [JavaScript కాలిక్యులేటర్](../samples/javascript/README.md)
- [TypeScript కాలిక్యులేటర్](../samples/typescript/README.md)
- [Python కాలిక్యులేటర్](../../../../03-GettingStarted/samples/python)

## అదనపు వనరులు

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## తదుపరి ఏముందిది

## తరువాతి దశలు

మీరు stdio ట్రాన్స్పోర్ట్‌తో MCP సర్వర్లు ఎలా నిర్మించాలో నేర్చుకున్న తరువాత, మరింత అధునాతన అంశాలను అన్వేషించవచ్చు:

- **తదుపరి:** [MCP తో HTTP స్ట్రీమింగ్ (Streamable HTTP)](../06-http-streaming/README.md) - రిమోట్ సర్వర్ల కోసం మద్దతు ఉన్న మరొక ట్రాన్స్పోర్ట్ మెకానిజం గురించి తెలుసుకోండి
- **అధునాతన:** [MCP భద్రత ఉత్తమ ప్రాక్టీసులు](../../02-Security/README.md) - మీ MCP సర్వర్లలో భద్రతను అమలు చేయండి
- **ప్రొడక్షన్:** [డిప్లాయ్‌మెంట్ వ్యూహాలు](../09-deployment/README.md) - ప్రొడక్షన్‌లో మీ సర్వర్‌లను బ్యాక్ చేయండి

## అదనపు వనరులు

- [MCP స్పెసిఫికేషన్ 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - అధికారిక స్పెసిఫికేషన్
- [MCP SDK డాక్యుమెంటేషన్](https://github.com/modelcontextprotocol/sdk) - అన్ని భాషలకి SDK సూచికలు
- [సమాజ ఉదాహరణలు](../../06-CommunityContributions/README.md) - సమాజం నుండి మరిన్ని సర్వర్ ఉదాహరణలు

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మనం సరైనత కోసం ప్రయత్నిస్తుండగా, స్వయంచాలిత అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండొచ్చు అని దయచేసి గుర్తించండి. స్వభావ భాషలోiginal డాక్యుమెంట్ అధికారిక మూలంగా పరిగణించబడాలి. ముఖ్యమైన సమాచారం కోసం, వృత్తిగత మానవ అనువాదం సిఫార్సు చేయబడింది. ఈ అనువాదం వాడకం వల్ల జరిగిన ఏవైనా అవగాహన లోపాలు లేదా తప్పైన అర్ధాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->