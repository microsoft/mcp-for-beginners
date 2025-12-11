<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77735b446eb79b1bba9c849865cd0ced",
  "translation_date": "2025-12-11T11:49:57+00:00",
  "source_file": "03-GettingStarted/05-stdio-server/README.md",
  "language_code": "te"
}
-->
# stdio ట్రాన్స్‌పోర్ట్‌తో MCP సర్వర్

> **⚠️ ముఖ్యమైన నవీకరణ**: MCP స్పెసిఫికేషన్ 2025-06-18 నుండి, స్టాండలోన్ SSE (సర్వర్-సెంట్ ఈవెంట్స్) ట్రాన్స్‌పోర్ట్ **డిప్రికేటెడ్** అయింది మరియు దాన్ని "స్ట్రీమబుల్ HTTP" ట్రాన్స్‌పోర్ట్‌తో మార్చారు. ప్రస్తుత MCP స్పెసిఫికేషన్ రెండు ప్రధాన ట్రాన్స్‌పోర్ట్ మెకానిజంలను నిర్వచిస్తుంది:
> 1. **stdio** - స్టాండర్డ్ ఇన్‌పుట్/అవుట్‌పుట్ (స్థానిక సర్వర్ల కోసం సిఫార్సు చేయబడింది)
> 2. **స్ట్రీమబుల్ HTTP** - SSEని అంతర్గతంగా ఉపయోగించే రిమోట్ సర్వర్ల కోసం
>
> ఈ పాఠం **stdio ట్రాన్స్‌పోర్ట్** పై దృష్టి సారించడానికి నవీకరించబడింది, ఇది ఎక్కువ MCP సర్వర్ అమలుల కోసం సిఫార్సు చేయబడిన విధానం.

stdio ట్రాన్స్‌పోర్ట్ MCP సర్వర్లు క్లయింట్లతో స్టాండర్డ్ ఇన్‌పుట్ మరియు అవుట్‌పుట్ స్ట్రీమ్స్ ద్వారా కమ్యూనికేట్ చేయడానికి అనుమతిస్తుంది. ఇది ప్రస్తుత MCP స్పెసిఫికేషన్‌లో అత్యంత సాధారణంగా ఉపయోగించే మరియు సిఫార్సు చేయబడిన ట్రాన్స్‌పోర్ట్ మెకానిజం, వివిధ క్లయింట్ అప్లికేషన్లతో సులభంగా ఇంటిగ్రేట్ చేయగల MCP సర్వర్లను సృష్టించడానికి సరళమైన మరియు సమర్థవంతమైన మార్గాన్ని అందిస్తుంది.

## అవలోకనం

ఈ పాఠం stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి MCP సర్వర్లను ఎలా నిర్మించాలో మరియు వినియోగించాలో కవర్ చేస్తుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి MCP సర్వర్‌ను నిర్మించండి.
- Inspector ఉపయోగించి MCP సర్వర్‌ను డీబగ్ చేయండి.
- Visual Studio Code ఉపయోగించి MCP సర్వర్‌ను వినియోగించండి.
- ప్రస్తుత MCP ట్రాన్స్‌పోర్ట్ మెకానిజంలను మరియు stdio ఎందుకు సిఫార్సు చేయబడిందో అర్థం చేసుకోండి.

## stdio ట్రాన్స్‌పోర్ట్ - ఇది ఎలా పనిచేస్తుంది

stdio ట్రాన్స్‌పోర్ట్ ప్రస్తుత MCP స్పెసిఫికేషన్ (2025-06-18)లో మద్దతు పొందిన రెండు ట్రాన్స్‌పోర్ట్ రకాలలో ఒకటి. ఇది ఎలా పనిచేస్తుందో ఇక్కడ ఉంది:

- **సరళమైన కమ్యూనికేషన్**: సర్వర్ స్టాండర్డ్ ఇన్‌పుట్ (`stdin`) నుండి JSON-RPC సందేశాలను చదువుతుంది మరియు స్టాండర్డ్ అవుట్‌పుట్ (`stdout`) కు సందేశాలను పంపుతుంది.
- **ప్రాసెస్ ఆధారిత**: క్లయింట్ MCP సర్వర్‌ను సబ్‌ప్రాసెస్‌గా ప్రారంభిస్తుంది.
- **సందేశ ఫార్మాట్**: సందేశాలు వ్యక్తిగత JSON-RPC అభ్యర్థనలు, నోటిఫికేషన్లు లేదా ప్రతిస్పందనలు, కొత్త లైన్లతో విభజించబడ్డాయి.
- **లాగింగ్**: సర్వర్ లాగింగ్ కోసం స్టాండర్డ్ ఎర్రర్ (`stderr`) కు UTF-8 స్ట్రింగ్స్ రాయవచ్చు.

