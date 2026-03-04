# MCP సర్వర్ stdio ట్రాన్స్‌పోర్ట్‌తో

> **⚠️ ముఖ్యమైన నవీకరణ**: MCP స్పెసిఫికేషన్ 2025-06-18 ప్రకారం, stand-alone SSE (Server-Sent Events) ట్రాన్స్‌పోర్ట్‌ను **పేర్కొనడం నిలిపివేసింది** మరియు "Streamable HTTP" ట్రాన్స్‌పోర్ట్‌తో మార్చింది. ప్రస్తుత MCP స్పెసిఫికేషన్ రెండు ప్రాథమిక ట్రాన్స్‌పోర్ట్ విధానాలను నిర్వచిస్తుంది:
> 1. **stdio** - స్టాండర్డ్ ఇన్‌పుట్/అవుట్పుట్ (స్థానిక సర్వర్‌ల కోసం సూచించబడింది)
> 2. **Streamable HTTP** - SSE ని అంతర్గతంగా ఉపయోగించే రిమోట్ సర్వర్‌ల కోసం
>
> ఈ పాఠం **stdio ట్రాన్స్‌పోర్ట్** పై దృష్టి సారించేలా నవీకరించబడింది, ఇది ఎక్కువ MCP సర్వర్ అమలులకు సూచించిన విధానం.

stdio ట్రాన్స్‌పోర్ట్ MCP సర్వర్‌లు క్లయింట్‌లతో స్టాండర్డ్ ఇన్‌పుట్ మరియు అవుట్పుట్ స్ట్రీమ్ల ద్వారా కమ్యూనికేట్ చేయడానికి అనుమతిస్తుంది. ఈ ప్రస్తుత MCP స్పెసిఫికేషన్‌లో అత్యంత సాధారణంగా ఉపయోగించే మరియు సూచించబడి ట్రాన్స్‌పోర్ట్ విధానం, ఇది వివిధ క్లయింట్ అప్లికేషన్‌లతో సులభంగా సమగ్రపరచదగిన MCP సర్వర్‌లను సృష్టించడానికి సులభమైన మరియు సమర్థవంతమైన మార్గాన్ని అందిస్తుంది.

## అవలోకనం

ఈ పాఠం stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి MCP సర్వర్‌లను ఎలా నిర్మించాలో మరియు వినియోగించాలో కవర్ చేస్తుంది.

## అభ్యసన లక్ష్యాలు

ఈ పాఠం ముగిసిన తర్వాత మీరు చేయగలుగుతారు:

- stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి MCP సర్వర్‌ను నిర్మించండి.
- Inspector ఉపయోగించి MCP సర్వర్‌ను డీబగ్ చేయండి.
- Visual Studio Code ఉపయోగించి MCP సర్వర్‌ను వినియోగించండి.
- ప్రస్తుత MCP ట్రాన్స్‌పోర్ట్ మెకానిజమ్‌లు మరియు ఎందుకు stdio సూచించబడిందో అర్థం చేసుకోండి.

## stdio ట్రాన్స్‌పోర్ట్ - ఇది ఎలా పనిచేస్తుంది

stdio ట్రాన్స్‌పోర్ట్ ప్రస్తుత MCP స్పెసిఫికేషన్ (2025-06-18)లో మద్దతు ఉన్న రెండు ట్రాన్స్‌పోర్ట్ రకాలలో ఒకటి. ఇక్కడ ఇది ఎలా పనిచేస్తుంది:

- **సరళమైన కమ్యూనికేషన్**: సర్వర్ JSON-RPC మెసేజ్‌లను స్టాండర్డ్ ఇన్‌పుట్ (`stdin`) నుండి చదువుము మరియు మెసేజ్‌లను స్టాండర్డ్ అవుట్పుట్ (`stdout`)కి పంపిస్తుంది.
- **ప్రాసెస్ ఆధారిత**: క్లయింట్ MCP సర్వర్‌ను సబ్‌ప్రాసెస్‌గా ప్రారంభిస్తుంది.
- **మెసేజ్ ఫార్మాట్**: మెసేజ్‌లు వ్యక్తిగత JSON-RPC అభ్యర్థనలు, నోటిఫికేషన్‌లు లేదా ప్రతిస్పందనలు, లైన్లుతో విడదీసినవి ఉంటాయి.
- **లాగింగ్**: సర్వర్ లాగింగ్ కోసం స్టాండర్డ్ ఎర్రర్ (`stderr`)కి UTF-8 స్ట్రింగ్స్ రాయవచ్చు.

### ముఖ్యమైన అవసరాలు:
- మెసేజ్‌లు లైన్లుతో తప్పనిసరిగా విడదీసి ఉండాలి మరియు ఎంబెడ్డెడ్ లైన్ల్స్ ఉండకూడదు
- సర్వర్ `stdout`లో చెల్లుబాటు అయ్యే MCP మెసేజ్ కాదని ఏమీ రాసుకోకూడదు
- క్లయింట్ సర్వర్ యొక్క `stdin`కు చెల్లుబాటు అయ్యే MCP మెసేజ్ కాకుండా ఏమీ రాయకూడదు

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

పై కోడులో:

- మేము MCP SDK నుండి `Server` క్లాస్ మరియు `StdioServerTransport`ను ఇంపోర్ట్ చేస్తాము
- సాధారణ కాన్ఫిగరేషన్ మరియు సామర్థ్యాలతో సర్వర్ ఇన్‌స్టెన్స్ తయారు చేస్తాము

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

పై కోడులో:

- MCP SDK ఉపయోగించి సర్వర్ ఇన్‌స్టెన్స్ సృష్టించడం
- డెకొరేటర్ల ద్వారా టూల్స్ నిర్వచించడం
- ట్రాన్స్‌పోర్ట్ నిర్వహించడానికి stdio_server కాంటెక్స్ట్ మేనేజర్ ఉపయోగించడం

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

SSE నుండి ప్రధాన భిన్నత ఏమిటంటే stdio సర్వర్‌లు:

- వెబ్ సర్వర్ సెటప్ లేదా HTTP ఎండ్పాయింట్లు అవసరం లేకుండా
- క్లయింట్ సబ్‌ప్రాసెస్‌లుగా ప్రారంభిస్తారు
- stdin/stdout స్ట్రీముల ద్వారా కమ్యూనికేట్ చేస్తారు
- అమలు చేయడం మరియు డీబగ్ చేయడం సులభంగా ఉంటుంది

## ఆసక్తికర కార్యం: stdio సర్వర్ సృష్టించడం

మా సర్వర్‌ను సృష్టించాలనుకుంటే, రెండింటిని గమనించాలి:

- కనెక్షన్ మరియు మెసేజ్‌ల కోసం ఎండ్పాయింట్లు అందించడానికి వెబ్ సర్వర్ ఉపయోగించాలి.
## ప్రయోగశాల: సులభమైన MCP stdio సర్వర్ సృష్టించడం

ఈ ప్రయోగశాలో, మేము సూచించిన stdio ట్రాన్స్‌పోర్ట్ ఉపయోగించి సులభమైన MCP సర్వర్ సృష్టిస్తాము. ఈ సర్వర్ క్లయింట్‌లు స్టాండర్డ్ మోడెల్ కాంటెక్స్ట్ ప్రోటోకాల్ ఉపయోగించి కాల్ చేయగల టూల్స్‌ను అందిస్తుంది.

### అవసరమైనవి

- Python 3.8 లేదా తర్వాతి వర్షన్
- MCP Python SDK: `pip install mcp`
- అసింక్రన్ ప్రోగ్రామింగ్ గురించి ప్రాథమిక అవగాహన

మొదటి MCP stdio సర్వర్ సృష్టించడం ప్రారంభిద్దాం:

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
    # stdio రవాణా ఉపయోగించండి
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## నిలిపివేసిన SSE విధానంతో కీలక భేదాలు

