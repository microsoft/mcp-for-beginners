# MCP سرور stdio ٹرانسپورٹ کے ساتھ

> **⚠️ اہم اپ ڈیٹ**: MCP وضاحت 2025-06-18 کے مطابق، اسٹینڈ اکی SSE (سرور-سینٹ ایونٹس) ٹرانسپورٹ کو **قبول نہیں کیا گیا** اور اسے "اسٹریمیبل HTTP" ٹرانسپورٹ سے بدل دیا گیا ہے۔ موجودہ MCP وضاحت دو بنیادی ٹرانسپورٹ طریقے متعین کرتی ہے:
> 1. **stdio** - معیاری ان پٹ/آؤٹ پٹ (مقامی سرورز کے لیے سفارش کی گئی)
> 2. **اسٹریمیبل HTTP** - دور دراز کے سرورز کے لیے جو داخلی طور پر SSE استعمال کر سکتے ہیں
>
> اس سبق کو اپ ڈیٹ کیا گیا ہے تاکہ وہ **stdio ٹرانسپورٹ** پر مرکوز ہو، جو زیادہ تر MCP سرور امپلیمینٹیشنز کے لیے سفارش کردہ طریقہ ہے۔

stdio ٹرانسپورٹ MCP سرورز کو کلائنٹس کے ساتھ معیاری ان پٹ اور آؤٹ پٹ اسٹریمز کے ذریعے بات چیت کرنے کی اجازت دیتا ہے۔ یہ موجودہ MCP وضاحت میں سب سے زیادہ استعمال ہونے والا اور سفارش کردہ ٹرانسپورٹ میکانزم ہے، جو آسان اور مؤثر طریقہ فراہم کرتا ہے تاکہ MCP سرورز بنائے جا سکیں جو مختلف کلائنٹ ایپلیکیشنز کے ساتھ آسانی سے ضم ہو سکیں۔

## جائزہ

یہ سبق stdio ٹرانسپورٹ استعمال کرتے ہوئے MCP سرورز بنانے اور استعمال کرنے کا طریقہ بیان کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے آخر تک، آپ کر سکیں گے:

- stdio ٹرانسپورٹ استعمال کرتے ہوئے MCP سرور بنانا۔
- انسپیکٹر استعمال کرتے ہوئے MCP سرور کو ڈیبگ کرنا۔
- Visual Studio Code استعمال کرتے ہوئے MCP سرور کو استعمال کرنا۔
- موجودہ MCP ٹرانسپورٹ طریقوں کو سمجھنا اور stdio کی سفارش کی وجوہات جاننا۔

## stdio ٹرانسپورٹ - یہ کیسے کام کرتا ہے

stdio ٹرانسپورٹ دو سپورٹ شدہ ٹرانسپورٹ اقسام میں سے ایک ہے جو موجودہ MCP وضاحت (2025-06-18) میں شامل ہے۔ یہ اس طرح کام کرتا ہے:

- **سادہ بات چیت**: سرور معیاری ان پٹ (`stdin`) سے JSON-RPC پیغامات پڑھتا ہے اور معیاری آؤٹ پٹ (`stdout`) پر پیغامات بھیجتا ہے۔
- **عمل پر مبنی**: کلائنٹ MCP سرور کو بطور سب پروسیس لانچ کرتا ہے۔
- **پیغام فارمیٹ**: پیغامات الگ الگ JSON-RPC درخواستیں، اطلاعات، یا جوابات ہوتے ہیں، جو نئی لائنز سے جدا ہوتے ہیں۔
- **لاگنگ**: سرور لاگنگ کے لیے معیاری ایرر (`stderr`) پر UTF-8 سٹرنگ لکھ سکتا ہے۔

### اہم ضروریات:
- پیغامات نئی لائنز سے جدا کرنے چاہیے اور ان میں ایمبیڈڈ نئی لائنز نہیں ہونی چاہئیں۔
- سرور `stdout` پر صرف قابل قبول MCP پیغامات لکھے، کوئی غیر متعلقہ مواد نہیں۔
- کلائنٹ سرور کے `stdin` پر صرف قابل قبول MCP پیغامات لکھے۔

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

