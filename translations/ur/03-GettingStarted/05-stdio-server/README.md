# ایم سی پی سرور مع اسٹڈیو ٹرانسپورٹ

> **⚠️ اہم اپڈیٹ**: ایم سی پی اسپیسفیکیشن 2025-06-18 کے مطابق، اسٹینڈ الون ایس ایس ای (سرور-سینٹ ایونٹس) ٹرانسپورٹ کو **منسوخ** کر دیا گیا ہے اور "اسٹریمیبل HTTP" ٹرانسپورٹ سے تبدیل کر دیا گیا ہے۔ موجودہ ایم سی پی اسپیسفیکیشن دو بنیادی ٹرانسپورٹ میکانزمز کی وضاحت کرتا ہے:
> 1. **stdio** - اسٹینڈرڈ ان پٹ/آؤٹ پٹ (مقامی سرورز کے لیے تجویز کردہ)
> 2. **اسٹریمیبل HTTP** - دور دراز سرورز کے لیے جو اندرونی طور پر ایس ایس ای استعمال کر سکتے ہیں
>
> یہ سبق **stdio ٹرانسپورٹ** پر مرکوز کرنے کے لیے اپڈیٹ کیا گیا ہے، جو زیادہ تر ایم سی پی سرور امپلیمنٹیشنز کے لیے تجویز کردہ طریقہ ہے۔

stdio ٹرانسپورٹ ایم سی پی سرورز کو کلائنٹس کے ساتھ اسٹینڈرڈ ان پٹ اور آؤٹ پٹ اسٹریمز کے ذریعے بات چیت کرنے کی اجازت دیتا ہے۔ یہ موجودہ ایم سی پی اسپیسفیکیشن میں سب سے زیادہ استعمال ہونے والا اور تجویز کردہ ٹرانسپورٹ میکانزم ہے، جو ایم سی پی سرورز کو مختلف کلائنٹ ایپلیکیشنز کے ساتھ آسانی سے انٹیگریٹ کرنے کا ایک سادہ اور مؤثر طریقہ فراہم کرتا ہے۔

## جائزہ

یہ سبق ایم سی پی سرورز کو stdio ٹرانسپورٹ کے ذریعے بنانے اور استعمال کرنے کا طریقہ بیان کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ:

- stdio ٹرانسپورٹ کا استعمال کرتے ہوئے ایم سی پی سرور بنا سکیں گے۔
- ایم سی پی سرور کو انسپیکٹر کے ذریعے ڈیبگ کر سکیں گے۔
- ایم سی پی سرور کو ویژول اسٹوڈیو کوڈ کے ذریعے استعمال کر سکیں گے۔
- موجودہ ایم سی پی ٹرانسپورٹ میکانزمز کو سمجھ سکیں گے اور جان سکیں گے کہ stdio کیوں تجویز کیا جاتا ہے۔

## stdio ٹرانسپورٹ - یہ کیسے کام کرتا ہے

stdio ٹرانسپورٹ موجودہ ایم سی پی اسپیسفیکیشن (2025-06-18) میں دو معاون ٹرانسپورٹ اقسام میں سے ایک ہے۔ یہ اس طرح کام کرتا ہے:

- **سادہ مواصلت**: سرور اسٹینڈرڈ ان پٹ (`stdin`) سے JSON-RPC پیغامات پڑھتا ہے اور اسٹینڈرڈ آؤٹ پٹ (`stdout`) پر پیغامات بھیجتا ہے۔
- **پروسیس پر مبنی**: کلائنٹ ایم سی پی سرور کو سب پروسیس کے طور پر لانچ کرتا ہے۔
- **پیغام کی شکل**: پیغامات انفرادی JSON-RPC درخواستیں، نوٹیفیکیشنز، یا جوابات ہوتے ہیں، جو نئی لائنز سے الگ کیے جاتے ہیں۔
- **لاگنگ**: سرور لاگنگ کے لیے اسٹینڈرڈ ایرر (`stderr`) پر UTF-8 اسٹرنگز لکھ سکتا ہے۔

