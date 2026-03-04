# سرور MCP با ترابری stdio

> **⚠️ بروزرسانی مهم**: از نسخه MCP Specification 2025-06-18، ترابری SSE (Server-Sent Events) مستقل **منسوخ** شده و جایگزین آن ترابری "Streamable HTTP" شده است. نسخه فعلی MCP دو مکانیزم ترابری اصلی را تعریف می‌کند:
> 1. **stdio** - ورودی/خروجی استاندارد (توصیه شده برای سرورهای محلی)
> 2. **Streamable HTTP** - برای سرورهای راه دور که ممکن است به صورت داخلی SSE استفاده کنند
>
> این درس به روز شده تا تمرکز خود را بر **ترابری stdio** بگذارد، که روش پیشنهادی برای بیشتر پیاده‌سازی‌های سرور MCP است.

ترابری stdio به سرورهای MCP اجازه می‌دهد تا از طریق جریان‌های ورودی و خروجی استاندارد با کلاینت‌ها ارتباط برقرار کنند. این رایج‌ترین و توصیه‌شده‌ترین مکانیزم ترابری در نسخه فعلی MCP است که راهی ساده و کارآمد برای ساخت سرورهای MCP فراهم می‌کند که به سادگی با برنامه‌های مختلف کلاینت ادغام شوند.

## مرور کلی

این درس نحوه ساخت و استفاده از سرورهای MCP با استفاده از ترابری stdio را پوشش می‌دهد.

## اهداف یادگیری

تا پایان این درس، قادر خواهید بود:

- یک سرور MCP با استفاده از ترابری stdio بسازید.
- یک سرور MCP را با استفاده از Inspector اشکال‌زدایی کنید.
- از یک سرور MCP با Visual Studio Code استفاده کنید.
- مکانیزم‌های ترابری فعلی MCP و دلیل توصیه شدن stdio را درک کنید.

## ترابری stdio - نحوه عملکرد

ترابری stdio یکی از دو نوع ترابری پشتیبانی شده در نسخه فعلی MCP (2025-06-18) است. نحوه عملکرد آن به این صورت است:

- **ارتباط ساده**: سرور پیام‌های JSON-RPC را از ورودی استاندارد (`stdin`) می‌خواند و پیام‌ها را به خروجی استاندارد (`stdout`) ارسال می‌کند.
- **بر پایه فرآیند**: کلاینت سرور MCP را به صورت یک زیر فرایند راه‌اندازی می‌کند.
- **فرمت پیام**: پیام‌ها درخواست‌ها، اطلاعیه‌ها یا پاسخ‌های JSON-RPC مجزا هستند که با خط جدید جدا شده‌اند.
- **لاگ‌گذاری**: سرور می‌تواند رشته‌های UTF-8 را برای اهداف لاگ‌گذاری به خروجی خطا (`stderr`) بنویسد.

### الزامات کلیدی:
- پیام‌ها باید با خط جدید جدا شده و نباید درون خود خط جدید داشته باشند
- سرور نباید هیچ چیزی به `stdout` بنویسد که پیام MCP معتبر نباشد
- کلاینت نباید هیچ چیزی به `stdin` سرور بنویسد که پیام MCP معتبر نباشد

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

در کد بالا:

- کلاس `Server` و `StdioServerTransport` از SDK MCP وارد شده‌اند
- یک نمونه سرور با پیکربندی و قابلیت‌های پایه ایجاد شده است

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ایجاد نمونه سرور
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

در کد بالا ما:

- یک نمونه سرور با استفاده از SDK MCP می‌سازیم
- ابزارها را با دکوراتورها تعریف می‌کنیم
- از context manager `stdio_server` برای مدیریت ترابری استفاده می‌کنیم

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

تفاوت کلیدی با SSE این است که سرورهای stdio:

- نیازی به راه‌اندازی وب سرور یا نقاط انتهایی HTTP ندارند
- به عنوان زیر فرایند توسط کلاینت راه‌اندازی می‌شوند
- از طریق جریان‌های stdin/stdout ارتباط برقرار می‌کنند
- پیاده‌سازی و اشکال‌زدایی ساده‌تری دارند

