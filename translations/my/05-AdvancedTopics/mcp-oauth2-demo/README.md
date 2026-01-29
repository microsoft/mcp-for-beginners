# MCP OAuth2 Demo

ဤပရောဂျက်သည် **အနည်းဆုံး Spring Boot အက်ပလီကေးရှင်း** ဖြစ်ပြီး အောက်ပါအဖြစ် လုပ်ဆောင်သည်-

* **Spring Authorization Server** (client_credentials flow ဖြင့် JWT access token များထုတ်ပေးခြင်း), နှင့်  
* **Resource Server** (ကိုယ်ပိုင် `/hello` endpoint ကို ကာကွယ်ထားခြင်း) ဖြစ်သည်။

ဒါဟာ [Spring blog post (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) တွင် ဖော်ပြထားသည့် စနစ်နှင့် တူညီသည်။

---

## အမြန်စတင်ခြင်း (local)

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

## OAuth2 ဖွဲ့စည်းမှု စမ်းသပ်ခြင်း

OAuth2 လုံခြုံရေး ဖွဲ့စည်းမှုကို အောက်ပါအဆင့်များဖြင့် စမ်းသပ်နိုင်သည်-

### 1. ဆာဗာ လည်ပတ်နေပြီး လုံခြုံမှုရှိကြောင်း အတည်ပြုပါ

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. client credentials အသုံးပြု၍ access token ရယူပါ

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

မှတ်ချက်- Basic Authentication header (`bWNwLWNsaWVudDpzZWNyZXQ=`) သည် `mcp-client:secret` ကို Base64 encode လုပ်ထားခြင်းဖြစ်သည်။

### 3. token ကို အသုံးပြု၍ ကာကွယ်ထားသော endpoint သို့ ဝင်ရောက်ပါ

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" ဟူသော အောင်မြင်သော တုံ့ပြန်ချက်သည် OAuth2 ဖွဲ့စည်းမှုမှန်ကန်စွာ လည်ပတ်နေကြောင်း အတည်ပြုသည်။

---

## Container တည်ဆောက်ခြင်း

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** သို့ တင်သွင်းခြင်း

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

ingress FQDN သည် သင့် **issuer** (`https://<fqdn>`) ဖြစ်လာမည်။  
Azure သည် `*.azurecontainerapps.io` အတွက် ယုံကြည်စိတ်ချရသော TLS certificate ကို အလိုအလျောက် ပေးအပ်သည်။

---

## **Azure API Management** နှင့် ချိတ်ဆက်ခြင်း

သင့် API တွင် အောက်ပါ inbound policy ကို ထည့်သွင်းပါ-

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

APIM သည် JWKS ကို ရယူပြီး တောင်းဆိုမှုတိုင်းကို စစ်ဆေးမည်ဖြစ်သည်။

---

## နောက်တစ်ဆင့်

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။