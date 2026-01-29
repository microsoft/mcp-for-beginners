# MCP OAuth2 ডেমো

এই প্রজেক্টটি একটি **সর্বনিম্ন Spring Boot অ্যাপ্লিকেশন** যা একই সাথে কাজ করে:

* একটি **Spring Authorization Server** (যা `client_credentials` ফ্লো ব্যবহার করে JWT অ্যাক্সেস টোকেন ইস্যু করে), এবং  
* একটি **Resource Server** (যা নিজের `/hello` এন্ডপয়েন্টকে সুরক্ষিত করে)।

এটি [Spring ব্লগ পোস্ট (2 এপ্রিল 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) এ দেখানো সেটআপের প্রতিফলন।

---

## দ্রুত শুরু (লোকাল)

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

## OAuth2 কনফিগারেশন পরীক্ষা করা

নিম্নলিখিত ধাপগুলো অনুসরণ করে আপনি OAuth2 সিকিউরিটি কনফিগারেশন পরীক্ষা করতে পারেন:

### 1. সার্ভার চলছে এবং সুরক্ষিত আছে কিনা যাচাই করুন

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. ক্লায়েন্ট ক্রেডেনশিয়াল ব্যবহার করে অ্যাক্সেস টোকেন নিন

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

দ্রষ্টব্য: Basic Authentication হেডার (`bWNwLWNsaWVudDpzZWNyZXQ=`) হলো `mcp-client:secret` এর Base64 এনকোডিং।

### 3. টোকেন ব্যবহার করে সুরক্ষিত এন্ডপয়েন্টে প্রবেশ করুন

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" সহ সফল রেসপন্স পাওয়া মানে OAuth2 কনফিগারেশন সঠিকভাবে কাজ করছে।

---

## কন্টেইনার বিল্ড

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** এ ডিপ্লয় করুন

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

ইনগ্রেস FQDN আপনার **issuer** হয়ে যাবে (`https://<fqdn>`)।  
Azure স্বয়ংক্রিয়ভাবে `*.azurecontainerapps.io` এর জন্য একটি বিশ্বাসযোগ্য TLS সার্টিফিকেট প্রদান করে।

---

## **Azure API Management** এর সাথে সংযুক্ত করুন

আপনার API তে এই ইনবাউন্ড পলিসি যোগ করুন:

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

APIM JWKS নিয়ে আসবে এবং প্রতিটি রিকোয়েস্ট যাচাই করবে।

---

## পরবর্তী ধাপ

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।