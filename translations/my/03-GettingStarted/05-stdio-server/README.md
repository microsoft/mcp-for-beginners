# MCP Server with stdio Transport

> **⚠️ အရေးကြီး အပ်ဒိတ်**: MCP Specification 2025-06-18 အရ standalone SSE (Server-Sent Events) transport ကို **deprecated** လုပ်ပြီး "Streamable HTTP" transport ဖြင့် အစားထိုးထားပါသည်။ လက်ရှိ MCP specification တွင် အဓိက transport mechanism နှစ်ခုကို ဖော်ပြထားသည်။
> 1. **stdio** - Standard input/output (ဒေသတွင်း server များအတွက် အကြံပြုထားသည်)
> 2. **Streamable HTTP** - Remote server များအတွက် (အတွင်းပိုင်းတွင် SSE ကို အသုံးပြုနိုင်သည်)
>
> ဒီသင်ခန်းစာကို **stdio transport** ကို အဓိကထားပြီး အပ်ဒိတ်လုပ်ထားပါသည်။ ဒါဟာ MCP server implementation များအတွက် အများဆုံး အကြံပြုထားသော နည်းလမ်းဖြစ်သည်။

stdio transport သည် MCP server များကို client များနှင့် standard input/output stream များမှတဆင့် ဆက်သွယ်စေသည်။ ဒါဟာ လက်ရှိ MCP specification တွင် အများဆုံး အသုံးပြုသော transport mechanism ဖြစ်ပြီး client application များနှင့် လွယ်ကူစွာ ပေါင်းစည်းနိုင်သော server များကို တည်ဆောက်ရန် အကျိုးရှိသော နည်းလမ်းဖြစ်သည်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာတွင် stdio transport ကို အသုံးပြု၍ MCP Server များကို တည်ဆောက်ခြင်းနှင့် အသုံးပြုခြင်းကို လေ့လာပါမည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာအဆုံးတွင် သင်သည် အောက်ပါအရာများကို လုပ်နိုင်မည်ဖြစ်သည်-

- stdio transport ကို အသုံးပြု၍ MCP Server တစ်ခုကို တည်ဆောက်နိုင်မည်။
- MCP Server ကို Inspector ဖြင့် Debug လုပ်နိုင်မည်။
- Visual Studio Code ကို အသုံးပြု၍ MCP Server ကို အသုံးပြုနိုင်မည်။
- လက်ရှိ MCP transport mechanism များကို နားလည်ပြီး stdio ကို အကြံပြုထားသော အကြောင်းရင်းကို သိရှိနိုင်မည်။

## stdio Transport - အလုပ်လုပ်ပုံ

stdio transport သည် MCP specification (2025-06-18) တွင် support လုပ်ထားသော transport type နှစ်ခုအနက် တစ်ခုဖြစ်သည်။ အလုပ်လုပ်ပုံမှာ-

- **ရိုးရှင်းသော ဆက်သွယ်မှု**: Server သည် standard input (`stdin`) မှ JSON-RPC message များကို ဖတ်ပြီး standard output (`stdout`) သို့ message များကို ပို့သည်။
- **Process-based**: Client သည် MCP server ကို subprocess အဖြစ် စတင်လုပ်ဆောင်သည်။
- **Message Format**: Message များသည် individual JSON-RPC request, notification, response များဖြစ်ပြီး newline ဖြင့် ခွဲထားသည်။
- **Logging**: Server သည် UTF-8 string များကို standard error (`stderr`) သို့ log ရေးရန် MAY အသုံးပြုနိုင်သည်။

### အဓိကလိုအပ်ချက်များ:
- Message များသည် newline ဖြင့် ခွဲထားရမည်။ embedded newline မပါဝင်ရ။
- Server သည် `stdout` တွင် valid MCP message မဟုတ်သော အရာများကို မရေးရ။
- Client သည် server ၏ `stdin` တွင် valid MCP message မဟုတ်သော အရာများကို မရေးရ။

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

အထက်ပါ code တွင်-

- `Server` class နှင့် `StdioServerTransport` ကို MCP SDK မှ import လုပ်ထားသည်။
- အခြေခံ configuration နှင့် capabilities ဖြင့် server instance တစ်ခုကို ဖန်တီးထားသည်။

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

အထက်ပါ code တွင်-

- MCP SDK ကို အသုံးပြု၍ server instance တစ်ခုကို ဖန်တီးထားသည်။
- Decorator များကို အသုံးပြု၍ tools များကို သတ်မှတ်ထားသည်။
- stdio_server context manager ကို transport ကို handle လုပ်ရန် အသုံးပြုထားသည်။

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

