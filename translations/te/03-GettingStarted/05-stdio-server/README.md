# stdio ట్రాన్స్‌పోర్ట్‌తో MCP సర్వర్

> **⚠️ ముఖ్యమైన అప్‌డేట్**: MCP స్పెసిఫికేషన్ 2025-06-18 నుండి, స్టాండ్లోన్ SSE (సర్వర్-సెంటెడ్ ఈవెంట్స్) ట్రాన్స్‌పోర్ట్ **డిప్రీకేటెడ్** కాగా, దాని స్థానంలో "స్ట్రీమబుల్ HTTP" ట్రాన్స్‌పోర్ట్ వచ్చేసింది. ప్రస్తుత MCP స్పెసిఫికేషన్ రెండు ప్రధాన ట్రాన్స్‌పోర్ట్ మెకానిజమ్‌లను నిర్వచిస్తుంది:
> 1. **stdio** - స్టాండర్డ్ ఇన్‌పుట్/ఔట్‌పుట్ (లోకల్ సర్వర్లకు సిఫార్సు చేయబడింది)
> 2. **స్ట్రీమబుల్ HTTP** - SSE అంతర్గతంగా ఉపయోగించే రిమోట్ సర్వర్లకు
>
> ఈ పాఠం ఎక్కువగా **stdio ట్రాన్స్‌పోర్ట్** పై కేంద్రీకరించబడింది, ఇది చాలా MCP సర్వర్ అమలులో సిఫార్సు చేసిన విధానం.

stdio ట్రాన్స్‌పోర్ట్ MCP సర్వర్లను కస్టమర్లతో స్టాండర్డ్ ఇన్‌పుట్ మరియు ఔట్‌పుట్ స్ట్రీమ్‌ల ద్వారా కమ్యూనికేట్ చేయడానికి అనుమతిస్తుంది. ఇది ప్రస్తుత MCP స్పెసిఫికేషన్‌లో అత్యంత సాధారణంగా వాడే మరియు సిఫార్సు చేయబడిన ట్రాన్స్‌పోర్ట్ మెకానిజం, ఇది విభిన్న కస్టమర్ అప్లికేషన్‌లతో సులభంగా ఏకీకృతం కాన MCP సర్వర్లను నిర్మించడానికి సరళమైన, సమర్థవంతమైన మార్గాన్ని అందిస్తుంది.

## సమీక్ష

ఈ పాఠం stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి MCP సర్వర్లను ఎలా నిర్మించాలి మరియు వినియోగించాలి అనే అంశాన్ని కవర్చేస్తుంది.

## నేర్చుకోవాల్సిన లక్ష్యాలు

ఈ పాఠం ముగింపులో మీరు చేయగలుగుతారు:

- stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి MCP సర్వర్ నిర్మించడం.
- ఇన్‌స్పెక్టర్ ఉపయోగించి MCP సర్వర్ డీబగ్గింగ్ చేయడం.
- Visual Studio Code ఉపయోగించి MCP సర్వర్ వినియోగించడం.
- ప్రస్తుత MCP ట్రాన్స్‌పోర్ట్ మెకానిజమ్‌లు మరియు stdio ఎందుకు సిఫార్సు చేయబడిందో అర్థం చేసుకోవడం.


## stdio ట్రాన్స్‌పోర్ట్ - ఇది ఎలా పనిచేస్తుంది

stdio ట్రాన్స్‌పోర్ట్ MCP స్పెసిఫికేషన్ `2026-07-28` లో రెండు ప్రామాణిక ట్రాన్స్‌పోర్ట్లలో ఒకటి. ఇది ఎలా పనిచేస్తుందో ఇలా ఉంది:


- **సరళమైన కమ్యూనికేషన్**: సర్వర్ స్టాండర్డ ఇన్‌పుట్ (`stdin`) నుండి JSON-RPC సందేశాలు చదువుతుంది మరియు స్టాండర్డ్ ఔట్‌పుట్ (`stdout`) కు సందేశాలు పంపుతుంది.
- **ప్రొసెస్-ఆధారిత**: కస్టమర్ MCP సర్వర్‌ను సబ్‌ప్రొసెస్‌గా ప్రారంభిస్తుంది.
- **సందేశ ఫార్మాట్**: సందేశాలు వ్యక్తిగత JSON-RPC అభ్యర్థనలు, నోటిఫికేషన్లు లేదా ప్రత్యుత్తరాలు, న్యూలైన్స్ ద్వారా వేరుచేయబడతాయి.
- **లాగింగ్**: సర్వర్ లాగింగ్ కోసం UTF-8 స్ట్రింగులను స్టాండర్డ్ ఎర్రర్ (`stderr`) కు రాస్తూ ఉండవచ్చు.

### కీలక అవసరాలు:
- సందేశాలు తప్పనిసరిగా న్యూలైన్స్ ద్వారా వేరుచేయబడాలి మరియు న్యూలైన్‌లు లోపల ఉండకూడదు.
- సర్వర్ `stdout` కు సరైన MCP సందేశం కాకుండా ఏదీ రాయకూడదు.
- క్లయింట్ సర్వర్ యొక్క `stdin` కు సరైన MCP సందేశం కాకుండా ఏదీ రాయకూడదు.

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

పూర్వ కోడ్‌లో:

- మేము MCP SDK నుండి `Server` క్లాస్ మరియు `StdioServerTransport` ను దిగుమతి చేసుకోాము
- మేము ప్రాథమిక కాన్ఫిగరేషన్ మరియు సామర్థ్యాలతో సర్వర్ ఉదాహరణను సృష్టించాము
- `StdioServerTransport` ఉదాహరణను సృష్టించి సర్వర్‌ను దీనితో కనెక్ట్ చేసి, stdin/stdout ద్వారా కమ్యూనికేషన్ సక్రియం చేసాము

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

పూర్వ కోడ్‌లో మేము:

- MCP SDK ఉపయోగించి సర్వర్ ఉదాహరణను సృష్టించాము
- డెకొరేటర్లను ఉపయోగించి టూల్స్ నిర్వచించాము
- ట్రాన్స్‌పోర్ట్‌ను నిర్వహించేందుకు stdio_server కాంటెక్స్ట్ మేనేజర్ ఉపయోగించాము

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

SSE నుండి ప్రధాన తేడా stdio సర్వర్‌లు:

- వెబ్ సర్వర్ సెటప్ లేదా HTTP ఎండ్‌పాయింట్‌లను అవసరం కావు
- క్లయింట్ సబ్‌ప్రొసెస్‌లుగా ప్రారంభిస్తారు
- stdin/stdout స్ట్రీమ్స్ ద్వారా కమ్యూనికేట్ చేస్తారు
- అమలు చేయడం మరియు డీబగ్ చేయడం సులభం

## వ్యాయామం: stdio సర్వర్ సృష్టించడం

మా సర్వర్ సృష్టించడానికి, రెండు విషయాలను గుర్తుంచుకోండి:

- కనెక్షన్ మరియు సందేశాల కోసం ఎండ్‌పాయింట్‌లను బయటపెట్టడానికి వెబ్ సర్వర్ ఉపయోగించాలి.
## ల్యాబ్: సింపుల్ MCP stdio సర్వర్ సృష్టించడం


ఈ ప్రయోగశాలలో, మేము సిఫారసు చేసిన stdio ట్రాన్స్పోర్ట్ ఉపయోగించి ఒక సరళమైన MCP సర్వర్‌ను సృష్టించబోతున్నాము. ఈ సర్వర్ కస్టమర్లు ప్రామాణిక Model Context Protocol ఉపయోగించి కాల్ చేయగల సాధనాలను అందిస్తుంది.

### ముందస్తు అవసరాలు

- Python 3.8 లేదా తరువాత
- MCP Python SDK: `pip install mcp`
- అసింక్రనస్ ప్రోగ్రామింగ్ యొక్క ప్రాథమిక అవగాహన

మనం మన మొదటి MCP stdio సర్వర్ సృష్టించడం ప్రారంభిద్దాము:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# లాగింగ్‌ను కన్ఫిగర్ చేయండి
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
    # stdio ట్రాన్స్పోర్ట్‌ను ఉపయోగించండి
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## పాత SSE విధానం నుండి ముఖ్య తేడాలు

