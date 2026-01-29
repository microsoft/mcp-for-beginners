# Деплојмент Spring AI MCP апликације на Azure Container Apps

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Слика: Spring AI MCP сервер заштићен Spring Authorization Server-ом. Сервер издаје приступне токене клијентима и верификује их приликом долазних захтева (извор: Spring блог) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Да бисте деплојовали Spring MCP сервер, направите га као контејнер и користите Azure Container Apps са спољним приступом. На пример, помоћу Azure CLI можете покренути:

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

Ово креира јавну Container App са омогућеним HTTPS-ом (Azure издаје бесплатан TLS сертификат за подразумевани `*.azurecontainerapps.io` домен ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Излаз команде садржи FQDN апликације (нпр. `my-mcp-app.eastus.azurecontainerapps.io`), који постаје основа за **issuer URL**. Обавезно омогућите HTTP приступ (као горе) како би APIM могао да приступи апликацији. У тест/развојном окружењу користите опцију `--ingress external` (или повежите прилагођени домен са TLS-ом према [Microsoft документацији](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Чувате осетљиве податке (као што су OAuth client secrets) у Container Apps secrets или Azure Key Vault и мапирате их у контејнер као променљиве окружења.

## Конфигурисање Spring Authorization Server-а

У коду ваше Spring Boot апликације укључите Spring Authorization Server и Resource Server стартере. Конфигуришите `RegisteredClient` (за `client_credentials` grant у развоју/тесту) и извор JWT кључа. На пример, у `application.properties` можете поставити:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Омогућите Authorization Server и Resource Server дефинисањем security filter chain. На пример:

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

Ова конфигурација ће изложити подразумеване OAuth2 крајње тачке: `/oauth2/token` за токене и `/oauth2/jwks` за JSON Web Key Set. (Подразумевано, Spring-ов `AuthorizationServerSettings` мапира `/oauth2/token` и `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сервер ће издавати JWT приступне токене потписане RSA кључем наведеним горе и објављивати свој јавни кључ на `https://<your-app>:/oauth2/jwks`.

**Омогућите OpenID Connect откривање:** Да би APIM аутоматски преузимао issuer и JWKS, омогућите OIDC provider configuration endpoint додавањем `.oidc(Customizer.withDefaults())` у вашу security конфигурацију ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). На пример:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Ово изложи `/.well-known/openid-configuration`, који APIM може користити за метаподатке. На крају, можда ћете желети да прилагодите JWT **audience** claim како би APIM-ова провера `<audiences>` прошла. На пример, додајте token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ово осигурава да токени носе `"aud": ["mcp-client"]`, што одговара client ID-ју или scope-у који APIM очекује.

## Излагање Token и JWKS крајњих тачака

Након деплоја, **issuer URL** ваше апликације биће `https://<app-fqdn>`, нпр. `https://my-mcp-app.eastus.azurecontainerapps.io`. Њене OAuth2 крајње тачке су:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – клијенти овде добијају токене (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – враћа JWK сет (који APIM користи за добијање кључева за потписивање).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC откривачки JSON (садржи `issuer`, `token_endpoint`, `jwks_uri` итд.).

APIM ће користити **OpenID configuration URL** са ког ће открити `jwks_uri`. На пример, ако је FQDN ваше Container App `my-mcp-app.eastus.azurecontainerapps.io`, онда APIM-ов `<openid-config url="...">` треба да користи `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Подразумевано, Spring ће у тим метаподацима поставити `issuer` на исти базни URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Конфигурисање Azure API Management-а (`validate-jwt`)

У Azure APIM додајте inbound политику која користи `<validate-jwt>` за проверу долазних JWT-ова према вашем Spring Authorization Server-у. За једноставну конфигурацију можете користити OpenID Connect metadata URL. Пример исечка политике:

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

Ова политика каже APIM-у да преузме OpenID конфигурацију са Spring Auth Server-а, добије његов JWKS и провери да је сваки токен потписан поузданим кључем и да има исправан audience. (Ако изоставите `<issuers>`, APIM ће аутоматски користити `issuer` claim из метаподатака.) `<audience>` треба да одговара вашем client ID-ју или идентификатору API ресурса у токену (у горњем примеру постављено је на `"mcp-client"`). Ово је у складу са Microsoft документацијом о коришћењу `validate-jwt` са `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Након валидације, APIM ће проследити захтев (укључујући оригинални `Authorization` хедер) ка backend-у. Пошто је Spring апликација такође resource server, она ће поново проверити токен, али APIM је већ потврдио његову валидност. (За развој можете се ослонити на проверу APIM-а и онемогућити додатне провере у апликацији ако желите, али је безбедније задржати обе.)

## Пример подешавања

| Подешавање        | Пример вредности                                                    | Напомене                                   |
|-------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | URL ваше Container App апликације (базни URI) |
| **Token endpoint**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Подразумевана Spring token крајња тачка ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Подразумевана JWK Set крајња тачка ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC откривачки документ (аутоматски генерисан) |
| **APIM audience** | `mcp-client`                                                       | OAuth client ID или име API ресурса        |
| **APIM policy**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` користи овај URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Чести проблеми

- **HTTPS/TLS:** APIM gateway захтева да OpenID/JWKS крајње тачке буду HTTPS са важећим сертификатом. Подразумевано, Azure Container Apps обезбеђује поуздан TLS сертификат за Azure-managed домен ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако користите прилагођени домен, обавезно повежите сертификат (можете користити Azure-ову бесплатну managed cert опцију) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако APIM не може да верује сертификату крајње тачке, `<validate-jwt>` неће моћи да преузме метаподатке.

- **Доступност крајњих тачака:** Обезбедите да су крајње тачке Spring апликације доступне са APIM-а. Коришћење `--ingress external` (или омогућавање приступа у порталу) је најједноставније. Ако сте изабрали интерно или vNet окружење, APIM (који је по подразумеваној вредности јавни) можда неће моћи да приступи осим ако није у истом VNet-у. У тест окружењу препоручује се јавни приступ како би APIM могао да позове `.well-known` и `/jwks` URL-ове.

- **Омогућено OpenID откривање:** Подразумевано, Spring Authorization Server **не излаже** `/.well-known/openid-configuration` ако OIDC није омогућен. Обавезно укључите `.oidc(Customizer.withDefaults())` у security конфигурацију (погледајте горе) да би provider configuration endpoint био активан ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). У супротном, APIM-ов позив `<openid-config>` ће вратити 404.

- **Audience claim:** Подразумевано понашање Spring-а је да постави `aud` claim на client ID. Ако APIM-ова провера `<audience>` не прође, можда ћете морати да прилагодите токен (као што је приказано горе) или да измените APIM политику. Обавезно да `audience` у вашем JWT одговара ономе што конфигуришете у `<audience>`.

- **Парсирање JSON метаподатака:** OpenID конфигурациони JSON мора бити валидан. Подразумевана Spring конфигурација ће генерисати стандардни OIDC метаподаци документ. Проверите да садржи исправан `issuer` и `jwks_uri`. Ако хостујете Spring иза проксија или са рутом заснованом на путањи, детаљно проверите URL-ове у овим метаподацима. APIM ће користити ове вредности онако како јесу.

- **Редослед политика:** У APIM политици, `<validate-jwt>` поставите **пре** било каквог рутирања ка backend-у. У супротном, позиви могу стићи до апликације без валиданог токена. Такође, уверите се да `<validate-jwt>` стоји одмах испод `<inbound>` (не унутар другог услова) како би APIM могао да га примени.

Пратећи ове кораке, можете покренути ваш Spring AI MCP сервер у Azure Container Apps и омогућити Azure API Management да верификује долазне OAuth2 JWT токене уз минималну политику. Кључне ствари су: изложити Spring Auth крајње тачке јавно са TLS-ом, омогућити OIDC откривање и усмерити APIM-ов `validate-jwt` на OpenID конфигурациони URL (да аутоматски преузме JWKS). Ова конфигурација је погодна за развојно/тест окружење; за продукцију размислите о правилном управљању тајнама, времену трајања токена и ротацији кључева у JWKS по потреби.
**References:** Погледајте документацију Spring Authorization Server за подразумеване крајње тачке ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) и OIDC конфигурацију ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); погледајте Microsoft APIM документацију за примере `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); и Azure Container Apps документацију за деплој и сертификате ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.