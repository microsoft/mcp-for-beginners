# MCP سرور stdio ٹرانسپورٹ کے ساتھ

> **⚠️ اہم اپ ڈیٹ**: MCP وضاحت 2025-06-18 کے مطابق، اسٹینڈ اکی SSE (سرور-سینٹ ایونٹس) ٹرانسپورٹ کو **ختم** کر دیا گیا ہے اور "Streamable HTTP" ٹرانسپورٹ نے اس کی جگہ لے لی ہے۔ موجودہ MCP وضاحت دو اہم ٹرانسپورٹ میکانزمز کی وضاحت کرتی ہے:
> 1. **stdio** - معیاری ان پٹ/آؤٹ پٹ (مقامی سرورز کے لیے سفارش کی گئی)
> 2. **Streamable HTTP** - دور دراز کے سرورز کے لیے جو داخلی طور پر SSE استعمال کر سکتے ہیں
>
> اس سبق کو اپ ڈیٹ کیا گیا ہے تاکہ اس پر توجہ دی جائے **stdio ٹرانسپورٹ** پر، جو زیادہ تر MCP سرور کی تنصیبات کے لیے تجویز کردہ طریقہ ہے۔

stdio ٹرانسپورٹ MCP سرورز کو معیاری ان پٹ اور آؤٹ پٹ ذرائع کے ذریعے کلائنٹس کے ساتھ بات چیت کرنے کی اجازت دیتا ہے۔ یہ موجودہ MCP وضاحت میں سب سے زیادہ استعمال شدہ اور تجویز کردہ ٹرانسپورٹ میکانزم ہے، جو MCP سرورز بنانے کا ایک آسان اور مؤثر طریقہ فراہم کرتا ہے جو مختلف کلائنٹ ایپلیکیشنز کے ساتھ آسانی سے ضم کیے جا سکتے ہیں۔

## جائزہ

یہ سبق MCP سرورز کو stdio ٹرانسپورٹ کے ذریعے بنانے اور استعمال کرنے کا احاطہ کرتا ہے۔

## سیکھنے کے اہداف

اس سبق کے آخر تک، آپ قابل ہوں گے:

- stdio ٹرانسپورٹ کا استعمال کرتے ہوئے MCP سرور بنانا۔
- انسپکٹر کا استعمال کر کے MCP سرور کی ڈیبگنگ کرنا۔
- Visual Studio Code میں MCP سرور کو استعمال کرنا۔
- موجودہ MCP ٹرانسپورٹ میکانزمز کو سمجھنا اور یہ جاننا کہ stdio کیوں تجویز کیا گیا ہے۔

## stdio ٹرانسپورٹ - یہ کیسے کام کرتا ہے

stdio ٹرانسپورٹ موجودہ MCP وضاحت (2025-06-18) میں دو سپورٹ شدہ ٹرانسپورٹ اقسام میں سے ایک ہے۔ یہ اس طرح کام کرتا ہے:

- **سادہ کمیونیکیشن**: سرور JSON-RPC پیغامات کو معیاری ان پٹ (`stdin`) سے پڑھتا ہے اور معیاری آؤٹ پٹ (`stdout`) پر پیغامات بھیجتا ہے۔
- **پروسس بیسڈ**: کلائنٹ MCP سرور کو بطور subprocess لانچ کرتا ہے۔
- **پیغام فارمیٹ**: پیغامات الگ الگ JSON-RPC درخواستیں، اطلاعات، یا جوابات ہوتے ہیں جنہیں نئی لائنز سے الگ کیا جاتا ہے۔
- **لاگنگ**: سرور UTF-8 سٹرنگز کو معیاری ایرر (`stderr`) پر لاگنگ کے لیے لکھ سکتا ہے۔

### کلیدی ضروریات:
- پیغامات نئی لائنز سے الگ ہونے چاہئیں اور ان میں ایمبیڈڈ نئی لائن نہیں ہونی چاہیے۔
- سرور کو `stdout` پر کوئی چیز لکھنے کی اجازت نہیں جو ایک قابل قبول MCP پیغام نہ ہو۔
- کلائنٹ سرور کے `stdin` پر ایسی کوئی چیز نہیں لکھے جو ایک قابل قبول MCP پیغام نہ ہو۔

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