درج بالا کوڈ میں:

- ہم MCP SDK سے `Server` کلاس اور `StdioServerTransport` درآمد کرتے ہیں۔
- بنیادی کنفیگریشن اور صلاحیتوں کے ساتھ ایک سرور انстанس تخلیق کرتے ہیں۔
- `StdioServerTransport` انستانس بناتے ہیں اور سرور کو اس سے جوڑتے ہیں، تاکہ stdin/stdout کے ذریعے بات چیت ہو سکے۔

### پائتھن

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# سرور کا مثالی تخلیق کریں
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

درج بالا کوڈ میں ہم:

- MCP SDK استعمال کرتے ہوئے سرور انستانس بناتے ہیں۔
- ڈیکوریٹرز کے ذریعے ٹولز کی تعریف کرتے ہیں۔
- stdio_server کانٹیکسٹ مینیجر استعمال کرکے ٹرانسپورٹ کو ہینڈل کرتے ہیں۔

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

- ویب سرور سیٹ اپ یا HTTP اینڈ پوائنٹس کے بغیر چلتے ہیں۔
- کلائنٹ کے ذریعہ سب پروسیس کے طور پر لانچ ہوتے ہیں۔
- stdin/stdout اسٹریمز کے ذریعے بات چیت کرتے ہیں۔
- آسانی سے امپلیمینٹ اور ڈیبگ کیے جا سکتے ہیں۔

## مشق: stdio سرور بنانا

اپنا سرور بنانے کے لیے، ہمیں دو باتیں ذہن میں رکھنی ہوں گی:

- ہمیں کنکشن اور پیغامات کے اینڈ پوائنٹس ظاہر کرنے کے لیے ویب سرور استعمال کرنے کی ضرورت ہے۔

## لیب: ایک سادہ MCP stdio سرور بنانا

اس لیب میں، ہم سفارش شدہ stdio ٹرانسپورٹ استعمال کرتے ہوئے ایک سادہ MCP سرور بنائیں گے۔ یہ سرور وہ ٹولز ظاہر کرے گا جنہیں کلائنٹس معیاری ماڈل کانٹیکسٹ پروٹوکول کے ذریعے کال کر سکیں گے۔

### ضروریات

- پائتھن 3.8 یا بعد کا ورژن
- MCP پائتھان SDK: `pip install mcp`
- ایسینک پروگرامنگ کی بنیادی سمجھ

چلیں اپنا پہلا MCP stdio سرور بناتے ہیں:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# لاگنگ ترتیب دیں
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

## منسوخ شدہ SSE طریقہ سے اہم فرق

**Stdio ٹرانسپورٹ (موجودہ معیار):**
- سادہ سب پروسیس ماڈل - کلائنٹ سرور کو چائلڈ پروسیس کے طور پر لانچ کرتا ہے۔
- JSON-RPC پیغامات کے ذریعے stdin/stdout سے بات چیت۔
- HTTP سرور سیٹ اپ کی ضرورت نہیں۔
- بہتر کارکردگی اور سیکورٹی۔
- آسان ڈیبگنگ اور ترقی۔

**SSE ٹرانسپورٹ (MCP 2025-06-18 سے منسوخ):**
- SSE اینڈ پوائنٹس والے HTTP سرور کی ضرورت تھی۔
- ویب سرور انفراسٹرکچر کے ساتھ زیادہ پیچیدہ سیٹ اپ۔
- HTTP اینڈ پوائنٹس کے لیے اضافی حفاظتی تدابیر۔
- اب ویب بیسڈ استعمال کے لیے Streamable HTTP سے تبدیل کر دیا گیا ہے۔

### stdio ٹرانسپورٹ سے سرور بنانا

stdio سرور بنانے کے لیے ہمیں:

1. **ضروری لائبریریز امپورٹ کریں** - MCP سرور کے اجزاء اور stdio ٹرانسپورٹ
2. **سرور انستانس بنائیں** - صلاحیتوں کے ساتھ سرور کو تعریف کریں
3. **ٹولز ڈیفائن کریں** - وہ فنکشنز شامل کریں جو ظاہر کرنا چاہتے ہیں
4. **ٹرانسپورٹ سیٹ اپ کریں** - stdio کمیونیکیشن کی ترتیب دیں
5. **سرور چلائیں** - سرور شروع کریں اور پیغامات ہینڈل کریں

آئیے اسے مرحلہ وار بنائیں:

### مرحلہ 1: ایک بنیادی stdio سرور بنائیں

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# لاگنگ کو تشکیل دیں
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

سرور شروع ہوگا اور stdin سے ان پٹ کا انتظار کرے گا۔ یہ stdio ٹرانسپورٹ کے ذریعے JSON-RPC پیغامات کا تبادلہ کرتا ہے۔

### مرحلہ 4: انسپیکٹر کے ساتھ ٹیسٹنگ

آپ MCP انسپیکٹر استعمال کرکے اپنا سرور ٹیسٹ کر سکتے ہیں:

1. انسپیکٹر انسٹال کریں: `npx @modelcontextprotocol/inspector`
2. انسپیکٹر چلائیں اور اپنے سرور کی طرف پوائنٹ کریں
3. بنائے گئے ٹولز کو ٹیسٹ کریں

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## اپنے stdio سرور کو ڈیبگ کرنا

### MCP انسپیکٹر کا استعمال

MCP انسپیکٹر MCP سرورز کی ڈیبگنگ اور ٹیسٹنگ کے لیے قیمتی ٹول ہے۔ اسے اپنے stdio سرور کے ساتھ استعمال کرنے کا طریقہ یہ ہے:

1. **انسپیکٹر انسٹال کریں**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **انسپیکٹر چلائیں**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **سرور کی جانچ کریں**: انسپیکٹر ویب انٹرفیس فراہم کرتا ہے جہاں آپ:
   - سرور کی صلاحیتیں دیکھ سکتے ہیں
   - مختلف پیرامیٹرز کے ساتھ ٹولز ٹیسٹ کر سکتے ہیں
   - JSON-RPC پیغامات کی مانیٹرنگ کر سکتے ہیں
   - کنکشن کے مسائل کو ڈیبگ کر سکتے ہیں

### VS Code کا استعمال

آپ VS Code میں براہ راست اپنا MCP سرور ڈیبگ کر سکتے ہیں:

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

2. سرور کوڈ میں بریک پوائنٹس سیٹ کریں
3. ڈیبگر چلائیں اور انسپیکٹر کے ساتھ ٹیسٹ کریں

### عام ڈیبگنگ نکات

- لاگنگ کے لیے `stderr` کا استعمال کریں - `stdout` پر کبھی بھی لکھیں نہیں کیونکہ یہ MCP پیغامات کے لیے مخصوص ہے۔
- تمام JSON-RPC پیغامات نئی لائنز سے جدا ہونے چاہئیں۔
- سب سے پہلے سادہ ٹولز کے ساتھ ٹیسٹ کریں اس سے پہلے کہ پیچیدہ فنکشنز شامل کریں۔
- پیغام فارمیٹس کی جانچ کے لیے انسپیکٹر استعمال کریں۔

## VS Code میں اپنے stdio سرور کا استعمال

جب آپ نے اپنا MCP stdio سرور بنا لیا ہو، تو آپ اسے VS Code کے ساتھ ضم کر سکتے ہیں تاکہ اسے Claude یا دیگر MCP-مطابق کلائنٹس کے ساتھ استعمال کیا جا سکے۔

### کنفیگریشن