## تمرین: ایجاد یک سرور stdio

برای ایجاد سرور خود، باید دو نکته را مد نظر داشته باشیم:

- برای اتصال و پیام‌ها نیاز به استفاده از یک وب سرور برای تهیه نقاط انتهایی داریم.
## آزمایشگاه: ایجاد یک سرور ساده MCP stdio

در این آزمایشگاه، یک سرور ساده MCP با استفاده از ترابری stdio توصیه‌شده ایجاد می‌کنیم. این سرور ابزارهایی را ارائه می‌دهد که کلاینت‌ها می‌توانند از طریق پروتکل استاندارد Model Context فراخوانی کنند.

### پیش‌نیازها

- پایتون 3.8 یا بالاتر
- MCP Python SDK: `pip install mcp`
- درک اولیه از برنامه‌نویسی ناهمگام (async)

بیایید با ایجاد اولین سرور MCP stdio خود شروع کنیم:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# پیکربندی لاگ‌برداری
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ایجاد سرور
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
    # استفاده از انتقال stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## تفاوت‌های کلیدی با روش منسوخ SSE

**ترابری stdio (استاندارد فعلی):**
- مدل زیر فرایند ساده — کلاینت سرور را به عنوان فرایند فرزند راه‌اندازی می‌کند
- ارتباط از طریق stdin/stdout با پیام‌های JSON-RPC
- نیاز به راه‌اندازی سرور HTTP ندارد
- کارایی و امنیت بهتر
- اشکال‌زدایی و توسعه آسان‌تر

**ترابری SSE (از MCP 2025-06-18 منسوخ شده):**
- نیازمند سرور HTTP با نقاط انتهایی SSE
- راه‌اندازی پیچیده‌تر با زیرساخت وب سرور
- ملاحظات امنیتی بیشتر برای نقاط انتهایی HTTP
- اکنون جایگزین شده توسط Streamable HTTP برای سناریوهای وب

### ایجاد سرور با ترابری stdio

برای ساخت سرور stdio خود، باید:

1. **وارد کردن کتابخانه‌های لازم** - نیازمند مؤلفه‌های سرور MCP و ترابری stdio هستیم
2. **ایجاد نمونه سرور** - تعریف سرور با قابلیت‌هایش
3. **تعریف ابزارها** - افزودن قابلیت‌هایی که می‌خواهیم ارائه دهیم
4. **تنظیم ترابری** - پیکربندی ارتباط stdio
5. **اجرای سرور** - راه‌اندازی سرور و پردازش پیام‌ها

بیایید قدم به قدم این کار را انجام دهیم:

### مرحله 1: ایجاد یک سرور stdio پایه

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# پیکربندی لاگ‌گیری
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ایجاد سرور
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

### مرحله 2: افزودن ابزارهای بیشتر

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

### مرحله 3: اجرای سرور

کد را به نام `server.py` ذخیره کرده و از خط فرمان اجرا کنید:

```bash
python server.py
```

سرور شروع به کار کرده و منتظر ورودی از `stdin` می‌شود. ارتباط از طریق پیام‌های JSON-RPC روی ترابری stdio انجام می‌شود.

### مرحله 4: تست با Inspector

شما می‌توانید سرور خود را با استفاده از MCP Inspector تست کنید:

1. نصب Inspector: `npx @modelcontextprotocol/inspector`
2. اجرای Inspector و متصل شدن به سرور خود
3. تست ابزارهایی که ساخته‌اید

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## اشکال‌زدایی سرور stdio شما

### استفاده از MCP Inspector

MCP Inspector ابزاری ارزشمند برای اشکال‌زدایی و تست سرورهای MCP است. نحوه استفاده از آن با سرور stdio شما به شرح زیر است:

1. **نصب Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **اجرای Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **تست سرور خود**: Inspector یک رابط وب فراهم می‌کند که می‌توانید:
   - قابلیت‌های سرور را مشاهده کنید
   - ابزارها را با پارامترهای مختلف تست کنید
   - پیام‌های JSON-RPC را دنبال کنید
   - مشکلات اتصال را اشکال‌زدایی کنید

