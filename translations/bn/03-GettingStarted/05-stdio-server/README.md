# MCP সার্ভার stdio পরিবহন সহ

> **⚠️ গুরুত্বপূর্ণ আপডেট**: MCP স্পেসিফিকেশন 2025-06-18 অনুযায়ী, স্ট্যান্ডঅ্যালোন SSE (Server-Sent Events) পরিবহন **অপ্রচলিত** এবং "Streamable HTTP" পরিবহনে প্রতিস্থাপিত হয়েছে। বর্তমান MCP স্পেসিফিকেশন দুটি প্রধান পরিবহন পদ্ধতি সংজ্ঞায়িত করে:
> 1. **stdio** - স্ট্যান্ডার্ড ইনপুট/আউটপুট (স্থানীয় সার্ভারের জন্য সুপারিশকৃত)
> 2. **Streamable HTTP** - দূরবর্তী সার্ভারের জন্য যা অভ্যন্তরীণভাবে SSE ব্যবহার করতে পারে
>
> এই পাঠটি **stdio পরিবহন**-এর উপর ফোকাস করতে আপডেট করা হয়েছে, যা বেশিরভাগ MCP সার্ভার বাস্তবায়নের জন্য সুপারিশকৃত পদ্ধতি।

stdio পরিবহন MCP সার্ভারগুলিকে স্ট্যান্ডার্ড ইনপুট এবং আউটপুট স্ট্রিমের মাধ্যমে ক্লায়েন্টদের সাথে যোগাযোগ করতে দেয়। এটি বর্তমান MCP স্পেসিফিকেশনে সবচেয়ে সাধারণ এবং সুপারিশকৃত পরিবহন পদ্ধতি, যা MCP সার্ভার তৈরি করার একটি সহজ এবং কার্যকর উপায় প্রদান করে যা বিভিন্ন ক্লায়েন্ট অ্যাপ্লিকেশনের সাথে সহজেই সংহত করা যায়।

## সংক্ষিপ্ত বিবরণ

এই পাঠটি stdio পরিবহন ব্যবহার করে MCP সার্ভার তৈরি এবং ব্যবহার করার পদ্ধতি কভার করে।

## শেখার লক্ষ্য

এই পাঠ শেষে, আপনি সক্ষম হবেন:

- stdio পরিবহন ব্যবহার করে MCP সার্ভার তৈরি করতে।
- MCP সার্ভারকে Inspector দিয়ে ডিবাগ করতে।
- Visual Studio Code ব্যবহার করে MCP সার্ভার ব্যবহার করতে।
- বর্তমান MCP পরিবহন পদ্ধতি এবং stdio কেন সুপারিশকৃত তা বুঝতে।

## stdio পরিবহন - এটি কীভাবে কাজ করে

stdio পরিবহন বর্তমান MCP স্পেসিফিকেশনে (2025-06-18) সমর্থিত দুটি পরিবহন প্রকারের একটি। এটি কীভাবে কাজ করে:

- **সহজ যোগাযোগ**: সার্ভার স্ট্যান্ডার্ড ইনপুট (`stdin`) থেকে JSON-RPC বার্তা পড়ে এবং স্ট্যান্ডার্ড আউটপুট (`stdout`) এ বার্তা পাঠায়।
- **প্রক্রিয়া-ভিত্তিক**: ক্লায়েন্ট MCP সার্ভারকে একটি সাবপ্রসেস হিসাবে চালু করে।
- **বার্তা বিন্যাস**: বার্তাগুলি পৃথক JSON-RPC অনুরোধ, বিজ্ঞপ্তি বা প্রতিক্রিয়া, যা নতুন লাইনের মাধ্যমে পৃথক করা হয়।
- **লগিং**: সার্ভার লগিং উদ্দেশ্যে স্ট্যান্ডার্ড ত্রুটি (`stderr`) এ UTF-8 স্ট্রিং লিখতে পারে।

### প্রধান প্রয়োজনীয়তা:
- বার্তাগুলি অবশ্যই নতুন লাইনের মাধ্যমে পৃথক করা হবে এবং এতে এম্বেডেড নতুন লাইন থাকা উচিত নয়।
- সার্ভার `stdout`-এ এমন কিছু লিখতে পারবে না যা বৈধ MCP বার্তা নয়।
- ক্লায়েন্ট সার্ভারের `stdin`-এ এমন কিছু লিখতে পারবে না যা বৈধ MCP বার্তা নয়।

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

উপরের কোডে:

- আমরা MCP SDK থেকে `Server` ক্লাস এবং `StdioServerTransport` আমদানি করি।
- আমরা মৌলিক কনফিগারেশন এবং সক্ষমতা সহ একটি সার্ভার ইনস্ট্যান্স তৈরি করি।

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

উপরের কোডে আমরা:

- MCP SDK ব্যবহার করে একটি সার্ভার ইনস্ট্যান্স তৈরি করি।
- ডেকোরেটর ব্যবহার করে টুল সংজ্ঞায়িত করি।
- stdio_server কনটেক্সট ম্যানেজার ব্যবহার করে পরিবহন পরিচালনা করি।

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

SSE থেকে stdio সার্ভারের মূল পার্থক্য:

- ওয়েব সার্ভার সেটআপ বা HTTP এন্ডপয়েন্টের প্রয়োজন নেই।
- ক্লায়েন্ট দ্বারা সাবপ্রসেস হিসাবে চালু করা হয়।
- stdin/stdout স্ট্রিমের মাধ্যমে যোগাযোগ করে।
- বাস্তবায়ন এবং ডিবাগ করা সহজ।

## অনুশীলন: একটি stdio সার্ভার তৈরি করা

আমাদের সার্ভার তৈরি করতে, দুটি বিষয় মনে রাখতে হবে:

- সংযোগ এবং বার্তার জন্য এন্ডপয়েন্ট প্রকাশ করতে একটি ওয়েব সার্ভার ব্যবহার করতে হবে।

## ল্যাব: একটি সাধারণ MCP stdio সার্ভার তৈরি করা

এই ল্যাবে, আমরা stdio পরিবহন ব্যবহার করে একটি সাধারণ MCP সার্ভার তৈরি করব। এই সার্ভারটি টুল প্রকাশ করবে যা ক্লায়েন্টরা স্ট্যান্ডার্ড Model Context Protocol ব্যবহার করে কল করতে পারবে।

### প্রয়োজনীয়তা

- Python 3.8 বা তার পরবর্তী সংস্করণ
- MCP Python SDK: `pip install mcp`
- অ্যাসিঙ্ক প্রোগ্রামিংয়ের মৌলিক ধারণা

চলুন আমাদের প্রথম MCP stdio সার্ভার তৈরি করি:

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

## অপ্রচলিত SSE পদ্ধতির সাথে মূল পার্থক্য

**Stdio পরিবহন (বর্তমান মান):**
- সহজ সাবপ্রসেস মডেল - ক্লায়েন্ট সার্ভারকে চাইল্ড প্রসেস হিসাবে চালু করে।
- stdin/stdout ব্যবহার করে JSON-RPC বার্তার মাধ্যমে যোগাযোগ।
- HTTP সার্ভার সেটআপের প্রয়োজন নেই।
- উন্নত পারফরম্যান্স এবং নিরাপত্তা।
- সহজ ডিবাগিং এবং উন্নয়ন।

**SSE পরিবহন (MCP 2025-06-18 অনুযায়ী অপ্রচলিত):**
- SSE এন্ডপয়েন্ট সহ HTTP সার্ভারের প্রয়োজন।
- ওয়েব সার্ভার অবকাঠামো সহ আরও জটিল সেটআপ।
- HTTP এন্ডপয়েন্টের জন্য অতিরিক্ত নিরাপত্তা বিবেচনা।
- ওয়েব-ভিত্তিক পরিস্থিতির জন্য Streamable HTTP দ্বারা প্রতিস্থাপিত।

### stdio পরিবহন সহ একটি সার্ভার তৈরি করা

stdio সার্ভার তৈরি করতে আমাদের করতে হবে:

1. **প্রয়োজনীয় লাইব্রেরি আমদানি করা** - MCP সার্ভার কম্পোনেন্ট এবং stdio পরিবহন প্রয়োজন।
2. **একটি সার্ভার ইনস্ট্যান্স তৈরি করা** - সার্ভারকে তার সক্ষমতা সহ সংজ্ঞায়িত করা।
3. **টুল সংজ্ঞায়িত করা** - আমরা যে কার্যকারিতা প্রকাশ করতে চাই তা যোগ করা।
4. **পরিবহন সেটআপ করা** - stdio যোগাযোগ কনফিগার করা।
5. **সার্ভার চালানো** - সার্ভার শুরু করা এবং বার্তা পরিচালনা করা।

চলুন ধাপে ধাপে এটি তৈরি করি:

### ধাপ ১: একটি মৌলিক stdio সার্ভার তৈরি করা

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

### ধাপ ২: আরও টুল যোগ করা

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

সার্ভার শুরু হবে এবং stdin থেকে ইনপুটের জন্য অপেক্ষা করবে। এটি stdio পরিবহন ব্যবহার করে JSON-RPC বার্তার মাধ্যমে যোগাযোগ করে।

### ধাপ ৪: Inspector দিয়ে পরীক্ষা করা

আপনার সার্ভার MCP Inspector ব্যবহার করে পরীক্ষা করতে পারেন:

1. Inspector ইনস্টল করুন: `npx @modelcontextprotocol/inspector`
2. Inspector চালান এবং আপনার সার্ভারের দিকে নির্দেশ করুন।
3. আপনি যে টুল তৈরি করেছেন তা পরীক্ষা করুন।

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## আপনার stdio সার্ভার ডিবাগ করা

### MCP Inspector ব্যবহার করে

MCP Inspector MCP সার্ভার ডিবাগ এবং পরীক্ষা করার জন্য একটি মূল্যবান টুল। এটি আপনার stdio সার্ভারের সাথে কীভাবে ব্যবহার করবেন:

1. **Inspector ইনস্টল করুন**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector চালান**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **আপনার সার্ভার পরীক্ষা করুন**: Inspector একটি ওয়েব ইন্টারফেস প্রদান করে যেখানে আপনি:
   - সার্ভারের সক্ষমতা দেখতে পারেন।
   - বিভিন্ন প্যারামিটার সহ টুল পরীক্ষা করতে পারেন।
   - JSON-RPC বার্তা পর্যবেক্ষণ করতে পারেন।
   - সংযোগ সমস্যাগুলি ডিবাগ করতে পারেন।

### Visual Studio Code ব্যবহার করে

আপনার MCP সার্ভার সরাসরি VS Code-এ ডিবাগ করতে পারেন:

1. `.vscode/launch.json`-এ একটি লঞ্চ কনফিগারেশন তৈরি করুন:
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

2. আপনার সার্ভার কোডে ব্রেকপয়েন্ট সেট করুন।
3. ডিবাগার চালান এবং Inspector দিয়ে পরীক্ষা করুন।

### সাধারণ ডিবাগিং টিপস

- লগিংয়ের জন্য `stderr` ব্যবহার করুন - কখনোই `stdout`-এ লিখবেন না কারণ এটি MCP বার্তার জন্য সংরক্ষিত।
- নিশ্চিত করুন যে সমস্ত JSON-RPC বার্তা নতুন লাইনে পৃথক করা হয়েছে।
- জটিল কার্যকারিতা যোগ করার আগে সহজ টুল দিয়ে পরীক্ষা করুন।
- বার্তা বিন্যাস যাচাই করতে Inspector ব্যবহার করুন।

## Visual Studio Code-এ আপনার stdio সার্ভার ব্যবহার করা

আপনার MCP stdio সার্ভার তৈরি করার পরে, আপনি এটি Claude বা অন্যান্য MCP-সামঞ্জস্যপূর্ণ ক্লায়েন্টের সাথে ব্যবহার করতে VS Code-এ সংহত করতে পারেন।

### কনফিগারেশন

1. **একটি MCP কনফিগারেশন ফাইল তৈরি করুন** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) বা `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac)-এ:

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

2. **Claude পুনরায় চালু করুন**: নতুন সার্ভার কনফিগারেশন লোড করতে Claude বন্ধ করুন এবং পুনরায় খুলুন।

3. **সংযোগ পরীক্ষা করুন**: Claude-এর সাথে একটি কথোপকথন শুরু করুন এবং আপনার সার্ভারের টুলগুলি ব্যবহার করার চেষ্টা করুন:
   - "আমাকে অভিবাদন টুল ব্যবহার করে অভিবাদন করতে পারো?"
   - "15 এবং 27 এর যোগফল গণনা করো।"
   - "সার্ভারের তথ্য কী?"

### TypeScript stdio সার্ভারের উদাহরণ

এখানে একটি সম্পূর্ণ TypeScript উদাহরণ:

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

### .NET stdio সার্ভারের উদাহরণ

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

## সারসংক্ষেপ

এই আপডেট করা পাঠে, আপনি শিখেছেন:

- বর্তমান **stdio পরিবহন** (সুপারিশকৃত পদ্ধতি) ব্যবহার করে MCP সার্ভার তৈরি করতে।
- SSE পরিবহন কেন stdio এবং Streamable HTTP দ্বারা প্রতিস্থাপিত হয়েছে তা বুঝতে।
- MCP ক্লায়েন্ট দ্বারা কল করা যেতে পারে এমন টুল তৈরি করতে।
- MCP Inspector ব্যবহার করে আপনার সার্ভার ডিবাগ করতে।
- Visual Studio Code এবং Claude-এর সাথে আপনার stdio সার্ভার সংহত করতে।

stdio পরিবহন একটি সহজ, আরও নিরাপদ এবং আরও কার্যকর উপায় প্রদান করে MCP সার্ভার তৈরি করার জন্য, যা অপ্রচলিত SSE পদ্ধতির তুলনায় অনেক বেশি সুবিধাজনক। এটি 2025-06-18 স্পেসিফিকেশন অনুযায়ী বেশিরভাগ MCP সার্ভার বাস্তবায়নের জন্য সুপারিশকৃত পরিবহন।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।