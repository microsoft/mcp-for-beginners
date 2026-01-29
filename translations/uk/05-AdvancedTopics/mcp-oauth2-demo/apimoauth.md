# Розгортання Spring AI MCP додатку в Azure Container Apps

 ([Захист серверів Spring AI MCP за допомогою OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Ілюстрація: Сервер Spring AI MCP захищений Spring Authorization Server. Сервер видає клієнтам токени доступу та перевіряє їх при вхідних запитах (джерело: Spring blog) ([Захист серверів Spring AI MCP за допомогою OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Для розгортання Spring MCP сервера зберіть його у контейнер і використовуйте Azure Container Apps з зовнішнім ingress. Наприклад, за допомогою Azure CLI можна виконати:

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

Це створює публічно доступний Container App з увімкненим HTTPS (Azure видає безкоштовний TLS сертифікат для домену за замовчуванням `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). У виводі команди буде FQDN додатку (наприклад, `my-mcp-app.eastus.azurecontainerapps.io`), який стає базою для **issuer URL**. Переконайтеся, що HTTP ingress увімкнено (як показано вище), щоб APIM міг дістатися додатку. Для тестового/розробницького середовища використовуйте опцію `--ingress external` (або прив’яжіть власний домен з TLS відповідно до [документації Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Зберігайте будь-які конфіденційні властивості (наприклад, секрети OAuth клієнтів) у секретах Container Apps або Azure Key Vault і передавайте їх у контейнер як змінні середовища.

## Налаштування Spring Authorization Server

У коді вашого Spring Boot додатку додайте стартери Spring Authorization Server та Resource Server. Налаштуйте `RegisteredClient` (для `client_credentials` гранту у dev/test) та джерело ключів JWT. Наприклад, у `application.properties` можна вказати:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Увімкніть Authorization Server та Resource Server, визначивши security filter chain. Наприклад:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Enable the Authorization Server endpoints
            .apply(authzServer.and())
            // Enable the Resource Server (validate JWT on incoming requests)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Disable CSRF (MCP server is not browser-based)
            .csrf(csrf -> csrf.disable())
            // Allow CORS for client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Define an in-memory client (RegisteredClient) and a JWK source:
    @Bean
    public RegisteredClientRepository registeredClientRepository() {
        RegisteredClient client = RegisteredClient.withId("1")
            .clientId("mcp-client")
            .clientSecret("{noop}secret")
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Generate an RSA key (for dev/test, generate anew at startup)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ця конфігурація відкриє стандартні OAuth2 кінцеві точки: `/oauth2/token` для отримання токенів та `/oauth2/jwks` для JSON Web Key Set. (За замовчуванням Spring `AuthorizationServerSettings` відображає `/oauth2/token` та `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сервер видаватиме JWT токени доступу, підписані RSA ключем, і публікуватиме свій публічний ключ за адресою `https://<your-app>:/oauth2/jwks`.

**Увімкнення OpenID Connect discovery:** Щоб APIM міг автоматично отримувати issuer та JWKS, увімкніть endpoint конфігурації OIDC провайдера, додавши `.oidc(Customizer.withDefaults())` у вашу конфігурацію безпеки ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Наприклад:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Це відкриває `/.well-known/openid-configuration`, який APIM використовує для отримання метаданих. Нарешті, можливо, захочете налаштувати JWT **audience** claim, щоб перевірка `<audiences>` в APIM пройшла успішно. Наприклад, додайте кастомізатор токенів:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Це гарантує, що токени містять `"aud": ["mcp-client"]`, що відповідає client ID або очікуваному scope в APIM.

## Відкриття кінцевих точок Token та JWKS

Після розгортання ваш **issuer URL** буде `https://<app-fqdn>`, наприклад `https://my-mcp-app.eastus.azurecontainerapps.io`. OAuth2 кінцеві точки:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – тут клієнти отримують токени (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – повертає набір JWK (APIM використовує для отримання ключів підпису).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON для OIDC discovery (містить `issuer`, `token_endpoint`, `jwks_uri` тощо).

APIM вказує на **OpenID configuration URL**, звідки отримує `jwks_uri`. Наприклад, якщо FQDN вашого Container App `my-mcp-app.eastus.azurecontainerapps.io`, то `<openid-config url="...">` в APIM має бути `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (За замовчуванням Spring встановлює `issuer` у цих метаданих на той самий базовий URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Налаштування Azure API Management (`validate-jwt`)

В Azure APIM додайте вхідну політику, яка використовує `<validate-jwt>` для перевірки вхідних JWT проти вашого Spring Authorization Server. Для простої конфігурації можна використати URL метаданих OpenID Connect. Приклад фрагменту політики:

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

Ця політика вказує APIM отримати OpenID конфігурацію з Spring Auth Server, завантажити JWKS і перевірити, що кожен токен підписаний довіреним ключем і має правильний audience. (Якщо опустити `<issuers>`, APIM автоматично використовує `issuer` з метаданих.) `<audience>` має відповідати вашому client ID або ідентифікатору API ресурсу в токені (у наведеному прикладі це `"mcp-client"`). Це відповідає документації Microsoft щодо використання `validate-jwt` з `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Після перевірки APIM пересилає запит (включно з оригінальним заголовком `Authorization`) на бекенд. Оскільки Spring додаток також є resource server, він повторно перевірить токен, але APIM вже гарантує його дійсність. (Для розробки можна покладатися на перевірку APIM і вимкнути додаткові перевірки в додатку, але безпечніше зберігати обидві.)

## Приклад налаштувань

| Налаштування       | Приклад значення                                                   | Примітки                                   |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL вашого Container App (базовий URI)     |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Стандартна кінцева точка Spring для токенів ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Стандартна кінцева точка для JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Документ OIDC discovery (генерується автоматично) |
| **APIM audience**  | `mcp-client`                                                      | OAuth client ID або ім’я API ресурсу       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` використовує цей URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Типові помилки

- **HTTPS/TLS:** APIM gateway вимагає, щоб OpenID/JWKS endpoint був доступний через HTTPS з дійсним сертифікатом. За замовчуванням Azure Container Apps надає довірений TLS сертифікат для домену, яким керує Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Якщо ви використовуєте власний домен, обов’язково прив’яжіть сертифікат (можна скористатися безкоштовним керованим сертифікатом Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Якщо APIM не довіряє сертифікату endpoint, `<validate-jwt>` не зможе отримати метадані.

- **Доступність кінцевих точок:** Переконайтеся, що кінцеві точки Spring додатку доступні з APIM. Найпростіше використовувати `--ingress external` (або увімкнути ingress у порталі). Якщо ви обрали внутрішнє або vNet-середовище, APIM (за замовчуванням публічний) може не мати доступу, якщо не розміщений у тій же VNet. Для тестування краще використовувати публічний ingress, щоб APIM міг викликати `.well-known` та `/jwks` URL.

- **Увімкнення OpenID Discovery:** За замовчуванням Spring Authorization Server **не відкриває** `/.well-known/openid-configuration`, якщо OIDC не увімкнено. Обов’язково додайте `.oidc(Customizer.withDefaults())` у конфігурацію безпеки (див. вище), щоб endpoint конфігурації провайдера був активним ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Інакше виклик APIM `<openid-config>` поверне 404.

- **Audience Claim:** За замовчуванням Spring встановлює `aud` claim у client ID. Якщо перевірка `<audience>` в APIM не проходить, можливо, потрібно кастомізувати токен (як показано вище) або змінити політику APIM. Переконайтеся, що audience у вашому JWT відповідає тому, що ви вказали в `<audience>`.

- **Парсинг JSON метаданих:** JSON конфігурації OpenID має бути валідним. За замовчуванням Spring генерує стандартний OIDC документ метаданих. Перевірте, що він містить правильні `issuer` та `jwks_uri`. Якщо ви розміщуєте Spring за проксі або з маршрутизацією за шляхом, уважно перевірте URL у метаданих. APIM використовує ці значення без змін.

- **Порядок політик:** У політиці APIM розміщуйте `<validate-jwt>` **перед** будь-яким маршрутизуванням на бекенд. Інакше запити можуть доходити до додатку без дійсного токена. Також переконайтеся, що `<validate-jwt>` знаходиться безпосередньо під `<inbound>` (не вкладений у інші умови), щоб APIM застосував його.

Дотримуючись цих кроків, ви зможете запустити Spring AI MCP сервер у Azure Container Apps і налаштувати Azure API Management для перевірки вхідних OAuth2 JWT з мінімальною політикою. Головні моменти: відкрийте Spring Auth кінцеві точки публічно з TLS, увімкніть OIDC discovery і вкажіть APIM `validate-jwt` на URL OpenID конфігурації (щоб автоматично отримувати JWKS). Ця конфігурація підходить для dev/test середовища; для продакшену враховуйте належне керування секретами, час життя токенів і ротацію ключів у JWKS за потреби.
**Посилання:** Дивіться документацію Spring Authorization Server для стандартних кінцевих точок ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) та налаштувань OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); дивіться документацію Microsoft APIM для прикладів `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); а також документацію Azure Container Apps щодо розгортання та сертифікатів ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.