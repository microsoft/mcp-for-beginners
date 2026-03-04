# MCP ဆာဗာကို stdio သယ်ယူပို့ဆောင်မှုဖြင့်

> **⚠️ အရေးကြီးသော အချက်ပြချက်** - MCP အချက်အလက် အမျိုးအစား 2025-06-18 အဆိုအရ၊ သီးသန့် SSE (Server-Sent Events) သယ်ယူပို့ဆောင်မှုကို **အသုံးမပြုတော့ပဲ** "Streamable HTTP" သယ်ယူပို့ဆောင်မှုဖြင့် ပြောင်းလဲခဲ့ပါသည်။ လက်ရှိ MCP အချက်အလက်သည် သယ်ယူပို့ဆောင်မှုရေးရာအလုပ်သမားနှစ်မျိုးကို သတ်မှတ်ထားသည်-
> 1. **stdio** - စံသတ်မှတ်သည့် ဝင်ရိုး-ထွက်ရိုး (ဒေသခံ ဆာဗာများအတွက် အကြံပြု)
> 2. **Streamable HTTP** - SSE ကို အတွင်းပိုင်းတွင် အသုံးပြုနိုင်သော ဝေးလံသော ဆာဗာများအတွက်
>
> ဒီသင်ခန်းစာကို MCP ဆာဗာများအတွက် ဘာသာရပ်သီးသန့် **stdio သယ်ယူပို့ဆောင်မှု** ကို ဦးတည်၍ ပြင်ဆင်ထားပါသည်။

stdio သယ်ယူပို့ဆောင်မှုက MCP ဆာဗာများကို client များနှင့် စံသတ်မှတ်သော ဝင်-ထွက်စီးကြောင်းများမှတဆင့် ဆက်သွယ်နိုင်စေသည်။ လက်ရှိ MCP သတ်မှတ်ချက်အရ အများဆုံး အသုံးပြုနည်းဖြစ်ပြီး သင့်လျော်သော ဆာဗာများဆောက်ရန် အလွယ်ကူ၍ ထိရောက်သော နည်းလမ်းဖြစ်သည်။

## အနှစ်ချုပ်

ဒီသင်ခန်းစာမှာ stdio သယ်ယူပို့ဆောင်မှုကို အသုံးပြုပြီး MCP ဆာဗာများဘယ်လို ဆောက်ပြီး အသုံးပြုရမယ်ဆိုတာ ဆွေးနွေးပါမယ်။

## သင်ယူရမည့် ရည်ရွယ်ချက်များ

ဒီသင်ခန်းစာပြီးဆုံးသောအချိန်မှာ သင်ဦးတည်နိုင်မှာတွေက-

- stdio သယ်ယူပို့ဆောင်မှုဖြင့် MCP ဆာဗာတစ်ခု တည်ဆောက်ရန်။
- Inspector ကို အသုံးပြု၍ MCP ဆာဗာကို debug ပြုလုပ်နိုင်ရန်။
- Visual Studio Code ဖြင့် MCP ဆာဗာကို သုံးနိုင်ရန်။
- လက်ရှိ MCP သယ်ယူပို့ဆောင်မှုနည်းလမ်းများနဲ့ stdio ကို ဘာကြောင့် အကြံပြုကြောင်းနားလည်ရန်။

## stdio သယ်ယူပို့ဆောင်မှု - အလုပ်လုပ်ပုံ

stdio သယ်ယူပို့ဆောင်မှုဟာ လက်ရှိ MCP သတ်မှတ်ချက် (2025-06-18) အရ ပံ့ပိုးထားသည့် သယ်ယူပို့ဆောင်မှု၂မျိုးထဲက တစ်ခုဖြစ်ပြီး အလုပ်လုပ်ပုံမှာ-

