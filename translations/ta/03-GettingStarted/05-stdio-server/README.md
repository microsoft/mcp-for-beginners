# MCP சர்வர் stdio பரிமாற்றத்துடன்

> **⚠️ முக்கியமான புதுப்பிப்பு**: MCP குறிப்புரை 2025-06-18 முதல், தனித்துவமான SSE (Server-Sent Events) பரிமாற்றம் **மெழுகு** என மதிப்பிடப்பட்டது மற்றும் அதற்கு பதிலாக "Streamable HTTP" பரிமாற்றம் அறிமுகப்படுத்தப்பட்டது. தற்போதைய MCP குறிப்புரை இரண்டு முக்கிய பரிமாற்ற முறைமைகளை வரையறுக்கிறது:
> 1. **stdio** - ஸ்டான்டர்ட் இன்புட்/ஆட்ட்புட் (உள்ளூர் சர்வர்களுக்கான பரிந்துரையானது)
> 2. **Streamable HTTP** - உட்பயன்பாட்டில் SSE பயன்படுத்தக்கூடிய தொலை சர்வர்களுக்காக
>
> இந்த பாடம் **stdio பரிமாற்றம்** மீது கவனம் செலுத்தி புதுப்பிக்கப்பட்டது, இது பெரும்பாலான MCP சர்வர் செயலாக்கங்கள் కోసం பரிந்துரைக்கப்படுபவை.

stdio பரிமாற்றம் MCP சர்வர்கள் ஸ்டான்டர்ட் இன்புட் மற்றும் ஆட்ட்புட் ஸ்ட்ரீம்களுக்குள் வாடிக்கையாளர்களுடன் தொடர்பு கொள்வதற்கான வழியை வழங்குகிறது. இது தற்போதைய MCP குறிப்புரையில் மிகவும் பிரபலமாகவும் பரிந்துரைக்கப்டும் பரிமாற்ற முறையாகவும் உள்ளதுசெய்து எளிதாக பலவிதமான வாடிக்கையாளர் பயன்பாடுகளுடன் ஒருங்கிணைக்கக்கூடிய MCP சர்வர்களை உருவாக்க ஒரு எளிமையான மற்றும் திறமையான வழியைக் கொடுக்கிறது.

## கண்ணோட்டம்

இந்த பாடம் stdio பரிமாற்றத்தைப் பயன்படுத்தி MCP சர்வர்களை எப்படிப்படிப்பதாக உருவாக்கி மற்றும் பயன்படுத்துவது என கற்பிக்கும்.

## கற்றல் நோக்குக்கள்

இந்த பாடம் முடிந்த பிறகு, நீங்கள்:

- stdio பரிமாற்றத்தைப் பயன்படுத்தி MCP சர்வரை உருவாக்க முடியும்.
- MCP சர்வரை Inspector மூலம் பிழைத்திருத்த முடியும்.
- Visual Studio Code மூலம் MCP சர்வரை பயன்படுத்த முடியும்.
- தற்போதைய MCP பரிமாற்ற முறைகள் மற்றும் stdio பரிந்துரைக்கப்படுவதன் காரணங்களை புரிந்து கொள்வீர்கள்.


## stdio பரிமாற்றம் - அது எப்படி வேலை செய்கிறது

stdio பரிமாற்றம் தற்போதைய MCP குறிப்புரையில் (2025-06-18) ஆதரவு பெறும் இரு பரிமாற்ற வகைகளில் ஒன்று. இது எப்படி செயல்படுகிறது என்பது இதோ:

- **எளிய தொடர்பு**: சர்வர் JSON-RPC செய்திகளை ஸ்டான்டர்ட் இன்புட் (`stdin`) இலிருந்து வாசித்து, ஸ்டான்டர்ட் ஆட்ட்புட் (`stdout`) க்கு அனுப்புகிறது.
- **செயல்முறை அடிப்படையிலானது**: வாடிக்கையாளர் MCP சர்வரை துணைசெயல்முறையாக (subprocess) துவங்குகிறது.
- **செய்தி வடிவம்**: செய்திகள் தனி JSON-RPC கோரிக்கைகள், அறிவிப்புகள் அல்லது பதில்கள், வரிசை மாற்றங்களால் பிரிக்கப்பட்டவை.
- **பதிவு**: சர்வர் பதிவு நோக்கத்திற்காக ஸ்டான்டர்ட் தவறு (`stderr`) இல் UTF-8 எழுத்துச்சண்டைகளை எழுதலாம்.

### முக்கிய தேவைகள்:
- செய்திகள் வரிசை மாற்றங்களால் பிரிக்கப்பட்டிருக்க வேண்டும் மற்றும் உள்ளிட்டு வரிசை மாற்றங்களை கொண்டிருக்கக்கூடாது
- சர்வர் செல்லுபடியான MCP செய்தி அல்லாத எதுவும் `stdout`-க்கு எழுதியேண்டும் இல்லை
- வாடிக்கையாளர் செல்லுபடியான MCP செய்தி அல்லாத எதுவும் சர்வரின் `stdin`-க்கு எழுதியேண்டும் இல்லை

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

பின்வரும் குறியீட்டில்:

- MCP SDK இலிருந்து `Server` வகுப்பு மற்றும் `StdioServerTransport` இறக்குமதி செய்யப்படும்
- அடிப்படை கட்டமைப்பும் திறன்களுடன் ஒரு சர்வர் உருவாக்கப்படுகிறது
- `StdioServerTransport` உள்ளீடு உருவாக்கி சர்வரை அத்துடன் இணைத்து stdin/stdout வழியில் தொடர்பை இயக்குகிறது

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# சர்வர் உதரணம் உருவாக்கவும்
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

பின்வரும் குறியீட்டில்:

- MCP SDK பயன்படுத்தி ஒரு சர்வர் உருவாக்கப்படுகிறது
- அலங்காரிகளை பயன்படுத்தி கருவிகள் வரையறுக்கப்படுகின்றன
- stdio_server சூழல் மேலாளரை பயன்படுத்தி பரிமாற்றத்தை கையாள்கிறோம்

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

SSE உடன் முக்கிய வேறுபாடு stdio சர்வர்கள்:

- வலை சர்வர் அமைப்பு அல்லது HTTP முனைகள்தான் தேவையில்லை
- வாடிக்கையாளர் துணைசெயல்முறையாக சர்வரை துவங்குகிறது
- stdin/stdout ஸ்ட்ரீம்களில் தொடர்பு கொள்கின்றன
- செயல்பாட்டிலும் பிழைத்திருத்தத்திலும் எளிது

## பயிற்சி: stdio சர்வர் உருவாக்குதல்

எமது சர்வரை உருவாக்க, இரண்டு விஷயங்களை நினைவில் கொள்ள வேண்டும்:

- இணைய சர்வரை பயன்படுத்தி இணைப்பு மற்றும் செய்திகளுக்கான முனைகளை வெளிப்படுத்த வேண்டும்.
## பயிற்சிக் கூடம்: எளிய MCP stdio சர்வர் உருவாக்குதல்

இந்த பயிற்சிக் கூடத்தில், பரிந்துரைக்கப்பட்ட stdio பரிமாற்றத்தைப் பயன்படுத்தி ஒரு எளிய MCP சர்வரை உருவாக்கப்போகிறோம். இந்த சர்வர் வாடிக்கையாளர்கள் ஸ்டான்டர்ட் Model Context Protocol மூலம் அழைக்கக்கூடிய கருவிகளை வெளிப்படுத்தும்.

### தேவைகள்

- Python 3.8 அல்லது அதற்கு மேலர் பதிப்பு
- MCP Python SDK: `pip install mcp`
- ஒத்த்செயலாக்கம் பற்றிய அடிப்படை அறிவு

