# MCP সার্ভার stdio ট্রান্সপোর্ট সহ

> **⚠️ গুরুত্বপূর্ণ আপডেট**: MCP স্পেসিফিকেশন 2025-06-18 অনুযায়ী, স্ট্যান্ডঅ্যালোন SSE (সার্ভার-সেন্ট ইভেন্টস) ট্রান্সপোর্টটি **অব্যবহৃত** ঘোষণা করা হয়েছে এবং "Streamable HTTP" ট্রান্সপোর্ট দ্বারা প্রতিস্থাপিত হয়েছে। বর্তমান MCP স্পেসিফিকেশন দুটি প্রাথমিক ট্রান্সপোর্ট মেকানিজম নির্ধারণ করে:
> 1. **stdio** - স্ট্যান্ডার্ড ইনপুট/আউটপুট (স্থানীয় সার্ভারের জন্য সুপারিশকৃত)
> 2. **Streamable HTTP** - রিমোট সার্ভারগুলোর জন্য যা অভ্যন্তরীণভাবে SSE ব্যবহার করতে পারে
>
> এই পাঠটি আপডেট করা হয়েছে stdio ট্রান্সপোর্টের উপর ফোকাস করতে, যা অধিকাংশ MCP সার্ভার ইমপ্লিমেন্টেশনের জন্য প্রস্তাবিত পদ্ধতি।

stdio ট্রান্সপোর্ট MCP সার্ভারগুলোকে স্ট্যান্ডার্ড ইনপুট এবং আউটপুট স্ট্রীমের মাধ্যমে ক্লায়েন্টদের সাথে যোগাযোগ করার সুযোগ দেয়। এটি বর্তমানে MCP স্পেসিফিকেশনে সবচেয়ে সাধারণ এবং প্রস্তাবিত ট্রান্সপোর্ট মেকানিজম, যা সহজ এবং দক্ষভাবে MCP সার্ভার তৈরি করার উপায় দেয় যা বিভিন্ন ক্লায়েন্ট অ্যাপ্লিকেশনের সাথে সহজেই সমন্বিত হতে পারে।

## ওভারভিউ

এই পাঠে stdio ট্রান্সপোর্ট ব্যবহার করে MCP সার্ভার তৈরি এবং ব্যবহার করার পদ্ধতি আলোচনা করা হয়েছে।

## শেখার উদ্দেশ্য

এই পাঠের শেষে আপনি পারবেন:

- stdio ট্রান্সপোর্ট ব্যবহার করে MCP সার্ভার তৈরি করা।
- MCP সার্ভার Inspector ব্যবহার করে ডিবাগ করা।
- Visual Studio Code ব্যবহার করে MCP সার্ভার ব্যবহার করা।
- বর্তমান MCP ট্রান্সপোর্ট মেকানিজমগুলো বুঝতে এবং কেন stdio প্রস্তাব করা হয়েছে তা জানতে।


## stdio ট্রান্সপোর্ট - এটি কীভাবে কাজ করে

stdio ট্রান্সপোর্ট বর্তমান MCP স্পেসিফিকেশন (2025-06-18) এ সমর্থিত দুটি ট্রান্সপোর্ট টাইপের একটি। এটি কীভাবে কাজ করে:

- **সিধা যোগাযোগ**: সার্ভার স্ট্যান্ডার্ড ইনপুট (`stdin`) থেকে JSON-RPC মেসেজ পড়ে এবং স্ট্যান্ডার্ড আউটপুট (`stdout`) এ মেসেজ পাঠায়।
- **প্রসেস-ভিত্তিক**: ক্লায়েন্ট MCP সার্ভারকে সাবপ্রসেস হিসেবে লঞ্চ করে।
- **মেসেজ ফরম্যাট**: মেসেজগুলো একক JSON-RPC রিকোয়েস্ট, নোটিফিকেশন অথবা রেসপন্স, যা নিউলাইন দ্বারা আলাদা হয়।
- **লগিং**: লগিংয়ের জন্য সার্ভার স্ট্যান্ডার্ড এরর (`stderr`) এ UTF-8 স্ট্রিং লিখতে পারে।

