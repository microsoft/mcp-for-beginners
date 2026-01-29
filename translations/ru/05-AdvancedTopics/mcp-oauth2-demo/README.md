# MCP OAuth2 Demo

Этот проект — **минимальное Spring Boot приложение**, которое выполняет две роли одновременно:

* **Spring Authorization Server** (выдаёт JWT access токены через поток `client_credentials`), и  
* **Resource Server** (защищает собственный эндпоинт `/hello`).

Он повторяет настройку, показанную в [посте в блоге Spring (2 апреля 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Быстрый старт (локально)

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

## Тестирование конфигурации OAuth2

Вы можете проверить настройку безопасности OAuth2, выполнив следующие шаги:

### 1. Убедитесь, что сервер запущен и защищён

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Получите access токен с помощью client credentials

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

Примечание: заголовок Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) — это Base64-кодировка строки `mcp-client:secret`.

### 3. Получите доступ к защищённому эндпоинту с помощью токена

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успешный ответ с сообщением "Hello from MCP OAuth2 Demo!" подтверждает, что конфигурация OAuth2 работает корректно.

---

## Сборка контейнера

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Развёртывание в **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Полное доменное имя ingress становится вашим **issuer** (`https://<fqdn>`).  
Azure автоматически предоставляет доверенный TLS-сертификат для `*.azurecontainerapps.io`.

---

## Интеграция с **Azure API Management**

Добавьте эту входящую политику в ваш API:

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

APIM будет получать JWKS и проверять каждый запрос.

---

## Что дальше

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.