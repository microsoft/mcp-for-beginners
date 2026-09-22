# Розгортання Spring AI MCP додатку у Azure Container Apps

> [!WARNING]
> Цей об’єднаний сервер авторизації/ресурсів призначений для навчання і
> використання у середовищах розробки/тестування. Виробничі системи повинні використовувати спеціалізованого провайдера ідентичності,
> постійні ключі підпису та облікові дані, збережені у керованому сховищі секретів.

 ([Захист серверів Spring AI MCP за допомогою OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Ілюстрація: Spring AI MCP сервер, захищений Spring Authorization Server. Сервер видає токени доступу клієнтам і перевіряє їх під час вхідних запитів (джерело: Spring blog) ([Захист серверів Spring AI MCP за допомогою OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Для розгортання сервера Spring MCP зберіть його як контейнер і використовуйте Azure Container Apps з зовнішнім інгресом. Наприклад, за допомогою Azure CLI можна виконати:

```bash
az containerapp up \
  --name my-mcp-app \
  --resource-group MyResourceGroup \
  --location eastus \
  --environment MyContainerEnv \
  --image myregistry.azurecr.io/my-mcp-server:latest \
  --ingress external \
  --target-port 8080 \
  --query properties.configuration.ingress.fqdn
```

Це створює загальнодоступний Container App з увімкненим HTTPS (Azure надає безкоштовний TLS сертифікат для домену за замовчуванням `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). У виводі команди є повне доменне ім’я додатку (наприклад, `my-mcp-app.eastus.azurecontainerapps.io`), яке стає базою для **URL видавця**. Переконайтеся, що HTTP інгрес увімкнено (як показано вище), щоб APIM мав доступ до додатку. У тестовому/розробницькому середовищі використовуйте опцію `--ingress external` (або прив’яжіть користувацький домен з TLS відповідно до [документації Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Зберігайте конфіденційні властивості (наприклад, OAuth клієнтські секрети) у секретах Container Apps або Azure Key Vault та відображайте їх у контейнер як змінні оточення.

## Налаштування Spring Authorization Server

В коді вашого Spring Boot додатку включіть стартери Spring Authorization Server та Resource Server. Налаштуйте `RegisteredClient` (для гранту `client_credentials` у dev/test) та джерело ключа JWT. Наприклад, у `application.properties` можна встановити:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Увімкніть Authorization Server та Resource Server, визначивши ланцюжок безпеки (security filter chain). Наприклад:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Увімкнути кінцеві точки сервера авторизації
            .apply(authzServer.and())
            // Увімкнути сервер ресурсів (валідація JWT у вхідних запитах)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Вимкнути CSRF (сервер MCP не базується на браузері)
            .csrf(csrf -> csrf.disable())
            // Дозволити CORS для клієнтських демонстраційних інструментів
            .cors(withDefaults());
        return http.build();
    }

    // Визначити в пам’яті клієнта (RegisteredClient) та джерело JWK:
    @Bean
    public RegisteredClientRepository registeredClientRepository(
        @Value("${demo.oauth.client-id}") String clientId,
        @Value("${demo.oauth.client-secret}") String clientSecret) {
      PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
        RegisteredClient client = RegisteredClient.withId("1")
        .clientId(clientId)
        .clientSecret(encoder.encode(clientSecret))
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Згенерувати RSA ключ (для розробки/тестування генерується щоразу при запуску)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ця конфігурація відкриє стандартні OAuth2 кінцеві точки: `/oauth2/token` для отримання токенів і `/oauth2/jwks` для JSON Web Key Set. (За замовчуванням `AuthorizationServerSettings` Spring налаштовує `/oauth2/token` та `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сервер видаватиме JWT токени доступу, підписані RSA ключем, і публікуватиме свій відкритий ключ за адресою `https://<your-app>:/oauth2/jwks`.

**Увімкнення OpenID Connect discovery:** Щоб APIM автоматично отримував видавця та JWKS, активуйте кінцеву точку конфігурації провайдера OIDC, додавши `.oidc(Customizer.withDefaults())` у вашу конфігурацію безпеки ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Наприклад:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– увімкнути /.well-known/openid-configuration
```

Це відкриє `/.well-known/openid-configuration`, який APIM може використовувати для метаданих. Нарешті, можливо, захочете налаштувати JWT клейм **audience**, щоб перевірка `<audiences>` у APIM пройшла успішно. Наприклад, додайте кастомізатор токенів:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Встановіть власну аудиторію (наприклад, ідентифікатор клієнта або ідентифікатор API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Це гарантує, що токени містять `"aud": ["mcp-client"]`, співпадаючи з ідентифікатором клієнта або очікуваною областю APIM.

## Відкриття кінцевих точок Token та JWKS

Після розгортання **URL видавця** вашого додатку буде `https://<app-fqdn>`, наприклад, `https://my-mcp-app.eastus.azurecontainerapps.io`. Його OAuth2 кінцеві точки:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` — тут клієнти отримують токени (потік client_credentials).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` — повертає набір JWK (використовується APIM для отримання ключів підпису).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` — JSON для OIDC discovery (містить `issuer`, `token_endpoint`, `jwks_uri` тощо).

APIM вказує на **URL конфігурації OpenID**, з якого він отримує `jwks_uri`. Наприклад, якщо ваш FQDN Container App `my-mcp-app.eastus.azurecontainerapps.io`, то `<openid-config url="...">` в APIM має використовувати `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (За замовчуванням Spring встановлює `issuer` у цій метаданій на той самий базовий URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Налаштування Azure API Management (`validate-jwt`)

В Azure APIM додайте вхідну політику, яка використовує `<validate-jwt>` для перевірки вхідних JWT проти вашого Spring Authorization Server. Для простої конфігурації можна використати URL метаданих OpenID Connect. Приклад уривка політики:

```xml
<inbound>
  <validate-jwt header-name="Authorization" require-scheme="Bearer">
    <openid-config url="https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration" />
    <audiences>
      <audience>mcp-client</audience>  <!-- Expected audience in the JWT -->
    </audiences>
    <issuers>
      <issuer>https://my-mcp-app.eastus.azurecontainerapps.io</issuer>
    </issuers>
  </validate-jwt>
  <!-- (optional) other policies -->
</inbound>
```

Ця політика інструктує APIM отримати конфігурацію OpenID від Spring Auth Server, забрати її JWKS та перевірити, що кожен токен підписаний довіреним ключем і має правильний audience. (Якщо пропущено `<issuers>`, APIM автоматично використає клейм `issuer` із метаданих.) `<audience>` має відповідати вашому ідентифікатору клієнта або ідентифікатору API у токені (в прикладі вище встановлено `"mcp-client"`). Це відповідає документації Microsoft щодо використання `validate-jwt` з `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Після перевірки APIM перенаправить запит (включно з оригінальним заголовком `Authorization`) до бекенда. Оскільки Spring додаток також є ресурсним сервером, він повторно перевірить токен, але APIM вже гарантує його дійсність. (Для розробки можна покладатися на перевірку APIM і відключити додаткові перевірки в додатку за потреби, але безпечніше тримати обидві.)

## Приклади налаштувань

| Налаштування       | Приклад значення                                                   | Примітки                                  |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL вашого Container App (базовий URI)   |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Стандартна кінцева точка токенів Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Стандартна кінцева точка JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Документ OIDC discovery (генерується автоматично) |
| **APIM audience**  | `mcp-client`                                                         | Ідентифікатор OAuth клієнта або API      |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | Використання `<validate-jwt>` з цим URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Типові помилки

- **HTTPS/TLS:** шлюз APIM вимагає, щоб кінцеві точки OpenID/JWKS були HTTPS з дійсним сертифікатом. За замовчуванням Azure Container Apps надає довірений TLS сертифікат для керованого домену Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Якщо ви використовуєте користувацький домен, обов’язково прив’яжіть сертифікат (можна використати безкоштовну керовану функцію сертифікатів Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Якщо APIM не довірятиме сертифікату кінцевої точки, `<validate-jwt>` не зможе отримати метадані.

- **Доступність кінцевої точки:** Переконайтеся, що кінцеві точки додатка Spring доступні для APIM. Найпростіше використовувати `--ingress external` (або увімкнути інгрес у порталі). Якщо вибране внутрішнє або прив’язане до vNet середовище, APIM (який за замовчуванням публічний) може не мати доступу, якщо не розміщений у тому ж VNet. У тестовому середовищі рекомендується публічний інгрес, щоб APIM міг звертатися до `.well-known` і `/jwks` URL.

- **Увімкнений OpenID Discovery:** За замовчуванням Spring Authorization Server **не відкриває** `/.well-known/openid-configuration`, якщо OIDC не увімкнено. Обов’язково додайте `.oidc(Customizer.withDefaults())` у конфігурацію безпеки (див. вище), щоб була активна кінцева точка налаштування провайдера ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). В іншому разі виклик `<openid-config>` у APIM поверне 404.

- **Клейм Audience:** Стандартна поведінка Spring — встановити клейм `aud` як ідентифікатор клієнта. Якщо перевірка `<audience>` в APIM не проходить, можливо, потрібно кастомізувати токен (як показано вище) або відкоригувати політику APIM. Переконайтеся, що audience у вашому JWT відповідає конфігурації у `<audience>`.

- **Аналіз JSON метаданих:** JSON OpenID конфігурації повинен бути валідним. Стандартна конфігурація Spring створює типову OIDC метадані. Перевірте, що там присутні правильні значення `issuer` та `jwks_uri`. Якщо хостите Spring за проксі або маршрутами на основі шляху, переконайтеся у правильності URL цих метаданих. APIM використовуватиме ці значення без змін.

- **Порядок політик:** У політиках APIM `<validate-jwt>` слід розмістити **перед** будь-яким маршрутизуванням до бекенду. Інакше виклики можуть доходити до вашого додатку без чинного токена. Також переконайтеся, що `<validate-jwt>` розміщений безпосередньо під `<inbound>` (не вкладений у інший умовний блок), щоб APIM застосував його.

Дотримуючись зазначених кроків, ви можете запустити ваш Spring AI MCP сервер у Azure Container Apps, і Azure API Management перевірятиме OAuth2 JWT токени з мінімальною політикою. Ключові моменти: відкриття Spring Auth кінцевих точок публічно з TLS, увімкнення OIDC discovery, і направлення `validate-jwt` APIM на URL OpenID конфігурації для автоматичного отримання JWKS. Ця конфігурація підходить для середовища розробки/тесту; для продуктивного використання варто розглянути керування секретами, терміни життя токенів та ротацію ключів у JWKS.


**Джерела:** Див. документацію Spring Authorization Server для стандартних кінцевих точок ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) та конфігурації OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); див. документацію Microsoft APIM для прикладів `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); та документацію Azure Container Apps щодо розгортання та сертифікатів ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->