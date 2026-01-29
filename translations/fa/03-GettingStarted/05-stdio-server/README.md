# سرور MCP با انتقال stdio

> **⚠️ به‌روزرسانی مهم**: از تاریخ مشخصات MCP 2025-06-18، انتقال مستقل SSE (رویدادهای ارسال‌شده توسط سرور) **منسوخ شده** و با انتقال "HTTP قابل جریان" جایگزین شده است. مشخصات فعلی MCP دو مکانیزم انتقال اصلی را تعریف می‌کند:
> 1. **stdio** - ورودی/خروجی استاندارد (توصیه‌شده برای سرورهای محلی)
> 2. **HTTP قابل جریان** - برای سرورهای راه دور که ممکن است داخلی از SSE استفاده کنند
>
> این درس به‌روزرسانی شده است تا بر انتقال **stdio** تمرکز کند، که روش توصیه‌شده برای اکثر پیاده‌سازی‌های سرور MCP است.

انتقال stdio به سرورهای MCP اجازه می‌دهد تا از طریق جریان‌های ورودی و خروجی استاندارد با کلاینت‌ها ارتباط برقرار کنند. این مکانیزم انتقال رایج‌ترین و توصیه‌شده در مشخصات فعلی MCP است و راهی ساده و کارآمد برای ساخت سرورهای MCP فراهم می‌کند که به‌راحتی با برنامه‌های کلاینت مختلف یکپارچه می‌شوند.

## مرور کلی

این درس نحوه ساخت و استفاده از سرورهای MCP با استفاده از انتقال stdio را پوشش می‌دهد.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- یک سرور MCP با استفاده از انتقال stdio بسازید.
- یک سرور MCP را با استفاده از Inspector دیباگ کنید.
- یک سرور MCP را با استفاده از Visual Studio Code مصرف کنید.
- مکانیزم‌های انتقال فعلی MCP را درک کنید و بدانید چرا stdio توصیه می‌شود.

## انتقال stdio - نحوه کارکرد

انتقال stdio یکی از دو نوع انتقال پشتیبانی‌شده در مشخصات فعلی MCP (2025-06-18) است. نحوه کار آن به شرح زیر است:

- **ارتباط ساده**: سرور پیام‌های JSON-RPC را از ورودی استاندارد (`stdin`) می‌خواند و پیام‌ها را به خروجی استاندارد (`stdout`) ارسال می‌کند.
- **مبتنی بر فرآیند**: کلاینت سرور MCP را به‌عنوان یک زیرفرآیند اجرا می‌کند.
- **فرمت پیام**: پیام‌ها درخواست‌ها، اعلان‌ها یا پاسخ‌های JSON-RPC جداگانه هستند که با خطوط جدید جدا می‌شوند.
- **لاگ‌گیری**: سرور ممکن است رشته‌های UTF-8 را برای اهداف لاگ‌گیری به خطای استاندارد (`stderr`) بنویسد.

### الزامات کلیدی:
- پیام‌ها باید با خطوط جدید جدا شوند و نباید خطوط جدید داخلی داشته باشند.
- سرور نباید چیزی به `stdout` بنویسد که پیام معتبر MCP نباشد.
- کلاینت نباید چیزی به `stdin` سرور بنویسد که پیام معتبر MCP نباشد.

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

- کلاس `Server` و `StdioServerTransport` را از SDK MCP وارد می‌کنیم.
- یک نمونه سرور با پیکربندی و قابلیت‌های پایه ایجاد می‌کنیم.

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

در کد بالا:

- یک نمونه سرور با استفاده از SDK MCP ایجاد می‌کنیم.
- ابزارها را با استفاده از دکوریتورها تعریف می‌کنیم.
- از مدیریت‌کننده زمینه `stdio_server` برای مدیریت انتقال استفاده می‌کنیم.

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

تفاوت کلیدی با SSE این است که سرورهای stdio:

- نیاز به تنظیم سرور وب یا نقاط پایانی HTTP ندارند.
- به‌عنوان زیرفرآیند توسط کلاینت اجرا می‌شوند.
- از طریق جریان‌های stdin/stdout ارتباط برقرار می‌کنند.
- پیاده‌سازی و دیباگ ساده‌تری دارند.