### ముఖ్యమైన అవసరాలు:
- సందేశాలు కొత్త లైన్లతో విభజించబడాలి మరియు లోపల కొత్త లైన్లు ఉండకూడదు
- సర్వర్ `stdout` కు చెల్లుబాటు అయ్యే MCP సందేశం కాని ఏదీ రాయకూడదు
- క్లయింట్ సర్వర్ యొక్క `stdin` కు చెల్లుబాటు అయ్యే MCP సందేశం కాని ఏదీ రాయకూడదు

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

పైన ఇచ్చిన కోడ్‌లో:

- మేము MCP SDK నుండి `Server` క్లాస్ మరియు `StdioServerTransport` ను దిగుమతి చేసుకుంటాము
- మేము ప్రాథమిక కాన్ఫిగరేషన్ మరియు సామర్థ్యాలతో సర్వర్ ఉదాహరణను సృష్టిస్తాము

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

పైన ఇచ్చిన కోడ్‌లో మేము:

- MCP SDK ఉపయోగించి సర్వర్ ఉదాహరణను సృష్టిస్తాము
- డెకొరేటర్లను ఉపయోగించి టూల్స్ నిర్వచిస్తాము
- ట్రాన్స్‌పోర్ట్‌ను నిర్వహించడానికి stdio_server కాంటెక్స్ట్ మేనేజర్ ఉపయోగిస్తాము

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

SSE నుండి ప్రధాన తేడా stdio సర్వర్లు:

- వెబ్ సర్వర్ సెటప్ లేదా HTTP ఎండ్‌పాయింట్లు అవసరం లేదు
- క్లయింట్ సబ్‌ప్రాసెస్‌లుగా ప్రారంభిస్తారు
- stdin/stdout స్ట్రీమ్స్ ద్వారా కమ్యూనికేట్ చేస్తారు
- అమలు చేయడం మరియు డీబగ్ చేయడం సులభం

## వ్యాయామం: stdio సర్వర్ సృష్టించడం

మా సర్వర్‌ను సృష్టించడానికి, రెండు విషయాలను మనసులో ఉంచుకోవాలి:

- కనెక్షన్ మరియు సందేశాల కోసం ఎండ్‌పాయింట్లను ప్రదర్శించడానికి వెబ్ సర్వర్ ఉపయోగించాలి.

## ప్రయోగశాల: సరళమైన MCP stdio సర్వర్ సృష్టించడం

ఈ ప్రయోగశాలలో, మేము సిఫార్సు చేయబడిన stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి సరళమైన MCP సర్వర్‌ను సృష్టిస్తాము. ఈ సర్వర్ క్లయింట్లు కాల్ చేయగల టూల్స్‌ను ప్రదర్శిస్తుంది, ఇది స్టాండర్డ్ మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ ఉపయోగిస్తుంది.

### ముందస్తు అవసరాలు

- Python 3.8 లేదా తరువాతి సంస్కరణ
- MCP Python SDK: `pip install mcp`
- అసింక్ ప్రోగ్రామింగ్ యొక్క ప్రాథమిక అవగాహన

మొదటి MCP stdio సర్వర్‌ను సృష్టించడం ప్రారంభిద్దాం:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# లాగింగ్‌ను కాన్ఫిగర్ చేయండి
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
    # stdio ట్రాన్స్‌పోర్ట్‌ను ఉపయోగించండి
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## డిప్రికేటెడ్ SSE విధానం నుండి ముఖ్యమైన తేడాలు

**Stdio ట్రాన్స్‌పోర్ట్ (ప్రస్తుత ప్రమాణం):**
- సరళమైన సబ్‌ప్రాసెస్ మోడల్ - క్లయింట్ సర్వర్‌ను చైల్డ్ ప్రాసెస్‌గా ప్రారంభిస్తుంది
- JSON-RPC సందేశాలను ఉపయోగించి stdin/stdout ద్వారా కమ్యూనికేషన్
- HTTP సర్వర్ సెటప్ అవసరం లేదు
- మెరుగైన పనితీరు మరియు భద్రత
- సులభమైన డీబగింగ్ మరియు అభివృద్ధి