SSE နှင့် stdio server များ၏ အဓိကကွာခြားချက်မှာ-

- Web server setup သို့မဟုတ် HTTP endpoint မလိုအပ်ပါ။
- Client မှ subprocess အဖြစ် server ကို စတင်လုပ်ဆောင်သည်။
- stdin/stdout stream များမှတဆင့် ဆက်သွယ်သည်။
- တည်ဆောက်ရန်နှင့် debug လုပ်ရန် ပိုမိုရိုးရှင်းသည်။

## လက်တွေ့လေ့ကျင့်ခန်း: stdio Server တစ်ခုကို တည်ဆောက်ခြင်း

Server တစ်ခုကို တည်ဆောက်ရန်အတွက် အောက်ပါအချက်နှစ်ချက်ကို သတိထားရမည်-

- Connection နှင့် message များအတွက် endpoint များကို expose လုပ်ရန် web server ကို အသုံးပြုရမည်။

## Lab: ရိုးရှင်းသော MCP stdio server တစ်ခုကို တည်ဆောက်ခြင်း

ဒီ Lab တွင် stdio transport ကို အသုံးပြု၍ MCP server တစ်ခုကို တည်ဆောက်ပါမည်။ ဒီ server သည် client များက standard Model Context Protocol ကို အသုံးပြု၍ ခေါ်နိုင်သော tools များကို expose လုပ်ပါမည်။

### လိုအပ်ချက်များ

- Python 3.8 သို့မဟုတ် အထက်
- MCP Python SDK: `pip install mcp`
- async programming အခြေခံကို နားလည်ထားရမည်

အခုတော့ ပထမ MCP stdio server ကို တည်ဆောက်လိုက်ကြစို့-

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

## Deprecated SSE နည်းလမ်းနှင့် stdio Transport ၏ အဓိကကွာခြားချက်များ

**Stdio Transport (လက်ရှိ Standard):**
- ရိုးရှင်းသော subprocess model - client သည် server ကို child process အဖြစ် စတင်လုပ်ဆောင်သည်။
- stdin/stdout မှတဆင့် JSON-RPC message များဖြင့် ဆက်သွယ်သည်။
- HTTP server setup မလိုအပ်ပါ။
- ပိုမိုကောင်းမွန်သော performance နှင့် security
- Debug လုပ်ရန်နှင့် တည်ဆောက်ရန် ပိုမိုလွယ်ကူသည်။

**SSE Transport (MCP 2025-06-18 အရ Deprecated):**
- SSE endpoint များပါဝင်သော HTTP server လိုအပ်သည်။
- Web server infrastructure ဖြင့် ပိုမိုရှုပ်ထွေးသော setup
- HTTP endpoint များအတွက် အပို security စဉ်းစားရန်လိုအပ်သည်။
- Web-based scenario များအတွက် Streamable HTTP ဖြင့် အစားထိုးထားသည်။

### stdio server တစ်ခုကို တည်ဆောက်ခြင်း

stdio server တစ်ခုကို တည်ဆောက်ရန်အတွက်-

1. **လိုအပ်သော library များကို import လုပ်ပါ** - MCP server component နှင့် stdio transport ကို လိုအပ်သည်။
2. **Server instance တစ်ခုကို ဖန်တီးပါ** - Server ၏ capabilities ကို သတ်မှတ်ပါ။
3. **Tools များကို သတ်မှတ်ပါ** - expose လုပ်လိုသော functionality များကို ထည့်ပါ။
4. **Transport ကို setup လုပ်ပါ** - stdio communication ကို configure လုပ်ပါ။
5. **Server ကို run လုပ်ပါ** - Server ကို စတင်ပြီး message များကို handle လုပ်ပါ။

အဆင့်ဆင့် တည်ဆောက်ကြစို့-

### အဆင့် 1: ရိုးရှင်းသော stdio server တစ်ခုကို ဖန်တီးပါ

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

### အဆင့် 2: Tools များကို ပိုမိုထည့်သွင်းပါ

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

### အဆင့် 3: Server ကို run လုပ်ပါ

Code ကို `server.py` အဖြစ် save လုပ်ပြီး command line မှ run လုပ်ပါ-

```bash
python server.py
```

Server သည် stdin မှ input ကို စောင့်နေပြီး JSON-RPC message များကို stdio transport မှတဆင့် ဆက်သွယ်ပါမည်။

### အဆင့် 4: Inspector ဖြင့် စမ်းသပ်ခြင်း

MCP Inspector ကို အသုံးပြု၍ server ကို စမ်းသပ်နိုင်သည်-