- **ရိုးရွင်းသော ဆက်သွယ်မှု** - ဆာဗာက JSON-RPC ပုံစံနဲ့ စံထွက်ဝင်စီးကြောင်း (`stdin`) မှ ပို့သော စာတိုက်များကို ဖတ်ပြီး စံထွက်ထွက်စီးကြောင်း (`stdout`) မှာ မက်ဆေ့ခ်ျများ ပို့ဆောင်သည်။
- **Process-based** - Client က MCP ဆာဗာကို subprocess အဖြစ် စတင်အသုံးပြုသည်။
- **မက်ဆေ့ခ်ျ ပုံစံ** - မက်ဆေ့ချ်များမှာ JSON-RPC တစ်ခုချင်းစာတို, အသိပေးချက်၊ ဒါမှမဟုတ် တုံ့ပြန်ချက်များဖြစ်ပြီး newlines ဖြင့် ခွဲခြားထားသည်။
- **မှတ်တမ်းတင်ခြင်း** - ဆာဗာက `stderr` မှာ UTF-8 စာတန်းများရေးနိုင်ပြီး မှတ်တမ်းတင်ရာတွင် အသုံးပြုသည်။

### အဓိကလိုအပ်ချက်များ-
- မက်ဆေ့ခ်ျများကို newlines ဖြင့် ခွဲခြားပေးရမည်၊ မက်ဆေ့ချ်ထဲမှာ embedded newlines မတွေ့ရမည်။
- ဆာဗာမှ `stdout` ထဲသို့ MCP မက်ဆေ့ခ်် မဟုတ်သော အရာကို မရေးသင့်ပါ။
- Client မှ ဆာဗာ၏ `stdin` ကို MCP မက်ဆေ့ခ်် မဟုတ်သော အရာဖြင့် မရေးသင့်ပါ။

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

အထက်ပါ ကုဒ်မှာ-

- MCP SDK မှ `Server` class နှင့် `StdioServerTransport` ကို ထည့်သွင်းသုံးစွဲသည်။
- အခြေခံ configuration နှင့် စွမ်းဆောင်ရည်များဖြင့် ဆာဗာ ကို instantiate လုပ်သည်။

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ဆာဗာ အထူးကုန်ပစ္စည်း ဖန်တီးပါ။
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

အထက်ပါ ကုဒ်မှာ-

- MCP SDK ဖြင့် ဆာဗာအသစ်တစ်ခု ဖန်တီးသည်။
- decorator များဖြင့် tools ကို သတ်မှတ်သည်။
- stdio_server context manager ဖြင့် သယ်ယူပို့ဆောင်မှုကို ထိန်းချုပ်သည်။

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

SSE နှင့်အနည်းဆုံး ကွာခြားချက်မှာ stdio ဆာဗာများသည်-

- web server setup သို့မဟုတ် HTTP endpoint မလိုအပ်ပဲ
- client မှ subprocess အဖြစ် စတင်
- stdin/stdout စီးကြောင်းများမှတဆင့် ဆက်သွယ်
- အလွယ်တကူ ဆောက်လုပ်ရန် နှင့် debug ပြုလုပ်ရန် ပိုမိုလွယ်ကူသည်။

## လေ့ကျင့်ခန်း - stdio ဆာဗာတစ်ခု ဖန်တီးခြင်း

ကျွန်တော်တို့ ဆာဗာဖန်တီးရန်အတွက် ယခုအရာ၂ခုကို မှတ်သားထားရမှာ ဖြစ်သည်-

- လက်လှမ်းမီရန် endpoints ဖွင့်ရန် Web server จำเป็นဖြစ်သည်။

## လက်တွေ့ လေ့ကျင့်ခန်း - ရိုးရှင်းသော MCP stdio ဆာဗာတစ်ခု ဖန်တီးခြင်း

ဒီလက်တွေ့မှာ အကြံပြုထားသည့် stdio သယ်ယူပို့ဆောင်မှုကို အသုံးပြုပြီး ရိုးရှင်းသည့် MCP ဆာဗာတစ်ခု ဖန်တီးပါမည်။ ဒီဆာဗာက Model Context Protocol အသုံးပြုတဲ့ client များ ဖုန်းခေါ်နိုင်သော tools များကို ဖော်ပြပါမယ်။

### မပြင်ဆင်မီ လိုအပ်ချက်များ

- Python 3.8 သို့မဟုတ် အထက်
- MCP Python SDK - `pip install mcp`
- async programming အခြေခံသဘောတရား နားလည်မှု

