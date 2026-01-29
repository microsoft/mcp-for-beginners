# تشغيل هذا المثال

إليك كيفية تشغيل خادم وعميل HTTP التقليدي للبث، بالإضافة إلى خادم وعميل MCP للبث باستخدام Python.

### نظرة عامة

- ستقوم بإعداد خادم MCP يقوم ببث إشعارات التقدم إلى العميل أثناء معالجة العناصر.
- سيعرض العميل كل إشعار في الوقت الفعلي.
- يغطي هذا الدليل المتطلبات الأساسية، الإعداد، التشغيل، واستكشاف الأخطاء وإصلاحها.

### المتطلبات الأساسية

- Python 3.9 أو أحدث
- حزمة Python `mcp` (قم بتثبيتها باستخدام `pip install mcp`)

### التثبيت والإعداد

1. قم باستنساخ المستودع أو تنزيل ملفات الحل.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **قم بإنشاء وتفعيل بيئة افتراضية (موصى به):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **قم بتثبيت التبعيات المطلوبة:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### الملفات

- **الخادم:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **العميل:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### تشغيل خادم HTTP التقليدي للبث

1. انتقل إلى دليل الحل:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. قم بتشغيل خادم HTTP التقليدي للبث:

   ```pwsh
   python server.py
   ```

3. سيبدأ الخادم ويعرض:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### تشغيل عميل HTTP التقليدي للبث

1. افتح نافذة طرفية جديدة (قم بتفعيل نفس البيئة الافتراضية والدليل):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. يجب أن ترى الرسائل المتدفقة مطبوعة بشكل متسلسل:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### تشغيل خادم MCP للبث

1. انتقل إلى دليل الحل:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. قم بتشغيل خادم MCP باستخدام النقل "streamable-http":
   ```pwsh
   python server.py mcp
   ```
3. سيبدأ الخادم ويعرض:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### تشغيل عميل MCP للبث

1. افتح نافذة طرفية جديدة (قم بتفعيل نفس البيئة الافتراضية والدليل):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. يجب أن ترى الإشعارات مطبوعة في الوقت الفعلي أثناء معالجة الخادم لكل عنصر:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### خطوات التنفيذ الرئيسية

1. **قم بإنشاء خادم MCP باستخدام FastMCP.**
2. **حدد أداة تقوم بمعالجة قائمة وترسل إشعارات باستخدام `ctx.info()` أو `ctx.log()`.**
3. **قم بتشغيل الخادم باستخدام `transport="streamable-http"`.**
4. **قم بتنفيذ عميل مع معالج رسائل لعرض الإشعارات عند وصولها.**

### استعراض الكود
- يستخدم الخادم وظائف غير متزامنة وسياق MCP لإرسال تحديثات التقدم.
- يقوم العميل بتنفيذ معالج رسائل غير متزامن لطباعة الإشعارات والنتيجة النهائية.

### نصائح واستكشاف الأخطاء وإصلاحها

- استخدم `async/await` للعمليات غير المحظورة.
- تعامل دائمًا مع الاستثناءات في كل من الخادم والعميل لضمان المتانة.
- اختبر مع عدة عملاء لملاحظة التحديثات في الوقت الفعلي.
- إذا واجهت أخطاء، تحقق من إصدار Python الخاص بك وتأكد من تثبيت جميع التبعيات.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة أو هامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.