1. Inspector ကို install လုပ်ပါ: `npx @modelcontextprotocol/inspector`
2. Inspector ကို run လုပ်ပြီး server ကို pointing လုပ်ပါ။
3. သင်ဖန်တီးထားသော tools များကို စမ်းသပ်ပါ။

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## stdio server ကို Debug လုပ်ခြင်း

### MCP Inspector ကို အသုံးပြုခြင်း

MCP Inspector သည် MCP server များကို debug လုပ်ရန်နှင့် စမ်းသပ်ရန် အထောက်အကူပြု tool ဖြစ်သည်။ stdio server နှင့် အသုံးပြုရန်အဆင့်များ-

1. **Inspector ကို install လုပ်ပါ**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ကို run လုပ်ပါ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Server ကို စမ်းသပ်ပါ**: Inspector သည် web interface ကို ပေးပြီး-
   - Server capabilities ကို ကြည့်ရှုနိုင်သည်။
   - Tools များကို parameter များဖြင့် စမ်းသပ်နိုင်သည်။
   - JSON-RPC message များကို စောင့်ကြည့်နိုင်သည်။
   - Connection issue များကို debug လုပ်နိုင်သည်။

### VS Code ကို အသုံးပြု၍ Debug လုပ်ခြင်း

VS Code တွင် MCP server ကို တိုက်ရိုက် debug လုပ်နိုင်သည်-

1. `.vscode/launch.json` တွင် launch configuration တစ်ခု ဖန်တီးပါ:
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

2. Server code တွင် breakpoints ထည့်ပါ။
3. Debugger ကို run လုပ်ပြီး Inspector ဖြင့် စမ်းသပ်ပါ။

### Debugging အတွက် အကြံပြုချက်များ

- `stderr` ကို log ရေးရန် အသုံးပြုပါ - `stdout` သည် MCP message များအတွက်သာ reserved ဖြစ်သည်။
- JSON-RPC message များကို newline ဖြင့် ခွဲထားရန် သေချာပါ။
- ရိုးရှင်းသော tools များကို စမ်းသပ်ပြီးမှ ရှုပ်ထွေးသော functionality များကို ထည့်ပါ။
- Inspector ကို အသုံးပြု၍ message format များကို အတည်ပြုပါ။

## stdio server ကို VS Code တွင် အသုံးပြုခြင်း

stdio server ကို တည်ဆောက်ပြီးနောက် Claude သို့မဟုတ် MCP-compatible client များနှင့် အသုံးပြုနိုင်သည်။

### Configuration

