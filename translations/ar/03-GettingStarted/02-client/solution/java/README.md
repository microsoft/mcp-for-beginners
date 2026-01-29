# MCP Java Client - عرض توضيحي للآلة الحاسبة

يُظهر هذا المشروع كيفية إنشاء عميل Java يتصل بخادم MCP (بروتوكول سياق النموذج) ويتفاعل معه. في هذا المثال، سنقوم بالاتصال بخادم الآلة الحاسبة من الفصل 01 وتنفيذ عمليات رياضية مختلفة.

## المتطلبات الأساسية

قبل تشغيل هذا العميل، تحتاج إلى:

1. **تشغيل خادم الآلة الحاسبة** من الفصل 01:
   - انتقل إلى مجلد خادم الآلة الحاسبة: `03-GettingStarted/01-first-server/solution/java/`
   - قم ببناء وتشغيل خادم الآلة الحاسبة:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - يجب أن يكون الخادم قيد التشغيل على `http://localhost:8080`

2. **تثبيت Java 21 أو أحدث** على نظامك  
3. **Maven** (مضمن عبر Maven Wrapper)

## ما هو SDKClient؟

`SDKClient` هو تطبيق Java يوضح كيفية:
- الاتصال بخادم MCP باستخدام نقل Server-Sent Events (SSE)  
- عرض الأدوات المتاحة من الخادم  
- استدعاء وظائف الآلة الحاسبة المختلفة عن بُعد  
- معالجة الردود وعرض النتائج  

## كيف يعمل

يستخدم العميل إطار عمل Spring AI MCP لـ:

1. **إقامة الاتصال**: ينشئ عميل WebFlux SSE للاتصال بخادم الآلة الحاسبة  
2. **تهيئة العميل**: يضبط عميل MCP ويؤسس الاتصال  
3. **اكتشاف الأدوات**: يعرض جميع عمليات الآلة الحاسبة المتاحة  
4. **تنفيذ العمليات**: يستدعي وظائف رياضية مختلفة باستخدام بيانات تجريبية  
5. **عرض النتائج**: يعرض نتائج كل عملية حسابية  

## هيكل المشروع

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## التبعيات الرئيسية

يستخدم المشروع التبعيات الرئيسية التالية:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

تقدم هذه التبعية:
- `McpClient` - واجهة العميل الرئيسية  
- `WebFluxSseClientTransport` - نقل SSE للاتصالات عبر الويب  
- مخططات بروتوكول MCP وأنواع الطلبات/الردود  

## بناء المشروع

قم ببناء المشروع باستخدام Maven wrapper:

```cmd
.\mvnw clean install
```

## تشغيل العميل

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**ملاحظة**: تأكد من تشغيل خادم الآلة الحاسبة على `http://localhost:8080` قبل تنفيذ أي من هذه الأوامر.

## ما الذي يفعله العميل

عند تشغيل العميل، سيقوم بـ:

1. **الاتصال** بخادم الآلة الحاسبة على `http://localhost:8080`  
2. **عرض الأدوات** - يعرض جميع عمليات الآلة الحاسبة المتاحة  
3. **إجراء الحسابات**:  
   - الجمع: 5 + 3 = 8  
   - الطرح: 10 - 4 = 6  
   - الضرب: 6 × 7 = 42  
   - القسمة: 20 ÷ 4 = 5  
   - الأس: 2^8 = 256  
   - الجذر التربيعي: √16 = 4  
   - القيمة المطلقة: |-5.5| = 5.5  
   - المساعدة: يعرض العمليات المتاحة  

## المخرجات المتوقعة

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**ملاحظة**: قد تظهر تحذيرات Maven حول وجود خيوط متبقية في النهاية - هذا أمر طبيعي في التطبيقات التفاعلية ولا يشير إلى وجود خطأ.

## فهم الكود

### 1. إعداد النقل  
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```  
هذا ينشئ نقل SSE (Server-Sent Events) يتصل بخادم الآلة الحاسبة.

### 2. إنشاء العميل  
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```  
ينشئ عميل MCP متزامن ويهيئ الاتصال.

### 3. استدعاء الأدوات  
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```  
يستدعي أداة "add" مع المعاملات a=5.0 و b=3.0.

## استكشاف الأخطاء وإصلاحها

### الخادم غير قيد التشغيل  
إذا واجهت أخطاء في الاتصال، تأكد من تشغيل خادم الآلة الحاسبة من الفصل 01:  
```
Error: Connection refused
```  
**الحل**: قم بتشغيل خادم الآلة الحاسبة أولاً.

### المنفذ مستخدم بالفعل  
إذا كان المنفذ 8080 مشغولاً:  
```
Error: Address already in use
```  
**الحل**: أوقف التطبيقات الأخرى التي تستخدم المنفذ 8080 أو قم بتعديل الخادم لاستخدام منفذ مختلف.

### أخطاء البناء  
إذا واجهت أخطاء في البناء:  
```cmd
.\mvnw clean install -DskipTests
```

## تعلم المزيد

- [توثيق Spring AI MCP](https://docs.spring.io/spring-ai/reference/api/mcp/)  
- [مواصفات بروتوكول سياق النموذج](https://modelcontextprotocol.io/)  
- [توثيق Spring WebFlux](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.