**SSE ట్రాన్స్‌పోర్ట్ (MCP 2025-06-18 నుండి డిప్రికేటెడ్):**
- SSE ఎండ్‌పాయింట్లతో HTTP సర్వర్ అవసరం
- వెబ్ సర్వర్ ఇన్‌ఫ్రాస్ట్రక్చర్‌తో మరింత క్లిష్టమైన సెటప్
- HTTP ఎండ్‌పాయింట్ల కోసం అదనపు భద్రతా పరిగణనలు
- ఇప్పుడు వెబ్-ఆధారిత సందర్భాల కోసం స్ట్రీమబుల్ HTTPతో మార్చబడింది

### stdio ట్రాన్స్‌పోర్ట్‌తో సర్వర్ సృష్టించడం

మా stdio సర్వర్‌ను సృష్టించడానికి, మేము:

1. **అవసరమైన లైబ్రరీలను దిగుమతి చేసుకోండి** - MCP సర్వర్ భాగాలు మరియు stdio ట్రాన్స్‌పోర్ట్ అవసరం
2. **సర్వర్ ఉదాహరణను సృష్టించండి** - దాని సామర్థ్యాలతో సర్వర్‌ను నిర్వచించండి
3. **టూల్స్ నిర్వచించండి** - మేము ప్రదర్శించదలచిన ఫంక్షనాలిటీని జోడించండి
4. **ట్రాన్స్‌పోర్ట్‌ను సెటప్ చేయండి** - stdio కమ్యూనికేషన్‌ను కాన్ఫిగర్ చేయండి
5. **సర్వర్‌ను నడపండి** - సర్వర్‌ను ప్రారంభించి సందేశాలను నిర్వహించండి

దీన్ని దశలవారీగా నిర్మిద్దాం:

### దశ 1: ప్రాథమిక stdio సర్వర్ సృష్టించండి

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# లాగింగ్‌ను కాన్ఫిగర్ చేయండి
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

### దశ 2: మరిన్ని టూల్స్ జోడించండి

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

### దశ 3: సర్వర్ నడపడం

కోడ్‌ను `server.py` గా సేవ్ చేసి కమాండ్ లైన్ నుండి నడపండి:

```bash
python server.py
```

సర్వర్ ప్రారంభమై stdin నుండి ఇన్‌పుట్ కోసం వేచి ఉంటుంది. ఇది stdio ట్రాన్స్‌పోర్ట్ ద్వారా JSON-RPC సందేశాలను ఉపయోగించి కమ్యూనికేట్ చేస్తుంది.

### దశ 4: Inspector తో పరీక్షించడం

మీ సర్వర్‌ను MCP Inspector ఉపయోగించి పరీక్షించవచ్చు:

1. Inspector ను ఇన్‌స్టాల్ చేయండి: `npx @modelcontextprotocol/inspector`
2. Inspector ను నడపండి మరియు మీ సర్వర్‌ను పాయింట్ చేయండి
3. మీరు సృష్టించిన టూల్స్‌ను పరీక్షించండి

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## మీ stdio సర్వర్‌ను డీబగ్ చేయడం

### MCP Inspector ఉపయోగించడం

MCP Inspector MCP సర్వర్లను డీబగ్ చేయడానికి మరియు పరీక్షించడానికి విలువైన సాధనం. మీ stdio సర్వర్‌తో దీన్ని ఎలా ఉపయోగించాలో ఇక్కడ ఉంది:

1. **Inspector ను ఇన్‌స్టాల్ చేయండి**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ను నడపండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **మీ సర్వర్‌ను పరీక్షించండి**: Inspector వెబ్ ఇంటర్‌ఫేస్‌ను అందిస్తుంది, అక్కడ మీరు:
   - సర్వర్ సామర్థ్యాలను చూడవచ్చు
   - వివిధ పారామితులతో టూల్స్‌ను పరీక్షించవచ్చు
   - JSON-RPC సందేశాలను మానిటర్ చేయవచ్చు
   - కనెక్షన్ సమస్యలను డీబగ్ చేయవచ్చు

### VS Code ఉపయోగించడం

మీ MCP సర్వర్‌ను నేరుగా VS Code లో కూడా డీబగ్ చేయవచ్చు:

1. `.vscode/launch.json` లో లాంచ్ కాన్ఫిగరేషన్ సృష్టించండి:
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

2. మీ సర్వర్ కోడ్‌లో బ్రేక్‌పాయింట్లు సెట్ చేయండి
3. డీబగ్గర్‌ను నడపండి మరియు Inspector తో పరీక్షించండి

### సాధారణ డీబగింగ్ సూచనలు