**Stdio ట్రాన్స్‌పోర్ట్ (ప్రస్తుత ప్రమాణం):**
- సులభమైన సబ్‌ప్రాసెస్ మోడల్ - క్లయింట్ సర్వర్‌ను చైల్డ్ ప్రాసెస్‌గా ప్రారంభిస్తుంది
- stdin/stdout ద్వారా JSON-RPC మెసేజ్‌ల ద్వారా కమ్యూనికేషన్
- HTTP సర్వర్ సెటప్ అవసరం లేదు
- మెరుగైన పనితీరుతో కూడిన భద్రత
- సులభమైన డీబగ్గింగ్ మరియు అభివృద్ధి

**SSE ట్రాన్స్‌పోర్ట్ (MCP 2025-06-18 నుండి నిలిపివేయబడింది):**
- SSE ఎండ్పాయింట్లతో HTTP సర్వర్ అవసరం
- వెబ్ సర్వర్ ఇన్‌ఫ్రాస్ట్రక్చర్‌తో మరింత క్లిష్ట సెటప్
- HTTP ఎండ్పాయింట్ల భద్రతకు అదనపు ఆలోచనలు
- ఇప్పుడు వెబ్-ఆధారిత సన్నివేశాల కోసం Streamable HTTPతో మార్చబడింది

### stdio ట్రాన్స్‌పోర్ట్‌తో సర్వర్ సృష్టించడం

stdio సర్వర్ సృష్టించడానికి, మేము చేయవలసిందిగా:

1. **అవసరమైన లైబ్రరీలు ఇంపోర్ట్ చేయండి** - MCP సర్వర్ కంపోనెంట్లు మరియు stdio ట్రాన్స్‌పోర్ట్ కావాలి
2. **సర్వర్ ఇన్‌స్టెన్స్ సృష్టించండి** - సామర్థ్యాలతో సర్వర్ నిర్వచించండి
3. **టూల్స్ నిర్వచించండి** - ఎక్స్‌పోజ్ చేయవలసిన ఫంక్షనాలిటీని జోడించండి
4. **ట్రాన్స్‌పోర్ట్ సెట్ చేయండి** - stdio కమ్యూనికేషన్‌ను కాన్ఫిగర్ చేయండి
5. **సర్వర్ రన్ చేయండి** - సర్వర్‌ను ప్రారంభించి మెసేజ్‌లను నిర్వహించండి

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

కోడ్‌ను `server.py`గా సేవ్ చేసి, కింద ఎంచిన కమాండ్ లైన్లో నడపండి:

```bash
python server.py
```

సర్వర్ ప్రారంభమవుతుంది మరియు stdin నుండి ఇన్‌పుట్ కోసం ఎదురు చూస్తుంది. ఇది stdio ట్రాన్స్‌పోర్ట్ ద్వారా JSON-RPC మెసేజ్‌లతో కమ్యూనికేట్ చేస్తుంది.

### దశ 4: Inspector తో పరీక్షించడం

మీ సర్వర్‌ను MCP Inspector ఉపయోగించి పరీక్షించవచ్చు:

1. Inspector ను ఇన్‌స్టాల్ చేయండి: `npx @modelcontextprotocol/inspector`
2. Inspector నడిపించి, మీ సర్వర్ వైపు సూచించండి
3. మీరు సృష్టించిన టూల్స్‌ను పరీక్షించండి

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## మీ stdio సర్వర్‌ను డీబగింగ్ చేయడం

### MCP Inspector ఉపయోగించడం

MCP Inspector MCP సర్వర్‌లను డీబగ్ చేయడం మరియు పరీక్షించడం కోసం విలువైన టూల్. మీ stdio సర్వర్‌తో దీన్ని ఎలా ఉపయోగించాలో ఇక్కడ ఉంది:

1. **Inspector ఇన్‌స్టాల్ చేయండి**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector నడపండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **మీ సర్వర్‌ను పరీక్షించండి**: Inspector ఒక వెబ్ ఇంటర్ఫేస్ అందిస్తుంది, సద్వినియోగం చేయగలిగే విధంగా:
   - సర్వర్ సామర్థ్యాలను వీక్షించండి
   - వేరు వేరే పారామీటర్లతో టూల్స్ పరీక్షించండి
   - JSON-RPC మెసేజ్‌లను మానిటర్ చేయండి
   - కనెక్షన్ సమస్యలను డీబగ్ చేయండి

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

2. మీ సర్వర్ కోడులో బ్రేక్ పాయింట్లు సెట్ చేయండి
3. డీబగర్ నడిపించి Inspectorతో పరీక్షించండి

### సాధారణ డీబగింగ్ చిట్కాలు

- లాగింగ్ కోసం `stderr` ఉపయోగించండి - MCP మెసేజ్‌ల కోసం `stdout`ని వ్రాయకండి
- అన్ని JSON-RPC మెసేజ్‌లు లైన్ బ్రేక్‌లతో విడదీయబడినట్లుగా ఉండాలి
- క్లిష్ట ఫంక్షనాలిటీలకు ముందు సరళమైన టూల్స్‌తో పరీక్షించండి
- మెసేజ్ ఫార్మాట్‌లను ధృవీకరించడానికి Inspector ఉపయోగించండి

## VS Code లో మీ stdio సర్వర్‌ను వినియోగించడం

మీ MCP stdio సర్వర్ సృష్టించిన తరువాత, మీరు దీన్ని VS Codeతో ఇంటిగ్రేట్ చేయవచ్చు, Claude లేదా ఇతర MCP అనుకూల క్లయింట్లు ఉపయోగించడానికి.

### కాన్ఫిగరేషన్

1. %APPDATA%\Claude\claude_desktop_config.json (విండోస్) లేదా ~/Library/Application Support/Claude/claude_desktop_config.json (మాక్) వద్ద MCP కాన్ఫిగరేషన్ ఫైల్ సృష్టించండి:

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

2. **Claude‌ను రీస్టార్ట్ చేయండి**: కొత్త సర్వర్ కాన్ఫిగరేషన్ లోడ్ చేసుకోడానికి Claude ని మూసి తిరిగి ఓపెన్ చేయండి.

3. **కనెక్షన్ ని పరీక్షించండి**: Claude తో సంభాషణ మొదలు పెడుతూ మరియు మీ సర్వర్ టూల్స్ ఉపయోగించి చూడండి:
   - "Greeting tool ఉపయోగించి నన్ను గ్రీట్ చేయగలవా?"
   - "15 మరియు 27 యొక్క మొత్తం లెక్కించు"
   - "సర్వర్ సమాచారం ఏమిటి?"

### TypeScript stdio సర్వర్ ఉదాహరణ

ఇది పూర్తి TypeScript ఉదాహరణ కోడ్:

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

// పరికరాలను జోడించండి
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

ఈ నవీకరించిన పాఠంలో మీరు:

- ప్రస్తుత **stdio ట్రాన్స్‌పోర్ట్** ఉపయోగించి MCP సర్వర్‌లు ఎలా నిర్మించాలో నేర్చుకున్నారు (సూచించబడిన విధానం)
- SSE ట్రాన్స్‌పోర్ట్ ఎందుకు నిలిపివేయబడిందో మరియు stdio, Streamable HTTP వల్ల ఎలా మార్చబడిందో అర్థం చేసుకున్నారు
- MCP క్లయింట్‌ల ద్వారా కాల్ చేయబడగల టూల్స్ సృష్టించారు
- MCP Inspector ఉపయోగించి సర్వర్‌ను డీబగ్ చేశారు
- stdio సర్వర్‌ను VS Code మరియు Claudeతో ఇంటిగ్రేట్ చేశారు

stdio ట్రాన్స్‌పోర్ట్ నిలిపివేత SSE విధానంతో పోలిస్తే సులభం, భద్రతగలది, మరియు మెరుగైన పనితీరు కలిగిఉంది. ఇది 2025-06-18 స్పెసిఫికేషన్ నాటి నుండి ఎక్కువ MCP సర్వర్ అమలులకు సూచించబడిన ట్రాన్స్‌పోర్ట్.