ယခု MCP stdio ဆာဗာ ထူထောင်ခြင်းစတင်ကြပါစို့-

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# မှတ်တမ်းတင်ခြင်းကို ဖွဲ့စည်းပါ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ဆာဗာကို လုပ်ပါ
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
    # stdio သယ်ယူပို့ဆောင်မှုကို အသုံးပြုပါ
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ရှေ့နောက် SSE နည်းလမ်းမှ အသစ် stdio နည်းလမ်း ထွက်ခြားချက်များ

**Stdio Transport (လက်ရှိ စံ)**:
- ရိုးရွင်းသော subprocess မော်ဒယ် - client က ဆာဗာကို child process အဖြစ် စတင်
- stdin/stdout မှ JSON-RPC စာတိုများဖြင့် ဆက်သွယ်မှု
- HTTP server နှင့် endpoint မလိုအပ်
- လုပ်ဆောင်ချက် မြန်ဆန်ပြီး လုံခြုံမှုကောင်းမွန်
- debug ပြုလုပ်ရလွယ်ကူပြီး ဖော်ဆောင်သူများ အဆင်ပြေ

**SSE Transport (MCP 2025-06-18 မှ ရုပ်သိမ်း)**:
- HTTP server ပေါ်တွင် SSE endpoint များလိုအပ်
- web server infrastructure ဖြင့် မြှပ်နှံတည်ဆောက်မှုရှုပ်ထွေး
- HTTP endpoint များအတွက် လုံခြုံရေး ဆောင်ရွက်ချက်များ လိုအပ်
- Streamable HTTP ဖြင့် အစားထိုးပြောင်းလဲထားပြီး

### stdio သယ်ယူပို့ဆောင်မှုဖြင့် ဆာဗာ ဖန်တီးခြင်း

stdio ဆာဗာ ဖန်တီးရန်လိုအပ်ချက်များ-

1. **လိုအပ်သော libraries များကို ယူပါ** - MCP ဆာဗာ အသုံးပြုမှုများနှင့် stdio transport
2. **ဆာဗာကို instantiate လုပ်ပါ** - ဆာဗာ၏ စွမ်းဆောင်ရည်ကို သတ်မှတ်ပါ
3. **tools များကို သတ်မှတ်ပါ** - ဖော်ပြလိုသော လုပ်ဆောင်ချက်များ ထည့်ပါ
4. **သယ်ယူပို့ဆောင်မှုကို ပြင်ဆင်ပါ** - stdio ဆက်သွယ်မှု ဖွဲ့စည်းပါ
5. **ဆာဗာကို စတင်ပါ** - ဆာဗာကို run နိုင်ရန် ပြင်ဆင်ပါ

အဆင့်ဆင့် တည်ဆောက်ကြရအောင်-

### အဆင့် ၁: ရိုးရှင်းသော stdio ဆာဗာတစ်ခု ဖန်တီးခြင်း

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# မှတ်တမ်းတင်မှု ကို ပုံသဏ္ဍာန်ချ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ဆာဗာကို ဖန်တီးပါ
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

### အဆင့် ၂: tools များ များသောကြာ ထပ်ထည့်ခြင်း

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

### အဆင့် ၃: ဆာဗာ run ပြုလုပ်ခြင်း

`server.py` အဖြစ် သိမ်းပြီး command line မှ run ပါ။

```bash
python server.py
```

ဆာဗာက စတင်ပြီး stdin မှ မက်ဆေ့ခ်ျများကို စောင့်ကြည့်သည်။ JSON-RPC မက်ဆေ့ခ်ျများဖြင့် stdio သယ်ယူပို့ဆောင်မှုမှာ ဆက်သွယ်သည်။

### အဆင့် ၄: Inspector ဖြင့် စမ်းသပ်ခြင်း

မိမိဆာဗာကို MCP Inspector ဖြင့် စမ်းသပ်နိုင်သည်။

1. Inspector ကို တင်ပါ - `npx @modelcontextprotocol/inspector`
2. Inspector ကို run ပြီး ဆာဗာထံ ချိန်ညှိပါ
3. သင့်လုပ်ထားသော tools များကို စမ်းသပ်ကြည့်ပါ

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio ဆာဗာ Debug ပြုလုပ်ခြင်း

