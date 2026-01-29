# MCP OAuth2 Demo

Овај пројекат је **минимална Spring Boot апликација** која служи као:

* **Spring Authorization Server** (који издаје JWT приступне токене преко `client_credentials` флоуа), и  
* **Resource Server** (који штити свој `/hello` ендпоинт).

Ово одговара подешавању приказаном у [Spring блог посту (2. април 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Брзи почетак (локално)

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

## Тестирање OAuth2 конфигурације

Можете тестирати OAuth2 безбедносну конфигурацију следећим корацима:

### 1. Проверите да ли сервер ради и да је заштићен

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Узмите приступни токен користећи client credentials

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

Напомена: Basic Authentication хедер (`bWNwLWNsaWVudDpzZWNyZXQ=`) је Base64 енкодирана вредност за `mcp-client:secret`.

### 3. Приступите заштићеном ендпоинту користећи токен

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успешан одговор са "Hello from MCP OAuth2 Demo!" потврђује да OAuth2 конфигурација исправно функционише.

---

## Изградња контејнера

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Деплој на **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN постаје ваш **issuer** (`https://<fqdn>`).  
Azure аутоматски обезбеђује поуздан TLS сертификат за `*.azurecontainerapps.io`.

---

## Повезивање са **Azure API Management**

Додајте ову inbound политику у ваш API:

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

APIM ће преузимати JWKS и валидарати сваки захтев.

---

## Шта следи

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.