### মূল শর্তাবলী:
- মেসেজগুলো অবশ্যই নিউলাইন দ্বারা আলাদা থাকবে এবং এতে এম্বেডেড নিউলাইন থাকবে না
- সার্ভার `stdout`-এ এমন কিছু লিখতে পারবে না যা বৈধ MCP মেসেজ নয়
- ক্লায়েন্ট সার্ভারের `stdin`-এ এমন কিছু লিখতে পারবে না যা বৈধ MCP মেসেজ নয়

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
```

উপরের কোডে:

- MCP SDK থেকে `Server` ক্লাস এবং `StdioServerTransport` ইমপোর্ট করা হয়েছে
- মৌলিক কনফিগারেশন এবং সক্ষমতা সহ একটি সার্ভার ইনস্ট্যান্স তৈরি করা হয়েছে

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

- MCP SDK ব্যবহার করে একটি সার্ভার ইনস্ট্যান্স তৈরি করেছি
- ডেকোরেটর দিয়ে টুলস সংজ্ঞায়িত করেছি
- stdio_server কন্টেক্সট ম্যানেজার ব্যবহার করে ট্রান্সপোর্ট পরিচালনা করেছি

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

SSE থেকে প্রধান পার্থক্য হচ্ছে stdio সার্ভার:

- ওয়েব সার্ভার সেটআপ বা HTTP এন্ডপয়েন্ট প্রয়োজন নয়
- ক্লায়েন্ট সাবপ্রসেস হিসেবে সার্ভার চালায়
- stdin/stdout স্ট্রীমের মাধ্যমে যোগাযোগ করে
- ইমপ্লিমেন্ট এবং ডিবাগ করা সহজ

## এক্সারসাইজ: stdio সার্ভার তৈরি করা

আমাদের সার্ভার তৈরি করতে গেলে দুটি বিষয় মাথায় রাখতে হবে:

- আমাদের ওয়েব সার্ভার ব্যবহার করে কানেকশন এবং মেসেজের জন্য এন্ডপয়েন্ট উন্মুক্ত করতে হবে।
## ল্যাব: একটি সহজ MCP stdio সার্ভার তৈরি

এই ল্যাবে, আমরা সুপারিশকৃত stdio ট্রান্সপোর্ট ব্যবহার করে একটি সহজ MCP সার্ভার তৈরি করব। এই সার্ভার ক্লায়েন্টরা স্ট্যান্ডার্ড Model Context Protocol ব্যবহার করে কল করতে পারবে এমন টুলস উন্মুক্ত করবে।

### প্রয়োজনীয়তা

- পাইথন 3.8 বা উপরে
- MCP পাইথন SDK: `pip install mcp`
- অ্যাসিঙ্ক্রোনাস প্রোগ্রামিং এর মৌলিক ধারণা

আমাদের প্রথম MCP stdio সার্ভার তৈরি করা শুরু করি:

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
    # stdio পরিবহন ব্যবহার করুন
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## অব্যবহৃত SSE পদ্ধতির সাথে মূল পার্থক্যসমূহ

**Stdio ট্রান্সপোর্ট (বর্তমান স্ট্যান্ডার্ড):**
- সরল সাবপ্রসেস মডেল - ক্লায়েন্ট সাবপ্রসেস হিসেবে সার্ভার চালায়
- stdin/stdout মাধ্যমে JSON-RPC মেসেজের যোগাযোগ
- HTTP সার্ভার সেটআপের প্রয়োজন নেই
- উন্নত কর্মক্ষমতা এবং নিরাপত্তা
- সহজ ডিবাগিং এবং উন্নয়ন

**SSE ট্রান্সপোর্ট (MCP 2025-06-18 থেকে অব্যবহৃত):**
- SSE এন্ডপয়েন্ট সহ HTTP সার্ভার প্রয়োজন ছিল
- ওয়েব সার্ভার কাঠামোর আরও জটিল সেটআপ
- HTTP এন্ডপয়েন্টের জন্য অতিরিক্ত নিরাপত্তা বিবেচনা
- এখন ওয়েব-ভিত্তিক পরিস্থিতির জন্য Streamable HTTP দ্বারা প্রতিস্থাপিত

### stdio ট্রান্সপোর্ট সহ সার্ভার তৈরি করা

আমাদের stdio সার্ভার তৈরি করতে হবে:

1. **প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করুন** - MCP সার্ভার কম্পোনেন্ট এবং stdio ট্রান্সপোর্ট দরকার
2. **সার্ভার ইনস্ট্যান্স তৈরি করুন** - সক্ষমতাসহ সার্ভার সংজ্ঞায়িত করুন
3. **টুলস সংজ্ঞায়িত করুন** - এক্সপোজ করতে চান এমন ফাংশনালিটি যোগ করুন
4. **ট্রান্সপোর্ট সেটআপ করুন** - stdio যোগাযোগ কনফিগার করুন
5. **সার্ভার চালান** - সার্ভার শুরু করুন এবং মেসেজ পরিচালনা করুন

ধাপে ধাপে তৈরি করি:

### ধাপ 1: একটি বেসিক stdio সার্ভার তৈরি করুন

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

### ধাপ 2: আরও টুলস যোগ করুন

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

### ধাপ 3: সার্ভার চালানো

`server.py` নামে কোড সংরক্ষণ করুন এবং কমান্ড লাইনের মাধ্যমে চালান:

```bash
python server.py
```

সার্ভার শুরু হবে এবং stdin থেকে ইনপুটের জন্য অপেক্ষা করবে। এটি stdio ট্রান্সপোর্টের মাধ্যমে JSON-RPC মেসেজ ব্যবহার করে যোগাযোগ করে।

### ধাপ 4: Inspector দিয়ে পরীক্ষা

আপনি MCP Inspector ব্যবহার করে আপনার সার্ভার পরীক্ষা করতে পারেন:

1. Inspector ইনস্টল করুন: `npx @modelcontextprotocol/inspector`
2. Inspector চালু করুন এবং আপনার সার্ভার পয়েন্ট করুন
3. আপনি তৈরি করা টুলগুলো পরীক্ষা করুন

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## আপনার stdio সার্ভার ডিবাগিং

### MCP Inspector ব্যবহার

MCP Inspector MCP সার্ভার ডিবাগিং এবং টেস্টিংয়ের একটি মূল্যবান টুল। এটি আপনার stdio সার্ভারের সাথে ব্যবহার করার পদ্ধতি:

1. **Inspector ইনস্টল করুন**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector চালান**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **সার্ভার পরীক্ষা করুন**: Inspector একটি ওয়েব ইন্টারফেস দেয় যেখানে আপনি পারবেন:
   - সার্ভারের সক্ষমতা দেখুন
   - বিভিন্ন প্যারামিটার দিয়ে টুল পরীক্ষা করুন
   - JSON-RPC মেসেজ পর্যবেক্ষণ করুন
   - কানেকশন সমস্যাগুলো ডিবাগ করুন

### VS Code ব্যবহার

আপনি সরাসরি VS Code তেও MCP সার্ভার ডিবাগ করা যাবে:

1. `.vscode/launch.json` এ একটি লঞ্চ কনফিগারেশন তৈরি করুন:
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

2. সার্ভার কোডে ব্রেকপয়েন্ট সেট করুন
3. ডিবাগার চালান এবং Inspector দিয়ে পরীক্ষা করুন

### সাধারণ ডিবাগিং টিপস

- লগিংয়ের জন্য `stderr` ব্যবহার করুন - `stdout` এ কখনও কিছু লিখবেন না কারণ এটি MCP মেসেজের জন্য সংরক্ষিত
- নিশ্চিত করুন সব JSON-RPC মেসেজ নিউলাইন-দ্বারা আলাদা
- সহজ টুল দিয়ে প্রথমে পরীক্ষা করুন তারপর জটিল ফাংশনালিটি যোগ করুন
- মেসেজ ফরম্যাট যাচাই করতে Inspector ব্যবহার করুন

## VS Code-এ আপনার stdio সার্ভার ব্যবহার করা

আপনি যখন MCP stdio সার্ভার বানিয়ে ফেলেছেন, তখন এটিকে VS Code এর মাধ্যমে Claude বা অন্য MCP-সমর্থিত ক্লায়েন্টের সাথে সংযুক্ত করতে পারেন।

### কনফিগারেশন

1. একটি MCP কনফিগারেশন ফাইল তৈরি করুন `%APPDATA%\Claude\claude_desktop_config.json` (Windows) অথবা `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. Claude পুনরায় চালু করুন: Claude বন্ধ করুন এবং আবার খুলুন যাতে নতুন সার্ভার কনফিগারেশন লোড হয়।

