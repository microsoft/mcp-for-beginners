# MCP সার্ভার stdio ট্রান্সপোর্ট সহ

> **⚠️ গুরুত্বপূর্ণ আপডেট**: MCP স্পেসিফিকেশন 2025-06-18 অনুসারে, স্ট্যান্ডঅ্যালোন SSE (সার্ভার-সেন্ট ইভেন্টস) ট্রান্সপোর্ট **ডিপ্রিকেটেড** হয়েছে এবং তার পরিবর্তে "Streamable HTTP" ট্রান্সপোর্ট ব্যবহার করা হচ্ছে। বর্তমান MCP স্পেসিফিকেশন দুটি প্রধান ট্রান্সপোর্ট পদ্ধতি সংজ্ঞায়িত করে:
> ১. **stdio** - স্ট্যান্ডার্ড ইনপুট/আউটপুট (স্থানীয় সার্ভারগুলোর জন্য সুপারিশকৃত)
> ২. **Streamable HTTP** - রিমোট সার্ভারগুলোর জন্য যারা অভ্যন্তরীণভাবে SSE ব্যবহার করতে পারে
>
> এই লেসনে আমাদের ফোকাস **stdio ট্রান্সপোর্ট**-এ, যা অধিকাংশ MCP সার্ভার ইমপ্লিমেন্টেশনের জন্য সুপারিশকৃত পদ্ধতি।

stdio ট্রান্সপোর্ট MCP সার্ভারগুলিকে ক্লায়েন্টদের সাথে স্ট্যান্ডার্ড ইনপুট এবং আউটপুট স্ট্রিমের মাধ্যমে যোগাযোগ করার সুযোগ দেয়। এই পদ্ধতিটি বর্তমান MCP স্পেসিফিকেশনে সবচেয়ে বেশি ব্যবহৃত এবং সুপারিশকৃত, যা সহজ এবং কার্যকর উপায়ে MCP সার্ভার তৈরি করতে দেয় যা বিভিন্ন ক্লায়েন্ট অ্যাপ্লিকেশনের সাথে সহজে ইন্টিগ্রেট করা যায়।

## ওভারভিউ

এই লেসনে stdio ট্রান্সপোর্ট ব্যবহার করে কিভাবে MCP সার্ভার তৈরি এবং ব্যবহার করবেন তা বলা হয়েছে।

## শেখার লক্ষ্যসমূহ

এই লেসন শেষে আপনি পারবেন:

- stdio ট্রান্সপোর্ট ব্যবহার করে MCP সার্ভার তৈরি করতে।
- Inspector ব্যবহার করে MCP সার্ভার ডিবাগ করতে।
- Visual Studio Code ব্যবহার করে MCP সার্ভার ব্যবহার করতে।
- বর্তমান MCP ট্রান্সপোর্ট পদ্ধতিগুলো বুঝতে এবং কেন stdio সুপারিশকৃত তা জানতে।

## stdio ট্রান্সপোর্ট - এটি কিভাবে কাজ করে

stdio ট্রান্সপোর্ট বর্তমান MCP স্পেসিফিকেশন (2025-06-18) এ সমর্থিত দুটি ট্রান্সপোর্টের একটি। এটি কাজ করে এভাবে:

- **সহজ যোগাযোগ**: সার্ভার স্ট্যান্ডার্ড ইনপুট (`stdin`) থেকে JSON-RPC মেসেজ পড়ে এবং স্ট্যান্ডার্ড আউটপুট (`stdout`) এ মেসেজ পাঠায়।
- **প্রসেস ভিত্তিক**: ক্লায়েন্ট MCP সার্ভারকে একটি subprocess হিসেবে চালায়।
- **মেসেজ ফরম্যাট**: মেসেজগুলো আলাদা আলাদা JSON-RPC রিকোয়েস্ট, নোটিফিকেশন, বা রেসপন্স যা নিউ লাইনে বিভক্ত।
- **লগিং**: সার্ভার লগ করার জন্য স্ট্যান্ডার্ড এরর (`stderr`) এ UTF-8 স্ট্রিং লেখা যেতে পারে।

