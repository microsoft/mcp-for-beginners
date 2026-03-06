# stdio போக்குவரத்து கொண்ட MCP சர்வர்

> **⚠️ முக்கியமான புதுப்பிப்பு**: MCP குறிப்புரை 2025-06-18 இன் படி, தனிநபர் SSE (Server-Sent Events) போக்குவரத்து **கைவிடப்பட்டது** மற்றும் அதை "Streamable HTTP" போக்குவரத்தால் மாற்றப்பட்டது. தற்போதைய MCP குறிப்புரை இரண்டு முக்கிய போக்குவரத்து முறைகளைக் குறிப்பிடுகிறது:
> 1. **stdio** - முறைசார் உள்ளீடு/வெளியீடு (உள்ளூர் சர்வர்களுக்கு பரிந்துரைக்கப்படுகிறது)
> 2. **Streamable HTTP** - SSE உள்ளகமாகப் பயன்படுத்தக்கூடிய தொலைநிலை சர்வர்களுக்கு
>
> இந்த பாடம் **stdio போக்குவரத்துக்கு** கவனம் செலுத்தி புதுப்பிக்கப்பட்டது, இது மிகப் பல MCP சர்வர் செயலாக்கங்களுக்கு பரிந்துரைக்கப்படும் முறையாகும்.

stdio போக்குவரத்து MCP சர்வர்களுக்கு பொதுவான இயல்பான உள்ளீடு மற்றும் வெளியீடு ஓட்டுகளின் மூலம் கிளையன்ட்களுடன் தொடர்பு கொள்ள உதவுகிறது. இது இன்றைய MCP குறிப்புரையில் மிகப் பரவலாகப் பயன்படுத்தப்படும் மற்றும் பரிந்துரைக்கப்படும் போக்குவரத்து முறைமையாகும், எளிமையாகவும் திறமையாகவும் MCP சர்வர்களை உருவாக்குவதற்கான வழியைக் கொடுக்கிறது, மேலும் பல வகையான கிளையன்ட் பயன்பாடுகளுடன் எளிதில் இணைக்க முடியும்.

## ஓவர்வியூ

இந்த பாடம் stdio போக்குவரத்து பயன்படுத்தி MCP சர்வர்களை உருவாக்கி பயன்படுத்துவது எப்படி என்று கற்பிக்கிறது.

## கற்றல் குறிக்கோள்கள்

இந்தப் பாடம் முடிவுக்கு வரும் போது, நீங்கள்:

- stdio போக்குவரத்தைப் பயன்படுத்து MCP சர்வரை உருவாக்க முடியும்.
- Inspector மூலம் MCP சர்வரை பிழைதிருத்தம் செய்ய முடியும்.
- Visual Studio Code மூலம் MCP சர்வரை பயன்படுத்த முடியும்.
- தற்போதைய MCP போக்குவரத்து முறைகள் மற்றும் ஏன் stdio பரிந்துரைக்கப்படுகிறது என்பதை புரிந்துகொள்ள முடியும்.

## stdio போக்குவரத்து - இது எப்படி செயல்படுகிறது

stdio போக்குவரத்து, தற்போதைய MCP குறிப்புரையின் (2025-06-18) இரண்டு ஆதரவு போக்குவரத்து வகைகளில் ஒன்றாகும். இதோ இது எப்படி செயல்படுகிறது:

- **எளிய தொடர்பு**: சர்வர் JSON-RPC پیامங்களைக் பொதுவான உள்ளீட்டிலிருந்து (`stdin`) வாசித்து, பொதுவான வெளியீட்டிற்கு (`stdout`) அனுப்புகிறது.
- **செயல்பாட்டுக்குள்**: கிளையன்ட் MCP சர்வரை ஒரு துணை செயலியாகத் தொடக்குகிறது.
- **பதிவடிவம்**: پیامங்கள் தனித்த JSON-RPC கோரிக்கைகள், அறிவிப்புகள் அல்லது பதில்கள், புதிய வரிகளால் பிரிக்கப்பட்டவை.
- **லாக்கிங்**: சர்வர் பதிவு நோக்கங்களுக்காக UTF-8 எழுத்துகளை பொதுவான பிழை வெளியீட்டிற்கு (`stderr`) எழுதலாம்.

### முக்கிய தேவைகள்:
- پیامங்கள் புதிய வரிகளால் பிரிக்கப்பட்டிருக்க வேண்டும் மற்றும் உள்ளிடப்பட்ட புதிய வரிகளை கொண்டிருக்கக்கூடாது
- சர்வர் `stdout` இல் செல்லுபடியாகும் MCP پیامம் அல்லாததை எழுதக்கூடாது
- கிளையன்ட் `stdin` இல் செல்லுபடியாகும் MCP پیامம் அல்லாததை சர்வருக்கு எழுதக்கூடாது

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

