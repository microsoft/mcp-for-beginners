# Разгръщане на Spring AI MCP приложението в Azure Container Apps

> [!WARNING]
> Този комбиниран сървър за удостоверяване/ресурси е предназначен за учебна и
> разработка/тестова употреба. Продукционните системи трябва да използват отделен доставчик на идентичност,
> постоянни ключове за подписване и учетни данни, съхранявани в управляван хранилище за тайни.

 ([Защитаване на Spring AI MCP сървъри с OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Фигура: Spring AI MCP сървър защитен със Spring Authorization Server. Сървърът издава токени за достъп на клиентите и ги валидира при входящи заявки (източник: Spring блог) ([Защитаване на Spring AI MCP сървъри с OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* За да разположите Spring MCP сървъра, изградете го като контейнер и използвайте Azure Container Apps с външен вход. Например, използвайки Azure CLI можете да изпълните:

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

Това създава публично достъпно контейнерно приложение с активиран HTTPS (Azure издава безплатен TLS сертификат за домейн по подразбиране `*.azurecontainerapps.io` ([Потребителски домейни и безплатни управлявани сертификати в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Резултатът от командата включва пълния домейн на приложението (например `my-mcp-app.eastus.azurecontainerapps.io`), който става основната **issuer URL**. Уверете се, че HTTP входът е разрешен (както е описано по-горе), за да може APIM да осъществи връзка с приложението. При тестова/разработваща среда използвайте опцията `--ingress external` (или свържете потребителски домейн с TLS според [документацията на Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Потребителски домейни и безплатни управлявани сертификати в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Съхранявайте всички чувствителни свойства (като OAuth client тайни) в секретите на Container Apps или Azure Key Vault и ги картографирайте в контейнера като променливи на средата.

## Конфигуриране на Spring Authorization Server

В кода на вашето Spring Boot приложение, включете стартери за Spring Authorization Server и Resource Server. Конфигурирайте `RegisteredClient` (за гранта `client_credentials` в dev/test) и източник на JWT ключове. Например, в `application.properties` можете да зададете:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Активирайте Authorization Server и Resource Server като дефинирате security filter chain. Например:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Активиране на крайните точки на Сървъра за удостоверяване
            .apply(authzServer.and())
            // Активиране на Сървъра за ресурси (валидиране на JWT при входящи заявки)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Забраняване на CSRF (MCP сървърът не е базиран на браузър)
            .csrf(csrf -> csrf.disable())
            // Позволяване на CORS за клиентски демонстрационни инструменти
            .cors(withDefaults());
        return http.build();
    }

    // Дефиниране на клиент в паметта (RegisteredClient) и източник на JWK:
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
        // Генериране на RSA ключ (за разработка/тест, генерирането става наново при стартиране)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Тази конфигурация ще изложи стандартните OAuth2 крайни точки: `/oauth2/token` за токени и `/oauth2/jwks` за JSON Web Key Set. (По подразбиране `AuthorizationServerSettings` на Spring свързва `/oauth2/token` и `/oauth2/jwks` ([Конфигурационен модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сървърът ще издава JWT токени подписани с горния RSA ключ и ще публикува публичния си ключ на адрес `https://<your-app>:/oauth2/jwks`.

**Активиране на OpenID Connect откриване:** За да позволите на APIM автоматично да извлича issuer-а и JWKS, активирайте OIDC конфигурационната крайна точка, като добавите `.oidc(Customizer.withDefaults())` във вашата сигурностна конфигурация ([Конфигурационен модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Например:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– активира /.well-known/openid-configuration
```

Това прави достъпна `/.well-known/openid-configuration`, която APIM може да използва за метаданни. Накрая, може да искате да персонализирате JWT **audience** claim така, че проверката `<audiences>` на APIM да премине. Например, добавете token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Задайте персонализирана аудитория (напр. клиентски идентификатор или API идентификатор)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Това гарантира токените да съдържат `"aud": ["mcp-client"]`, съвпадащ с клиентския ID или очаквания scope на APIM.

## Излагане на Token и JWKS крайни точки

След разгръщане, **issuer URL** на вашето приложение ще бъде `https://<app-fqdn>`, например `https://my-mcp-app.eastus.azurecontainerapps.io`. Неговите OAuth2 крайни точки са:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – тук клиентите получават токени (client_credentials поток).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – връща JWK комплекта (използван от APIM за получаване на подписващи ключове).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON за откриване на OIDC (съдържа `issuer`, `token_endpoint`, `jwks_uri` и др.).

APIM ще сочи към **OpenID configuration URL**, от което ще открие `jwks_uri`. Например, ако FQDN на Container App е `my-mcp-app.eastus.azurecontainerapps.io`, `<openid-config url="...">` на APIM трябва да използва `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (По подразбиране Spring задава `issuer` в тези метаданни като същия основен URL ([Конфигурационен модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Конфигуриране на Azure API Management (`validate-jwt`)

В Azure APIM добавете inbound policy, която използва `<validate-jwt>` политиката за проверка на входящи JWT-та спрямо вашия Spring Authorization Server. За проста настройка може да използвате OpenID Connect метаданните. Примерен откъс от политика:

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

Тази политика казва на APIM да вземе OpenID конфигурацията от Spring Auth Server, да извлече неговия JWKS и да валидира, че всеки токен е подписан с доверен ключ и има правилния audience. (Ако пропуснете `<issuers>`, APIM автоматично ще използва `issuer` claim-а от метаданните.) `<audience>` трябва да съвпада с вашия клиентски ID или API ресурсен идентификатор в токена (в примера по-горе зададохме `"mcp-client"`). Това съответства на документацията на Microsoft за използване на `validate-jwt` с `<openid-config>` ([Политика на Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

След валидирането, APIM ще препрати заявката (включително оригиналния `Authorization` хедър) към бекенда. Тъй като Spring приложението също е ресурсен сървър, то ще пре-валидира токена, но APIM вече е гарантирал неговата валидност. (За разработка можете да разчитате само на проверката на APIM и да изключите допълнителни проверки в приложението, ако желаете, но по-безопасно е да ги запазите и двете.)

## Примерни настройки

| Настройка          | Примерна стойност                                                   | Бележки                                     |
|--------------------|----------------------------------------------------------------------|---------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                   | URL на вашето контейнерно приложение (основен URI) |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`      | По подразбиране OAuth2 token крайна точка на Spring ([Конфигурационен модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`       | По подразбиране JWK Set крайна точка ([Конфигурационен модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))     |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Документ за откриване на OIDC (генериран автоматично)  |
| **APIM audience**  | `mcp-client`                                                        | OAuth клиентски ID или име на API ресурс    |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` използва този URL ([Политика на Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Чести проблеми

- **HTTPS/TLS:** APIM шлюз изисква OpenID/JWKS крайната точка да е HTTPS с валиден сертификат. По подразбиране Azure Container Apps осигурява доверен TLS сертификат за управлявания от Azure домейн ([Потребителски домейни и безплатни управлявани сертификати в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако използвате персонализиран домейн, уверете се, че сте свързали сертификат (можете да използвате безплатния управляван сертификат на Azure) ([Потребителски домейни и безплатни управлявани сертификати в Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако APIM не може да се довери на сертификата на крайната точка, `<validate-jwt>` ще се провали при взимането на метаданните.

- **Достъпност на крайните точки:** Уверете се, че крайните точки на Spring приложението са достъпни от APIM. Използването на `--ingress external` (или активиране на вход в портала) е най-простият вариант. Ако сте избрали вътрешна или vNet-зависима среда, APIM (публичен по подразбиране) може да няма достъп до нея, освен ако не е в същия VNet. При тестова конфигурация предпочитайте публичен вход, за да може APIM да извика `.well-known` и `/jwks` URL адресите.

- **Активиране на OpenID откриване:** По подразбиране Spring Authorization Server **не излага** `/.well-known/openid-configuration`, освен ако OIDC не е активиран. Уверете се, че сте включили `.oidc(Customizer.withDefaults())` в конфигурацията за сигурност (виж по-горе), за да бъде активна крайна точка за конфигурация на доставчика ([Конфигурационен модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). В противен случай повикването на `<openid-config>` от APIM ще върне 404.

- **Audience Claim:** По подразбиране Spring задава `aud` claim-а като клиентски ID. Ако проверката на `<audience>` в APIM се провали, може да се наложи да персонализирате токена (както е показано по-горе) или да коригирате APIM политиката. Уверете се, че audience в JWT съвпада с това, което конфигурирате в `<audience>`.

- **Парсване на JSON метаданни:** OpenID конфигурационният JSON трябва да е валиден. По подразбиране Spring ще издаде стандартен OIDC метаданен документ. Проверете дали съдържа правилния `issuer` и `jwks_uri`. Ако хоствате Spring зад прокси или по пътен маршрут, проверете повторно URL адресите в тези метаданни. APIM ще ги използва директно.

- **Подредба на политика:** В APIM политиката поставете `<validate-jwt>` **преди** всяко маршрутизиране към бекенда. В противен случай заявките може да достигнат приложението без валиден токен. Също така се уверете, че `<validate-jwt>` е веднага под `<inbound>` (не вложено в условие), така че APIM да го приложи.

Следвайки горните стъпки, можете да изпълните вашия Spring AI MCP сървър в Azure Container Apps и да накарате Azure API Management да валидира входящите OAuth2 JWT-та с минимална политика. Ключовите моменти са: излагайте публично Spring Auth крайните точки с TLS, активирайте OIDC откриването и насочете `validate-jwt` на APIM към OpenID конфигурационния URL (за да можем автоматично да вземе JWKS). Тази конфигурация е подходяща за dev/test среда; за продукция обмислете правилното управление на тайните, времетраенето на токена и ротиране на ключове в JWKS при нужда.


**Препратки:** Вижте документацията на Spring Authorization Server за подразбиращи се крайни точки ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) и OIDC конфигурация ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); вижте документацията на Microsoft APIM за примери с `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); и документацията на Azure Container Apps за разгръщане и сертификати ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->