گزشتہ کوڈ میں:

- ہم MCP SDK سے `Server` کلاس اور `StdioServerTransport` کو امپورٹ کرتے ہیں
- ہم بنیادی کنفیگریشن اور صلاحیتوں کے ساتھ ایک سرور انسٹینس بناتے ہیں

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# سرور کا نمونہ بنائیں
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

گزشتہ کوڈ میں ہم نے:

- MCP SDK استعمال کرتے ہوئے سرور انسٹینس بنایا ہے
- ڈیکوریٹرز کے ذریعے ٹولز کی تعریف کی ہے
- stdio_server کنٹیکسٹ منیجر استعمال کیا ہے تاکہ ٹرانسپورٹ کو ہینڈل کیا جا سکے

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

SSE سے اہم فرق یہ ہے کہ stdio سرورز:

- ویب سرور سیٹ اپ یا HTTP اینڈ پوائنٹس کی ضرورت نہیں رکھتے
- کلائنٹ کے ذریعے subprocess کے طور پر لانچ ہوتے ہیں
- stdin/stdout اسٹریمز کے ذریعے بات چیت کرتے ہیں
- نفاذ اور ڈیبگنگ میں آسان ہیں

## مشق: stdio سرور بنانا

اپنا سرور بنانے کے لیے ہمیں دو باتوں کا خیال رکھنا ہوگا:

- ہمیں endpoints کو کنکشن اور پیغامات کے لیے ظاہر کرنے کے لیے ویب سرور استعمال کرنا ہوتا ہے۔

## لیب: ایک سادہ MCP stdio سرور بنانا

اس لیب میں، ہم ایک سادہ MCP سرور بنائیں گے جو سفارش شدہ stdio ٹرانسپورٹ استعمال کرتا ہے۔ یہ سرور ٹولز کو ظاہر کرے گا جنہیں کلائنٹس Model Context Protocol کے ذریعے کال کر سکتے ہیں۔

### ضروریات

- Python 3.8 یا بعد کا ورژن
- MCP Python SDK: `pip install mcp`
- Async پروگرامنگ کی بنیادی سمجھ

آئیے اپنا پہلا MCP stdio سرور بنانا شروع کرتے ہیں:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# لاگنگ کو ترتیب دیں
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# سرور بنائیں
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
    # stdio ٹرانسپورٹ استعمال کریں
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


## ختم شدہ SSE طریقہ سے اہم فرق

**Stdio ٹرانسپورٹ (موجودہ معیار):**
- آسان subprocess ماڈل - کلائنٹ سرور کو ہمارے بچے کے پراسیس کے طور پر لانچ کرتا ہے
- stdin/stdout کے ذریعے JSON-RPC پیغامات کے تبادلے کی کمیونیکیشن
- HTTP سرور سیٹ اپ کی ضرورت نہیں
- بہتر کارکردگی اور سیکیورٹی
- آسان ڈیبگنگ اور ڈیولپمنٹ

**SSE ٹرانسپورٹ (MCP 2025-06-18 سے ختم شدہ):**
- SSE اینڈ پوائنٹس والے HTTP سرور کی ضرورت تھی
- ویب سرور کی انفراسٹرکچر کے ساتھ زیادہ پیچیدہ سیٹ اپ
- HTTP اینڈ پوائنٹس کے لیے اضافی سیکیورٹی غور و فکر
- اب اس کی جگہ Streamable HTTP نے لے لی ہے جو ویب پر مبنی صورتوں کے لیے ہے

### stdio ٹرانسپورٹ کے ساتھ سرور بنانا

stdio سرور بنانے کے لیے ہمیں:

1. **ضروری لائبریریاں امپورٹ کریں** - MCP سرور جز اور stdio ٹرانسپورٹ کی ضرورت ہے
2. **سرور انسٹینس بنائیں** - سرور کو اس کی صلاحیتوں کے ساتھ وضع کریں
3. **ٹولز کی تعریف کریں** - وہ فنکشنز شامل کریں جو آپ ظاہر کرنا چاہتے ہیں
4. **ٹرانسپورٹ سیٹ اپ کریں** - stdio کمیونیکیشن کی ترتیب دیں
5. **سرور چلائیں** - سرور شروع کریں اور پیغامات سنبھالیں

آئیے اسے مرحلہ وار بنائیں:

### مرحلہ 1: ایک بنیادی stdio سرور بنائیں

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# لاگنگ کو ترتیب دیں
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# سرور بنائیں
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

سرور شروع ہو جائے گا اور stdin سے ان پٹ کے انتظار میں رہے گا۔ یہ stdio ٹرانسپورٹ کے ذریعے JSON-RPC پیغامات استعمال کرتے ہوئے کمیونیکیشن کرتا ہے۔

### مرحلہ 4: انسپکٹر کے ساتھ ٹیسٹنگ

آپ MCP انسپکٹر استعمال کر کے اپنے سرور کی جانچ کر سکتے ہیں:

1. انسپکٹر انسٹال کریں: `npx @modelcontextprotocol/inspector`
2. انسپکٹر چلائیں اور اپنے سرور کی طرف پوائنٹ کریں
3. بنائے گئے ٹولز کی جانچ کریں

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## اپنی stdio سرور کی ڈیبگنگ

### MCP انسپکٹر کا استعمال

MCP انسپکٹر MCP سرورز کی ڈیبگنگ اور ٹیسٹنگ کے لیے ایک قیمتی آلہ ہے۔ یہاں دی گئی طریقہ stdio سرور کے ساتھ اسے استعمال کرنے کا عمل ہے:

1. **انسپکٹر انسٹال کریں**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **انسپکٹر چلائیں**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **اپنے سرور کی جانچ کریں**: انسپکٹر ایک ویب انٹرفیس فراہم کرتا ہے جہاں آپ:
   - سرور کی صلاحیتیں دیکھ سکتے ہیں
   - مختلف پیرامیٹرز کے ساتھ ٹولز کی جانچ کر سکتے ہیں
   - JSON-RPC پیغامات کی نگرانی کر سکتے ہیں
   - کنکشن کے مسائل ڈیبگ کر سکتے ہیں

### VS Code کا استعمال

آپ اپنے MCP سرور کو براہ راست VS Code میں بھی ڈیبگ کر سکتے ہیں:

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

2. اپنے سرور کوڈ میں بریک پوائنٹس سیٹ کریں
3. ڈیبگر چلائیں اور انسپکٹر کے ساتھ ٹیسٹ کریں

### عام ڈیبگنگ نکات

- لاگنگ کے لیے `stderr` استعمال کریں — `stdout` پر کبھی کچھ نہ لکھیں کیونکہ یہ MCP پیغامات کے لیے مخصوص ہے
- یقینی بنائیں کہ تمام JSON-RPC پیغامات نئی لائن سے جدا ہیں
- پہلے آسان ٹولز کے ساتھ ٹیسٹ کریں اس سے پہلے کہ پیچیدہ فنکشنالیٹی شامل کریں
- پیغام فارمیٹس کی تصدیق کے لیے انسپکٹر استعمال کریں

## VS Code میں اپنی stdio سرور کا استعمال

جب آپ نے MCP stdio سرور بنا لیا، تو آپ اسے VS Code کے ساتھ انضمام کر کے Claude یا دیگر MCP-مطابقت رکھنے والے کلائنٹس کے ساتھ استعمال کر سکتے ہیں۔

### کنفیگریشن

1. **ایک MCP کنفیگریشن فائل بنائیں** `%APPDATA%\Claude\claude_desktop_config.json` (ونڈوز) یا `~/Library/Application Support/Claude/claude_desktop_config.json` (میک) پر:

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