3. কানেকশন পরীক্ষা করুন: Claude এর সাথে কথোপকথন শুরু করুন এবং আপনার সার্ভারের টুল ব্যবহার করে দেখুন:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### টাইপস্ক্রিপ্ট stdio সার্ভার উদাহরণ

রেফারেন্সের জন্য সম্পূর্ণ টাইপস্ক্রিপ্ট উদাহরণ:

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

## সারসংক্ষেপ

এই আপডেট করা পাঠে, আপনি শিখেছেন:

- বর্তমান **stdio ট্রান্সপোর্ট** ব্যবহার করে MCP সার্ভার তৈরি করতে (সুপারিশকৃত পদ্ধতি)
- কেন SSE ট্রান্সপোর্ট অব্যবহৃত হলো এবং stdio ও Streamable HTTP এর পক্ষে হয়েছে
- MCP ক্লায়েন্ট দ্বারা কল করা যেতে পারে এমন টুলস তৈরি করতে
- MCP Inspector ব্যবহার করে সার্ভার ডিবাগ করতে
- stdio সার্ভার VS Code এবং Claude এর সাথে সংযুক্ত করতে

stdio ট্রান্সপোর্ট একটি সহজ, আরও সুরক্ষিত এবং উচ্চ কর্মক্ষমতা সম্পন্ন পদ্ধতি MCP সার্ভার তৈরি করার জন্য যা অব্যবহৃত SSE পদ্ধতির তুলনায় উন্নত। 2025-06-18 স্পেসিফিকেশন অনুসারে এটি অধিকাংশ MCP সার্ভার ইমপ্লিমেন্টেশনের জন্য প্রস্তাবিত।

