# stdio போக்குவரத்துடன் MCP சேவையகம்

> **⚠️ முக்கியமான புதுப்பிப்பு**: MCP நெறிமுறை 2025-06-18 முதல், தனித்தனி SSE (Server-Sent Events) போக்குவரத்து **பழையதாக** மாறி "Streamable HTTP" போக்குவரத்தால் மாற்றப்பட்டுள்ளது. தற்போதைய MCP நெறிமுறை இரண்டு முக்கிய போக்குவரத்து முறைகளை வரையறுக்கிறது:
> 1. **stdio** - நிலையான உள்ளீடு/வெளியீடு (உள்ளூர் சேவையகங்களுக்கு பரிந்துரைக்கப்படுகிறது)
> 2. **Streamable HTTP** - பின்முகமாக SSE உட்பட உபயோகிக்கும் தொலைதூர சேவையகங்களுக்கு
>
> இந்த பாடம் **stdio போக்குவரத்து**-ஆற்கான கவனத்தை மாற்றி, பெரும்பாலும் MCP சேவையகமான்களுக்கான பரிந்துரையான முறையாக உள்ளது.

stdio போக்குவரத்து MCP சேவையகங்கள் பொதுவாக உள்ளீடு மற்றும் வெளியீடு ஓடுபாதைகள் மூலம் கிளையன்ட்களுடன் தொடர்பு கொள்கிறது. இது தற்போதைய MCP நெறிமுறையில் அதிகம் பயன்படுத்தப்படும் மற்றும் பரிந்துரைக்கப்படும் போக்குவரத்து முறைமை ஆகும், எளிய மற்றும் திறமையான முறையில் MCP சேவையகங்களை உருவாக்க அனுமதிக்கிறது, பலவகையான கிளையன்ட் பயன்பாடுகளோடு எளிதில் ஒன்று சேர்க்கக்கூடியது.

## கண்ணோட்டம்

இந்த பாடம் stdio போக்குவரத்தைப் பயன்படுத்தி MCP சேவையகங்களை எப்படி உருவாக்கி பயன்படுத்துவது என்பதைக் கற்றுக் கொடுக்கிறது.

## கற்றல் இலக்குகள்

இந்த பாடம் முடிவில் நீங்கள்:

- stdio போக்குவரத்தை பயன்படுத்தி MCP சேவையகத்தை உருவாக்க முடியும்.
- Inspector ஐப் பயன்படுத்தி MCP சேவையகத்தை டீபக் செய்ய முடியும்.
- Visual Studio Code மூலம் MCP சேவையகத்தை நுகர முடியும்.
- தற்போதைய MCP போக்குவரத்து முறைகளையும் stdio ஏன் பரிந்துரைக்கப்படுகிறது என்பதையும் புரிந்து கொள்ள முடியும்.


## stdio போக்குவரத்து - அது எப்படி வேலை செய்கிறது

stdio போக்குவரத்து MCP நிர்ணயத்தில் இரண்டு நிலையான போக்குவரத்துகளில் ஒன்றாகும்
`2026-07-28`. இது எவ்வாறு செயல்படுகிறது:

- **எளிய தொடர்பு**: சேவையகம் JSON-RPC செய்திகளை நிலையான உள்ளீடு (`stdin`) இலிருந்து படித்து நிலையான வெளியீடு (`stdout`) க்கு அனுப்பும்.
- **செயல்முறை அடிப்படையிலானது**: கிளையன்ட் MCP சேவையகத்தை துணை செயலியாகத் துவக்குகிறது.
- **செய்தி வடிவம்**: செய்திகள் தனிப்பட்ட JSON-RPC கோரிக்கைகள், அறிவிப்புகள் அல்லது பதில்கள், வரிசையில் கருதி பிரிக்கப்பட்டவை.
- **லாகிங்**: சேவையகம் பதிவு நோக்கத்திற்காக நிலையான பிழை வெளியீடு (`stderr`)-க்கு UTF-8 ஸ்டிரிங்களை எழுதலாம்.

### முக்கிய தேவைகள்:
- செய்திகள் வரிசைபடுத்தப்பட்ட வரிகள் மூலம் பிரிக்கப்பட்டிருக்க வேண்டும் மற்றும் உள்ளிடப்பட்ட வரிகளை கொண்டிருக்க கூடாது
- சேவையகம் `stdout`-க்கு செல்லுபடியாகும் MCP செய்தியல்லாத எதையும் எழுதக் கூடாது
- கிளையன்ட் சேவையகத்தின் `stdin`-க்கு செல்லுபடியாகும் MCP செய்தியல்லாத எதையும் எழுதக் கூடாது

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