## تمرین: ایجاد یک سرور stdio

برای ایجاد سرور خود، باید دو نکته را در نظر داشته باشید:

- باید از یک سرور وب برای افشای نقاط پایانی برای اتصال و پیام‌ها استفاده کنیم.

## آزمایشگاه: ایجاد یک سرور ساده MCP با انتقال stdio

در این آزمایشگاه، یک سرور ساده MCP با استفاده از انتقال توصیه‌شده stdio ایجاد خواهیم کرد. این سرور ابزارهایی را افشا می‌کند که کلاینت‌ها می‌توانند با استفاده از پروتکل مدل کانتکست استاندارد فراخوانی کنند.

### پیش‌نیازها

- Python 3.8 یا بالاتر
- SDK MCP Python: `pip install mcp`
- درک پایه از برنامه‌نویسی async

بیایید اولین سرور MCP stdio خود را ایجاد کنیم:

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

## تفاوت‌های کلیدی با روش منسوخ‌شده SSE

**انتقال stdio (استاندارد فعلی):**
- مدل زیرفرآیند ساده - کلاینت سرور را به‌عنوان فرآیند فرزند اجرا می‌کند.
- ارتباط از طریق stdin/stdout با استفاده از پیام‌های JSON-RPC
- نیاز به تنظیم سرور HTTP ندارد.
- عملکرد و امنیت بهتر
- دیباگ و توسعه آسان‌تر

**انتقال SSE (منسوخ‌شده از تاریخ MCP 2025-06-18):**
- نیاز به سرور HTTP با نقاط پایانی SSE داشت.
- تنظیم پیچیده‌تر با زیرساخت سرور وب
- ملاحظات امنیتی اضافی برای نقاط پایانی HTTP
- اکنون برای سناریوهای مبتنی بر وب با HTTP قابل جریان جایگزین شده است.

### ایجاد سرور با انتقال stdio

برای ایجاد سرور stdio خود، باید:

1. **کتابخانه‌های مورد نیاز را وارد کنید** - به اجزای سرور MCP و انتقال stdio نیاز داریم.
2. **یک نمونه سرور ایجاد کنید** - سرور را با قابلیت‌های آن تعریف کنید.
3. **ابزارها را تعریف کنید** - عملکردی که می‌خواهیم افشا کنیم اضافه کنید.
4. **انتقال را تنظیم کنید** - ارتباط stdio را پیکربندی کنید.
5. **سرور را اجرا کنید** - سرور را راه‌اندازی کنید و پیام‌ها را مدیریت کنید.

بیایید این مراحل را گام‌به‌گام انجام دهیم:

### مرحله 1: ایجاد یک سرور پایه stdio

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

کد را به‌عنوان `server.py` ذخیره کنید و از خط فرمان اجرا کنید:

```bash
python server.py
```

سرور شروع به کار می‌کند و منتظر ورودی از stdin می‌ماند. ارتباط با استفاده از پیام‌های JSON-RPC از طریق انتقال stdio انجام می‌شود.

### مرحله 4: آزمایش با Inspector

می‌توانید سرور خود را با استفاده از MCP Inspector آزمایش کنید:

1. Inspector را نصب کنید: `npx @modelcontextprotocol/inspector`
2. Inspector را اجرا کنید و آن را به سرور خود متصل کنید.
3. ابزارهایی که ایجاد کرده‌اید را آزمایش کنید.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## دیباگ کردن سرور stdio خود

### استفاده از MCP Inspector

MCP Inspector ابزاری ارزشمند برای دیباگ و آزمایش سرورهای MCP است. نحوه استفاده از آن با سرور stdio شما:

1. **Inspector را نصب کنید**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector را اجرا کنید**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **سرور خود را آزمایش کنید**: Inspector یک رابط وب ارائه می‌دهد که در آن می‌توانید:
   - قابلیت‌های سرور را مشاهده کنید.
   - ابزارها را با پارامترهای مختلف آزمایش کنید.
   - پیام‌های JSON-RPC را نظارت کنید.
   - مشکلات اتصال را دیباگ کنید.

