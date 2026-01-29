# عرض توضيحي لـ MCP OAuth2

هذا المشروع هو **تطبيق Spring Boot بسيط** يعمل كـ:

* **خادم تفويض Spring** (يصدر رموز وصول JWT عبر تدفق `client_credentials`)، و  
* **خادم موارد** (يحمي نقطة النهاية الخاصة به `/hello`).

يُطابق الإعداد المعروض في [مقالة مدونة Spring (2 أبريل 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## بداية سريعة (محليًا)

```bash
# build & run
./mvnw spring-boot:run

# obtain a token
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## اختبار إعداد OAuth2

يمكنك اختبار إعداد أمان OAuth2 باتباع الخطوات التالية:

### 1. تحقق من أن الخادم يعمل ومؤمن

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. الحصول على رمز وصول باستخدام بيانات اعتماد العميل

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

ملاحظة: رأس المصادقة الأساسية (`bWNwLWNsaWVudDpzZWNyZXQ=`) هو الترميز Base64 لـ `mcp-client:secret`.

### 3. الوصول إلى نقطة النهاية المحمية باستخدام الرمز

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

الرد الناجح مع "Hello from MCP OAuth2 Demo!" يؤكد أن إعداد OAuth2 يعمل بشكل صحيح.

---

## بناء الحاوية

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## النشر على **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

يصبح اسم المجال الكامل للمدخل هو **المُصدر** الخاص بك (`https://<fqdn>`).  
توفر Azure شهادة TLS موثوقة تلقائيًا لـ `*.azurecontainerapps.io`.

---

## الربط مع **Azure API Management**

أضف سياسة الدخول هذه إلى واجهة برمجة التطبيقات الخاصة بك:

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

سيقوم APIM بجلب JWKS والتحقق من كل طلب.

---

## ما التالي

- [5.4 الجذور السياقية](../mcp-root-contexts/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.