மேல் உள்ள குறியீட்டில்:

- MCP SDK இல் இருந்து `Server` வகுப்பு மற்றும் `StdioServerTransport` ஐ இறக்குமதி செய்கின்றோம்
- அடிப்படை அமைப்புகளுடன் மற்றும் திறன்களுடன் சர்வர் உதாரணத்தை உருவாக்குகிறோம்

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# சர்வர் இன்ஸ்டான்ஸ் உருவாக்கவும்
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

மேல் உள்ள குறியீட்டில் நாம்:

- MCP SDK பயன்படுத்தி சர்வர் உதாரணத்தை உருவாக்குகிறோம்
- டெகாரேட்டர்களைப் பயன்படுத்தி கருவிகளை నిర్వచிக்கின்றோம்
- stdio_server சூழல் மேலாளரைப் பயன்படுத்தி போக்குவரத்தைக் கையாள்கிறோம்

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

SSE இலிருந்து முக்கிய வித்தியாசம் stdio சர்வர்களில்:

- வலை சர்வர் அமைப்போ அல்லது HTTP புள்ளிகளோ தேவையில்லை
- கிளையன்டால் துணை செயலிகளாக தொடங்கப்படுகின்றன
- stdin/stdout ஓட்டுகளின் மூலம் தொடர்பு கொள்கின்றன
- செயல்படுத்த மற்றும் பிழைத்திருத்த எளிது

## பயிற்சி: stdio சர்வர் உருவாக்குதல்

சர்வரை உருவாக்க, இரண்டு அம்சங்களை கவனிக்க வேண்டும்:

- இணக்கம் மற்றும் پیامங்களுக்கு வெப்சர்வரை பயன்படுத்தி புள்ளிகளை வெளிப்படுத்த வேண்டும்.
## பயிற்சி கட்டளை: எளிய MCP stdio சர்வர் உருவாக்குதல்

இந்த பயிற்சியில், பரிந்துரைக்கப்பட்ட stdio போக்குவரத்தைக் கொண்டு ஒரு எளிய MCP சர்வரை உருவாக்குவோம். இந்த சர்வர் கிளையன்ட்கள் Model Context Protocol பயன்படுத்திச் கூப்பிடக்கூடிய கருவிகளை வெளிப்படுத்தும்.

### தேவைகள்

- Python 3.8 அல்லது அதற்கு மேற்பட்டது
- MCP Python SDK: `pip install mcp`
- அசிச்ன்க் (async) நிரலாக்க விசாரணை அடிப்படை அறிவு

நாம் முதல் MCP stdio சர்வரை உருவாக்குவோம்:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# பதிவேற்றத்தை அமைக்கவும்
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
    # stdio பரிமாற்றத்தை பயன்படுத்தவும்
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## கைவிடப்பட்ட SSE முறையிலிருந்து முக்கிய வித்தியாசங்கள்

**Stdio போக்குவரத்து (தற்போதைய தரநிலை):**
- எளிய துணை செயலி மாதிரி - கிளையன்ட் சர்வரை குழந்தை செயலியாக தொடங்குகிறது
- stdin/stdout வழியாக JSON-RPC پیامங்களால் தொடர்பு
- HTTP சர்வர் அமைப்புக்கு தேவையில்லை
- மேம்பட்ட செயல்திறன் மற்றும் பாதுகாப்பு
- எளிமையான பிழைத்திருத்தம் மற்றும் மேம்பாடு

**SSE போக்குவரத்து (2025-06-18 MCP இல் இருந்து கைவிடப்பட்டது):**
- SSE புள்ளிகளுடன் HTTP சர்வர் தேவைப்படுவது
- வலை சர்வர் அமைப்பு கூடுதல் சிக்கல் கொண்டது
- HTTP புள்ளிகளுக்கான கூடுதல் பாதுகாப்பு கவலைகள்
- இப்போது web சார்ந்த இடைப்பயன்பாடுகளுக்கான Streamable HTTP மூலம் மாற்றப்பட்டது

### stdio போக்குவரத்துடன் சர்வர் உருவாக்குதல்

stdio சர்வர் உருவாக்குவதற்கு:

1. **தேவையான நூலகங்களை இறக்குமதி செய்க** - MCP சர்வர் கூறுகள் மற்றும் stdio போக்குவரத்து
2. **சர்வர் உதாரணத்தை உருவாக்குக** - திறன்களுடன் சர்வரை வரையறுக்கவும்
3. **கருவிகளை வரையறுக்கவும்** - வெளிப்படுத்த விரும்பும் செயல்பாடுகளை சேர்க்கவும்
4. **போக்குவரத்தை அமைக்கவும்** - stdio தொடர்பை கட்டமைக்கவும்
5. **சர்வரை இயக்கவும்** - சர்வரை தொடங்கி پیامங்களை கையாளவும்

இதனை படி படியாக கட்டுருவோம்:

### படி 1: அடிப்படை stdio சர்வர் உருவாக்குக

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# பதிவு முறையை கீழ்த்தழுவு
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# சேவையகத்தை உருவாக்கு
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

### படி 2: மேலும் கருவிகள் சேர்க்கவும்

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

### படி 3: சர்வரை இயக்குக

குறியீட்டினை `server.py` என்று சேமித்து கட்டளை வரியில் இருந்து இயக்கவும்:

```bash
python server.py
```

சர்வர் தொடங்கி stdin இல் இருந்து உள்ளீட்டை காத்திருக்கும். stdio போக்குவரத்து வழியாக JSON-RPC پیامங்களில் தொடர்பு கொள்ளுகிறது.

### படி 4: Inspector உடன் சோதனை

Inspector மூலம் உங்கள் சர்வரை சோதிக்கலாம்:

1. Inspector ஐ நிறுவுக: `npx @modelcontextprotocol/inspector`
2. Inspector ஐ இயக்கி உங்கள் சர்வரை நோக்கி அமைக்கவும்
3. நீங்கள் உருவாக்கிய கருவிகளை சோதிக்கவும்

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## உங்கள் stdio சர்வர் பிழைத்திருத்தம்

### MCP Inspector பயன்படுத்துதல்

MCP Inspector MCP சர்வர்களின் பிழைத்திருத்தத்திற்கு மற்றும் சோதனைக்கான வலுவான கருவி. உங்கள் stdio சர்வருடன் இதைப் பயன்படுத்துவது எப்படி:

1. **Inspector ஐ நிறுவுக**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ஐ இயக்குக**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **உங்கள் சர்வரை சோதிக்கவும்**: Inspector வலை இடைமுகத்தை வழங்குகிறது, அதில் நீங்கள்:
   - சர்வர் திறன்களை பார்வையிடலாம்
   - வேறுபட்ட கொள்கலன்களுடன் கருவிகளை சோதிக்கலாம்
   - JSON-RPC پیامங்களை கண்காணிக்கலாம்
   - இணைப்பு பிரச்சினைகளை பிழைத்திருத்தலாம்

### Visual Studio Code பயன்படுத்துதல்

VS Code இல் நேரடியாக உங்கள் MCP சர்வரை பிழைத்திருத்தலாம்:

1. `.vscode/launch.json` இல் ஒரு தொடக்க ஏற்பாடுகள் உருவாக்கவும்:
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

2. உங்கள் சர்வர் குறியீட்டில் இடைநிறுத்தங்களை அமைக்கவும்
3. டீபக்கரை இயக்கி Inspector உடன் சோதிக்கவும்

### பொதுவான பிழைத்திருத்த குறிப்புகள்

- பதிவுக்கு `stderr` ஐப் பயன்படுத்துங்கள் - MCP پیامங்களுக்கு `stdout` எப்போதும் மட்டும் உபயோகிக்கப்பட வேண்டும்
- அனைத்து JSON-RPC پیامங்களும் புதிய வரிகளால் பிரிக்கப்பட்டிருப்பதை உறுதிசெய்யுங்கள்
- முதலில் எளிய கருவிகளுடன் சோதனை செய்து பிறகு சிக்கலான செயல்பாடுகளைச் சேர்க்கவும்
- پیام வடிவங்களை சரிபார்க்க Inspector ஐ பயன்படுத்தவும்

## VS Code இல் உங்கள் stdio சர்வரை பயன்படுத்துதல்

MCP stdio சர்வரை உருவாக்கியபின், அதை VS Code உடன் Claude அல்லது மற்ற MCP-உத்தரவாதமான கிளையன்ட்களுடன் ஒருங்கிணைக்கலாம்.

### கட்டமைப்பு

1. Windows-ல் `%APPDATA%\Claude\claude_desktop_config.json` அல்லது Mac-ல் `~/Library/Application Support/Claude/claude_desktop_config.json` இல் MCP கட்டமைப்பு கோப்பை உருவாக்கவும்:

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