### .NET

1. প্রথমে কিছু টুল তৈরি করি, এর জন্য একটি ফাইল *Tools.cs* তৈরি করব নিম্নলিখিত বিষয়বস্তু সহ:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## এক্সারসাইজ: আপনার stdio সার্ভার পরীক্ষা

এখন যেহেতু আপনি আপনার stdio সার্ভার তৈরি করে ফেলেছেন, চলুন পরীক্ষা করে দেখি এটি সঠিকভাবে কাজ করছে কিনা।

### প্রয়োজনীয়তা

1. MCP Inspector ইনস্টল আছে কিনা নিশ্চিত করুন:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. আপনার সার্ভার কোড সংরক্ষণ করুন (যেমন, `server.py`)

### Inspector দিয়ে পরীক্ষা করা

1. **Inspector আপনার সার্ভার দিয়ে চালান**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ওয়েব ইন্টারফেস খুলুন**: Inspector একটি ব্রাউজার উইন্ডো খুলবে যেখানে আপনার সার্ভারের সক্ষমতাসমূহ দেখাবে।

3. **টুলস পরীক্ষা করুন**: 
   - `get_greeting` টুল বিভিন্ন নামে চেষ্টা করুন
   - `calculate_sum` টুল বিভিন্ন সংখ্যায় পরীক্ষা করুন
   - সার্ভারের মেটাডেটা দেখতে `get_server_info` টুল কল করুন

4. **যোগাযোগ নজরদারি করুন**: Inspector দেখায় ক্লায়েন্ট এবং সার্ভারের মধ্যে JSON-RPC মেসেজ বিনিময়।

### আপনি যা দেখতে পাবেন

যখন আপনার সার্ভার সঠিকভাবে শুরু হবে, তখন দেখতে পাবেন:
- Inspector-এ সার্ভারের সক্ষমতা তালিকাভুক্ত
- টেস্ট করার জন্য টুলস উপলব্ধ
- সফল JSON-RPC মেসেজ আদান-প্রদান
- ইন্টারফেসে টুল রেসপন্স দেখানো হবে

### সাধারণ সমস্যা এবং সমাধান

**সার্ভার শুরু হচ্ছে না:**
- সমস্ত ডিপেনডেন্সি ইনস্টল হয়েছে কিনা দেখুন: `pip install mcp`
- পাইথন সিনট্যাক্স এবং ইন্ডেন্টেশন পরীক্ষা করুন
- কনসোল-এ ত্রুটি মেসেজ দেখুন