### MCP Inspector အသုံးပြုခြင်း

MCP Inspector က MCP ဆာဗာများ Debug နှင့် စမ်းသပ်ရာတွင် အကောင်းဆုံး ကိရိယာ ဖြစ်သည်။ stdioဆာဗာနှင့် လုပ်ဆောင်မည် -

1. **Inspector ကို တင်ပါ**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ကို run ပါ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ဆာဗာကို စမ်းသပ်ပါ**: Inspector သည် web interface ပေးပြီး-
   - ဆာဗာ၏ စွမ်းဆောင်ရည်များ ကြည့်ရှုနိုင်
   - tools များကို အမျိုးမျိုးသော parameters ဖြင့် စမ်းသပ်နိုင်
   - JSON-RPC မက်ဆေ့ခ်ျများ ပေးပို့မှု ကြည့်ရှုနိုင်
   - ချိတ်ဆက်မႈပြဿနာများကို Debug လုပ်နိုင်

### VS Code အသုံးပြုခြင်း

VS Code တိုက်ရိုက် မိမိ MCP ဆာဗာကို Debug ပြုလုပ်နိုင်သည်-

1. `.vscode/launch.json` တည်ဆောက်ပါ -
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

2. ဆာဗာကုဒ်တွင် breakpoint တွေထားပါ
3. Debugger ကို run နှင့် Inspector ဖြင့် စမ်းသပ်ပါ

### ပြဿနာများနှင့် debugging အကြံပေးချက်များ

- `stderr` ကို log မှာသာ အသုံးပြုပါ - MCP message မဟုတ်သည့်စာတွေကို `stdout` မှာ ရေးမထားပါနှင့်။
- JSON-RPC message အားလုံးကို newline ဖြင့် ခွဲစိတ်ထားสิ
- ရိုးရှင်းသော tools များ အရင် စမ်းသပ်ပြီး အဆင့်မြှင့် ကြိုတင်လုပ်ပါ
- Inspector ဖြင့် message format မှန်ကန်မှု စစ်ဆေးပါ

## VS Code မှ stdio ဆာဗာကို သုံးခြင်း

MCP stdio ဆာဗာကို တည်ဆောက်ပြီးပါက VS Code နှင့် Claude သို့မဟုတ် MCP သဟဇာတ client များနှင့် ပေါင်းစည်း၍ အသုံးပြုနိုင်သည်။

### ဖော်ပြချက်

