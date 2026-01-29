# Развертывание приложения Spring AI MCP в Azure Container Apps

 ([Защита серверов Spring AI MCP с помощью OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Иллюстрация: сервер Spring AI MCP, защищённый с помощью Spring Authorization Server. Сервер выдаёт клиентам токены доступа и проверяет их при входящих запросах (источник: блог Spring) ([Защита серверов Spring AI MCP с помощью OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Для развертывания сервера Spring MCP соберите его в контейнер и используйте Azure Container Apps с внешним входом. Например, с помощью Azure CLI можно выполнить:

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

Это создаст общедоступное приложение Container App с включённым HTTPS (Azure выдаёт бесплатный TLS-сертификат для домена по умолчанию `*.azurecontainerapps.io` ([Пользовательские домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). В выводе команды будет указан FQDN приложения (например, `my-mcp-app.eastus.azurecontainerapps.io`), который станет базовым **URL издателя**. Убедитесь, что HTTP-вход включён (как указано выше), чтобы APIM мог обращаться к приложению. В тестовой или девелоперской среде используйте опцию `--ingress external` (или привяжите пользовательский домен с TLS согласно [документации Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Пользовательские домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Храните любые чувствительные данные (например, секреты OAuth-клиентов) в секретах Container Apps или Azure Key Vault и передавайте их в контейнер через переменные окружения.

## Настройка Spring Authorization Server

В коде вашего Spring Boot приложения подключите стартеры Spring Authorization Server и Resource Server. Настройте `RegisteredClient` (для гранта `client_credentials` в dev/test) и источник ключей JWT. Например, в `application.properties` можно указать:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Включите Authorization Server и Resource Server, определив цепочку фильтров безопасности. Например:

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

Эта конфигурация откроет стандартные OAuth2 эндпоинты: `/oauth2/token` для получения токенов и `/oauth2/jwks` для набора JSON Web Key Set. (По умолчанию Spring `AuthorizationServerSettings` сопоставляет `/oauth2/token` и `/oauth2/jwks` ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сервер будет выдавать JWT токены доступа, подписанные RSA-ключом, и публиковать публичный ключ по адресу `https://<your-app>:/oauth2/jwks`.

**Включите OpenID Connect discovery:** Чтобы APIM мог автоматически получать URL издателя и JWKS, активируйте endpoint конфигурации провайдера OIDC, добавив `.oidc(Customizer.withDefaults())` в вашу конфигурацию безопасности ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Например:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Это откроет `/.well-known/openid-configuration`, который APIM использует для получения метаданных. Наконец, возможно, вам захочется настроить JWT-клейм **audience**, чтобы проверка `<audiences>` в APIM проходила успешно. Например, добавьте кастомизацию токена:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Это гарантирует, что в токенах будет `"aud": ["mcp-client"]`, совпадающее с ID клиента или ожидаемой областью APIM.

## Открытие эндпоинтов Token и JWKS

После развертывания URL вашего приложения-издателя будет `https://<app-fqdn>`, например, `https://my-mcp-app.eastus.azurecontainerapps.io`. Его OAuth2 эндпоинты:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – здесь клиенты получают токены (поток client_credentials).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – возвращает набор JWK (используется APIM для получения ключей подписи).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON для OIDC discovery (содержит `issuer`, `token_endpoint`, `jwks_uri` и др.).

APIM будет использовать **URL конфигурации OpenID**, откуда узнаёт `jwks_uri`. Например, если FQDN вашего Container App — `my-mcp-app.eastus.azurecontainerapps.io`, то в `<openid-config url="...">` APIM укажите `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (По умолчанию Spring выставит `issuer` в этих метаданных равным базовому URL ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Настройка Azure API Management (`validate-jwt`)

В Azure APIM добавьте входящую политику, использующую `<validate-jwt>`, чтобы проверять входящие JWT от вашего Spring Authorization Server. Для простой настройки можно использовать URL метаданных OpenID Connect. Пример фрагмента политики:

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

Эта политика указывает APIM получить конфигурацию OpenID с сервера Spring Auth, загрузить JWKS и проверить, что каждый токен подписан доверенным ключом и имеет правильный audience. (Если не указывать `<issuers>`, APIM автоматически возьмёт `issuer` из метаданных.) `<audience>` должен совпадать с вашим client ID или идентификатором API в токене (в примере выше — `"mcp-client"`). Это соответствует документации Microsoft по использованию `validate-jwt` с `<openid-config>` ([Справочник по политикам Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

После проверки APIM перенаправит запрос (включая оригинальный заголовок `Authorization`) на бэкенд. Поскольку Spring-приложение также является ресурсным сервером, оно повторно проверит токен, но APIM уже гарантировал его валидность. (Для разработки можно полагаться на проверку APIM и отключить дополнительные проверки в приложении, но безопаснее оставить обе.)

## Пример настроек

| Параметр           | Пример значения                                                    | Примечания                                 |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL вашего Container App (базовый URI)     |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Стандартный endpoint Spring для токенов ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Стандартный endpoint для JWK Set ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Документ OIDC discovery (генерируется автоматически) |
| **APIM audience**  | `mcp-client`                                                      | OAuth client ID или имя ресурса API        |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` использует этот URL ([Справочник по политикам Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Распространённые ошибки

- **HTTPS/TLS:** Шлюз APIM требует, чтобы OpenID/JWKS эндпоинты были доступны по HTTPS с действительным сертификатом. По умолчанию Azure Container Apps предоставляет доверенный TLS-сертификат для домена, управляемого Azure ([Пользовательские домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Если вы используете пользовательский домен, обязательно привяжите сертификат (можно использовать бесплатный управляемый сертификат Azure) ([Пользовательские домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Если APIM не сможет доверять сертификату эндпоинта, `<validate-jwt>` не сможет получить метаданные.

- **Доступность эндпоинтов:** Убедитесь, что эндпоинты Spring-приложения доступны из APIM. Использование `--ingress external` (или включение входа в портале) — самый простой способ. Если вы выбрали внутреннюю или vNet-связанную среду, APIM (по умолчанию публичный) может не иметь доступа, если не находится в той же VNet. В тестовой среде предпочтительнее использовать публичный вход, чтобы APIM мог обращаться к `.well-known` и `/jwks`.

- **Включён OpenID Discovery:** По умолчанию Spring Authorization Server **не открывает** `/.well-known/openid-configuration`, если OIDC не включён. Обязательно добавьте `.oidc(Customizer.withDefaults())` в конфигурацию безопасности (см. выше), чтобы endpoint конфигурации провайдера был активен ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Иначе вызов `<openid-config>` в APIM вернёт 404.

- **Клейм Audience:** По умолчанию Spring устанавливает `aud` равным client ID. Если проверка `<audience>` в APIM не проходит, возможно, потребуется кастомизировать токен (как показано выше) или скорректировать политику APIM. Убедитесь, что audience в JWT совпадает с тем, что указано в `<audience>`.

- **Парсинг JSON метаданных:** JSON конфигурации OpenID должен быть корректным. Стандартная конфигурация Spring выдаёт валидный документ OIDC. Проверьте, что в нём правильно указаны `issuer` и `jwks_uri`. Если вы размещаете Spring за прокси или с маршрутизацией по путям, внимательно проверьте URL в метаданных. APIM использует эти значения без изменений.

- **Порядок политик:** В политике APIM разместите `<validate-jwt>` **до** любых маршрутов на бэкенд. Иначе запросы могут попасть в приложение без валидного токена. Также убедитесь, что `<validate-jwt>` находится непосредственно внутри `<inbound>` (не вложен в другие условия), чтобы APIM применял его.

Следуя этим рекомендациям, вы сможете запустить сервер Spring AI MCP в Azure Container Apps и настроить Azure API Management для проверки входящих OAuth2 JWT с минимальной политикой. Основные моменты: открывайте публично Spring Auth эндпоинты с TLS, включайте OIDC discovery и указывайте в `validate-jwt` URL конфигурации OpenID (чтобы JWKS подтягивался автоматически). Такая схема подходит для dev/test среды; для продакшена учитывайте управление секретами, время жизни токенов и ротацию ключей JWKS по мере необходимости.
**Ссылки:** См. документацию Spring Authorization Server для стандартных конечных точек ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) и настройки OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); см. документацию Microsoft APIM для примеров `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); а также документацию Azure Container Apps по развертыванию и сертификатам ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.