# تصحيح الأخطاء باستخدام MCP Inspector

> [!NOTE]
> الأوامر التي تستخدم `--sse` وروابط URL التي تنتهي بـ `/sse` تختبر بروتوكول HTTP+SSE القديم.
> بالنسبة لخادم MCP الجديد `2026-07-28`، استخدم إصدار Inspector الذي
> يدعم HTTP القابل للتدفق واختر هذا البروتوكول بدلاً من ذلك.

أداة **MCP Inspector** هي أداة تصحيح أخطاء أساسية تتيح لك اختبار خوادم MCP الخاصة بك والتعامل معها بشكل تفاعلي بدون الحاجة إلى تطبيق مضيف ذكاء اصطناعي كامل. اعتبرها "Postman لـ MCP" - توفر واجهة بصرية لإرسال الطلبات، عرض الردود، وفهم كيفية تصرف الخادم.

## لماذا تستخدم MCP Inspector؟

عند بناء خوادم MCP، ستواجه غالبًا هذه التحديات:

- **"هل خادمي يعمل أصلاً؟"** - Inspector يعرض حالة الاتصال
- **"هل أدواتي مسجلة بشكل صحيح؟"** - Inspector يسرد جميع الأدوات المتاحة
- **"ما هو تنسيق الاستجابة؟"** - Inspector يعرض ردود JSON كاملة
- **"لماذا هذه الأداة لا تعمل؟"** - Inspector يعرض رسائل خطأ مفصلة

## المتطلبات الأساسية

- تثبيت Node.js 18 أو أحدث
- npm (يأتي مع Node.js)
- خادم MCP للاختبار (انظر [الوحدة 3.1 - أول خادم](../01-first-server/README.md))

## التثبيت

### الخيار 1: التشغيل باستخدام npx (موصى به للاختبار السريع)

```bash
npx @modelcontextprotocol/inspector
```

### الخيار 2: التثبيت عالميًا

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### الخيار 3: الإضافة إلى مشروعك

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

أضف إلى `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## الاتصال بخادمك

### خوادم stdio (عملية محلية)

للخوادم التي تتواصل عبر الإدخال/الإخراج القياسي:

```bash
# خادم بايثون
npx @modelcontextprotocol/inspector python -m your_server_module

# خادم Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# مع متغيرات البيئة
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### خوادم SSE/HTTP (شبكة)

للخوادم التي تعمل كخدمات HTTP:

1. ابدأ خادمك أولاً:
   ```bash
   python server.py  # الخادم يعمل على http://localhost:8080
   ```

2. شغّل Inspector واتصل:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## نظرة عامة على واجهة Inspector