நாம் நமது முதற்படியான MCP stdio சர்வர் உருவாக்குவோம்:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# பதிவு செய்வதை அமைக்கவும்
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# சேவையகத்தை உருவாக்கவும்
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
    # stdio போக்குவரத்தைக் பயன்படுத்தவும்
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## மதிப்பிடப்பட்ட SSE முறைக்கு முக்கிய வேறுபாடுகள்

**Stdio பரிமாற்றம் (தற்போதைய தரநிலை):**
- எளிய துணைசெயல்முறை மாதிரி - வாடிக்கையாளர் சர்வரை குழந்தை செயலாக துவக்கும்
- JSON-RPC செய்திகளுடன் stdin/stdout வழியாக தொடர்பு
- HTTP சர்வர் அமைப்பு தேவையில்லை
- சிறந்த செயல்திறன் மற்றும் பாதுகாப்பு
- எளிதான பிழைத்திருத்தம் மற்றும் மேம்பாடு

**SSE பரிமாற்றம் (MCP 2025-06-18 முதல் மெழுகு):**
- SSE முனைகளுடன் HTTP சர்வர் தேவையானது
- வலை சர்வர் கட்டமைப்புடன் சிக்கலான அமைப்பு
- HTTP முனைகளுக்கான கூடுதல் பாதுகாப்பு கருதல்கள்
- தற்போது Streamable HTTP-ஆல் மாற்றப்பட்டது

### stdio பரிமாற்றத்துடன் சர்வர் உருவாக்குதல்

stdio சர்வரை உருவாக்க நாம்:

1. **தேவையான நூலகங்களை இறக்குமதி செய்யவும்** - MCP சர்வர் கூறுகள் மற்றும் stdio பரிமாற்றம்
2. **ஒரு சர்வர் உருவாக்கவும்** - திறன்களுடன் சர்வரை வரையறுக்கவும்
3. **கருவிகள் வரையறுக்கவும்** - வெளிப்படுத்த வேண்டிய செயல்பாடுகள் சேர்க்கவும்
4. **பரிமாற்றத்தை அமைக்கவும்** - stdio தொடர்பை  கட்டமைக்கவும்
5. **சர்வரை இயக்கவும்** - சர்வரை துவக்கி செய்திகளை கையாளவும்

கட்டத்துடன் கட்டமாக உருவாக்குவோம்:

### கட்டம் 1: அடிப்படை stdio சர்வர் உருவாக்கல்

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# பதிவு அமைக்க
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# சேவையகம் உருவாக்கவும்
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

### கட்டம் 2: மேலும் கருவிகள் சேர்க்கவும்

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

### கட்டம் 3: சர்வரை இயக்குதல்

`server.py` என கோப்பாக சேமித்து கட்டளைகோட்டிலிருந்து இயக்கு:

```bash
python server.py
```

சர்வர் துவங்கி stdin இலிருந்து உள்ளீட்டுக்காக காத்திருக்கும். stdio பரிமாற்றம் வழியாக JSON-RPC செய்திகளுடன் தொடர்பு கொள்கிறது.

### கட்டம் 4: Inspector மூலம் சோதனை

Inspector ஐ பயன்படுத்தி உங்கள் சர்வரை சோதிக்கலாம்:

1. Inspector ஐ நிறுவுக: `npx @modelcontextprotocol/inspector`
2. Inspector ஐ இயக்கி உங்கள் சர்வரை குறிப்பிடுக
3. நீங்கள் உருவாக்கிய கருவிகளை சோதிக்கவும்

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio சர்வரை பிழைத்திருத்தல்

### MCP Inspector பயன்படுத்துதல்

MCP Inspector என்பது MCP சர்வர்களை பிழைத்திருத்தவும் சோதிக்கவும் அமைய ஒரு முக்கிய கருவி. உங்கள் stdio சர்வருடன் இதனை பயன்படுத்த:

1. **Inspector ஐ நிறுவுக**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ஐ இயக்குக**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **உங்கள் சர்வரைத் சோதிக்கவும்**: Inspector ஒரு வலை இடைமுகத்தை வழங்குகிறது, அங்கு:
   - சர்வர் திறன்களை பார்க்கலாம்
   - வெவ்வேறு அளவுருக்களுடன் கருவிகளை சோதிக்கலாம்
   - JSON-RPC செய்திகளை கண்காணிக்கலாம்
   - இணைப்பு பிரச்சினைகளை பிழைத்திருத்தலாம்

### VS Code பயன்படுத்துதல்

VS Code இல் நேரடியாக MCP சர்வரை பிழைத்திருத்தவும் முடியும்:

1. `.vscode/launch.json` இல் ஒரு தொடக்க அமைப்பு உருவாக்குக:
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

2. சர்வர் குறியீட்டில் இடைநிறுத்தப்புள்ளிகளை அமைக்க
3. பிழைத்திருத்தியை இயக்கு மற்றும் Inspector உடன் சோதனை செய்

### பொதுவான பிழைத்திருத்த குறிப்புகள்

- பதிவு செய்ய `stderr` பயன்படுத்தவும் - MCP செய்திகளுக்கான `stdout`-க்கே எழுதியேண்டும் இல்லை
- அனைத்து JSON-RPC செய்திகள் வரிசை மாற்றங்களால் பிரிக்கப்பட்டிருக்க வேண்டும்
- முதலில் எளிய கருவிகளுடன் சோதனை செய்து பிறகு சிக்கல் செயல்பாடுகள் சேர்க்கவும்
- செய்தி வடிவங்களை பரிசோதிக்க Inspector ஐ பயன்படுத்தவும்

## VS Code இல் stdio சர்வரை பயன்படுத்துதல்

உங்கள் MCP stdio சர்வர் கட்டிய பிறகு, அதை VS Code உடன் ஒருங்கிணைத்து Claude அல்லது பிற MCP-பொதுக்கருத்து வாடிக்கையாளர்களுடன் பயன்படுத்தலாம்.

### கட்டமைப்பு

