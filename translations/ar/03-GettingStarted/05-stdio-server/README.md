# خادم MCP مع نقل stdio

> **⚠️ تحديث هام**: اعتبارًا من مواصفة MCP 2025-06-18، تم **إيقاف** نقل SSE المستقل (Server-Sent Events) واستبداله بنقل "HTTP قابل للبث". تحدد مواصفة MCP الحالية آليتين رئيسيتين للنقل:
> 1. **stdio** - الإدخال/الإخراج القياسي (موصى به للخوادم المحلية)
> 2. **HTTP قابل للبث** - للخوادم البعيدة التي قد تستخدم SSE داخليًا
>
> تم تحديث هذا الدرس للتركيز على **نقل stdio**، وهو النهج الموصى به لمعظم تطبيقات خوادم MCP.

يسمح نقل stdio لخوادم MCP بالتواصل مع العملاء عبر تدفقات الإدخال والإخراج القياسية. هذه هي آلية النقل الأكثر استخدامًا والمُوصى بها في مواصفة MCP الحالية، حيث توفر طريقة بسيطة وفعالة لبناء خوادم MCP يمكن دمجها بسهولة مع تطبيقات العملاء المختلفة.

## نظرة عامة

يغطي هذا الدرس كيفية بناء واستهلاك خوادم MCP باستخدام نقل stdio.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- بناء خادم MCP باستخدام نقل stdio.
- تصحيح أخطاء خادم MCP باستخدام Inspector.
- استهلاك خادم MCP باستخدام Visual Studio Code.
- فهم آليات النقل الحالية في MCP ولماذا يُنصح باستخدام stdio.

## نقل stdio - كيف يعمل

نقل stdio هو أحد نوعي النقل المدعومين في مواصفة MCP الحالية (2025-06-18). إليك كيفية عمله:

- **التواصل البسيط**: يقرأ الخادم رسائل JSON-RPC من الإدخال القياسي (`stdin`) ويرسل الرسائل إلى الإخراج القياسي (`stdout`).
- **قائم على العمليات**: يطلق العميل خادم MCP كعملية فرعية.
- **تنسيق الرسائل**: الرسائل هي طلبات JSON-RPC منفردة أو إشعارات أو استجابات، تُفصل بواسطة أسطر جديدة.
- **التسجيل**: يمكن للخادم كتابة سلاسل UTF-8 إلى الخطأ القياسي (`stderr`) لأغراض التسجيل.

### متطلبات أساسية:
- يجب أن تُفصل الرسائل بأسطر جديدة ولا يجب أن تحتوي على أسطر جديدة مضمنة
- لا يجب على الخادم كتابة أي شيء إلى `stdout` غير رسائل MCP صالحة
- لا يجب على العميل كتابة أي شيء إلى `stdin` الخاص بالخادم غير رسائل MCP صالحة

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

في الكود السابق:

- نستورد فئة `Server` و`StdioServerTransport` من SDK لـ MCP
- ننشئ مثيل خادم بإعدادات وقدرات أساسية
- ننشئ مثيل `StdioServerTransport` ونوصل الخادم به، مما يتيح التواصل عبر stdin/stdout

### بايثون

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# إنشاء نسخة من الخادم
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

في الكود السابق قمنا بـ:

- إنشاء مثيل خادم باستخدام SDK لـ MCP
- تعريف الأدوات باستخدام مزخرفات
- استخدام مدير السياق stdio_server للتعامل مع النقل

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

الفرق الرئيسي عن SSE هو أن خوادم stdio:

- لا تتطلب إعداد خادم ويب أو نقاط نهاية HTTP
- تُطلق كعمليات فرعية من قبل العميل
- تتواصل عبر تدفقات stdin/stdout
- أبسط في التنفيذ والتصحيح

## التمرين: إنشاء خادم stdio

لإنشاء خادمنا، يجب أن نضع شيئين في الاعتبار:

- نحتاج إلى استخدام خادم ويب لعرض نقاط نهاية للاتصال والرسائل.
## المختبر: إنشاء خادم MCP بسيط بنقل stdio

في هذا المختبر، سننشئ خادم MCP بسيط باستخدام النقل الموصى به stdio. سيعرض هذا الخادم أدوات يمكن للعملاء استدعاؤها باستخدام بروتوكول سياق النموذج القياسي.

### المتطلبات الأساسية

- بايثون 3.8 أو أحدث
- MCP Python SDK: `pip install mcp`
- فهم أساسي للبرمجة غير المتزامنة

لنبدأ بإنشاء أول خادم MCP لـ stdio لدينا:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# تكوين تسجيل الدخول
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# إنشاء الخادم
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
    # استخدام نقل stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## الفروق الرئيسية عن النهج المتوقف SSE