### .NET

1. టూల్స్ మొదట సృష్టిద్దాం, దీని కోసం మనం *Tools.cs* అనే ఫైల్ క్రింది కంటెంట్‌తో సృష్టిస్తాము:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## ఆసక్తికర కార్యం: మీ stdio సర్వర్‌ను పరీక్షించడం

మీరు stdio సర్వర్ నిర్మించిన తర్వాత, అది సరిగ్గా పని చేస్తున్నదా అని పరీక్షిద్దాం.

### అవసరమైనవి

1. MCP Inspector ని ఇన్‌స్టాల్ చేశారని నిర్ధారించుకోండి:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. మీ సర్వర్ కోడ్ సేవ్ అయి ఉందా (ఉదా: `server.py`గా)

### Inspector తో పరీక్షించడం

1. **మీ సర్వర్‌తో Inspector ప్రారంభించండి**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **వెబ్ ఇంటర్‌ఫేస్ తెరవండి**: Inspector మీ సర్వర్ సామర్థ్యాలను చూపిస్తూ బ్రౌజర్ విండో తెరవును.

3. **టూల్స్‌ను పరీక్షించండి**:
   - వేరే పేర్లతో `get_greeting` టూల్ ప్రయత్నించండి
   - వివిధ సంఖ్యలతో `calculate_sum` టూల్ పరీక్షించండి
   - సర్వర్ మెటాడేటా చూడటానికి `get_server_info` టూల్ కాల్ చేయండి

4. **కమ్యూనికేషన్‌ను పర్యవేక్షించండి**: Inspector క్లయింట్ మరియు సర్వర్ మధ్య JSON-RPC మెసేజ్‌లు మార్పిడి అవుతున్నాయని చూపిస్తుంది.

### మీరు చూడవలసిందిగా ఏమిటి

మీ సర్వర్ సక్రమంగా ప్రారంభమైతే, మీరు చూడగలవు:
- Inspectorలో సర్వర్ సామర్థ్యాలు
- టెస్టింగ్ కోసం అందుబాటులో ఉన్న టూల్స్
- విజయవంతమైన JSON-RPC మెసేజ్ మార్పిడి
- ఇంటర్ఫేస్‌లో టూల్ స్పందనలు

### సాధారణ సమస్యలు మరియు పరిష్కారాలు

**సర్వర్ మొదలుకాలేదు:**
- అన్ని ఆధారాలు `pip install mcp` ద్వారా ఇన్‌స్టాల్ అయ్యాయా చూడండి
- Python సింటాక్స్ మరియు ఇన్డెంటేషన్ తనిఖీ చేయండి
- కన్‌సోల్‌లో ఎర్రర్ మెసేజ్‌ల కోసం చూడండి

**టూల్స్ కనపడట్లేదు:**
- `@server.tool()` డెకొరేటర్లు ఉన్నాయా ధృవీకరించండి
- `main()`కు ముందు టూల్ ఫంక్షన్లు నిర్వచించబడ్డాయా తనిఖీ చేయండి
- సర్వర్ సరైన కాన్ఫిగరేషన్‌లో ఉన్నదని నిర్ధారించండి

**కనెక్షన్ సమస్యలు:**
- సర్వర్ stdio ట్రాన్స్‌పోర్ట్‌ను సరిగ్గా ఉపయోగిస్తున్నారు అని ధృవీకరించండి
- ఇతర ప్రాసెస్‌లు జోక్యం లేకుండా చూసుకోండి
- Inspector కమాండ్ సింటాక్స్ తనిఖీ చేయండి

## అసైన్‌మెంట్

