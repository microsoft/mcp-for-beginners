# سرور MCP با ترابری stdio

> **⚠️ به‌روزرسانی مهم**: از نسخه MCP مشخصات ۲۰۲۵-۰۶-۱۸، ترابری مستقل SSE (Server-Sent Events) ***منسوخ*** شده و جایگزین آن "HTTP قابل پخش (Streamable HTTP)" شده است. مشخصات کنونی MCP دو مکانیزم اصلی ترابری را تعریف می‌کند:
> 1. **stdio** - ورودی/خروجی استاندارد (توصیه‌شده برای سرورهای محلی)
> 2. **HTTP قابل پخش** - برای سرورهای راه دور که ممکن است از SSE به صورت داخلی استفاده کنند
>
> این درس به‌روزرسانی شده تا بر **ترابری stdio** که رویکرد توصیه‌شده برای بیشتر پیاده‌سازی‌های سرور MCP است تمرکز کند.

ترابری stdio به سرورهای MCP اجازه می‌دهد که از طریق جریان‌های ورودی و خروجی استاندارد با کلاینت‌ها ارتباط برقرار کنند. این رایج‌ترین و توصیه‌شده‌ترین مکانیزم ترابری در مشخصات کنونی MCP است که روشی ساده و کارآمد برای ساخت سرورهای MCP ارائه می‌دهد که به آسانی با برنامه‌های مختلف کلاینت قابل ادغام هستند.

## مرور کلی

این درس پوشش می‌دهد که چگونه با استفاده از ترابری stdio سرورهای MCP بسازیم و مصرف کنیم.

## اهداف یادگیری

در پایان این درس قادر خواهید بود:

- ساخت یک سرور MCP با ترابری stdio.
- اشکال‌زدایی یک سرور MCP با استفاده از Inspector.
- مصرف یک سرور MCP با استفاده از Visual Studio Code.
- درک مکانیزم‌های ترابری کنونی MCP و دلیل توصیه شدن stdio.

## ترابری stdio - چگونه کار می‌کند

ترابری stdio یکی از دو نوع ترابری پشتیبانی شده در مشخصات فعلی MCP (۲۰۲۵-۰۶-۱۸) است. عملکرد آن به شرح زیر است:

- **ارتباط ساده**: سرور پیام‌های JSON-RPC را از ورودی استاندارد (`stdin`) می‌خواند و پیام‌ها را به خروجی استاندارد (`stdout`) ارسال می‌کند.
- **بر پایه فرایند**: کلاینت سرور MCP را به عنوان زیرروند (subprocess) راه‌اندازی می‌کند.
- **فرمت پیام**: پیام‌ها درخواست‌ها، اعلان‌ها یا پاسخ‌های JSON-RPC جدا شده با خطوط جدید (newline) هستند.
- **لاگ‌برداری**: سرور ممکن است رشته‌های UTF-8 را برای لاگ‌برداری به خطای استاندارد (`stderr`) بنویسد.

### الزامات کلیدی:
- پیام‌ها باید با خطوط جدید جدا شده و نباید شامل خطوط جدید داخلی باشند
- سرور نباید چیزی به `stdout` بنویسد که پیام معتبر MCP نباشد
- کلاینت نباید چیزی به `stdin` سرور بفرستد که پیام معتبر MCP نباشد

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

در کد بالا:

- کلاس `Server` و `StdioServerTransport` را از SDK MCP وارد می‌کنیم
- نمونه سرور را با پیکربندی و قابلیت‌های پایه ایجاد می‌کنیم
- نمونه یک `StdioServerTransport` می‌سازیم و سرور را به آن متصل می‌کنیم تا ارتباط روی stdin/stdout برقرار شود

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

در کد بالا:

- یک نمونه سرور با استفاده از SDK MCP ایجاد می‌کنیم
- ابزارها را با استفاده از دکوراتورها تعریف می‌کنیم
- از context manager به نام stdio_server برای مدیریت ترابری استفاده می‌کنیم

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

