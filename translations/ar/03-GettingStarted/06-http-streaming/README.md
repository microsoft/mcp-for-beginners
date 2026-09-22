# البث عبر HTTPS باستخدام بروتوكول سياق النموذج (MCP)

يوفر هذا الفصل دليلاً شاملاً لتنفيذ البث الآمن والقابل للتوسع ووقت-حقيقي باستخدام بروتوكول سياق النموذج (MCP) عبر HTTPS. يغطي الدوافع للبث، وآليات النقل المتاحة، كيفية تنفيذ HTTP القابل للبث في MCP، أفضل ممارسات الأمان، الانتقال من SSE، والإرشادات العملية لبناء تطبيقات MCP قابلة للبث خاصة بك.

> [!WARNING]
> تستهدف أمثلة التنفيذ في هذا الدرس **مواصفات MCP
> `2025-11-25`** وتوضح مصافحة `initialize` القديمة،
> `Mcp-Session-Id`، تدفق الأحداث عبر GET، ونموذج إمكانية الاستئناف. تزيل MCP `2026-07-28`
> هذه الميزات. طلبات HTTP القابلة للبث الحالية هي طلبات POST مستقلة مع رؤوس `MCP-Protocol-Version` و `Mcp-Method`، بالإضافة إلى
> `Mcp-Name` عند الحاجة. راجع
> [ما الجديد في MCP: مواصفات 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> قبل استخدام هذه الأمثلة في تنفيذ جديد.


## آليات النقل والبث في MCP

يستعرض هذا القسم آليات النقل المختلفة المتاحة في MCP ودورها في تمكين قدرات البث للتواصل في الوقت الحقيقي بين العملاء والخوادم.

### ما هي آلية النقل؟

تعرف آلية النقل كيفية تبادل البيانات بين العميل والخادم. يدعم MCP أنواع نقل متعددة لتناسب بيئات ومتطلبات مختلفة:

- **stdio**: الإدخال/الإخراج القياسي، مناسب للأدوات المحلية وأدوات سطر الأوامر. بسيط لكنه غير مناسب للويب أو السحابة.
- **HTTP+SSE**: النقل البعيد القديم، تم إيقافه في MCP `2025-03-26`
    واستبداله بـ Streamable HTTP. لا تستخدمه في تنفيذات جديدة.
- **Streamable HTTP**: نقل بث حديث معتمد على HTTP، يدعم الإشعارات وقابلية التوسع الأفضل. يوصى به لمعظم سيناريوهات الإنتاج والسحابة.

### جدول المقارنة

ألقِ نظرة على جدول المقارنة أدناه لفهم الاختلافات بين آليات النقل هذه:

| النقل | الحالة | الإشعارات | الاستخدام النموذجي |
|---|---|---|---|
| stdio | الحالي | نعم | عمليات فرعيه محلية |
| HTTP+SSE | متوقف | نعم | تنفيذات بعيدة قديمة |
| Streamable HTTP | الحالي | نعم | خوادم بعيدة وسحابية |

> **نصيحة:** اختيار النقل الصحيح يؤثر على الأداء، وقابلية التوسع، وتجربة المستخدم. يُوصى بـ **Streamable HTTP** لتطبيقات حديثة، قابلة للتوسع، ومهيأة للسحابة.

النقلات القياسية هي stdio و Streamable HTTP. يظهر HTTP+SSE في
أمثلة قديمة فقط.

## البث: المفاهيم والدوافع

فهم المفاهيم الأساسية والدوافع وراء البث ضروري لتنفيذ أنظمة تواصل في الوقت الحقيقي فعالة.

**البث** هو تقنية في برمجة الشبكات تسمح بإرسال واستقبال البيانات على شكل قطع صغيرة قابلة للإدارة أو كتسلسل من الأحداث، بدلاً من انتظار استكمال الاستجابة بالكامل. هذا مفيد بشكل خاص لـ:

- الملفات أو مجموعات البيانات الكبيرة.
- التحديثات في الوقت الحقيقي (مثل: الدردشة، أشرطة التقدم).
- الحسابات طويلة الأمد حيث تريد إبقاء المستخدم على اطلاع.

إليك ما تحتاج إلى معرفته حول البث على مستوى عالٍ:

- يتم تسليم البيانات تدريجيًا، وليس دفعة واحدة.
- يمكن للعميل معالجة البيانات أثناء وصولها.
- يقلل من الكمون الظاهر ويحسن تجربة المستخدم.

### لماذا نستخدم البث؟

الأسباب لاستخدام البث هي كما يلي:


- يحصل المستخدمون على ردود فورية، وليس فقط في النهاية
- يتيح تطبيقات الوقت الحقيقي وواجهات مستخدم سريعة الاستجابة
- استخدام أكثر كفاءة لموارد الشبكة والحوسبة

### مثال بسيط: خادم وعميل للبث عبر HTTP

إليك مثالًا بسيطًا عن كيفية تنفيذ البث:

#### بايثون

**الخادم (بايثون، باستخدام FastAPI و StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**العميل (بايثون، باستخدام requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

يوضح هذا المثال خادمًا يرسل سلسلة من الرسائل إلى العميل فور توفرها، بدلاً من الانتظار حتى تصبح كل الرسائل جاهزة.

**كيف يعمل:**

- الخادم يوفر كل رسالة بمجرد جاهزيتها.
- العميل يستقبل ويطبع كل جزء بمجرد وصوله.

**المتطلبات:**

- يجب أن يستخدم الخادم استجابة بث (مثل `StreamingResponse` في FastAPI).
- يجب على العميل معالجة الاستجابة كتدفق (`stream=True` في requests).
- نوع المحتوى يكون عادة `text/event-stream` أو `application/octet-stream`.

#### جافا

**الخادم (جافا، باستخدام Spring Boot و Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**العميل (جافا، باستخدام Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**ملاحظات تنفيذ جافا:**

- يستخدم مكدس Spring Boot التفاعلي مع `Flux` للبث
- يوفر `ServerSentEvent` بثًا منظمًا للأحداث مع أنواع أحداث
- `WebClient` مع `bodyToFlux()` يمكّن الاستهلاك التفاعلي للبث
- `delayElements()` يحاكي وقت المعالجة بين الأحداث
- يمكن أن يكون للأحداث أنواع (`info`، `result`) لتحكم أفضل في العميل

### مقارنة: البث الكلاسيكي مقابل بث MCP

يمكن تصوير الاختلافات بين كيفية عمل البث بطريقة "كلاسيكية" مقابل كيفية عمله في MCP كما يلي:

| الميزة                | بث HTTP كلاسيكي               | بث MCP (الإشعارات)               |
|------------------------|-------------------------------|-------------------------------------|
| الرد الرئيسي          | مقسم إلى أجزاء               | واحد، في النهاية                   |
| تحديثات التقدم       | تُرسل كقطع بيانات            | تُرسل كإشعارات                   |
| متطلبات العميل       | يجب معالجة التدفق            | يجب تنفيذ معالج الرسائل          |
| حالة الاستخدام       | ملفات كبيرة، تدفقات رموز AI  | التقدم، السجلات، ردود فعل فورية  |

### الفروق الرئيسية الملحوظة

بالإضافة إلى ذلك، هنا بعض الفروق الرئيسية:

- **نمط التواصل:**
  - بث HTTP الكلاسيكي: يستخدم ترميز نقل مقسم بسيط لإرسال البيانات في أجزاء
  - بث MCP: يستخدم نظام إشعارات منظم مع بروتوكول JSON-RPC

- **تنسيق الرسائل:**
  - HTTP الكلاسيكي: أجزاء نص عادي مع أسطر جديدة
  - MCP: كائنات Notification من نوع LoggingMessage بها بيانات وصفية

- **تنفيذ العميل:**
  - HTTP الكلاسيكي: عميل بسيط يعالج الردود المتدفقة
  - MCP: عميل أكثر تعقيدًا مع معالج رسائل للتعامل مع أنواع مختلفة من الرسائل

- **تحديثات التقدم:**
  - HTTP الكلاسيكي: التقدم جزء من تدفق الرد الرئيسي
  - MCP: التقدم يُرسل عبر رسائل إشعارات منفصلة بينما الرد الرئيسي يأتي في النهاية

### التوصيات

هناك بعض الأمور التي نوصي بها عند اختيار تنفيذ البث الكلاسيكي (كنقطة نهاية عرضناها أعلاه باستخدام `/stream`) مقابل اختيار البث عبر MCP.

- **للحاجة لبث بسيط:** البث الكلاسيكي عبر HTTP أبسط في التنفيذ وكافٍ لاحتياجات البث الأساسية.


- **للتطبيقات المعقدة والتفاعلية:** يوفر البث في MCP نهجًا أكثر تنظيمًا مع بيانات وصفية أغنى وفصلًا بين الإشعارات والنتائج النهائية.

- **لتطبيقات الذكاء الاصطناعي:** نظام الإشعارات في MCP مفيد بشكل خاص للمهام الذكاء الاصطناعي طويلة الأمد حيث تريد إبقاء المستخدمين على اطلاع بالتقدم.

## البث في MCP

حسنًا، لقد رأيت بعض التوصيات والمقارنات حتى الآن حول الفرق بين البث الكلاسيكي والبث في MCP. لنخوض في التفاصيل حول كيف يمكنك استخدام البث في MCP.

فهم كيفية عمل البث ضمن إطار MCP أمر ضروري لبناء تطبيقات تفاعلية تقدم ملاحظات في الوقت الحقيقي للمستخدمين أثناء العمليات طويلة الأمد.

في MCP، البث ليس عن إرسال الاستجابة الرئيسية على أجزاء، بل عن إرسال **الإشعارات** إلى العميل أثناء معالجة الأداة لطلب ما. هذه الإشعارات يمكن أن تشمل تحديثات التقدم، السجلات، أو أحداث أخرى.

### كيف يعمل

يتم إرسال النتيجة الرئيسية ما زالت كرد واحد كامل. ومع ذلك، يمكن إرسال الإشعارات كرسائل منفصلة أثناء المعالجة ومن ثم تحديث العميل في الوقت الفعلي. يجب أن يكون العميل قادرًا على التعامل مع هذه الإشعارات وعرضها.

### تمرين اختياري: الاتصال بخادم MCP مستضاف

يمكنك أيضًا استخدام بروتوكول HTTP القابل للبث دون تشغيل خادم محلي. هذا المثال
يتصل بـ [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp)،
يكتشف أدواته، ويبحث في توثيق MCP العام باستخدام نفس
SDK الخاص بـ Python كما في [العميل المحلي](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

نقطة النهاية المجهولة في Parallel لا تتطلب حسابًا أو مفتاح API. الوصول المجاني
محدود بمعدل. تشغيل هذا السكربت يرسل استعلامات البحث، الهدف، و
معرف جلسة عشوائي إلى Parallel. تقدم الخدمة أيضًا `web_fetch`،
الذي يرسل عناوين URL المطلوبة وأي سياق مقدم إلى Parallel. استخدم المعلومات العامة
لهذا التمرين؛ راجع شروطها [terms](https://parallel.ai/customer-terms)
وسياسة الخصوصية [privacy policy](https://parallel.ai/privacy-policy).

مع Python 3.10 أو أحدث وبيئة افتراضية مفعلة، قم بتثبيت SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

احفظ هذا باسم `hosted_search.py` وشغّل `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

توقع أن يتضمن الاكتشاف `web_search` و `web_fetch`، تليها استجابة بحث تحتوي على عناوين URL للمصادر ومقتطفات. يمكن أن تختلف النتائج أو تكون فارغة.
يتحقق السكربت من `isError` لأن الأداة قد تفشل حتى لو نجح طلب HTTP.
إذا كان الوصول محدودًا بالمعدل، انتظر قبل المحاولة مجددًا. أعد استخدام نفس
`session_id` إذا قمت بتوسيع السكربت لاستدعاءات بحث أو جلب مرتبطة.


نتيجة JSON كاملة بدون إشعارات تقدم. يتولى SDK التعامل مع
النقل. واصل مع المثال المحلي أدناه لتتعلم عن الإشعارات.
هذا السكربت الاختياري يقوم ببحث واضح واحد ويغلق اتصالَه عند
الانتهاء. إذا قمت لاحقًا بكشف هذه الأدوات لوكيل، قد يستدعيها الوكيل أثناء عمله؛ تعامل مع النص المستخلص من الويب كبيانات غير موثوقة.



## ما هو الإشعار؟

لقد قلنا "إشعار"، ماذا يعني ذلك في سياق MCP؟

الإشعار هو رسالة JSON-RPC لا تحتوي على `id` ولا
تتلقى ردًا. يستخدم MCP الإشعارات للتقدم، الإلغاء، و
أحداث أحادية الاتجاه أخرى.

في MCP `2025-11-25`، يرسل العميل `notifications/initialized` بعد ال

مصافحة التهيئة. MCP `2026-07-28` لا يحتوي على مصافحة تهيئة، لذا
هذا الإشعار هو سلوك قديم.

يبدو الإشعار على النحو التالي كرسالة JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

التسجيل هو ميزة تستخدم الإشعارات؛ الإشعارات نفسها هي
نوع رسالة JSON-RPC عام.

> **مهمل في MCP `2026-07-28`:** تظل ميزة التسجيل متاحة
> للتوافق لكنها مؤهلة للإزالة في أول مراجعة للمواصفات
> الصادرة في أو بعد 28 يوليو 2027. يجب على التنفيذات الجديدة استخدام
> `stderr` مع stdio أو OpenTelemetry للرصد المهيكل.

بالنسبة لتنفيذ قديم `2025-11-25`، يقوم الخادم بتمكين
قدرة التسجيل كما يلي:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> اعتمادًا على SDK المستخدم، قد يتم تمكين التسجيل افتراضيًا، أو قد تحتاج إلى تمكينه صراحةً في تكوين الخادم الخاص بك.

هناك أنواع مختلفة من الإشعارات:

| المستوى     | الوصف                       | مثال على الاستخدام            |
|-----------|---------------------------|------------------------------|
| تصحيح     | معلومات تفصيلية للتصحيح      | نقاط دخول/خروج الوظائف       |
| معلومات   | رسائل إعلامية عامة           | تحديثات تقدم العملية         |
| إشعار     | أحداث عادية لكنها مهمة       | تغييرات التكوين              |
| تحذير     | حالات تحذيرية                | استخدام ميزة مهملة            |
| خطأ       | حالات خطأ                   | فشل العمليات                |
| حرج       | حالات حرجة                   | فشل مكونات النظام            |
| تنبيه     | يجب اتخاذ إجراء فورًا         | اكتشاف تلف في البيانات       |
| حالة طوارئ| النظام غير قابل للاستخدام     | فشل كامل للنظام             |

## تنفيذ الإشعارات في MCP

لتنفيذ الإشعارات في MCP، تحتاج إلى إعداد كل من جانب الخادم والعميل للتعامل مع التحديثات اللحظية. يسمح هذا لتطبيقك بتقديم ردود فورية للمستخدمين أثناء العمليات طويلة الأمد.

### جانب الخادم: إرسال الإشعارات

لنبدأ بجانب الخادم. في MCP، تعرف الأدوات التي يمكنها إرسال الإشعارات أثناء معالجة الطلبات. يستخدم الخادم كائن السياق (عادةً `ctx`) لإرسال الرسائل إلى العميل.

#### بايثون

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

في المثال السابق، ترسل أداة `process_files` ثلاث إشعارات إلى العميل أثناء معالجة كل ملف. تُستخدم الطريقة `ctx.info()` لإرسال رسائل معلومات.

بالإضافة إلى ذلك، لتمكين الإشعارات، تأكد أن الخادم الخاص بك يستخدم وسيلة نقل تدفقية (مثل `streamable-http`) وأن العميل الخاص بك ينفذ معالج رسائل لمعالجة الإشعارات. إليك كيف يمكنك إعداد الخادم لاستخدام وسيلة النقل `streamable-http`:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

في هذا المثال لـ .NET، تُزين أداة `ProcessFiles` بالسمات `Tool` وترسل ثلاث إشعارات إلى العميل أثناء معالجة كل ملف. تُستخدم الطريقة `ctx.Info()` لإرسال رسائل معلومات.

لتمكين الإشعارات في خادم MCP الخاص بك على .NET، تأكد من استخدام وسيلة نقل تدفقية:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### جانب العميل: استقبال الإشعارات

يجب على العميل تنفيذ معالج رسائل لمعالجة وعرض الإشعارات حال وصولها.

#### بايثون

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```


في الكود السابق، تتحقق الدالة `message_handler` مما إذا كانت الرسالة الواردة هي إشعار. إذا كانت كذلك، فإنها تطبع الإشعار؛ وإلا فإنها تعالجه كرسالة خادم عادية. لاحظ أيضًا كيف يتم تهيئة `ClientSession` باستخدام `message_handler` للتعامل مع الإشعارات الواردة.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```


في هذا المثال الخاص بـ .NET، تتحقق الدالة `MessageHandler` مما إذا كانت الرسالة الواردة هي إشعار. إذا كانت كذلك، تقوم بطباعة الإشعار؛ وإلا فإنها تعالجه كرسالة عادية من الخادم. يتم تهيئة `ClientSession` مع معالج الرسائل عبر `ClientSessionOptions`.

لتمكين الإشعارات، تأكد من أن خادمك يستخدم نقل البث (مثل `streamable-http`) وأن عميلك ينفذ معالج رسائل لمعالجة الإشعارات.

## إشعارات التقدم والسيناريوهات

يشرح هذا القسم مفهوم إشعارات التقدم في MCP، ولماذا هي مهمة، وكيفية تنفيذها باستخدام Streamable HTTP. ستجد أيضًا مهمة عملية لتعزيز فهمك.

إشعارات التقدم هي رسائل في الوقت الحقيقي يرسلها الخادم إلى العميل أثناء العمليات طويلة الأمد. بدلاً من انتظار انتهاء العملية بالكامل، يبقي الخادم العميل محدثًا حول الحالة الحالية. هذا يحسن الشفافية وتجربة المستخدم ويسهل التصحيح.

**مثال:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### لماذا نستخدم إشعارات التقدم؟

إشعارات التقدم ضرورية لأسباب عدة:

- **تجربة مستخدم أفضل:** يرى المستخدمون التحديثات أثناء تقدم العمل، وليس فقط في النهاية.
- **ردود فعل في الوقت الحقيقي:** يمكن للعملاء عرض شريط تقدم أو سجلات، مما يجعل التطبيق يبدو تفاعليًا.
- **تصحيح ورصد أسهل:** يمكن للمطورين والمستخدمين معرفة أين قد تكون العملية بطيئة أو متوقفة.

### كيفية تنفيذ إشعارات التقدم

إليك كيفية تنفيذ إشعارات التقدم في MCP:

- **على الخادم:** استخدم `ctx.info()` أو `ctx.log()` لإرسال الإشعارات أثناء معالجة كل عنصر. هذا يرسل رسالة إلى العميل قبل أن يكون النتيجة الرئيسية جاهزة.
- **على العميل:** نفذ معالج رسائل يستمع للإشعارات ويعرضها عند وصولها. يميز هذا المعالج بين الإشعارات والنتيجة النهائية.

**مثال على الخادم:**

#### بايثون

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**مثال على العميل:**

#### بايثون

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## اعتبارات الأمان

يجب أن يكون الأمان أولوية قصوى عند تنفيذ أي خادم، خاصة عند استخدام نقل قائم على HTTP مثل Streamable HTTP في MCP.

عند تنفيذ خوادم MCP باستخدام نقل قائم على HTTP، يصبح الأمان قضية رئيسية تتطلب اهتمامًا دقيقًا بعدة اتجاهات هجومية وآليات حماية.

### نظرة عامة

الأمان أمر حاسم عند تعريض خوادم MCP عبر HTTP. يقدم Streamable HTTP أسطح هجوم جديدة ويتطلب إعدادًا دقيقًا.

فيما يلي بعض اعتبارات الأمان الرئيسية:

- **التحقق من رأس Origin:** دائمًا تحقق من رأس `Origin` لمنع هجمات ربط DNS.
- **الربط بـ localhost:** للتطوير المحلي، اربط الخوادم بـ `localhost` لتجنب تعريضها للإنترنت العام.
- **المصادقة:** نفذ مصادقة (مثل مفاتيح API، OAuth) للنشر في البيئات الإنتاجية.
- **CORS:** قم بإعداد سياسات مشاركة الموارد عبر الأصول (CORS) لتقييد الوصول.
- **HTTPS:** استخدم HTTPS في الإنتاج لتشفير المرور.

### أفضل الممارسات

بالإضافة إلى ذلك، إليك بعض أفضل الممارسات التي يجب اتباعها عند تنفيذ الأمان في خادم بث MCP الخاص بك:

- لا تثق أبدًا في الطلبات الواردة دون التحقق منها.
- سجل وراقب كل الوصول والأخطاء.
- حدث التبعيات بانتظام لسد الثغرات الأمنية.

### التحديات

ستواجه بعض التحديات عند تنفيذ الأمان في خوادم بث MCP:

- التوازن بين الأمان وسهولة التطوير
- ضمان التوافق مع بيئات العملاء المختلفة


## الترقية من SSE إلى Streamable HTTP

للتطبيقات التي تستخدم حاليًا Server-Sent Events (SSE)، توفر الترقية إلى Streamable HTTP قدرات محسنة واستدامة أفضل طويلة الأمد لتطبيقات MCP الخاصة بك.

### لماذا الترقية؟

هناك سببان مقنعان للترقية من SSE إلى Streamable HTTP:

- يقدم Streamable HTTP قابلية توسع أفضل، توافقًا أعلى، ودعم إشعارات أغنى مقارنة بـ SSE.
- هو النقل الموصى به لتطبيقات MCP الجديدة.

### خطوات الترحيل

إليك كيفية الترحيل من SSE إلى Streamable HTTP في تطبيقات MCP الخاصة بك:

- **تحديث كود الخادم** لاستخدام `transport="streamable-http"` في `mcp.run()`.
- **تحديث كود العميل** لاستخدام `streamablehttp_client` بدلًا من عميل SSE.
- **تنفيذ معالج رسائل** في العميل لمعالجة الإشعارات.
- **اختبر التوافق** مع الأدوات وسير العمل الحالية.

### الحفاظ على التوافق

يُنصح بالحفاظ على التوافق مع عملاء SSE الحاليين أثناء عملية الترحيل. إليك بعض الاستراتيجيات:

- يمكنك دعم كلاً من SSE وStreamable HTTP بتشغيل كلا النقلين على نقاط نهاية مختلفة.
- ترحيل العملاء تدريجيًا إلى النقل الجديد.

### التحديات

تأكد من معالجة التحديات التالية أثناء الترحيل:

- ضمان تحديث جميع العملاء
- التعامل مع اختلافات تسليم الإشعارات

### المهمة: بناء تطبيق MCP بث خاص بك

**السيناريو:**
بناء خادم وعميل MCP حيث يعالج الخادم قائمة من العناصر (مثل الملفات أو المستندات) ويرسل إشعارًا لكل عنصر تتم معالجته. يجب على العميل عرض كل إشعار فور وصوله.

**الخطوات:**

1. تنفيذ أداة خادم تعالج قائمة وترسل إشعارات لكل عنصر.
2. تنفيذ عميل مع معالج رسائل لعرض الإشعارات في الوقت الحقيقي.
3. اختبار التنفيذ بتشغيل كل من الخادم والعميل، ومراقبة الإشعارات.

[الحل](./solution/README.md)

## المزيد من القراءة وما القادم؟

لمواصلة رحلتك مع بث MCP وتوسيع معرفتك، يقدم هذا القسم موارد إضافية وخطوات مقترحة لبناء تطبيقات أكثر تقدمًا.

### المزيد من القراءة

- [Microsoft: مقدمة في بث HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: أحداث المرسل من الخادم (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS في ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: طلبات بث](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### ما القادم؟

- جرب بناء أدوات MCP أكثر تقدمًا تستخدم البث للتحليلات في الوقت الحقيقي، الدردشة، أو التحرير التعاوني.
- استكشف دمج بث MCP مع أُطُر العمل الأمامية (React, Vue, إلخ) لتحديثات واجهة المستخدم الحية.
- التالي: [استخدام مجموعة أدوات الذكاء الاصطناعي لـ VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->