### استفاده از VS Code

شما همچنین می‌توانید سرور MCP خود را مستقیماً در VS Code اشکال‌زدایی کنید:

1. ایجاد پیکربندی اجرای اشکال‌زدایی در `.vscode/launch.json`:
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

2. نقاط توقف را در کد سرور خود تنظیم کنید
3. اشکال‌زدای را اجرا کرده و با Inspector تست کنید

### نکات رایج در اشکال‌زدایی

- از `stderr` برای لاگ‌گذاری استفاده کنید - هرگز به `stdout` ننویسید چون برای پیام‌های MCP رزرو شده است
- اطمینان حاصل کنید که همه پیام‌های JSON-RPC با خط جدید جدا شده‌اند
- ابتدا با ابزارهای ساده تست کنید قبل از افزودن قابلیت‌های پیچیده
- از Inspector برای بررسی فرمت پیام‌ها استفاده کنید

## استفاده از سرور stdio خود در VS Code

وقتی سرور MCP stdio خود را ساختید، می‌توانید آن را با VS Code ادغام کنید تا با کلاینت‌هایی مثل Claude یا سایر کلاینت‌های سازگار MCP استفاده کنید.

### پیکربندی

1. **یک فایل پیکربندی MCP** بسازید در `%APPDATA%\Claude\claude_desktop_config.json` (ویندوز) یا `~/Library/Application Support/Claude/claude_desktop_config.json` (مک):

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

2. **راه‌اندازی مجدد Claude**: Claude را ببندید و دوباره باز کنید تا پیکربندی جدید سرور بارگذاری شود.

3. **تست اتصال**: با Claude مکالمه‌ای را شروع کرده و تلاش کنید از ابزارهای سرور خود استفاده کنید:
   - "می‌توانی با استفاده از ابزار خوش‌آمدگویی به من سلام کنی؟"
   - "جمع ۱۵ و ۲۷ را حساب کن"
   - "اطلاعات سرور چیست؟"

### نمونه سرور stdio TypeScript

در اینجا یک نمونه کامل TypeScript جهت مرجع آورده شده است:

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

// افزودن ابزارها
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

### نمونه سرور stdio .NET

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

## خلاصه

در این درس به‌روزشده، شما یاد گرفتید چگونه:

- سرورهای MCP را با استفاده از **ترابری stdio فعلی** بسازید (روش توصیه شده)
- بفهمید چرا ترابری SSE منسوخ شد و چرا stdio و Streamable HTTP ترجیح داده شدند
- ابزارهایی بسازید که توسط کلاینت‌های MCP فراخوانی شوند
- با استفاده از MCP Inspector سرور خود را اشکال‌زدایی کنید
- سرور stdio خود را با VS Code و Claude ادغام کنید

ترابری stdio راهی ساده‌تر، امن‌تر و با عملکرد بهتر برای ساخت سرورهای MCP نسبت به روش منسوخ SSE فراهم می‌کند. این ترابری به‌عنوان روش توصیه‌شده برای بیشتر پیاده‌سازی‌های سرور MCP طبق نسخه 2025-06-18 شناخته شده است.

### .NET

1. ابتدا بیایید چند ابزار بسازیم، برای این کار یک فایل *Tools.cs* با محتوای زیر ایجاد می‌کنیم:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## تمرین: تست سرور stdio خود

حال که سرور stdio خود را ساخته‌اید، بیایید آن را تست کنیم تا مطمئن شویم به درستی کار می‌کند.

### پیش‌نیازها

1. اطمینان حاصل کنید که MCP Inspector نصب شده است:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. کد سرور شما باید ذخیره شده باشد (مثلاً به نام `server.py`)

### تست با Inspector

1. **Inspector را با سرور خود راه‌اندازی کنید**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **رابط وب را باز کنید**: Inspector یک پنجره مرورگر باز می‌کند که قابلیت‌های سرور شما را نمایش می‌دهد.

