# عميل آلة حاسبة LLM

تطبيق جافا يوضح كيفية استخدام LangChain4j للاتصال بخدمة آلة حاسبة MCP (بروتوكول سياق النموذج) عبر واجهة برمجة التطبيقات MiniMax المتوافقة مع OpenAI.

## المتطلبات الأساسية

- جافا 21 أو أعلى
- Maven 3.6+ (أو استخدم ملف المافن المرفق)
- مفتاح API من MiniMax
- خدمة آلة حاسبة MCP تعمل على `http://localhost:8080`

## الحصول على مفتاح API

يستخدم هذا التطبيق واجهة برمجة التطبيقات MiniMax المتوافقة مع OpenAI. اتبع الخطوات التالية للحصول على مفتاحك ونقطة النهاية:

### 1. اختيار نقطة النهاية
1. استخدم `https://api.minimax.io/v1` للنقطة النهائية العالمية
2. استخدم `https://api.minimaxi.com/v1` للنقطة النهائية في الصين

### 2. إنشاء مفتاح API
1. أنشئ مفتاح API من MiniMax من حسابك في MiniMax
2. احتفظ بالمفتاح في مكان آمن

### 3. تعيين متغيرات البيئة

#### على ويندوز (موجه الأوامر):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### على ويندوز (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### على ماك أو إس/لينكس:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## الإعداد والتثبيت

1. **استنساخ أو التنقل إلى مجلد المشروع**

2. **تثبيت التبعيات**:
   ```cmd
   mvnw clean install
   ```
   أو إذا كان لديك Maven مثبتًا عالميًا:
   ```cmd
   mvn clean install
   ```

3. **إعداد متغيرات البيئة** (راجع قسم "الحصول على مفتاح API" أعلاه)

4. **تشغيل خدمة آلة حاسبة MCP**:
   تأكد من تشغيل خدمة آلة حاسبة MCP من الفصل 1 على `http://localhost:8080/sse`. يجب أن تكون هذه الخدمة تعمل قبل بدء تشغيل العميل.

## تشغيل التطبيق

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ماذا يفعل التطبيق

يوضح التطبيق ثلاث تفاعلات رئيسية مع خدمة الآلة الحاسبة:

1. **الجمع**: يحسب مجموع 24.5 و 17.3
2. **الجذر التربيعي**: يحسب الجذر التربيعي للعدد 144
3. **المساعدة**: يعرض الوظائف المتاحة للآلة الحاسبة

## الإخراج المتوقع

عند التشغيل بنجاح، يجب أن ترى إخراج مشابه لـ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

1. **"متغير البيئة OPENAI_API_KEY غير مضبوط"**
   - تأكد من تعيين متغير البيئة `OPENAI_API_KEY`
   - أعد تشغيل الطرفية/موجه الأوامر بعد تعيين المتغير

2. **"رفض الاتصال بـ localhost:8080"**
   - تحقق من تشغيل خدمة آلة حاسبة MCP على المنفذ 8080
   - تحقق إذا كانت خدمة أخرى تستخدم المنفذ 8080

3. **"فشل التوثيق"**
   - تحقق من صحة مفتاح API الخاص بك
   - تحقق من أن `OPENAI_BASE_URL` يطابق نقطة النهاية التي ترغب في استخدامها

4. **أخطاء بناء Maven**
   - تأكد من أنك تستخدم جافا 21 أو أعلى: `java -version`
   - حاول تنظيف البناء: `mvnw clean`

### التصحيح

لتمكين تسجيل التصحيح، أضف الوسيط JVM التالي عند التشغيل:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## التهيئة

تم تهيئة التطبيق ليقوم بـ:
- استخدام MiniMax-M3 بشكل افتراضي؛ اضبط `MINIMAX_MODEL_ID` لاختيار إما `MiniMax-M3` أو `MiniMax-M2.7`
- الاتصال بـ `OPENAI_BASE_URL` عند تعيينه؛ وإلا يستخدم `https://api.minimaxi.com/v1` عندما تكون `MINIMAX_REGION=cn_zh`، أو `https://api.minimax.io/v1` افتراضيًا
- الاتصال بخدمة MCP على `http://localhost:8080/sse`
- استخدام مهلة 60 ثانية للطلبات

## التبعيات

التبعيات الأساسية المستخدمة في هذا المشروع:
- **LangChain4j**: للتكامل مع الذكاء الاصطناعي وإدارة الأدوات
- **LangChain4j MCP**: لدعم بروتوكول سياق النموذج
- **LangChain4j OpenAI الرسمي**: لتكامل واجهة برمجة تطبيقات MiniMax المتوافقة مع OpenAI
- **Spring Boot**: لإطار العمل والتصريف التلقائي للتبعيات

## الترخيص

هذا المشروع مرخص بموجب رخصة Apache 2.0 - راجع ملف [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) للتفاصيل.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->