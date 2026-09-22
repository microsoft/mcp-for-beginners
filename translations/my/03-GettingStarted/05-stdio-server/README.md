# stdio သယ်ယူပို့ဆောင်မှုဖြင့် MCP ဆာဗာ

> **⚠️ အရေးကြီး သတင်း**: MCP သတ်မှတ်ချက် ၂၀၂၅-၀၆-၁၈ မှစ၍ standalone SSE (Server-Sent Events) သယ်ယူပို့ဆောင်မှုကို **အသုံးမပြုတော့ဘဲ** "Streamable HTTP" သယ်ယူပို့ဆောင်မှုဖြင့်အစားထိုးထားသည်။ လက်ရှိ MCP သတ်မှတ်ချက်တွင် သယ်ယူပို့ဆောင်မှုနည်းလမ်းအဓိကနှစ်ခု ပေးထားသည်-
> 1. **stdio** - ပုံမှန် input/output (သူဌေးဆာဗာများအတွက် အကြံပြု)
> 2. **Streamable HTTP** - SSE ကို အတွင်းပိုင်းအသုံးပြုနိုင်သည့် အဝေးဆာဗာများအတွက်
>
> ဒီသင်ခန်းစာမှာ **stdio သယ်ယူပို့ဆောင်မှု** ပေါ်မှာ အာရုံစူးစိုက်ထားပြီး MCP ဆာဗာများအတွက် အကြံပြုနည်းဖြစ်သည်။

stdio သယ်ယူပို့ဆောင်မှုက MCP ဆာဗာများကို client တွေနဲ့ ပုံမှန် input/output stream များဖြင့် ဆက်သွယ်ရာအတွက် အရမ်းအသုံးများပြီး လွယ်ကူတဲ့ နည်းလမ်းဖြစ်သည်။ လက်ရှိ MCP သတ်မှတ်ချက်အရ အဓိကအသုံးပြုမှုဖြစ်ပြီး စွမ်းဆောင်ရည်ကောင်းစွာ MCP ဆာဗာများကို client app မျိုးစုံနဲ့ ပေါင်းစပ်ဖန်တီးနိုင်စေသည်။

## အနှစ်ချုပ်

ဒီသင်ခန်းစာက stdio သယ်ယူပို့ဆောင်မှုဖြင့် MCP ဆာဗာတွေ ဘယ်လိုတည်ဆောက်ပြီး လက်တွဲအသုံးပြုမလဲ ဆိုတာကို ဖော်ပြပေးထားပါတယ်။

## သင်ယူရမည့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာအပြီးမှာ သင်တတ်မြောက်နိုင်မှာတွေကတော့-

- stdio သယ်ယူပို့ဆောင်မှုကို အသုံးပြု MCP ဆာဗာတည်ဆောက်ခြင်း
- Inspector ကို အသုံးပြုပြီး MCP ဆာဗာကို ချည်းပါခြင်း
- Visual Studio Code ဖြင့် MCP ဆာဗာကို အသုံးပြုခြင်း
- လက်ရှိ MCP သယ်ယူပို့ဆောင်မှု နည်းလမ်းများနှင့် stdio အကြံပြုချက်ကို နားလည်ခြင်း


## stdio သယ်ယူပို့ဆောင်မှု - အလုပ်လုပ်ပုံ

stdio သယ်ယူပို့ဆောင်မှုသည် MCP သတ်မှတ်ချက်  
`2026-07-28` တွင် ပါဝင်သော သယ်ယူပို့ဆောင်မှု နှစ်ခုထဲမှ တစ်ခုဖြစ်သည်။ အလုပ်လုပ်ပုံကတော့-

- **စနစ်တကျ ဆက်သွယ်မှု**: ဆာဗာက standard input (`stdin`) မှ JSON-RPC ဆန်းချက်များကို ဖတ်ပြီး standard output (`stdout`) သို့ အချက်ပြများ ပို့သည်။
- **လုပ်ငန်းစဉ်အခြေပြု**: Client က MCP ဆာဗာကို subprocess အဖြစ် စတင်ဖြစ်စေသည်။
- **သတင်းအချက်အလက် ပုံစံ**: Message များသည် ထိုင်းတစ်ခုချင်း JSON-RPC အမိန့်များ နှင့် တုံ့ပြန်ချက်များဖြစ်ပြီး သတ်မှတ်ထားသော newline များဖြင့် ခွဲခြားထားသည်။
- **မှတ်တမ်းတင်ခြင်း**: ဆာဗာသည် logging အတွက် standard error (`stderr`) သို့ UTF-8 စာသားများ ရေးသားနိုင်သည်။