**Stdio ట్రాన్స్పోర్ట్ (ప్రస్తుత ప్రమాణం):**
- సరళమైన సబ్రోసెస్ మోడల్ - క్లయింట్ సర్వర్ను చైల్డ్ ప్రాసెస్‌గా ప్రారంభిస్తుంది
- JSON-RPC సందేశాలను ఉపయోగించి stdin/stdout ద్వారా సంభాషణ
- HTTP సర్వర్ సెటప్ అవసరం లేదు
- మెరుగైన పనితీరు మరియు భద్రత
- సులువు డీబగ్గింగ్ మరియు అభివృద్ధి

**SSE ట్రాన్స్పోర్ట్ (MCP 2025-06-18 నుండి పాతవైంది):**
- SSE ఎండ్‌పాయింట్లు ఉన్న HTTP సర్వర్ అవసరం
- వెబ్ సర్వర్ ఇన్‌ఫ్రాస్ట్రక్చర్‌తో ఎక్కువ సంక్లిష్ట సెటప్
- HTTP ఎండ్‌పాయింట్ల కోసం అదనపు భద్రతా పరిగణనలు
- ఇప్పుడు వెబ్ ఆధారిత సందర్భాలకు Streamable HTTP ద్వారా మార్చబడింది

### stdio ట్రాన్స్పోర్ట్ తో సర్వర్ సృష్టించడం

మన stdio సర్వర్ సృష్టించడానికి, మనం చేయాల్సింది:

1. **అవసరమైన లైబ్రరీలను దిగుమతి చేసుకోండి** - మనకు MCP సర్వర్ భాగాలు మరియు stdio ట్రాన్స్పోర్ట్ అవసరం
2. **సర్వర్ ను సృష్టించండి** - సర్వర్ మరియు దాని సామర్థ్యాలను నిర్వచించండి
3. **సాధనాలు నిర్వచించండి** - మనం అందించాలనుకునే ఫంక్షనాలిటీని జోడించండి
4. **ట్రాన్స్పోర్ట్ సెట్ చేయండి** - stdio కమ్యూనికేషన్‌ను కాన్ఫిగర్ చేయండి
5. **సర్వర్ నడపండి** - సర్వర్ ప్రారంభించి సందేశాలను నిర్వహించండి

మనం దాన్ని ఒక్కొక్క దశగా నిర్మిద్దాము:

### దశ 1: ఒక ప్రాథమిక stdio సర్వర్ సృష్టించండి

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# లాగింగ్‌ని అమర్చండి
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

### దశ 2: మరిన్ని సాధనాలు జోడించండి

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

కోడ్‌ని `server.py`గా సేవ్ చేసి కమాండ్ లైన్ నుండి నడిపించండి:

```bash
python server.py
```

సర్వర్ ప్రారంభమై stdin నుండి ఇన్‌పుట్ కోసం వేచి ఉంటుంది. ఇది stdio ట్రాన్స్పోర్ట్‌ ద్వారా JSON-RPC సందేశాలను ఉపయోగించి సంభాషిస్తుంది.

### దశ 4: ఇన్స్పెక్టర్ తో పరీక్షించడం

మీరు MCP ఇన్స్పెక్టర్ ఉపయోగించి మీ సర్వర్‌ను పరీక్షించవచ్చు:

1. ఇన్స్పెక్టర్ ఇన్స్టాల్ చేయండి: `npx @modelcontextprotocol/inspector`
2. ఇన్స్పెక్టర్ నడపండి మరియు దాన్ని మీ సర్వర్‌కి పాయింట్ చేయండి
3. మీరు సృష్టించిన సాధనాలను పరీక్షించండి

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## మీ stdio సర్వర్‌ను డీబగ్ చేయడం

### MCP ఇన్స్పెక్టర్ ఉపయోగించడం

MCP ఇన్స్పెక్టర్ MCP సర్వర్లను డీబగ్గింగ్ మరియు పరీక్షించడానికి విలువైన సాధనం. మీరు దాన్ని మీ stdio సర్వర్‌తో ఎలా ఉపయోగించాలో ఇక్కడ ఉంది:

1. **ఇన్స్పెక్టర్ ఇన్స్టాల్ చేయండి**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **ఇన్స్పెక్టర్ నడపండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **మీ సర్వర్‌ను పరీక్షించండి**: ఇన్స్పెక్టర్ ఒక వెబ్ ఇంటర్ఫేస్ అందిస్తుంది, అక్కడ మీరు:
   - సర్వర్ సామర్థ్యాలను చూడవచ్చు
   - వేరువేరుగా ప్యారామీటర్లతో సాధనాలను పరీక్షించవచ్చు
   - JSON-RPC సందేశాలను పర్యవేక్షించవచ్చు
   - కనెక్షన్ సమస్యలను డీబగ్ చేయవచ్చు

### VS కోడ్ ఉపయోగించడం

మీరు కూడా మీ MCP సర్వర్‌ను నేరుగా VS Codeలో డీబగ్ చేయవచ్చు:

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

2. మీ సర్వర్ కోడ్‌లో బ్రేక్‌పాయింట్లు సెట్ చేయండి
3. డీబగ్గర్ నడపండి మరియు ఇన్స్పెక్టర్‌తో పరీక్షించండి

### సాధారణ డీబగ్గింగ్ సూచనలు

- లాగ్స్ కోసం `stderr` ఉపయోగించండి - MCP సందేశాలకు `stdout` ఉపయోగించవద్దు
- అన్ని JSON-RPC సందేశాలు కొత్త లైన్‌తో విభజించబడి ఉండాలి
- సంక్లిష్ట ఫంక్షనాలిటీ జోడించే ముందు సరళమైన సాధనాలతో పరీక్షించండి

- సందేశ రూపరేఖలను ధృవీకరించడానికి ఇన్‌స్పెక్టర్‌ను ఉపయోగించండి

## VS కోడ్‌లో మీ stdio సర్వర్‌ను వినియోగించడం


మీరు మీ MCP stdio సర్వర్‌ని నిర్మించిన తర్వాత, దానిని VS కోడ్‌తో ఇంటిగ్రేట్ చేసి, దానిని Claude లేదా ఇతర MCP-అనుకూల క్లయింట్లు ఉపయోగించడానికి ఉపయోగించవచ్చు.

### కాన్ఫిగరేషన్

1. **MCP కాన్ఫిగరేషన్ ఫైల్ సృష్టించండి** `%APPDATA%\Claude\claude_desktop_config.json` (విండోస్) లేదా `~/Library/Application Support/Claude/claude_desktop_config.json` (మాక్) వద్ద:

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

2. **Claude ను రీస్టార్ట్ చేయండి**: కొత్త సర్వర్ కాన్ఫిగరేషన్‌ను లోడ్ చేసుకోవడానికి Claude ను ముగించి మళ్లీ తెరవండి.

3. **కనెక్షన్‌ని పరీక్షించండి**: Claude తో సంభాషణ మొదలుపెట్టి మీ సర్వర్ టూల్స్ ఉపయోగించండి:
   - "మీరు గ్రీటింగ్ టూల్ ఉపయోగించి నాకు అంగీకరించగలరా?"
   - "15 మరియు 27 యొక్క జమ చేయి లెక్కించండి"
   - "సర్వర్ సమాచారం ఏమిటి?"

### టైప్‌స్క్రిప్ట్ stdio సర్వర్ ఉదాహరణ

సూచన కోసం పూర్తి టైప్‌స్క్రిప్ట్ ఉదాహరణ ఇస్తున్నాము:

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

// సాధనాలను జత చేయండి
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

ఈ నవీకరించబడిన పాఠంలో మీరు నేర్చుకున్న విషయాలు:

- ప్రస్తుత **stdio ట్రాన్స్‌పోర్ట్** ఉపయోగించి MCP సర్వర్లను నిర్మించడం (సిఫారసు చేసిన పద్ధతి)
- SSE ట్రాన్స్‌పోర్ట్ ఎందుకు stdio మరియు Streamable HTTP కి భర్తీ అయింది అనుభవం
- MCP క్లయింట్లు పిలవగల టూల్స్ రూపొందించడం
- MCP ఇన్‌స్పెక్టర్ ఉపయోగించి మీ సర్వర్‌ను డీబగ్ చేయడం
- మీ stdio సర్వర్‌ను VS కోడ్ మరియు Claude తో ఇంటిగ్రేట్ చేయడం

