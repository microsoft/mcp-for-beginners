# Разгръщане на Spring AI MCP приложението в Azure Container Apps

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Фигура: Spring AI MCP сървър, защитен със Spring Authorization Server. Сървърът издава access токени на клиентите и ги валидира при входящи заявки (източник: Spring блог) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* За да разположите Spring MCP сървъра, изградете го като контейнер и използвайте Azure Container Apps с външен ingress. Например, чрез Azure CLI можете да изпълните:

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

Това създава публично достъпно Container App с активиран HTTPS (Azure издава безплатен TLS сертификат за стандартния домейн `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Изходът от командата включва FQDN на приложението (например `my-mcp-app.eastus.azurecontainerapps.io`), който става основа за **issuer URL**. Уверете се, че HTTP ingress е активиран (както е описано по-горе), за да може APIM да достигне приложението. В тестова или дев среда използвайте опцията `--ingress external` (или свържете персонализиран домейн с TLS според [Microsoft документацията](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Съхранявайте чувствителни свойства (като OAuth client secrets) в Container Apps secrets или Azure Key Vault и ги мапирайте в контейнера като променливи на средата.

## Конфигуриране на Spring Authorization Server

В кода на вашето Spring Boot приложение включете стартерите за Spring Authorization Server и Resource Server. Конфигурирайте `RegisteredClient` (за `client_credentials` grant в dev/test) и източник на JWT ключове. Например, в `application.properties` може да зададете:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Активирайте Authorization Server и Resource Server чрез дефиниране на security filter chain. Например:

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

Тази конфигурация ще изложи стандартните OAuth2 крайни точки: `/oauth2/token` за токени и `/oauth2/jwks` за JSON Web Key Set. (По подразбиране Spring `AuthorizationServerSettings` мапва `/oauth2/token` и `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сървърът ще издава JWT access токени, подписани с RSA ключа по-горе, и ще публикува публичния си ключ на `https://<your-app>:/oauth2/jwks`.

**Активиране на OpenID Connect discovery:** За да може APIM автоматично да извлича issuer и JWKS, активирайте OIDC provider configuration endpoint, като добавите `.oidc(Customizer.withDefaults())` в конфигурацията на сигурността ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Например:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Това ще изложи `/.well-known/openid-configuration`, който APIM може да използва за метаданни. Накрая, може да искате да персонализирате JWT claim-а **audience**, така че проверката на APIM `<audiences>` да премине успешно. Например, добавете token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Това гарантира, че токените съдържат `"aud": ["mcp-client"]`, съвпадащо с client ID или scope, очакван от APIM.

## Излагане на Token и JWKS крайни точки

След разгръщане, **issuer URL** на вашето приложение ще бъде `https://<app-fqdn>`, например `https://my-mcp-app.eastus.azurecontainerapps.io`. Неговите OAuth2 крайни точки са:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – тук клиентите получават токени (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – връща JWK набора (използван от APIM за получаване на ключове за подпис).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (съдържа `issuer`, `token_endpoint`, `jwks_uri` и др.).

APIM ще сочи към **OpenID configuration URL**, от който открива `jwks_uri`. Например, ако FQDN на Container App е `my-mcp-app.eastus.azurecontainerapps.io`, тогава `<openid-config url="...">` в APIM трябва да използва `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (По подразбиране Spring задава `issuer` в тези метаданни на същия базов URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Конфигуриране на Azure API Management (`validate-jwt`)

В Azure APIM добавете inbound policy, която използва `<validate-jwt>` за проверка на входящите JWT-та спрямо вашия Spring Authorization Server. За опростена конфигурация можете да използвате OpenID Connect metadata URL. Примерен откъс от политика:

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

Тази политика инструктира APIM да изтегли OpenID конфигурацията от Spring Auth Server, да получи JWKS и да валидира, че всеки токен е подписан с доверен ключ и има правилния audience. (Ако пропуснете `<issuers>`, APIM автоматично ще използва `issuer` claim от метаданните.) `<audience>` трябва да съвпада с client ID или идентификатора на API ресурса в токена (в горния пример зададохме `"mcp-client"`). Това е в съответствие с документацията на Microsoft за използване на `validate-jwt` с `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

След валидирането APIM ще препрати заявката (включително оригиналния `Authorization` хедър) към бекенда. Тъй като Spring приложението също е resource server, то ще повтори проверката на токена, но APIM вече е гарантирал неговата валидност. (За разработка можете да разчитате само на проверката на APIM и да изключите допълнителните проверки в приложението, но е по-безопасно да се поддържат и двете.)

## Примерни настройки

| Настройка          | Примерна стойност                                                   | Бележки                                    |
|--------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | URL на вашето Container App (базов URI)    |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Стандартна Spring token крайна точка ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Стандартна JWK Set крайна точка ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery документ (генериран автоматично)    |
| **APIM audience**  | `mcp-client`                                                       | OAuth client ID или име на API ресурс      |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` използва този URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Чести проблеми

- **HTTPS/TLS:** APIM gateway изисква OpenID/JWKS крайна точка да е HTTPS с валиден сертификат. По подразбиране Azure Container Apps предоставя доверен TLS сертификат за Azure управлявания домейн ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако използвате персонализиран домейн, задължително свържете сертификат (можете да използвате безплатната управлявана функция на Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако APIM не може да се довери на сертификата на крайна точка, `<validate-jwt>` няма да успее да изтегли метаданните.

- **Достъпност на крайни точки:** Уверете се, че крайни точки на Spring приложението са достъпни от APIM. Използването на `--ingress external` (или активиране на ingress през портала) е най-лесно. Ако сте избрали вътрешна или vNet-свързана среда, APIM (който по подразбиране е публичен) може да не достигне приложението, освен ако не е в същия VNet. В тестова среда предпочитайте публичен ingress, за да може APIM да извиква `.well-known` и `/jwks` URL адресите.

- **Активиране на OpenID Discovery:** По подразбиране Spring Authorization Server **не излага** `/.well-known/openid-configuration`, освен ако OIDC не е активиран. Уверете се, че сте включили `.oidc(Customizer.withDefaults())` в конфигурацията на сигурността (виж по-горе), за да е активна крайна точка за конфигурация на доставчика ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). В противен случай APIM заявката към `<openid-config>` ще върне 404.

- **Audience Claim:** По подразбиране Spring задава `aud` claim на client ID. Ако проверката на APIM `<audience>` не преминава, може да се наложи да персонализирате токена (както е показано по-горе) или да коригирате APIM политиката. Уверете се, че audience в JWT съвпада с конфигурацията в `<audience>`.

- **Парсване на JSON метаданни:** OpenID конфигурационният JSON трябва да е валиден. По подразбиране Spring издава стандартен OIDC metadata документ. Проверете дали съдържа правилните `issuer` и `jwks_uri`. Ако хоствате Spring зад прокси или с път-базирано маршрутизиране, проверете URL адресите в тези метаданни. APIM ще използва тези стойности без промяна.

- **Подредба на политиките:** В APIM политиката поставете `<validate-jwt>` **преди** всякакво маршрутизиране към бекенда. В противен случай заявките може да достигнат приложението без валиден токен. Също така се уверете, че `<validate-jwt>` е директно под `<inbound>` (не е вложен в друга условна конструкция), за да бъде приложен от APIM.

Следвайки горните стъпки, можете да стартирате вашия Spring AI MCP сървър в Azure Container Apps и да накарате Azure API Management да валидира входящите OAuth2 JWT-та с минимална политика. Ключовите моменти са: изложете Spring Auth крайни точки публично с TLS, активирайте OIDC discovery и насочете `validate-jwt` на APIM към OpenID конфигурационния URL (за автоматично изтегляне на JWKS). Тази конфигурация е подходяща за dev/test среда; за продукция обмислете правилно управление на тайни, срокове на токените и ротация на ключове в JWKS при необходимост.
**References:** Вижте документацията на Spring Authorization Server за стандартните крайни точки ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) и конфигурацията на OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); вижте документацията на Microsoft APIM за примери с `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); и документацията на Azure Container Apps за разгръщане и сертификати ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.