முன்னோட்டக் கோடுகளில்:

- MCP SDK இல் இருந்து `Server` வகுப்பும் `StdioServerTransport`-ஐ இறக்குமதி செய்கிறோம்
- அடிப்படை உள்ளமைவு மற்றும் திறன்களுடன் சேவையக ஓர் உருவாக்குகிறோம்
- `StdioServerTransport` உருவாக்கி அதன் மூலம் சேவையகத்தை இணைத்துக் கொள்ள, stdin/stdout மூலம் தொடர்பு ஏற்பட அனுமதிக்கிறோம்

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# சர்வர் உதாரணத்தை உருவாக்கவும்
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

முன்னோட்டக் கோடுகளில் நாம்:

- MCP SDK பயன்படுத்தி சேவையக உருவாக்குகிறோம்
- அலங்காரிகளில் கருவிகள் வரையறுக்கின்றோம்
- போக்குவரத்தை கையாள stdio_server சூழல் மேலாளர் பயன்படுத்துகிறோம்

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

SSE உடன் முக்கிய வேறுபாடு stdio சேவையகங்கள்:

- வலை சேவையகம் அமைப்பு அல்லது HTTP முனைகளுக்கு தேவையில்லை
- கிளையன்ட் மூலம் துணை செயலிகளில் துவக்கப்படுகின்றன
- stdin/stdout ஓடுபாதைகளில் தொடர்பு கொள்கின்றன
- எளிதாக நிறைவேற்றவும் டீபக் செய்யவும் முடியும்

## பயிற்சி: stdio சேவையகம் உருவாக்கல்

சேவையகத்தை உருவாக்க நாம் இரண்டு விஷயங்களை நினைவில் வைக்க வேண்டும்:

- இணைப்பு மற்றும் செய்திகளுக்கான முனைகளை வெளிப்படுத்த வலை சேவையகத்தை பயன்படுத்த வேண்டும்.
## ஆய்வு: எளிய MCP stdio சேவையக உருவாக்கம்

இந்த ஆய்வில், பரிந்துரைக்கப்படும் stdio போக்குவரத்தைப் பயன்படுத்தி எளிய MCP சேவையகத்தை உருவாக்குகிறோம். இந்த சேவையகம் கிளையன்ட்கள் பொதுவாக பயன்படுத்தும் Model Context Protocol-ஐ பயன்படுத்தி அழைக்கக்கூடிய கருவிகளை வெளிப்படுத்தும்.

### தேவைப்படும் பொருட்கள்

- Python 3.8 அல்லது மேல
- MCP Python SDK: `pip install mcp`
- அசிங்கிரண நிரலாக்கத்தின் அடிப்படை புரிதல்

முதலில் எங்கள் முதல் MCP stdio சேவையகத்தை உருவாக்குவோம்:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# பதிவு செய்யும் அமைப்பை உள்ளமைவு செய்க
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# சேவையகத்தை உருவாக்குக
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
    # stdio பரிமாற்றத்தை பயன்படுத்துக
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## பழைய SSE முறையிலிருந்து முக்கிய வேறுபாடுகள்

**Stdio போக்குவரத்து (தற்போதைய நிலை):**
- எளிய துணை செயலி மாதிரி - கிளையன்ட் சேவையகத்தை குழந்தை செயலியாக துவக்கும்
- JSON-RPC செய்திகளுக்கான stdin/stdout மூலம் தொடர்பு
- HTTP சேவையகம் அமைப்பு தேவையில்லை
- சிறந்த செயல்திறன் மற்றும் பாதுகாப்பு
- எளிதான டீபக் மற்றும் வளர்ச்சி

**SSE போக்குவரத்து (MCP 2025-06-18 வரை பழையதாக):**
- SSE முனைகளுடன் HTTP சேவையகம் தேவைப்படுகிறது
- வலை சேவையக கட்டமைப்பு காரணமாக சிக்கலான அமைப்பு
- HTTP முனைகளுக்கான கூடுதல் பாதுகாப்பு விதிகள்
- தற்போது Streamable HTTP மூலம் மாற்றப்பட்டுள்ளது

### stdio போக்குவரத்துடன் சேவையகத்தை உருவாக்குதல்

எங்கள் stdio சேவையகத்தை உருவாக்க, நாம்:

1. **தேவையான நூலகங்களை இறக்குமதி செய்து கொள்ள வேண்டும்** - MCP சேவையக கூறுகள் மற்றும் stdio போக்குவரத்தை
2. **சேவையக உருவாக்கு** - திறன்களை வரையறு
3. **கருவிகளை வரையறு** - வெளிப்படுத்த விரும்பும் செயல்பாடுகள் சேர்க்க
4. **போக்குவரத்தை அமைக்க** - stdio தொடர்பை உள்ளமைக்க
5. **சேவையகத்தை இயக்கு** - சேவையகத்தையும் செய்திகளையும் கையாள

நாம் இவ்வாறு படி படியாக உருவாக்குவோம்:

### படி 1: அடிப்படை stdio சேவையக உருவாக்கல்

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# பதிவு செய்யலை அமைக்கவும்
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# சர்வரை உருவாக்கவும்
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

### படி 2: கூடுதல் கருவிகள் சேர்க்கவும்

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

### படி 3: சேவையகத்தை இயக்குதல்

கோடுகளை `server.py` என சேமித்து கட்டளை வரியில் இயக்கவும்:

```bash
python server.py
```

சேவையகம் துவங்கி stdin-இல் உள்ளீட்டை காத்திருக்கும். JSON-RPC செய்திகளை stdio போக்குவரத்து மூலம் தொடர்பு கொள்கிறது.

### படி 4: Inspector மூலம் சோதனை செய்ய

உங்கள் சேவையகத்தை MCP Inspector மூலம் சோதிக்கலாம்:

1. Inspector ஐ நிறுவவும்: `npx @modelcontextprotocol/inspector`
2. Inspector ஐ இயக்கி உங்கள் சேவையை நோக்கிச் செல்லவும்
3. நீங்கள் உருவாக்கிய கருவிகளை சோதனை செய்யவும்

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## உங்கள் stdio சேவையகத்தை டீபக் செய்தல்

### MCP Inspector ஐப் பயன்படுத்துதல்

MCP Inspector MCP சேவையகங்களை டீபக் மற்றும் சோதனை செய்ய மதிப்புமிக்க கருவி. உங்கள் stdio சேவையகத்தில் இதைப் பயன்படுத்துவது எப்படி:

1. **Inspector ஐ நிறுவவும்**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ஐ இயக்கவும்**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **உங்கள் சேவையகத்தை சோதிக்கவும்**: Inspector ஒரு வலை இடைமுகத்தை வழங்குகிறது இதில் நீங்கள்:
   - சேவையக திறன்களை பார்க்கலாம்
   - பல்வேறு அளவுருக்களுடன் கருவிகளை சோதிக்கலாம்
   - JSON-RPC செய்திகளை கண்காணிக்கலாம்
   - இணைப்பு பிரச்சினைகளை தீர்க்கலாம்

### VS Code பயன்படுத்துதல்

ஏற்றுக்கொள்ளும் MCP சேவையகத்தை நேரடியாக VS Code-ல் டீபக் செய்யலாம்:

1. `.vscode/launch.json`-இல் ஒரு லாஞ்ச் கன்ஃபிகரேஷனை உருவாக்கவும்:
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

2. உங்கள் சேவையகக் கோடுகளில் இடைவெளிகளை அமைக்கவும்
3. டீபகர் இயக்கி Inspector மூலம் சோதனை செய்யவும்

### பொதுவான டீபக்க் குறிப்புகள்

- பதிவு செய்ய `stderr`-ஐ பயன்படுத்தவும் - MCP செய்திகளுக்காக `stdout`-க்கு எழுத வேண்டாம்
- அனைத்து JSON-RPC செய்திகள் வரிசைபடுத்தப்பட்டவரியாக இருத்தல் அவசியம்
- சிக்கல் செயல்பாடுகளுக்கு முன் எளிய கருவிகளுடன் முயற்சி செய்யவும்
- செய்தி வடிவங்களை சரிபார்க்க Inspector ஐ பயன்படுத்தவும்

## VS Code-ல் உங்கள் stdio சேவையகத்தை நுகர்வு

ஒரு MCP stdio சேவையகத்தை உருவாக்கியவுடன், அதை VS Code உடன்Claude அல்லது பிற MCP பொருந்தக்கூடிய கிளையன்ட்-களுடன் இணைக்கலாம்.

### அமைப்பு