1. **MCP கட்டமைப்பு கோப்பை உருவாக்கு** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) அல்லது `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Claude ஐ மீண்டும் துவக்கு**: புதிய சர்வர் கட்டமைப்பை ஏற்ற Claude ஐ மூடி மீண்டும் திறக்கவும்.

3. **இணைப்பை சோதிக்கவும்**: Claude உடன் உரையாடலை துவக்கி உங்கள் சர்வர் கருவிகளைப் பயன்படுத்த முயற்சி செய்யவும்:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio சர்வர் எடுத்துக்காட்டு

பலவகை TypeScript எடுத்துக்காட்டு:

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

// கருப்பொருட்களைச் சேர்க்கவும்
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

### .NET stdio சர்வர் எடுத்துக்காட்டு

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

இந்த புதுப்பிக்கப்பட்ட பாடத்தில், நீங்கள் கற்றுக் கொண்டது:

- தற்போதைய **stdio பரிமாற்றத்தைப்** பயன்படுத்தி MCP சர்வர்களை உருவாக்குதல் (பரிந்துரைக்கப்படும் முறை)
- SSE பரிமாற்றம் மெழுகு செய்யப்பட்டு stdio மற்றும் Streamable HTTP எதனால் பதிலாக பரிந்துரைக்கப்படுகிறது என்பதை புரிதல்
- MCP வாடிக்கையாளர்களால் அழைக்கக்கூடிய கருவிகளை உருவாக்குதல்
- MCP Inspector மூலம் உங்கள் சர்வரை பிழைத்திருத்துதல்
- VS Code மற்றும் Claude உடன் உங்கள் stdio சர்வரை ஒருங்கிணைத்தல்

stdio பரிமாற்றம் மெழுகு செய்யப்பட்ட SSE முறையைவிட எளிமையான, பாதுகாப்பான மற்றும் அதிக செயல்திறன் வாய்ந்த MCP சர்வர்கள் உருவாக்க வழி வழங்குகிறது. 2025-06-18 குறிப்புரையின் படி இது பெரும்பாலான MCP சர்வர் செயலாக்கங்களுக்கு பரிந்துரைக்கப்படுகிறது.


### .NET

1. முதலில் சில கருவிகளை உருவாக்குவோம், இதற்காக *Tools.cs* என ஒரு கோப்பை பின்வரும் உள்ளடக்கத்துடன் உருவாக்குவோம்:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## பயிற்சி: உங்கள் stdio சர்வரைச் சோதித்தல்

இப்போது உங்கள் stdio சர்வரை கட்டியுள்ளீர்கள், சரியான முறையில் செயல்படுகிறதா என்பதைச் சோதிப்போம்.

### தேவைகள்

1. MCP Inspector நிறுவியிருக்கிறீா் என்பதை உறுதி செய்யவும்:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. உங்கள் சர்வர் குறியீடு சேமிக்கப்பட்டிருக்கும் (உதா., `server.py`)

### Inspector மூலம் சோதனை

1. **Inspector ஐ உங்கள் சர்வருடன் துவக்கு**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **வலை இடைமுகத்தை திறக்கவும்**: Inspector உங்கள் சர்வரின் திறன்களை காண ஒரு உலாவி விண்டோ திறக்கும்.

3. **கருவிகளை சோதிக்கவும்**: 
   - வெவ்வேறு பெயர்களைக் கொண்டு `get_greeting` கருவியை முயற்சி செய்யவும்
   - பல எண்களுடன் `calculate_sum` கருவியைப் பரிசோதிக்கவும்
   - சர்வர் தகவல்களைப் பார்ப்பதற்காக `get_server_info` கருவியை அழைக்கவும்

4. **தொடர்பை கண்காணிக்கவும்**: Inspector வாடிக்கையாளர் மற்றும் சர்வர் இடையேயான JSON-RPC செய்திகளை காண்பிக்கும்.

### நீங்கள் காண வேண்டியது

சர்வர் சரியான முறையில் துவங்கும் போது, நீங்கள் காண்பீர்கள்:
- Inspector இல் சர்வர் திறன்கள் பட்டியலிடப்பட்டுள்ளன
- சோதனைக்கான கருவிகள் கிடைக்கின்றன
- JSON-RPC செய்தி பரிமாற்றங்கள் வெற்றிகரமாக நடைபெறுகின்றன
- கருவி பதில்கள் இடைமுகத்தில் காட்டப்படுகின்றன

### பொதுவான பிரச்சினைகள் மற்றும் தீர்வுகள்

**சர்வர் துவங்கவில்லை:**
- அனைத்து பொது சார்பு நூலகங்கள் நிறுவப்பட்டுள்ளனவா என சரிபார்க்கவும்: `pip install mcp`
- Python இலக்கணம் மற்றும் இடைவெளிகள் சரிபார்க்கவும்
- கமாண்ட் லைன் பிழை செய்திகள் பாருங்கள்

**கருவிகள் தோன்றவில்லை:**
- `@server.tool()` அலங்காரிகள் உள்ளனவா எனப் பாருங்கள்
- கருவி செயல்பாடுகள் `main()` க்கு முன்பாக வரையறுக்கப்பட்டுள்ளனவா
- சர்வர் சீராக கட்டமைக்கப்பட்டுள்ளதா

**இணைப்பு பிரச்சினைகள்:**
- சர்வர் stdio பரிமாற்றத்தை சரியாக பயன்படுத்துகிறதா
- மற்ற செயலிகள் தடையாக இல்லையா
- Inspector கட்டளை உரைப் பிழை இல்லை

## பணி

உங்கள் சர்வரை மேலதிக திறன்களுடன் விரிவுபடுத்த முயற்சி செய்யவும். [இந்த பக்கம்](https://api.chucknorris.io/) இல் இருந்து எடுத்துக்காட்டு API அழைப்பை செய்யக்கூடிய கருவியைச் சேர்க்கலாம். சர்வரை எப்படி வடிவமைப்பது என்பது உங்களுடைய தேர்வு. மகிழ்ச்சியாக செயல்படுங்கள் :)
## தீர்வு

[தீர்வு](./solution/README.md) செயற்படும் குறியீடு உடன் சாத்தியமான தீர்வு.

## முக்கியமான எடுத்துக்காட்டுக்கள்

இந்த அதிகாரத்தில் இருந்து முக்கியமான எடுத்துக்காட்டுக்கள்:

- stdio பரிமாற்றம் உள்ளூர் MCP சர்வர்களுக்கான பரிந்துரைக்கப்டutha முறை.
- stdio பரிமாற்றம் MCP சர்வர்கள் மற்றும் வாடிக்கையாளர்களுக்கு ஸ்டான்டர்ட் இன்புட் மற்றும் ஆட்ட்புட் ஸ்ட்ரீம்களிடையே எளிய தொடர்புக்களை வழங்குகிறது.
- stdio சர்வர்களை நேரடியாக பயன்படுத்த Inspector மற்றும் Visual Studio Code இரண்டையும் பயன்படுத்த முடியும், இது பிழைத்திருத்தத்தையும் ஒருங்கிணைப்பையும் எளிமையாக்குகிறது.

## மாதிரிகள் 

- [Java கணக்கிடுபவர்](../samples/java/calculator/README.md)
- [.Net கணக்கிடுபவர்](../../../../03-GettingStarted/samples/csharp)
- [JavaScript கணக்கிடுபவர்](../samples/javascript/README.md)
- [TypeScript கணக்கிடுபவர்](../samples/typescript/README.md)
- [Python கணக்கிடுபவர்](../../../../03-GettingStarted/samples/python) 

## கூடுதல் வளங்கள்

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## அடுத்தது என்ன

## அடுத்த படிகள்

இப்போது நீங்கள் stdio பரிமாற்றத்தை பயன்படுத்தி MCP சர்வர்கள் எப்படி கட்டுவது என்பதை கற்றுக்கொண்ட பிறகு, மேலதிக தலைப்புகளை ஆராயலாம்:

- **அடுத்தது**: [MCP உடன் HTTP ஸ்ட்ரீமிங் (Streamable HTTP)](../06-http-streaming/README.md) - தொலை சர்வர்களுக்கான மற்றொரு ஆதரவு பெற்ற பரிமாற்ற முறை
- **அதிகமாக**: [MCP பாதுகாப்பு சிறந்த நடைமுறைகள்](../../02-Security/README.md) - உங்கள் MCP சர்வர்களில் பாதுகாப்பை அமல் படுத்துதல்
- **உற்பத்தி**: [பரப்புரையிடும்  நடைமுறைகள்](../09-deployment/README.md) - உற்பத்தி பயன்பாட்டிற்கு சர்வர்களை பரப்புதல்

## கூடுதல் வளங்கள்

- [MCP குறிப்புரை 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - அதிகாரப்பூர்வ குறிப்புரை
- [MCP SDK ஆவணங்கள்](https://github.com/modelcontextprotocol/sdk) - அனைத்து மொழிகளுக்குமான SDK குறிப்பு
- [சங்க சமூக எடுத்துக்காட்டுகள்](../../06-CommunityContributions/README.md) - சமூகத்திலிருந்து மேலும் சர்வர் எடுத்துக்காட்டுகள்

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**வெளியீட்டு அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியமானது என்பதற்காக முயற்சி செய்கிறோம் என்றாலும், தானாகவே செய்யப்படும் மொழிபெயர்ப்பில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கருத்தில் கொள்ளவும். தமிழில் உள்ள அசல் ஆவணம் அதிகாரபூர்வமான மூலமானது ஆகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்காக, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் உருவாகும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->