మీరు మరిన్ని సామర్థ్యాలతో మీ సర్వర్‌ను నిర్మించాలని ప్రయత్నించండి. ఉదాహరణకు, [ఈ పేజీ](https://api.chucknorris.io/)లో ఒక APIను కాల్ చేసే టూల్ జోడించండి. సర్వర్ ఎలా ఉండాలో మీరు నిర్ణయించండి. ఆనందించండి :)

## పరిష్కారం

[పరిష్కారం](./solution/README.md) ఇది ఒక శ్రేయోభిలాషా పరిష్కారం పని చేసే కోడ్‌తో.

## ముఖ్యమైన విషయాలు

ఈ అధ్యాయం నుండి ముఖ్యమైన విషయాలు ఇవి:

- stdio ట్రాన్స్‌పోర్ట్ స్థానిక MCP సర్వర్‌లకు సూచించబడిన మెకానిజం.
- stdio ట్రాన్స్‌పోర్ట్ MCP సర్వర్‌లు మరియు క్లయింట్‌లు స్టాండర్డ్ ఇన్‌పుట్ మరియు అవుట్పుట్ స్ట్రీమ్లను ఉపయోగించి అంతరిరహిత కమ్యూనికేషన్ చేయడానికి అనుమతిస్తుంది.
- మీరు Inspector మరియు Visual Studio Code రెండు ఉపయోగించి stdio సర్వర్‌లను నేరుగా వినియోగించవచ్చు, ఇది డీబగ్గింగ్ మరియు ఇంటిగ్రేషన్‌ను సులభతరం చేస్తుంది.

## నమూనాలు

- [Java కాలిక్యులేటర్](../samples/java/calculator/README.md)
- [.Net కాలిక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [JavaScript కాలిక్యులేటర్](../samples/javascript/README.md)
- [TypeScript కాలిక్యులేటర్](../samples/typescript/README.md)
- [Python కాలిక్యులేటర్](../../../../03-GettingStarted/samples/python)

## అదనపు వనరులు

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## తదుపరి

## తదుపరి దశలు

stdio ట్రాన్స్‌పోర్ట్‌తో MCP సర్వర్‌లను నిర్మించడం నేర్చుకున్న తరువాత, మీరు మరింత అధునాతన విషయాలను అన్వేషించవచ్చు:

- **తదుపరి**: [MCP తో HTTP స్ట్రీమింగ్ (Streamable HTTP)](../06-http-streaming/README.md) - రిమోట్ సర్వర్‌ల కోసం మద్దతు ఉన్న మరో ట్రాన్స్‌పోర్ట్ మెకానిజంకు సంబంధించినది
- **అధునాతన**: [MCP భద్రత ఉత్తమ పద్ధతులు](../../02-Security/README.md) - మీ MCP సర్వర్‌లలో భద్రతను అమలు చేయండి
- **ఉత్పత్తి కావటం**: [డిప్లాయ్‌మెంట్ వ్యూహాలు](../09-deployment/README.md) - ఉత్పత్తి వాడుకోడానికి సర్వర్‌లను డిప్లాయ్ చేయండి

## అదనపు వనరులు

- [MCP స్పెసిఫికేషన్ 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - అధికారిక స్పెసిఫికేషన్
- [MCP SDK డాక్యుమెంటేషన్](https://github.com/modelcontextprotocol/sdk) - అన్ని భాషలకు SDK రిఫరెన్సులు
- [కమ్యూనిటీ ఉదాహరణలు](../../06-CommunityContributions/README.md) - కమ్యూనిటీ నుండి మరింత సర్వర్ ఉదాహరణలు

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్ట DISCLAIMER**:  
ఈ డాక్యుమెంట్ AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వాన్ని లక్ష్యంగా పెట్టుకున్నప్పటికీ, ఆటోమేటిక్ అనువాదాల్లో పొ/errorsలు లేదా అసత్యతలు ఉండవచ్చు. అసలు డాక్యుమెంట్ ద్విపాక్షిక భాషలో ఉన్నది అధికారిక మూలంగా పరిగణించాలి. కీలక సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదం చేయించడం సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగించి కలిగే ఏవైనా తప్పుదోవలందకాలు లేదా తప్పుదోహతలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->