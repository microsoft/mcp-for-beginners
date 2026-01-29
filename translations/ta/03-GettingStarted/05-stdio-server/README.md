# MCP Server stdio போக்குவரத்து

> **⚠️ முக்கியமான புதுப்பிப்பு**: MCP Specification 2025-06-18 முதல், தனித்துவமான SSE (Server-Sent Events) போக்குவரத்து **நீக்கப்பட்டது** மற்றும் "Streamable HTTP" போக்குவரத்து மூலம் மாற்றப்பட்டது. தற்போதைய MCP Specification இரண்டு முக்கிய போக்குவரத்து முறைகளை வரையறுக்கிறது:
> 1. **stdio** - நிலையான உள்ளீடு/வெளியீடு (உள்ளூர் சேவைகளுக்கு பரிந்துரைக்கப்படுகிறது)
> 2. **Streamable HTTP** - தொலை சேவைகள், SSE-ஐ உள்நோக்கமாக பயன்படுத்தலாம்
>
> இந்த பாடம் stdio போக்குவரத்து மீது கவனம் செலுத்துவதற்காக புதுப்பிக்கப்பட்டது, இது பெரும்பாலான MCP சேவையக செயல்பாடுகளுக்கு பரிந்துரைக்கப்படும் அணுகுமுறை.

stdio போக்குவரத்து MCP சேவையகங்கள் மற்றும் வாடிக்கையாளர்களுக்கு இடையே நிலையான உள்ளீடு மற்றும் வெளியீட்டு ஸ்ட்ரீம்கள் மூலம் தொடர்பு கொள்ள அனுமதிக்கிறது. இது தற்போதைய MCP Specification-இல் மிகவும் பரவலாக பயன்படுத்தப்படும் மற்றும் பரிந்துரைக்கப்படும் போக்குவரத்து முறையாகும், இது MCP சேவையகங்களை எளிதாகவும் பல்வேறு வாடிக்கையாளர் பயன்பாடுகளுடன் ஒருங்கிணைக்கவும் உதவுகிறது.

## கண்ணோட்டம்

இந்த பாடம் stdio போக்குவரத்து மூலம் MCP சேவையகங்களை உருவாக்குவது மற்றும் பயன்படுத்துவது எப்படி என்பதை உள்ளடக்குகிறது.

## கற்றல் நோக்கங்கள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- stdio போக்குவரத்து மூலம் MCP சேவையகத்தை உருவாக்க முடியும்.
- MCP சேவையகத்தை Inspector மூலம் Debug செய்ய முடியும்.
- Visual Studio Code மூலம் MCP சேவையகத்தை பயன்படுத்த முடியும்.
- தற்போதைய MCP போக்குவரத்து முறைகளை புரிந்து கொள்ளவும், stdio ஏன் பரிந்துரைக்கப்படுகிறது என்பதை அறியவும்.

## stdio போக்குவரத்து - இது எப்படி செயல்படுகிறது

stdio போக்குவரத்து தற்போதைய MCP Specification (2025-06-18) இல் ஆதரிக்கப்படும் இரண்டு போக்குவரத்து வகைகளில் ஒன்றாகும். இது எப்படி செயல்படுகிறது:

- **எளிய தொடர்பு**: சேவையகம் JSON-RPC செய்திகளை நிலையான உள்ளீட்டில் (`stdin`) படிக்கிறது மற்றும் செய்திகளை நிலையான வெளியீட்டில் (`stdout`) அனுப்புகிறது.
- **செயல்முறை அடிப்படையிலானது**: வாடிக்கையாளர் MCP சேவையகத்தை துணை செயல்முறையாக தொடங்குகிறது.
- **செய்தி வடிவம்**: செய்திகள் தனித்துவமான JSON-RPC கோரிக்கைகள், அறிவிப்புகள் அல்லது பதில்கள், புதிய வரிகளால் பிரிக்கப்பட்டவை.
- **பதிவேடு**: சேவையகம் UTF-8 strings-ஐ நிலையான பிழை (`stderr`) மூலம் பதிவு செய்ய MAY எழுதலாம்.

### முக்கிய தேவைகள்:
- செய்திகள் புதிய வரிகளால் பிரிக்கப்பட வேண்டும் மற்றும் உள்ளடக்கப்பட்ட புதிய வரிகளை கொண்டிருக்கக்கூடாது
- சேவையகம் `stdout`-க்கு MCP செய்தியாக இல்லாததை எழுதக்கூடாது
- வாடிக்கையாளர் சேவையகத்தின் `stdin`-க்கு MCP செய்தியாக இல்லாததை எழுதக்கூடாது

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

