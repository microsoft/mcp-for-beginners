# MCP OAuth2 Демо

> [!WARNING]
> Ово је локални пример за учење, а не производни сервис за ауторизацију. Користи
> клијента у меморији и генерише нови кључ за потписивање при покретању. Никада
> не постављајте са заједничким, подразумеваним или у контролисаном коду клијентским тајним кључем.

## Увод

OAuth2 је индустријски стандардни протокол за ауторизацију, који омогућава безбедан приступ ресурсима без дељења акредитива. У MCP (Model Context Protocol) имплементацијама, OAuth2 пружа робусан начин да се аутентификују и овласти клијенти (као што су AI агенти) за приступ MCP серверима и њиховим алатима.

Овај пример показује како имплементирати OAuth2 аутентификацију за MCP сервере користећи Spring Boot, уобичајени образац за предузећа и производна окружења.

## Циљеви учења

До краја овог часа ћете:
- Разумети како се OAuth2 интегрише са MCP серверима
- Имплементирати Spring Authorization Server за издавање токена
- Заштитити MCP крајње тачке аутентификацијом заснованом на JWT
- Конфигурисати flow клијентских акредитива за комуникацију машина-с-машином

## Неопходни услови

- Основно познавање Јаве и Spring Boot
- Познавање MCP концепата из претходних модула
- Инсталиран Maven или Gradle

---

## Преглед пројекта

Овај пројекат је **минимална Spring Boot апликација** која делује као и:

* **Spring Authorization Server** (издаје JWT приступне токене преко `client_credentials` flow-а), и  
* **Resource Server** (штити свој `/hello` крајњу тачку).

Ово одговара подешавању приказаном у [Spring блогу (2. април 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Брзи почетак (локално)

```bash
# Користите јединствену локалну вредност и по могућству држите је ван историје шела.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# набавите токен
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# позовите заштићени крајњи пункт
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Тестирање OAuth2 конфигурације

Можете тестирати OAuth2 безбедносну конфигурацију следећим корацима:

### 1. Потврдите да сервер ради и да је заштићен

```bash
# Ово би требало да врати 401 Unauthorized, што потврђује да је OAuth2 безбедност активна
curl -v http://localhost:8081/
```

### 2. Добијте приступни токен користећи клијентске акредитиве

```bash
# Узми и издвоји пун одговор са токеном
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Или да издвојиш само токен (захтева jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

На PowerShell-у поставите локалну тајну вредност пре покретања Mavena:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Приступите заштићеној крајњој тачки користећи токен

```bash
# Користећи сачувани токен
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Или директно са вредношћу токена
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успешан одговор са "Hello from MCP OAuth2 Demo!" потврђује да OAuth2 конфигурација исправно ради.

---

## Изградња контејнера

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Производна безбедност

За производно окружење користите посебног провајдера идентитета уместо
овог демонстрационог сервера за ауторизацију у процесу. Чувајте акредитиве у управљаном
складишту тајни, ротирајте их, користите трајне кључеве за потписивање, ограничавајте опсеге и
дефинишите експлицитног издаваоца. Никада не стављајте клијентске тајне у изворни код, имидже контејнера,
манифесте за распоређивање или излаз команде.

За Azure Container Apps, чувајте вредност као тајну у Container Apps подржану од стране
Key Vault-а где је могуће, а затим излагати само референцу на тајну кроз
`OAUTH_CLIENT_SECRET` променљиву окружења.

---

## Распоређивање на **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Улазни FQDN постаје ваш **издаваоц** (`https://<fqdn>`).  
Azure аутоматски обезбеђује поуздан TLS сертификат за `*.azurecontainerapps.io`.

---

## Повезивање са **Azure API Management**

Додајте ову inbound политику за ваш API:

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

APIM ће преузети JWKS и валидарати сваки захтев.

---

## Шта следи

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->