### মূল শর্তাবলী:
- মেসেজগুলো অবশ্যই নিউ লাইনে বিভক্ত হতে হবে এবং ভিতরে কোনো এম্বেডেড নিউলাইন থাকা যাবে না
- `stdout` এ সার্ভার থেকে শুধুমাত্র বৈধ MCP মেসেজ লেখা উচিত
- ক্লায়েন্ট থেকে সার্ভারের `stdin` এ শুধুমাত্র বৈধ MCP মেসেজ পাঠানো উচিত

### টাইপস্ক্রিপ্ট

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

উপরের কোডে:

- আমরা MCP SDK থেকে `Server` ক্লাস এবং `StdioServerTransport` কে ইমপোর্ট করি
- একটি সার্ভার ইন্সট্যান্স তৈরি করি বেসিক কনফিগারেশন এবং ক্যাপাবিলিটি সহ
- `StdioServerTransport` ইন্সট্যান্স তৈরি করে সার্ভারকে সেটির সাথে কানেক্ট করি, যা stdin/stdout এর মাধ্যমে যোগাযোগ সক্ষম করে

### পাইথন

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# সার্ভার ইনস্ট্যান্স তৈরি করুন
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

উপরের কোডে আমরা:

- MCP SDK ব্যবহার করে একটি সার্ভার ইন্সট্যান্স তৈরি করি
- ডেকোরেটর ব্যবহার করে টুলস ডিফাইন করি
- stdio_server কনটেক্সট ম্যানেজার ব্যবহার করে ট্রান্সপোর্ট হ্যান্ডেল করি

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

SSE থেকে মূল পার্থক্যগুলি হলো stdio সার্ভারগুলো:

- ওয়েব সার্ভার সেটআপ বা HTTP এন্ডপয়েন্টের দরকার পড়ে না
- ক্লায়েন্ট সেগুলো সাবপ্রসেস হিসেবে চালায়
- stdin/stdout স্ট্রিমের মাধ্যমে যোগাযোগ করে
- ইমপ্লিমেন্ট এবং ডিবাগ করা সহজ

## ব্যায়াম: stdio সার্ভার তৈরি করা

আমরা সার্ভার তৈরি করতে গেলে দুটি বিষয়ে মনোযোগ দিতে হবে:

- কানেকশন এবং মেসেজের জন্য এন্ডপয়েন্ট প্রকাশ করতে ওয়েব সার্ভার ব্যবহার করতে হবে।
## ল্যাব: একটি সাধারণ MCP stdio সার্ভার তৈরি করা

এই ল্যাবে, আমরা সুপারিশকৃত stdio ট্রান্সপোর্ট ব্যবহার করে একটি সাধারণ MCP সার্ভার তৈরি করব। এই সার্ভার ক্লায়েন্টরা মানক Model Context Protocol ব্যবহার করে কল করার জন্য টুলস প্রকাশ করবে।

### প্রয়োজনীয়তা

- পাইথন ৩.৮ বা পরবর্তী
- MCP পাইথন SDK: `pip install mcp`
- অ্যাসিঙ্ক প্রোগ্রামিংয়ের বেসিক ধারণা

আমাদের প্রথম MCP stdio সার্ভার তৈরি শুরু করি:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# লগিং কনফিগার করুন
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# সার্ভার তৈরি করুন
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
    # stdio ট্রান্সপোর্ট ব্যবহার করুন
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ডিপ্রিকেটেড SSE পদ্ধতির সঙ্গে মূল পার্থক্য

**Stdio ট্রান্সপোর্ট (বর্তমান স্ট্যান্ডার্ড):**
- সহজ সাবপ্রসেস মডেল - ক্লায়েন্ট সার্ভারকে চাইল্ড প্রোসেস হিসেবে চালায়
- stdin/stdout দিয়ে JSON-RPC মেসেজের মাধ্যমে যোগাযোগ
- HTTP সার্ভার সেটআপের প্রয়োজন নেই
- উন্নত পারফরম্যান্স ও নিরাপত্তা
- সহজ ডিবাগিং ও ডেভেলপমেন্ট

**SSE ট্রান্সপোর্ট (MCP 2025-06-18 থেকে ডিপ্রিকেটেড):**
- SSE এন্ডপয়েন্ট সহ HTTP সার্ভার থাকা আবশ্যক ছিল
- ওয়েব সার্ভার সেটআপ ও ইনফ্রাস্ট্রাকচারের কারণে বেশি জটিল
- HTTP এন্ডপয়েন্টের অতিরিক্ত নিরাপত্তা বিবেচনা ছিল
- এখন Streamable HTTP দ্বারা প্রতিস্থাপিত

