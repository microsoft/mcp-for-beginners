# Демонстрація MCP OAuth2

> [!WARNING]
> Це локальний навчальний приклад, а не сервіс авторизації для продуктивного використання. Він
> використовує клієнт в пам’яті та генерує новий ключ підпису при запуску. Ніколи не
> розгортайте його з загальним, типовим або контрольованим в системі контролю версій секретом клієнта.

## Вступ

OAuth2 — це стандартний у галузі протокол авторизації, який забезпечує безпечний доступ до ресурсів без спільного використання облікових даних. У реалізаціях MCP (Model Context Protocol) OAuth2 забезпечує надійний спосіб аутентифікації та авторизації клієнтів (наприклад, агентів штучного інтелекту) для доступу до MCP-серверів та їх інструментів.

Цей урок демонструє, як реалізувати аутентифікацію OAuth2 для MCP-серверів за допомогою Spring Boot — поширеного підходу для корпоративних та продуктивних розгортань.

## Цілі навчання

До кінця цього уроку ви:
- Зрозумієте, як OAuth2 інтегрується з MCP-серверами
- Реалізуєте Spring Authorization Server для видачі токенів
- Захистите кінцеві точки MCP за допомогою аутентифікації на основі JWT
- Налаштуєте flow client credentials для машинного взаємозв’язку

## Вимоги

- Базові знання Java та Spring Boot
- Знайомство з концепціями MCP з попередніх модулів
- Встановлений Maven або Gradle

---

## Огляд проєкту

Цей проєкт — **мінімальний додаток на Spring Boot**, який виконує обидві ролі:

* **Сервер авторизації Spring** (який видає JWT-ключі доступу через flow `client_credentials`), та  
* **Ресурсний сервер** (який захищає власний кінцевий пункт `/hello`).

Він відображає налаштування, показані в [публікації блогу Spring (2 квітня 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Швидкий запуск (локально)

```bash
# Використовуйте унікальне локальне значення і за можливості тримайте його поза історією shell.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# отримати токен
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# викликати захищений кінцевий пункт
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Тестування конфігурації OAuth2

Ви можете протестувати конфігурацію безпеки OAuth2 наступними кроками:

### 1. Перевірте, що сервер працює і захищений

```bash
# Це має повернути 401 Unauthorized, підтверджуючи, що безпека OAuth2 активна
curl -v http://localhost:8081/
```

### 2. Отримайте токен доступу за допомогою client credentials

```bash
# Отримати та витягти повну відповідь токена
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Або витягти лише токен (потребує jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

В PowerShell встановіть локальний секрет перед запуском Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Отримайте доступ до захищеного кінцевого пункту за допомогою токена

```bash
# Використання збереженого токена
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Або безпосередньо зі значенням токена
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успішна відповідь із "Hello from MCP OAuth2 Demo!" підтверджує, що конфігурація OAuth2 працює правильно.

---

## Збірка контейнера

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Безпека для продуктивного середовища

Для продуктивного розгортання використовуйте спеціалізованого провайдера ідентичності, а не
цей демонстраційний сервер авторизації в процесі виконання. Зберігайте облікові дані в керованому
сховищі секретів, регулярно їх обновляйте, використовуйте стійкі ключі підпису, обмежуйте області доступу та
задавайте явного видавця. Ніколи не розміщуйте секрет клієнта в коді, образах контейнера,
манифестах розгортання або у виводі команд.

Для Azure Container Apps зберігайте значення в секреті Container Apps, підтримуваному
Key Vault, якщо це можливо, а потім відкривайте лише посилання на секрет через
змінну оточення `OAUTH_CLIENT_SECRET`.

---

## Розгортання в **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ім’я домену входу (FQDN) стає вашим **видавцем** (`https://<fqdn>`).  
Azure автоматично надає довірений TLS-сертифікат для `*.azurecontainerapps.io`.

---

## Інтеграція з **Azure API Management**

Додайте цю політику вхідних запитів до вашого API:

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->