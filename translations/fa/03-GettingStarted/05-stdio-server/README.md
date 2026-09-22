# سرور MCP با حمل و نقل stdio

> **⚠️ به‌روزرسانی مهم**: از تاریخ مشخصات MCP 2025-06-18، حمل و نقل SSE مستقل (Server-Sent Events) **منسوخ شده** و جایگزین آن حمل و نقل "Streamable HTTP" شده است. مشخصات فعلی MCP دو مکانیزم حمل و نقل اصلی را تعریف می‌کند:
> 1. **stdio** - ورودی/خروجی استاندارد (پیشنهادی برای سرورهای محلی)
> 2. **Streamable HTTP** - برای سرورهای دور که ممکن است از SSE به صورت داخلی استفاده کنند
>
> این درس برای تمرکز روی **حمل و نقل stdio** به‌روزرسانی شده است، که روش پیشنهادی برای اکثر پیاده‌سازی‌های سرور MCP است.

حمل و نقل stdio به سرورهای MCP اجازه می‌دهد تا از طریق جریان‌های ورودی و خروجی استاندارد با کلاینت‌ها ارتباط برقرار کنند. این محبوب‌ترین و توصیه‌شده‌ترین مکانیزم حمل و نقل در مشخصات فعلی MCP است که راه ساده و کارآمدی برای ساخت سرورهای MCP ارائه می‌دهد که می‌توانند به راحتی با برنامه‌های مختلف کلاینت ادغام شوند.

## مرور کلی

این درس پوشش می‌دهد که چگونه سرورهای MCP را با استفاده از حمل و نقل stdio بسازیم و مصرف کنیم.

## اهداف یادگیری

تا پایان این درس، شما قادر خواهید بود:

- ساخت یک سرور MCP با استفاده از حمل و نقل stdio.
- اشکال‌زدایی یک سرور MCP با استفاده از Inspector.
- مصرف یک سرور MCP با استفاده از Visual Studio Code.
- درک مکانیزم‌های حمل و نقل فعلی MCP و چرا stdio توصیه می‌شود.


## حمل و نقل stdio - چگونه کار می‌کند

حمل و نقل stdio یکی از دو حمل و نقل استاندارد در مشخصات MCP
`2026-07-28` است. این‌گونه کار می‌کند:

- **ارتباط ساده**: سرور پیام‌های JSON-RPC را از ورودی استاندارد (`stdin`) می‌خواند و پیام‌ها را به خروجی استاندارد (`stdout`) ارسال می‌کند.
- **مبتنی بر فرآیند**: کلاینت سرور MCP را به عنوان یک فرایند فرعی راه‌اندازی می‌کند.
- **فرمت پیام**: پیام‌ها درخواست‌ها، اطلاع‌رسانی‌ها یا پاسخ‌های JSON-RPC فردی هستند که با خطوط جدید جدا شده‌اند.
- **ثبت وقایع**: سرور می‌تواند برای ثبت وقایع رشته‌های UTF-8 را به خطای استاندارد (`stderr`) بنویسد.

### الزامات کلیدی:
- پیام‌ها باید با خطوط جدید جدا شده باشند و نباید شامل خطوط جدید تو در تو باشند
- سرور نباید چیزی به `stdout` بنویسد که پیام MCP معتبر نباشد
- کلاینت نباید چیزی به `stdin` سرور بنویسد که پیام MCP معتبر نباشد

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
- یک نمونه سرور با پیکربندی و قابلیت‌های پایه می‌سازیم
- یک نمونه `StdioServerTransport` ایجاد کرده و سرور را به آن متصل می‌کنیم تا ارتباط از طریق stdin/stdout فعال شود

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

- با استفاده از SDK MCP یک نمونه سرور ایجاد می‌کنیم
- با دکوراتورها ابزارها را تعریف می‌کنیم
- از مدیریت زمینه stdio_server برای حمل و نقل استفاده می‌کنیم

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

