# stdio သယ်ယူပို့ဆောင်မှုနှင့် MCP Server

> **⚠️ အရေးကြီးသော အပ်ဒိတ်** - MCP Specification 2025-06-18 အရ ၊ standalone SSE (Server-Sent Events) သယ်ယူပို့ဆောင်မှုကို **အသုံးမပြုတော့ပါ** ။ "Streamable HTTP" သယ်ယူပို့ဆောင်မှုဖြင့်အစားထိုးထားသည်။ လက်ရှိ MCP specification တွင် သယ်ယူပို့ဆောင်မှု မော်ဒယ်နှစ်မျိုးအောက်ပါအတိုင်း သတ်မှတ်ထားသည့်အတွက်ဖြစ်သည် -  
> 1. **stdio** - စံတော်ချိန် input/output (ဒေသীয় server များအတွက် အကြံပြု)  
> 2. **Streamable HTTP** - SSE ကိုအတွင်းပိုင်းအသုံးပြုနိုင်သော အကွာအဝေး server များအတွက်  
>
> ယခုသင်ခန်းစာသည် **stdio transport** ကို အခြေခံ၍ အားကောင်းအပ်ခဲ့ပြီး MCP server များအတွက် အကြံပြုထားသောနည်းလမ်းဖြစ်သည်ကို အထူးသတိပေးသည်။

stdio transport သည် MCP server များကို standard input နှင့် output stream များမှတဆင့် clients နှင့်ဆက်သွယ်နိုင်စေရန်ခွင့်ပြုသည်။ လက်ရှိ MCP specification တွင် အများဆုံးအသုံးပြု၍ အကြံပြုသည့် သယ်ယူပို့ဆောင်မှုနည်းလမ်းဖြစ်ပြီး စနစ်တကျ ရိုးရှင်းစွာ MCP server များ တည်ဆောက်ရန်နှင့် မတူညီသော client application များနှင့်လွယ်ကူစွာ ပေါင်းစည်းအသုံးပြုနိုင်သည်။

## အနှစ်ချုပ်

ဤသင်ခန်းစာသည် stdio transport အသုံးပြု၍ MCP Server များကို မည်သို့ တည်ဆောက်အသုံးပြုရမည်ကို ဖော်ပြပေးသည်။

## သင်ယူရမည့် ရည်ရွယ်ချက်များ

ဤသင်ခန်းစာ ဖတ်ပြီးဆုံးသည်နှင့် တွင် -

- stdio transport ဖြင့် MCP Server တစ်ခု တည်ဆောက်နိုင်သည်။
- Inspector ကို အသုံးပြု၍ MCP Server တစ်ခုကို Debug လုပ်နိုင်သည်။
- Visual Studio Code ဖြင့် MCP Server ကိုအသုံးပြုနိုင်သည်။
- လက်ရှိ MCP သယ်ယူပို့ဆောင်မှု မော်ဒယ်များကို နားလည်ပြီး stdio သယ်ယူပို့မှုကို ဘာကြောင့် အကြံပြုသည်ကို သိရှိနိုင်သည်။

## stdio Transport - မည်သို့ လုပ်ဆောင်သည်

stdio transport သည် လက်ရှိ MCP specification (2025-06-18) တွင် ထောက်ခံထားသော သယ်ယူပို့ဆောင်မှု များမှ တစ်ခုဖြစ်သည်။ အောက်ပါအတိုင်း လုပ်ဆောင်ပုံ ဖြစ်သည် -

- **ရိုးရှင်းသော ဆက်သွယ်မှု** - server သည် standard input (`stdin`) မှ JSON-RPC message များ ဖတ်ပြီး standard output (`stdout`) သို့ message များ ပို့ပေးသည်။
- **Process-based** - client က MCP server ကို subprocess အဖြစ် စတင်ခေါ်ယူသည်။
- **Message ဖော်မတ်** - message များမှာ JSON-RPC requests, notifications, responses တစ်ခုချင်း လိုင်းအသစ်ခွဲပြထားသည်။
- **Logging** - server သည် log ရေးရန် ရည်ရွယ်၍ UTF-8 စာသားများကို standard error (`stderr`) မှာရေးနိုင်သည်။