- లాగింగ్ కోసం `stderr` ఉపయోగించండి - MCP సందేశాలకు `stdout` ఎప్పుడూ రాయకండి
- అన్ని JSON-RPC సందేశాలు newline-డెలిమిటెడ్ ఉన్నాయో నిర్ధారించండి
- క్లిష్టమైన ఫంక్షనాలిటీ జోడించే ముందు సరళమైన టూల్స్‌తో పరీక్షించండి
- సందేశ ఫార్మాట్లను ధృవీకరించడానికి Inspector ఉపయోగించండి

## VS Code లో మీ stdio సర్వర్‌ను వినియోగించడం

మీ MCP stdio సర్వర్‌ను నిర్మించిన తర్వాత, మీరు దాన్ని VS Code తో ఇంటిగ్రేట్ చేసి Claude లేదా ఇతర MCP-అనుకూల క్లయింట్లతో ఉపయోగించవచ్చు.

### కాన్ఫిగరేషన్

1. Windows లో `%APPDATA%\Claude\claude_desktop_config.json` లేదా Mac లో `~/Library/Application Support/Claude/claude_desktop_config.json` వద్ద MCP కాన్ఫిగరేషన్ ఫైల్ సృష్టించండి:

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

2. **Claude ను రీస్టార్ట్ చేయండి**: కొత్త సర్వర్ కాన్ఫిగరేషన్‌ను లోడ్ చేయడానికి Claude ను మూసి మళ్లీ తెరవండి.

3. **కనెక్షన్‌ను పరీక్షించండి**: Claude తో సంభాషణ ప్రారంభించి మీ సర్వర్ టూల్స్‌ను ఉపయోగించండి:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio సర్వర్ ఉదాహరణ

సూచన కోసం పూర్తి TypeScript ఉదాహరణ ఇక్కడ ఉంది:

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

## సారాంశం

ఈ నవీకరించిన పాఠంలో, మీరు నేర్చుకున్నారు:

- ప్రస్తుత **stdio ట్రాన్స్‌పోర్ట్** (సిఫార్సు చేయబడిన విధానం) ఉపయోగించి MCP సర్వర్లను నిర్మించడం
- SSE ట్రాన్స్‌పోర్ట్ ఎందుకు డిప్రికేటెడ్ అయిందో మరియు stdio మరియు స్ట్రీమబుల్ HTTP ఎందుకు ప్రాధాన్యం పొందాయో అర్థం చేసుకోవడం
- MCP క్లయింట్లు కాల్ చేయగల టూల్స్ సృష్టించడం
- MCP Inspector ఉపయోగించి మీ సర్వర్‌ను డీబగ్ చేయడం
- VS Code మరియు Claude తో మీ stdio సర్వర్‌ను ఇంటిగ్రేట్ చేయడం

stdio ట్రాన్స్‌పోర్ట్ డిప్రికేటెడ్ SSE విధానంతో పోలిస్తే MCP సర్వర్లను నిర్మించడానికి సరళమైన, భద్రతగల, మరియు మెరుగైన పనితీరు కలిగిన మార్గాన్ని అందిస్తుంది. 2025-06-18 స్పెసిఫికేషన్ ప్రకారం ఇది ఎక్కువ MCP సర్వర్ అమలుల కోసం సిఫార్సు చేయబడిన ట్రాన్స్‌పోర్ట్.

### .NET

1. ముందుగా కొన్ని టూల్స్ సృష్టిద్దాం, దీనికోసం *Tools.cs* అనే ఫైల్ క్రింది కంటెంట్‌తో సృష్టిస్తాము:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## వ్యాయామం: మీ stdio సర్వర్‌ను పరీక్షించడం

మీరు stdio సర్వర్‌ను నిర్మించిన తర్వాత, అది సరిగ్గా పనిచేస్తుందో లేదో పరీక్షిద్దాం.

### ముందస్తు అవసరాలు

1. MCP Inspector ఇన్‌స్టాల్ అయి ఉందని నిర్ధారించుకోండి:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. మీ సర్వర్ కోడ్ సేవ్ అయి ఉండాలి (ఉదా: `server.py`)

### Inspector తో పరీక్షించడం

1. **మీ సర్వర్‌తో Inspector ప్రారంభించండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **వెబ్ ఇంటర్‌ఫేస్ తెరవండి**: Inspector మీ సర్వర్ సామర్థ్యాలను చూపించే బ్రౌజర్ విండో తెరుస్తుంది.