1. MCP configuration ဖိုင်တစ်ခု ဖန်တီးပါ၊ Windows မှာ `%APPDATA%\Claude\claude_desktop_config.json`၊ Mac မှာ `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

2. Claude ကို ပြန်စတင်ပါ - Claude ကိုပိတ်ပြီး ပြန်ဖွင့်ပါ။
3. ချိတ်ဆက်မှု စမ်းသပ်ပါ - Claude နှင့် စကားပြောစရာဆွေးနွေးပြီး သင့်ဆာဗာ tools များ အသုံးပြုကြည့်ပါ-
   - "greeting tool ကို အသုံးပြုပြီး ဂရုတစိုက် ပြောပါ"
   - "15 နှင့် 27 ကို ပေါင်းချက်တွက်ပါ"
   - "ဆာဗာအချက်အလက်တွေ ဘာတွေလဲ?"

### TypeScript stdio ဆာဗာ ဥပမာ

အောက်မှာပြည့်စုံသော TypeScript ဥပမာ ပါရှိသည်-

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

// ကိရိယာများ ထည့်သွင်းပါ
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

### .NET stdio ဆာဗာ ဥပမာ

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

## အနှစ်ချုပ်

ဒီပြင်ဆင်ထားသော သင်ခန်းစာဖြင့် သင်-

- လက်ရှိ **stdio သယ်ယူပို့ဆောင်မှု** ဖြင့် MCP ဆာဗာကို ဘယ်လို ဖန်တီးရပြီး လမ်းညွှန်ချက်ကို သုံးဖြတ်နိုင်သလဲကို သင်ယူပြီး
- SSE သယ်ယူပို့ဆောင်မှုအား ရုပ်သိမ်းဘို့ အကြောင်းရင်းနဲ့ stdio, Streamable HTTP တို့ကို နားလည်သွားပြီး
- MCP clients မှ ခေါ်ယူနိုင်သော tools များဖန်တီးပြီး
- MCP Inspector ဖြင့် ဆာဗာကို debug လုပ်နည်းကို သိရှိပြီး
- VS Code နှင့် Claude နှင့် ပေါင်းစည်းအသုံးပြုနည်းကို ရရှိသည်

stdio သယ်ယူပို့ဆောင်မှုသည် မပြောင်းလဲတော့သော SSE နည်းလမ်းထက် ပိုမို ရိုးရှင်းပြီး၊ လုံခြုံမှုကောင်းမြင့်နေရုံသာမက လုပ်ဆောင်ချက်လည်းမြန်ဆန်သော MCP ဆာဗာဆောက်ရန် အကြံပြုသော နည်းလမ်းဖြစ်သည်။ 2025-06-18 MCP Specification အရ MCP ဆာဗာနှင့်အတူ ထိပ်တန်းအကြံပြုနည်းဖြစ်သည်။

### .NET

1. အရင်ဆုံး tools တချို့ ဖန်တီးပါမယ်။ ဒီအတွက် *Tools.cs* ဖိုင်တစ်ခုကို အောက်ပါအကြောင်းအရာဖြင့် ဖန်တီးပါ–

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## လေ့ကျင့်ခန်း - stdio ဆာဗာ စမ်းသပ်ခြင်း

stdio ဆာဗာတည်ဆောက်ပြီးသည့်အခါ မှန်ကန်စွာ အလုပ်လုပ်မလား စမ်းသပ်ကြည့်ရအောင်။

### လိုအပ်ချက်များ

1. MCP Inspector ကို တပ်ဆင်ထားခြင်းရှိပါစေ-
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. ဆာဗာကုတ်ကို သိမ်းပြီး ရှိပါက (ဥပမာ - `server.py`)

### Inspector ဖြင့် စမ်းသပ်ခြင်း

1. **မိမိဆာဗာဖြင့် Inspector စတင်ပါ** -
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **web interface ကို ဖွင့်ပါ** - Inspector က browser window တစ်ခု ဖွင့်ပြီး ဆာဗာစွမ်းဆောင်ရည်များကို ပြသမည်။
3. **tools များကို စမ်းသပ်ပါ** -
   - `get_greeting` tool ကို အမည်အမျိုးမျိုးဖြင့် စမ်းသပ်ပါ
   - `calculate_sum` tool ကို ကိန်းဂဏန်း များစွာဖြင့် စမ်းသပ်ပါ
   - `get_server_info` tool ကို ခေါ်၍ ဆာဗာ meta data ကြည့်ပါ
4. **ဆက်သွယ်မှုကို ကြည့်ရှုပါ** - Inspector က client နှင့် ဆာဗာအကြား JSON-RPC မက်ဆေ့ချ်များကို ပြသသည်။

### ဘာတွေ မြင်ရမှာလဲ

ဆာဗာမှတဆင့် စတင်တာလိမ့်မယ်ဆိုရင်-

- Inspector မှာ ဆာဗာစွမ်းဆောင်ရည်များ ကိုကြည့်ရှုနိုင်မည်
- စမ်းသပ်ရန် tools များ တွေ့ရမည်
- JSON-RPC မက်ဆေ့ခ်ျများ လွှဲပြောင်းမှု အောင်မြင်မှုရှိ
- Interface တွင် tools များ၏ တုံ့ပြန်ချက်တွေ ပြသမည်

### ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

**ဆာဗာ မစတင်ခြင်း:**
- dependency များ ရှိ/မရှိ စစ်ဆေးပါ - `pip install mcp`
- Python syntax နှင့် indentation ကို စစ်ဆေးပါ
- console မှ error message များ ကြည့်ရှုပါ

**tools မတင်ပြခြင်း:**
- `@server.tool()` decorators ရှိ/မရှိ စစ်ဆေးပါ
- tool function များကို `main()` အရှေ့မှာ သတ်မှတ်ထားသည်ကို သေချာပါစေ
- ဆာဗာကို မှန်ကန်စွာ configure လုပ်ထားပါ

**ချိတ်ဆက်မှု ပြဿနာများ:**
- ဆာဗာကို stdio transport နဲ့ မှန်မှန်သုံးထားသည်ကို စစ်ဆေးပါ
- အခြား process များကသာ လှုပ်ရှားမှု မကြောင့် မတားဆီးရေး စစ်ဆေးပါ
- Inspector command syntax ပြတ်သားစွာ ရေးထားမှု

## Project တင်ပြချက်

ပိုမိုစွမ်းဆောင်နိုင်စေရန် ဆာဗာကို တိုးချဲ့ ဆောက်လုပ်ပါ။ ဥပမာ- [ဒီစာမျက်နှာ](https://api.chucknorris.io/) ကို ရှုပါ၊ API ခေါ်မှု လုပ်နိုင်သော tools တစ်ခု ထည့်ပါ။ ဆာဗာ ဘယ်လို ဖွဲ့စည်းမလဲ သင်ပိုင်ပါတယ်။ မြောက်မြားသောပျော်ရွှင်မှု ရယူပါ :)

## ဖြေဖြတ်ချက်

[ဖြေဖြတ်ချက်](./solution/README.md)  မှာ အလုပ်လုပ်ထိုက်တဲ့ ကုဒ်နဲ့ ဖြေရှင်းနည်း ပါသည်

## အဓိက သဘောတရားများ

ဒီအခန်းထဲက အဓိကသိရှိရမယ့် အချက်တွေက-

- stdio transport ကို ဒေသခံ MCP ဆာဗာများအတွက် အကြံပြုနည်းပဲဖြစ်သည်။
- stdio transport က MCP ဆာဗာနှင့် client များကို standard input/output စီးကြောင်း ဖြင့် ပေါင်းသင်းဆက်ဆံခွင့် ပေးသည်။
- Inspector နဲ့ Visual Studio Code နှစ်ခုလုံးကို stdio ဆာဗာများကို တိုက်ရိုက်သုံးနိုင်ပြီး Debug နှင့် ပေါင်းစည်းခြင်း အလွယ်တကူ။

## အပုံစံ နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## အပိုဆောင်း အရင်းအမြစ်များ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## နောက်တစ်ခု ဘာများရှိလဲ

## နောက်တစ်ဆင့်

stdio transport ဖြင့် MCP ဆာဗာများ ဖန်တီးနည်းသင်ပြီးနောက်မှာ သင့်ကို အဆင့်မြင့်ဘာသာရပ်များကို စူးစမ်းလေ့လာနိုင်သည်-

- **နောက်တစ်ဆင့်**: [HTTP Streaming နဲ့ MCP (Streamable HTTP)](../06-http-streaming/README.md) - ဝေးလံသော ဆာဗာများအတွက် ထောက်ပံ့ထားသော သယ်ယူပို့ဆောင်မှုနည်းလမ်း
- **အဆင့်မြင့်**: [MCP လုံခြုံရေးကောင်းမွန်မှုများ](../../02-Security/README.md) - MCP ဆာဗာများတွင် လုံခြုံရေးဆောင်ရွက်ခြင်း
- **ထုတ်လုပ်ရေး**: [အသုံးပြုမှုအတွက် အကောင်အထည်ဖော်မှု မဟာမိတ်များ](../09-deployment/README.md) - ဆာဗာများထုတ်လုပ်ရေးအတွက် ပြင်ဆင်ခြင်း

## အပိုဆောင်း အရင်းအမြစ်များ

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - တရားဝင်သတ်မှတ်ချက်
- [MCP SDK စာတမ်းများ](https://github.com/modelcontextprotocol/sdk) - ဘာသာစကားတိုင်းအတွက် SDK မှတ်တမ်းများ
- [အသိုင်းအဝိုင်း ဥပမာများ](../../06-CommunityContributions/README.md) - အသိုင်းအဝိုင်းကနေ ဆာဗာ ဥပမာများ ပိုမိုတွေ့ရှိရန်

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件已使用人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力保证准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->