### အဓိကလိုအပ်ချက်များ
- Message များကို newline ဖြင့် သတ်မှတ်ရမည် ဖြစ်ပြီး message တွေရဲ့ အတွင်းတွင် embedded newline မပါဝင်သင့်။
- ဆာဗာသည် `stdout` တွင် မှားယွင်းသော MCP message မရေးသင့်။
- client သည် ဆာဗာ၏ `stdin` တွင် မှားယွင်းသော MCP message မရေးသင့်။

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

အထက်ပါကုဒ်တွင်-

- MCP SDK မှ `Server` class နှင့် `StdioServerTransport` အား ယူသုံးသည်။
- အခြေခံပုံစံနှင့် စွမ်းရည်များပါသော server instance တစ်ခုဖန်တီးသည်။
- `StdioServerTransport` instance တစ်ခုဖန်တီးပြီး ဆာဗာကို stdin/stdout ပေါ်မှာ ဆက်သွယ်နိုင်စေသည်။

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ဆာဗာ အဖြစ် အသစ်ဖန်တီးပါ
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

အထက်ပါကုဒ်တွင်-

- MCP SDK ဖြင့် server instance ဖန်တီးခြင်း
- decorator များဖြင့် tools ကို သတ်မှတ်ခြင်း
- stdio_server context manager ကို သယ်ယူပို့ဆောင်မှုကို ကောင်းကောင်း ဆောင်ရွက်ရန် အသုံးပြုခြင်း

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

SSE နှင့် မတူတာ အဓိကချက်က stdio ဆာဗာတွေအနေနဲ့-

- web server သို့ HTTP endpoint မလိုအပ်ပါ
- client က subprocess အဖြစ် စတင်ဖြစ်စေသည်
- stdin/stdout streams တွင် ဆက်သွယ်မှု ရှိသည်
- ဆောင်ရွက်ရလွယ်ကူပြီး ချည်းပိတ်ရလွယ်သည်

## လေ့ကျင့်ခန်း: stdio ဆာဗာဖန်တီးခြင်း

ဆာဗာကို ဖန်တီးရာတွင် ဆောင်ရွက်ရန် အချက်နှစ်ချက်ရှိသည်-

- ဆက်သွယ်ရန်နှင့် message endpoint များ ဖော်ပြရန် web server တစ်ခုလိုအပ်သည်။
## လက်တွေ့ကျောင်း: ရိုးရှင်းသော MCP stdio ဆာဗာ ဖန်တီးခြင်း

ဒီ lab မှာ အကြံပြုထားသော stdio သယ်ယူပို့ဆောင်မှုကို အသုံးပြု၍ ရိုးရှင်း MCP ဆာဗာ တစ်ခု ဖန်တီးပါမည်။ ၎င်းဆာဗာသည် client များ Model Context Protocol ကို အသုံးပြုပြီး ခေါ်ယူနိုင်မည့် tools များ ထုတ်ဖော်ပေးပါမည်။

### လိုအပ်ချက်များ

- Python 3.8 (သို့) နောက်ပိုင်း
- MCP Python SDK: `pip install mcp`
- async programming အဓိကနားလည်မှု

MCP stdio ဆာဗာ ပထမဆုံးကို ဖန်တီးကြစို့-

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# မှတ်တမ်းစနစ်ကို ပြင်ဆင်ပါ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ဆာဗာကို ဖန်တီးပါ
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
    # stdio ပို့ဆောင်မှုကို အသုံးပြုပါ
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## SSE နည်းလမ်း ပျက်ကွက်မှုမှ ကွဲပြားချက်များ

**Stdio သယ်ယူပို့ဆောင်မှု (လက်ရှိစံချိန်):**
- ရိုးရှင်းသော subprocess မော်ဒယ် - client က ဆာဗာကို child process အဖြစ် စတင်သည်
- JSON-RPC message များအား stdin/stdout ဖြင့် ဆက်သွယ်သည်
- HTTP server တပ်ဆင်ရန် မလိုအပ်ပါ
- သာလွန်သော စွမ်းဆောင်ရည် နှင့် လုံခြုံမှု ရှိသည်
- ချည်းပိတ်ခြင်းနှင့် ဖွံ့ဖြိုးရေး လွယ်ကူသည်