- نیازی به راه‌اندازی سرور وب یا نقاط پایانی HTTP ندارند
- به عنوان زیرروند به وسیله کلاینت لانچ می‌شوند
- از طریق جریان‌های stdin/stdout ارتباط برقرار می‌کنند
- پیاده‌سازی و اشکال‌زدایی ساده‌تری دارند

## تمرین: ایجاد یک سرور stdio

برای ایجاد سرور خود، دو نکته را باید در نظر داشته باشیم:

- ما باید از یک سرور وب برای باز کردن نقاط پایانی برای اتصال و پیام‌ها استفاده کنیم.

## آزمایشگاه: ساخت یک سرور ساده MCP با ترابری stdio

در این آزمایشگاه، یک سرور ساده MCP می‌سازیم که از ترابری stdio توصیه‌شده استفاده می‌کند. این سرور ابزارهایی را ارائه می‌دهد که کلاینت‌ها می‌توانند از طریق پروتکل استاندارد Model Context صدا بزنند.

### پیش‌نیازها

- پایتون نسخه ۳.۸ یا بالاتر
- SDK پایتون MCP: `pip install mcp`
- درک پایه‌ای از برنامه‌نویسی ناهمگام (async)

بیا با ساخت اولین سرور stdio MCP شروع کنیم:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# پیکربندی لاگ‌گیری
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# سرور را ایجاد کنید
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
    # از ترنسپورت stdio استفاده کنید
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


## تفاوت‌های کلیدی با رویکرد منسوخ SSE

**ترابری Stdio (استاندارد کنونی):**
- مدل زیرروند ساده - کلاینت سرور را به عنوان فرزند فرایند اجرا می‌کند
- ارتباط از طریق stdin/stdout با پیام‌های JSON-RPC
- نیاز به راه‌اندازی سرور HTTP نیست
- عملکرد و امنیت بهتر
- اشکال‌زدایی و توسعه آسان‌تر

**ترابری SSE (منسوخ شده از MCP ۲۰۲۵-۰۶-۱۸):**
- نیازمند سرور HTTP با نقاط پایانی SSE
- راه‌اندازی پیچیده‌تر با زیرساخت وب سرور
- ملاحظات امنیتی اضافی برای نقاط پایانی HTTP
- اکنون با HTTP قابل پخش برای سناریوهای مبتنی بر وب جایگزین شده است

### ایجاد سرور با ترابری stdio

برای ایجاد سرور stdio ما باید:

1. **وارد کردن کتابخانه‌های مورد نیاز** - ما به کامپوننت‌های سرور MCP و ترابری stdio نیاز داریم
2. **ایجاد یک نمونه سرور** - تعریف سرور با قابلیت‌هایش
3. **تعریف ابزارها** - افزودن عملکردی که می‌خواهیم ارائه دهیم
4. **راه‌اندازی ترابری** - پیکربندی ارتباط stdio
5. **اجرای سرور** - شروع سرور و مدیریت پیام‌ها

بیایید قدم به قدم بسازیم:

### مرحله ۱: ایجاد یک سرور ساده stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# پیکربندی ثبت وقایع
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

### مرحله ۲: افزودن ابزارهای بیشتر

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

### مرحله ۳: اجرای سرور

کد را به نام `server.py` ذخیره کنید و از خط فرمان اجرا کنید:

```bash
python server.py
```

سرور شروع می‌شود و منتظر ورودی از stdin می‌ماند. ارتباط از طریق پیام‌های JSON-RPC روی ترابری stdio برقرار می‌شود.

### مرحله ۴: آزمایش با Inspector

می‌توانید سرور خود را با استفاده از MCP Inspector آزمایش کنید:

1. Inspector را نصب کنید: `npx @modelcontextprotocol/inspector`
2. Inspector را اجرا کرده و به سرور خود اشاره دهید
3. ابزارهایی که ساخته‌اید را تست کنید

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## اشکال‌زدایی سرور stdio شما

### استفاده از MCP Inspector

MCP Inspector ابزاری ارزشمند برای اشکال‌زدایی و تست سرورهای MCP است. نحوه استفاده از آن با سرور stdio شما:

1. **نصب Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **اجرای Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **تست سرور**: Inspector یک رابط وب ارائه می‌دهد که می‌توانید:
   - قابلیت‌های سرور را مشاهده کنید
   - ابزارها را با پارامترهای مختلف تست کنید
   - پیام‌های JSON-RPC را نظارت کنید
   - مشکلات اتصال را اشکال‌زدایی کنید

### استفاده از VS Code

همچنین می‌توانید سرور MCP خود را مستقیماً در VS Code اشکال‌زدایی کنید:

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

۲. نقاط توقف (breakpoints) را در کد سرور خود تنظیم کنید
۳. اشکال‌زداینده را اجرا کرده و با Inspector تست کنید

### نکات رایج اشکال‌زدایی

- از `stderr` برای لاگ‌برداری استفاده کنید - هرگز به `stdout` ننویسید زیرا برای پیام‌های MCP رزرو شده است
- مطمئن شوید همه پیام‌های JSON-RPC جدا شده با خطوط جدید هستند
- ابتدا با ابزارهای ساده تست کنید قبل از افزودن عملکرد پیچیده
- از Inspector برای تایید فرمت پیام‌ها استفاده کنید

## مصرف سرور stdio شما در VS Code

پس از ساخت سرور stdio MCP، می‌توانید آن را با VS Code ادغام کنید تا با Claude یا سایر کلاینت‌های سازگار MCP استفاده شود.

### پیکربندی

۱. **یک فایل پیکربندی MCP بسازید** در `%APPDATA%\Claude\claude_desktop_config.json` (ویندوز) یا `~/Library/Application Support/Claude/claude_desktop_config.json` (مک):

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

۲. **Claude را ریستارت کنید**: برنامه Claude را ببندید و دوباره باز کنید تا پیکربندی جدید سرور بارگذاری شود.

۳. **اتصال را تست کنید**: یک گفتگو با Claude شروع کنید و سعی کنید از ابزارهای سرور خود استفاده کنید:
   - "می‌توانی با استفاده از ابزار greeting به من سلام کنی؟"
   - "مجموع ۱۵ و ۲۷ را محاسبه کن"
   - "اطلاعات سرور چیست؟"

### نمونه سرور stdio در TypeScript

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

### نمونه سرور stdio در .NET

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

در این درس به‌روزشده، یاد گرفتید چگونه:

- سرورهای MCP را با استفاده از ترابری **stdio** بسازید (رویکرد توصیه‌شده)
- دلیل منسوخ شدن ترابری SSE و جایگزینی آن با stdio و HTTP قابل پخش را بفهمید
- ابزارهایی بسازید که کلاینت‌های MCP بتوانند آن‌ها را فراخوانی کنند
- سرور خود را با MCP Inspector اشکال‌زدایی کنید
- سرور stdio خود را با VS Code و Claude ادغام کنید

ترابری stdio روشی ساده‌تر، امن‌تر و با عملکرد بهتر برای ساخت سرورهای MCP نسبت به رویکرد منسوخ SSE ارائه می‌دهد. این ترابری توصیه‌شده برای بیشتر پیاده‌سازی‌های سرور MCP طبق مشخصات نسخه ۲۰۲۵-۰۶-۱۸ است.

### .NET

۱. اجازه دهید ابتدا چند ابزار بسازیم، برای این کار فایلی به نام *Tools.cs* با محتوای زیر ایجاد می‌کنیم:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## تمرین: تست سرور stdio شما

اکنون که سرور stdio خود را ساختید، بیایید آن را تست کنیم تا مطمئن شویم درست کار می‌کند.

### پیش‌نیازها

1. اطمینان حاصل کنید MCP Inspector نصب شده است:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

۲. کد سرور شما ذخیره شده باشد (مثلاً `server.py`)

### تست با Inspector

1. **Inspector را با سرور خود راه‌اندازی کنید**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

۲. **رابط وب را باز کنید**: Inspector یک پنجره مرورگر باز می‌کند که قابلیت‌های سرور شما را نشان می‌دهد.

