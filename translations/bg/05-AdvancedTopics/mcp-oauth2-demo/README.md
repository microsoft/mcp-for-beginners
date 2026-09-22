# MCP OAuth2 Демонстрация

> [!WARNING]
> Това е локален учебен пример, а не производствена услуга за упълномощаване. Той
> използва клиент в паметта и генерира нов ключ за подписване при стартиране. Никога
> не го разгръщайте с споделен, по подразбиране или контролиращ се от изходен код клиентски таен ключ.

## Въведение

OAuth2 е индустриалният стандартен протокол за упълномощаване, позволяващ сигурен достъп до ресурси без споделяне на идентификационни данни. В имплементациите на MCP (Model Context Protocol) OAuth2 предоставя стабилен начин за удостоверяване и упълномощаване на клиенти (като AI агенти) за достъп до MCP сървъри и техните инструменти.

Този урок демонстрира как да се реализира OAuth2 удостоверяване за MCP сървъри с помощта на Spring Boot, често използван модел за корпоративни и производствени разгръщания.

## Цели на урока

Към края на урока ще:
- Разберете как OAuth2 се интегрира с MCP сървъри
- Реализирате Spring Authorization Server за издаване на токени
- Защитите MCP крайни точки с JWT-базирано удостоверяване
- Конфигурирате поток с клиентски идентификационни данни за комуникация машина-до-машина

## Предварителни изисквания

- Основни познания по Java и Spring Boot
- Запознатост с MCP концепции от по-ранни модули
- Инсталирани Maven или Gradle

---

## Преглед на проекта

Този проект е **минимално Spring Boot приложение**, което действа както:

* **Spring Authorization Server** (издаващ JWT достъпни токени чрез `client_credentials` поток), и  
* **Resource Server** (защитаващ собствената си крайна точка `/hello`).

Той отразява настройката, показана в [блог поста на Spring (2 април 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Бърз старт (локално)

```bash
# Използвайте уникална локална стойност и я пазете извън историята на shell, където е възможно.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# получаване на токен
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# извикване на защитения краен пункт
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Тестване на OAuth2 конфигурацията

Можете да тествате сигурността с OAuth2 чрез следните стъпки:

### 1. Проверете дали сървърът работи и е защитен

```bash
# Това трябва да върне 401 Unauthorized, потвърждавайки, че OAuth2 сигурността е активна
curl -v http://localhost:8081/
```

### 2. Вземете достъп токен чрез клиентски идентификационни данни

```bash
# Вземете и извлечете пълния отговор с токена
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Или за да извлечете само токена (изисква jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

В PowerShell задайте локалния таен ключ преди да стартирате Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Достъп до защитената крайна точка с токена

```bash
# Използване на запазения токен
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Или директно със стойността на токена
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Успешен отговор с "Hello from MCP OAuth2 Demo!" потвърждава, че OAuth2 конфигурацията работи правилно.

---

## Създаване на контейнер

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Производствена сигурност

За производствено разгръщане използвайте отделен доставчик на идентичност, а не
този демонстрационен сървър за упълномощаване с процес в приложение. Съхранявайте идентификационните данни в управляван
тайник, извършвайте ротация, използвайте постоянни ключове за подписване, ограничавайте обхватите и
задайте явен издател. Никога не поставяйте клиентски таен ключ в изходния код, контейнери,
манифести за разгръщане или изход на команди.

За Azure Container Apps съхранявайте стойността като секрет в Container Apps, подкрепен от
Key Vault, когато е възможно, и след това излагайте само референция към секрета чрез
`OAUTH_CLIENT_SECRET` променливата на средата.

---

## Разгръщане в **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Входящото FQDN става вашия **издател** (`https://<fqdn>`).  
Azure автоматично предоставя доверен TLS сертификат за `*.azurecontainerapps.io`.

---

## Свързване с **Azure API Management**

Добавете тази входяща политика към вашия API:

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

APIM ще извлича JWKS и ще валидира всяка заявка.

---

## Какво следва

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->