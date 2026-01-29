# الدرس: بناء خادم MCP للبحث على الويب

يُظهر هذا الفصل كيفية بناء وكيل ذكاء اصطناعي عملي يتكامل مع واجهات برمجة التطبيقات الخارجية، ويتعامل مع أنواع بيانات متنوعة، ويدير الأخطاء، وينسق بين أدوات متعددة — كل ذلك بصيغة جاهزة للإنتاج. سترى:

- **التكامل مع واجهات برمجة التطبيقات الخارجية التي تتطلب المصادقة**
- **التعامل مع أنواع بيانات متنوعة من نقاط نهاية متعددة**
- **استراتيجيات قوية لإدارة الأخطاء وتسجيلها**
- **تنسيق أدوات متعددة في خادم واحد**

بحلول النهاية، ستحصل على خبرة عملية في الأنماط وأفضل الممارسات الضرورية لتطبيقات الذكاء الاصطناعي المتقدمة والمدعومة بنماذج اللغة الكبيرة.

## المقدمة

في هذا الدرس، ستتعلم كيفية بناء خادم MCP متقدم وعميل يوسع قدرات نماذج اللغة الكبيرة باستخدام بيانات الويب الحية عبر SerpAPI. هذه مهارة حاسمة لتطوير وكلاء ذكاء اصطناعي ديناميكيين يمكنهم الوصول إلى معلومات محدثة من الإنترنت.

## أهداف التعلم

بحلول نهاية هذا الدرس، ستكون قادرًا على:

- دمج واجهات برمجة التطبيقات الخارجية (مثل SerpAPI) بأمان في خادم MCP
- تنفيذ أدوات متعددة للبحث على الويب، الأخبار، المنتجات، والأسئلة والأجوبة
- تحليل وتنسيق البيانات المهيكلة لاستهلاكها بواسطة نماذج اللغة الكبيرة
- التعامل مع الأخطاء وإدارة حدود معدل استدعاء API بفعالية
- بناء واختبار عملاء MCP تلقائيين وتفاعليين

## خادم MCP للبحث على الويب

يقدم هذا القسم بنية وميزات خادم MCP للبحث على الويب. سترى كيف يُستخدم FastMCP وSerpAPI معًا لتوسيع قدرات نماذج اللغة الكبيرة ببيانات ويب حية.

### نظرة عامة

يتميز هذا التطبيق بأربع أدوات تُظهر قدرة MCP على التعامل مع مهام متنوعة مدفوعة بواجهات برمجة التطبيقات الخارجية بأمان وكفاءة:

- **general_search**: للنتائج العامة على الويب
- **news_search**: للعناوين الإخبارية الحديثة
- **product_search**: لبيانات التجارة الإلكترونية
- **qna**: لقصاصات الأسئلة والأجوبة

### الميزات
- **أمثلة برمجية**: تتضمن كتل كود خاصة بلغات معينة مثل بايثون (وقابلة للتوسيع بسهولة للغات أخرى) باستخدام محاور الكود للوضوح

### بايثون

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

