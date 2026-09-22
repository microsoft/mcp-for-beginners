# خادم MCP مع نقل stdio

> **⚠️ تحديث مهم**: اعتبارًا من مواصفة MCP بتاريخ 2025-06-18، تم **إيقاف** النقل المستقل SSE (Server-Sent Events) وتم استبداله بنقل "HTTP القابل للبث". تحدد مواصفة MCP الحالية آليتين رئيسيتين للنقل:
> 1. **stdio** - الدخل/الإخراج القياسي (موصى به للخوادم المحلية)
> 2. **HTTP القابل للبث** - للخوادم البعيدة التي قد تستخدم SSE داخليًا
>
> تم تحديث هذا الدرس للتركيز على **نقل stdio**، وهو النهج الموصى به لمعظم تطبيقات خوادم MCP.

يسمح نقل stdio لخوادم MCP بالتواصل مع العملاء من خلال تدفقات الدخل والإخراج القياسية. هذا هو آلية النقل الأكثر استخدامًا وتوصية في مواصفة MCP الحالية، حيث يوفر طريقة بسيطة وفعالة لبناء خوادم MCP يمكن دمجها بسهولة مع تطبيقات العملاء المختلفة.

## نظرة عامة

يغطي هذا الدرس كيفية بناء واستهلاك خوادم MCP باستخدام نقل stdio.

## الأهداف التعليمية

بنهاية هذا الدرس، ستكون قادرًا على:

- بناء خادم MCP باستخدام نقل stdio.
- تصحيح أخطاء خادم MCP باستخدام Inspector.
- استهلاك خادم MCP باستخدام Visual Studio Code.
- فهم آليات النقل الحالية في MCP ولماذا يُوصى باستخدام stdio.


## نقل stdio - كيف يعمل

نقل stdio هو واحد من آليتين قياسيتين في مواصفة MCP
`2026-07-28`. هكذا يعمل:

- **اتصال بسيط**: يقرأ الخادم رسائل JSON-RPC من الدخل القياسي (`stdin`) ويرسل الرسائل إلى الإخراج القياسي (`stdout`).
- **معتمد على العمليات**: يطلق العميل خادم MCP كعملية فرعية.
- **صيغة الرسائل**: الرسائل تكون طلبات، إشعارات، أو ردود JSON-RPC منفصلة عن بعضها بخطوط جديدة.
- **التسجيل**: يمكن للخادم كتابة سلاسل UTF-8 إلى الخطأ القياسي (`stderr`) لأغراض التسجيل.

### المتطلبات الأساسية:
- يجب أن تكون الرسائل مفصولة بخطوط جديدة ويجب ألا تحتوي على خطوط جديدة داخلية
- يجب ألا يكتب الخادم أي شيء في `stdout` غير رسالة MCP صالحة
- يجب ألا يكتب العميل أي شيء إلى `stdin` الخاص بالخادم غير رسالة MCP صالحة

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

- نستورد فئة `Server` و `StdioServerTransport` من حزمة MCP SDK
- ننشئ مثالًا لخادم مع تكوين وقدرات أساسية
- ننشئ مثيلًا لـ `StdioServerTransport` ونربط الخادم به، مما يتيح التواصل عبر stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# إنشاء مثيل الخادم
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

- ننشئ مثال خادم باستخدام MCP SDK
- نُعرّف الأدوات باستخدام الزخارف
- نستخدم مدير السياق stdio_server لمعالجة النقل

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
- يتم إطلاقها كعمليات فرعية بواسطة العميل
- تتواصل عبر تدفقات stdin/stdout
- أبسط في التنفيذ والتصحيح

## تمرين: إنشاء خادم stdio

لإنشاء خادمنا، نحتاج إلى تذكر أمرين:

- نحتاج إلى استخدام خادم ويب لعرض نقاط نهاية للاتصال والرسائل.
## مختبر: إنشاء خادم MCP بسيط باستخدام stdio

في هذا المختبر، سننشئ خادم MCP بسيط باستخدام نقل stdio الموصى به. سيعرض هذا الخادم أدوات يمكن للعملاء استدعاؤها باستخدام بروتوكول نموذج السياق القياسي.

### المتطلبات الأساسية

- Python 3.8 أو أحدث
- حزمة MCP Python SDK: `pip install mcp`
- فهم أساسي للبرمجة غير المتزامنة

لنبدأ بإنشاء أول خادم stdio MCP لدينا:

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

## الاختلافات الرئيسية عن النهج القديم SSE