- نیاز به راه‌اندازی سرور وب یا نقاط پایان HTTP ندارند
- توسط کلاینت به صورت فرایند فرعی راه‌اندازی می‌شوند
- از طریق جریان‌های stdin/stdout ارتباط برقرار می‌کنند
- پیاده‌سازی و اشکال‌زدایی ساده‌تری دارند

## تمرین: ایجاد یک سرور stdio

برای ایجاد سرور خود باید دو نکته را در نظر داشته باشیم:

- باید از یک سرور وب برای نمایش نقاط اتصال و پیام‌ها استفاده کنیم.
## آزمایشگاه: ایجاد یک سرور ساده MCP stdio

در این آزمایشگاه، یک سرور ساده MCP با استفاده از حمل و نقل stdio پیشنهادی ایجاد می‌کنیم. این سرور ابزارهایی را ارائه می‌دهد که کلاینت‌ها می‌توانند با استفاده از پروتکل مدل کانتکست استاندارد فراخوانی کنند.

### پیش‌نیازها

- پایتون 3.8 یا بالاتر
- SDK پایتون MCP: `pip install mcp`
- درک پایه‌ای از برنامه‌نویسی ناهمگام

بیایید با ایجاد اولین سرور MCP stdio خود شروع کنیم:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# تنظیم لاگ‌گیری
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

## تفاوت‌های کلیدی با روش SSE منسوخ شده

**حمل و نقل Stdio (استاندارد فعلی):**
- مدل فرایند فرعی ساده - کلاینت سرور را به عنوان فرآیند فرزند اجرا می‌کند
- ارتباط از طریق stdin/stdout با استفاده از پیام‌های JSON-RPC
- نیازی به راه‌اندازی سرور HTTP نیست
- عملکرد و امنیت بهتر
- اشکال‌زدایی و توسعه آسان‌تر

**حمل و نقل SSE (از 2025-06-18 منسوخ شده):**
- نیاز به سرور HTTP با نقاط پایان SSE
- راه‌اندازی پیچیده‌تر با زیرساخت سرور وب
- ملاحظات امنیتی اضافی برای نقاط پایان HTTP
- اکنون جایگزین شده با Streamable HTTP برای سناریوهای مبتنی بر وب

### ایجاد سرور با حمل و نقل stdio

برای ایجاد سرور stdio ما باید:

1. **وارد کردن کتابخانه‌های مورد نیاز** - باید اجزای سرور MCP و حمل و نقل stdio را وارد کنیم
2. **ایجاد یک نمونه سرور** - سرور را با قابلیت‌هایش تعریف کنیم
3. **تعریف ابزارها** - تابعیت‌هایی را که می‌خواهیم ارائه دهیم اضافه کنیم
4. **راه‌اندازی حمل و نقل** - تنظیم ارتباط stdio
5. **اجرای سرور** - سرور را اجرا کنیم و پیام‌ها را مدیریت کنیم

بیایید قدم به قدم این را بسازیم:

### مرحله 1: ایجاد یک سرور stdio پایه

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# پیکربندی لاگ‌ها
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# سرور را ایجاد کنید
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

### مرحله 2: اضافه کردن ابزارهای بیشتر

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

کد را به نام `server.py` ذخیره کنید و از خط فرمان آن را اجرا کنید:

```bash
python server.py
```

سرور شروع به کار می‌کند و منتظر ورودی از stdin می‌ماند. ارتباط با استفاده از پیام‌های JSON-RPC بر روی حمل و نقل stdio انجام می‌شود.

### مرحله 4: تست با Inspector

می‌توانید سرور خود را با استفاده از MCP Inspector تست کنید:

1. Inspector را نصب کنید: `npx @modelcontextprotocol/inspector`
2. Inspector را اجرا کنید و به سرور خود اشاره دهید
3. ابزارهایی که ساخته‌اید را تست کنید

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## اشکال‌زدایی سرور stdio شما

### استفاده از MCP Inspector

MCP Inspector ابزاری ارزشمند برای اشکال‌زدایی و تست سرورهای MCP است. در اینجا نحوه استفاده از آن با سرور stdio شما آمده است:

1. **نصب Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **اجرای Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **تست سرور خود**: Inspector یک رابط وب فراهم می‌کند که در آن می‌توانید:
   - قابلیت‌های سرور را مشاهده کنید
   - ابزارها را با پارامترهای مختلف امتحان کنید
   - پیام‌های JSON-RPC را پایش کنید
   - مشکلات اتصال را اشکال‌زدایی کنید

### استفاده از VS Code

می‌توانید سرور MCP خود را مستقیماً در VS Code اشکال‌زدایی کنید:

1. یک پیکربندی شروع در `.vscode/launch.json` بسازید:
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

2. نقاط توقف در کد سرور خود تنظیم کنید
3. اشکال‌زدایی را اجرا کنید و با Inspector تست کنید

### نکات رایج در اشکال‌زدایی

- از `stderr` برای لاگ‌نویسی استفاده کنید - هرگز به `stdout` چیزی ننویسید چون مخصوص پیام‌های MCP است
- اطمینان حاصل کنید که همه پیام‌های JSON-RPC با خط جدید جدا شده باشند
- اول با ابزارهای ساده تست کنید قبل از اضافه کردن عملکردهای پیچیده‌تر
- از Inspector برای بررسی فرمت پیام‌ها استفاده کنید

## مصرف سرور stdio شما در VS Code

پس از ساخت سرور MCP stdio خود، می‌توانید آن را با VS Code ادغام کنید تا با Claude یا دیگر کلاینت‌های سازگار MCP استفاده شود.

### پیکربندی

1. **یک فایل پیکربندی MCP** در `%APPDATA%\Claude\claude_desktop_config.json` (ویندوز) یا `~/Library/Application Support/Claude/claude_desktop_config.json` (مک) ایجاد کنید:

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

2. **ری‌استارت Claude**: Claude را ببندید و دوباره باز کنید تا پیکربندی جدید بارگذاری شود.

3. **اتصال را تست کنید**: گفتگو را با Claude شروع کنید و سعی کنید از ابزارهای سرور استفاده کنید:
   - "می‌توانی با ابزار خوش‌آمدگویی به من سلام کنی؟"
   - "حاصل جمع ۱۵ و ۲۷ را محاسبه کن"
   - "وضعیت سرور چیست؟"

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

در این درس به‌روزشده، شما یاد گرفتید که چگونه:

- سرورهای MCP را با استفاده از **حمل و نقل stdio** فعلی بسازید (روش پیشنهادی)
- درک کنید چرا حمل و نقل SSE به نفع stdio و Streamable HTTP منسوخ شده است
- ابزارهایی بسازید که کلاینت‌های MCP بتوانند آنها را فراخوانی کنند
- سرور خود را با استفاده از MCP Inspector اشکال‌زدایی کنید
- سرور stdio خود را با VS Code و Claude ادغام کنید

حمل و نقل stdio راهی ساده‌تر، امن‌تر و با عملکرد بهتر برای ساخت سرورهای MCP نسبت به روش منسوخ SSE ارائه می‌دهد. این روش برای اکثر پیاده‌سازی‌های سرور MCP از تاریخ 2025-06-18 توصیه شده است.


### .NET

1. ابتدا برخی ابزار بسازیم، برای این کار فایلی به نام *Tools.cs* با محتوای زیر ایجاد می‌کنیم:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## تمرین: تست سرور stdio شما

اکنون که سرور stdio خود را ساخته‌اید، بیایید آن را تست کنیم تا مطمئن شویم به درستی کار می‌کند.

### پیش‌نیازها

1. مطمئن شوید MCP Inspector نصب شده است:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. کد سرور شما باید ذخیره شده باشد (مثلاً به نام `server.py`)

### تست با Inspector

1. **Inspector را با سرور خود اجرا کنید**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **رابط وب را باز کنید**: Inspector یک پنجره مرورگر باز می‌کند که قابلیت‌های سرور شما را نشان می‌دهد.