**SSE သယ်ယူပို့ဆောင်မှု (MCP ၂၀၂၅-၀၆-၁၈မှ စ၍ ပျက်ကွက်):**
- SSE endpoint မပါသော HTTP server လိုအပ်သည်
- web server အခြေခံခြင်းမှာ ပိုရှုပ်ထွေးသည်
- HTTP endpoint များအတွက် လုံခြုံရေးလိုအပ်ချက်များ ပိုများသည်
- Streamable HTTP ကို အသုံးပြုရန် အစားထိုးထားသည်

### stdio သယ်ယူပို့ဆောင်မှုဖြင့် ဆာဗာ တည်ဆောက်ခြင်း

stdio ဆာဗာ ဖန်တီးရန် ကျွန်တော်တို့ လုပ်ရမည့်အချက်များ-

1. **လိုအပ်သော library များကို import ပြုလုပ်ခြင်း** - MCP ဆာဗာအစိတ်အပိုင်းနှင့် stdio transport များ
2. **ဆာဗာ instance တည်ဆောက်ခြင်း** - အင်အားများနှင့် server ကို သတ်မှတ်ခြင်း
3. **tools သတ်မှတ်ခြင်း** - ဖော်ပြလိုသည့် လုပ်ဆောင်ချက်များ ရေးဆွဲခြင်း
4. **သယ်ယူပို့ဆောင်မှု ကို စီမံခြင်း** - stdio communication ကိစ္စများ သတ်မှတ်ခြင်း
5. **ဆာဗာကို အားပေးမောင်းနှင်ခြင်း** - ဆာဗာစတင်ပြီး message များ ကိုင်တွယ်မှု

အဆင့်ဆင့်နဲ့ တည်ဆောက်ကြစို့-

### အဆင့် ၁: အခြေခံ stdio ဆာဗာ ဖန်တီးခြင်း

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# မှတ်တမ်းတင်ခြင်းကို စီမံရမည်
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ဆာဗာကို ဖန်တီးရမည်
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

### အဆင့် ၂: tools ပိုများ ပြုလုပ်ခြင်း

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

### အဆင့် ၃: ဆာဗာကို လည်ပတ်ခြင်း

ကုဒ်ကို `server.py` ဟုသိမ်းပြီး command line ကနေ ပြေးပါ-

```bash
python server.py
```

ဆာဗာသည် stdin မှ input များ ကို စောင့်ဆိုင်းဖြစ်ပြီး stdio သယ်ယူပို့ဆောင်မှုမှတဆင့် JSON-RPC message များကို ဆက်သွယ်ပါသည်။

### အဆင့် ၄: Inspector ဖြင့် စမ်းသပ်ခြင်း

MCP Inspector ကို အသုံးပြုပြီး သင့်ဆာဗာကို စမ်းသပ်နိုင်သည်-

1. Inspector ကို ထည့်သွင်းပါ: `npx @modelcontextprotocol/inspector`
2. Inspector ကို အလုပ်သွားစေပြီး သင့်ဆာဗာကို ဖော်ညွှန်းပါ
3. ဖန်တီးထားသော tool များကို စမ်းသပ်ပါ

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## သင့် stdio ဆာဗာကို ချည်းပါခြင်း

### MCP Inspector အသုံးပြုခြင်း

MCP Inspector သည် MCP ဆာဗာများ လုပ်ဆောင်မှု များကို ချည်းညပ်စောင့်စစ်ရန် အသုံးဝင်သည်။ သင့် stdio ဆာဗာနှင့် အသုံးပြုရန် အဆင့်ဆင့်-

1. **Inspector ကို ထည့်သွင်းမည်**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ကို စတင်မည်**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **သင့်ဆာဗာကို စမ်းသပ်မည်**: Inspector တွင် ဝက်ဘ်အင်တာဖေ့စ်ဖြင့်-
   - ဆာဗာစွမ်းရည်များ ကြည့်ရှုနိုင်သည်
   - ကွဲပြားသော parameter များဖြင့် tools များ စမ်းသပ်နိုင်သည်
   - JSON-RPC message များ ကြည့်ရှုနိုင်သည်
   - ဆက်သွယ်မှု ပြဿနာများကို ချည်းပိတ်နိုင်သည်