### သတ်မှတ်ချက်အဓိကများ
- message များကို လိုင်းအသစ် (newline) ဖြင့် ခွဲစိတ်ရမည်၊ message ထဲတွင် embedded newlines မပါသင့်ပါ။
- server သည် `stdout` ထဲတွင် မှန်ကန်သော MCP message မဟုတ်သည့် အရာ မရေးသင့်ပါ။
- client သည် server ၏ `stdin` တွင် မှန်ကန်သော MCP message မဟုတ်သည့် အရာ မရေးသင့်ပါ။

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
  
အထက်ပါ code တွင် -

- MCP SDK မှ 'Server' class နှင့် 'StdioServerTransport' ကို import လုပ်သည်။
- ရိုးရှင်းသော configuration နှင့် capabilities ပါသော server instance တည်ဆောက်သည်။
- 'StdioServerTransport' instance တစ်ခု ဖန်တီး၍ server ကို stdin/stdout နဲ့ ဆက်ထားသည်။

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ဆာဗာ အင်စတန့် စတင် ဖန်တီးပါ
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
  
အထက်ပါ code တွင် -

- MCP SDK ဖြင့် server instance တစ်ခု ဖန်တီးသည်
- decorators ကို အသုံးပြုပြီး tools များ သတ်မှတ်သည်
- transport ကို ကိုင်တွယ်ရန် stdio_server context manager ကို အသုံးပြုသည်

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
  
SSE နှင့် ကွာခြားချက် အဓိကမှာ stdio servers တွင် -

- Web server setup သို့မဟုတ် HTTP endpoints မလိုအပ်ပါ
- client မှ subprocess အဖြစ် server ကို စတင်ခေါ်ယူသည်
- stdin/stdout stream မှတဆင့် ဆက်သွယ်မှု ဖြစ်သည်
- တည်ဆောက်ရလွယ်ကူပြီး debug လုပ်ရာ အဆင်ပြေသည်

## လေ့ကျင့်ခန်း - stdio Server တည်ဆောက်ခြင်း

server တည်ဆောက်​ရာတွင် တွေးစဉ်ရန် -

- ဆက်သွယ်ရေး နှင့် message များအတွက် endpoint များ ဖော်ပြရန် web server လိုအပ်သည်။

## လေ့လာရေးအတန်း - ရိုးရှင်းသော MCP stdio server တည်ဆောက်ခြင်း

ဤလေ့လာရေးအတန်းတွင် MCP server ရိုးရှင်းတစ်ခု stdio transport အသုံးပြုပြီး တည်ဆောက်မည်ဖြစ်သည်။ client များက Model Context Protocol အတိုင်း ခေါ်ယူနိုင်သော tools များ ထုတ်ပေးပါမည်။

### လိုအပ်သော စက်ပစ္စည်းများ

- Python 3.8+
- MCP Python SDK: `pip install mcp`
- async programming အကြောင်းဖြစ်စေ နားလည်မှုပုံစံ

ပထမ MCP stdio server ကို ဖန်တီးခြင်းကိုစလိုက်ပါ -

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# မှတ်တမ်းရေးစနစ်ကိုဆက်တင်ရန်
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ဆာဗာကိုဖန်တီးရန်
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
    # stdio သယ်ယူပို့ဆောင်မှုကိုအသုံးပြုရန်
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


## deprecated ဖြစ်သွားသော SSE နည်းလမ်းနှင့် ကွာခြားချက်များ

**Stdio Transport (လက်ရှိ မူဝါဒ):**
- ရိုးရှင်းသော subprocess model - client က server ကို child process အဖြစ် စတင်ခေါ်ယူသည်
- stdin/stdout ကနေ JSON-RPC message များ ဖြင့် ဆက်သွယ်မှု
- HTTP server setup လိုအပ်ချက် မရှိ
- ပိုမိုမြန်ဆန်ပြီး လုံခြုံမှု ကောင်းမွန်သည်
- Debug နဲ့ တိုးတက်မှု လွယ်ကူသည်

**SSE Transport (MCP 2025-06-18 မှအပြီး deprecated):**
- SSE endpoints ပါသော HTTP server လိုအပ်ခဲ့
- Web server infrastructure ကြောင့် ခက်ခဲမှုများရှိခဲ့
- HTTP endpoints အတွက် လုံခြုံမှု အပြင်အဆင်များ ရှိခဲ့
- ယခုတွင် Streamable HTTP ဖြင့် အစားထိုး