3. **ابزارها را تست کنید**: 
   - ابزار `get_greeting` را با نام‌های مختلف امتحان کنید
   - ابزار `calculate_sum` را با اعداد مختلف تست کنید
   - ابزار `get_server_info` را برای دیدن متاداده سرور فراخوانی کنید

4. **تماس‌های ارتباطی را پایش کنید**: Inspector پیام‌های JSON-RPC مبادله‌شده بین کلاینت و سرور را نشان می‌دهد.

### آنچه باید ببینید

زمانی که سرور شما به درستی شروع شود، باید موارد زیر را مشاهده کنید:
- قابلیت‌های سرور که در Inspector فهرست شده‌اند
- ابزارهای قابل استفاده برای تست
- تبادل موفق پیام‌های JSON-RPC
- نمایش پاسخ ابزارها در رابط کاربری

### مشکلات رایج و راه‌حل‌ها

**سرور اجرا نمی‌شود:**
- بررسی کنید که تمام وابستگی‌ها نصب شده باشند: `pip install mcp`
- سینتکس و تو رفتگی پایتون را بررسی کنید
- به دنبال پیام‌های خطا در کنسول بگردید

**ابزارها ظاهر نمی‌شوند:**
- اطمینان حاصل کنید که دکوراتورهای `@server.tool()` وجود دارند
- بررسی کنید که توابع ابزار قبل از `main()` تعریف شده باشند
- مطمئن شوید سرور به درستی پیکربندی شده است

**مشکلات اتصال:**
- مطمئن شوید سرور به درستی از حمل و نقل stdio استفاده می‌کند
- بررسی کنید که فرایندهای دیگری مزاحم نباشند
- سینتکس دستورهای Inspector را بررسی کنید

## تمرین

تلاش کنید سرور خود را با قابلیت‌های بیشتر بسازید. به [این صفحه](https://api.chucknorris.io/) نگاه کنید تا مثلاً ابزاری بسازید که یک API را فراخوانی کند. خودتان تصمیم بگیرید سرور چگونه باشد. خوش بگذرد :)
## راه‌حل

[راه‌حل](./solution/README.md) در اینجا یک راه‌حل ممکن با کد کاری آمده است.

## نکات کلیدی

نکات کلیدی این بخش عبارتند از:

- حمل و نقل stdio مکانیزم پیشنهادی برای سرورهای محلی MCP است.
- حمل و نقل stdio اجازه ارتباط بی‌وقفه بین سرورهای MCP و کلاینت‌ها را با استفاده از ورودی و خروجی استاندارد می‌دهد.
- شما می‌توانید هم از Inspector و هم از Visual Studio Code برای مصرف سرورهای stdio مستقیماً استفاده کنید، که اشکال‌زدایی و ادغام را ساده می‌کند.

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)

## منابع اضافی

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ادامه مسیر

## مراحل بعدی

اکنون که یاد گرفته‌اید چگونه سرورهای MCP را با حمل و نقل stdio بسازید، می‌توانید موضوعات پیشرفته‌تر را کاوش کنید:

- **بعدی**: [پخش HTTP با MCP (Streamable HTTP)](../06-http-streaming/README.md) - درباره مکانیزم حمل و نقل پشتیبانی‌شده دیگر برای سرورهای دور بیاموزید
- **پیشرفته**: [بهترین شیوه‌های امنیتی MCP](../../02-Security/README.md) - امنیت را در سرورهای MCP خود پیاده‌سازی کنید
- **تولید**: [استراتژی‌های استقرار](../09-deployment/README.md) - سرورهای خود را برای استفاده در تولید مستقر کنید

## منابع اضافی

- [مشخصات MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - مشخصات فعلی
- [مستندات SDK MCP](https://github.com/modelcontextprotocol/sdk) - منابع SDK برای تمام زبان‌ها
- [نمونه‌های جامعه](../../06-CommunityContributions/README.md) - نمونه‌های بیشتر سرور از جامعه

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->