2. **Claude ஐ மீண்டும் தொடங்கவும்**: புதிய சர்வர் கட்டமைப்பை ஏற்ற Claude ஐ மூடி திறக்கவும்.

3. **இணைப்பைச் சோதிக்கவும்**: Claude உடன் உரையாடலை தொடங்கி உங்கள் சர்வர் கருவிகளை பயன்படுத்து முயற்சி செய்யவும்:
   - "greeting tool மூலம் என்னை வாழ்த்த முடியுமா?"
   - "15 மற்றும் 27 இன் கூட்டுத்தொகையை கணக்கிடு"
   - "சர்வர் தகவல் என்ன?"

### TypeScript stdio சர்வர் உதாரணம்

பொர referenceக்குத், முழுமையான TypeScript உதாரணம்:

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

// கருவிகளைச் சேர்க்கவும்
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

### .NET stdio சர்வர் உதாரணம்

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

இதன் புது பாடத்தில், நீங்கள் கற்றுக்கொண்டது:

- தற்போதைய **stdio போக்குவரத்தை**ப் பயன்படுத்தி MCP சர்வர்களை உருவாக்குவது (பரிந்துரைக்கப்பட்ட முறை)
- SSE போக்குவரத்தை ஏன் கைவிட்டது மற்றும் stdio மற்றும் Streamable HTTP உடன் மாற்றப்பட்டது என்பதை புரிந்து கொள்வது
- MCP கிளையன்ட்கள் கூப்பிடக்கூடிய கருவிகளை உருவாக்குதல்
- MCP Inspector மூலம் உங்கள் சர்வரை பிழைத்திருத்துதல்
- stdio சர்வரை VS Code மற்றும் Claude உடன் ஒருங்கிணைத்தல்

stdio போக்குவரத்து, கைவிடப்பட்ட SSE முறைமையைவிட எளிதான, அதிக பாதுகாப்பான மற்றும் சிறந்த செயல்திறன் வாய்ந்த MCP சர்வர் கட்டமைப்பை வழங்குகிறது. 2025-06-18 குறிப்புரையின் படி, இது பெரும்பாலான MCP சர்வர் செயலாக்கங்களுக்கு பரிந்துரைக்கப்படும் போக்குவரத்து.

### .NET

1. முதலில் சில கருவிகளை உருவாக்குவோம், இதற்காக *Tools.cs* என்ற கோப்பை கீழ்காணும் உள்ளடக்கத்துடன் உருவாக்குவோம்:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## பயிற்சி: உங்கள் stdio சர்வரை சோதனை செய்வது

இப்போது உங்கள் stdio சர்வரை உருவாக்கியுள்ளீர்கள், அதை சரியாக செயல்படுகின்றதா என சோதிக்கலாம்.

### தேவைகள்

1. MCP Inspector நிறுவப்பட்டுள்ளதை உறுதிசெய்யவும்:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. உங்கள் சர்வர் குறியீட்டை சேமித்து வைத்திருப்பது (எ.கா., `server.py`)

### Inspector உடன் சோதனை

1. **உங்கள் சர்வருடன் Inspector ஐ துவங்குக**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **வலை இடைமுகத்தை திறக்கவும்**: Inspector உங்கள் சர்வர் திறன்களை காட்டும் உலாவி சாளரத்தை திறக்கும்.

3. **கருவிகளைக் சோதிக்கவும்**: 
   - வெவ்வேறு பெயர்களுடன் `get_greeting` கருவியை முயற்சிக்கவும்
   - பல எண்களுடன் `calculate_sum` கருவியை சோதிக்கவும்
   - சர்வர் தகவல்களை காண `get_server_info` கருவியை கூப்பிடுங்கள்

4. **தொடர்பை கண்காணிக்கவும்**: Inspector கிளையன்ட் மற்றும் சர்வர் இடையே பரிமாற்றமாகும் JSON-RPC پیامங்களை காட்டுகிறது.

### நீங்கள் காண வேண்டியது

உங்கள் சர்வர் சரியாக துவங்கினால், பின்வற்றை காணலாம்:
- Inspector இல் சர்வர் திறன்கள் பட்டியலிடப்பட்டிருக்கும்
- சோதனைக்கான கருவிகள் கிடைக்கும்
- வெற்றிகரமான JSON-RPC پیام பரிமாற்றங்கள் நடக்கின்றன
- கருவிகள் பதில்கள் இடைமுகத்தில் காட்டுப்படும்

### பொதுவான பிரச்சினைகள் மற்றும் தீர்வுகள்