### stdio transport နှင့် server တည်ဆောက်ခြင်း

server တည်ဆောက်ရန် -

1. စာကြောင်းလိုအပ်သည့် libraries များ import လုပ်ရန် (MCP server component များနှင့် stdio transport)
2. server instance တစ်ခု ဖန်တီးရန်။ capabilities နှင့်အတူ ပြန်အပ်
3. tools များ သတ်မှတ်ရန်
4. stdio communication ကို ချိတ်ဆက်ရန်
5. server ကို စတင် Run လုပ်၍ message များကို ကိုင်တွယ်ရန်

အဆင့်ဆင့် တည်ဆောက်ကြမယ် -

### အဆင့် ၁ - ရိုးရှင်းသော stdio server တည်ဆောက်ခြင်း

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# မှတ်တမ်းရေးရာစနစ်ကို ပြင်ဆင်ပါ
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


### အဆင့် ၂ - tools များ ထပ်တွဲခြင်း

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


### အဆင့် ၃ - server ကို ပြေးဆွဲခြင်း

code ကို `server.py` အဖြစ် သိမ်းပြီး command line မှ run ပါ။

```bash
python server.py
```
  
server သည် stdin မှ input တောင်းဆိုကာ JSON-RPC message များဖြင့် stdio transport အား အသုံးပြု ဆက်သွယ်မည်။

### အဆင့် ၄ - Inspector ဖြင့် စမ်းသပ်ခြင်း

MCP Inspector သုံး၍ သင်၏ server ကို စမ်းသပ်နိုင်သည် -

1. Inspector 설치 : `npx @modelcontextprotocol/inspector`
2. Inspector တွင် သင့် server ကို ချိတ်ဆက်ပါ
3. ဖန်တီးထားသော tools များကို စမ်းသပ်ကြည့်ပါ

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## stdio server ကို debug လုပ်ခြင်း

### MCP Inspector အသုံးပြုပြီး

MCP Inspector သည် MCP server များ debug လုပ်ရန်အတွက်အသုံးဝင်သောကိရိယာဖြစ်သည်။ stdio server နှင့် အသုံးပြုပုံက -

1. Inspector ကို 설치
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. Inspector run ပြုလုပ်ရန်
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. Inspector မှာ -
   - Server capabilities ကြည့်ရှူနိုင်သည်
   - parameter များဖြင့် tools စမ်းသပ်နိုင်သည်
   - JSON-RPC message များကို မျက်မှောက်ထိန်းချုပ်နိုင်သည်
   - ဆက်သွယ်မှု ပြဿနာများ debug လုပ်နိုင်သည်

### VS Code အသုံးပြုပြီး

VS Code မှတစ်ဆင့် တိုက်ရိုက် MCP server debug လုပ်နိုင်သည် -

1. `.vscode/launch.json` မှာ launch ကွန်‌ဖစ်ပြုလုပ်ပါ
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

2. Server code တွင် breakpoints များ ထားပါ
3. Debugger run နှင့် Inspector နဲ့ စမ်းသပ်ပါ

### များစွာ ကြုံတွေ့သော debugging အကြံပြုချက်များ

- Logging အတွက် `stderr` ကို အသုံးပြုပါ။ MCP message များအတွက် `stdout` ကို တစ်ခါမှ မရေးရ။
- JSON-RPC message များကို လိုင်းအသစ်ဖြင့် ခွဲစိတ်ထားကြောင်း သေချာစေပါ။
- ရိုးရှင်းသော tools များဖြင့် စမ်းသပ်ပြီး နောက်ပိုင်း ဆက်လုပ်ပါ။
- Inspector ဖြင့် message format များကို စစ်ဆေးပါ။

## VS Code မှ stdio server ကို အသုံးပြုခြင်း

stdio server တည်ဆောက်ပြီးနောက် VS Code နှင့် ပေါင်းစည်းပြီး Claude သို့မဟုတ် MCP client များနှင့် အသုံးပြုနိုင်သည်။

### သတ်မှတ်ချက်

