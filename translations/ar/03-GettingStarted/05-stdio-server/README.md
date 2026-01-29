# خادم MCP باستخدام stdio Transport

> **⚠️ تحديث مهم**: اعتبارًا من مواصفات MCP بتاريخ 2025-06-18، تم **إيقاف** النقل المستقل SSE (Server-Sent Events) واستبداله بنقل "Streamable HTTP". تحدد مواصفات MCP الحالية آليتين رئيسيتين للنقل:
> 1. **stdio** - الإدخال/الإخراج القياسي (موصى به للخوادم المحلية)
> 2. **Streamable HTTP** - للخوادم البعيدة التي قد تستخدم SSE داخليًا
>
> تم تحديث هذا الدرس للتركيز على **stdio transport**، وهو النهج الموصى به لمعظم تطبيقات خادم MCP.

يسمح stdio transport لخوادم MCP بالتواصل مع العملاء عبر تدفقات الإدخال والإخراج القياسية. هذه هي آلية النقل الأكثر استخدامًا والموصى بها في مواصفات MCP الحالية، حيث توفر طريقة بسيطة وفعالة لبناء خوادم MCP يمكن دمجها بسهولة مع تطبيقات العملاء المختلفة.

## نظرة عامة

يغطي هذا الدرس كيفية بناء واستهلاك خوادم MCP باستخدام stdio transport.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- بناء خادم MCP باستخدام stdio transport.
- تصحيح أخطاء خادم MCP باستخدام Inspector.
- استهلاك خادم MCP باستخدام Visual Studio Code.
- فهم آليات النقل الحالية لـ MCP ولماذا يُوصى باستخدام stdio.

## stdio Transport - كيف يعمل

stdio transport هو أحد نوعي النقل المدعومين في مواصفات MCP الحالية (2025-06-18). إليك كيف يعمل:

- **تواصل بسيط**: يقرأ الخادم رسائل JSON-RPC من الإدخال القياسي (`stdin`) ويرسل الرسائل إلى الإخراج القياسي (`stdout`).
- **قائم على العمليات**: يقوم العميل بتشغيل خادم MCP كعملية فرعية.
- **تنسيق الرسائل**: الرسائل هي طلبات JSON-RPC فردية أو إشعارات أو ردود، مفصولة بأسطر جديدة.
- **التسجيل**: يمكن للخادم كتابة سلاسل UTF-8 إلى الخطأ القياسي (`stderr`) لأغراض التسجيل.

### المتطلبات الرئيسية:
- يجب أن تكون الرسائل مفصولة بأسطر جديدة ولا تحتوي على أسطر جديدة مضمنة.
- يجب ألا يكتب الخادم أي شيء إلى `stdout` ليس رسالة MCP صالحة.
- يجب ألا يكتب العميل أي شيء إلى `stdin` الخاص بالخادم ليس رسالة MCP صالحة.

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

في الكود السابق:

- نقوم باستيراد `Server` و `StdioServerTransport` من MCP SDK.
- نقوم بإنشاء مثيل للخادم مع إعدادات وقدرات أساسية.

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

في الكود السابق:

- نقوم بإنشاء مثيل للخادم باستخدام MCP SDK.
- نحدد الأدوات باستخدام decorators.
- نستخدم مدير السياق stdio_server للتعامل مع النقل.

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

الفرق الرئيسي عن SSE هو أن خوادم stdio:

- لا تتطلب إعداد خادم ويب أو نقاط نهاية HTTP.
- يتم تشغيلها كعمليات فرعية بواسطة العميل.
- تتواصل عبر تدفقات stdin/stdout.
- أسهل في التنفيذ والتصحيح.

## تمرين: إنشاء خادم stdio

لإنشاء خادمنا، يجب أن نضع في اعتبارنا أمرين:

- نحتاج إلى استخدام خادم ويب لتوفير نقاط نهاية للاتصال والرسائل.

## مختبر: إنشاء خادم MCP stdio بسيط

في هذا المختبر، سنقوم بإنشاء خادم MCP بسيط باستخدام stdio transport الموصى به. سيقوم هذا الخادم بتوفير أدوات يمكن للعملاء استدعاؤها باستخدام بروتوكول Model Context القياسي.

### المتطلبات الأساسية

- Python 3.8 أو أحدث
- MCP Python SDK: `pip install mcp`
- فهم أساسي للبرمجة غير المتزامنة

لنبدأ بإنشاء أول خادم MCP stdio:

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

## الفروقات الرئيسية عن نهج SSE الموقوف

