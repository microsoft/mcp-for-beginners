# خادم MCP مع نقل stdio

> **⚠️ تحديث مهم**: اعتبارًا من مواصفة MCP بتاريخ 2025-06-18، تم **إيقاف استخدام** نقل SSE المستقل (Server-Sent Events) واستبداله بنقل "HTTP القابل للتدفق". تحدد مواصفة MCP الحالية آليتي نقل رئيسيتين:
> 1. **stdio** - الإدخال/الإخراج القياسي (موصى به للخوادم المحلية)
> 2. **HTTP القابل للتدفق** - للخوادم البعيدة التي قد تستخدم SSE داخليًا
>
> تم تحديث هذا الدرس ليركز على **نقل stdio**، وهو النهج الموصى به لمعظم تطبيقات خوادم MCP.

يتيح نقل stdio لخوادم MCP التواصل مع العملاء عبر تدفقات الإدخال والإخراج القياسية. هذا هو آلية النقل الأكثر استخدامًا والأكثر توصية في مواصفة MCP الحالية، حيث يوفر طريقة بسيطة وفعالة لبناء خوادم MCP يمكن دمجها بسهولة مع تطبيقات العملاء المختلفة.

## نظرة عامة

يغطي هذا الدرس كيفية بناء واستهلاك خوادم MCP باستخدام نقل stdio.

## أهداف التعلم

بحلول نهاية هذا الدرس، ستكون قادرًا على:

- بناء خادم MCP باستخدام نقل stdio.
- تصحيح أخطاء خادم MCP باستخدام Inspector.
- استهلاك خادم MCP باستخدام Visual Studio Code.
- فهم آليات النقل الحالية لـ MCP ولماذا يوصى باستخدام stdio.


## نقل stdio - كيف يعمل

نقل stdio هو أحد نوعي النقل المدعومين في مواصفة MCP الحالية (2025-06-18). وإليك كيف يعمل:

- **اتصال بسيط**: يقرأ الخادم رسائل JSON-RPC من الإدخال القياسي (`stdin`) ويرسل الرسائل إلى الإخراج القياسي (`stdout`).
- **يعتمد على العمليات**: يطلق العميل خادم MCP كعملية فرعية.
- **تنسيق الرسالة**: الرسائل هي طلبات JSON-RPC منفردة أو إشعارات أو استجابات، مفصولة بواسطة أسطر جديدة.
- **تسجيل**: يجوز للخادم كتابة سلاسل UTF-8 إلى الخطأ القياسي (`stderr`) لأغراض التسجيل.

### المتطلبات الرئيسية:
- يجب أن تكون الرسائل مفصولة بأسطر جديدة ويجب ألا تحتوي على أسطر جديدة مدمجة
- يجب ألا يكتب الخادم أي شيء إلى `stdout` لا يعد رسالة MCP صالحة
- يجب ألا يكتب العميل أي شيء إلى `stdin` الخاص بالخادم لا يعد رسالة MCP صالحة

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

- نستورد فئة `Server` و`StdioServerTransport` من MCP SDK
- ننشئ مثيل خادم مع تكوين وقدرات أساسية

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

في الكود السابق نقوم بـ:

- إنشاء مثيل خادم باستخدام MCP SDK
- تعريف الأدوات باستخدام الزخارف
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
- يتم إطلاقها كعمليات فرعية بواسطة العميل
- تتواصل عبر تدفقات stdin/stdout
- أبسط في التنفيذ والتصحيح

## تمرين: إنشاء خادم stdio

لإنشاء خادمنا، نحتاج إلى تذكر أمرين:

- نحتاج إلى استخدام خادم ويب لعرض نقاط نهاية للاتصال والرسائل.
## مختبر: إنشاء خادم MCP بسيط باستخدام stdio

في هذا المختبر، سننشئ خادم MCP بسيط باستخدام نقل stdio الموصى به. سيعرض هذا الخادم الأدوات التي يمكن للعملاء استدعاؤها باستخدام بروتوكول نموذج السياق القياسي.

### المتطلبات المسبقة

- بايثون 3.8 أو أحدث
- MCP Python SDK: `pip install mcp`
- فهم أساسي للبرمجة غير المتزامنة

لنبدأ بإنشاء أول خادم MCP باستخدام stdio:

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

## الفروق الرئيسية عن نهج SSE المُلغى