**نقل stdio (المعيار الحالي):**
- نموذج بسيط للعملية الفرعية - العميل يشغل الخادم كعملية طفل
- التواصل عبر stdin/stdout باستخدام رسائل JSON-RPC
- لا حاجة لإعداد خادم HTTP
- أداء وأمان أفضل
- تصحيح وتطوير أسهل

**نقل SSE (تم إيقافه اعتبارًا من MCP 2025-06-18):**
- يتطلب خادم HTTP مع نقاط نهاية SSE
- إعداد أكثر تعقيدًا مع بنية خادم الويب
- اعتبارات أمان إضافية لنقاط نهاية HTTP
- تم استبداله الآن بـ HTTP القابل للبث للسيناريوهات القائمة على الويب

### إنشاء خادم باستخدام نقل stdio

لإنشاء خادم stdio الخاص بنا، نحتاج إلى:

1. **استيراد المكتبات المطلوبة** - نحتاج مكونات خادم MCP ونقل stdio
2. **إنشاء نسخة من الخادم** - تعيين الخادم مع قدراته
3. **تعريف الأدوات** - إضافة الوظائف التي نريد عرضها
4. **إعداد النقل** - تهيئة اتصال stdio
5. **تشغيل الخادم** - بدء الخادم ومعالجة الرسائل

لنبني هذا خطوة بخطوة:

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

احفظ الكود باسم `server.py` وشغله من سطر الأوامر:

```bash
python server.py
```

سيبدأ الخادم وينتظر الإدخال من stdin. يتواصل باستخدام رسائل JSON-RPC عبر نقل stdio.

### الخطوة 4: الاختبار باستخدام Inspector

يمكنك اختبار خادمك باستخدام MCP Inspector:

1. قم بتنصيب Inspector: `npx @modelcontextprotocol/inspector`
2. شغّل Inspector ووجهه إلى خادمك
3. اختبر الأدوات التي أنشأتها

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## تصحيح خادم stdio الخاص بك

### استخدام MCP Inspector

MCP Inspector هو أداة قيمة لتصحيح واختبار خوادم MCP. هكذا تستخدمه مع خادم stdio الخاص بك:

1. **تنصيب Inspector**:
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
   - تصحيح مشاكل الاتصال

### استخدام VS Code

يمكنك أيضًا تصحيح خادم MCP الخاص بك مباشرةً في VS Code:

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

2. حدد نقاط توقف في كود الخادم
3. شغّل المصحح واختبر باستخدام Inspector

### نصائح شائعة للتصحيح

- استخدم `stderr` للتسجيل - لا تكتب أبدًا في `stdout` لأنه مخصص لرسائل MCP
- تأكد من أن جميع رسائل JSON-RPC مفصولة بخطوط جديدة
- ابدأ بالاختبار بأدوات بسيطة قبل إضافة وظائف معقدة
- استخدم Inspector للتحقق من صيغ الرسائل

## استهلاك خادم stdio في VS Code

بمجرد أن تبني خادم MCP stdio الخاص بك، يمكنك دمجه مع VS Code لاستخدامه مع Claude أو عملاء MCP متوافقين آخرين.

### التهيئة

1. **انشئ ملف تكوين MCP** في `%APPDATA%\Claude\claude_desktop_config.json` (ويندوز) أو في `~/Library/Application Support/Claude/claude_desktop_config.json` (ماك):

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

2. **أعد تشغيل Claude**: أغلق وأعد فتح Claude لتحميل تكوين الخادم الجديد.

3. **اختبر الاتصال**: ابدأ محادثة مع Claude وجرب استخدام أدوات خادمك:
   - "هل يمكنك تحيتي باستخدام أداة التحية؟"
   - "احسب مجموع 15 و27"
   - "ما هي معلومات الخادم؟"

### مثال خادم stdio بلغة TypeScript

إليك مثالًا كاملًا بلغة TypeScript للرجوع إليه:

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

### مثال خادم stdio بلغة .NET

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

## الخلاصة

في هذا الدرس المحدث، تعلمت كيف:

- تبني خوادم MCP باستخدام **نقل stdio** الحالي (النهج الموصى به)
- تفهم سبب إيقاف نقل SSE لصالح stdio وHTTP القابل للبث
- تنشئ أدوات يمكن للعملاء MCP استدعاؤها
- تصحح خادمك باستخدام MCP Inspector
- تدمج خادم stdio الخاص بك مع VS Code وClaude

يوفر نقل stdio طريقة أبسط، وأكثر أمانًا، وأكثر أداءً لبناء خوادم MCP مقارنة بالنهج القديم SSE. إنه النقل الموصى به لمعظم تطبيقات خوادم MCP حسب مواصفة 2025-06-18.