மேலே உள்ள குறியீட்டில்:

- `Server` வகை மற்றும் `StdioServerTransport`-ஐ MCP SDK-இல் இருந்து இறக்குமதி செய்கிறோம்
- அடிப்படை கட்டமைப்பு மற்றும் திறன்களுடன் சேவையகத்தை உருவாக்குகிறோம்

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

மேலே உள்ள குறியீட்டில்:

- MCP SDK-ஐ பயன்படுத்தி சேவையகத்தை உருவாக்குகிறோம்
- அலுவல்களை அலங்காரங்களுடன் வரையறுக்கிறோம்
- stdio_server context manager-ஐ போக்குவரத்தை கையாள பயன்படுத்துகிறோம்

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

SSE-இன் முக்கிய வித்தியாசம் stdio சேவையகங்கள்:

- வலை சேவையக அமைப்பு அல்லது HTTP முடுக்குகள் தேவைப்படாது
- வாடிக்கையாளர் துணை செயல்முறையாக சேவையகத்தை தொடங்குகிறது
- stdin/stdout ஸ்ட்ரீம்கள் மூலம் தொடர்பு கொள்ளுகிறது
- செயல்படுத்தவும் Debug செய்யவும் எளிதானது

## பயிற்சி: stdio சேவையகத்தை உருவாக்குதல்

சேவையகத்தை உருவாக்க, இரண்டு விஷயங்களை மனதில் கொள்ள வேண்டும்:

- இணைப்பு மற்றும் செய்திகளுக்கான முடுக்குகளை வெளிப்படுத்த வலை சேவையகத்தை பயன்படுத்த வேண்டும்.
## Lab: எளிய MCP stdio சேவையகத்தை உருவாக்குதல்

இந்த Lab-இல், பரிந்துரைக்கப்பட்ட stdio போக்குவரத்தைப் பயன்படுத்தி எளிய MCP சேவையகத்தை உருவாக்குவோம். இந்த சேவையகம் வாடிக்கையாளர்கள் Model Context Protocol-ஐப் பயன்படுத்தி அழைக்கக்கூடிய கருவிகளை வெளிப்படுத்தும்.

### முன் தேவைகள்

- Python 3.8 அல்லது அதற்கு மேல்
- MCP Python SDK: `pip install mcp`
- async programming அடிப்படை புரிதல்

முதலாவது MCP stdio சேவையகத்தை உருவாக்குவோம்:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## நீக்கப்பட்ட SSE அணுகுமுறையிலிருந்து முக்கிய வித்தியாசங்கள்

**Stdio போக்குவரத்து (தற்போதைய தரநிலை):**
- எளிய துணை செயல்முறை முறை - வாடிக்கையாளர் சேவையகத்தை குழந்தை செயல்முறையாக தொடங்குகிறது
- stdin/stdout மூலம் JSON-RPC செய்திகளைப் பயன்படுத்தி தொடர்பு
- HTTP சேவையக அமைப்பு தேவைப்படாது
- சிறந்த செயல்திறன் மற்றும் பாதுகாப்பு
- Debug செய்யவும் உருவாக்கவும் எளிதானது

**SSE போக்குவரத்து (MCP 2025-06-18 முதல் நீக்கப்பட்டது):**
- SSE முடுக்குகளுடன் HTTP சேவையகம் தேவைப்பட்டது
- வலை சேவையக உள்கட்டமைப்புடன் சிக்கலான அமைப்பு
- HTTP முடுக்குகளுக்கான கூடுதல் பாதுகாப்பு கருத்துக்கள்
- வலை அடிப்படையிலான சூழல்களுக்கு Streamable HTTP மூலம் மாற்றப்பட்டது

### stdio போக்குவரத்துடன் சேவையகத்தை உருவாக்குதல்

stdio சேவையகத்தை உருவாக்க, நாம் செய்ய வேண்டியது:

1. **தேவையான நூலகங்களை இறக்குமதி செய்யுங்கள்** - MCP சேவையக கூறுகள் மற்றும் stdio போக்குவரத்து தேவை
2. **சேவையகத்தை உருவாக்குங்கள்** - அதன் திறன்களுடன் சேவையகத்தை வரையறுக்கவும்
3. **கருவிகளை வரையறுக்கவும்** - வெளிப்படுத்த விரும்பும் செயல்பாடுகளைச் சேர்க்கவும்
4. **போக்குவரத்தை அமைக்கவும்** - stdio தொடர்பை உள்ளமைக்கவும்
5. **சேவையகத்தை இயக்கவும்** - சேவையகத்தை தொடங்கவும் மற்றும் செய்திகளை கையாளவும்

இதை படிப்படியாக உருவாக்குவோம்:

### படி 1: அடிப்படை stdio சேவையகத்தை உருவாக்குதல்

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### படி 2: மேலும் கருவிகளைச் சேர்க்கவும்

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

குறியீட்டை `server.py` என சேமித்து, கட்டளைக் கோரியிலிருந்து இயக்கவும்:

```bash
python server.py
```

சேவையகம் தொடங்கி stdin-இல் உள்ளீட்டுக்காக காத்திருக்கும். இது stdio போக்குவரத்தில் JSON-RPC செய்திகளைப் பயன்படுத்தி தொடர்பு கொள்ளும்.

### படி 4: Inspector மூலம் சோதனை

MCP Inspector-ஐப் பயன்படுத்தி உங்கள் சேவையகத்தை சோதிக்கலாம்:

1. Inspector-ஐ நிறுவவும்: `npx @modelcontextprotocol/inspector`
2. Inspector-ஐ இயக்கி உங்கள் சேவையகத்தைச் சுட்டிக்காட்டவும்
3. நீங்கள் உருவாக்கிய கருவிகளை சோதிக்கவும்

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## உங்கள் stdio சேவையகத்தை Debug செய்யுதல்

### MCP Inspector பயன்படுத்துதல்

MCP Inspector என்பது MCP சேவையகங்களை Debug மற்றும் சோதனை செய்ய மதிப்புமிக்க கருவியாகும். stdio சேவையகத்துடன் இதைப் பயன்படுத்துவது எப்படி:

1. **Inspector-ஐ நிறுவவும்**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector-ஐ இயக்கவும்**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **உங்கள் சேவையகத்தை சோதிக்கவும்**: Inspector ஒரு வலை இடைமுகத்தை வழங்குகிறது, இதில்:
   - சேவையக திறன்களைப் பார்க்கவும்
   - பல்வேறு அளவுருக்களுடன் கருவிகளை சோதிக்கவும்
   - JSON-RPC செய்திகளை கண்காணிக்கவும்
   - இணைப்பு பிரச்சினைகளை Debug செய்யவும்

### VS Code பயன்படுத்துதல்

VS Code-இல் உங்கள் MCP சேவையகத்தை நேரடியாக Debug செய்யலாம்:

1. `.vscode/launch.json`-இல் ஒரு Launch Configuration உருவாக்கவும்:
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

2. உங்கள் சேவையக குறியீட்டில் Breakpoints அமைக்கவும்
3. Debugger-ஐ இயக்கி Inspector மூலம் சோதிக்கவும்

### பொதுவான Debugging குறிப்புகள்

- `stderr`-ஐ பதிவு செய்ய பயன்படுத்தவும் - MCP செய்திகளுக்காக `stdout`-ஐ எழுத வேண்டாம்
- அனைத்து JSON-RPC செய்திகளும் புதிய வரிகளால் பிரிக்கப்பட வேண்டும் என்பதை உறுதிப்படுத்தவும்
- சிக்கலான செயல்பாடுகளைச் சேர்க்கும் முன் எளிய கருவிகளை முதலில் சோதிக்கவும்
- Inspector-ஐ பயன்படுத்தி செய்தி வடிவங்களை சரிபார்க்கவும்

## உங்கள் stdio சேவையகத்தை VS Code-இல் பயன்படுத்துதல்

stdio சேவையகத்தை உருவாக்கிய பிறகு, Claude அல்லது MCP-இன் இணக்கமான வாடிக்கையாளர்களுடன் பயன்படுத்த அதை VS Code-இல் ஒருங்கிணைக்கலாம்.

### அமைப்பு