قبل تشغيل العميل، من المفيد فهم ما يفعله الخادم. ملف [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ينفذ خادم MCP، ويعرض أدوات للبحث على الويب، الأخبار، المنتجات، والأسئلة والأجوبة من خلال التكامل مع SerpAPI. يتعامل مع الطلبات الواردة، يدير استدعاءات API، يحلل الردود، ويعيد نتائج مهيكلة إلى العميل.

يمكنك مراجعة التنفيذ الكامل في [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

إليك مثالًا موجزًا عن كيفية تعريف وتسجيل أداة في الخادم:

### خادم بايثون

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **التكامل مع API الخارجية**: يوضح كيفية التعامل الآمن مع مفاتيح API والطلبات الخارجية
- **تحليل البيانات المهيكلة**: يبين كيفية تحويل ردود API إلى صيغ مناسبة لنماذج اللغة الكبيرة
- **إدارة الأخطاء**: معالجة قوية للأخطاء مع تسجيل مناسب
- **عميل تفاعلي**: يشمل اختبارات تلقائية ووضع تفاعلي للاختبار
- **إدارة السياق**: يستفيد من MCP Context لتسجيل وتتبع الطلبات

## المتطلبات الأساسية

قبل البدء، تأكد من إعداد بيئتك بشكل صحيح باتباع الخطوات التالية. هذا يضمن تثبيت جميع التبعيات وتكوين مفاتيح API بشكل صحيح لتطوير واختبار سلس.

- بايثون 3.8 أو أحدث
- مفتاح API من SerpAPI (سجل في [SerpAPI](https://serpapi.com/) - يوجد خطة مجانية)

## التثبيت

لبدء العمل، اتبع الخطوات التالية لإعداد بيئتك:

1. ثبت التبعيات باستخدام uv (موصى به) أو pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. أنشئ ملف `.env` في جذر المشروع وضع فيه مفتاح SerpAPI الخاص بك:

```
SERPAPI_KEY=your_serpapi_key_here
```

## الاستخدام

خادم MCP للبحث على الويب هو المكون الأساسي الذي يعرض أدوات للبحث على الويب، الأخبار، المنتجات، والأسئلة والأجوبة من خلال التكامل مع SerpAPI. يتعامل مع الطلبات الواردة، يدير استدعاءات API، يحلل الردود، ويعيد نتائج مهيكلة إلى العميل.

يمكنك مراجعة التنفيذ الكامل في [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### تشغيل الخادم

لتشغيل خادم MCP، استخدم الأمر التالي:

```bash
python server.py
```

سيعمل الخادم كخادم MCP يعتمد على stdio يمكن للعميل الاتصال به مباشرة.

### أوضاع العميل

يدعم العميل (`client.py`) وضعين للتفاعل مع خادم MCP:

- **الوضع العادي**: يشغل اختبارات تلقائية تغطي جميع الأدوات وتتحقق من ردودها. هذا مفيد لفحص سريع أن الخادم والأدوات تعمل كما هو متوقع.
- **الوضع التفاعلي**: يبدأ واجهة قائمة تتيح لك اختيار الأدوات يدويًا، إدخال استعلامات مخصصة، ورؤية النتائج في الوقت الحقيقي. هذا مثالي لاستكشاف قدرات الخادم وتجربة مدخلات مختلفة.

يمكنك مراجعة التنفيذ الكامل في [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### تشغيل العميل

لتشغيل الاختبارات التلقائية (سيبدأ الخادم تلقائيًا):

```bash
python client.py
```

أو التشغيل في الوضع التفاعلي:

```bash
python client.py --interactive
```

### الاختبار بطرق مختلفة

هناك عدة طرق لاختبار والتفاعل مع الأدوات التي يوفرها الخادم، حسب احتياجاتك وسير عملك.

#### كتابة سكربتات اختبار مخصصة باستخدام MCP Python SDK
يمكنك أيضًا بناء سكربتات اختبار خاصة بك باستخدام MCP Python SDK:

# [بايثون](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

في هذا السياق، يعني "سكربت اختبار" برنامج بايثون مخصص تكتبه ليعمل كعميل لخادم MCP. بدلاً من أن يكون اختبار وحدة رسمي، يتيح لك هذا السكربت الاتصال برمجيًا بالخادم، استدعاء أي من أدواته مع المعلمات التي تختارها، وفحص النتائج. هذا الأسلوب مفيد لـ:
- النمذجة والتجريب مع استدعاءات الأدوات
- التحقق من كيفية استجابة الخادم لمدخلات مختلفة
- أتمتة استدعاءات الأدوات المتكررة
- بناء سير عمل أو تكاملات خاصة بك فوق خادم MCP

يمكنك استخدام سكربتات الاختبار لتجربة استعلامات جديدة بسرعة، تصحيح سلوك الأدوات، أو حتى كنقطة انطلاق لأتمتة أكثر تقدمًا. أدناه مثال على كيفية استخدام MCP Python SDK لإنشاء مثل هذا السكربت:

## وصف الأدوات

يمكنك استخدام الأدوات التالية التي يوفرها الخادم لأداء أنواع مختلفة من عمليات البحث والاستعلامات. كل أداة موصوفة أدناه مع معلماتها وطريقة استخدامها كمثال.

يوفر هذا القسم تفاصيل عن كل أداة متاحة ومعلماتها.

### general_search

ينفذ بحثًا عامًا على الويب ويعيد نتائج منسقة.

**كيفية استدعاء هذه الأداة:**

يمكنك استدعاء `general_search` من سكربتك الخاص باستخدام MCP Python SDK، أو تفاعليًا باستخدام Inspector أو وضع العميل التفاعلي. إليك مثال برمجي باستخدام SDK:

# [مثال بايثون](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

بدلاً من ذلك، في الوضع التفاعلي، اختر `general_search` من القائمة وأدخل استعلامك عند الطلب.

**المعلمات:**
- `query` (نص): استعلام البحث

**مثال طلب:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

يبحث عن مقالات إخبارية حديثة مرتبطة باستعلام.

**كيفية استدعاء هذه الأداة:**

يمكنك استدعاء `news_search` من سكربتك الخاص باستخدام MCP Python SDK، أو تفاعليًا باستخدام Inspector أو وضع العميل التفاعلي. إليك مثال برمجي باستخدام SDK:

# [مثال بايثون](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

بدلاً من ذلك، في الوضع التفاعلي، اختر `news_search` من القائمة وأدخل استعلامك عند الطلب.

**المعلمات:**
- `query` (نص): استعلام البحث

**مثال طلب:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

يبحث عن منتجات تطابق استعلامًا معينًا.

**كيفية استدعاء هذه الأداة:**

يمكنك استدعاء `product_search` من سكربتك الخاص باستخدام MCP Python SDK، أو تفاعليًا باستخدام Inspector أو وضع العميل التفاعلي. إليك مثال برمجي باستخدام SDK:

# [مثال بايثون](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

بدلاً من ذلك، في الوضع التفاعلي، اختر `product_search` من القائمة وأدخل استعلامك عند الطلب.

**المعلمات:**
- `query` (نص): استعلام البحث عن المنتج

**مثال طلب:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

يحصل على إجابات مباشرة للأسئلة من محركات البحث.

**كيفية استدعاء هذه الأداة:**

يمكنك استدعاء `qna` من سكربتك الخاص باستخدام MCP Python SDK، أو تفاعليًا باستخدام Inspector أو وضع العميل التفاعلي. إليك مثال برمجي باستخدام SDK:

# [مثال بايثون](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

بدلاً من ذلك، في الوضع التفاعلي، اختر `qna` من القائمة وأدخل سؤالك عند الطلب.

**المعلمات:**
- `question` (نص): السؤال الذي تريد إيجاد إجابة له

**مثال طلب:**

```json
{
  "question": "what is artificial intelligence"
}
```

## تفاصيل الكود

يوفر هذا القسم مقتطفات برمجية ومراجع لتنفيذات الخادم والعميل.

# [بايثون](../../../../05-AdvancedTopics/web-search-mcp)

راجع [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) و[`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) للتفاصيل الكاملة للتنفيذ.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## مفاهيم متقدمة في هذا الدرس

قبل أن تبدأ في البناء، إليك بعض المفاهيم المتقدمة المهمة التي ستظهر طوال هذا الفصل. فهمها سيساعدك على المتابعة حتى لو كنت جديدًا عليها:

- **تنسيق أدوات متعددة**: يعني تشغيل عدة أدوات مختلفة (مثل البحث على الويب، البحث في الأخبار، البحث عن المنتجات، والأسئلة والأجوبة) ضمن خادم MCP واحد. يسمح هذا لخادمك بالتعامل مع مهام متنوعة، وليس مهمة واحدة فقط.
- **إدارة حدود معدل API**: العديد من واجهات برمجة التطبيقات الخارجية (مثل SerpAPI) تحدد عدد الطلبات التي يمكنك إرسالها خلال فترة زمنية معينة. الكود الجيد يتحقق من هذه الحدود ويتعامل معها بسلاسة، حتى لا يتعطل تطبيقك عند الوصول للحد.
- **تحليل البيانات المهيكلة**: ردود API غالبًا ما تكون معقدة ومتداخلة. هذا المفهوم يتعلق بتحويل تلك الردود إلى صيغ نظيفة وسهلة الاستخدام تناسب نماذج اللغة الكبيرة أو البرامج الأخرى.
- **استرداد الأخطاء**: أحيانًا تحدث مشاكل — قد يفشل الاتصال، أو لا تعود API بما تتوقعه. استرداد الأخطاء يعني أن كودك يمكنه التعامل مع هذه المشاكل ويعطي ملاحظات مفيدة بدلاً من التعطل.
- **التحقق من المعلمات**: يتعلق هذا بالتأكد من أن جميع المدخلات لأدواتك صحيحة وآمنة للاستخدام. يشمل تعيين القيم الافتراضية والتأكد من صحة الأنواع، مما يساعد على منع الأخطاء واللبس.

## استكشاف الأخطاء وإصلاحها

سيساعدك هذا القسم على تشخيص وحل المشكلات الشائعة التي قد تواجهها أثناء العمل مع خادم MCP للبحث على الويب. إذا واجهت أخطاء أو سلوكًا غير متوقع أثناء العمل مع الخادم، يوفر هذا القسم حلولًا للمشكلات الأكثر شيوعًا. راجع هذه النصائح قبل طلب المساعدة — فهي غالبًا ما تحل المشاكل بسرعة.

### المشكلات الشائعة

فيما يلي بعض المشاكل الأكثر تكرارًا التي يواجهها المستخدمون، مع شروحات واضحة وخطوات لحلها:

1. **مفتاح SERPAPI_KEY مفقود في ملف .env**
   - إذا رأيت الخطأ `SERPAPI_KEY environment variable not found`، فهذا يعني أن التطبيق لا يستطيع العثور على مفتاح API اللازم للوصول إلى SerpAPI. لحل المشكلة، أنشئ ملفًا باسم `.env` في جذر المشروع (إذا لم يكن موجودًا) وأضف السطر `SERPAPI_KEY=your_serpapi_key_here`. تأكد من استبدال `your_serpapi_key_here` بالمفتاح الفعلي الخاص بك من موقع SerpAPI.

2. **أخطاء عدم وجود وحدة (Module not found)**
   - أخطاء مثل `ModuleNotFoundError: No module named 'httpx'` تعني أن حزمة بايثون المطلوبة مفقودة. يحدث هذا عادة إذا لم تقم بتثبيت جميع التبعيات. لحل المشكلة، شغّل الأمر `pip install -r requirements.txt` في الطرفية لتثبيت كل ما يحتاجه مشروعك.

3. **مشاكل الاتصال**
   - إذا حصلت على خطأ مثل `Error during client execution`، فهذا غالبًا يعني أن العميل لا يستطيع الاتصال بالخادم، أو أن الخادم لا يعمل كما هو متوقع. تحقق من أن العميل والخادم من إصدارات متوافقة، وأن ملف `server.py` موجود ويعمل في الدليل الصحيح. إعادة تشغيل الخادم والعميل قد تساعد أيضًا.

4. **أخطاء SerpAPI**
   - ظهور رسالة `Search API returned error status: 401` يعني أن مفتاح SerpAPI مفقود، غير صحيح، أو منتهي الصلاحية. اذهب إلى لوحة تحكم SerpAPI، تحقق من مفتاحك، وقم بتحديث ملف `.env` إذا لزم الأمر. إذا كان المفتاح صحيحًا ولكن الخطأ مستمر، تحقق مما إذا كانت الحصة المجانية قد انتهت.

### وضع التصحيح (Debug Mode)

افتراضيًا، يسجل التطبيق المعلومات المهمة فقط. إذا أردت رؤية تفاصيل أكثر عما يحدث (مثلًا لتشخيص مشاكل معقدة)، يمكنك تفعيل وضع DEBUG. سيعرض هذا المزيد من التفاصيل عن كل خطوة يقوم بها التطبيق.

**مثال: الإخراج العادي**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**مثال: إخراج DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

لاحظ كيف يتضمن وضع DEBUG أسطرًا إضافية عن طلبات HTTP، الردود، وتفاصيل داخلية أخرى. هذا مفيد جدًا لاستكشاف الأخطاء وإصلاحها.
لتفعيل وضع DEBUG، قم بضبط مستوى التسجيل إلى DEBUG في أعلى ملف `client.py` أو `server.py` الخاص بك:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## ما التالي

- [5.10 البث المباشر في الوقت الحقيقي](../mcp-realtimestreaming/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.