1. **MCP کنفیگریشن فائل بنائیں** `%APPDATA%\Claude\claude_desktop_config.json` (ونڈوز) یا `~/Library/Application Support/Claude/claude_desktop_config.json` (میک):

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

2. **Claude کو ری اسٹارٹ کریں**: Claude بند کریں اور دوبارہ کھولیں تاکہ نیا سرور کنفیگریشن لوڈ ہو جائے۔

3. **کنکشن ٹیسٹ کریں**: Claude کے ساتھ بات چیت شروع کریں اور اپنے سرور کے ٹولز استعمال کریں:
   - "کیا آپ مجھے greeting tool استعمال کرتے ہوئے سلام کر سکتے ہیں؟"
   - "15 اور 27 کا مجموعہ حساب کرو"
   - "سرور کی معلومات کیا ہیں؟"

### ٹائپ اسکرپٹ stdio سرور کی مثال

مکمل ٹائپ اسکرپٹ مثال یہاں ہے:

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

اس نئے سبق میں، آپ نے سیکھا کہ:

- موجودہ **stdio ٹرانسپورٹ** (سفارش کردہ طریقہ) کے ساتھ MCP سرور کیسے بنائیں۔
- SSE ٹرانسپورٹ کو کیوں منسوخ کر دیا گیا اور stdio اور Streamable HTTP کو کیوں ترجیح دی گئی۔
- وہ ٹولز بنائیں جو MCP کلائنٹس کال کر سکتے ہیں۔
- MCP انسپیکٹر سے اپنے سرور کو ڈیبگ کریں۔
- VS Code اور Claude کے ساتھ اپنے stdio سرور کو کیسے ضم کریں۔

stdio ٹرانسپورٹ ایک آسان، زیادہ محفوظ، اور بہتر کارکردگی فراہم کرنے والا طریقہ ہے MCP سرورز بنانے کے لیے، جو منسوخ SSE طریقے کے مقابلے میں بہتر ہے۔ 2025-06-18 کی وضاحت کے مطابق یہ زیادہ تر MCP سرور امپلیمینٹیشنز کے لیے سفارش کردہ ٹرانسپورٹ ہے۔

### .NET

1. پہلے کچھ ٹولز بنائیں۔ اس کے لیے ہم *Tools.cs* نامی فائل بنائیں گے جس میں یہ مواد ہوگا:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## مشق: اپنے stdio سرور کی جانچ کرنا

اب جب آپ نے اپنا stdio سرور بنا لیا ہے، تو چلو اس کی جانچ کرتے ہیں کہ یہ صحیح کام کرتا ہے۔

### ضروریات

1. یقینی بنائیں کہ MCP انسپیکٹر انسٹال ہے:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. آپ کا سرور کوڈ محفوظ ہو (مثلاً `server.py` کے طور پر)

### انسپیکٹر کے ساتھ ٹیسٹنگ

1. **اپنے سرور کے ساتھ انسپیکٹر شروع کریں**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ویب انٹرفیس کھولیں**: انسپیکٹر ایک براؤزر ونڈو کھولے گا جہاں آپ کے سرور کی صلاحیتیں دکھائی جائیں گی۔

3. **ٹولز کی جانچ کریں**:
   - مختلف ناموں کے ساتھ `get_greeting` ٹول آزمائیں۔
   - مختلف نمبروں کے ساتھ `calculate_sum` ٹول ٹیسٹ کریں۔
   - `get_server_info` ٹول کال کریں تاکہ سرور میٹا ڈیٹا دیکھ سکیں۔

4. **کمیونیکیشن مانیٹر کریں**: انسپیکٹر JSON-RPC پیغامات دکھاتا ہے جو کلائنٹ اور سرور کے درمیان تبادلہ ہوتے ہیں۔

### آپ کو کیا دیکھنا چاہیے

جب آپ کا سرور صحیح طریقے سے شروع ہوتا ہے، تو آپ کو دیکھنا چاہیے:
- انسپیکٹر میں سرور کی صلاحیتیں درج ہوں۔
- ٹیسٹ کرنے کے لیے دستیاب ٹولز۔
- کامیاب JSON-RPC پیغام کا تبادلہ۔
- انٹرفیس میں ٹول کے جوابات نظر آئیں۔