**টুলস প্রদর্শিত হচ্ছে না:**
- নিশ্চিত করুন `@server.tool()` ডেকোরেটর আছে
- `main()` এর আগে টুল ফাংশন ডিফাইন করা হয়েছে কিনা দেখুন
- সার্ভার সঠিক কনফিগার করা আছে কিনা যাচাই করুন

**কানেকশন সমস্যা:**
- সার্ভার stdio ট্রান্সপোর্ট সঠিক ব্যবহার করছে কিনা নিশ্চিত করুন
- অন্যান্য প্রসেস বাধা দিচ্ছে কিনা পরীক্ষা করুন
- Inspector কমান্ড সিনট্যাক্স যাচাই করুন

## অ্যাসাইনমেন্ট

আপনার সার্ভার আরও সক্ষমতা সহ তৈরি করার চেষ্টা করুন। যেমন, [এই পৃষ্ঠা](https://api.chucknorris.io/) থেকে একটা API কল করে টুল তৈরি করতে পারেন। সার্ভারের আকার আপনি নির্ধারণ করবেন। মজা করুন :)

## সমাধান

[সমাধান](./solution/README.md) এখানে একটি কাজ করা কোড সহ সম্ভব সমাধান দেয়া হয়েছে।

## মূল বিষয়সমূহ

এই অধ্যায় থেকে মূল বোধগম্য বিষয়গুলো হল:

- stdio ট্রান্সপোর্ট স্থানীয় MCP সার্ভারগুলোর জন্য সুপারিশকৃত মেকানিজম।
- stdio ট্রান্সপোর্ট স্ট্যান্ডার্ড ইনপুট এবং আউটপুট স্ট্রীম ব্যবহার করে MCP সার্ভার ও ক্লায়েন্টের মধ্যে নির্বিঘ্ন যোগাযোগ প্রদান করে।
- আপনি Inspector এবং Visual Studio Code উভয় ব্যবহার করে সরাসরি stdio সার্ভার ব্যবহার ও ডিবাগ করতে পারেন, যা ডিবাগিং এবং সংহতকরণ সহজ করে।

## নমুনা 

- [জাভা ক্যালকুলেটর](../samples/java/calculator/README.md)
- [.Net ক্যালকুলেটর](../../../../03-GettingStarted/samples/csharp)
- [জাভাস্ক্রিপ্ট ক্যালকুলেটর](../samples/javascript/README.md)
- [টাইপস্ক্রিপ্ট ক্যালকুলেটর](../samples/typescript/README.md)
- [পাইথন ক্যালকুলেটর](../../../../03-GettingStarted/samples/python)

## অতিরিক্ত সম্পদ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## পরবর্তী ধাপ

## আগামী ধাপসমূহ

আপনি stdio ট্রান্সপোর্ট ব্যবহার করে MCP সার্ভার তৈরি করা শিখেছেন, এখন আরও উন্নত বিষয় অনুসন্ধান করতে পারেন:

- **পরবর্তী**: [MCP এর HTTP স্ট্রিমিং (Streamable HTTP)](../06-http-streaming/README.md) - রিমোট সার্ভারের জন্য অন্য সমর্থিত ট্রান্সপোর্ট মেকানিজম।
- **উন্নত**: [MCP সিকিউরিটি সেরা অনুশীলন](../../02-Security/README.md) - MCP সার্ভারে নিরাপত্তা বাস্তবায়ন।
- **প্রোডাকশন**: [ডিপ্লয়মেন্ট স্ট্র্যাটেজি](../09-deployment/README.md) - প্রোডাকশনের জন্য আপনার সার্ভার ডিপ্লয় করা।

## অতিরিক্ত উত্স

- [MCP স্পেসিফিকেশন 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - অফিসিয়াল স্পেসিফিকেশন
- [MCP SDK ডকুমেন্টেশন](https://github.com/modelcontextprotocol/sdk) - সব ভাষার SDK রেফারেন্স
- [কমিউনিটি উদাহরণ](../../06-CommunityContributions/README.md) - কমিউনিটির আরো সার্ভার উদাহরণ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ডিসক্লেইমার**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসত্যতা থাকতে পারে তা অনুগ্রহ করে বিবেচনা করুন। মূল নথি তার মাতৃভাষায় কর্তৃপক্ষ সম্পন্ন উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো বিভ্রান্তি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->