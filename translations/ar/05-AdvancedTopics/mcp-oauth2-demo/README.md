# عرض توضيحي لـ MCP OAuth2

> [!WARNING]
> هذا نموذج تعليمي محلي، وليس خدمة تفويض للإنتاج. إنه
> يستخدم عميلًا في الذاكرة ويولد مفتاح توقيع جديد عند بدء التشغيل. لا
> تنشره أبدًا مع سر عميل مشترك أو افتراضي أو خاضع للتحكم في المصدر.

## مقدمة

OAuth2 هو بروتوكول الصناعة القياسي للتفويض، مما يتيح الوصول الآمن إلى الموارد بدون مشاركة بيانات الاعتماد. في تطبيقات MCP (بروتوكول سياق النموذج)، يوفر OAuth2 طريقة قوية للمصادقة وتفويض العملاء (مثل وكلاء الذكاء الاصطناعي) للوصول إلى خوادم MCP وأدواتها.

يوضح هذا الدرس كيفية تنفيذ مصادقة OAuth2 لخوادم MCP باستخدام Spring Boot، وهو نمط شائع للنشر في المؤسسات والإنتاج.

## أهداف التعلم

بنهاية هذا الدرس، ستتمكن من:
- فهم كيفية دمج OAuth2 مع خوادم MCP
- تنفيذ خادم تفويض Spring لإصدار الرموز
- حماية نقاط نهاية MCP باستخدام مصادقة قائمة على JWT
- تكوين سير بيانات اعتماد العميل للتواصل بين الأجهزة

## المتطلبات الأساسية

- فهم أساسي لجافا وSpring Boot
- الإلمام بمفاهيم MCP من الوحدات السابقة
- تثبيت Maven أو Gradle

---

## نظرة عامة على المشروع

هذا المشروع هو **تطبيق Spring Boot مبسط** يعمل كـ:

* **خادم تفويض Spring** (يصدر رموز وصول JWT عبر تدفق `client_credentials`), و  
* **خادم موارد** (يحمي نقطة النهاية `/hello` الخاصة به).

هو يعكس الإعداد الموضح في [مدونة Spring (2 أبريل 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## بدء سريع (محلي)

```bash
# استخدم قيمة محلية فريدة واحتفظ بها خارج سجل الأوامر للصدفة حيثما أمكن.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# الحصول على رمز
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# استدعاء نقطة النهاية المحمية
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## اختبار تكوين OAuth2

يمكنك اختبار تكوين أمان OAuth2 باستخدام الخطوات التالية:

### 1. تحقق من تشغيل الخادم وأمانه

```bash
# يجب أن تُرجع 401 غير مصرح، مما يؤكد أن أمان OAuth2 نشط
curl -v http://localhost:8081/
```

### 2. الحصول على رمز وصول باستخدام بيانات اعتماد العميل

```bash
# احصل على استجابة رمز كاملة واستخرجها
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# أو لاستخراج الرمز فقط (يتطلب jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

على PowerShell، قم بتعيين السر المحلي قبل تشغيل Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. الوصول إلى نقطة النهاية المحمية باستخدام الرمز

```bash
# باستخدام الرمز المحفوظ
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# أو مباشرةً باستخدام قيمة الرمز
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

استجابة ناجحة مع "Hello from MCP OAuth2 Demo!" تؤكد أن تكوين OAuth2 يعمل بشكل صحيح.

---

## بناء الحاوية

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## أمان الإنتاج

لنشر الإنتاج، استخدم مزود هوية مخصص بدلًا من
هذا خادم التفويض الداخلي التجريبي. خزن بيانات الاعتماد في
مخزن أسرار مُدار، قم بتدويرها، استخدم مفاتيح توقيع دائمة، قيد الصلاحيات، و
عيّن مُصدرًا صريحًا. لا تضع سر العميل في التعليمات البرمجية المصدر، أو صور الحاوية، أو
مخططات النشر، أو مخرجات الأوامر.

بالنسبة لتطبيقات الحاويات في Azure، خزن القيمة كسر لتطبيقات الحاويات مدعوم بواسطة
Key Vault حيثما أمكن، ثم اعرض فقط مرجع السر عبر
متغير البيئة `OAUTH_CLIENT_SECRET`.

---

## النشر إلى **تطبيقات الحاويات في Azure**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

يصبح FQDN الدخول هو **المُصدر** (`https://<fqdn>`).  
تقدم Azure شهادة TLS موثوقة تلقائيًا لـ `*.azurecontainerapps.io`.

---

## الربط مع **إدارة واجهة برمجة التطبيقات Azure**

أضف هذه السياسة الواردة إلى API الخاص بك:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

ستقوم APIM بجلب JWKS والتحقق من صحة كل طلب.

---

## ما التالي

- [5.4 سياقات الجذر](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->