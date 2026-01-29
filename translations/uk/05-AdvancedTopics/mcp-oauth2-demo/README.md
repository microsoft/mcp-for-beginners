# MCP OAuth2 Demo

Цей проєкт — **мінімальний Spring Boot додаток**, який виконує роль як:

* **Spring Authorization Server** (видає JWT токени доступу через `client_credentials` flow), так і  
* **Resource Server** (захищає власний ендпоінт `/hello`).

Він відтворює налаштування, показані в [публікації блогу Spring (2 квітня 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Швидкий старт (локально)

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

## Тестування конфігурації OAuth2

Ви можете перевірити налаштування безпеки OAuth2 за допомогою наступних кроків:

### 1. Переконайтеся, що сервер працює і захищений

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Отримайте токен доступу, використовуючи client credentials

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

Примітка: заголовок Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) — це Base64-кодування рядка `mcp-client:secret`.

### 3. Отримайте доступ до захищеного ендпоінту, використовуючи токен

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успішна відповідь з повідомленням "Hello from MCP OAuth2 Demo!" підтверджує, що конфігурація OAuth2 працює правильно.

---

## Збірка контейнера

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Розгортання в **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ім'я FQDN для входу стає вашим **issuer** (`https://<fqdn>`).  
Azure автоматично надає довірений TLS сертифікат для `*.azurecontainerapps.io`.

---

## Інтеграція з **Azure API Management**

Додайте цю політику inbound до вашого API:

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

APIM завантажить JWKS і перевірятиме кожен запит.

---

## Що далі

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.