**Stdio Transport (المعيار الحالي):**
- نموذج عملية فرعية بسيط - يقوم العميل بتشغيل الخادم كعملية فرعية.
- التواصل عبر stdin/stdout باستخدام رسائل JSON-RPC.
- لا يتطلب إعداد خادم HTTP.
- أداء وأمان أفضل.
- أسهل في التصحيح والتطوير.

**SSE Transport (تم إيقافه اعتبارًا من MCP 2025-06-18):**
- يتطلب خادم HTTP مع نقاط نهاية SSE.
- إعداد أكثر تعقيدًا مع بنية تحتية لخادم ويب.
- اعتبارات أمان إضافية لنقاط نهاية HTTP.
- تم استبداله الآن بـ Streamable HTTP للسيناريوهات القائمة على الويب.

### إنشاء خادم باستخدام stdio transport

لإنشاء خادم stdio، نحتاج إلى:

1. **استيراد المكتبات المطلوبة** - نحتاج إلى مكونات خادم MCP وstdio transport.
2. **إنشاء مثيل للخادم** - تعريف الخادم مع قدراته.
3. **تحديد الأدوات** - إضافة الوظائف التي نريد توفيرها.
4. **إعداد النقل** - تكوين التواصل عبر stdio.
5. **تشغيل الخادم** - بدء تشغيل الخادم ومعالجة الرسائل.

لنقم ببناء هذا خطوة بخطوة:

### الخطوة 1: إنشاء خادم stdio أساسي

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

### الخطوة 2: إضافة المزيد من الأدوات

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

### الخطوة 3: تشغيل الخادم

احفظ الكود باسم `server.py` وقم بتشغيله من سطر الأوامر:

```bash
python server.py
```

سيبدأ الخادم وينتظر الإدخال من stdin. يتواصل باستخدام رسائل JSON-RPC عبر stdio transport.

### الخطوة 4: الاختبار باستخدام Inspector

يمكنك اختبار خادمك باستخدام MCP Inspector:

1. قم بتثبيت Inspector: `npx @modelcontextprotocol/inspector`
2. قم بتشغيل Inspector وأشر إلى خادمك.
3. اختبر الأدوات التي أنشأتها.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## تصحيح أخطاء خادم stdio الخاص بك

### باستخدام MCP Inspector

MCP Inspector هو أداة قيمة لتصحيح الأخطاء واختبار خوادم MCP. إليك كيفية استخدامه مع خادم stdio الخاص بك:

1. **تثبيت Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **تشغيل Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **اختبار خادمك**: يوفر Inspector واجهة ويب حيث يمكنك:
   - عرض قدرات الخادم.
   - اختبار الأدوات باستخدام معلمات مختلفة.
   - مراقبة رسائل JSON-RPC.
   - تصحيح مشاكل الاتصال.

### باستخدام VS Code

يمكنك أيضًا تصحيح أخطاء خادم MCP الخاص بك مباشرة في VS Code:

1. قم بإنشاء تكوين تشغيل في `.vscode/launch.json`:
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

2. قم بتعيين نقاط توقف في كود الخادم الخاص بك.
3. قم بتشغيل المصحح واختبر باستخدام Inspector.

### نصائح التصحيح الشائعة

- استخدم `stderr` للتسجيل - لا تكتب إلى `stdout` لأنه مخصص لرسائل MCP.
- تأكد من أن جميع رسائل JSON-RPC مفصولة بأسطر جديدة.
- اختبر باستخدام أدوات بسيطة أولاً قبل إضافة وظائف معقدة.
- استخدم Inspector للتحقق من تنسيقات الرسائل.

## استهلاك خادم stdio الخاص بك في VS Code

بمجرد إنشاء خادم MCP stdio الخاص بك، يمكنك دمجه مع VS Code لاستخدامه مع Claude أو العملاء الآخرين المتوافقين مع MCP.

### التكوين

