# MCP OAuth2 ڈیمو

یہ پروجیکٹ ایک **سادہ Spring Boot ایپلیکیشن** ہے جو دونوں کام کرتی ہے:

* ایک **Spring Authorization Server** کے طور پر (جو `client_credentials` فلو کے ذریعے JWT ایکسیس ٹوکن جاری کرتا ہے)، اور  
* ایک **Resource Server** کے طور پر (جو اپنے `/hello` اینڈپوائنٹ کی حفاظت کرتا ہے)۔

یہ [Spring بلاگ پوسٹ (2 اپریل 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) میں دکھائی گئی ترتیب کی عکاسی کرتا ہے۔

---

## فوری آغاز (لوکل)

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

## OAuth2 کنفیگریشن کی جانچ

آپ OAuth2 سیکیورٹی کنفیگریشن کو درج ذیل مراحل سے آزما سکتے ہیں:

### 1. تصدیق کریں کہ سرور چل رہا ہے اور محفوظ ہے

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. کلائنٹ کریڈینشلز کے ذریعے ایکسیس ٹوکن حاصل کریں

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

نوٹ: Basic Authentication ہیڈر (`bWNwLWNsaWVudDpzZWNyZXQ=`) `mcp-client:secret` کا Base64 انکوڈنگ ہے۔

### 3. ٹوکن استعمال کرتے ہوئے محفوظ اینڈپوائنٹ تک رسائی حاصل کریں

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" کے ساتھ کامیاب جواب اس بات کی تصدیق کرتا ہے کہ OAuth2 کنفیگریشن صحیح طریقے سے کام کر رہی ہے۔

---

## کنٹینر بلڈ

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** پر تعینات کریں

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

انگریس FQDN آپ کا **issuer** بن جاتا ہے (`https://<fqdn>`)۔  
Azure خودکار طور پر `*.azurecontainerapps.io` کے لیے ایک معتبر TLS سرٹیفکیٹ فراہم کرتا ہے۔

---

## **Azure API Management** میں شامل کریں

اپنے API میں یہ inbound پالیسی شامل کریں:

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

APIM JWKS حاصل کرے گا اور ہر درخواست کی تصدیق کرے گا۔

---

## آگے کیا ہے

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