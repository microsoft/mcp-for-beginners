# Развертывание приложения Spring AI MCP в Azure Container Apps

> [!WARNING]
> Этот объединенный сервер авторизации/ресурсов предназначен для обучения и
> использования в разработке/тестировании. В продуктивных системах рекомендуется использовать выделенного провайдера идентификации,
> постоянные ключи для подписания и учетные данные, хранящиеся в управляемом хранилище секретов.

 ([Защита серверов Spring AI MCP с помощью OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Рисунок: сервер Spring AI MCP защищен с помощью Spring Authorization Server. Сервер выдает токены доступа клиентам и проверяет их при входящих запросах (источник: блог Spring) ([Защита серверов Spring AI MCP с помощью OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Для развертывания сервера Spring MCP соберите его как контейнер и используйте Azure Container Apps с внешним входом. Например, с помощью Azure CLI можно выполнить:

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

Это создаст общедоступное приложение Container App с включенным HTTPS (Azure выдает бесплатный сертификат TLS для домена по умолчанию `*.azurecontainerapps.io` ([Именованные домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). В выводе команды будет указан FQDN приложения (например, `my-mcp-app.eastus.azurecontainerapps.io`), который станет базой для **URL издателя**. Убедитесь, что HTTP-вход разрешен (как выше), чтобы APIM мог получить доступ к приложению. В тестовой/разработческой среде используйте опцию `--ingress external` (или привяжите пользовательский домен с TLS согласно [документации Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Именованные домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Любые конфиденциальные свойства (например, секреты OAuth клиентов) храните в секретах Container Apps или Azure Key Vault и передавайте их в контейнер в виде переменных окружения.

## Настройка Spring Authorization Server

В коде вашего Spring Boot приложения подключите стартеры Spring Authorization Server и Resource Server. Настройте `RegisteredClient` (для `client_credentials` в dev/test) и источник ключей JWT. Например, в `application.properties` можно задать:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Для включения Authorization Server и Resource Server определите цепочку фильтров безопасности. Например:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Включить конечные точки сервера авторизации
            .apply(authzServer.and())
            // Включить сервер ресурсов (проверять JWT во входящих запросах)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Отключить CSRF (сервер MCP не основан на браузере)
            .csrf(csrf -> csrf.disable())
            // Разрешить CORS для демонстрационных клиентских инструментов
            .cors(withDefaults());
        return http.build();
    }

    // Определить клиент в памяти (RegisteredClient) и источник JWK:
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
        // Сгенерировать RSA ключ (для разработки/тестирования генерировать заново при запуске)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Такая конфигурация откроет стандартные OAuth2 эндпоинты: `/oauth2/token` для выдачи токенов и `/oauth2/jwks` для JSON Web Key Set. (По умолчанию `AuthorizationServerSettings` Spring маппит `/oauth2/token` и `/oauth2/jwks` ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сервер будет выдавать JWT токены доступа, подписанные RSA ключом выше, и публиковать открытый ключ по адресу `https://<your-app>:/oauth2/jwks`.

**Включение обнаружения OpenID Connect:** Чтобы APIM автоматически получал URL издателя и JWKS, включите endpoint конфигурации OIDC провайдера, добавив `.oidc(Customizer.withDefaults())` в настройку безопасности ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Например:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– включает /.well-known/openid-configuration
```

Это откроет `/.well-known/openid-configuration`, который APIM сможет использовать для метаданных. Наконец, возможно, вы захотите настроить JWT claim **audience**, чтобы проверка APIM по `<audiences>` прошла успешно. Например, добавьте кастомизацию токена:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Установите пользовательскую аудиторию (например, идентификатор клиента или идентификатор API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Это гарантирует, что токены содержат `"aud": ["mcp-client"]`, совпадающее с client ID или ожидаемым по области доступа APIM.

## Открытие эндпоинтов токена и JWKS

После развертывания **URL издателя** вашего приложения будет `https://<app-fqdn>`, например, `https://my-mcp-app.eastus.azurecontainerapps.io`. Его OAuth2 эндпоинты:

- **Эндпоинт токенов:** `https://<app-fqdn>/oauth2/token` – здесь клиенты получают токены (поток client_credentials).
- **Эндпоинт JWKS:** `https://<app-fqdn>/oauth2/jwks` – возвращает набор JWK (используется APIM для получения ключей подписания).
- **OpenID конфигурация:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON для OIDC обнаружения (содержит `issuer`, `token_endpoint`, `jwks_uri` и др.).

APIM будет ссылаться на **URL конфигурации OpenID**, откуда узнает `jwks_uri`. Например, если FQDN вашего Container App — `my-mcp-app.eastus.azurecontainerapps.io`, то в конфигурации APIM `<openid-config url="...">` следует использовать `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (По умолчанию Spring устанавливает `issuer` в этих метаданных равным базовому URL ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Настройка Azure API Management (`validate-jwt`)

В Azure APIM добавьте входящую политику, которая использует `<validate-jwt>`, чтобы проверять входящие JWT на основе вашего Spring Authorization Server. Для простой настройки можно использовать URL метаданных OpenID Connect. Пример сниппета политики:

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

Эта политика инструктирует APIM получить OpenID конфигурацию с Spring Auth Server, загрузить его JWKS и проверить, что каждый токен подписан доверенным ключом и содержит правильную аудиторию. (Если пропустить `<issuers>`, APIM автоматически возьмет значение `issuer` из метаданных.) `<audience>` должен совпадать с вашим client ID или идентификатором ресурса API в токене (в приведенном примере это `"mcp-client"`). Это соответствует документации Microsoft о использовании `validate-jwt` с `<openid-config>` ([Справочник по политике Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

После валидации APIM перенаправит запрос (включая оригинальный заголовок `Authorization`) на бэкенд. Поскольку Spring-приложение также является сервером ресурсов, оно повторно проверит токен, но APIM уже удостоверился в его валидности. (Для разработки можно полагаться на проверку APIM и при желании отключить дополнительные проверки в приложении, однако безопаснее оставить обе.)

## Пример настроек

| Настройка         | Пример значения                                                    | Примечания                                  |
|------------------|-------------------------------------------------------------------|---------------------------------------------|
| **Издатель**      | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL вашего Container App (базовый URI)      |
| **Эндпоинт токена** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`  | Стандартный эндпоинт токена Spring ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Эндпоинт JWKS** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Стандартный эндпоинт JWK Set ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **OpenID конфигурация** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Документ обнаружения OIDC (автогенерируемый) |
| **Аудитория APIM** | `mcp-client`                                                     | OAuth client ID или имя API ресурса          |
| **Политика APIM** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` использует этот URL ([Справочник по политике Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Распространённые ошибки

- **HTTPS/TLS:** шлюз APIM требует, чтобы OpenID/JWKS эндпоинты были доступны по HTTPS и имели действующий сертификат. По умолчанию Azure Container Apps предоставляет доверенный TLS сертификат для домена, управляемого Azure ([Именованные домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Если вы используете пользовательский домен, убедитесь, что сертификат к нему привязан (можно использовать бесплатный управляемый сертификат Azure) ([Именованные домены и бесплатные управляемые сертификаты в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Если APIM не доверяет сертификату эндпоинта, `<validate-jwt>` не сможет получить метаданные.

- **Доступность эндпоинтов:** убедитесь, что эндпоинты Spring приложения доступны из APIM. Использование `--ingress external` (или включение входа в портале) — самый простой вариант. Если выбран внутренний или vNet-ограниченный режим, APIM (по умолчанию публичный) может не получить к ним доступ, если не находится в той же vNet. В тестовой среде предпочтительнее публичный вход, чтобы APIM мог обращаться к `.well-known` и `/jwks`.

- **Включено обнаружение OpenID:** по умолчанию Spring Authorization Server **не открывает** `/.well-known/openid-configuration`, если OIDC не включен. Обязательно добавьте `.oidc(Customizer.withDefaults())` в конфигурацию безопасности (см. выше), чтобы endpoint конфигурации провайдера был активен ([Модель конфигурации :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Иначе вызов APIM `<openid-config>` вернет 404.

- **Claim аудитории:** поведение Spring по умолчанию — устанавливать `aud` равным client ID. Если проверка `<audience>` в APIM не проходит, возможно, потребуется кастомизация токена (как показано выше) или корректировка политики APIM. Убедитесь, что аудитория в JWT совпадает с конфигурацией в `<audience>`.

- **Парсинг JSON метаданных:** JSON OpenID конфигурации должен быть валиден. Стандартная конфигурация Spring выдает типовой OIDC метадокумент. Проверьте наличие правильных значений `issuer` и `jwks_uri`. Если Spring размещен за прокси или маршрутизатором с путевой маршрутизацией, тщательно проверьте URL-адреса в метаданных. APIM использует их без изменений.

- **Порядок политик:** в политике APIM размещайте `<validate-jwt>` **до** любых правил маршрутизации на бэкенд. Иначе запросы могут достигать вашего приложения без валидного токена. Также убедитесь, что `<validate-jwt>` находится сразу под `<inbound>` (а не вложен в другое условие), чтобы APIM применил его.

Следуя этим шагам, вы сможете запустить сервер Spring AI MCP в Azure Container Apps и настроить Azure API Management для проверки входящих OAuth2 JWT с минимальной политикой. Главное — открыть публичный доступ к Spring Auth эндпоинтам с TLS, включить обнаружение OIDC и указать `validate-jwt` в APIM на URL OpenID конфигурации (чтобы JWKS подтягивался автоматически). Эта конфигурация подходит для среды разработки/тестирования; для продакшена учитывайте управление секретами, срок действия токенов и ротацию ключей JWKS по мере необходимости.


**Ссылки:** См. документацию Spring Authorization Server для стандартных конечных точек ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) и настройку OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); см. документацию Microsoft APIM для примеров `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); и документацию Azure Container Apps для развертывания и сертификатов ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->