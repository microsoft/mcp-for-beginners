# خدمة الآلة الحاسبة الأساسية MCP

تقدم هذه الخدمة عمليات آلة حاسبة أساسية عبر بروتوكول سياق النموذج (MCP) باستخدام Spring Boot مع نقل WebFlux. تم تصميمها كمثال بسيط للمبتدئين الذين يتعلمون عن تطبيقات MCP.

لمزيد من المعلومات، راجع وثائق المرجع [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html).

## استخدام الخدمة

تعرض الخدمة نقاط نهاية API التالية عبر بروتوكول MCP:

- `add(a, b)`: جمع رقمين معًا
- `subtract(a, b)`: طرح الرقم الثاني من الأول
- `multiply(a, b)`: ضرب رقمين
- `divide(a, b)`: قسمة الرقم الأول على الثاني (مع التحقق من القسمة على صفر)
- `power(base, exponent)`: حساب قوة رقم ما
- `squareRoot(number)`: حساب الجذر التربيعي (مع التحقق من الأرقام السالبة)
- `modulus(a, b)`: حساب الباقي عند القسمة
- `absolute(number)`: حساب القيمة المطلقة

## التبعيات

يتطلب المشروع التبعيات الرئيسية التالية:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## بناء المشروع

قم ببناء المشروع باستخدام Maven:
```bash
./mvnw clean install -DskipTests
```

## تشغيل الخادم

### باستخدام Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### باستخدام MCP Inspector

يعد MCP Inspector أداة مفيدة للتفاعل مع خدمات MCP. لاستخدامه مع خدمة الآلة الحاسبة هذه:

1. **قم بتثبيت وتشغيل MCP Inspector** في نافذة طرفية جديدة:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **ادخل إلى واجهة الويب** بالنقر على الرابط الذي يعرضه التطبيق (عادة http://localhost:6274)

3. **قم بتكوين الاتصال**:
   - اضبط نوع النقل على "SSE"
   - اضبط عنوان URL إلى نقطة نهاية SSE الخاصة بالخادم الذي يعمل لديك: `http://localhost:8080/sse`
   - انقر على "Connect"

4. **استخدم الأدوات**:
   - انقر على "List Tools" لرؤية العمليات المتاحة في الآلة الحاسبة
   - اختر أداة وانقر على "Run Tool" لتنفيذ العملية

![MCP Inspector Screenshot](../../../../../../translated_images/ar/tool.40e180a7b0d0fe20.webp)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.