2. **Claude کو ری سٹارٹ کریں**: Claude کو بند کر کے دوبارہ کھولیں تاکہ نیا سرور کنفیگریشن لوڈ ہو سکے۔

3. **کنکشن ٹیسٹ کریں**: Claude کے ساتھ گفتگو شروع کریں اور اپنے سرور کے ٹولز استعمال کریں:
   - "کیا آپ مجھے greeting tool استعمال کرتے ہوئے سلام کر سکتے ہیں؟"
   - "15 اور 27 کا مجموعہ نکالیں"
   - "سرور کی معلومات کیا ہے؟"

### TypeScript stdio سرور کی مثال

یہاں حوالہ کے لیے مکمل TypeScript مثال ہے:

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

// آلات شامل کریں
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

### .NET stdio سرور کی مثال

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


## خلاصہ

اس اپ ڈیٹ شدہ سبق میں، آپ نے سیکھا کہ:

- موجودہ **stdio ٹرانسپورٹ** (تجویز کردہ طریقہ) استعمال کر کے MCP سرورز کیسے بنائیں
- SSE ٹرانسپورٹ کو کیوں ختم کیا گیا اور stdio و Streamable HTTP کو ترجیح دی گئی
- ایسے ٹولز بنائیں جنہیں MCP کلائنٹس کال کر سکیں
- MCP انسپکٹر کے ذریعے اپنے سرور کی ڈیبگنگ کریں
- VS Code اور Claude کے ساتھ اپنے stdio سرور کو انٹیگریٹ کریں

stdio ٹرانسپورٹ ایک سادہ، زیادہ محفوظ اور زیادہ کارکردگی والا طریقہ فراہم کرتا ہے MCP سرورز بنانے کے لیے، جو ختم شدہ SSE طریقہ سے بہتر ہے۔ یہ 2025-06-18 کی وضاحت کے مطابق زیادہ تر MCP سرور تنصیبات کے لیے تجویز کردہ ٹرانسپورٹ ہے۔

### .NET

1. آئیے پہلے کچھ ٹولز بناتے ہیں، اس کے لیے ہم ایک فائل *Tools.cs* بنائیں گے جس میں درج ذیل مواد ہو گا:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## مشق: اپنی stdio سرور کی جانچ

اب جب آپ نے اپنا stdio سرور بنا لیا ہے، تو اسے جانچتے ہیں تاکہ یہ یقینی بنایا جا سکے کہ یہ صحیح کام کر رہا ہے۔

### ضروریات

1. یقینی بنائیں کہ MCP انسپکٹر انسٹال کیا ہوا ہے:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. آپ کا سرور کوڈ محفوظ ہو (مثلاً `server.py` کے طور پر)

### انسپکٹر کے ساتھ جانچ

1. **اپنے سرور کے ساتھ انسپکٹر شروع کریں**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ویب انٹرفیس کھولیں**: انسپکٹر ایک براؤزر ونڈو کھولے گا جو آپ کے سرور کی صلاحیتیں دکھائے گا۔

3. **ٹولز کی جانچ کریں**: 
   - مختلف ناموں کے ساتھ `get_greeting` ٹول آزمائیں
   - مختلف نمبروں کے ساتھ `calculate_sum` ٹول ٹیسٹ کریں
   - `get_server_info` ٹول کال کریں تاکہ سرور کے میٹا ڈیٹا کو دیکھ سکیں

4. **کمیونیکیشن کی نگرانی کریں**: انسپکٹر دکھاتا ہے کہ JSON-RPC پیغامات کلائنٹ اور سرور کے درمیان کیسے تبادلہ ہو رہے ہیں۔

### آپ کو کیا دیکھنا چاہیے

جب آپ کا سرور صحیح سے شروع ہو جائے گا تو آپ کو یہ چیزیں نظر آئیں گی:
- انسپکٹر میں سرور کی صلاحیتیں درج ہوں گی
- ٹولز ٹیسٹنگ کے لیے دستیاب ہوں گے
- JSON-RPC پیغامات کا کامیاب تبادلہ ہوگا
- انٹرفیس میں ٹول کے جوابات دکھائے جائیں گے