stdio ట్రాన్స్‌పోర్ట్ deprecated అయిన SSE పద్ధతితో పోల్చుకుంటే ఒక సులభమైన, మరింత సురక్షితమైన మరియు మెరుగైన పనితీరు కలిగిన పద్ధతి MCP సర్వర్లను నిర్మించడానికి. ఇది 2025-06-18 స్పెసిఫికేషన్ ప్రకారం చాలా MCP సర్వర్ అమలు క‌ల‌కి సిఫారసు చేయబడిన ట్రాన్స్‌పోర్ట్.


### .NET

1. ముందుగా కొన్ని టూల్స్ సృష్టిద్దాం, దీని కోసం *Tools.cs* అనే ఫైల్ క్రింద పేర్కొన్న కంటెంట్‌తో తయారుచేస్తాము:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## వ్యాయామం: మీ stdio సర్వర్‌ని పరీక్షించడం

మీరు మీ stdio సర్వర్‌ని నిర్మించిన తర్వాత, దాని సక్రమంగా పనిచేస్తుందా అని పరీక్షిద్దాం.

### ముందస్తు అవసరాలు

1. మీరు MCP ఇన్‌స్పెక్టర్ ఇన్‌స్టాల్ చేసి ఉన్నారా అని నిర్ధారించుకోండి:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. మీ సర్వర్ కోడ్ సేవ్ చేసి ఉంచాలి (ఉదా., `server.py` గా)

### ఇన్‌స్పెక్టర్ తో పరీక్షించడం

1. **మీ సర్వర్‌తో ఇన్‌స్పెక్టర్ ప్రారంభించండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **వెబ్ ఇంటర్‌ఫేస్‌ను తెరవండి**: ఇన్‌స్పెక్టర్ మీ సర్వర్ సామర్థ్యాలను చూపిస్తూ బ్రౌజర్ విండో తెరవుతుంది.

3. **టూల్స్‌ని పరీక్షించండి**: 
   - వివిధ పేర్లతో `get_greeting` టూల్ ప్రయత్నించండి
   - వేర్వేరు సంఖ్యలతో `calculate_sum` టూల్‌ని పరీక్షించండి
   - సర్వర్ మెటాడేటా చూడటానికి `get_server_info` టూల్‌ కాల్ చేయండి

4. **కమ్యూనికేషన్‌ని మానిటర్ చేయండి**: ఇన్‌స్పెక్టర్ క్లయింట్ మరియు సర్వర్ మధ్య మార్పిడి అయ్యే JSON-RPC సందేశాలను చూపిస్తుంది.

### మీరు చూడవలసినది

మీ సర్వర్ సక్రమంగా ప్రారంభించబడినప్పుడు మీరు చూడవలసింది:
- ఇన్‌స్పెక్టర్‌లో సర్వర్ సామర్థ్యాలు జాబితా
- పరీక్షించడానికి టూల్స్ అందుబాటులో ఉండడం
- విజయవంతమైన JSON-RPC సందేశ మార్పిడి
- ఇంటర్‌ఫేస్‌లో టూల్ ప్రతిస్పందనలు ప్రదర్శన

### సాధారణ సమస్యలు మరియు పరిష్కారాలు

**సర్వర్ ప్రారంభించట్లేదు:**
- అన్ని ఆధారాలు ఇన్‌స్టాల్ చేసినదాని ధృవపరిచండి: `pip install mcp`
- Python సింటాక్స్ మరియు ఇండెంటేషన్‌ను తనిఖీ చేయండి
- కన్సోల్ లో ఎర్రర్ సందేశాలు చూసండి

**టూల్స్ కనపడటం లేదు:**
- `@server.tool()` డెకరేటర్లు ఉన్నాయని నిర్ధారించుకోండి
- `main()` ముందు టూల్ ఫంక్షన్లు నిర్వచించబడినాయో చూడండి
- సర్వర్ సరిగ్గా కాన్ఫిగర్ చేయబడిందా అన్నది పరిశీలించండి