### استفاده از VS Code

می‌توانید سرور MCP خود را مستقیماً در VS Code دیباگ کنید:

1. یک پیکربندی اجرا در `.vscode/launch.json` ایجاد کنید:
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

2. نقاط توقف را در کد سرور خود تنظیم کنید.
3. دیباگر را اجرا کنید و با Inspector آزمایش کنید.

### نکات رایج دیباگ

- از `stderr` برای لاگ‌گیری استفاده کنید - هرگز چیزی به `stdout` ننویسید زیرا برای پیام‌های MCP رزرو شده است.
- اطمینان حاصل کنید که همه پیام‌های JSON-RPC با خطوط جدید جدا شده‌اند.
- ابتدا ابزارهای ساده را آزمایش کنید و سپس عملکرد پیچیده‌تر اضافه کنید.
- از Inspector برای تأیید فرمت پیام‌ها استفاده کنید.

## مصرف سرور stdio خود در VS Code

پس از ساخت سرور MCP stdio خود، می‌توانید آن را با VS Code یکپارچه کنید تا از آن با Claude یا سایر کلاینت‌های سازگار با MCP استفاده کنید.

### پیکربندی

1. **یک فایل پیکربندی MCP ایجاد کنید** در `%APPDATA%\Claude\claude_desktop_config.json` (ویندوز) یا `~/Library/Application Support/Claude/claude_desktop_config.json` (مک):

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

2. **Claude را مجدداً راه‌اندازی کنید**: Claude را ببندید و دوباره باز کنید تا پیکربندی جدید سرور بارگذاری شود.

3. **اتصال را آزمایش کنید**: یک مکالمه با Claude شروع کنید و ابزارهای سرور خود را آزمایش کنید:
   - "می‌توانی با ابزار خوش‌آمدگویی به من سلام کنی؟"
   - "مجموع 15 و 27 را محاسبه کن."
   - "اطلاعات سرور چیست؟"

### نمونه سرور stdio TypeScript

در اینجا یک نمونه کامل TypeScript برای مرجع آورده شده است:

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

## خلاصه

در این درس به‌روزرسانی‌شده، یاد گرفتید که:

- سرورهای MCP را با انتقال فعلی **stdio** (روش توصیه‌شده) بسازید.
- درک کنید چرا انتقال SSE به نفع stdio و HTTP قابل جریان منسوخ شد.
- ابزارهایی ایجاد کنید که کلاینت‌های MCP بتوانند فراخوانی کنند.
- سرور خود را با استفاده از MCP Inspector دیباگ کنید.
- سرور stdio خود را با VS Code و Claude یکپارچه کنید.

انتقال stdio راهی ساده‌تر، امن‌تر و با عملکرد بهتر برای ساخت سرورهای MCP نسبت به روش منسوخ‌شده SSE فراهم می‌کند. این مکانیزم انتقال توصیه‌شده برای اکثر پیاده‌سازی‌های سرور MCP طبق مشخصات 2025-06-18 است.

### .NET

1. ابتدا بیایید چند ابزار ایجاد کنیم، برای این کار یک فایل *Tools.cs* با محتوای زیر ایجاد می‌کنیم:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## تمرین: آزمایش سرور stdio خود

اکنون که سرور stdio خود را ساخته‌اید، بیایید آن را آزمایش کنیم تا مطمئن شویم به‌درستی کار می‌کند.

### پیش‌نیازها

1. اطمینان حاصل کنید که MCP Inspector نصب شده است:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. کد سرور شما باید ذخیره شده باشد (مثلاً به‌عنوان `server.py`)

### آزمایش با Inspector

1. **Inspector را با سرور خود اجرا کنید**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **رابط وب را باز کنید**: Inspector یک پنجره مرورگر باز می‌کند که قابلیت‌های سرور شما را نشان می‌دهد.

3. **ابزارها را آزمایش کنید**: 
   - ابزار `get_greeting` را با نام‌های مختلف امتحان کنید.
   - ابزار `calculate_sum` را با اعداد مختلف آزمایش کنید.
   - ابزار `get_server_info` را فراخوانی کنید تا متادیتای سرور را ببینید.

