# MCP OAuth2 Demo

Този проект е **минимално Spring Boot приложение**, което изпълнява ролята както на:

* **Spring Authorization Server** (издава JWT access токени чрез `client_credentials` flow), и  
* **Resource Server** (защитава собствената си `/hello` крайна точка).

Той отразява конфигурацията, показана в [Spring блог поста (2 април 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Бърз старт (локално)

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

## Тестване на OAuth2 конфигурацията

Можете да тествате OAuth2 сигурността с следните стъпки:

### 1. Проверете дали сървърът работи и е защитен

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Вземете access токен чрез client credentials

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

Забележка: Basic Authentication хедърът (`bWNwLWNsaWVudDpzZWNyZXQ=`) е Base64 кодираното `mcp-client:secret`.

### 3. Достъп до защитената крайна точка с токена

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успешен отговор с "Hello from MCP OAuth2 Demo!" потвърждава, че OAuth2 конфигурацията работи правилно.

---

## Създаване на контейнер

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Деплой в **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN става вашият **issuer** (`https://<fqdn>`).  
Azure автоматично предоставя доверен TLS сертификат за `*.azurecontainerapps.io`.

---

## Свързване с **Azure API Management**

Добавете тази inbound политика към вашето API:

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

APIM ще изтегли JWKS и ще валидира всяка заявка.

---

## Какво следва

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.