**சர்வர் துவங்கவில்லை:**
- அனைத்து சார்பு பொருட்கள் நிறுவப்பட்டுள்ளதா சரிபார்க்கவும்: `pip install mcp`
- Python தொகுப்பு மற்றும் இடைவெளிகளை சரிபார்க்கவும்
- கான்சோலில் பிழை پیامங்கள் தேடவும்

**கருவிகள் காணப்படவில்லை:**
- `@server.tool()` டெகாரேட்டர்கள் உள்ளன என்பதை உறுதிசெய்க
- கருவி செயல்பாடுகள் `main()` முன்பே வரையறுக்கப்பட்டுள்ளன என்பதை உறுதிசெய்க
- சர்வர் சரியாக கட்டமைக்கப்பட்டுள்ளதா என சரிபார்க்கவும்

**இணைப்பு பிரச்சினைகள்:**
- சர்வர் stdio போக்குவரத்தை சரியாக பயன்படுத்துகிறதா என சரிபார்க்கவும்
- பிற செயலிகள் தடுப்பதில்லை என உறுதிசெய்க
- Inspector கட்டளை நடைமுறைகள் சரியுள்ளதா என பார்த்து கொள்ளவும்

## பணி

உங்கள் சர்வரை மேலும் திறன்களுடன் விரிவாக்க முயற்சி செய்க. உதாரணத்திற்கு, [இந்த பக்கம்](https://api.chucknorris.io/) பார்க்கலாம், அங்கு ஒரு API க்கு அழைக்கக்கூடிய கருவி சேர்க்கலாம். சர்வர் எப்படி இருக்க வேண்டும் என்பது உங்கள் விருப்பம். உபயோகிக்கவும் :)

## தீர்வு

[தீர்வு](./solution/README.md) இயங்கும் குறியீட்டுடன் ஒரு சாத்தியமான தீர்வு இங்கே உள்ளது.

## முக்கியக் குறிப்பு

இந்த அத்தியாயத்தில் இருந்து முக்கியமாக எடுத்துக்கொள்ள வேண்டியது:

- stdio போக்குவரத்து உள்ளூர் MCP சர்வர்களுக்கு பரிந்துரைக்கப்படும் முறைமையாகும்.
- stdio போக்குவரத்து MCP சர்வர்களுக்கும் கிளையன்ட்களுக்கும் உள்ளீடு மற்றும் வெளியீடு ஓட்டுகளின் மூலம் ஒருங்கிணைந்த தொடர்பை வழங்குகிறது.
- Inspector மற்றும் Visual Studio Code இரண்டும் stdio சர்வர்களை நேரடியாகப் பயன்படுத்த உதவுகின்றன, இது பிழைத்திருத்தம் மற்றும் ஒருங்கிணைப்பை எளிமையாக்கிறது.

## மாதிரிகள்

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## கூடுதல் வளங்கள்

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## அடுத்து என்ன

## அடுத்த படிகள்

stdio போக்குவரத்துடன் MCP சர்வர்களை உருவாக்குவது கற்றுக்கொண்டபின், மேலான தலைப்புகளை ஆராயலாம்:

- **அடுத்து**: [MCP உடன் HTTP ஸ்ட்ரீமிங் (Streamable HTTP)](../06-http-streaming/README.md) - தொலைநிலை சர்வர்களுக்கான மற்ற ஆதரவு போக்குவரத்தை கற்றுக்கொள்ளவும்
- **மேம்பட்ட**: [MCP பாதுகாப்பு சிறந்த நடைமுறைகள்](../../02-Security/README.md) - உங்கள் MCP சர்வர்களில் பாதுகாப்பை செயல்படுத்தவும்
- **உற்பத்தி**: [பதிவேற்றும் रणनीतிகள்](../09-deployment/README.md) - உற்பத்திக்கு உங்கள் சர்வர்களை வெளியிடவும்

## கூடுதல் வளங்கள்

- [MCP குறிப்புரை 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - அதிகாரப்பூர்வ குறிப்புரை
- [MCP SDK ஆவணம்](https://github.com/modelcontextprotocol/sdk) - அனைத்து மொழிகளுக்கான SDK குறிப்புகள்
- [ஊற்றுமுக உதாரணங்கள்](../../06-CommunityContributions/README.md) - சமூகத்தினரின் கூடுதல் சர்வர் உதாரணங்கள்

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழி மாற்ற சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்தன்மைக்காக முயற்சி செய்கிறோம் என்றாலும், தானாக செய்யப்பட்ட மொழி மாற்றங்களில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதன் மீது கவனம் செலுத்தவும். அதன் சொந்த மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்ப மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டினால் ஏற்பட்ட எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பாக இருக்க மாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->