3. **ابزارها را تست کنید**: 
   - ابزار `get_greeting` را با نام‌های مختلف امتحان کنید
   - ابزار `calculate_sum` را با اعداد مختلف تست کنید
   - ابزار `get_server_info` را برای دیدن متادیتای سرور فراخوانی کنید

4. **ارتباط را نظارت کنید**: Inspector پیام‌های JSON-RPC رد و بدل شده بین کلاینت و سرور را نمایش می‌دهد.

### آنچه باید ببینید

زمانی که سرور شما به درستی شروع به کار کرد، باید موارد زیر را مشاهده کنید:
- قابلیت‌های سرور در Inspector لیست شده باشد
- ابزارهایی برای تست در دسترس باشند
- تبادل موفقیت‌آمیز پیام‌های JSON-RPC
- پاسخ‌های ابزار در رابط کاربری نمایش داده شوند

### مشکلات رایج و راه‌حل‌ها

**سرور شروع نمی‌شود:**
- بررسی کنید که همه وابستگی‌ها نصب شده باشند: `pip install mcp`
- نحو و تورفتگی پایتون را بررسی کنید
- پیام‌های خطا را در کنسول بررسی کنید

**ابزارها نمایش داده نمی‌شوند:**
- بررسی کنید دکوراتورهای `@server.tool()` وجود داشته باشند
- مطمئن شوید توابع ابزار قبل از `main()` تعریف شده‌اند
- اطمینان حاصل کنید سرور به درستی پیکربندی شده است

**مشکلات اتصال:**
- مطمئن شوید سرور ترابری stdio را به درستی استفاده می‌کند
- بررسی کنید فرایندهای دیگری تداخلی ایجاد نمی‌کنند
- نحو فرمان Inspector را بررسی کنید

## تمرین

سعی کنید سرور خود را با قابلیت‌های بیشتر توسعه دهید. به [این صفحه](https://api.chucknorris.io/) مراجعه کنید تا مثلاً ابزاری اضافه کنید که به یک API فراخوانی بزند. شما تصمیم می‌گیرید سرور چگونه باشد. موفق باشید :)

## راه‌حل

[راه‌حل](./solution/README.md) اینجا یک راه‌حل ممکن با کد کاری ارائه شده است.

## نکات کلیدی

نکات کلیدی این فصل عبارتند از:

- ترابری stdio مکانیزم توصیه شده برای سرورهای محلی MCP است.
- ترابری stdio ارتباط بی‌وقفه بین سرورها و کلاینت‌های MCP را با استفاده از جریان‌های ورودی و خروجی استاندارد فراهم می‌کند.
- می‌توانید به طور مستقیم از Inspector و Visual Studio Code برای استفاده از سرورهای stdio بهره ببرید که اشکال‌زدایی و ادغام را ساده می‌کند.

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین حساب TypeScript](../samples/typescript/README.md)
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python) 

## منابع بیشتر

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ادامه مسیر

## گام‌های بعدی

حالا که یاد گرفته‌اید چگونه سرورهای MCP با ترابری stdio بسازید، می‌توانید موضوعات پیشرفته‌تری را دنبال کنید:

- **بعدی**: [HTTP Streaming با MCP (Streamable HTTP)](../06-http-streaming/README.md) - درباره مکانیزم ترابری دیگر برای سرورهای راه دور یاد بگیرید
- **پیشرفته**: [بهترین شیوه‌های امنیتی MCP](../../02-Security/README.md) - پیاده‌سازی امنیت در سرورهای MCP
- **تولید**: [استراتژی‌های استقرار](../09-deployment/README.md) - استقرار سرورها برای استفاده در محیط تولید

## منابع بیشتر

- [مشخصات MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - مشخصات رسمی
- [مستندات MCP SDK](https://github.com/modelcontextprotocol/sdk) - مراجع SDK برای تمام زبان‌ها
- [نمونه‌های انجمن](../../06-CommunityContributions/README.md) - نمونه‌های بیشتر سرورها از جامعه کاربران

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطا یا نادرستی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هر گونه سوءتفاهم یا سوءتعبیر ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->