**కనెక్షన్ సమస్యలు:**
- సర్వర్ stdio ట్రాన్స్‌పోర్ట్ సరైనంగా ఉపయోగిస్తున్నదా అనేది చూసుకోండి
- ఇతర ప్రాసెస్‌లు జోక్యం కాకుండా చూసుకోండి
- ఇన్‌స్పెక్టర్ కమాండ్ సింటాక్స్‌ను ధృవీకరించండి

## అసైన్మెంట్

మీ సర్వర్‌ను మరిన్ని సామర్థ్యాలతో నిర్మించి చూడండి. ఉదాహరణకు, API ని పిలుస్తున్న టూల్‌ని జోడించడానికి [ఈ పేజీ](https://api.chucknorris.io/) చూడండి. సర్వర్ ఎలా ఉండాలన్నదిని మీరు నిర్ణయించండి. సంతోషంగా కొనసాగండి :)
## పరిష్కారం

[పరిష్కారం](./solution/README.md) పని చేస్తున్న కోడ్‌తో కూడిన ఒక సాధ్యమైన పరిష్కారం ఇక్కడ ఉంది.

## ముఖ్యమైన పాఠాలు

ఈ అధ్యాయం నుండి ముఖ్యంగా నేర్చుకున్న విషయాలు:

- stdio ట్రాన్స్‌పోర్ట్ స్థానిక MCP సర్వర్ల కోసం సిఫారసు చేసిన పద్ధతి.
- stdio ట్రాన్స్‌పోర్ట్ MCP సర్వర్లు మరియు క్లయింట్లు మధ్య సజావుగా కమ్యూనికేషన్ ఏర్పరుచుకోవడానికి స్టాండర్డ్ ఇన్‌పుట్ మరియు అవుట్‌పుట్ స్ట్రీమ్‌లను ఉపయోగిస్తుంది.
- మీరు ఇన్‌స్పెక్టర్ మరియు విజువల్ స్టూడియో కోడ్ రెండింటినీ ఉపయోగించి stdio సర్వర్లను డైరెక్ట్‌గా ఉపయోగించవచ్చు, తద్వారా డీబగ్గింగ్ మరియు ఇంటిగ్రేషన్ సులభం అవుతుంది.

## నమూనాలు

- [జావా క్యాలిక్యులేటర్](../samples/java/calculator/README.md)
- [.Net క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [జావాస్క్రిప్ట్ క్యాలిక్యులేటర్](../samples/javascript/README.md)
- [టైప్‌స్క్రిప్ట్ క్యాలిక్యులేటర్](../samples/typescript/README.md)
- [పైథాన్ క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/python) 

## అదనపు వనరులు

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## తరువాత ఏమిటి

## తరువాతి దశలు

stdio ట్రాన్స్‌పోర్ట్‌తో MCP సర్వర్లను నిర్మించడాన్ని నేర్చుకున్న తర్వాత, మీరు మరింత అభివృద్ధి చెందిన అంశాలను అన్వేషించవచ్చు:

- **తదుపరి**: [MCP తో HTTP స్ట్రీమింగ్ (Streamable HTTP)](../06-http-streaming/README.md) - రిమోట్ సర్వర్ల కోసం మద్దతు ఉన్న పద్ధతి గురించి తెలుసుకోండి
- **అధిక**: [MCP భద్రత గానే ప్రాక్టీసులు](../../02-Security/README.md) - మీ MCP సర్వర్లలో భద్రత అమలు చేయండి
- **ఉత్పత్తి**: [డిప్లాయ్‌మెంట్ వ్యూహాలు](../09-deployment/README.md) - ఉత్పత్తి ఉపయోగానికి మీ సర్వర్లను డిప్లాయ్ చేయండి

## అదనపు వనరులు

- [MCP స్పెసిఫికేషన్ 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - ప్రస్తుత స్పెసిఫికేషన్
- [MCP SDK డాక్యుమెంటేషన్](https://github.com/modelcontextprotocol/sdk) - అన్ని భాషల కోసం SDK సూచనలు
- [సమాజాన్ని ఉదాహరణలు](../../06-CommunityContributions/README.md) - సమాజం నుండి మరిన్ని సర్వర్ ఉదాహరణలు

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->