3. **టూల్స్‌ను పరీక్షించండి**: 
   - వివిధ పేర్లతో `get_greeting` టూల్ ప్రయత్నించండి
   - వివిధ సంఖ్యలతో `calculate_sum` టూల్ పరీక్షించండి
   - సర్వర్ మెటాడేటాను చూడటానికి `get_server_info` టూల్ కాల్ చేయండి

4. **కమ్యూనికేషన్‌ను మానిటర్ చేయండి**: Inspector క్లయింట్ మరియు సర్వర్ మధ్య మార్పిడీ JSON-RPC సందేశాలను చూపిస్తుంది.

### మీరు చూడవలసినది

మీ సర్వర్ సరిగ్గా ప్రారంభమైనప్పుడు, మీరు చూడగలుగుతారు:
- Inspectorలో సర్వర్ సామర్థ్యాలు జాబితా చేయబడ్డాయి
- పరీక్ష కోసం టూల్స్ అందుబాటులో ఉన్నాయి
- JSON-RPC సందేశాల విజయవంతమైన మార్పిడి
- ఇంటర్‌ఫేస్‌లో టూల్ ప్రతిస్పందనలు ప్రదర్శించబడ్డాయి

### సాధారణ సమస్యలు మరియు పరిష్కారాలు

**సర్వర్ ప్రారంభం కావడం లేదు:**
- అన్ని డిపెండెన్సీలు ఇన్‌స్టాల్ అయ్యాయో చూడండి: `pip install mcp`
- Python సింటాక్స్ మరియు ఇన్డెంటేషన్ తనిఖీ చేయండి
- కన్సోల్‌లో ఎర్రర్ సందేశాలు చూడండి

**టూల్స్ కనిపించడం లేదు:**
- `@server.tool()` డెకొరేటర్లు ఉన్నాయో నిర్ధారించండి
- `main()` ముందు టూల్ ఫంక్షన్లు నిర్వచించబడ్డాయో చూడండి
- సర్వర్ సరిగ్గా కాన్ఫిగర్ అయ్యిందో తనిఖీ చేయండి

**కనెక్షన్ సమస్యలు:**
- సర్వర్ stdio ట్రాన్స్‌పోర్ట్‌ను సరిగ్గా ఉపయోగిస్తున్నదో చూడండి
- ఇతర ప్రాసెస్‌లు జోక్యం చేసుకుంటున్నాయో తనిఖీ చేయండి
- Inspector కమాండ్ సింటాక్స్ సరైనదో చూడండి

## అసైన్‌మెంట్

మీ సర్వర్‌ను మరిన్ని సామర్థ్యాలతో నిర్మించడానికి ప్రయత్నించండి. ఉదాహరణకు, [ఈ పేజీ](https://api.chucknorris.io/) చూడండి, అక్కడ మీరు API కాల్ చేసే టూల్‌ను జోడించవచ్చు. సర్వర్ ఎలా ఉండాలో మీరు నిర్ణయించండి. సరదాగా ఉండండి :)

## పరిష్కారం

[పరిష్కారం](./solution/README.md) ఇక్కడ పని చేసే కోడ్‌తో ఒక సాధ్యమైన పరిష్కారం ఉంది.

## ముఖ్యమైన పాఠాలు

ఈ అధ్యాయం నుండి ముఖ్యమైన పాఠాలు:

- stdio ట్రాన్స్‌పోర్ట్ స్థానిక MCP సర్వర్ల కోసం సిఫార్సు చేయబడిన మెకానిజం.
- stdio ట్రాన్స్‌పోర్ట్ MCP సర్వర్లు మరియు క్లయింట్ల మధ్య స్టాండర్డ్ ఇన్‌పుట్ మరియు అవుట్‌పుట్ స్ట్రీమ్స్ ఉపయోగించి సజావుగా కమ్యూనికేట్ చేయడానికి అనుమతిస్తుంది.
- మీరు Inspector మరియు Visual Studio Code రెండింటినీ ఉపయోగించి stdio సర్వర్లను నేరుగా వినియోగించవచ్చు, ఇది డీబగింగ్ మరియు ఇంటిగ్రేషన్‌ను సులభతరం చేస్తుంది.

## నమూనాలు

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## అదనపు వనరులు

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## తదుపరి ఏమిటి

## తదుపరి దశలు

stdio ట్రాన్స్‌పోర్ట్‌తో MCP సర్వర్లు ఎలా నిర్మించాలో మీరు నేర్చుకున్న తర్వాత, మీరు మరింత అభివృద్ధ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->