### stdio ট্রান্সপোর্ট সহ সার্ভার তৈরি করা

আমাদের stdio সার্ভার তৈরি করতে হবে:

১. **প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করা** - MCP সার্ভার কম্পোনেন্ট এবং stdio ট্রান্সপোর্ট দরকার
২. **সার্ভার ইন্সট্যান্স তৈরি** - সার্ভার এর ক্যাপাবিলিটি নির্ধারণ
৩. **টুলস ডিফাইন করা** - প্রকাশ করতে চাওয়া ফাংশনালিটি যোগ করা
৪. **ট্রান্সপোর্ট সেটআপ করা** - stdio যোগাযোগ কনফিগারেশন
৫. **সার্ভার চালানো** - সার্ভার শুরু করে মেসেজ হ্যান্ডলিং

ধাপে ধাপে গড়ে তুলি:

### ধাপ ১: একটি বেসিক stdio সার্ভার তৈরি করা

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# লগিং কনফিগার করুন
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# সার্ভার তৈরি করুন
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

### ধাপ ২: আরও টুলস যোগ করা

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

### ধাপ ৩: সার্ভার চালানো

কোডটি `server.py` নামে সংরক্ষণ করুন এবং কমান্ড লাইন থেকে চালান:

```bash
python server.py
```

সার্ভার শুরু হবে এবং stdin থেকে ইনপুটের জন্য অপেক্ষা করবে। এটি stdio ট্রান্সপোর্টের মাধ্যমে JSON-RPC মেসেজ ব্যবহার করে যোগাযোগ করে।

### ধাপ ৪: Inspector দিয়ে পরীক্ষা করা

আপনি MCP Inspector ব্যবহার করে আপনার সার্ভার পরীক্ষা করতে পারেন:

১. Inspector ইনস্টল করুন: `npx @modelcontextprotocol/inspector`
২. Inspector চালান এবং আপনার সার্ভারে পয়েন্ট করুন
৩. তৈরি করা টুলস পরীক্ষা করুন

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio সার্ভার ডিবাগ করা

### MCP Inspector ব্যবহার করা

MCP Inspector MCP সার্ভার ডিবাগ এবং টেস্ট করার জন্য একটি মূল্যবান টুল। stdio সার্ভারের সাথে এটি কীভাবে ব্যবহার করবেন:

১. **Inspector ইনস্টল করুন**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

২. **Inspector চালান**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

৩. **সার্ভার পরীক্ষা করুন**: Inspector একটি ওয়েব ইন্টারফেস দেয় যেখানে আপনি:
   - সার্ভারের ক্ষমতাসমূহ দেখতে পারেন
   - বিভিন্ন প্যারামিটার দিয়ে টুলস টেস্ট করতে পারেন
   - JSON-RPC মেসেজ মনিটর করতে পারেন
   - কানেকশন ইস্যু ডিবাগ করতে পারেন

### VS Code ব্যবহার করে

আপনি সরাসরি VS Code থেকে MCP সার্ভার ডিবাগ করতে পারেন:

১. `.vscode/launch.json` এ একটি লঞ্চ কনফিগারেশন তৈরি করুন:
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

২. সার্ভার কোডে ব্রেকপয়েন্ট সেট করুন
৩. ডিবাগার চালান এবং Inspector দিয়ে টেস্ট করুন

### সাধারণ ডিবাগিং টিপস

- লগিং এর জন্য `stderr` ব্যবহার করুন - `stdout` কখনো লিখবেন না কারণ এটি MCP মেসেজের জন্য রিজার্ভ করা
- সব JSON-RPC মেসেজ অবশ্যই নিউ লাইনে বিভক্ত থাকতে হবে
- প্রথমে সহজ টুল দিয়ে পরীক্ষা করুন, তারপর জটিল ফাংশনালিটি যোগ করুন
- মেসেজ ফরম্যাট যাচাই করতে Inspector ব্যবহার করুন

## VS Code এ আপনার stdio সার্ভার ব্যবহার করা