### اہم ضروریات:
- پیغامات نئی لائنز سے الگ کیے جانے چاہئیں اور ان میں اندرونی نئی لائنز نہیں ہونی چاہئیں۔
- سرور کو `stdout` پر کچھ بھی نہیں لکھنا چاہیے جو ایم سی پی پیغام کے طور پر درست نہ ہو۔
- کلائنٹ کو سرور کے `stdin` پر کچھ بھی نہیں لکھنا چاہیے جو ایم سی پی پیغام کے طور پر درست نہ ہو۔

### ٹائپ اسکرپٹ

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

اوپر دیے گئے کوڈ میں:

- ہم ایم سی پی ایس ڈی کے سے `Server` کلاس اور `StdioServerTransport` کو امپورٹ کرتے ہیں۔
- ہم بنیادی کنفیگریشن اور صلاحیتوں کے ساتھ ایک سرور انسٹینس بناتے ہیں۔

### پائتھون

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

اوپر دیے گئے کوڈ میں ہم:

- ایم سی پی ایس ڈی کے کا استعمال کرتے ہوئے ایک سرور انسٹینس بناتے ہیں۔
- ڈیکوریٹرز کے ذریعے ٹولز کی وضاحت کرتے ہیں۔
- stdio_server کانٹیکسٹ مینیجر کا استعمال کرتے ہوئے ٹرانسپورٹ کو ہینڈل کرتے ہیں۔

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

ایس ایس ای سے اہم فرق یہ ہے کہ stdio سرورز:

- ویب سرور سیٹ اپ یا HTTP اینڈ پوائنٹس کی ضرورت نہیں رکھتے۔
- کلائنٹ کے ذریعے سب پروسیس کے طور پر لانچ کیے جاتے ہیں۔
- stdin/stdout اسٹریمز کے ذریعے بات چیت کرتے ہیں۔
- نافذ کرنے اور ڈیبگ کرنے میں آسان ہیں۔

## مشق: stdio سرور بنانا

اپنا سرور بنانے کے لیے، ہمیں دو چیزوں کو ذہن میں رکھنا ہوگا:

- ہمیں کنکشن اور پیغامات کے لیے اینڈ پوائنٹس کو ظاہر کرنے کے لیے ایک ویب سرور استعمال کرنا ہوگا۔

## لیب: ایک سادہ ایم سی پی stdio سرور بنانا

اس لیب میں، ہم تجویز کردہ stdio ٹرانسپورٹ کا استعمال کرتے ہوئے ایک سادہ ایم سی پی سرور بنائیں گے۔ یہ سرور وہ ٹولز ظاہر کرے گا جنہیں کلائنٹس اسٹینڈرڈ ماڈل کانٹیکسٹ پروٹوکول کا استعمال کرتے ہوئے کال کر سکتے ہیں۔

### ضروریات

- پائتھون 3.8 یا اس سے جدید
- ایم سی پی پائتھون ایس ڈی کے: `pip install mcp`
- async پروگرامنگ کی بنیادی سمجھ

آئیے اپنا پہلا ایم سی پی stdio سرور بناتے ہیں:

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

## منسوخ شدہ ایس ایس ای طریقہ سے اہم فرق

**Stdio ٹرانسپورٹ (موجودہ معیار):**
- سادہ سب پروسیس ماڈل - کلائنٹ سرور کو چائلڈ پروسیس کے طور پر لانچ کرتا ہے۔
- stdin/stdout کے ذریعے JSON-RPC پیغامات کے ساتھ مواصلت۔
- HTTP سرور سیٹ اپ کی ضرورت نہیں۔
- بہتر کارکردگی اور سیکیورٹی۔
- آسان ڈیبگنگ اور ترقی۔

**SSE ٹرانسپورٹ (ایم سی پی 2025-06-18 کے مطابق منسوخ):**
- HTTP سرور کے ساتھ ایس ایس ای اینڈ پوائنٹس کی ضرورت تھی۔
- ویب سرور انفراسٹرکچر کے ساتھ زیادہ پیچیدہ سیٹ اپ۔
- HTTP اینڈ پوائنٹس کے لیے اضافی سیکیورٹی کے مسائل۔
- اب ویب پر مبنی منظرناموں کے لیے اسٹریمیبل HTTP سے تبدیل کر دیا گیا ہے۔

### stdio ٹرانسپورٹ کے ساتھ سرور بنانا

اپنا stdio سرور بنانے کے لیے ہمیں:

1. **ضروری لائبریریاں امپورٹ کریں** - ہمیں ایم سی پی سرور کے اجزاء اور stdio ٹرانسپورٹ کی ضرورت ہے۔
2. **سرور انسٹینس بنائیں** - سرور کی صلاحیتوں کے ساتھ وضاحت کریں۔
3. **ٹولز کی وضاحت کریں** - وہ فعالیت شامل کریں جو ہم ظاہر کرنا چاہتے ہیں۔
4. **ٹرانسپورٹ سیٹ اپ کریں** - stdio مواصلت کو کنفیگر کریں۔
5. **سرور چلائیں** - سرور شروع کریں اور پیغامات ہینڈل کریں۔

آئیے اسے مرحلہ وار بنائیں:

### مرحلہ 1: ایک بنیادی stdio سرور بنائیں

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

### مرحلہ 2: مزید ٹولز شامل کریں

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

### مرحلہ 3: سرور چلانا

کوڈ کو `server.py` کے طور پر محفوظ کریں اور کمانڈ لائن سے چلائیں:

```bash
python server.py
```

سرور شروع ہوگا اور stdin سے ان پٹ کا انتظار کرے گا۔ یہ stdio ٹرانسپورٹ کے ذریعے JSON-RPC پیغامات کے ساتھ بات چیت کرتا ہے۔

### مرحلہ 4: انسپیکٹر کے ساتھ ٹیسٹنگ

آپ اپنے سرور کو ایم سی پی انسپیکٹر کے ذریعے ٹیسٹ کر سکتے ہیں:

1. انسپیکٹر انسٹال کریں: `npx @modelcontextprotocol/inspector`
2. انسپیکٹر چلائیں اور اپنے سرور کی طرف اشارہ کریں۔
3. وہ ٹولز ٹیسٹ کریں جو آپ نے بنائے ہیں۔

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## اپنے stdio سرور کو ڈیبگ کرنا

### ایم سی پی انسپیکٹر کا استعمال

ایم سی پی انسپیکٹر ایم سی پی سرورز کو ڈیبگ اور ٹیسٹ کرنے کے لیے ایک قیمتی ٹول ہے۔ اپنے stdio سرور کے ساتھ اسے استعمال کرنے کا طریقہ یہ ہے:

1. **انسپیکٹر انسٹال کریں**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **انسپیکٹر چلائیں**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **اپنے سرور کو ٹیسٹ کریں**: انسپیکٹر ایک ویب انٹرفیس فراہم کرتا ہے جہاں آپ:
   - سرور کی صلاحیتیں دیکھ سکتے ہیں۔
   - مختلف پیرامیٹرز کے ساتھ ٹولز ٹیسٹ کر سکتے ہیں۔
   - JSON-RPC پیغامات کی نگرانی کر سکتے ہیں۔
   - کنکشن کے مسائل کو ڈیبگ کر سکتے ہیں۔

### ویژول اسٹوڈیو کوڈ کا استعمال

آپ اپنے ایم سی پی سرور کو براہ راست ویژول اسٹوڈیو کوڈ میں بھی ڈیبگ کر سکتے ہیں:

1. `.vscode/launch.json` میں لانچ کنفیگریشن بنائیں:
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

2. اپنے سرور کوڈ میں بریک پوائنٹس سیٹ کریں۔
3. ڈیبگر چلائیں اور انسپیکٹر کے ساتھ ٹیسٹ کریں۔

### عام ڈیبگنگ تجاویز

- لاگنگ کے لیے `stderr` کا استعمال کریں - کبھی بھی `stdout` پر نہ لکھیں کیونکہ یہ ایم سی پی پیغامات کے لیے مخصوص ہے۔
- یقینی بنائیں کہ تمام JSON-RPC پیغامات نئی لائن سے الگ کیے گئے ہیں۔
- پہلے سادہ ٹولز کے ساتھ ٹیسٹ کریں، پھر پیچیدہ فعالیت شامل کریں۔
- پیغام کی شکلوں کی تصدیق کے لیے انسپیکٹر کا استعمال کریں۔

## ویژول اسٹوڈیو کوڈ میں اپنے stdio سرور کو استعمال کرنا

جب آپ اپنا ایم سی پی stdio سرور بنا لیں، تو آپ اسے ویژول اسٹوڈیو کوڈ کے ساتھ انٹیگریٹ کر سکتے ہیں تاکہ اسے Claude یا دیگر ایم سی پی-کمپیٹیبل کلائنٹس کے ساتھ استعمال کیا جا سکے۔