1. **MCP configuration file တစ်ခုကို ဖန်တီးပါ** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) သို့မဟုတ် `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Claude ကို restart လုပ်ပါ**: Claude ကို ပိတ်ပြီး ပြန်ဖွင့်ပါ။

3. **Connection ကို စမ်းသပ်ပါ**: Claude နှင့် စကားပြောစတင်ပြီး server ၏ tools များကို စမ်းသပ်ပါ-
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio server ဥပမာ

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

### .NET stdio server ဥပမာ

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

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာတွင် သင်သည် အောက်ပါအရာများကို လေ့လာခဲ့သည်-

- လက်ရှိ **stdio transport** (အကြံပြုထားသော နည်းလမ်း) ကို အသုံးပြု၍ MCP server များကို တည်ဆောက်ခြင်း
- SSE transport ကို stdio နှင့် Streamable HTTP ဖြင့် အစားထိုးထားသော အကြောင်းရင်းကို နားလည်ခြင်း
- MCP client များက ခေါ်နိုင်သော tools များကို ဖန်တီးခြင်း
- MCP Inspector ကို အသုံးပြု၍ server ကို debug လုပ်ခြင်း
- stdio server ကို VS Code နှင့် Claude တွင် ပေါင်းစည်းခြင်း

stdio transport သည် SSE approach ကို အစားထိုးပြီး MCP server များကို တည်ဆောက်ရန် ပိုမိုရိုးရှင်းသော၊ ပိုမိုလုံခြုံသော၊ ပိုမိုကောင်းမွန်သော နည်းလမ်းဖြစ်သည်။ 2025-06-18 specification အရ MCP server implementation များအတွက် အကြံပြုထားသော transport ဖြစ်သည်။

### .NET

1. Tools များကို ပထမဆုံး ဖန်တီးပါ၊ *Tools.cs* ဖိုင်ကို အောက်ပါ content ဖြင့် ဖန်တီးပါ:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## လက်တွေ့လေ့ကျင့်ခန်း: stdio server ကို စမ်းသပ်ခြင်း

stdio server ကို တည်ဆောက်ပြီးနောက် အလုပ်လုပ်မှုကို စမ်းသပ်ပါ။

### လိုအပ်ချက်များ

1. MCP Inspector ကို install လုပ်ထားရမည်:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Server code ကို save လုပ်ထားရမည် (ဥပမာ - `server.py`)

### Inspector ဖြင့် စမ်းသပ်ခြင်း

1. **Inspector ကို server နှင့်အတူ စတင်ပါ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Web interface ကို ဖွင့်ပါ**: Inspector သည် browser window ကို ဖွင့်ပြီး server ၏ capabilities ကို ပြသပါမည်။

3. **Tools များကို စမ်းသပ်ပါ**: 
   - `get_greeting` tool ကို အမျိုးမျိုးသော name များဖြင့် စမ်းသပ်ပါ။
   - `calculate_sum` tool ကို အမျိုးမျိုးသော number များဖြင့် စမ်းသပ်ပါ။
   - `get_server_info` tool ကို ခေါ်ပြီး server metadata ကို ကြည့်ပါ။

4. **ဆက်သွယ်မှုကို စောင့်ကြည့်ပါ**: Inspector သည် client နှင့် server အကြား JSON-RPC message များကို ပြသပါမည်။

### သင်မြင်ရမည့်အရာများ

Server သည် မှန်ကန်စွာ စတင်လျှင်-
- Server capabilities များကို Inspector တွင် ပြသပါမည်။
- Tools များကို စမ်းသပ်နိုင်ပါမည်။
- JSON-RPC message များအောင်မြင်စွာ လွှဲပြောင်းမှုကို မြင်ရပါမည်။
- Tool response များကို interface တွင် ပြသပါမည်။

### အများဆုံးတွေ့ရသော ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

**Server မစတင်နိုင်ခြင်း:**
- Dependency များကို install လုပ်ထားပါ: `pip install mcp`
- Python syntax နှင့် indentation ကို စစ်ဆေးပါ။
- Console တွင် error message များကို ကြည့်ပါ။

**Tools မပေါ်ခြင်း:**
- `@server.tool()` decorator များကို သေချာစွာ ထည့်ထားပါ။
- Tool function များကို `main()` မတိုင်မီ သတ်မှတ်ထားပါ။
- Server ကို မှန်ကန်စွာ configure လုပ်ထားပါ။

**Connection ပြဿနာများ:**
- Server သည် stdio transport ကို မှန်ကန်စွာ အသုံးပြုနေကြောင်း သေချာပါ။
- အခြား process များ interference မရှိကြောင်း စစ်ဆေးပါ။
- Inspector command syntax ကို စစ်ဆေးပါ။

## အလုပ်ပေးစာ

Server ကို ပိုမို functionality များဖြင့် တိုးချဲ့ပါ။ [ဒီစာမျက်နှာ](https://api.chucknorris.io/) ကို ကြည့်ပြီး API ကို ခေါ်သည့် tool တစ်ခုကို ထည့်ပါ။ Server ကို ဘယ်လို ဖြစ်သင့်တယ်ဆိုတာ သင်ဆုံးဖြတ်ပါ။ ပျော်ရွှင်ပါ :)

## ဖြေရှင်းနည်း

[Solution](./solution/README.md) အလုပ်လုပ်သော code ဖြင့်ဖြေရှင်းနည်းတစ်ခု။

## အဓိက Takeaways

ဒီ chapter မှ အဓိက takeaway များမှာ-

- stdio transport သည် ဒေသတွင်း MCP server များအတွက် အကြံပြုထားသော mechanism ဖြစ်သည်။
- stdio transport သည် standard input/output stream များကို အသုံးပြု၍ MCP server များနှင့် client များအကြား seamless communication ကို ပေးသည်။
- Inspector နှင့် Visual Studio Code ကို အသုံးပြု၍ stdio server များကို တိုက်ရိုက် အသုံးပြုနိုင်ပြီး debug လုပ်ရန်နှင့် integration လုပ်ရန် ရိုးရှင်းစေသည်။

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## အပိုဆောင်း ရင်းမြစ်များ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## အနာဂတ်အတွက် အစီအစဉ်

## Next Steps

stdio transport ကို အသုံးပြု၍ MCP server များကို တည်ဆောက်ပုံကို သင်လေ့လာပြီးနောက် အဆင့်မြင့်သော အကြောင်းအရာများကို လေ့လာနိုင်သည်-

- **Next**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - Remote server များအတွက် support လုပ်ထားသော transport mechanism ကို လေ့လာပါ။
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - MCP server များတွင် security ကို အကောင်အထည်ဖော်ပါ။
- **Production**: [Deployment Strategies](../09-deployment/README.md) - Production အတွက် server များကို deploy လ

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် ရှုလေ့ရှိသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။