আপনি MCP stdio সার্ভার তৈরি করার পর, এটি VS Code এর মাধ্যমে Claude বা অন্যান্য MCP-সাপোর্টেড ক্লায়েন্টের সাথে ইন্টিগ্রেট করতে পারেন।

### কনফিগারেশন

১. একটি MCP কনফিগারেশন ফাইল তৈরি করুন `%APPDATA%\Claude\claude_desktop_config.json` (Windows) অথবা `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

২. ক্লড বন্ধ করে পুনরায় চালু করুন যাতে নতুন সার্ভার কনফিগারেশন লোড হয়।

৩. কানেকশন পরীক্ষা করুন: Claude-এর সাথে কথোপকথন শুরু করে আপনার সার্ভারের টুলগুলো ব্যবহার করে দেখুন:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### টাইপস্ক্রিপ্ট stdio সার্ভার উদাহরণ

সম্পূর্ণ টাইপস্ক্রিপ্ট উদাহরণের জন্য:

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

// সরঞ্জাম যোগ করুন
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

### .NET stdio সার্ভার উদাহরণ

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

## সারাংশ

এই আপডেটেড লেসনে আপনি শিখেছেন:

- বর্তমান **stdio ট্রান্সপোর্ট** (সুপারিশকৃত পদ্ধতি) ব্যবহার করে MCP সার্ভার তৈরি করা
- কেন SSE ট্রান্সপোর্ট ডিপ্রিকেটেড হয়েছে এবং stdio ও Streamable HTTP কেন বেশি ভাল
- MCP ক্লায়েন্ট থেকে কল করতে পারা টুলস তৈরি করা
- MCP Inspector ব্যবহার করে সার্ভার ডিবাগ করা
- VS Code এবং Claude এর সাথে stdio সার্ভার ইন্টিগ্রেট করা

stdio ট্রান্সপোর্ট একটি সহজ, নিরাপদ এবং উচ্চ কার্যক্ষমতার পদ্ধতি সরবরাহ করে MCP সার্ভার নির্মাণে, যা ডিপ্রিকেটেড SSE পদ্ধতির থেকে অনেক ভালো। এটি MCP সার্ভারের অধিকাংশ ইমপ্লিমেন্টেশনের জন্য 2025-06-18 স্পেসিফিকেশনের পর সুপারিশকৃত।

### .NET

১. প্রথমে কিছু টুল তৈরি করি, এজন্য আমরা *Tools.cs* নামে একটি ফাইল তৈরি করব নিচের কনটেন্ট সহ:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## ব্যায়াম: আপনার stdio সার্ভার পরীক্ষা করা

আপনি stdio সার্ভার তৈরি করার পর, এটি সঠিকভাবে কাজ করছে কিনা তা পরীক্ষা করা যাক।

### প্রয়োজনীয়তা

১. নিশ্চিত করুন MCP Inspector ইনস্টল করা আছে:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

২. আপনার সার্ভার কোড সংরক্ষিত আছে (যেমন `server.py`)

### Inspector দিয়ে পরীক্ষা

১. **Inspector চালু করুন আপনার সার্ভার নিয়ে**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

২. **ওয়েব ইন্টারফেস খুলুন**: Inspector একটি ব্রাউজার উইন্ডো খুলবে যেখানে আপনার সার্ভারের ক্ষমতাসমূহ দেখানো হবে।

৩. **টুলস পরীক্ষা করুন**: 
   - পরিবত্নন নাম ব্যবহার করে `get_greeting` টুল পরীক্ষা করুন
   - ভিন্ন সংখ্যা নিয়ে `calculate_sum` টুল পরীক্ষা করুন
   - সার্ভার মেটাডাটা দেখতে `get_server_info` টুল কল করুন

৪. **যোগাযোগ মনিটর করুন**: Inspector ক্লায়েন্ট ও সার্ভারের মধ্যে JSON-RPC মেসেজ বিনিময় তুলে ধরে।

### আপনি কি দেখতে পাবেন

যখন আপনার সার্ভার সঠিকভাবে চালু হয়, আপনি দেখতে পাবেন:
- Inspector এ সার্ভারের ক্ষমতাসমূহ তালিকাভুক্ত
- টুলস টেস্ট করার জন্য উপলব্ধ
- সফল JSON-RPC মেসেজ বিনিময়
- ইন্টারফেসে টুল রেসপন্স প্রদর্শিত

### সাধারণ সমস্যা ও সমাধান

**সার্ভার শুরু হয় না:**
- নিশ্চিত করুন সব ডিপেন্ডেন্সি ইনস্টল করা হয়েছে: `pip install mcp`
- পাইথন সিনট্যাক্স ও ইনডেন্টেশন যাচাই করুন
- কনসোলে এরর মেসেজ দেখুন

**টুলস দেখা যাচ্ছে না:**
- নিশ্চিত করুন `@server.tool()` ডেকোরেটর রয়েছে
- `main()` ফাংশনের আগে টুল ফাংশনগুলো ডিফাইন আছে কিনা দেখুন
- সার্ভার ঠিকঠাক কনফিগার আছে কিনা যাচাই করুন

**কানেকশন সমস্যা:**
- সার্ভার stdio ট্রান্সপোর্ট সঠিক ব্যবহার করছে কিনা দেখুন
- অন্য কোনো প্রসেস বাধা দিচ্ছে কিনা পরীক্ষা করুন
- Inspector কমান্ড সিনট্যাক্স সঠিক কিনা দেখুন

## অ্যাসাইনমেন্ট

আপনার সার্ভার আরও ক্ষমতাসম্পন্ন করে তুলুন। [এই পৃষ্ঠা](https://api.chucknorris.io/) দেখতে পারেন, উদাহরণস্বরূপ একটি টুল যোগ করতে যা একটি API কল করবে। সার্ভার কেমন হবে তা আপনি নির্ধারণ করবেন। মজা করুন :)

## সমাধান

[সমাধান](./solution/README.md) এখানে একটি সম্ভাব্য সমাধান দেওয়া হলো যা কাজ করে।

## প্রধান বিষয়গুলো

এই অধ্যায় থেকে সবচেয়ে গুরুত্বপূর্ণ বিষয়গুলো হলো:

- stdio ট্রান্সপোর্ট স্থানীয় MCP সার্ভারের জন্য সুপারিশকৃত পদ্ধতি।
- stdio ট্রান্সপোর্ট MCP সার্ভার ও ক্লায়েন্টের মধ্যে স্ট্যান্ডার্ড ইনপুট ও আউটপুট স্ট্রিম ব্যবহার করে নির্বিঘ্ন যোগাযোগ নিশ্চিত করে।
- আপনাকে Inspector এবং Visual Studio Code ব্যবহার করে সরাসরি stdio সার্ভার ব্যবহার এবং ডিবাগ করার সুযোগ দেয়।

## নমুনা

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## অতিরিক্ত সম্পদ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## পরবর্তী কী

## পরবর্তী ধাপসমূহ

আপনি stdio ট্রান্সপোর্ট ব্যবহার করে MCP সার্ভার তৈরি শিখেছেন, এখন আরও উন্নত বিষয় অন্বেষণ করতে পারেন:

- **পরবর্তী**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - রিমোট সার্ভারের জন্য আরেকটি ট্রান্সপোর্ট পদ্ধতি শিখুন
- **উন্নত**: [MCP Security Best Practices](../../02-Security/README.md) - MCP সার্ভারে নিরাপত্তা বাস্তবায়ন
- **প্রোডাকশন**: [Deployment Strategies](../09-deployment/README.md) - প্রোডাকশনের জন্য সার্ভার ডিপ্লয়মেন্ট

## অতিরিক্ত সম্পদ

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - অফিসিয়াল স্পেসিফিকেশন
- [MCP SDK ডকুমেন্টেশন](https://github.com/modelcontextprotocol/sdk) - সব ভাষার SDK রেফারেন্স
- [কমিউনিটি উদাহরণসমূহ](../../06-CommunityContributions/README.md) - কমিউনিটির আরও সার্ভার উদাহরণসমূহ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**সতর্কতা**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) দিয়ে অনূদিত হয়েছে। যদিও আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে বলে অনুগ্রহ করে সচেতন থাকুন। মূল নথিটি তার স্বাভাবিক ভাষায় সর্বোত্তম উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করা সুপারিশ করা হচ্ছে। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনও ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->