1. MCP configuration ဖိုင် `%APPDATA%\Claude\claude_desktop_config.json` (Windows) သို့မဟုတ် `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) တွင် ဖန်တီးပါ -

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

2. Claude ကို ပြန်ဖွင့်ကာ server configuration ကို load ပြန်ပါ။
3. Claude နှင့် စတင်စကားပြောပြီး server tools များကို စမ်းသပ်ပါ -
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio server ဥပမာ

အောက်ပါ TypeScript ကုဒ် ကို ကိုးကားပါ -

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

// ကိရိယာများထည့်ပါ
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

ဤသင်ခန်းစာအဆင့်မြှင့် အပိုင်းတွင် -

- **stdio transport** အသုံးပြုပြီး MCP server များ တည်ဆောက်ခြင်း သင်ရရှိခဲ့သည် (အကြံပြုနည်း)
- SSE သည် stdio နှင့် Streamable HTTP သို့ ဘာကြောင့် အသုံးမပြုတော့တာကို နားလည်ခဲ့သည်
- MCP client များ မှာ ခေါ်ယူနိုင်သော tools များ ဖန်တီးမှု
- MCP Inspector ဖြင့် server ကို debug လုပ်နည်း
- VS Code နှင့် Claude အတွက် stdio server ပေါင်းစည်းခြင်း

stdio transport သည် deprecated SSE နည်းလမ်းနှင့် ယှဉ်၍ လွယ်ကူ၊ ပိုမိုလုံခြုံပြီး မြန်ဆန်မှုကောင်းမွန်သော သယ်ယူပို့ဆောင်မှုဖြစ်သည်။ MCP server အများစုအတွက် 2025-06-18 specs အရ အကြံပြုနည်းလမ်း ဖြစ်လာသည်။

### .NET

1. အရင်ဆုံး tools များကို တီထွင်ကြမယ်။ ဒါအတွက် *Tools.cs* ဖိုင်ကို အောက်ပါအတိုင်း ပြုလုပ်ပါ -

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## လေ့ကျင့်ခန်း - stdio server စမ်းသပ်ခြင်း

stdio server တည်ဆောက်ပြီးနောက် စမ်းသပ်ပါ။

### လိုအပ်ချက်များ

1. MCP Inspector တပ်ဆင်ထား မဖြစ်မနေလိုသည်။
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Server code ကို သိမ်းဆည်းထားပါ (ဥပမာ - `server.py`)

### Inspector ဖြင့် စမ်းသပ်ခြင်း

1. Inspector ကို server ဖြင့် ပြေးပါ -
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. Browser မှာ web interface ဖွင့်ပြီး server capabilities များ ကြည့်ရှူနိုင်သည်။
3. tools များ စမ်းသပ်ပါ -
   - `get_greeting` tool ကို နာမည်ပေါင်း မတူညီချက်များဖြင့် စမ်းသပ်ပါ
   - `calculate_sum` tool ကို အရေအတွက်များ ဖြင့် စမ်းသပ်ပါ
   - `get_server_info` tool ကိုခေါ်ယူကြည့်ပါ
4. ဆက်သွယ်မှု monitor လုပ်ပါ - Inspector မှ client နှင့် server အကြား JSON-RPC message များ ပြသပေးသည်။

### တွေ့ရဖွယ် အချက်များ

server သင့်တော်စွာ စတင်နေရင် -

- Inspector တွင် server capabilities မြင်ရမည်
- စမ်းသပ်ရန် tools များ ရှိနေရမည်
- JSON-RPC message လွတ်လပ်စွာလည်ပတ်နိုင်သည်
- tool များ၏ တုံ့ပြန်ချက်များ မြင်ရမည်

### ရောဂါများနှင့် ဖြေရှင်းနည်းများ

**Server မစတင်ပါဘူး**  
- `pip install mcp` ဖြင့် dependencies ပြည့်စုံကြောင်း စစ်ဆေးပါ  
- Python syntax နှင့် indentation ကိုစစ်ဆေးပါ  
- console ထဲ error message များအတွက်စစ်ဆေးပါ

**Tools မမြင်ရ**  
- `@server.tool()` decorator များ သပ်ရပ်မှုရှိပါသလား စစ်ဆေးပါ  
- tool function များကို `main()` မခေါ်မီ သတ်မှတ်ထားပါသလား စစ်ဆေးပါ  
- server configuration မှန်ကန်မှုရှိပါသလား စစ်ဆေးပါ

**ဆက်သွယ်မှု ပြဿနာ**  
- stdio transport မှန်ကန်စွာ အသုံးပြုထားခြင်း စစ်ဆေးပါ  
- အခြား process များက တိုက်ခိုက်ခြင်း မရှိကြောင်း စစ်ဆေးပါ  
- Inspector command syntax မှန်ကန်ကြောင်း စစ်ဆေးပါ

## လုပ်ငန်းမှာ

server ကို အပို capabilities နှင့် တိုးချဲ့ ဖန်တီးကြည့်ပါ။ ဥပမာအဖြစ် [ဒီစာမျက်နှာ](https://api.chucknorris.io/) တွင် API ခေါ်ယူနိုင်သော tool တည်ဆောက်ပါ။ server ကို မည်သို့ ဖော်ပြမည်ကို သင်ပိုင်နိုင်သည်။ ပျော်ရွှင်စွာ လုပ်ဆောင်ပါ :)

## ဖြေရှင်းချက်

[ဖြေရှင်းချက်](./solution/README.md) - လက်တွေ့ ကုဒ်ပါသော ဖြေရှင်းချက်ဖြစ်သည်။

## အဓိက သင်ယူချက်များ

ဤအခန်းမှ သင်ယူရမည့် သတ်မှတ်ချက်များ -

- stdio transport ကို ဒေသတွင်း MCP server များအတွက် အကြံပြုထားသည်။
- stdio transport သည် MCP server နှင့် client များကို standard input/output stream ဖြင့်ချိတ်ဆက်ရန် ကောင်းမွန်စွာ အဆင်ပြေစေသည်။
- Inspector နှင့် Visual Studio Code နှစ်မျိုးစလုံးကို stdio server များ သုံးရန် အသုံးပြုနိုင်ပြီး debugging နှင့် integration လုပ်ကောင်းစေသည်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## အပိုဆောင်း အရင်းအမြစ်များ

- [Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## နောက်တစ်ဆင့်

## နောက်တစ်ဆင့်များ

stdio transport သုံး၍ MCP server များ တည်ဆောက်နည်း သင်ယူပြီးနောက် အဆင့်မြှင့်အကြောင်းအရာများကို စူးစမ်းလိုက်ပါ -

- **နောက်တစ်ဆင့်**: [MCP တွင် HTTP Streaming (Streamable HTTP)](../06-http-streaming/README.md) - အကွာအဝေး сервер များအတွက် နောက်ထပ်ထောက်ခံသယ်ယူပို့မှု မော်ဒယ်
- **အဆင့်မြှင့်**: [MCP လုံခြုံရေး အကောင်းဆုံးလေ့လာမှုများ](../../02-Security/README.md) - MCP server များတွင် လုံခြုံရေး ထည့်သွင်းရန်
- **ထုတ်လုပ်မှု**: [Deployment များ](../09-deployment/README.md) - server များကို ထုတ်လုပ်မှုတွင် အသုံးချရန်

## အပိုဆောင်း အရင်းအမြစ်များ

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - တရားဝင် သတ်မှတ်ချက်များ
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - ဘာသာစကားအားလုံးအတွက် SDK ရင်းမြစ်များ
- [Community Examples](../../06-CommunityContributions/README.md) - အသိုင်းအဝိုင်းမှ server ဥပမာများ ပိုမိုများပြားခြင်း

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**မှတ်ချက်**:  
ဤစာတမ်းကို AI ဘာသာပြန်မှုဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည်တိကျမှန်ကန်မှုအတွက်ကြိုးပမ်းထားသော်လည်း အလိုအလျောက်ဘာသာပြန်မှုတွင်အမှား သို့မဟုတ် မှားယွင်းချက်များ ပါရှိနိုင်ကြောင်း သတိပြုပါ။ မူရင်းစာတမ်းကို မိခင်ဘာသာဖြင့်သာ အတိအကျနှင့် စံနှုန်းအရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသောသတင်းအချက်အလက်များအတွက် လူမှုကြီးကြပ်ကောင်းမွန်သော ဘာသာပြန်တစ်ဦး၏ ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားအယူအဆများအတွက် ကျွန်ုပ်တို့ အများပြည်သူ တာဝန်မရှိပါကြောင်း သတိပေးအပ်ပါသည်။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->