**نقل stdio (المعيار الحالي):**
- نموذج عملية فرعية بسيط - العميل يطلق الخادم كعملية فرعية
- التواصل عبر stdin/stdout باستخدام رسائل JSON-RPC
- لا حاجة لإعداد خادم HTTP
- أداء وأمان أفضل
- تصحيح وأسهل تطوير

**نقل SSE (تم إيقافه اعتبارًا من MCP 2025-06-18):**
- يحتاج إلى خادم HTTP مع نقاط نهاية SSE
- إعداد أكثر تعقيدًا مع بنية خادم الويب
- اعتبارات أمان إضافية لنقاط نهاية HTTP
- الآن تم استبداله بـ HTTP القابل للبث للحالات المعتمدة على الويب

### إنشاء خادم باستخدام نقل stdio

لإنشاء الخادم، نحتاج إلى:

1. **استيراد المكتبات المطلوبة** - نحتاج إلى مكونات خادم MCP ونقل stdio
2. **إنشاء مثيل خادم** - تحديد الخادم مع قدراته
3. **تعريف الأدوات** - إضافة الوظائف التي نريد عرضها
4. **إعداد النقل** - تهيئة التواصل عبر stdio
5. **تشغيل الخادم** - بدء الخادم والتعامل مع الرسائل

لننشئ ذلك خطوة بخطوة:

### الخطوة 1: إنشاء خادم stdio أساسي

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# تكوين التسجيل
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# إنشاء الخادم
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

احفظ الكود كـ `server.py` وشغله من سطر الأوامر:

```bash
python server.py
```

سيبدأ الخادم وينتظر الإدخال من stdin. يتواصل باستخدام رسائل JSON-RPC عبر نقل stdio.

### الخطوة 4: الاختبار باستخدام Inspector

يمكنك اختبار خادمك باستخدام MCP Inspector:

1. ثبّت Inspector: `npx @modelcontextprotocol/inspector`
2. شغل Inspector وأشر إلى خادمك
3. اختبر الأدوات التي أنشأتها

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## تصحيح خادم stdio الخاص بك

### استخدام MCP Inspector

MCP Inspector هو أداة قيمة لتصحيح واختبار خوادم MCP. إليك كيفية استخدامه مع خادم stdio الخاص بك:

1. **تثبيت Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **تشغيل Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **اختبار الخادم**: يوفر Inspector واجهة ويب حيث يمكنك:
   - عرض قدرات الخادم
   - اختبار الأدوات مع معلمات مختلفة
   - مراقبة رسائل JSON-RPC
   - تصحيح مشكلات الاتصال

### استخدام VS Code

يمكنك أيضًا تصحيح خادم MCP الخاص بك مباشرة في VS Code:

1. أنشئ تكوين تشغيل في `.vscode/launch.json`:
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

2. ضع نقاط توقف في كود الخادم
3. شغّل المصحح واختبر مع Inspector

### نصائح شائعة للتصحيح

- استخدم `stderr` للتسجيل - لا تكتب أبدًا إلى `stdout` فهو مخصص لرسائل MCP
- تأكد من أن جميع رسائل JSON-RPC مفصولة بأسطر جديدة
- اختبر الأدوات البسيطة أولاً قبل إضافة الوظائف المعقدة
- استخدم Inspector للتحقق من تنسيقات الرسائل

## استهلاك خادم stdio الخاص بك في VS Code

بعد بناء خادم MCP stdio، يمكنك دمجه مع VS Code لاستخدامه مع Claude أو أي عملاء متوافقين مع MCP.

### الإعداد

1. **أنشئ ملف إعداد MCP** في `%APPDATA%\Claude\claude_desktop_config.json` (ويندوز) أو `~/Library/Application Support/Claude/claude_desktop_config.json` (ماك):

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

2. **أعد تشغيل Claude**: أغلق وافتح Claude لتحميل إعداد الخادم الجديد.

3. **اختبر الاتصال**: ابدأ محادثة مع Claude وحاول استخدام أدوات خادمك:
   - "هل يمكنك تحيتي باستخدام أداة التحية؟"
   - "احسب مجموع 15 و 27"
   - "ما هي معلومات الخادم؟"

### مثال خادم stdio بـ TypeScript

إليك مثال كامل TypeScript للرجوع إليه:

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

// أضف أدوات
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

### مثال خادم stdio بـ .NET

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

## الملخص

في هذا الدرس المحدث، تعلمت كيف:

- تبني خوادم MCP باستخدام نقل **stdio** الحالي (النهج الموصى به)
- تفهم لماذا تم إيقاف نقل SSE لصالح stdio وHTTP القابل للبث
- تنشئ أدوات يمكن استدعاؤها من قبل عملاء MCP
- تصحح خادمك باستخدام MCP Inspector
- تدمج خادم stdio مع VS Code وClaude