**نقل Stdio (المعيار الحالي):**
- نموذج عملية فرعية بسيط - يطلق العميل الخادم كعملية فرعية
- التواصل عبر stdin/stdout باستخدام رسائل JSON-RPC
- لا حاجة لإعداد خادم HTTP
- أداء وأمان أفضل
- تصحيح وبناء أسهل

**نقل SSE (تم إيقافه اعتبارًا من MCP 2025-06-18):**
- مطلوب خادم HTTP مع نقاط نهاية SSE
- إعداد أكثر تعقيدًا مع بنية خادم ويب
- اعتبارات أمان إضافية لنقاط نهاية HTTP
- تم استبداله الآن بـ HTTP القابل للتدفق لسيناريوهات الويب

### إنشاء خادم باستخدام نقل stdio

لإنشاء خادم stdio الخاص بنا، نحتاج إلى:

1. **استيراد المكتبات المطلوبة** - نحتاج مكونات خادم MCP ونقل stdio
2. **إنشاء مثيل خادم** - تعريف الخادم مع قدراته
3. **تعريف الأدوات** - إضافة الوظائف التي نريد عرضها
4. **إعداد النقل** - تكوين اتصال stdio
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

### الخطوة 2: إضافة أدوات أكثر

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

1. قم بتثبيت Inspector: `npx @modelcontextprotocol/inspector`
2. شغل Inspector ووجهه إلى خادمك
3. اختبر الأدوات التي أنشأتها

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## تصحيح خادم stdio الخاص بك

### باستخدام MCP Inspector

يعد MCP Inspector أداة قيمة لتصحيح واختبار خوادم MCP. إليك كيفية استخدامه مع خادم stdio الخاص بك:

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
   - اختبار الأدوات بمعلمات مختلفة
   - مراقبة رسائل JSON-RPC
   - تصحيح مشاكل الاتصال

### باستخدام VS Code

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
3. شغّل المصحح واختبر باستخدام Inspector

### نصائح شائعة لتصحيح الأخطاء

- استخدم `stderr` للتسجيل - لا تكتب أبدًا إلى `stdout` لأنه مخصص لرسائل MCP
- تأكد أن جميع رسائل JSON-RPC مفصولة بأسطر جديدة
- اختبر أولًا بأدوات بسيطة قبل إضافة وظائف معقدة
- استخدم Inspector للتحقق من تنسيق الرسائل

## استهلاك خادم stdio الخاص بك في VS Code

بمجرد بناء خادم MCP باستخدام نقل stdio، يمكنك دمجه مع VS Code لاستخدامه مع Claude أو عملاء MCP الآخرين.

### التكوين

1. **إنشاء ملف تكوين MCP** في `%APPDATA%\Claude\claude_desktop_config.json` (ويندوز) أو `~/Library/Application Support/Claude/claude_desktop_config.json` (ماك):

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

2. **إعادة تشغيل Claude**: أغلق وافتح Claude لتحميل تكوين الخادم الجديد.

3. **اختبر الاتصال**: ابدأ محادثة مع Claude وجرب استخدام أدوات خادمك:
   - "هل يمكنك تحيتي باستخدام أداة التحية؟"
   - "احسب مجموع 15 و 27"
   - "ما هي معلومات الخادم؟"

### مثال على خادم stdio باستخدام TypeScript

إليك مثال TypeScript كامل للرجوع إليه:

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

// أضف الأدوات
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

### مثال على خادم stdio باستخدام .NET

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

- بناء خوادم MCP باستخدام **نقل stdio الحالي** (النهج الموصى به)
- فهم سبب إيقاف استخدام نقل SSE لصالح stdio وHTTP القابل للتدفق
- إنشاء أدوات يمكن استدعاؤها من عملاء MCP
- تصحيح الخادم باستخدام MCP Inspector
- دمج خادم stdio الخاص بك مع VS Code وClaude

يوفر نقل stdio طريقة أبسط وأكثر أمانًا وأفضل أداء لبناء خوادم MCP مقارنة بنهج SSE الملغى. وهو آلية النقل الموصى بها لمعظم تطبيقات خوادم MCP حسب مواصفة 2025-06-18.


### .NET

1. لننشئ بعض الأدوات أولاً، لهذا سننشئ ملف *Tools.cs* بالمحتوى التالي:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## تمرين: اختبار خادم stdio الخاص بك