### عام مسائل اور حل

**سرور شروع نہیں ہوتا:**
- چیک کریں کہ تمام dependencies انسٹال ہیں: `pip install mcp`
- Python syntax اور indentation کو درست کریں
- کنسول میں ایرر میسجز دیکھیں

**ٹولز نظر نہیں آ رہے:**
- یقینی بنائیں کہ `@server.tool()` ڈیکوریٹرز موجود ہیں
- چیک کریں کہ ٹول فنکشنز `main()` سے پہلے ڈیفائن کیے گئے ہیں
- سرور کی صحیح کنفیگریشن کو یقینی بنائیں

**کنکشن کے مسائل:**
- یقینی بنائیں کہ سرور stdio ٹرانسپورٹ کو صحیح استعمال کر رہا ہے
- چیک کریں کہ کوئی اور پراسیس مداخلت نہیں کر رہا
- انسپکٹر کمانڈ کی ترکیب درست ہے

## اسائنمنٹ

اپنے سرور کو مزید صلاحیتوں کے ساتھ بنانا آزمائیں۔ مثال کے طور پر [اس صفحے](https://api.chucknorris.io/) کو دیکھیں، جہاں آپ ایک ایسا ٹول شامل کر سکتے ہیں جو API کو کال کرتا ہو۔ آپ فیصلہ کریں کہ سرور کیسا دکھنا چاہیے۔ مزہ کریں :)

## حل

[حل](./solution/README.md) یہاں ایک ممکنہ حل دیا گیا ہے جس میں مکمل کام کرنے والا کوڈ ہے۔

## اہم نکات

اس باب سے اہم نکات درج ذیل ہیں:

- stdio ٹرانسپورٹ مقامی MCP سرورز کے لیے تجویز کردہ میکانزم ہے۔
- stdio ٹرانسپورٹ MCP سرورز اور کلائنٹس کے درمیان معیاری ان پٹ اور آؤٹ پٹ اسٹریمز کا استعمال کرتے ہوئے آسان کمیونیکیشن کی اجازت دیتا ہے۔
- آپ دونوں انسپکٹر اور Visual Studio Code کا استعمال کرتے ہوئے stdio سرورز کو براہ راست استعمال کر سکتے ہیں، جو ڈیبگنگ اور انضمام کو آسان بناتا ہے۔

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوااسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھون کیلکولیٹر](../../../../03-GettingStarted/samples/python)

## اضافی وسائل

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## اگلا کیا ہے

## اگلے اقدامات

اب جب آپ نے stdio ٹرانسپورٹ کے ساتھ MCP سرورز بنانا سیکھ لیا ہے، تو آپ مزید پیچیدہ موضوعات پر جا سکتے ہیں:

- **اگلا:** [MCP کے ساتھ HTTP اسٹریمنگ (Streamable HTTP)](../06-http-streaming/README.md) - دور دراز سرورز کے لیے دوسرے سپورٹ شدہ ٹرانسپورٹ کے بارے میں جانیں
- **ترقی یافتہ:** [MCP سیکیورٹی بہترین عمل](../../02-Security/README.md) - اپنے MCP سرورز میں سیکیورٹی نافذ کریں
- **پروڈکشن:** [تنصیبی حکمت عملیاں](../09-deployment/README.md) - اپنے سرورز کو پروڈکشن میں نافذ کریں

## اضافی وسائل

- [MCP وضاحت 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - سرکاری وضاحت
- [MCP SDK دستاویزات](https://github.com/modelcontextprotocol/sdk) - تمام زبانوں کے لیے SDK حوالہ جات
- [کمیونٹی مثالیں](../../06-CommunityContributions/README.md) - کمیونٹی کی طرف سے مزید سرور کی مثالیں

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تاریخی دستبرداری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم صحت ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں مستند ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا ناانصافی کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->