1. **إنشاء ملف تكوين MCP** في `%APPDATA%\Claude\claude_desktop_config.json` (Windows) أو `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **إعادة تشغيل Claude**: أغلق وأعد فتح Claude لتحميل تكوين الخادم الجديد.

3. **اختبار الاتصال**: ابدأ محادثة مع Claude وجرب استخدام أدوات خادمك:
   - "هل يمكنك تحيتي باستخدام أداة التحية؟"
   - "احسب مجموع 15 و27"
   - "ما هي معلومات الخادم؟"

### مثال خادم stdio TypeScript

إليك مثال كامل لـ TypeScript كمرجع:

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

### مثال خادم stdio .NET

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

## الملخص

في هذا الدرس المحدث، تعلمت كيفية:

- بناء خوادم MCP باستخدام **stdio transport** (النهج الموصى به).
- فهم سبب إيقاف النقل SSE لصالح stdio وStreamable HTTP.
- إنشاء أدوات يمكن للعملاء استدعاؤها.
- تصحيح أخطاء خادمك باستخدام MCP Inspector.
- دمج خادم stdio الخاص بك مع VS Code وClaude.

يوفر stdio transport طريقة أبسط وأكثر أمانًا وأداءً لبناء خوادم MCP مقارنة بنهج SSE الموقوف. إنه النقل الموصى به لمعظم تطبيقات خادم MCP اعتبارًا من مواصفات 2025-06-18.

### .NET

1. لنقم بإنشاء بعض الأدوات أولاً، لهذا سنقوم بإنشاء ملف *Tools.cs* بالمحتوى التالي:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## تمرين: اختبار خادم stdio الخاص بك

الآن بعد أن قمت ببناء خادم stdio الخاص بك، دعنا نختبره للتأكد من أنه يعمل بشكل صحيح.

### المتطلبات الأساسية

1. تأكد من تثبيت MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. يجب أن يكون كود الخادم الخاص بك محفوظًا (على سبيل المثال، باسم `server.py`).

### الاختبار باستخدام Inspector

1. **ابدأ Inspector مع خادمك**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **افتح واجهة الويب**: سيفتح Inspector نافذة متصفح تعرض قدرات خادمك.

3. **اختبر الأدوات**: 
   - جرب أداة `get_greeting` بأسماء مختلفة.
   - اختبر أداة `calculate_sum` بأرقام متنوعة.
   - استدعِ أداة `get_server_info` لرؤية بيانات الخادم.

4. **راقب التواصل**: يعرض Inspector رسائل JSON-RPC المتبادلة بين العميل والخادم.

### ما يجب أن تراه

عندما يبدأ خادمك بشكل صحيح، يجب أن ترى:
- قدرات الخادم مدرجة في Inspector.
- الأدوات متاحة للاختبار.
- تبادل ناجح لرسائل JSON-RPC.
- استجابات الأدوات معروضة في الواجهة.

### المشاكل الشائعة والحلول

**الخادم لا يبدأ:**
- تحقق من تثبيت جميع التبعيات: `pip install mcp`.
- تأكد من صحة بناء جملة Python والمسافة البادئة.
- ابحث عن رسائل الخطأ في وحدة التحكم.

**الأدوات لا تظهر:**
- تأكد من وجود `@server.tool()` decorators.
- تحقق من تعريف وظائف الأدوات قبل `main()`.
- تأكد من تكوين الخادم بشكل صحيح.

**مشاكل الاتصال:**
- تأكد من أن الخادم يستخدم stdio transport بشكل صحيح.
- تحقق من عدم تدخل عمليات أخرى.
- تحقق من بناء جملة أمر Inspector.

## المهمة

حاول بناء خادمك بمزيد من القدرات. راجع [هذه الصفحة](https://api.chucknorris.io/) لإضافة أداة تستدعي API، على سبيل المثال. قرر كيف يجب أن يبدو الخادم. استمتع :)

## الحل

[الحل](./solution/README.md) إليك حل ممكن مع كود يعمل.

## النقاط الرئيسية

النقاط الرئيسية من هذا الفصل هي:

- stdio transport هو الآلية الموصى بها للخوادم المحلية لـ MCP.
- يسمح stdio transport بالتواصل السلس بين خوادم MCP والعملاء باستخدام تدفقات الإدخال والإخراج القياسية.
- يمكنك استخدام كل من Inspector وVisual Studio Code لاستهلاك خوادم stdio مباشرة، مما يجعل التصحيح والدمج بسيطًا.

## أمثلة 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## موارد إضافية

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ماذا بعد

## الخطوات التالية

الآن بعد أن تعلمت كيفية بناء خوادم MCP باستخدام stdio transport، يمكنك استكشاف مواضيع أكثر تقدمًا:

- **التالي**: [HTTP Streaming مع MCP (Streamable HTTP)](../06-http-streaming/README.md) - تعلم عن آلية النقل الأخرى المدعومة للخوادم البعيدة.
- **متقدم**: [أفضل ممارسات أمان MCP](../../02-Security/README.md) - تنفيذ الأمان في خوادم MCP الخاصة بك.
- **الإنتاج**: [استراتيجيات النشر](../09-deployment/README.md) - نشر خوادمك للاستخدام الإنتاجي.

## موارد إضافية

- [مواصفات MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - المواصفات الرسمية.
- [وثائق MCP SDK](https://github.com/modelcontextprotocol/sdk) - مراجع SDK لجميع اللغات.
- [أمثلة المجتمع](../../06-CommunityContributions/README.md) - المزيد من أمثلة الخوادم من المجتمع.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.