1. **ஒரு MCP அமைப்பு கோப்பை உருவாக்கவும்** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) அல்லது `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) இல்:

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

2. **Claude ஐ மறுதொடக்கம் செய்யவும்**: புதிய சேவையக அமைப்பை ஏற்ற Claude ஐ மூடி மீண்டும் திறக்கவும்.

3. **இணைப்பை சோதிக்கவும்**: Claude உடன் உரையாடலை துவக்கி உங்கள் சேவையக கருவிகளை முயற்சி செய்யவும்:
   - "வணக்க கருவியைப் பயன்படுத்தி எனக்கு வணக்கம் சொல்ல முடியுமா?"
   - "15 மற்றும் 27 இன் கூட்டுத்தொகையை கணக்கிடு"
   - "சேவையக தகவல் என்ன?"

### TypeScript stdio சேவையகம் உதாரணம்

ஒரு முழுமையான TypeScript உதாரணம் இங்கே:

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

// கருவிகள் சேர்க்கவும்
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

### .NET stdio சேவையகம் உதாரணம்

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

## சுருக்கம்

இந்த புதுப்பிக்கப்பட்ட பாடத்தில் நீங்கள் கற்றுக்கொண்டது:

- தற்போதைய **stdio போக்குவரத்தை** பயன்படுத்தி MCP சேவையகங்களை உருவாக்குவது (பரவலானது)
- SSE போக்குவரத்து stdio மற்றும் Streamable HTTP-க்கு மேம்படுத்தப்பட்டதன் காரணத்தை புரிந்து கொள்வது
- MCP கிளையன்ட்கள் அழைக்கக்கூடிய கருவிகளை உருவாக்குவது
- MCP Inspector மூலம் சேவையகத்தை டீபக் செய்வது
- VS Code மற்றும் Claude உடன் stdio சேவையகத்தை ஒருங்கிணைத்தல்

stdio போக்குவரத்து பழைய SSE முறையைவிட எளிதான, பாதுகாப்பான மற்றும் சிறந்த செயல்திறன் கொண்ட MCP சேவையக உருவாக்க வழியைக் கொடுக்கிறது. 2025-06-18 இல் வெளியிட்ட MCP நெறிமுறைக்கு இது பெரும்பாலான MCP சேவையக செயல்பாடுகளுக்கு பரிந்துரைக்கப்பட்ட போக்குவரத்து ஆகும்.


### .NET

1. முதலில் சில கருவிகளை உருவாக்குவோம், இதற்காக *Tools.cs* என்ற கோப்பில் பின்வரும் உள்ளடக்கத்தை உருவாக்குவோம்:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## பயிற்சி: உங்கள் stdio சேவையகத்தை சோதனை செய்தல்

stdio சேவையகத்தை உருவாக்கிய பிறகு, அது முறையாக இயங்குகிறதா என்று சோதிப்போம்.

### தேவைகள்

1. MCP Inspector நிறுவப்பட்டுள்ளதா என்பதை உறுதி செய்யவும்:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. உங்கள் சேவையகக் கோடு (எ.கா., `server.py`) சேமிக்கப்பட்டிருக்க வேண்டும்

### Inspector மூலம் சோதனை செய்யல்

1. **சேவையகத்துடன் Inspector ஐ துவக்கவும்**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **வலை இடைமுகம் திறக்கவும்**: Inspector உங்களுடைய சேவையக திறன்களை காட்டும் வலை உலாவல் சாளரம் திறக்கும்.

3. **கருவிகளை சோதனை செய்யவும்**: 
   - வெவ்வேறு பெயர்களுடன் `get_greeting` கருவியை முயற்சி செய்யவும்
   - பல எண்களுடன் `calculate_sum` கருவியை சோதிக்கவும்
   - சேவையக மாதிரியான தகவல்களை பெற `get_server_info` கருவியை அழைக்கவும்

4. **தொடர்பை கண்காணிக்கவும்**: Inspector JSON-RPC செய்திகள் பரிமாற்றத்தை காட்டுகிறது.

### நீங்கள் பார்க்க வேண்டியது

உங்கள் சேவையகம் சரியாக துவங்கினால் நீங்கள் காண்பீர்கள்:
- Inspector இல் சேவையக திறன்கள் பட்டியலிடல்
- சோதனைக்கான கருவிகள்
- வெற்றிகரமான JSON-RPC செய்தி பரிமாற்றங்கள்
- கருவி பதில்கள் இடைமுகத்தில் காட்டப்படுதல்

### பொதுவான பிரச்சனைகள் மற்றும் தீர்வுகள்

**சேவையகம் துவங்கவில்லை:**
- அனைத்து சார்புகளும் நிறுவப்பட்டுள்ளதா சரிபார்க்கவும்: `pip install mcp`
- Python இலக்கணம் மற்றும் இடைவெளிகளை சரிபார்க்கவும்
- கான்சோலில் உள்ள பிழை செய்திகளை கவனிக்கவும்

**கருவிகள் தெரியவில்லை:**
- `@server.tool()` அலங்காரிகள் உள்ளதா என்று உறுதி செய்யவும்
- `main()` முன் கருவி செயல்பாடுகள் வரையறுக்கப்பட்டுள்ளதா என்று காணவும்
- சேவையகம் சரியாக அமைக்கப்பட்டுள்ளதா என சரிபார்க்கவும்

**இணைப்பு பிரச்சினைகள்:**
- stdio போக்குவரத்தை சரியாக பயன்படுத்துகிறதா என உறுதிப்படுத்தவும்
- வேறு எந்த செயலிகள் தடையின்றி இருக்கிறதா பாருங்கள்
- Inspector கட்டளை இலக்கணத்தை சரிபார்க்கவும்

## பணிகள்

உங்கள் சேவையகத்தை மேலும் திறன்களுடன் உருவாக்க முயற்சிக்கவும். உதாரணமாக, ஒரு கருவி API க்கு அழைக்கும். [இந்தப் பக்கம்](https://api.chucknorris.io/) பார்க்கவும். சேவையகம் எப்படி இருக்க வேண்டும் என்று நீங்கள் தீர்மானிக்கவும். மகிழ்ச்சியா இருங்கள் :)
## தீர்வு

[தீர்வு](./solution/README.md) இங்கு செயற்படக்கூடிய கோடுடன் ஒரு தீர்வு உள்ளது.

## முக்கியப் பாடங்கள்

இந்த அத்தியாயத்திலிருந்து முக்கியமானவற்றின் பட்டியல்:

- stdio போக்குவரத்து உள்ளூர் MCP சேவையகங்களுக்கு பரிந்துரைக்கப்படும் முறை.
- stdio போக்குவரத்து MCP சேவையகம் மற்றும் கிளையன்ட்களுக்குள் நிலையான உள்ளீடு மற்றும் வெளியீடு ஓடுபாதைகளின் மூலம் எளிதான தொடர்பை வழங்குகிறது.
- stdio சேவையகங்களை நேரடியாக Inspector மற்றும் Visual Studio Code மூலம் நுகர முடியும், டீபக் மற்றும் ஒருங்கிணைப்பு எளிமையாகும்.

## உதாரணங்கள் 

- [Java கணக்கீட்டாளர்](../samples/java/calculator/README.md)
- [.Net கணக்கீட்டாளர்](../../../../03-GettingStarted/samples/csharp)
- [JavaScript கணக்கீட்டாளர்](../samples/javascript/README.md)
- [TypeScript கணக்கீட்டாளர்](../samples/typescript/README.md)
- [Python கணக்கீட்டாளர்](../../../../03-GettingStarted/samples/python) 

## கூடுதல் வளங்கள்

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## அடுத்தது என்ன

## அடுத்த படிகள்

நீங்கள் stdio போக்குவரத்துடன் MCP சேவையகங்களை கட்டிய பிறகு, மேலும் மேம்பட்ட தலைப்புகளை ஆராய முடியும்:

- **அடுத்து**: [MCP உடன் HTTP ஸ்ட்ரீமிங் (Streamable HTTP)](../06-http-streaming/README.md) - தொலைதூர சேவையகங்களுக்கு ஆதரவான மற்றொரு போக்குவரத்து முறையை கற்றுக்கொள்ளவும்
- **மேம்பட்டது**: [MCP பாதுகாப்பு சிறந்த நடைமுறைகள்](../../02-Security/README.md) - உங்கள் MCP சேவைகளில் பாதுகாப்பு நடைமுறைகளை செயல்படுத்தவும்
- **உற்பத்தி**: [பயன்படுத்தல் திட்டங்கள்](../09-deployment/README.md) - உற்பத்தி பயன்பாட்டிற்கு சேவைகளை ஒதுக்கவும்

## கூடுதல் வளங்கள்

- [MCP நெறிமுறை 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - தற்போதைய நெறிமுறை
- [MCP SDK ஆவணங்கள்](https://github.com/modelcontextprotocol/sdk) - அனைத்து மொழிகளுக்கும் SDK குறிப்பு
- [சமூக உதாரணங்கள்](../../06-CommunityContributions/README.md) - சமூகத்திலிருந்து மேலும் சேவையக உதாரணங்கள்

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->