۳. **ابزارها را تست کنید**:
   - ابزار `get_greeting` را با نام‌های مختلف امتحان کنید
   - ابزار `calculate_sum` را با اعداد مختلف تست کنید
   - ابزار `get_server_info` را برای مشاهده متادیتای سرور فراخوانی کنید

۴. **نظارت بر ارتباطات**: Inspector پیام‌های JSON-RPC بین کلاینت و سرور را نمایش می‌دهد.

### آنچه باید ببینید

وقتی سرور شما به درستی شروع شده باشد، باید ببینید:
- قابلیت‌های سرور در Inspector لیست شده‌اند
- ابزارها برای تست در دسترس هستند
- تبادل موفق پیام‌های JSON-RPC
- پاسخ ابزارها در رابط نمایش داده می‌شود

### مشکلات رایج و راه‌حل‌ها

**سرور شروع نمی‌شود:**
- بررسی کنید همه وابستگی‌ها نصب شده باشند: `pip install mcp`
- سینتکس و تورفتگی پایتون را بررسی کنید
- پیام‌های خطا در کنسول را نگاه کنید

**ابزارها نمایش داده نمی‌شوند:**
- مطمئن شوید دکوراتورهای `@server.tool()` وجود دارند
- بررسی کنید توابع ابزار قبل از `main()` تعریف شده باشند
- اطمینان حاصل کنید سرور به درستی پیکربندی شده باشد

**مشکل اتصال:**
- مطمئن شوید سرور به درستی از ترابری stdio استفاده می‌کند
- چک کنید فرایندهای دیگری تداخل ندارند
- سینتکس دستور Inspector را بررسی کنید

## تمرین

سعی کنید سرور خود را با قابلیت‌های بیشتر توسعه دهید. به [این صفحه](https://api.chucknorris.io/) مراجعه کنید تا مثلاً ابزاری بسازید که یک API را فراخوانی می‌کند. خودتان تصمیم بگیرید سرور چگونه باشد. خوش بگذرد :)

## راه‌حل

[راه‌حل](./solution/README.md) اینجا یک راه‌حل احتمالی با کد کارامد وجود دارد.

## نکات کلیدی

نکات کلیدی این فصل عبارتند از:

- ترابری stdio مکانیزم توصیه‌شده برای سرورهای MCP محلی است.
- ترابری stdio امکان برقراری ارتباط بدون مشکل بین سرورها و کلاینت‌ها را از طریق جریان‌های ورودی و خروجی استاندارد فراهم می‌کند.
- می‌توانید از Inspector و Visual Studio Code برای مصرف مستقیم سرورهای stdio استفاده کنید که اشکال‌زدایی و ادغام را ساده می‌کند.

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)

## منابع اضافی

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## گام بعدی

## مراحل بعدی

اکنون که یاد گرفته‌اید چگونه سرورهای MCP را با ترابری stdio بسازید، می‌توانید موضوعات پیشرفته‌تر را کشف کنید:

- **مرحله بعد**: [پخش HTTP با MCP (HTTP قابل پخش)](../06-http-streaming/README.md) - درباره مکانیزم ترابری دیگر برای سرورهای راه دور یاد بگیرید
- **پیشرفته**: [بهترین شیوه‌های امنیتی MCP](../../02-Security/README.md) - اجرای امنیت در سرورهای MCP خود
- **تولید**: [استراتژی‌های استقرار](../09-deployment/README.md) - استقرار سرورهای خود برای محیط تولید

## منابع اضافی

- [مشخصات MCP ۲۰۲۵-۰۶-۱۸](https://spec.modelcontextprotocol.io/specification/) - مشخصات رسمی
- [مستندات SDK MCP](https://github.com/modelcontextprotocol/sdk) - منابع SDK برای همه زبان‌ها
- [نمونه‌های جامعه](../../06-CommunityContributions/README.md) - نمونه‌های بیشتر سرور از جامعه کاربران

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم ترجمه‌ای دقیق ارائه دهیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوء تفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->