يوفر نقل stdio طريقة أبسط وأكثر أمانًا وأداء لبناء خوادم MCP مقارنةً بنهج SSE المتوقف. إنه آلية النقل الموصى بها لمعظم تطبيقات خادم MCP اعتبارًا من مواصفة 2025-06-18.

### .NET

1. دعونا ننشئ بعض الأدوات أولاً، لهذا سننشئ ملف *Tools.cs* بالمحتوى التالي:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## التمرين: اختبار خادم stdio الخاص بك

الآن بعد أن أنشأت خادم stdio الخاص بك، دعنا نختبره للتأكد من عمله بشكل صحيح.

### المتطلبات الأساسية

1. تأكد من تثبيت MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. يجب أن يكون كود الخادم محفوظًا (مثل `server.py`)

### الاختبار باستخدام Inspector

1. **ابدأ Inspector مع خادمك**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **افتح واجهة الويب**: سيفتح Inspector نافذة متصفح تعرض قدرات الخادم.

3. **اختبر الأدوات**: 
   - جرب أداة `get_greeting` مع أسماء مختلفة
   - اختبر أداة `calculate_sum` مع أرقام متنوعة
   - استدعِ أداة `get_server_info` لرؤية بيانات تعريف الخادم

4. **راقب الاتصال**: يعرض Inspector رسائل JSON-RPC المتبادلة بين العميل والخادم.

### ما يجب أن تراه

عندما يبدأ خادمك بشكل صحيح، سترى:
- قائمة قدرات الخادم في Inspector
- الأدوات المتاحة للاختبار
- تبادلات رسائل JSON-RPC الناجحة
- استجابات الأدوات معروضة في الواجهة

### المشاكل الشائعة وحلولها

**الخادم لا يبدأ:**
- تحقق من تثبيت كل الاعتمادات: `pip install mcp`
- راجع بناء جملة واختصارات بايثون
- ابحث عن رسائل الخطأ في الطرفية

**عدم ظهور الأدوات:**
- تأكد من وجود مزخرفات `@server.tool()`
- تحقق من تعريف وظائف الأدوات قبل `main()`
- تأكد من تكوين الخادم بشكل صحيح

**مشكلات الاتصال:**
- تحقق من استخدام نقل stdio بشكل صحيح في الخادم
- تحقق من عدم وجود عمليات أخرى تتداخل
- تحقق من صحة بناء جملة أوامر Inspector

## المهمة

حاول بناء خادمك مع المزيد من القدرات. راجع [هذه الصفحة](https://api.chucknorris.io/) لإضافة أداة تستدعي API، أنت تقرر شكل الخادم. استمتع :)

## الحل

[الحل](./solution/README.md) هنا حل ممكن مع كود يعمل.

## النقاط الرئيسية

النقاط الرئيسية من هذا الفصل هي:

- نقل stdio هو الآلية الموصى بها لخوادم MCP المحلية.
- يسمح نقل stdio بتواصل سلس بين خوادم MCP والعملاء باستخدام تدفقات الإدخال والإخراج القياسية.
- يمكنك استخدام كل من Inspector وVisual Studio Code لاستهلاك خوادم stdio مباشرة، مما يجعل التصحيح والتكامل بسيطًا.

## عينات

- [حاسبة جافا](../samples/java/calculator/README.md)
- [حاسبة .Net](../../../../03-GettingStarted/samples/csharp)
- [حاسبة جافا سكريبت](../samples/javascript/README.md)
- [حاسبة TypeScript](../samples/typescript/README.md)
- [حاسبة بايثون](../../../../03-GettingStarted/samples/python)

## موارد إضافية

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ما التالي

## الخطوات التالية

الآن بعد أن تعلمت كيفية بناء خوادم MCP باستخدام نقل stdio، يمكنك استكشاف مواضيع متقدمة أكثر:

- **التالي**: [البث عبر HTTP مع MCP (HTTP القابل للبث)](../06-http-streaming/README.md) - تعرف على آلية النقل الأخرى المدعومة للخوادم البعيدة
- **متقدم**: [أفضل ممارسات أمان MCP](../../02-Security/README.md) - نفذ الأمان في خوادم MCP الخاصة بك
- **للإنتاج**: [استراتيجيات النشر](../09-deployment/README.md) - نشر خوادمك للاستخدام في الإنتاج

## موارد إضافية

- [مواصفة MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - المواصفة الرسمية
- [توثيق MCP SDK](https://github.com/modelcontextprotocol/sdk) - مراجع SDK لكافة اللغات
- [أمثلة المجتمع](../../06-CommunityContributions/README.md) - المزيد من أمثلة الخوادم من المجتمع

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحرجة، يوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->