4. **ارتباط را نظارت کنید**: Inspector پیام‌های JSON-RPC که بین کلاینت و سرور ردوبدل می‌شوند را نشان می‌دهد.

### چیزی که باید ببینید

وقتی سرور شما به‌درستی شروع شود، باید ببینید:
- قابلیت‌های سرور در Inspector فهرست شده‌اند.
- ابزارها برای آزمایش در دسترس هستند.
- تبادل موفقیت‌آمیز پیام‌های JSON-RPC
- پاسخ‌های ابزار در رابط نمایش داده می‌شوند.

### مشکلات رایج و راه‌حل‌ها

**سرور شروع نمی‌شود:**
- بررسی کنید که همه وابستگی‌ها نصب شده‌اند: `pip install mcp`
- نحو و تورفتگی پایتون را بررسی کنید.
- پیام‌های خطا را در کنسول بررسی کنید.

**ابزارها ظاهر نمی‌شوند:**
- اطمینان حاصل کنید که دکوریتورهای `@server.tool()` وجود دارند.
- بررسی کنید که توابع ابزار قبل از `main()` تعریف شده‌اند.
- مطمئن شوید که سرور به‌درستی پیکربندی شده است.

**مشکلات اتصال:**
- مطمئن شوید که سرور به‌درستی از انتقال stdio استفاده می‌کند.
- بررسی کنید که هیچ فرآیند دیگری تداخل ایجاد نمی‌کند.
- دستور Inspector را بررسی کنید.

## تکلیف

سعی کنید سرور خود را با قابلیت‌های بیشتری گسترش دهید. به [این صفحه](https://api.chucknorris.io/) مراجعه کنید تا، به‌عنوان مثال، ابزاری اضافه کنید که یک API را فراخوانی کند. شما تصمیم می‌گیرید که سرور چگونه باشد. لذت ببرید :)

## راه‌حل

[راه‌حل](./solution/README.md) در اینجا یک راه‌حل ممکن با کد کاری آورده شده است.

## نکات کلیدی

نکات کلیدی این فصل به شرح زیر است:

- انتقال stdio مکانیزم توصیه‌شده برای سرورهای محلی MCP است.
- انتقال stdio ارتباط یکپارچه بین سرورهای MCP و کلاینت‌ها را با استفاده از جریان‌های ورودی و خروجی استاندارد فراهم می‌کند.
- می‌توانید از هر دو Inspector و Visual Studio Code برای مصرف مستقیم سرورهای stdio استفاده کنید، که دیباگ و یکپارچه‌سازی را آسان می‌کند.

## نمونه‌ها 

- [ماشین‌حساب جاوا](../samples/java/calculator/README.md)
- [ماشین‌حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین‌حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین‌حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین‌حساب پایتون](../../../../03-GettingStarted/samples/python) 

## منابع اضافی

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## چه چیزی در انتظار شماست

## مراحل بعدی

اکنون که یاد گرفتید چگونه سرورهای MCP را با انتقال stdio بسازید، می‌توانید موضوعات پیشرفته‌تر را بررسی کنید:

- **بعدی**: [HTTP قابل جریان با MCP](../06-http-streaming/README.md) - درباره مکانیزم انتقال دیگر برای سرورهای راه دور بیاموزید.
- **پیشرفته**: [بهترین شیوه‌های امنیتی MCP](../../02-Security/README.md) - امنیت را در سرورهای MCP خود پیاده‌سازی کنید.
- **تولید**: [استراتژی‌های استقرار](../09-deployment/README.md) - سرورهای خود را برای استفاده تولیدی مستقر کنید.

## منابع اضافی

- [مشخصات MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - مشخصات رسمی
- [مستندات SDK MCP](https://github.com/modelcontextprotocol/sdk) - مراجع SDK برای همه زبان‌ها
- [نمونه‌های جامعه](../../06-CommunityContributions/README.md) - نمونه‌های بیشتر سرور از جامعه

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.