بعد أن أنشأت خادم stdio الخاص بك، دعنا نختبره للتأكد من عمله بشكل صحيح.

### المتطلبات المسبقة

1. تأكد من تثبيت MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. يجب أن يكون كود الخادم محفوظًا (مثلًا كـ `server.py`)

### الاختبار باستخدام Inspector

1. **ابدأ Inspector مع خادمك**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **افتح واجهة الويب**: Inspector سيفتح نافذة المتصفح ليظهر قدرات الخادم.

3. **اختبر الأدوات**: 
   - جرّب أداة `get_greeting` بأسماء مختلفة
   - اختبر أداة `calculate_sum` بأرقام متنوعة
   - استدعي أداة `get_server_info` لرؤية بيانات التعريف الخاصة بالخادم

4. **راقب الاتصال**: يعرض Inspector رسائل JSON-RPC المتبادلة بين العميل والخادم.

### ما الذي يجب أن تراه

عند بدء الخادم بشكل صحيح، يجب أن ترى:
- قدرات الخادم مدرجة في Inspector
- الأدوات متاحة للاختبار
- تبادل رسائل JSON-RPC بنجاح
- ظهور استجابات الأدوات في الواجهة

### المشاكل الشائعة والحلول

**الخادم لا يبدأ:**
- تحقق من تثبيت جميع الاعتمادات: `pip install mcp`
- تحقق من صحة بناء الجملة والمسافة البادئة في بايثون
- ابحث عن رسائل خطأ في الكونسول

**عدم ظهور الأدوات:**
- تأكد من وجود زخارف `@server.tool()`
- تحقق من تعريف دوال الأدوات قبل `main()`
- تأكد من تكوين الخادم بشكل صحيح

**مشاكل الاتصال:**
- تأكد من استخدام خادم stdio النقل بشكل صحيح
- تحقق من عدم وجود عمليات أخرى تعيق الاتصال
- تحقق من صحة صياغة أمر Inspector

## الواجب

حاول بناء خادمك بإضافة قدرات أكثر. اطلع على [هذه الصفحة](https://api.chucknorris.io/) لإضافة أداة تستدعي API. لك حرية تحديد شكل الخادم. استمتع :)

## الحل

[الحل](./solution/README.md) هذا حل ممكن مع كود يعمل.

## النقاط الرئيسية

النقاط الرئيسية في هذا الفصل هي:

- نقل stdio هو الآلية الموصى بها لخوادم MCP المحلية.
- يسمح نقل stdio بالتواصل السلس بين خوادم MCP والعملاء باستخدام تدفقات الإدخال والإخراج القياسية.
- يمكنك استخدام كل من Inspector وVisual Studio Code لاستهلاك خوادم stdio مباشرة، مما يسهل التصحيح والدمج.

## عينات 

- [حاسبة جافا](../samples/java/calculator/README.md)
- [حاسبة .Net](../../../../03-GettingStarted/samples/csharp)
- [حاسبة جافا سكريبت](../samples/javascript/README.md)
- [حاسبة TypeScript](../samples/typescript/README.md)
- [حاسبة بايثون](../../../../03-GettingStarted/samples/python) 

## موارد إضافية

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ماذا بعد

## الخطوات التالية

بعد أن تعلمت كيف تبني خوادم MCP باستخدام نقل stdio، يمكنك استكشاف مواضيع متقدمة أكثر:

- **التالي**: [HTTP Streaming مع MCP (HTTP القابل للتدفق)](../06-http-streaming/README.md) - تعرف على آلية النقل الثانية المدعومة للخوادم البعيدة
- **متقدم**: [أفضل ممارسات أمان MCP](../../02-Security/README.md) - تنفيذ الأمان في خوادم MCP الخاصة بك
- **للإنتاج**: [استراتيجيات النشر](../09-deployment/README.md) - نشر خوادمك للاستخدام الإنتاجي

## موارد إضافية

- [مواصفة MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - المواصفة الرسمية
- [توثيق MCP SDK](https://github.com/modelcontextprotocol/sdk) - مراجع SDK لجميع اللغات
- [أمثلة المجتمع](../../06-CommunityContributions/README.md) - المزيد من أمثلة الخوادم من المجتمع

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى إلى الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. بالنسبة للمعلومات الحساسة، نوصي بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->