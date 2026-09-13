# Демонстрация MCP OAuth2

> [!WARNING]
> Это локальный учебный пример, а не продакшн-сервис авторизации. Он
> использует клиента в памяти и генерирует новый ключ подписи при запуске. Никогда
> не разворачивайте его с общим, стандартным или управляемым через систему контроля версиями секретом клиента.

## Введение

OAuth2 — это отраслевой стандартный протокол авторизации, позволяющий безопасно получать доступ к ресурсам без передачи учетных данных. В реализациях MCP (Model Context Protocol) OAuth2 обеспечивает надежный способ аутентификации и авторизации клиентов (например, AI-агентов) для доступа к MCP-серверам и их инструментам.

В этом уроке показано, как реализовать аутентификацию OAuth2 для MCP-серверов с использованием Spring Boot — общей схемы для корпоративных и производственных развертываний.

## Цели обучения

К концу этого урока вы:
- Поймете, как OAuth2 интегрируется с MCP-серверами
- Реализуете сервер авторизации Spring для выдачи токенов
- Защитите MCP endpoints с помощью аутентификации на основе JWT
- Настроите поток client credentials для взаимодействия машина с машиной

## Требования

- Базовые знания Java и Spring Boot
- Знакомство с концепциями MCP из предыдущих модулей
- Установленный Maven или Gradle

---

## Обзор проекта

Этот проект — **минимальное Spring Boot приложение**, которое выполняет две функции:

* **сервер авторизации Spring** (выдающий JWT токены доступа через поток `client_credentials`), и  
* **ресурсный сервер** (защищающий собственный endpoint `/hello`).

Он повторяет конфигурацию, описанную в [публикации в блоге Spring (2 апреля 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Быстрый старт (локально)

```bash
# Используйте уникальное локальное значение и по возможности не сохраняйте его в истории оболочки.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# получить токен
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# вызвать защищённый конечный пункт
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Тестирование конфигурации OAuth2

Вы можете проверить конфигурацию безопасности OAuth2 следующими шагами:

### 1. Убедитесь, что сервер запущен и защищен

```bash
# Это должно вернуть 401 Unauthorized, подтверждая, что безопасность OAuth2 активна
curl -v http://localhost:8081/
```

### 2. Получите токен доступа, используя учетные данные клиента

```bash
# Получить и извлечь полный ответ с токеном
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Или извлечь только токен (требуется jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

В PowerShell задайте локальный секрет перед запуском Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Обратитесь к защищенному endpoint с использованием токена

```bash
# Использование сохраненного токена
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Или напрямую с значением токена
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успешный ответ с "Hello from MCP OAuth2 Demo!" подтверждает корректную работу конфигурации OAuth2.

---

## Сборка контейнера

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Безопасность в продакшене

Для производственного развертывания используйте выделенного провайдера идентификации, а не
этот демонстрационный сервер авторизации, работающий в одном процессе. Храните учетные данные в управляемом
хранилище секретов, обновляйте их, используйте постоянные ключи подписи, ограничивайте области доступа и
задавайте явного издателя. Никогда не размещайте секрет клиента в исходном коде, образах контейнеров,
манифестах развертывания или выводе команд.

Для Azure Container Apps по возможности храните значение как секрет Container Apps, поддерживаемый
Key Vault, а затем предоставляйте только ссылку на секрет через
переменную окружения `OAUTH_CLIENT_SECRET`.

---

## Развертывание в **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

FQDN входящего трафика становится вашим **издателем** (`https://<fqdn>`).  
Azure автоматически предоставляет надежный TLS-сертификат для `*.azurecontainerapps.io`.

---

## Интеграция с **Azure API Management**

Добавьте эту политику входящего трафика в ваш API:

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

APIM загрузит JWKS и будет валидировать каждый запрос.

---

## Что дальше

- [5.4 Корневые контексты](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->