عند تشغيل Inspector، سترى واجهة ويب (عادة على `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## اختبار الأدوات

### سرد الأدوات المتاحة

1. انقر على علامة التبويب **الأدوات**
2. يقوم Inspector تلقائيًا باستدعاء `tools/list`
3. سترى جميع الأدوات المسجلة مع:
   - اسم الأداة
   - الوصف
   - مخطط الإدخال (المعلمات)

### استدعاء أداة

1. اختر أداة من القائمة
2. املأ المعلمات المطلوبة في النموذج
3. انقر **تشغيل الأداة**
4. اعرض الاستجابة في لوحة النتائج

**مثال: اختبار أداة الآلة الحاسبة**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### تصحيح أخطاء أدوات MCP

عند فشل أداة، يعرض Inspector:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

رموز الأخطاء الشائعة:
| الرمز | المعنى |
|------|---------|
| -32700 | خطأ في التحليل (JSON غير صالح) |
| -32600 | طلب غير صالح |
| -32601 | الطريقة غير موجودة |
| -32602 | معلمات غير صالحة |
| -32603 | خطأ داخلي |

---

## اختبار الموارد

### سرد الموارد

1. انقر على علامة التبويب **الموارد**
2. ينفذ Inspector استدعاء `resources/list`
3. سترى:
   - عناوين URI للموارد
   - الأسماء والأوصاف
   - أنواع MIME

### قراءة مورد

1. اختر موردًا
2. انقر **قراءة المورد**
3. عرض المحتوى المُعاد

**مثال على الإخراج:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## اختبار المطالبات

### سرد المطالبات

1. انقر على علامة التبويب **المطالبات**
2. ينفذ Inspector استدعاء `prompts/list`
3. عرض قوالب المطالبات المتاحة

### الحصول على مطالبة

1. اختر مطالبة
2. املأ أي معطيات مطلوبة
3. انقر **الحصول على مطالبة**
4. عرض رسائل المطالبة المعروضة

---

## تحليل سجل الرسائل

يعرض سجل الرسائل جميع رسائل بروتوكول MCP. المقتطف أدناه من
خادم قديم `2025-11-25` ويشمل مقبض المصافحة `initialize` الذي تمت إزالته. يستخدم خادم
`2026-07-28` بيانات وصفية مستقلة للطلبات و`server/discover`
بدلاً من ذلك.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### ما الذي تبحث عنه

- **أزواج الطلب/الاستجابة**: يجب أن يكون لكل `→` مقابله `←`
- **رسائل الخطأ**: ابحث عن `"error"` في الردود
- **التوقيت**: الفجوات الكبيرة قد تشير إلى مشاكل في الأداء
- **إصدار البروتوكول**: تأكد من تطابق إصدار الخادم والعميل

---

## التكامل مع VS Code

يمكنك تشغيل Inspector مباشرة من VS Code:

### استخدام launch.json

أضف إلى `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### استخدام المهام

أضف إلى `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## سيناريوهات تصحيح الأخطاء الشائعة

### السيناريو 1: خادم لا يتصل

**الأعراض:** يظهر Inspector "تم الفصل" أو يتوقف على "جار الاتصال..."

**قائمة التحقق:**
1. ✅ هل الأمر الخاص بالخادم صحيح؟
2. ✅ هل تم تثبيت جميع التبعيات؟
3. ✅ هل مسار الخادم مسار مطلق أو نسبي إلى الدليل الحالي؟
4. ✅ هل تم تعيين المتغيرات البيئية المطلوبة؟

**خطوات تصحيح الأخطاء:**
```bash
# اختبار الخادم يدويًا أولاً
python -c "import your_server_module; print('OK')"

# التحقق من وجود أخطاء في الاستيراد
python -m your_server_module 2>&1 | head -20

# التأكد من تثبيت MCP SDK
pip show mcp
```

### السيناريو 2: الأدوات لا تظهر

**الأعراض:** تبويب الأدوات يعرض قائمة فارغة

**الأسباب المحتملة:**
1. لم تُسجل الأدوات أثناء تهيئة الخادم
2. تعطل الخادم بعد بدء التشغيل
3. معالج `tools/list` يعيد مصفوفة فارغة

**خطوات تصحيح الأخطاء:**
1. تحقق من سجل الرسائل لرد `tools/list`
2. أضف تسجيلًا في كود تسجيل أدواتك
3. تحقق من وجود مزخرفات `@mcp.tool()` (بايثون)

### السيناريو 3: الأداة تُرجع خطأ

**الأعراض:** استدعاء الأداة يُرجع استجابة خطأ

**نهج التصحيح:**
1. اقرأ رسالة الخطأ بعناية
2. تحقق من تطابق أنواع المعاملات مع المخطط
3. أضف كتلة try/catch مع رسائل خطأ مفصلة
4. تحقق من سجلات الخادم لبحث أثر التطبق

**مثال على تحسين معالجة الخطأ:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # منطق الأداة هنا
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### السيناريو 4: محتوى المورد فارغ

**الأعراض:** المورد يعيد لكنه المحتوى فارغ أو null

**قائمة التحقق:**
1. ✅ هل مسار الملف أو URI صحيح
2. ✅ هل لدى الخادم صلاحية قراءة المورد
3. ✅ هل يتم إرجاع محتوى المورد بشكل صحيح

---

## ميزات Inspector المتقدمة

### رؤوس مخصصة (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### تسجيل تفصيلي

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### تسجيل الجلسات

يمكن لـ Inspector تصدير سجلات الرسائل للتحليل لاحقًا:
1. انقر **تصدير السجل** في لوحة الرسائل
2. احفظ ملف JSON
3. شاركه مع أعضاء الفريق لتصحيح الأخطاء

---

## أفضل الممارسات

1. **اختبر مبكرًا وبشكل متكرر** - استخدم Inspector أثناء التطوير، وليس فقط عند حدوث الأعطال
2. **ابدأ بالبساطة** - اختبر الاتصال الأساسي قبل استدعاءات الأدوات المعقدة
3. **تحقق من المخطط** - العديد من الأخطاء تأتي من عدم تطابق أنواع المعاملات
4. **اقرأ رسائل الخطأ** - أخطاء MCP عادة ما تكون وصفية
5. **احتفظ بـ Inspector مفتوحًا** - يساعد على اكتشاف المشكلات أثناء التطوير

---

## ما التالي

لقد أكملت الوحدة 3: البدء! تابع تعلمك:

- [الوحدة 4: التنفيذ العملي](../../04-PracticalImplementation/README.md)

---

## موارد إضافية

- [مستودع GitHub الخاص بـ MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [مواصفة MCP - رسائل البروتوكول](https://modelcontextprotocol.io/specification/2026-07-28/)
- [مواصفة JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->