### عام مسائل اور حل

**سرور شروع نہیں ہوتا:**
- یقینی بنائیں کہ تمام درکار میڈیولز انسٹال ہیں: `pip install mcp`
- پائتھن نحو اور انڈینٹیشن چیک کریں
- کنسول میں ایرر میسجز دیکھیں

**ٹولز دکھائی نہیں دے رہے:**
- `@server.tool()` ڈیکوریٹرز موجود ہوں
- `main()` سے پہلے ٹول فنکشنز ڈیفائن ہوں
- سرور صحیح طریقے سے کنفیگر ہو

**کنکشن مسائل:**
- سرور stdio ٹرانسپورٹ صحیح استعمال کر رہا ہو
- کوئی دوسرا پروسیس مداخلت نہ کر رہا ہو
- انسپیکٹر کمانڈ کی نحو درست ہو

## اسائنمنٹ

اپنے سرور میں مزید صلاحیتیں شامل کرنے کی کوشش کریں۔ [یہ صفحہ](https://api.chucknorris.io/) دیکھیں، مثال کے طور پر، ایک ایسا ٹول شامل کریں جو کوئی API کال کرے۔ آپ فیصلہ کریں کہ سرور کیسا ہونا چاہیے۔ خوش مزاجی :)

## حل

[حل](./solution/README.md) یہاں ایک ممکنہ حل ہے جس میں کام کرنے والا کوڈ شامل ہے۔

## کلیدی نکات

اس باب کے کلیدی نکات درج ذیل ہیں:

- stdio ٹرانسپورٹ مقامی MCP سرورز کے لیے سفارش کردہ میکانزم ہے۔
- stdio ٹرانسپورٹ MCP سرورز اور کلائنٹس کے درمیان معیاری ان پٹ اور آؤٹ پٹ اسٹریمز کے ذریعے آسان بات چیت کی اجازت دیتا ہے۔
- آپ انسپیکٹر اور Visual Studio Code دونوں استعمال کر کے stdio سرورز کو براہ راست استعمال اور ڈیبگ کر سکتے ہیں، جس سے انضمام آسان ہو جاتا ہے۔

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھن کیلکولیٹر](../../../../03-GettingStarted/samples/python)

## اضافی ذرائع

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## آگے کیا ہے

## اگلے مراحل

اب جب آپ نے stdio ٹرانسپورٹ کے ساتھ MCP سرورز بنانا سیکھ لیا ہے، آپ مزید پیشرفت موضوعات کی طرف جا سکتے ہیں:

- **اگلا**: [MCP کے ساتھ HTTP اسٹریمنگ (Streamable HTTP)](../06-http-streaming/README.md) - دور دراز کے سرورز کے لیے دوسرے معاون ٹرانسپورٹ میکانزم کے بارے میں جانیں
- **ایڈوانسڈ**: [MCP سیکورٹی بہترین عمل](../../02-Security/README.md) - اپنے MCP سرورز میں سیکورٹی نافذ کریں
- **پروڈکشن**: [تقرری حکمت عملیاں](../09-deployment/README.md) - اپنے سرورز کو پروڈکشن کے لیے تعینات کریں

## اضافی ذرائع

- [MCP وضاحت 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - سرکاری وضاحت
- [MCP SDK دستاویزات](https://github.com/modelcontextprotocol/sdk) - تمام زبانوں کے لیے SDK حوالہ جات
- [کمیونٹی مثالیں](../../06-CommunityContributions/README.md) - کمیونٹی کی طرف سے مزید سرور مثالیں

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**خلاصہ اخطار:**
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم ذہن میں رکھیں کہ خودکار تراجم میں غلطیاں یا عدم توازن ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تعبیر کی ذمہ داری ہماری نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->