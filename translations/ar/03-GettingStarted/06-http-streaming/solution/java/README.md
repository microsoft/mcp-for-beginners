# عرض توضيحي لتدفق HTTP في الآلة الحاسبة

يعرض هذا المشروع تدفق HTTP باستخدام Server-Sent Events (SSE) مع Spring Boot WebFlux. يتكون من تطبيقين:

- **خادم الآلة الحاسبة**: خدمة ويب تفاعلية تقوم بإجراء الحسابات وتدفق النتائج باستخدام SSE  
- **عميل الآلة الحاسبة**: تطبيق عميل يستهلك نقطة النهاية الخاصة بالتدفق

## المتطلبات الأساسية

- جافا 17 أو أعلى  
- مافن 3.6 أو أعلى

## هيكل المشروع

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## كيف يعمل

1. يقوم **خادم الآلة الحاسبة** بفتح نقطة نهاية `/calculate` التي:  
   - تقبل معلمات استعلام: `a` (رقم)، `b` (رقم)، `op` (عملية)  
   - العمليات المدعومة: `add`، `sub`، `mul`، `div`  
   - يعيد Server-Sent Events مع تقدم الحساب والنتيجة

2. يتصل **عميل الآلة الحاسبة** بالخادم ويقوم بـ:  
   - إرسال طلب لحساب `7 * 5`  
   - استهلاك الاستجابة المتدفقة  
   - طباعة كل حدث على وحدة التحكم

## تشغيل التطبيقات

### الخيار 1: باستخدام مافن (موصى به)

#### 1. تشغيل خادم الآلة الحاسبة

افتح نافذة طرفية وانتقل إلى مجلد الخادم:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

سيبدأ الخادم على `http://localhost:8080`

يجب أن ترى مخرجات مثل:  
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. تشغيل عميل الآلة الحاسبة

افتح **نافذة طرفية جديدة** وانتقل إلى مجلد العميل:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

سيتصل العميل بالخادم، ينفذ الحساب، ويعرض النتائج المتدفقة.

### الخيار 2: استخدام جافا مباشرة

#### 1. ترجمة وتشغيل الخادم:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. ترجمة وتشغيل العميل:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## اختبار الخادم يدويًا

يمكنك أيضًا اختبار الخادم باستخدام متصفح الويب أو curl:

### باستخدام متصفح الويب:  
قم بزيارة: `http://localhost:8080/calculate?a=10&b=5&op=add`

### باستخدام curl:  
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## المخرجات المتوقعة

عند تشغيل العميل، يجب أن ترى مخرجات متدفقة مشابهة لـ:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## العمليات المدعومة

- `add` - الجمع (a + b)  
- `sub` - الطرح (a - b)  
- `mul` - الضرب (a * b)  
- `div` - القسمة (a / b، ترجع NaN إذا كان b = 0)

## مرجع API

### GET /calculate

**المعلمات:**  
- `a` (مطلوب): الرقم الأول (double)  
- `b` (مطلوب): الرقم الثاني (double)  
- `op` (مطلوب): العملية (`add`، `sub`، `mul`، `div`)

**الاستجابة:**  
- نوع المحتوى: `text/event-stream`  
- يعيد Server-Sent Events مع تقدم الحساب والنتيجة

**مثال على الطلب:**  
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**مثال على الاستجابة:**  
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## استكشاف الأخطاء وإصلاحها

### المشاكل الشائعة

1. **المنفذ 8080 مستخدم بالفعل**  
   - أوقف أي تطبيقات أخرى تستخدم المنفذ 8080  
   - أو غيّر منفذ الخادم في `calculator-server/src/main/resources/application.yml`

2. **رفض الاتصال**  
   - تأكد من تشغيل الخادم قبل بدء العميل  
   - تحقق من أن الخادم بدأ بنجاح على المنفذ 8080

3. **مشاكل أسماء المعلمات**  
   - يتضمن هذا المشروع إعداد مافن للمترجم مع العلم `-parameters`  
   - إذا واجهت مشاكل في ربط المعلمات، تأكد من بناء المشروع بهذا الإعداد

### إيقاف التطبيقات

- اضغط `Ctrl+C` في الطرفية التي يعمل فيها كل تطبيق  
- أو استخدم `mvn spring-boot:stop` إذا كان يعمل كعملية في الخلفية

## تقنية المشروع

- **Spring Boot 3.3.1** - إطار عمل التطبيق  
- **Spring WebFlux** - إطار عمل ويب تفاعلي  
- **Project Reactor** - مكتبة تدفقات تفاعلية  
- **Netty** - خادم I/O غير محظور  
- **Maven** - أداة البناء  
- **Java 17+** - لغة البرمجة

## الخطوات التالية

حاول تعديل الكود لـ:  
- إضافة المزيد من العمليات الرياضية  
- تضمين معالجة الأخطاء للعمليات غير الصالحة  
- إضافة تسجيل الطلبات/الاستجابات  
- تنفيذ المصادقة  
- إضافة اختبارات وحدات

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.