### کنفیگریشن

1. **ایم سی پی کنفیگریشن فائل بنائیں** `%APPDATA%\Claude\claude_desktop_config.json` (ونڈوز) یا `~/Library/Application Support/Claude/claude_desktop_config.json` (میک) پر:

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

2. **Claude کو دوبارہ شروع کریں**: Claude کو بند کریں اور دوبارہ کھولیں تاکہ نیا سرور کنفیگریشن لوڈ ہو سکے۔

3. **کنکشن ٹیسٹ کریں**: Claude کے ساتھ گفتگو شروع کریں اور اپنے سرور کے ٹولز کو آزمانے کی کوشش کریں:
   - "کیا آپ مجھے گریٹنگ ٹول کے ذریعے سلام کر سکتے ہیں؟"
   - "15 اور 27 کا مجموعہ کیا ہے؟"
   - "سرور کی معلومات کیا ہیں؟"

### ٹائپ اسکرپٹ stdio سرور مثال

یہاں ایک مکمل ٹائپ اسکرپٹ مثال ہے حوالہ کے لیے:

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

### .NET stdio سرور مثال

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

## خلاصہ

اس اپڈیٹ شدہ سبق میں، آپ نے سیکھا کہ:

- موجودہ **stdio ٹرانسپورٹ** (تجویز کردہ طریقہ) کا استعمال کرتے ہوئے ایم سی پی سرورز بنائیں۔
- سمجھیں کہ ایس ایس ای ٹرانسپورٹ کو stdio اور اسٹریمیبل HTTP کے حق میں کیوں منسوخ کیا گیا۔
- ایسے ٹولز بنائیں جنہیں ایم سی پی کلائنٹس کال کر سکیں۔
- ایم سی پی انسپیکٹر کا استعمال کرتے ہوئے اپنے سرور کو ڈیبگ کریں۔
- اپنے stdio سرور کو ویژول اسٹوڈیو کوڈ اور Claude کے ساتھ انٹیگریٹ کریں۔

stdio ٹرانسپورٹ منسوخ شدہ ایس ایس ای طریقہ کے مقابلے میں ایم سی پی سرورز بنانے کا ایک سادہ، زیادہ محفوظ، اور زیادہ مؤثر طریقہ فراہم کرتا ہے۔ یہ 2025-06-18 اسپیسفیکیشن کے مطابق زیادہ تر ایم سی پی سرور امپلیمنٹیشنز کے لیے تجویز کردہ ٹرانسپورٹ ہے۔

### .NET

1. پہلے کچھ ٹولز بنائیں، اس کے لیے ہم ایک فائل *Tools.cs* بنائیں گے جس میں درج ذیل مواد ہوگا:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## مشق: اپنے stdio سرور کو ٹیسٹ کرنا

اب جب کہ آپ نے اپنا stdio سرور بنا لیا ہے، آئیے اسے ٹیسٹ کریں تاکہ یہ یقینی بنایا جا سکے کہ یہ صحیح طریقے سے کام کر رہا ہے۔

### ضروریات

1. یقینی بنائیں کہ آپ کے پاس ایم سی پی انسپیکٹر انسٹال ہے:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. آپ کا سرور کوڈ محفوظ ہونا چاہیے (مثلاً، `server.py` کے طور پر)

### انسپیکٹر کے ساتھ ٹیسٹنگ

1. **اپنے سرور کے ساتھ انسپیکٹر شروع کریں**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ویب انٹرفیس کھولیں**: انسپیکٹر ایک براؤزر ونڈو کھولے گا جو آپ کے سرور کی صلاحیتیں دکھائے گا۔

3. **ٹولز ٹیسٹ کریں**: 
   - مختلف ناموں کے ساتھ `get_greeting` ٹول آزمائیں۔
   - مختلف نمبروں کے ساتھ `calculate_sum` ٹول آزمائیں۔
   - سرور میٹا ڈیٹا دیکھنے کے لیے `get_server_info` ٹول کال کریں۔

4. **مواصلت کی نگرانی کریں**: انسپیکٹر کلائنٹ اور سرور کے درمیان تبادلہ کیے جانے والے JSON-RPC پیغامات دکھاتا ہے۔