### VS Code အသုံးပြုခြင်း

VS Code တွင်လည်း သင့် MCP ဆာဗာကို တိုက်ရိုက် ချည်းပါနိုင်သည်-

1. `.vscode/launch.json` တွင် launch configuration ဖန်တီးပါ-
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

2. ဆာဗာကုဒ်တွင် breakpoint များထည့်ပါ
3. Debugger ကို စတင်ပြီး Inspector နှင့် စမ်းသပ်ပါ

### ချည်းပိတ်ရာတွင် အထွေထွေ အကြံဉာဏ်များ

- logging အတွက် `stderr` ကိုသာ အသုံးပြုပါ - `stdout` သည် MCP message များအတွက် သီးသန့်ထားသည်။
- JSON-RPC message များအားလုံးကို newline ဖြင့် ခွဲခြားပါ။
- ရိုးရှင်းသော tool များဖြင့် စတင်စမ်းသပ်ပြီး နောက်ပိုင်းတွင် ရှုပ်ထွေးသော လုပ်ဆောင်ချက်များ ထည့်သွင်းပါ။
- Message ပုံစံတိကျမှန်ကန်ကြောင်း Inspector ဖြင့် အတည်ပြုပါ။

## VS Code တွင် သင်၏ stdio ဆာဗာကို အသုံးပြုခြင်း


သင့် MCP stdio ဆားဗာကို တည်ဆောက်ပြီးနောက်၊ ကျွန်တော်တို့ VS Code နှင့် ပေါင်းစပ်ပြီး Claude သို့မဟုတ် MCP ကိုက်ညီသော client များနှင့် အသုံးပြုနိုင်သည်။

### ပုံမှန်ချိန်ညှိမှု