### .NET

1. لننشئ أولًا بعض الأدوات، لهذا سننشئ ملف *Tools.cs* بالمحتوى التالي:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## تمرين: اختبار خادم stdio الخاص بك

الآن بعد أن أنشأت خادم stdio الخاص بك، دعنا نختبره لنتأكد من أنه يعمل بشكل صحيح.

### المتطلبات الأساسية

1. تأكد من تثبيت MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. يجب حفظ كود الخادم (مثلاً كـ `server.py`)

### الاختبار باستخدام Inspector

1. **ابدأ Inspector مع خادمك**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **افتح واجهة الويب**: سيفتح Inspector نافذة متصفح تعرض قدرات خادمك.

3. **اختبر الأدوات**: 
   - جرب أداة `get_greeting` بأسماء مختلفة
   - اختبر أداة `calculate_sum` بأرقام متنوعة
   - استدعِ أداة `get_server_info` لعرض بيانات الخادم

4. **راقب التواصل**: يعرض Inspector رسائل JSON-RPC المتبادلة بين العميل والخادم.

### ما يجب أن تراه

عند تشغيل خادمك بشكل صحيح، يجب أن ترى:
- قدرات الخادم مدرجة في Inspector
- الأدوات المتاحة للاختبار
- تبادل ناجح لرسائل JSON-RPC
- استجابات الأدوات معروضة في الواجهة

### مشاكل شائعة وحلولها

**الخادم لا يبدأ:**
- تحقق من تثبيت كل المكتبات المطلوبة: `pip install mcp`
- تحقق من صحة بناء الجملة والمسافات في بايثون
- ابحث عن رسائل الخطأ في الكونسول

**الأدوات لا تظهر:**
- تأكد من وجود زخارف `@server.tool()`
- تحقق من تعريف دوال الأدوات قبل الدالة `main()`
- تأكد من تكوين الخادم بشكل صحيح

**مشاكل الاتصال:**
- تأكد من أن الخادم يستخدم نقل stdio بشكل صحيح
- تحقق من عدم تعارض عمليات أخرى
- تحقق من صيغة أمر Inspector

## الواجب

حاول تطوير خادمك مع قدرات أكثر. اطلع على [هذه الصفحة](https://api.chucknorris.io/) لإضافة أداة تستدعي API مثلاً. القرار لك في شكل الخادم. بالتوفيق :)
## الحل

[الحل](./solution/README.md) إليك حل ممكن مع كود يعمل.

## النقاط الرئيسية المستفادة

النقاط الأساسية في هذا الفصل هي:

- نقل stdio هو الآلية الموصى بها لخوادم MCP المحلية.
- يسمح نقل stdio بتواصل سلس بين خوادم MCP والعملاء باستخدام تدفقات الدخل والإخراج القياسية.
- يمكنك استخدام كل من Inspector و Visual Studio Code لاستهلاك خوادم stdio مباشرة، مما يجعل التصحيح والتكامل بسيطًا.

## أمثلة 

- [حاسبة جافا](../samples/java/calculator/README.md)
- [حاسبة .Net](../../../../03-GettingStarted/samples/csharp)
- [حاسبة جافا سكريبت](../samples/javascript/README.md)
- [حاسبة TypeScript](../samples/typescript/README.md)
- [حاسبة بايثون](../../../../03-GettingStarted/samples/python) 

## موارد إضافية

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## التالي

## الخطوات التالية

الآن بعد أن تعلمت كيفية بناء خوادم MCP باستخدام نقل stdio، يمكنك استكشاف مواضيع أكثر تقدمًا:

- **التالي**: [البث عبر HTTP مع MCP (HTTP القابل للبث)](../06-http-streaming/README.md) - تعلم عن آلية النقل الأخرى المدعومة للخوادم البعيدة
- **متقدم**: [أفضل ممارسات أمان MCP](../../02-Security/README.md) - تطبيق الأمان في خوادم MCP الخاصة بك
- **الإنتاج**: [استراتيجيات النشر](../09-deployment/README.md) - نشر خوادمك للاستخدام الإنتاجي

## موارد إضافية

- [مواصفة MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - المواصفة الحالية
- [توثيق MCP SDK](https://github.com/modelcontextprotocol/sdk) - مراجع SDK لجميع اللغات
- [أمثلة المجتمع](../../06-CommunityContributions/README.md) - المزيد من أمثلة الخوادم من المجتمع

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->