### آپ کو کیا دیکھنا چاہیے

جب آپ کا سرور صحیح طریقے سے شروع ہوتا ہے، تو آپ کو دیکھنا چاہیے:
- انسپیکٹر میں سرور کی صلاحیتیں درج ہیں۔
- ٹیسٹنگ کے لیے دستیاب ٹولز۔
- کامیاب JSON-RPC پیغام کے تبادلے۔
- انٹرفیس میں ٹول کے جوابات دکھائے گئے۔

### عام مسائل اور حل

**سرور شروع نہیں ہو رہا:**
- چیک کریں کہ تمام ڈپینڈنسیز انسٹال ہیں: `pip install mcp`
- پائتھون کی نحو اور انڈینٹیشن کی تصدیق کریں۔
- کنسول میں ایرر میسیجز دیکھیں۔

**ٹولز ظاہر نہیں ہو رہے:**
- یقینی بنائیں کہ `@server.tool()` ڈیکوریٹرز موجود ہیں۔
- چیک کریں کہ ٹول فنکشنز `main()` سے پہلے بیان کیے گئے ہیں۔
- تصدیق کریں کہ سرور صحیح طریقے سے کنفیگر کیا گیا ہے۔

**کنکشن کے مسائل:**
- یقینی بنائیں کہ سرور stdio ٹرانسپورٹ کو صحیح طریقے سے استعمال کر رہا ہے۔
- چیک کریں کہ کوئی اور پروسیس مداخلت نہیں کر رہا۔
- انسپیکٹر کمانڈ نحو کی تصدیق کریں۔

## اسائنمنٹ

اپنے سرور کو مزید صلاحیتوں کے ساتھ بنانے کی کوشش کریں۔ [اس صفحے](https://api.chucknorris.io/) کو دیکھیں تاکہ، مثال کے طور پر، ایک ٹول شامل کریں جو ایک API کو کال کرتا ہے۔ آپ فیصلہ کریں کہ سرور کیسا ہونا چاہیے۔ مزے کریں :)

## حل

[حل](./solution/README.md) یہاں ایک ممکنہ حل ہے جس میں کام کرنے والا کوڈ شامل ہے۔

## اہم نکات

اس باب کے اہم نکات درج ذیل ہیں:

- stdio ٹرانسپورٹ مقامی ایم سی پی سرورز کے لیے تجویز کردہ میکانزم ہے۔
- stdio ٹرانسپورٹ ایم سی پی سرورز اور کلائنٹس کے درمیان اسٹینڈرڈ ان پٹ اور آؤٹ پٹ اسٹریمز کا استعمال کرتے ہوئے آسان مواصلت کی اجازت دیتا ہے۔
- آپ انسپیکٹر اور ویژول اسٹوڈیو کوڈ دونوں کا استعمال کرتے ہوئے stdio سرورز کو براہ راست استعمال کر سکتے ہیں، جس سے ڈیبگنگ اور انٹیگریشن آسان ہو جاتا ہے۔

## نمونے 

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھون کیلکولیٹر](../../../../03-GettingStarted/samples/python) 

## اضافی وسائل

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## آگے کیا ہے

## اگلے مراحل

اب جب کہ آپ نے stdio ٹرانسپورٹ کے ساتھ ایم سی پی سرورز بنانے کا طریقہ سیکھ لیا ہے، آپ مزید جدید موضوعات کو دریافت کر سکتے ہیں:

- **اگلا**: [ایچ ٹی ٹی پی اسٹریمنگ کے ساتھ ایم سی پی (اسٹریمیبل HTTP)](../06-http-streaming/README.md) - دور دراز سرورز کے لیے دوسرے معاون ٹرانسپورٹ میکانزم کے بارے میں جانیں۔
- **جدید**: [ایم سی پی سیکیورٹی کے بہترین طریقے](../../02-Security/README.md) - اپنے ایم سی پی سرورز میں سیکیورٹی نافذ کریں۔
- **پروڈکشن**: [ڈپلائمنٹ کی حکمت عملی](../09-deployment/README.md) - اپنے سرورز کو پروڈکشن کے لیے ڈپلائے کریں۔

## اضافی وسائل

- [ایم سی پی اسپیسفیکیشن 2025-06-18](https

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