1. **MCP அமைப்பு கோப்பை உருவாக்கவும்** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) அல்லது `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Claude-ஐ மீண்டும் தொடங்கவும்**: புதிய சேவையக அமைப்பை ஏற்றுவதற்கு Claude-ஐ மூடவும் மற்றும் மீண்டும் திறக்கவும்.

3. **இணைப்பை சோதிக்கவும்**: Claude உடன் உரையாடலைத் தொடங்கவும் மற்றும் உங்கள் சேவையகத்தின் கருவிகளை முயற்சிக்கவும்:
   - "வாழ்த்தும் கருவியைப் பயன்படுத்தி என்னை வாழ்த்த முடியுமா?"
   - "15 மற்றும் 27-இன் கூட்டுத்தொகையை கணக்கிடுங்கள்"
   - "சேவையக தகவல் என்ன?"

### TypeScript stdio சேவையக உதாரணம்

இது ஒரு முழுமையான TypeScript உதாரணம்:

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

// Add tools
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

### .NET stdio சேவையக உதாரணம்

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

## சுருக்கம்

இந்த புதுப்பிக்கப்பட்ட பாடத்தில், நீங்கள்:

- stdio போக்குவரத்தைப் பயன்படுத்தி தற்போதைய MCP சேவையகங்களை உருவாக்குவது (பரிந்துரைக்கப்பட்ட அணுகுமுறை)
- SSE போக்குவரத்து stdio மற்றும் Streamable HTTP-க்கு ஏன் மாற்றப்பட்டது என்பதைப் புரிந்து கொள்ளுங்கள்
- MCP வாடிக்கையாளர்களால் அழைக்கக்கூடிய கருவிகளை உருவாக்குங்கள்
- MCP Inspector மூலம் உங்கள் சேவையகத்தை Debug செய்யுங்கள்
- உங்கள் stdio சேவையகத்தை VS Code மற்றும் Claude உடன் ஒருங்கிணைக்கவும்

stdio போக்குவரத்து, நீக்கப்பட்ட SSE அணுகுமுறையுடன் ஒப்பிடும்போது, ​​MCP சேவையகங்களை உருவாக்க எளிமையான, பாதுகாப்பான மற்றும் செயல்திறனான வழியை வழங்குகிறது. MCP சேவையக செயல்பாடுகளுக்கு பரிந்துரைக்கப்படும் போக்குவரத்து இது 2025-06-18 Specification-இன் படி.

### .NET

1. முதலில் சில கருவிகளை உருவாக்குவோம், இதற்காக *Tools.cs* என்ற கோப்பை பின்வரும் உள்ளடக்கத்துடன் உருவாக்குவோம்:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## பயிற்சி: உங்கள் stdio சேவையகத்தை சோதித்தல்

stdio சேவையகத்தை உருவாக்கிய பிறகு, இது சரியாக செயல்படுகிறதா என்பதை உறுதிப்படுத்த சோதிக்கலாம்.

### முன் தேவைகள்

1. MCP Inspector நிறுவப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. உங்கள் சேவையக குறியீடு சேமிக்கப்பட்டிருக்க வேண்டும் (எ.கா., `server.py` என)

### Inspector மூலம் சோதனை

1. **உங்கள் சேவையகத்துடன் Inspector-ஐ தொடங்கவும்**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **வலை இடைமுகத்தை திறக்கவும்**: Inspector உங்கள் சேவையகத்தின் திறன்களை காட்டும் ஒரு உலாவி சாளரத்தைத் திறக்கும்.

3. **கருவிகளை சோதிக்கவும்**: 
   - `get_greeting` கருவியை பல்வேறு பெயர்களுடன் முயற்சிக்கவும்
   - `calculate_sum` கருவியை பல்வேறு எண்களுடன் சோதிக்கவும்
   - `get_server_info` கருவியை அழைத்து சேவையக metadata-ஐப் பார்க்கவும்

4. **தொடர்பை கண்காணிக்கவும்**: Inspector வாடிக்கையாளர் மற்றும் சேவையகத்துக்கு இடையே பரிமாறப்படும் JSON-RPC செய்திகளை காட்டுகிறது.

### நீங்கள் பார்க்க வேண்டியது

உங்கள் சேவையகம் சரியாக தொடங்கும்போது, நீங்கள் பார்க்க வேண்டும்:
- Inspector-இல் சேவையக திறன்கள் பட்டியலிடப்பட்டுள்ளன
- சோதனைக்கு கருவிகள் கிடைக்கின்றன
- JSON-RPC செய்தி பரிமாற்றங்கள் வெற்றிகரமாக
- இடைமுகத்தில் கருவி பதில்கள் காட்டப்படுகின்றன

### பொதுவான பிரச்சினைகள் மற்றும் தீர்வுகள்

**சேவையகம் தொடங்கவில்லை:**
- அனைத்து சார்புகள் நிறுவப்பட்டுள்ளதா என்பதை சரிபார்க்கவும்: `pip install mcp`
- Python syntax மற்றும் indentation சரிபார்க்கவும்
- Console-இல் பிழை செய்திகளைப் பார்க்கவும்

**கருவிகள் தோன்றவில்லை:**
- `@server.tool()` அலங்காரங்கள் உள்ளதா என்பதை உறுதிப்படுத்தவும்
- `main()`-க்கு முன் கருவி செயல்பாடுகள் வரையறுக்கப்பட்டுள்ளதா என்பதை சரிபார்க்கவும்
- சேவையகம் சரியாக உள்ளமைக்கப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்

**இணைப்பு பிரச்சினைகள்:**
- சேவையகம் stdio போக்குவரத்தை சரியாக பயன்படுத்துகிறதா என்பதை உறுதிப்படுத்தவும்
- பிற செயல்முறைகள் தடைசெய்கிறதா என்பதை சரிபார்க்கவும்
- Inspector கட்டளை syntax சரிபார்க்கவும்

## பணிக்கூற்று

உங்கள் சேவையகத்தை மேலும் திறன்களுடன் உருவாக்க முயற்சிக்கவும். [இந்த பக்கம்](https://api.chucknorris.io/) பார்க்கவும், உதாரணமாக, API-ஐ அழைக்கும் கருவியைச் சேர்க்கவும். சேவையகம் எப்படி இருக்க வேண்டும் என்பதை நீங்கள் முடிவு செய்யுங்கள். மகிழுங்கள் :)
## தீர்வு

[Solution](./solution/README.md) வேலை செய்யும் குறியீட்டுடன் ஒரு சாத்தியமான தீர்வு.

## முக்கிய எடுத்துக்காட்டுகள்

இந்த அத்தியாயத்தின் முக்கிய எடுத்துக்காட்டுகள் பின்வருவன:

- stdio போக்குவரத்து உள்ளூர் MCP சேவைகளுக்கு பரிந்துரைக்கப்படும் முறையாகும்.
- stdio போக்குவரத்து MCP சேவையகங்கள் மற்றும் வாடிக்கையாளர்களுக்கு இடையே நிலையான உள்ளீடு மற்றும் வெளியீட்டு ஸ்ட்ரீம்களைப் பயன்படுத்தி தொடர்பு கொள்ள அனுமதிக்கிறது.
- Inspector மற்றும் Visual Studio Code இரண்டையும் stdio சேவையகங்களை நேரடியாக Debug மற்றும் ஒருங்கிணைக்க பயன்படுத்தலாம், இது Debug மற்றும் ஒருங்கிணைப்பை எளிதாக்குகிறது.

## மாதிரிகள் 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## கூடுதல் வளங்கள்

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## அடுத்தது என்ன

## அடுத்த படிகள்

stdio போக்குவரத்துடன் MCP சேவையகங்களை உருவாக்குவது எப்படி என்பதை நீங்கள் கற்றுக்கொண்ட பிறகு, மேலும் மேம்பட்ட தலைப்புகளை ஆராயலாம்:

- **அடுத்தது**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - தொலை சேவைகளுக்கான மற்றொரு ஆதரிக்கப்படும் போக்குவரத்து முறையை கற்றுக்கொள்ளுங்கள்
- **மேம்பட்டது**: [MCP Security Best Practices](../../02-Security/README.md) - MCP சேவையகங்களில் பாதுகாப்பை செயல்படுத்துங்கள்
- **உற்பத்தி**: [Deployment Strategies](../09-deployment/README.md) - உற்பத்தி பயன்பாட்டிற்கான உங்கள் சேவையகங்களை வெளியிடுங்கள்

## கூடுதல் வளங்கள்

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - அதிகாரப்பூர்வ Specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - அனைத்து மொழிகளுக்கான SDK குறிப்புகள்
- [Community Examples](../../06-CommunityContributions/README.md) - சமூகத்திலிருந்து மேலும் சேவையக உதாரணங்கள்

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.