1. **MCP ပုံမှန်ချိန်ညှိမှုဖိုင်တစ်ခု ဖန်တီးပါ** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) သို့မဟုတ် `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) တွင်:

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

2. **Claude ကို ပြန်စတင်ပါ**: Claude ကို ပိတ်ပြီး ထပ်ဖြင့်ဖွင့်ကာ ဆားဗာ ပုံမှန်ချိန်ညှိမှုအသစ်ကို သိမ်းဆည်းပါ။

3. **ဆက်သွယ်မှုကို စမ်းသပ်ပါ**: Claude နှင့် စကားပြောခြင်း စတင်ပြီး သင့်ဆားဗာရဲ့ ကိရိယာများကို ကြိုးစားသုံးစွဲကြည့်ပါ။
   - "ကြိုဆိုသည့် ကိရိယာကို အသုံးပြုပြီး ကျေးဇူးပြု၍ ကြိုဆိုပေးပါနော်။"
   - "15 နဲ့ 27 ရဲ့ စုပေါင်းကိုတွက်ရန်"
   - "ဆားဗာအချက်အလက်များဘာဖြစ်နေလဲ?"

### TypeScript stdio ဆားဗာ ဥပမာ

ဤသင့်အတွက် ပြည့်စုံသော TypeScript ဥပမာ ဖြစ်ပါသည်။

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

// ကိရိယာများ ထည့်ရန်
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

### .NET stdio ဆားဗာ ဥပမာ

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

## အကျဉ်းချုပ်

ဒီ အသစ်ပြင်ဆင်ထားသော သင်ခန်းစာတွင် သင်တတ်မြောက်ပြီးပါပြီ။

- လက်ရှိ **stdio သယ်ယူပို့ဆောင်မှု** အသုံးပြု၍ MCP ဆားဗာများကို တည်ဆောက်ခြင်း (အကြံပြုသည့် နည်းလမ်း)
- SSE သယ်ယူပို့ဆောင်မှုကို မည်သူ က stdio နှင့် Streamable HTTP ကို ၎င်းတိုင်ပတ်ပဲဖြင့် ရပ်ဆိုင်းခဲ့ရသည်ကို နားလည်ခြင်း
- MCP client များမှ ခေါ်ယူနိုင်သော ကိရိယာများ ဖန်တီးခြင်း
- MCP Inspector ကို အသုံးပြု၍ သင့်ဆားဗာကို ရှာဖွေပြင်ဆင်ခြင်း
- သင့် stdio ဆားဗာကို VS Code နှင့် Claude နှင့် ပေါင်းစပ်ခြင်း

stdio သယ်ယူပို့ဆောင်မှုသည် စိတ်ရှည်ငြိမ်ပြီး လုံခြုံမှုမြင့်၊ နှင့် ပိုမိုမြန်ဆန်သော MCP ဆားဗာ တည်ဆောက်ခြင်းနည်းလမ်းဖြစ်ပြီး SSE နည်းလမ်း ရပ်ဆိုင်းခြင်းထက် ကောင်းမွန်သည်။ 2025-06-18 စံချိန်အတိုင်း MCP ဆားဗာများအတွက် အကြံပြုသည့် သယ်ယူပို့ဆောင်မှု ဖြစ်သည်။


### .NET

1. ပထမဦးဆုံး ကိရိယာများတည်ဆောက်ပါ၊ ဒီအတွက် *Tools.cs* ဆိုတဲ့ ဖိုင် တစ်ခု ဖန်တီးပြီး အောက်ပါ အကြောင်းအရာ ထည့်သွင်းပါ။

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## လေ့ကျင့်ခန်း: သင့် stdio ဆားဗာကို စမ်းသပ်ခြင်း

သင့် stdio ဆားဗာကို တည်ဆောက်ပြီးသွားပြီဆို အလုပ် လုပ်မည်ဟု သေချာစေရန် စမ်းသပ်ကြည့်မယ်။

### အခြေခံလိုအပ်ချက်များ

1. MCP Inspector ကို တပ်ဆင်ထားပါကြောင်း သေချာစေရန်။
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. သင့် ဆားဗာ ကုဒ်ကို သိမ်းဆည်းထား (ဥပမာ `server.py`)

### Inspector ဖြင့် စမ်းသပ်ခြင်း

1. **ဆားဗာနှင့် Inspector ကို စတင်ပါ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ဝက်ဘ်အင်တာဖေ့စ်ဖွင့်ပါ**: Inspector သည် သင့် ဆားဗာ၏ လုပ်ဆောင်ချက်များကို ပြသသော ဘရောက်ဇာပြတင်းပေါ်ကို ဖွင့်ပြသမည်။

3. **ကိရိယာများကို စမ်းသပ်ပါ**:
   - `get_greeting` ကိရိယာကို အမည်အမျိုးမျိုးဖြင့်စမ်းသပ်ရန်
   - `calculate_sum` ကိရိယာကို အစုံအလင် နံပါတ်များဖြင့် စမ်းသပ်ရန်
   - `get_server_info` ကိရိယာကို ခေါ်ပြီး ဆားဗာ၏ မိတ္တူ အချက်အလက်များကြည့်ရန်

4. **ဆက်သွယ်မှုကို ကြည့်ရှုစောင့်ကြည့်ပါ**: Inspector သည် client နှင့် ဆားဗာအကြား လဲလှယ်နေသော JSON-RPC ဆုတောင်းစာေတပ်များကို ပြသည်။

### သင့်မြင်ရမည့်အချက်များ

ဆားဗာမှန်ကန်စွာ စတင်လျှင် သင့်မြင်ရမည့် အချက်များမှာ
- Inspector တွင် ဆားဗာ၏ လုပ်ဆောင်ချက်များကို စာရင်းပြုလုပ်တင်ပြခြင်း
- စမ်းသပ်ရန် ရရှိနိုင်သော ကိရိယာများ
- JSON-RPC စာရင်းများ အောင်မြင်စွာ လဲလှယ်မှုများ
- ကိရိယာတုံ့ပြန်ချက်များကို အင်တာဖေ့စ်တွင် ပြသခြင်း

### ပုံမှန်ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

**ဆားဗာ မစတင်နိုင်ခြင်း:**
- လိုအပ်သော နေရာတတ်မှုများ `pip install mcp` ဖြင့် တပ်ဆင်ခြင်းကို စစ်ဆေးပါ။
- Python စာတမ်းအချက်အလက်နှင့် မျက်နှာဖုံး ကောင်းမွန်မှု စစ်ဆေးပါ
- ကွန်ဆိုင်းတွင် မှားယွင်းချက်စာမက်များ ရှာဖွေပါ

**ကိရိယာများ မမြင်ရခြင်း:**
- `@server.tool()` decorator များ ပါရှိကြောင်း သေချာစေပါ
- ကိရိယာ function များသည် `main()` မတိုင်မီ အမှန်တကယ် သတ်မှတ်ထားကြောင်း စစ်ဆေးပါ
- ဆားဗာကို မှန်ကန်စွာ ပုံမှန်ချိန်ညှိထားကြောင်း စစ်ဆေးပါ

**ဆက်သွယ်မှု ပြဿနာများ:**
- ဆားဗာသည် stdio သယ်ယူပို့ဆောင်မှု အတိုင်းမှန်ကန်စွာ အသုံးပြုနေကြောင်း သေချာပါစေ
- မည်သည့် အခြားလုပ်ငန်းစဉ်များက ထိခိုက်မပြုလုပ်နေတာကို စစ်ဆေးပါ
- Inspector အမိန့်ကောက်နည်း စာသားမှန်ကန်မှုကို စစ်ဆေးပါ

## တာဝန်

သင့် ဆားဗာကို ပိုမိုပြီး စွမ်းဆောင်ရည်များ ဖန်တီးရန် ကြိုးစားပါ။ ဥပမာအနေနဲ့ [ဤစာမျက်နှာ](https://api.chucknorris.io/) တွင် ရှိသည့် API ကို ခေါ်သည့် ကိရိယာတစ်ခု ထည့်နိုင်ပါတယ်။ ဆားဗာသည် မည်သို့ဖန်တီးမည်ဆိုတာကို သင်ကိုယ်တိုင်ဆုံးဖြတ်နိုင်သည်။ ပျော်ရွှင်ပါစေ :)
## ဖြေရှင်းချက်

[ဖြေရှင်းချက်](./solution/README.md) လုပ်ဆောင်နိုင်သော ကုဒ်ပါရှိသည့် နည်းလမ်းတစ်ခု။

## အဓိကသင်ခန်းစာများ

ဤအခန်းမှ အဓိက သင်ခန်းစာများမှာ အောက်ပါအတိုင်းဖြစ်သည်။

- stdio သယ်ယူပို့ဆောင်မှုမှာ ဒေသခံ MCP ဆားဗာများအတွက် အကြံပြုသည့် မက်ခရောနစ်ဖြစ်သည်။
- Stdio သယ်ယူပို့ဆောင်မှုသည် MCP ဆားဗာနှင့် client များအကြား စံထိပ် ရိုက်နှိပ်ပေးမှုနှင့် ထွက်သွားမှု streams တို့ဖြင့် ချိတ်ဆက်ရာမှာ လွယ်ကူစေသည်။
- Inspector နှင့် Visual Studio Code ကို အသုံးပြု၍ stdio ဆားဗာများကို တိုက်ရိုက် စီမံနိုင်ရာ Debugging နှင့် ပေါင်းစပ်ခြင်း ပိုမိုလွယ်ကူစေသည်။

## ဥပမာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## နောက်ထပ်အရင်းအမြစ်များ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## နောက်ထပ်ဘာတွေလုပ်မလဲ

## နောက်တစ်ဆင့်များ

stdio သယ်ယူပို့ဆောင်မှုဖြင့် MCP ဆားဗာ တည်ဆောက်နည်း သင်တတ်ပြီ ဖြစ်သောကြောင့် ထပ်မံပြီး ဆက်လက်လေ့လာနိုင်သော ခေါင်းစဉ်များကို ကြည့်ရှုလိုက်ပါ။

- **နောက်တော်တော်**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - ဝေးလံ ဆားဗာများအတွက် ဘယ်လို သယ်ယူပို့ဆောင်မှုနည်းလမ်း အသုံးပြုကြောင်း လေ့လာရန်
- **အဆင့်မြင့်**: [MCP Security Best Practices](../../02-Security/README.md) - သင့် MCP ဆားဗာများတွင် လုံခြုံရေးကာကွယ်မှုများ ဆောင်ရွက်ခြင်း
- **ထုတ်လုပ်မှု**: [Deployment Strategies](../09-deployment/README.md) - ဆားဗာများကို ထုတ်လုပ်ရေးအတွက် တပ်ဆင်ခြင်းနည်းလမ်းများ

## နောက်ထပ်အရင်းအမြစ်များ

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - လက်ရှိ သတ်မှတ်ချက်
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - ဘာသာစကားအားလုံးအတွက် SDK ကိုးကားချက်များ
- [အသိုင်းအဝိုင်း ဥပမာများ](../../06-CommunityContributions/README.md) - အသိုင်းအဝိုင်းမှ ဆားဗာ ဥပမာများ ပိုမိုလေ့လာရန်

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->